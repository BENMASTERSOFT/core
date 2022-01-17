from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, HttpResponseRedirect
from cooperative.models import *
from django.contrib import messages
from django.urls import reverse
from cooperative.forms import *
from django.db.models import Q
from django.db.models import Count, Sum
from datetime import datetime
from datetime import date
import datetime
from django.db.models import  F, CharField, Value as V
from django.db.models.functions import Concat
from cooperative.resources import NorminalRollResource, AccountDeductionsResource
from tablib import Dataset
from django.template import defaultfilters
from django.contrib import messages
from django.utils.dateparse import parse_date
from dateutil.relativedelta import relativedelta
import xlwt

now = datetime.datetime.now()

  
def secretary_home(request):
	title="Secretary"
	context={
	'title':title,
	}
	return render(request, "secretary_templates/dashboard.html",context)


def basic_form(request):
	return render(request, 'secretary_templates/basics/basic_form1.html')


def basic_table(request):
	return render(request, 'secretary_templates/basics/basic_tables.html')

def datatable_table(request):
	return render(request, 'secretary_templates/basics/datatable.html')


def membership_request_certification_list_load(request):
	submission_status=SubmissionStatus.objects.get(title='SUBMITTED')
	certification_status=CertificationStatus.objects.get(title='PENDING')

	transaction=CertifiableTransactions.objects.get(transaction__code='100')  
	certification_officer = CertificationOfficers.objects.get(transaction=transaction,officer_id=request.user.id)  
	
	applicants=MemberShipRequest.objects.filter(submission_status=submission_status,certification_officer=certification_officer,certification_status=certification_status)
	context={
	'applicants':applicants,
	}
	return render(request,'secretary_templates/membership_request_certification_list_load.html',context)


def membership_request_certification_info(request,pk):
	applicant=MemberShipRequest.objects.get(id=pk)
	officer=CustomUser.objects.get(id=request.user.id)

	comment_form =MemberShipRequestAdditionalInfo_form(request.POST or None)
	attachment_form =MemberShipRequestAdditionalAttachment_form(request.POST or None)

	records= MemberShipRequestAdditionalInfo.objects.filter(applicant_id=pk,officer_id=officer)
	attachments=MemberShipRequestAdditionalAttachment.objects.filter(officer=officer,applicant=applicant)

	existing_infos = MemberShipRequestAdditionalInfo.objects.filter(applicant_id=pk).exclude(officer=officer)
	existing_attachments = MemberShipRequestAdditionalAttachment.objects.filter(applicant_id=pk).exclude(officer=officer)


	if MemberShipRequestAdditionalInfo.objects.filter(officer=officer,applicant=applicant).exists():	
		comment_form.fields['comment'].initial=records[0].comment

	context={
	'comment_form':comment_form,
	'attachment_form':attachment_form,
	'pk':pk,
	'existing_infos':existing_infos,
	'existing_attachments':existing_attachments,
	'records':records,
	'attachments':attachments,
	}
	return render(request,'secretary_templates/membership_request_certification_info.html',context)


def membership_request_certification_additional_info_save(request,pk):
	applicant=MemberShipRequest.objects.get(id=pk)
	officer=CustomUser.objects.get(id=request.user.id)

	comment = request.POST.get('comment')
	if MemberShipRequestAdditionalInfo.objects.filter(officer=officer,applicant=applicant).exists():
		record=MemberShipRequestAdditionalInfo.objects.filter(officer=officer,applicant=applicant).first()
		record.comment=comment
		record.save()
		messages.success(request,"Record Updated Successfully")
		return HttpResponseRedirect(reverse('membership_request_certification_info',args=(pk,)))

	record=MemberShipRequestAdditionalInfo(comment=comment,officer=officer,applicant=applicant)
	record.save()
	messages.success(request,"Record Added Successfully")
	return HttpResponseRedirect(reverse('membership_request_certification_info',args=(pk,)))


def membership_request_certification_additional_info_delete(request,pk,return_pk):
	record=MemberShipRequestAdditionalInfo.objects.get(id=pk)
	record.delete()
	return HttpResponseRedirect(reverse('membership_request_certification_info',args=(return_pk,)))



def MemberShipRequestAdditionalAttachment_certification_save(request,pk):
	applicant=MemberShipRequest.objects.get(id=pk)
	officer=CustomUser.objects.get(id=request.user.id)

	if request.FILES.get('image', False):
		image = request.FILES['image']
		fs=FileSystemStorage()
		filename=fs.save(image.name,image)
		image_url=fs.url(filename)
	
	else:
		image_url=None
	
	caption=request.POST.get('caption')

	if MemberShipRequestAdditionalAttachment.objects.filter(officer=officer,applicant=applicant,caption=caption).exists():
		member= MemberShipRequestAdditionalAttachment.objects.get(officer=officer,applicant=applicant,caption=caption) 
		member.image=image_url
		member.save()
		messages.success(request,"Successfully Updated Record")
		return HttpResponseRedirect(reverse('membership_request_certification_info',args=(pk,)))

	member=MemberShipRequestAdditionalAttachment(image=image_url,officer=officer,applicant=applicant,caption=caption)      
	member.save()
	messages.success(request,"Successfully Added Record")
	return HttpResponseRedirect(reverse('membership_request_certification_info',args=(pk,)))


def MemberShipRequestAdditionalAttachment_certification_delete(request,pk,return_pk):
	record=MemberShipRequestAdditionalAttachment.objects.get(id=pk)
	record.delete()
	return HttpResponseRedirect(reverse('membership_request_certification_info',args=(return_pk,)))


def MemberShipRequest_certification_submit(request,pk):
	form=MemberShipRequest_certification_submit_form(request.POST or None)
	
	if request.method=="POST":
		certification_status_id=request.POST.get('certication_status')
		certification_status=CertificationStatus.objects.get(id=certification_status_id)

		record = MemberShipRequest.objects.get(id=pk)
		approval_officer_id = request.POST.get('approval_officers')
		approval_officer=ApprovalOfficers.objects.get(id=approval_officer_id)

		record.approval_officer=approval_officer
		record.certification_status=certification_status
		record.certified_date=datetime.date.today()
		record.save()
		return HttpResponseRedirect(reverse('membership_request_certification_list_load'))
	context={
	'form':form,
	}
	return render(request,'secretary_templates/MemberShipRequest_certification_submit.html',context)


def Loan_request_certification_list_load(request):
	current_user=CustomUser.objects.get(id=request.user.id)
	submission_status=SubmissionStatus.objects.get(title="SUBMITTED")
	certification_status=CertificationStatus.objects.get(title="PENDING")
	applicants=LoanRequest.objects.filter(certification_officer__officer_id=current_user,submission_status=submission_status,certification_status=certification_status)
	
	context={
	'applicants':applicants

	}
	return render(request,'secretary_templates/Loan_request_certification_list_load.html',context)


def Loan_request_certification_details(request,pk):
	loan_comment=LoanRequest.objects.get(id=pk)
	loan_analysis=LoanRequestSettings.objects.filter(applicant_id=pk,category='ANALYSIS')
	loan_summary=LoanRequestSettings.objects.filter(applicant_id=pk,category='SUMMARY')
	

	certification_status=CertificationStatus.objects.all()
	approval_officers=ApprovalOfficers.objects.filter(transaction__transaction_id=loan_comment.loan.id)


	if request.method=='POST':

		comment=request.POST.get('comment')
		officer_id=request.POST.get('officer')
		officer=ApprovalOfficers.objects.get(id=officer_id)

		status_id=request.POST.get('status')
		status=CertificationStatus.objects.get(id=status_id)

		certified_date= datetime.datetime.now()


		loan_comment.certification_status=status
		loan_comment.certification_comment=comment
		loan_comment.certification_date=certified_date
		loan_comment.approval_officer=officer
		loan_comment.save()
	
		return HttpResponseRedirect(reverse('Loan_request_certification_list_load'))

	context={
	'loan_analysis':loan_analysis,
	'loan_summary':loan_summary,
	'pk':pk,
	'loan_comment':loan_comment,
	'approval_officers':approval_officers,
	'certification_status':certification_status,
	}
	return render(request,'secretary_templates/Loan_request_certification_details.html',context)



def Loan_application_certification_list_load(request):
	current_user=CustomUser.objects.get(id=request.user.id)
	submission_status=SubmissionStatus.objects.get(title="SUBMITTED")
	certification_status=CertificationStatus.objects.get(title="PENDING")
	applicants=LoanApplication.objects.filter(certification_officer__officer_id=current_user,submission_status=submission_status,certification_status=certification_status)
	
	context={
	'applicants':applicants

	}
	return render(request,'secretary_templates/Loan_application_certification_list_load.html',context)


def Loan_application_certification_details(request,pk):
	loan_comment=LoanApplication.objects.get(id=pk)
	loan_analysis=LoanApplicationSettings.objects.filter(applicant_id=pk,category='ANALYSIS')
	loan_summary=LoanApplicationSettings.objects.filter(applicant_id=pk,category='SUMMARY')
	

	certification_status=CertificationStatus.objects.all()
	approval_officers=ApprovalOfficers.objects.filter(transaction__transaction_id=loan_comment.applicant.applicant.loan.id)


	if request.method=='POST':

		comment=request.POST.get('comment')
		officer_id=request.POST.get('officer')
		officer=ApprovalOfficers.objects.get(id=officer_id)

		status_id=request.POST.get('status')
		status=CertificationStatus.objects.get(id=status_id)

		certified_date= datetime.datetime.now()


		loan_comment.certification_status=status
		loan_comment.certification_comment=comment
		loan_comment.certification_date=certified_date
		loan_comment.approval_officer=officer
		loan_comment.save()
	
		return HttpResponseRedirect(reverse('Loan_application_certification_list_load'))

	context={
	'loan_analysis':loan_analysis,
	'loan_summary':loan_summary,
	'pk':pk,
	'loan_comment':loan_comment,
	'approval_officers':approval_officers,
	'certification_status':certification_status,
	}
	return render(request,'secretary_templates/Loan_application_certification_details.html',context)

