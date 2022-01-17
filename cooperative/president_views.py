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
current_date = datetime.date.today()
	

  
def president_home(request):
	title="President"
	context={
	'title':title,
	}
	return render(request, "president_templates/dashboard.html",context)


def basic_form(request):
	return render(request, 'president_templates/basics/basic_form1.html')


def basic_table(request):
	return render(request, 'president_templates/basics/basic_tables.html')

def datatable_table(request):
	return render(request, 'president_templates/basics/datatable.html')


def membership_request_approvals_list_load(request):
	submission_status=SubmissionStatus.objects.get(title='SUBMITTED')
	certification_status=CertificationStatus.objects.get(title='PENDING')
	approval_status=ApprovalStatus.objects.get(title='PENDING')

	transaction=ApprovableTransactions.objects.get(transaction__code='100')  
	approval_officer = ApprovalOfficers.objects.get(transaction=transaction,officer_id=request.user.id)  
	applicants=MemberShipRequest.objects.filter(approval_officer=approval_officer,submission_status=submission_status,approval_status=approval_status).exclude(certification_status=certification_status)
	context={
	'applicants':applicants,
	}
	return render(request,'president_templates/membership_request_approvals_list_load.html',context)


def membership_request_approval_info(request,pk):
	form_comment=MemberShipRequest_approval_comment_form(request.POST or None)
	form_attachment=MemberShipRequest_approval_attachment_form(request.POST or None)
	applicant=MemberShipRequest.objects.get(id=pk)
	officer=CustomUser.objects.get(id=request.user.id)

	existing_infos = MemberShipRequestAdditionalInfo.objects.filter(applicant_id=pk).exclude(officer=officer)
	existing_attachments = MemberShipRequestAdditionalAttachment.objects.filter(applicant_id=pk).exclude(officer=officer)
	approval_comments = MemberShipRequestAdditionalInfo.objects.filter(applicant_id=pk,officer=officer)
	approval_attachments = MemberShipRequestAdditionalAttachment.objects.filter(applicant_id=pk,officer=officer)

	
	context={
	'form_comment':form_comment,
	'form_attachment':form_attachment,
	'pk':pk,
	'existing_infos':existing_infos,
	'existing_attachments':existing_attachments,
	'approval_comments':approval_comments,
	'approval_attachments':approval_attachments,
	}
	return render(request,'president_templates/membership_request_approval_info.html',context)


def membership_request_approval_info_delete(request,pk):
	record= MemberShipRequestAdditionalInfo.objects.get(id=pk)
	return_pk=record.applicant_id
	record.delete()
	return HttpResponseRedirect(reverse('membership_request_approval_info',args=(return_pk,)))


def membership_request_approval_comment_save(request,pk):
	applicant=MemberShipRequest.objects.get(id=pk)
	officer=CustomUser.objects.get(id=request.user.id)
	if request.method=="POST" and 'btn_info' in request.POST:
		comment=request.POST.get('comment')
	
		record=MemberShipRequestAdditionalInfo(applicant=applicant,comment=comment,officer=officer)
		record.save()
		return HttpResponseRedirect(reverse('membership_request_approval_info',args=(pk,)))



def membership_request_approval_attachment_save(request,pk):
	applicant=MemberShipRequest.objects.get(id=pk)
	officer=CustomUser.objects.get(id=request.user.id)

	if request.method=="POST" and 'btn_attachment' in request.POST:
		attachment_form=MemberShipRequest_approval_attachment_form(request.POST)
		caption=request.POST.get('caption')
		
		
		if request.FILES.get('image', False):
			image = request.FILES['image']
			fs=FileSystemStorage()
			filename=fs.save(image.name,image)
			image_url=fs.url(filename)
	
		else:
			image_url=None

		record=MemberShipRequestAdditionalAttachment(image=image_url,applicant=applicant,caption=caption,officer=officer)
		record.save()
		return HttpResponseRedirect(reverse('membership_request_approval_info',args=(pk,)))


def membership_request_approval_attachment_delete(request,pk):
	record= MemberShipRequestAdditionalAttachment.objects.get(id=pk)
	return_pk=record.applicant_id
	record.delete()
	return HttpResponseRedirect(reverse('membership_request_approval_info',args=(return_pk,)))



def MemberShipRequest_approval_submit(request,pk):
	form=MemberShipRequest_approval_submit_form(request.POST or None)
	
	if request.method=="POST":
		approval_status_id=request.POST.get('approval_status')
		approval_status=ApprovalStatus.objects.get(id=approval_status_id)

		record = MemberShipRequest.objects.get(id=pk)
		
		record.approval_status=approval_status
		record.approved_date=datetime.date.today()
		record.save()
		return HttpResponseRedirect(reverse('membership_request_approvals_list_load'))
	context={
	'form':form,
	}
	return render(request,'president_templates/MemberShipRequest_approval_submit.html',context)


def loan_request_approval_list_load(request):
	certification_status=CertificationStatus.objects.get(title='CERTIFIED')
	approval_status=ApprovalStatus.objects.get(title='PENDING')
	current_user=CustomUser.objects.get(id=request.user.id)
	applicants=LoanRequest.objects.filter(approval_status=approval_status,certification_status=certification_status,approval_officer__officer_id=current_user)

	context={
	'applicants':applicants,
	}
	return render(request,'president_templates/loan_request_approval_list_load.html',context)


def Loan_request_approval_details(request,pk):
	loan_comment=LoanRequest.objects.get(id=pk)
	loan_analysis=LoanRequestSettings.objects.filter(applicant_id=pk,category='ANALYSIS')
	loan_summary=LoanRequestSettings.objects.filter(applicant_id=pk,category='SUMMARY')
	

	approval_status=ApprovalStatus.objects.all()
	


	if request.method=='POST':

		comment=request.POST.get('comment')
		approved_amount=request.POST.get('amount')

		if float(approved_amount)<=0:
			messages.info(request,"Amount approved cannot be less than or equal to Zero(0)")
			return HttpResponseRedirect(reverse('Loan_request_approval_details', args=(pk,)))
		
		if float(loan_comment.loan_amount) < float(approved_amount):
			messages.info(request,"Amount approved cannot be more than applied Amount")
			return HttpResponseRedirect(reverse('Loan_request_approval_details', args=(pk,)))

		status_id=request.POST.get('status')
		status=ApprovalStatus.objects.get(id=status_id)

		approved_date= datetime.datetime.now()


		loan_comment.approval_status=status
		loan_comment.approval_comment=comment
		loan_comment.approval_date=approved_date
		loan_comment.approved_amount=approved_amount
		loan_comment.save()
	
		return HttpResponseRedirect(reverse('loan_request_approval_list_load'))

	context={
	'loan_analysis':loan_analysis,
	'loan_summary':loan_summary,
	'pk':pk,
	'loan_comment':loan_comment,
	'approval_status':approval_status,
	}
	return render(request,'president_templates/Loan_request_approval_details.html',context)


def loan_application_approval_list_load(request):
	certification_status=CertificationStatus.objects.get(title='CERTIFIED')
	approval_status=ApprovalStatus.objects.get(title='PENDING')
	current_user=CustomUser.objects.get(id=request.user.id)
	applicants=LoanApplication.objects.filter(approval_status=approval_status,certification_status=certification_status,approval_officer__officer_id=current_user)

	context={
	'applicants':applicants,
	}
	return render(request,'president_templates/loan_application_approval_list_load.html',context)

def Loan_application_approval_details(request,pk):
	loan_comment=LoanApplication.objects.get(id=pk)
	loan_analysis=LoanApplicationSettings.objects.filter(applicant_id=pk,category='ANALYSIS')
	loan_summary=LoanApplicationSettings.objects.filter(applicant_id=pk,category='SUMMARY')
	approval_status=ApprovalStatus.objects.all()
	


	if request.method=='POST':

		comment=request.POST.get('comment')
		approved_amount=request.POST.get('amount')
		if float(loan_comment.loan_amount) < float(approved_amount):
			messages.success(request,"Amount approved cannot be more than applied Amount")
			return HttpResponseRedirect(reverse('Loan_request_approval_details', args=(pk,)))

		status_id=request.POST.get('status')
		status=ApprovalStatus.objects.get(id=status_id)

		approved_date= datetime.datetime.now()


		loan_comment.approval_status=status
		loan_comment.approval_comment=comment
		loan_comment.approval_date=approved_date
		loan_comment.approved_amount=approved_amount
		loan_comment.save()
	
		return HttpResponseRedirect(reverse('loan_application_approval_list_load'))

	context={
	'loan_analysis':loan_analysis,
	'loan_summary':loan_summary,
	'pk':pk,
	'loan_comment':loan_comment,
	'approval_status':approval_status,
	}
	return render(request,'president_templates/Loan_application_approval_details.html',context)


def savings_cash_withdrawal_list_load(request):
	status=TransactionStatus.objects.get(title='UNTREATED')
	approval_status=ApprovalStatus.objects.get(title='PENDING')
	current_user=CustomUser.objects.get(id=request.user.id)
	applicants=MembersCashWithdrawalsApplication.objects.filter(approval_status=approval_status,status=status,approval_officer__officer_id=current_user)

	context={
	'applicants':applicants,
	}
	return render(request,'president_templates/savings_cash_withdrawal_list_load.html',context)


def savings_cash_withdrawal_preview(request,pk):
	form=savings_cash_withdrawal_preview_form(request.POST or None)
	applicant=MembersCashWithdrawalsApplication.objects.get(id=pk)
	applied_date =applicant.created_at
	
	maturity_date=applicant.maturity_date
	exclusive_status=ExclusiveStatus.objects.get(title="EXCLUSIVE")
	
	if applicant.member.member.exclusive_status==exclusive_status:
		submission_status=True
	else:
		submission_status=False
		if maturity_date <= current_date:
			submission_status=True
	approval_status=ApprovalStatus.objects.get(title='APPROVED')
	form.fields['ledger_balance'].initial= applicant.ledger_balance
	form.fields['amount_applied'].initial= applicant.amount
	form.fields['amount_approved'].initial= applicant.amount
	form.fields['status'].initial= applicant.status.id
	form.fields['comment'].initial= "Please Process"
	form.fields['status'].initial= approval_status.id

	if request.method=="POST":
		status_id=request.POST.get('status')
		status=ApprovalStatus.objects.get(id=status_id)
		amount_approved=request.POST.get('amount_approved')
		amount_applied=request.POST.get('amount_applied')
		comment=request.POST.get('comment')
		certification_officer_id=request.POST.get('certification_officers')
	
		certification_officer=CertificationOfficers.objects.get(id=certification_officer_id)
		
		if status.title == 'APPROVED':			
			if float(amount_approved) > float(amount_applied):
				messages.error(request,'Amount Approved Cannot be More than Applied Amount')
				return HttpResponseRedirect(reverse('savings_cash_withdrawal_preview',args=(pk,)))
			applicant.approval_status=status
			applicant.approved_amount=amount_approved
			applicant.approval_comment=comment
			applicant.approval_status=status
			applicant.certification_officer=certification_officer
			applicant.save()
			return HttpResponseRedirect(reverse('savings_cash_withdrawal_list_load'))
		else:
			pass
	context={
	'applicant':applicant,
	'form':form,
	'submission_status':submission_status,
	}
	return render(request,'president_templates/savings_cash_withdrawal_preview.html',context)



def members_exclusiveness_list_load(request):
	status=TransactionStatus.objects.get(title='UNTREATED')
	approval_status=ApprovalStatus.objects.get(title='PENDING')
	current_user=CustomUser.objects.get(id=request.user.id)
	applicants=MembersExclusiveness.objects.filter(approval_status=approval_status,status=status,approval_officer__officer_id=current_user)
	
	context={
	'applicants':applicants,
	}
	return render(request,'president_templates/members_exclusiveness_list_load.html',context)

def members_exclusiveness_process(request,pk):
	form=members_exclusiveness_request_approval_process_form(request.POST or None)
	applicant=MembersExclusiveness.objects.get(id=pk)
	if request.method=="POST":
		comment=request.POST.get('comment')
		status_id=request.POST.get('approval_status')
		status=ApprovalStatus.objects.get(id=status_id)
		applicant.approval_status=status
		applicant.approval_comment=comment
		applicant.approved_at=now
		applicant.save()
		return HttpResponseRedirect(reverse('members_exclusiveness_list_load'))

	context={
	'form':form,
	'applicant':applicant,
	}
	return render(request,'president_templates/members_exclusiveness_process.html',context)


def Shares_Purchase_Request_Approval_List_Load(request):
	status=TransactionStatus.objects.get(title='UNTREATED')
	approval_status=ApprovalStatus.objects.get(title='PENDING')
	records=MembersSharePurchaseRequest.objects.filter(approval_status=approval_status,status=status)
	
	context={
	'records':records,
	}
	return render(request,'president_templates/Shares_Purchase_Request_Approval_List_Load.html',context)


def Shares_Purchase_Request_Approval_Processed(request,pk):
	form=Shares_Purchase_Request_Approval_Processed_form(request.POST or None)
	record=MembersSharePurchaseRequest.objects.get(id=pk)

	if request.method=="POST":
		units = request.POST.get("units")
		comment=request.POST.get('comment')

		approval_status_id=request.POST.get('approval_status')
		approval_status=ApprovalStatus.objects.get(id=approval_status_id)

		record.units=units
		record.approval_status=approval_status
		record.approval_date=now
		record.approval_comment=comment
		record.save()
		return HttpResponseRedirect(reverse('Shares_Purchase_Request_Approval_List_Load'))
	form.fields['units'].initial=record.units
	context={
	'form':form,
	'record':record,
	}
	return render(request,'president_templates/Shares_Purchase_Request_Approval_Processed.html', context)