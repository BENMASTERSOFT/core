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

def deskofficer_home(request):
	DataCapture=DataCaptureManager.objects.first()
	status=MembershipStatus.objects.get(title='ACTIVE')
	member_count=Members.objects.filter(status=status).count()

	title="System User"
	context={
	'title':title,
	'member_count':member_count,
	'DataCapture':DataCapture,
	}
	return render(request, "deskofficer_templates/dashboard.html",context)


def desk_basic_form(request):
	return render(request, 'deskofficer_templates/basics/basic_form1.html')


def desk_basic_table(request):
	return render(request, 'deskofficer_templates/basics/basic_tables.html')

def desk_datatable_table(request):
	return render(request, 'deskofficer_templates/basics/datatable.html')


@csrf_exempt
def check_receipt_no_already_used(request):
	status=ReceiptStatus.objects.get(title='USED')
	receipt_no=request.POST.get("receipt_no")
	receipt_no_obj=Receipts.objects.filter(receipt=receipt_no,status=status).exists()
	if receipt_no_obj:
		return HttpResponse(True)
	else:
		return  HttpResponse(False)


#########################################################
############### PROFILE MANAGER #########################
#########################################################
def Useraccount_manager(request):
	DataCapture=DataCaptureManager.objects.first()
	form=Useraccount_manager_form(request.POST or None)
	user=CustomUser.objects.get(id=request.user.id)

	form.fields['username'].initial= user.username
	if request.method == 'POST':
		change_password=request.POST.get('changepassword')
		username=request.POST.get('username')
		password1=request.POST.get('password1')
		password2=request.POST.get('password2')

		if change_password:
			
			if password1 != password2:
				messages.info(request,"Password Mistmatch")
				return HttpResponseRedirect(reverse('Useraccount_manager'))
		
			user.username=username
			user.set_password(password1)
			user.save()	
			return HttpResponseRedirect(reverse('Useraccount_manager'))
		else:
			user.username=username
			user.save()	
			return HttpResponseRedirect(reverse('Useraccount_manager'))


	
	context={
	'form':form,
	'DataCapture':DataCapture,
	}
	return render(request,'deskofficer_templates/Useraccount_manager.html',context)


#########################################################
############### MEMBERSHIP TASK #########################
#########################################################

def membership_request(request):
	DataCapture=DataCaptureManager.objects.first()
	form=MembershipRequest_form(request.POST or None)
	if request.method=="POST":
		form=MembershipRequest_form(request.POST)
		processed_by = CustomUser.objects.get(id=request.user.id)
		
		title_id=request.POST.get("titles")
		title=Titles.objects.get(id=title_id)

		first_name=request.POST.get("first_name").upper()
		last_name=request.POST.get("last_name").upper()
		middle_name=request.POST.get("middle_name").upper()
		phone_no=request.POST.get("phone_no")

		gender_id=request.POST.get("gender")
		gender=Gender.objects.get(id=gender_id)

		department_id=request.POST.get("department")
		department=Departments.objects.get(id=department_id)
		record=MemberShipRequest(title=title,first_name=first_name,last_name=last_name,middle_name=middle_name,phone_number=phone_no,gender=gender,department=department,processed_by=processed_by)
		record.save()

		
		return HttpResponseRedirect(reverse('membership_request_additional_info',args=(record.pk,)))
	context={
	'form':form,
	'DataCapture':DataCapture,
	}
	return render(request, 'deskofficer_templates/membership_request.html',context)


def membership_request_complete_search(request):
	DataCapture=DataCaptureManager.objects.first()
	title="Search Membership Request Completetion"
	form = searchForm(request.POST or None)
	return render(request,'deskofficer_templates/membership_request_complete_search.html',{'form':form,'title':title,})


def membership_request_complete_load(request):
	DataCapture=DataCaptureManager.objects.first()
	title="Complete Membership Request"
	form = searchForm(request.POST)
	if request.method == "POST":
		if request.POST.get("title")=="":
			return HttpResponseRedirect(reverse('membership_request_complete_search'))

		submission_status=SubmissionStatus.objects.get(title="PENDING")
		form = searchForm(request.POST)
		members=MemberShipRequest.objects.filter(Q(phone_number__icontains=form['title'].value()) | Q(first_name__icontains=form['title'].value()) | Q(last_name__icontains=form['title'].value()) | Q(middle_name__icontains=form['title'].value())).filter(submission_status=submission_status)
		context={
		'members':members,
		'title':title,
		'DataCapture':DataCapture,
		}
		return render(request,'deskofficer_templates/membership_request_complete_list_load.html',context)


def membership_request_additional_info(request,pk):
	DataCapture=DataCaptureManager.objects.first()
	applicant=MemberShipRequest.objects.get(id=pk)
	officer=CustomUser.objects.get(id=request.user.id)
	
	records=MemberShipRequestAdditionalInfo.objects.filter(officer=officer,applicant=applicant)
	attached_infos=MemberShipRequestAdditionalAttachment.objects.filter(officer=officer,applicant=applicant)
	
	comment_form =MemberShipRequestAdditionalInfo_form(request.POST or None)
	attachment_form =MemberShipRequestAdditionalAttachment_form(request.POST or None)

	if MemberShipRequestAdditionalInfo.objects.filter(officer=officer,applicant=applicant).exists():	
		comment_form.fields['comment'].initial=records[0].comment

	if MemberShipRequestAdditionalAttachment.objects.filter(officer=officer,applicant=applicant).exists():	
		attachment_form.fields['caption'].initial=attached_infos[0].caption

	context={
	'comment_form':comment_form,
	'attachment_form':attachment_form,
	'pk':pk,
	'records':records,
	'attached_infos':attached_infos,
	'DataCapture':DataCapture,
	}
	return render(request,'deskofficer_templates/membership_request_additional_info.html',context)


def membership_request_additional_info_save(request,pk):
	applicant=MemberShipRequest.objects.get(id=pk)
	officer=CustomUser.objects.get(id=request.user.id)

	comment = request.POST.get('comment')
	if MemberShipRequestAdditionalInfo.objects.filter(officer=officer,applicant=applicant).exists():
		record=MemberShipRequestAdditionalInfo.objects.filter(officer=officer,applicant=applicant).first()
		record.comment=comment
		record.save()
		messages.success(request,"Record Updated Successfully")
		return HttpResponseRedirect(reverse('membership_request_additional_info',args=(pk,)))

	record=MemberShipRequestAdditionalInfo(comment=comment,officer=officer,applicant=applicant)
	record.save()
	messages.success(request,"Record Added Successfully")
	return HttpResponseRedirect(reverse('membership_request_additional_info',args=(pk,)))


def membership_request_additional_info_delete_confirm(request,pk,return_pk):
	DataCapture=DataCaptureManager.objects.first()
	comment=MemberShipRequestAdditionalInfo.objects.get(id=pk)
	context={
	'comment':comment,
	'pk':pk,
	'return_pk':return_pk,
	'DataCapture':DataCapture,
	}
	return render(request,'deskofficer_templates/membership_request_additional_info_delete_confirm.html',context)




def membership_request_additional_info_delete(request,pk,return_pk):
	comment=MemberShipRequestAdditionalInfo.objects.get(id=pk)
	comment.delete()
	return HttpResponseRedirect(reverse('membership_request_additional_info',args=(return_pk,)))



def MemberShipRequestAdditionalAttachment_save(request,pk):
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
		return HttpResponseRedirect(reverse('membership_request_additional_info',args=(pk,)))

	member=MemberShipRequestAdditionalAttachment(image=image_url,officer=officer,applicant=applicant,caption=caption)      
	member.save()
	messages.success(request,"Successfully Added Record")
	return HttpResponseRedirect(reverse('membership_request_additional_info',args=(pk,)))


def MemberShipRequest_submit(request,pk):
	DataCapture=DataCaptureManager.objects.first()
	form=MemberShipRequest_submit_form(request.POST or None)
	if request.method=="POST":
		submission_status=SubmissionStatus.objects.get(title="SUBMITTED")
		form=MemberShipRequest_submit_form(request.POST)
		certification_officer_id=request.POST.get("certification_officers")
		certification_officer=CertificationOfficers.objects.get(id=certification_officer_id)
		record=MemberShipRequest.objects.get(id=pk)
		record.certification_officer=certification_officer
		record.submission_status=submission_status
		
		record.save()
		messages.success(request,"Record Successfully Updated")
		return HttpResponseRedirect(reverse('membership_request_complete_search'))

	context={
	'form':form,
	'DataCapture':DataCapture,
	}
	return render(request,'deskofficer_templates/MemberShipRequest_submit.html', context)


def membership_form_sales_list_load(request):
	DataCapture=DataCaptureManager.objects.first()
	approval_status=ApprovalStatus.objects.get(title='APPROVED')
	transaction_status=TransactionStatus.objects.get(title='UNTREATED')
	applicants=MemberShipRequest.objects.filter(transaction_status=transaction_status,approval_status=approval_status)
	
	context={
	'applicants':applicants,
	'DataCapture':DataCapture,
	}
	return render(request,'deskofficer_templates/membership_form_sales_list_load.html',context)


def membership_form_sales_preview(request,pk):
	DataCapture=DataCaptureManager.objects.first()
	applicant=MemberShipRequest.objects.get(pk=pk)
	comments=MemberShipRequestAdditionalInfo.objects.filter(applicant_id=pk)
	attachments=MemberShipRequestAdditionalAttachment.objects.filter(applicant_id=pk)
	context={
	'applicant':applicant,
	'comments':comments,
	'attachments':attachments,
	'DataCapture':DataCapture,
	}
	return render(request,'deskofficer_templates/membership_form_sales_preview.html',context)


def membership_form_sales_issue(request,pk):
	DataCapture=DataCaptureManager.objects.first()
	form=membership_form_sales_issue_form(request.POST or None)
	applicant=MemberShipRequest.objects.get(id=pk)

	shares = MembersShareConfigurations.objects.first()
	shares_uint_cost=shares.unit_cost

	welfare=0
	if MembersWelfare.objects.all().exists():
		welfare_obj=MembersWelfare.objects.first()
		welfare=welfare_obj.amount

	admin_charge = TransactionTypes.objects.get(code='100')
	registration_fees=admin_charge.admin_charges

	receipt_type=ReceiptTypes.objects.get(title='MANUAL')

	receipt_types_status=False
	if admin_charge.receipt_type == receipt_type:
		receipt_types_status=True


	if request.method=="POST":
		transaction_status1=TransactionStatus.objects.get(title='UNTREATED')
		transaction_status=TransactionStatus.objects.get(title='TREATED')
		processed_by=CustomUser.objects.get(id=request.user.id)
		status=ReceiptStatus.objects.get(title='USED')

		bank_ccount_id=request.POST.get('account')
		bank_ccount=CooperativeBankAccounts.objects.get(id=bank_ccount_id)
	
		payment_reference=request.POST.get('payment_reference')
		if payment_reference=="":
			messages.error(request,'Payment Reference is required')
			return HttpResponseRedirect(reverse('membership_form_sales_issue',args=(pk,)))

		amount_paid=request.POST.get('amount_paid')
		share_id=request.POST.get('unit')
		share = SharesUnits.objects.get(id=share_id)
		share_unit=float(share.unit)
		total_shares=float(shares_uint_cost) * share_unit

		amount_due=float(total_shares) + float(welfare) + float(registration_fees)

		if float(amount_due) != float(amount_paid):
			messages.error(request,"Invalid Payment Amounts")
			return HttpResponseRedirect(reverse('membership_form_sales_issue',args=(pk,)))

		if receipt_types_status==True:
			receipt_id=request.POST.get('receipt')
			receipt=Receipts.objects.get(receipt=receipt_id)
		
			
			if Receipts.objects.filter(receipt=receipt_id,status=status).exists():
				messages.error(request,"Receipt Already in Use")
				return HttpResponseRedirect(reverse('membership_form_sales_issue',args=(pk,)))
		else:
			receipt_id=AutoReceipt.objects.first()
			receipt='C-' + str(receipt_id.receipt).zfill(5)
		
		if request.FILES.get('image', False):
			image = request.FILES['image']
			fs=FileSystemStorage()
			filename=fs.save(image.name,image)
			image_url=fs.url(filename)
		else:
			image_url=None


	
		record=MemberShipFormSalesRecord(payment_reference=payment_reference,image=image_url,bank_ccount=bank_ccount,welfare_amount=welfare,receipt=receipt,applicant=applicant,shares=share_unit,share_amount=total_shares,admin_charge=registration_fees,processed_by=processed_by,status=transaction_status1)
		record.save()

		if receipt_types_status==True:
			receipt.status=status
			receipt.save()
		else:
			receipt_id.receipt= int(receipt_id.receipt) + 1
			receipt_id.save()

		applicant.transaction_status=transaction_status
		applicant.save()

		messages.success(request,"Record Added Successfully")
		return HttpResponseRedirect(reverse('membership_form_sales_list_load'))
	
	form.fields['share_unit_cost'].initial=shares_uint_cost
	form.fields['welfare'].initial=welfare
	form.fields['registration_fees'].initial=registration_fees
	form.fields['receipt'].initial=0

	context={
	'form':form,
	'applicant':applicant,
	'receipt_types_status':receipt_types_status,
	'shares_uint_cost':shares_uint_cost,
	'DataCapture':DataCapture,
	}
	return render(request,'deskofficer_templates/membership_form_sales_issue.html',context)





def membership_registration_list_load(request):
	DataCapture=DataCaptureManager.objects.first()
	status=TransactionStatus.objects.get(title='UNTREATED')
	applicants=MemberShipFormSalesRecord.objects.filter(status=status)
	context={
	'applicants':applicants,
	'DataCapture':DataCapture,
	}
	return render(request,'deskofficer_templates/membership_registration_list_load.html',context)


def membership_registration_register(request,pk):
	DataCapture=DataCaptureManager.objects.first()
	applicant=MemberShipFormSalesRecord.objects.get(id=pk)
	now = datetime.datetime.now()
	processed_by = CustomUser.objects.get(id=request.user.id)

	shares=applicant.shares
	unit_cost=float(applicant.share_amount)/float(applicant.shares)
	total_cost=applicant.share_amount
	welfare_amount=applicant.welfare_amount


	form= membership_registration_register_form()
	form.fields['first_name'].initial=applicant.applicant.first_name
	form.fields['last_name'].initial=applicant.applicant.last_name
	form.fields['middle_name'].initial=applicant.applicant.middle_name
	form.fields['title'].initial=applicant.applicant.title_id
	form.fields['gender'].initial=applicant.applicant.gender.id
	form.fields['phone_number'].initial=applicant.applicant.phone_number
	form.fields['department'].initial=applicant.applicant.department.id
	form.fields['date_joined'].initial=now
	
	if request.method=="POST":
		
		form=membership_registration_register_form(request.POST)
		status=TransactionStatus.objects.get(title='TREATED')

		member_id_obj = MembersIdManager.objects.first()
		default_password = DefaultPassword.objects.first()
		password=default_password.title

		user_type_obj = UserType.objects.get(title='MEMBERS')
		user_type=user_type_obj.code

		share_transaction=TransactionTypes.objects.get(code=700)
		share_account=str(share_transaction.code) + str(member_id_obj.member_id).zfill(5) 

		welfare_transaction=TransactionTypes.objects.get(code=800)
		welfare_account=str(welfare_transaction.code) + str(member_id_obj.member_id).zfill(5)

		member_id = member_id_obj.prefix_title + "/" +  str(member_id_obj.prefix_year) + "/" + str(member_id_obj.member_id).zfill(5) 
		first_name = request.POST.get("first_name")
		last_name= request.POST.get("last_name")
		middle_name = request.POST.get("middle_name")
		username = request.POST.get("username")
		email = request.POST.get("email")
		residential_address = request.POST.get("residential_address")
		permanent_home_address= request.POST.get("permanent_home_address")
		
		phone_number = request.POST.get("phone_number")
		file_no = request.POST.get("file_no")
		ippis_no = request.POST.get("ippis_no")
		email = request.POST.get("email")
		username = request.POST.get("username")
		date_joined = request.POST.get("date_joined")

		title_id = request.POST.get("title")
		title = Titles.objects.get(id=title_id)

		gender_id = request.POST.get("gender")
		gender = Gender.objects.get(id=gender_id)
		
		department_id = request.POST.get("department")
		department = Departments.objects.get(id=department_id)

		state_id = request.POST.get("state")
		state = States.objects.get(id=state_id)
		
		lga_id = request.POST.get("lga")
		lga = Lga.objects.get(id=lga_id)

		salary_institution_id = request.POST.get("salary_institution")
		salary_institution = SalaryInstitution.objects.get(id=salary_institution_id)
		
		if request.FILES.get('profile_pic', False):
			profile_pic = request.FILES['profile_pic']
			fs=FileSystemStorage()
			filename=fs.save(profile_pic.name,profile_pic)
			profile_pic_url=fs.url(filename)
		else:
			profile_pic_url=None

		if first_name=="":
			messages.error(request,"First Name Missing")
			return HttpResponseRedirect(reverse('membership_registration_register',args=(pk,)))

		if last_name=="":
			messages.error(request,"Missing Last Name")
			return HttpResponseRedirect(reverse('membership_registration_register',args=(pk,)))
		
		if file_no=="":
			messages.error(request,"Missing File No")
			return HttpResponseRedirect(reverse('membership_registration_register',args=(pk,)))

		if ippis_no=="":
			messages.error(request,"Missing IPPIS No or Salary Code")
			return HttpResponseRedirect(reverse('membership_registration_register',args=(pk,)))
			
		if email=="":
			messages.error(request,"Missing Email Address")
			return HttpResponseRedirect(reverse('membership_registration_register',args=(pk,)))
		
		if username=="":
			messages.error(request,"Missing Username")
			return HttpResponseRedirect(reverse('membership_registration_register',args=(pk,)))
			
		# try:
		user = CustomUser.objects.create_user(username=username,password=password,email=email,last_name=last_name,first_name=first_name,user_type=int(user_type))
		user.members.applicant=applicant
		user.members.member_id=member_id
		user.members.title=title
		user.members.middle_name=middle_name
		user.members.full_name=str(first_name) + ' ' + str(last_name) + ' ' + str(middle_name)
		user.members.phone_number=phone_number
		user.members.gender=gender
		user.members.residential_address=residential_address
		user.members.permanent_home_address=permanent_home_address
		user.members.department=department
		user.members.state=state
		user.members.lga=lga
		user.members.salary_institution=salary_institution
		user.members.file_no=file_no
		user.members.ippis_no=ippis_no
		user.members.date_joined=date_joined
	
	
		if profile_pic_url!=None:
			user.members.profile_pic=profile_pic_url

		user.save()
		
		member_id_obj.member_id=int(member_id_obj.member_id) + 1
		member_id_obj.save()
		
		share_account=MembersAccountsDomain(member=user.members,transaction=share_transaction,account_number=share_account)
		share_account.save()
		
		share_record=MembersShareAccounts(member=share_account,shares=shares,unit_cost=unit_cost,total_cost=total_cost,effective_date=now,year=now.year,processed_by=processed_by)
		share_record.save()
		
		

		particulars=share_transaction.name + " INITIAL PURCHASE OF " + str(shares) + ' BY ' + str(unit_cost) + " PER A UNIT"
		debit=0
		credit=float(total_cost)
		balance=credit

		ledger_status=MembershipStatus.objects.get(title='ACTIVE')
		record=PersonalLedger(member=user.members,transaction=share_transaction,account_number=share_account.account_number,particulars=particulars,debit=debit,credit=credit,balance=abs(balance),transaction_period=now,status=ledger_status)
		record.save()

		welfare_account=MembersAccountsDomain(member=user.members,transaction=welfare_transaction,account_number=welfare_account)
		welfare_account.save()

		welfare_record=MembersWelfareAccounts(member=welfare_account,amount=welfare_amount,year=now.year)
		welfare_record.save()




		applicant.status=status
		applicant.save()


		return HttpResponseRedirect(reverse("membership_registration_list_load"))
		# except:
		# 	messages.error(request,"Failed to add Member")
		# 	return HttpResponseRedirect(reverse('membership_registration_register',args=(pk,)))
	
	context={
	'form':form,
	'applicant':applicant,
	'DataCapture':DataCapture,
	}
	return render(request,'deskofficer_templates/membership_registration_register.html',context)



#########################################################
############### MEMBERS ACCOUNT CRERATIONS###############
#########################################################
def Members_Account_Creation_Search(request):
	DataCapture=DataCaptureManager.objects.first()
	title="Search Membership for Account Creation"
	form = searchForm(request.POST or None)
	return render(request,'deskofficer_templates/Members_Account_Creation_Search.html',{'form':form,'title':title,'DataCapture':DataCapture,})


def Members_Account_Creation_list_load(request):
	DataCapture=DataCaptureManager.objects.first()
	title="Loan Request order"
	form = searchForm(request.POST)
	if request.method == "POST":
		if request.POST.get("title")=="":
			return HttpResponseRedirect(reverse('Members_Account_Creation_Search'))

		status=MembershipStatus.objects.get(title="ACTIVE")
		form = searchForm(request.POST)
		members=Members.objects.filter(Q(file_no__icontains=form['title'].value()) | Q(ippis_no__icontains=form['title'].value()) | Q(member_id__icontains=form['title'].value()) |Q(phone_number__icontains=form['title'].value()) | Q(admin__first_name__icontains=form['title'].value()) | Q(admin__last_name__icontains=form['title'].value()) | Q(middle_name__icontains=form['title'].value())).filter(status=status)
		context={
		'members':members,
		'title':title,
		'DataCapture':DataCapture,
		}
		return render(request,'deskofficer_templates/Members_Account_Creation_list_load.html',context)

def Members_Account_Creation_preview(request,pk):
	DataCapture=DataCaptureManager.objects.first()
	member=Members.objects.get(id=pk)
	transactions=TransactionTypes.objects.filter(~Q(source__title="LOAN") & ~Q(source__title='GENERAL'))
	records=MembersAccountsDomain.objects.filter(member=member)
	context={
	'member':member,
	'transactions':transactions,
	'DataCapture':DataCapture,
	'records':records,
	}
	return render(request,'deskofficer_templates/Members_Account_Creation_process.html',context)


def Members_Account_Creation_process(request,pk):
	member=Members.objects.get(id=pk)
	transactions=TransactionTypes.objects.filter(~Q(source__title="LOAN") & ~Q(source__title='GENERAL'))
	member_id=list((member.member_id).split("/"))

	count=0
	my_id=member_id[2]
	for transaction in transactions:
		account_number=str(transaction.code) + str(my_id) 
		if MembersAccountsDomain.objects.filter(member=member,transaction=transaction,account_number=account_number).exists():
			pass
		else:
			count +=1
			record=MembersAccountsDomain(member=member,transaction=transaction,account_number=account_number)
			record.save()
	messages.success(request,str(count) + ' Account(s) Successfully Created' )
	return HttpResponseRedirect(reverse('Members_Account_Creation_preview',args=(member.pk,)))



def Members_Multiple_Account_Creation_preview(request):
	DataCapture=DataCaptureManager.objects.first()
	status=MembershipStatus.objects.get(title='ACTIVE')
	members=Members.objects.filter(status=status)
	transactions=TransactionTypes.objects.filter(~Q(source__title="LOAN") & ~Q(source__title='GENERAL'))
	
	context={
	'members':members,
	'transactions':transactions,
	'DataCapture':DataCapture,
	}
	return render(request,'deskofficer_templates/Members_Multiple_Account_Creation_preview.html',context)


def Members_Multiple_Account_Creation_process(request):
	status=MembershipStatus.objects.get(title='ACTIVE')
	members=Members.objects.filter(status=status)
	transactions=TransactionTypes.objects.filter(~Q(source__title="LOAN") & ~Q(source__title='GENERAL'))
	
	count=0
	for member in members:
		member_id=list((member.member_id).split("/"))
		my_id=member_id[2]

		for transaction in transactions:
			account_number=str(transaction.code) + str(my_id) 
			if MembersAccountsDomain.objects.filter(member=member,transaction=transaction,account_number=account_number).exists():
				pass
			else:
				count +=1
				record=MembersAccountsDomain(member=member,transaction=transaction,account_number=account_number)
				record.save()
	messages.success(request,str(count) + ' Account(s) Successfully Created')
	return HttpResponseRedirect(reverse('Members_Multiple_Account_Creation_preview'))


def Members_account_details_list(request,pk):
	transaction=TransactionTypes.objects.get(id=pk)
	records=MembersAccountsDomain.objects.filter(transaction=transaction)
	context={
	'records':records,
	'transaction':transaction,
	}
	return render(request,'deskofficer_templates/Members_account_details_list.html',context)



#########################################################
############### STANDING ORDER #########################
#########################################################
def standing_order_selected_search(request):
	DataCapture=DataCaptureManager.objects.first()
	title="Search Membership for Standing Order"
	form = searchForm(request.POST or None)
	return render(request,'deskofficer_templates/standing_order_selected_search.html',{'form':form,'title':title,'DataCapture':DataCapture,})


def standing_order_selected_list_load(request):
	DataCapture=DataCaptureManager.objects.first()
	title="Loan Request order"
	form = searchForm(request.POST)
	if request.method == "POST":
		if request.POST.get("title")=="":
			return HttpResponseRedirect(reverse('standing_order_selected_search'))

		status=MembershipStatus.objects.get(title="ACTIVE")
		form = searchForm(request.POST)
		members=Members.objects.filter(Q(file_no__icontains=form['title'].value()) | Q(ippis_no__icontains=form['title'].value()) | Q(member_id__icontains=form['title'].value()) |Q(phone_number__icontains=form['title'].value()) | Q(admin__first_name__icontains=form['title'].value()) | Q(admin__last_name__icontains=form['title'].value()) | Q(middle_name__icontains=form['title'].value())).filter(status=status)
		context={
		'members':members,
		'title':title,
		'DataCapture':DataCapture,
		}
		return render(request,'deskofficer_templates/standing_order_selected_list_load.html',context)


def standing_order_selected_form(request,pk):
	DataCapture=DataCaptureManager.objects.first()
	applicant=Members.objects.get(id=pk)
	form=standing_orderform(request.POST or None)
	standing_orders=StandingOrderAccounts.objects.filter(member_id=applicant.id)

	if request.method=="POST":
		form=standing_orderform(request.POST)
		if form.is_valid():			
			saving_id=form.cleaned_data["savings"]
			saving = TransactionTypes.objects.get(id=saving_id)
			amount=form.cleaned_data["amount"]

			minimum_amount = saving.minimum_amount
			
			if float(amount)<=0:
				messages.error(request,"Amount  cannot be zero(0)")
				return HttpResponseRedirect(reverse('standing_order_selected_form', args=(pk,)))


			if float(amount)<float(minimum_amount):
				messages.error(request,"Amount Specified is Less than " + str(minimum_amount) + " Minimum Amount allowed for this Transaction")
				return HttpResponseRedirect(reverse('standing_order_selected_form', args=(pk,)))

			if StandingOrderAccounts.objects.filter(member=applicant,transaction=saving).exists():
				member=StandingOrderAccounts.objects.get(member=applicant,transaction=saving)
				member.amount=amount
				member.save()
				return HttpResponseRedirect(reverse('standing_order_selected_form', args=(pk,)))


			member_id=list((applicant.member_id).split("/"))
	
			my_id=member_id[2]

			account_number=str(saving.code) + str(my_id) 
			member=StandingOrderAccounts(member=applicant,transaction=saving,amount=amount,account_number=account_number)
			member.save()
			return HttpResponseRedirect(reverse('standing_order_selected_form', args=(pk,)))
	context={
	'applicant':applicant,
	'form':form,
	'standing_orders':standing_orders,
	'DataCapture':DataCapture,
	}
	return render(request,'deskofficer_templates/standing_order_selected_form.html',context)


def standing_order_list_load(request):
	DataCapture=DataCaptureManager.objects.first()
	status=MembershipStatus.objects.get(title='ACTIVE')
	applicants=Members.objects.filter(status=status)
	context={
	'applicants':applicants,
	'DataCapture':DataCapture,
	}
	return render(request,'deskofficer_templates/standing_order_list_load.html',context)


def standing_order_form(request,pk):
	DataCapture=DataCaptureManager.objects.first()
	applicant=Members.objects.get(id=pk)
	form=standing_orderform(request.POST or None)
	standing_orders=StandingOrderAccounts.objects.filter(transaction__member=applicant)
	account_number=[]

	

	if request.method=="POST" and 'btn_submit' in request.POST:
		lock_status=LockedStatus.objects.get(title='LOCKED')
		form=standing_orderform(request.POST)
		
		saving_id=request.POST.get("savings")
		saving = TransactionTypes.objects.get(id=saving_id)

		if MembersAccountsDomain.objects.filter(member=applicant,transaction=saving).exists():
			account_number=MembersAccountsDomain.objects.get(member=applicant,transaction=saving)

		amount=request.POST.get("amount")

		minimum_amount = saving.minimum_amount
		
		if float(amount)<=0:
			messages.error(request,"Amount  cannot be zero(0)")
			return HttpResponseRedirect(reverse('standing_order_form', args=(pk,)))


		if float(amount)<float(minimum_amount):
			messages.error(request,"Amount Specified is Less than " + str(minimum_amount) + " Minimum Amount allowed for this Transaction")
			return HttpResponseRedirect(reverse('standing_order_form', args=(pk,)))

		if StandingOrderAccounts.objects.filter(transaction=account_number).exists():
			member=StandingOrderAccounts.objects.get(transaction=account_number)
			if member.lock_status.title == 'OPEN':
				member.amount=amount
				member.save()
			else:
				messages.error(request,"This Transaction is Locked, Update not Allowed from this point")
			return HttpResponseRedirect(reverse('standing_order_form', args=(pk,)))


		member=StandingOrderAccounts(transaction=account_number,amount=amount)
		member.save()
		return HttpResponseRedirect(reverse('standing_order_form', args=(pk,)))


	
	context={
	'applicant':applicant,
	'form':form,
	'standing_orders':standing_orders,
	'DataCapture':DataCapture,
	'account_number':account_number,
	}
	return render(request,'deskofficer_templates/standing_order_form.html',context)


def standing_order_locked(request,pk):
	status=LockedStatus.objects.get(title="LOCKED")
	all_record_update=StandingOrderAccounts.objects.filter(transaction__member_id=pk).update(lock_status=status)
	return HttpResponseRedirect(reverse('standing_order_form',args=(pk,)))




def standing_order_remove(request,pk):
	record = StandingOrderAccounts.objects.get(id=pk)
	return_pk=record.transaction.member_id
	record.delete()
	return HttpResponseRedirect(reverse('standing_order_form',args=(return_pk,)))



#########################################################
############### TRANSACTION  ADJUSTMENT #################
#########################################################
def Transaction_adjustment_search(request):
	DataCapture=DataCaptureManager.objects.first()
	title="Search Membership for Adjustment"
	form = searchForm(request.POST or None)
	return render(request,'deskofficer_templates/Transaction_adjustment_search.html',{'form':form,'title':title,'DataCapture':DataCapture,})


def Transaction_adjustment_List_load(request):
	DataCapture=DataCaptureManager.objects.first()
	title="Loan Request order"
	form = searchForm(request.POST)
	if request.method == "POST":
		if request.POST.get("title")=="":
			return HttpResponseRedirect(reverse('Transaction_adjustment_search'))

		status=MembershipStatus.objects.get(title="ACTIVE")
		form = searchForm(request.POST)
		members=Members.objects.filter(Q(file_no__icontains=form['title'].value()) | Q(ippis_no__icontains=form['title'].value()) | Q(member_id__icontains=form['title'].value()) |Q(phone_number__icontains=form['title'].value()) | Q(admin__first_name__icontains=form['title'].value()) | Q(admin__last_name__icontains=form['title'].value()) | Q(middle_name__icontains=form['title'].value())).filter(status=status)
		context={
		'members':members,
		'title':title,
		'DataCapture':DataCapture,
		}
		return render(request,'deskofficer_templates/Transaction_adjustment_List_load.html',context)


def Transaction_adjustment_Transactions_load(request,pk):
	status = TransactionStatus.objects.get(title='UNTREATED')
	DataCapture=DataCaptureManager.objects.first()
	form=Transaction_adjustment_Transactions_form(request.POST or None)
	member=Members.objects.get(id=pk)
	member_selected=MembersAccountsDomain.objects.filter(member=member).first()
	records=TransactionAjustmentRequest.objects.filter(member__member=member_selected.member_id,status=status)
	
	transactions=[]
	active_transactions=[]
	
	if request.method=="POST" and 'btn_transaction' in request.POST:
		transaction_id=request.POST.get('transactions')
		transaction=TransactionTypes.objects.get(id=transaction_id)
		
		return HttpResponseRedirect(reverse('Transaction_adjustment_Transactions_Accounts_load',args=(transaction.pk,pk,)))

	context={

	'form':form,
	'member':member,
	'transactions':transactions,
	'active_transactions':active_transactions,
	'DataCapture':DataCapture,
	'records':records,
	}
	return render(request,'deskofficer_templates/Transaction_adjustment_Transactions_load.html',context)


def Transaction_adjustment_Transactions_Accounts_load(request,pk, return_pk):
	status = TransactionStatus.objects.get(title='UNTREATED')
	DataCapture=DataCaptureManager.objects.first()
	transaction=TransactionTypes.objects.get(id=pk)
	minimum_amount=transaction.minimum_amount
	member=Members.objects.get(id=return_pk)

	form=Transaction_adjustment_selection_form(request.POST or None)
	member_selected=MembersAccountsDomain.objects.get(member=member,transaction=transaction)

	
	if request.method=="POST":
		
		account_number=request.POST.get("account_number")
		transaction=StandingOrderAccounts.objects.get(transaction__account_number=account_number)
		amount = request.POST.get('amount')
		effective_date=request.POST.get('effective_date')
		approval_officer_id=request.POST.get('approval_officers')
		approval_officer=ApprovalOfficers.objects.get(id=approval_officer_id)
		
		if TransactionAjustmentRequest.objects.filter(member=member_selected,status=status).exists():
			messages.info(request,'You still have an Incomplete Transactions')
			return HttpResponseRedirect(reverse('Transaction_adjustment_Transactions_Accounts_load',args=(pk, return_pk,)))
	
		if float(amount) == 0:
			pass
		elif float(amount) < float(minimum_amount):
			messages.info(request,'The amount specified is less then the Minimum Amount of ' +  str(minimum_amount) + ' allowed')
			return HttpResponseRedirect(reverse('Transaction_adjustment_Transactions_Accounts_load',args=(pk, return_pk,)))
		

		record=TransactionAjustmentRequest(member=member_selected,amount=amount,effective_date=effective_date,approval_officer=approval_officer)
		record.save()
		return HttpResponseRedirect(reverse('Transaction_adjustment_Transactions_load',args=(return_pk,)))

	active_transactions=StandingOrderAccounts.objects.filter(transaction=member_selected).first()
	if active_transactions:
		form.fields['effective_date'].initial=now
		context={
		'active_transactions':active_transactions,
		'form':form,
		'pk':pk,
		'return_pk':return_pk,
		'DataCapture':DataCapture,
		
		}
		return render(request,'deskofficer_templates/Transaction_adjustment_Transactions_Accounts_load.html',context)
	else:
		messages.info(request,'No active account for this Transaction')
		return HttpResponseRedirect(reverse('Transaction_adjustment_Transactions_load',args=(return_pk,)))


def Transaction_adjustment_Transactions_Accounts_Remove(request,pk):
	record=TransactionAjustmentRequest.objects.get(id=pk)
	return_pk=record.member.member_id
	record.delete()
	return HttpResponseRedirect(reverse('Transaction_adjustment_Transactions_load', args=(return_pk,)))



def Transaction_Adjustment_Approved_List_Load(request):
	approval_status=ApprovalStatus.objects.get(title='APPROVED')
	status=TransactionStatus.objects.get(title='UNTREATED')
	records=TransactionAjustmentRequest.objects.filter(approval_status=approval_status,status=status)

	context={
	'records':records,
	}
	return render(request,'deskofficer_templates/Transaction_Adjustment_Approved_List_Load.html',context)


def Transaction_Adjustment_Approved_Processed(request,pk):
	status=TransactionStatus.objects.get(title='TREATED')
	record=TransactionAjustmentRequest.objects.get(id=pk)
	amount=record.amount
	if float(amount) == 0:
		record.member.standingorderaccounts.delete()
	else:
		record.member.standingorderaccounts.amount=amount
		record.member.standingorderaccounts.save()
	record.status=status
	record.save()
	return HttpResponseRedirect(reverse('Transaction_Adjustment_Approved_List_Load'))


def Transaction_Loan_adjustment_search(request):
	DataCapture=DataCaptureManager.objects.first()
	title="Search Membership for Loan Adjustment"
	form = searchForm(request.POST or None)
	return render(request,'deskofficer_templates/Transaction_Loan_adjustment_search.html',{'form':form,'title':title,'DataCapture':DataCapture,})


def Transaction_Loan_adjustment_List_load(request):
	DataCapture=DataCaptureManager.objects.first()
	title="Loan Request order"
	form = searchForm(request.POST)
	if request.method == "POST":
		if request.POST.get("title")=="":
			return HttpResponseRedirect(reverse('Transaction_adjustment_search'))

		status=MembershipStatus.objects.get(title="ACTIVE")
		form = searchForm(request.POST)
		members=Members.objects.filter(Q(file_no__icontains=form['title'].value()) | Q(ippis_no__icontains=form['title'].value()) | Q(member_id__icontains=form['title'].value()) |Q(phone_number__icontains=form['title'].value()) | Q(admin__first_name__icontains=form['title'].value()) | Q(admin__last_name__icontains=form['title'].value()) | Q(middle_name__icontains=form['title'].value())).filter(status=status)
		context={
		'members':members,
		'title':title,
		'DataCapture':DataCapture,
		}
		return render(request,'deskofficer_templates/Transaction_Loan_adjustment_List_load.html',context)


def Transaction_Loan_adjustment_Transaction_load(request,pk):
	status=TransactionStatus.objects.get(title='UNTREATED')
	member=Members.objects.get(id=pk)
	records=LoansRepaymentBase.objects.filter(member=member,balance__lt=0)

	existing_requests=TransactionLoanAjustmentRequest.objects.filter(member__member=member,status=status)
	
	context={
	'records':records,
	'member':member,
	'existing_requests':existing_requests,
	}
	return render(request,'deskofficer_templates/Transaction_Loan_adjustment_Transaction_load.html',context)


def Transaction_Loan_adjustment_Transaction_Preview(request,pk,loan_code):
	form=Transaction_Loan_adjustment_selection_form(request.POST or None)

	member=Members.objects.get(id=pk)
	loan=[]
	if request.method=='POST':
		loan_id=request.POST.get('loan')
		loan=LoansRepaymentBase.objects.get(id=loan_id)
	else:
		loan=LoansRepaymentBase.objects.get(id=loan_code)

	context={
	'member':member,
	'loan':loan,
	'form':form,
	}
	return render(request,'deskofficer_templates/Transaction_Loan_adjustment_Transaction_Preview.html',context)


def Transaction_Loan_adjustment_Transaction_Process(request,pk,loan_code):
	# member=Members.objects.get(id=pk)
	loan=LoansRepaymentBase.objects.get(id=loan_code)
	if request.method =="POST":
		purpose=request.POST.get('purpose')
		repayment=request.POST.get('repayment')
		amount=request.POST.get('amount')
		approval_officer_id=request.POST.get('approval_officers')
		approval_officer=ApprovalOfficers.objects.get(id=approval_officer_id)
		effective_date=now


		if float(repayment) >= float(amount):
			messages.info(request,'Invalid Amount Specification')
			return HttpResponseRedirect(reverse('Transaction_Loan_adjustment_Transaction_Preview',args=(pk,loan_code,)))
		
		status=TransactionStatus.objects.get(title='UNTREATED')

		if TransactionLoanAjustmentRequest.objects.filter(member=loan,status=status):
			messages.info(request,'You still have an Incomplete Transactions')
			return HttpResponseRedirect(reverse('Transaction_Loan_adjustment_Transaction_Preview',args=(pk,loan_code,)))


		record=TransactionLoanAjustmentRequest(member=loan,
			amount=amount,approval_officer=approval_officer,effective_date=effective_date)
		record.save()

		return HttpResponseRedirect(reverse('Transaction_Loan_adjustment_Transaction_load',args=(pk,)))

def Transaction_Loan_adjustment_Transaction_Cancel(request,pk):
	record=TransactionLoanAjustmentRequest(id=pk)
	return_pk=record.member.member.id
	record.delete()
	return HttpResponseRedirect(reverse('Transaction_Loan_adjustment_Transaction_load',args=(return_pk,)))

def Transaction_Loan_adjustment_Transaction_Approved_List_Load(request):
	status=TransactionStatus.objects.get(title='UNTREATED')
	approval_status=ApprovalStatus.objects.get(title="APPROVED")
	records=TransactionLoanAjustmentRequest.objects.filter(status=status,approval_status=approval_status)
	context={
	'records':records,
	}
	return render(request,'deskofficer_templates/Transaction_Loan_adjustment_Transaction_Approved_List_Load.html',context)


#########################################################
############### LOAN TRANSACTION ########################
#########################################################


def loan_request_search(request):
	DataCapture=DataCaptureManager.objects.first()
	title="Search Membership Loan Request"
	form = searchForm(request.POST or None)
	return render(request,'deskofficer_templates/loan_request_search.html',{'form':form,'title':title,'DataCapture':DataCapture,})


def loan_request_list_load(request):
	DataCapture=DataCaptureManager.objects.first()
	title="Loan Request order"
	form = searchForm(request.POST)
	if request.method == "POST":
		if request.POST.get("title")=="":
			return HttpResponseRedirect(reverse('loan_request_search'))

		status=MembershipStatus.objects.get(title="ACTIVE")
		form = searchForm(request.POST)
		members=Members.objects.filter(Q(member_id__icontains=form['title'].value()) |Q(phone_number__icontains=form['title'].value()) | Q(admin__first_name__icontains=form['title'].value()) | Q(admin__last_name__icontains=form['title'].value()) | Q(middle_name__icontains=form['title'].value())).filter(status=status)
		context={
		'members':members,
		'title':title,
		'DataCapture':DataCapture,
		}
		return render(request,'deskofficer_templates/loan_request_list_load.html',context)


def loan_request_order(request,pk):
	DataCapture=DataCaptureManager.objects.first()
	submission_status=SubmissionStatus.objects.get(title="PENDING")
	transaction_status=TransactionStatus.objects.get(title="UNTREATED")
	form=loan_request_order_form(request.POST or None)
	member=Members.objects.get(id=pk)

	exist_loans = LoanRequest.objects.filter(member_id=member,submission_status=submission_status,transaction_status=transaction_status)

	if request.method=="POST":
		form=loan_request_order_form(request.POST)
		if form.is_valid():
			category=LoanCategory.objects.get(title='MONETARY')
			processed_by=CustomUser.objects.get(id=request.user.id)
			loan_obj = form.cleaned_data["loans"]
			loan=TransactionTypes.objects.get(id=loan_obj)  
			amount = form.cleaned_data["amount"]
			maximum_amount = loan.maximum_amount
			multiple_loan_status=loan.multiple_loan_status



			if LoansDisbursed.objects.filter(member=member,transaction=loan).filter(Q(balance__lt=0)).exists():
				if multiple_loan_status.title == 'NOT ALLOWED':
					messages.info(request,"Additional Loan not allowed for the Transaction")
					return HttpResponseRedirect(reverse('loan_request_order', args=(pk,)))

				if member.exclusive_status.title=="NON EXCLUSIVE":
					messages.info(request,"This member is not Permitted for Additional Loan for the Transaction, See the Management")
					return HttpResponseRedirect(reverse('loan_request_order', args=(pk,)))
				else:
					if MembersExclusiveness.objects.filter(transaction=loan).exists():
						pass
					else:
						messages.info(request,"This member is not Permitted for Additional Loan for the Transaction, See the Management")
						return HttpResponseRedirect(reverse('loan_request_order', args=(pk,)))
				
			if loan.category==category:
				if float(amount)>float(maximum_amount):
					messages.error(request,"Amount Specified is More than " + str(maximum_amount) + " Maximum Amount allowed for this Transaction")
					return HttpResponseRedirect(reverse('loan_request_order', args=(pk,)))

			if LoanRequest.objects.filter(member=member,loan=loan,transaction_status=transaction_status).exists():
				messages.error(request,"You still have Open Transaction")
				return HttpResponseRedirect(reverse('loan_request_order', args=(pk,)))

			record=LoanRequest(member=member,loan_amount=amount,loan=loan,submission_status=submission_status,transaction_status=transaction_status,processed_by=processed_by)
			record.save()
			return HttpResponseRedirect(reverse('loan_request_order', args=(pk,)))
	context={
	'form':form,

	'member':member,
	'exist_loans':exist_loans,
	'pk':pk,
	'DataCapture':DataCapture,
	}
	return render(request,'deskofficer_templates/loan_request_order.html',context)


def loan_request_order_delete(request,pk,return_pk):
	record=LoanRequest.objects.get(id=pk)
	LoanRequestAttachments.objects.filter(applicant=record).delete()
	record.delete()
	return HttpResponseRedirect(reverse('loan_request_order', args=(return_pk,)))




def loan_request_criteria_Load(request,pk):
	DataCapture=DataCaptureManager.objects.first()
	form=loan_criteria_external_fascilities_form(request.POST or None)
	applicant=LoanRequest.objects.get(id=pk)
	gross_pay=applicant.member.gross_pay




	if applicant.member.department:
		pass
	else:
		messages.info(request,"Members Department is Missing")
		return HttpResponseRedirect(reverse('loan_request_order',args=(applicant.member_id,)))

	if gross_pay <= 0:
		messages.info(request,'Please Upload Salary Information')
		return HttpResponseRedirect(reverse('loan_request_order',args=(applicant.member_id,)))

	total_savings=0
	savings=[]
	if StandingOrderAccounts.objects.filter(transaction__member_id=applicant.member_id).exists():
		savings = StandingOrderAccounts.objects.filter(transaction__member_id=applicant.member_id)
		savings_sum=StandingOrderAccounts.objects.filter(transaction__member_id=applicant.member_id).aggregate(total_amount=Sum('amount'))
		total_savings=savings_sum['total_amount']


	total_loans=0
	loans=[]
	loan_status=MembershipStatus.objects.get(title='ACTIVE')
	if LoansRepaymentBase.objects.filter(Q(balance__lt=0) & Q(member_id=applicant.member_id,status=loan_status)).exists():
		loans=LoansRepaymentBase.objects.filter(Q(balance__lt=0) & Q(member_id=applicant.member_id))
		loans_sum=LoansRepaymentBase.objects.filter(Q(balance__lt=0) & Q(member_id=applicant.member_id)).aggregate(total_amount=Sum('repayment'))
		total_loans=loans_sum['total_amount']


	shop_balance=0
	shops=[]
	if CooperativeShopLedger.objects.filter(member_id=applicant.member_id).exists():
		shops =CooperativeShopLedger.objects.filter(Q(balance__lt=0) & Q(member_id=applicant.member_id)).order_by('-id').first()
		shop_balance=abs(shops.balance)

	records_amount=0
	records=[]
	if ExternalFascilitiesTemp.objects.filter(member=applicant.member_id).exists():
		records=ExternalFascilitiesTemp.objects.filter(member=applicant.member_id)
		records_amount_sum=ExternalFascilitiesTemp.objects.filter(member=applicant.member_id).aggregate(total_amount=Sum('amount'))
		records_amount=records_amount_sum['total_amount']

	

	total_debit=float(total_savings)+float(total_loans)+float(shop_balance)+ float(records_amount)
	


	
	balance=float(gross_pay)-total_debit
	attachment_form=loan_request_document_attachment_form(request.POST or None)
	items=LoanRequestAttachments.objects.filter(applicant=applicant)
	
	
	if request.method=="POST" and 'attachment' in request.POST:
		attachment_form=loan_request_document_attachment_form(request.POST)
		if attachment_form.is_valid():
			processed_by=CustomUser.objects.get(id=request.user.id)
			description = attachment_form.cleaned_data["description"]

			if request.FILES.get('image', False):
				image = request.FILES['image']
				fs=FileSystemStorage()
				filename=fs.save(image.name,image)
				image_url=fs.url(filename)
			else:
				image_url=None

			if LoanRequestAttachments.objects.filter(applicant=applicant,description=description).exists():
				record_exist=LoanRequestAttachments.objects.filter(applicant=applicant,description=description).order_by('id').first()
				record_exist.image=image_url
				record_exist.processed_by=processed_by
				record_exist.save()
				return HttpResponseRedirect(reverse('loan_request_criteria_Load',args=(pk,)))


			record=LoanRequestAttachments(applicant=applicant,description=description,image=image_url,processed_by=processed_by)
			record.save()
			return HttpResponseRedirect(reverse('loan_request_criteria_Load',args=(pk,)))

	context={
	'form':form,
	'applicant':applicant,
	'savings':savings,
	'loans':loans,
	'shops':shops,
	'shop_balance':shop_balance,
	'records':records,
	'gross_pay':gross_pay,
	'total_debit':total_debit,
	'balance':balance,
	'pk':pk,
	'attachment_form':attachment_form,
	'items':items,

	'DataCapture':DataCapture,
	}
	return render(request,'deskofficer_templates/loan_request_criteria_Load.html',context)


def LoanRequestAttachments_delete(request,pk,return_pk):
	item=LoanRequestAttachments.objects.get(id=pk)
	item.delete()
	return HttpResponseRedirect(reverse('loan_request_criteria_Load',args=(return_pk,)))



def loan_request_preview(request,pk):
	DataCapture=DataCaptureManager.objects.first()
	applicant=LoanRequest.objects.get(id=pk)
	gross_pay=applicant.member.gross_pay
	
	if LoanBasedSavings.objects.all().exists():
		loan_based_saving = LoanBasedSavings.objects.first()
	else:		
		messages.info(request,'Loan Based Savings not Set')
		return HttpResponseRedirect(reverse('loan_request_criteria_Load', args=(pk,)))
	
	savings_saved=0
	if StandingOrderAccounts.objects.filter(transaction__transaction=loan_based_saving.savings,transaction__member=applicant.member).exists():
		account_id=StandingOrderAccounts.objects.get(transaction__transaction=loan_based_saving.savings,transaction__member=applicant.member)
	
		savings_ledger=PersonalLedger.objects.filter(account_number=account_id.transaction.account_number).last()
		savings_saved=savings_ledger.balance
		
	loan_based_saving_rating=applicant.loan.savings_rate



	loan_saving_relationship=float(int(loan_based_saving_rating)/100) * float(applicant.loan_amount)
	

	loan_savings_status=False
	if float(savings_saved) > float(loan_saving_relationship) :
		loan_savings_status=True

	
	total_savings=0
	savings_sum=StandingOrderAccounts.objects.filter(transaction__member_id=applicant.member_id).aggregate(total_amount=Sum('amount'))
	total_savings=savings_sum['total_amount']
	if total_savings==None:
		total_savings=0


	total_loans=0
	loans_sum=LoansRepaymentBase.objects.filter(Q(balance__lt=0) & Q(member_id=applicant.member_id)).aggregate(total_amount=Sum('repayment'))
	total_loans=loans_sum['total_amount']
	if total_loans==None:
		total_loans=0

	shop_balance=0
	shops =CooperativeShopLedger.objects.filter(Q(balance__lt=0) & Q(member_id=applicant.member_id)).order_by('-id').first()
	if shops:
		shop_balance=abs(shops.balance)

	status=TransactionStatus.objects.get(title='UNTREATED')
	records_amount=0
	records_amount_sum=ExternalFascilitiesMain.objects.filter(member__member_id=applicant.member_id,status=status).aggregate(total_amount=Sum('member__amount'))
	records_amount=records_amount_sum['total_amount']
	if records_amount==None:
		records_amount=0

	
	total_debit=float(total_savings)+float(total_loans)+float(shop_balance)+ float(records_amount)

	
	balance=float(gross_pay)-total_debit
		
	date_joined = applicant.member.date_joined
	now = datetime.datetime.now()


	same_type_loan=False
	if LoansDisbursed.objects.filter(Q(balance__gt=0) & Q(member__member_id=applicant.member_id) & Q(transaction_id=applicant.loan_id)).exists():
		same_type_loan=True


	loan_type=applicant.loan.name
	loan_amount=applicant.loan_amount
	duration = applicant.loan.duration
	salary_loan_relationship = applicant.loan.salary_loan_relationship
	salary_loan_relationship_computed= float(int(salary_loan_relationship)/100) * float(balance)

	interest_rate = applicant.loan.interest_rate
	interest= float(int(interest_rate)/100) * float(applicant.loan_amount)
	loan_age = applicant.loan.loan_age
	members_age = (now.year - date_joined.year) * 12 + (now.month - date_joined.month)

	interest_deduction=applicant.loan.interest_deduction

	if interest_deduction == "SOURCE":
		amount_scheduled = float(loan_amount)
	else:
		amount_scheduled = float(loan_amount)+ float(interest)
	if int(duration) == 0:
		messages.info(request,'Please set the Loan Dusration')
		return HttpResponseRedirect(reverse('loan_request_criteria_Load', args=(pk,)))
	
	part1= float(amount_scheduled)//float(duration)
	part2= float(amount_scheduled)%float(duration)

	if int(part2) >= 1:
		monthly_repayment='{0:.2f}'.format(float(part1)+ 1)
	else:
		monthly_repayment='{0:.2f}'.format(float(part1))

	salary_status=True
	if float(monthly_repayment)> float(salary_loan_relationship_computed):
		salary_status=False

	Member_Status = False
	if int(members_age)>int(loan_age):
		Member_Status = True

	exclusive=applicant.member.exclusive_status


	certification_officers=CertificationOfficers.objects.filter(transaction__transaction_id=applicant.loan_id)

	if request.method=="POST":
		submission_status=SubmissionStatus.objects.get(title="SUBMITTED")
		comment=request.POST.get("comment")
		officer_id=request.POST.get("officer")
		officer=CertificationOfficers.objects.get(id=officer_id)
		applicant.certification_officer=officer
		applicant.comment=comment
		applicant.submission_status=submission_status
		applicant.save()

		description="GROSS PAY"
		value=gross_pay
		loan_setting=LoanRequestSettings(applicant=applicant,description=description,value=value,category='ANALYSIS')
		loan_setting.save()
		

		description="SALARY BALANCE AFTER DEDUCTIONS"
		value=balance
		loan_setting=LoanRequestSettings(applicant=applicant,description=description,value=value,category='ANALYSIS')
		loan_setting.save()

		description=loan_type
		value=loan_amount
		loan_setting=LoanRequestSettings(applicant=applicant,description=description,value=value,category='ANALYSIS')
		loan_setting.save()

		description="MONTHLY DEDUCTIONS"
		value=total_savings
		loan_setting=LoanRequestSettings(applicant=applicant,description=description,value=value,category='ANALYSIS')
		loan_setting.save()

		description="MONTHLY LOAN REPAYMENTS"
		value=total_loans
		loan_setting=LoanRequestSettings(applicant=applicant,description=description,value=value,category='ANALYSIS')
		loan_setting.save()

		description="COOPERATIVE SHOP"
		value=shop_balance
		loan_setting=LoanRequestSettings(applicant=applicant,description=description,value=value,category='ANALYSIS')
		loan_setting.save()

		description="EXTERNAL FASCILITIES"
		value=records_amount
		loan_setting=LoanRequestSettings(applicant=applicant,description=description,value=value,category='ANALYSIS')
		loan_setting.save()

		description="LOAN DURATION"
		value=str(duration) + " MONTHS"
		loan_setting=LoanRequestSettings(applicant=applicant,description=description,value=value,category='ANALYSIS')
		loan_setting.save()

		description="SALARY LOAN RELATIONSHIP"
		value=str(salary_loan_relationship) + "%"
		loan_setting=LoanRequestSettings(applicant=applicant,description=description,value=value,category='ANALYSIS')
		loan_setting.save()


		description="SALARY LOAN RELATIONSHIP COMPUTED"
		value=salary_loan_relationship_computed
		loan_setting=LoanRequestSettings(applicant=applicant,description=description,value=value,category='ANALYSIS')
		loan_setting.save()

		description="LOAN AGE"
		value=str(loan_age) + " MONTHS" 
		loan_setting=LoanRequestSettings(applicant=applicant,description=description,value=value,category='ANALYSIS')
		loan_setting.save()	


		description="DATE JOINED"
		value=date_joined
		loan_setting=LoanRequestSettings(applicant=applicant,description=description,value=value,category='ANALYSIS')
		loan_setting.save()

		description="MEMBER AGE"
		value=str(members_age) + "MONTH(S)"
		loan_setting=LoanRequestSettings(applicant=applicant,description=description,value=value,category='ANALYSIS')
		loan_setting.save()

		description="LOAN INTEREST RATE"
		value=str(interest_rate) + "%"
		loan_setting=LoanRequestSettings(applicant=applicant,description=description,value=value,category='ANALYSIS')
		loan_setting.save()		


		description="INTEREST DEDUCTION"
		value=interest_deduction
		loan_setting=LoanRequestSettings(applicant=applicant,description=description,value=value,category='ANALYSIS')
		loan_setting.save()


		description="LOAN INTEREST"
		value=interest
		loan_setting=LoanRequestSettings(applicant=applicant,description=description,value=value,category='ANALYSIS')
		loan_setting.save()

		description="AMOUNT SCHEDULED"
		value=amount_scheduled
		loan_setting=LoanRequestSettings(applicant=applicant,description=description,value=value,category='ANALYSIS')
		loan_setting.save()


		description="MONTHLY REPAYMENT"
		value= round(float(monthly_repayment), 2) 
		# value= '{0:.2f}'.format(monthly_repayment) 
		loan_setting=LoanRequestSettings(applicant=applicant,description=description,value=value,category='ANALYSIS')
		loan_setting.save()

		description="LOAN BASED SAVINGS"
		value=loan_based_saving.savings.name
		loan_setting=LoanRequestSettings(applicant=applicant,description=description,value=value,category='ANALYSIS')
		loan_setting.save()

		description="LOAN BASED SAVINGS RATE"
		value=str(loan_based_saving_rating) + "%"
		loan_setting=LoanRequestSettings(applicant=applicant,description=description,value=value,category='ANALYSIS')
		loan_setting.save()



		description="MEMBER STATUS"
		value=Member_Status
		loan_setting=LoanRequestSettings(applicant=applicant,description=description,value=value,category='SUMMARY')
		loan_setting.save()


		description="EXCLUSIVE STATUS"
		value=exclusive
		loan_setting=LoanRequestSettings(applicant=applicant,description=description,value=value,category='SUMMARY')
		loan_setting.save()

		description="SAME LOAN TYPE"
		value=same_type_loan
		loan_setting=LoanRequestSettings(applicant=applicant,description=description,value=value,category='SUMMARY')
		loan_setting.save()

		description="SALARY STATUS"
		value=salary_status
		loan_setting=LoanRequestSettings(applicant=applicant,description=description,value=value,category='SUMMARY')
		loan_setting.save()

		description="LOAN SAVINGS BASED STATUS"
		value=loan_savings_status
		loan_setting=LoanRequestSettings(applicant=applicant,description=description,value=value,category='SUMMARY')
		loan_setting.save()


		return HttpResponseRedirect(reverse('loan_request_search'))


	if exclusive.title=="NON EXCLUSIVE":
	
		button_enabled=False
		if Member_Status == True and same_type_loan==False and salary_status==True and loan_savings_status==True:
			button_enabled=True
	else:
		button_enabled=True

	context={
	# 'form':form,
	'loan_type':loan_type,
	'exclusive':exclusive,
	'applicant':applicant,
	'loan_amount':loan_amount,
	'total_savings':total_savings,
	'total_loans':total_loans,
	'certification_officers':certification_officers,
	'shop_balance':shop_balance,
	'records_amount':records_amount,
	'gross_pay':gross_pay,
	'total_debit':total_debit,
	'balance':balance,
	'pk':pk,
	'duration':duration,
	'salary_loan_relationship':salary_loan_relationship,
	'salary_loan_relationship_computed':salary_loan_relationship_computed,
	'salary_status':salary_status,
	'interest_rate':interest_rate,
	'interest_deduction':interest_deduction,
	'interest':interest,
	'monthly_repayment':monthly_repayment,
	'loan_age':loan_age,
	'members_age':members_age,
	'date_joined':date_joined,
	'amount_scheduled':amount_scheduled,
	'same_type_loan':same_type_loan,
	'Member_Status':Member_Status,
	'loan_based_saving':loan_based_saving,
	'loan_based_saving_rating':loan_based_saving_rating,
	'loan_savings_status':loan_savings_status,
	'button_enabled':button_enabled,
	'DataCapture':DataCapture,
	}

	return render(request,'deskofficer_templates/loan_request_preview.html',context)




def loan_request_approved_list_load(request):
	DataCapture=DataCaptureManager.objects.first()
	transaction_status=TransactionStatus.objects.get(title='UNTREATED')
	approval_status=ApprovalStatus.objects.get(title='APPROVED')
	applicants=LoanRequest.objects.filter(approval_status=approval_status,transaction_status=transaction_status)
	context={
	'applicants':applicants,
	'DataCapture':DataCapture,
	}
	return render(request,'deskofficer_templates/loan_request_approved_list_load.html',context)


def loan_request_approved_list_form_sales(request,pk):
	DataCapture=DataCaptureManager.objects.first()
	loan=LoanRequest.objects.get(id=pk)
	loan_amount=loan.approved_amount
	admin_charges_minimum = loan.loan.admin_charges_minimum

	if float(loan_amount)> float(admin_charges_minimum):
		if loan.loan.admin_charges_rating.title == 'PERCENTAGE':
			rate=loan.loan.admin_charges
			admin_charge= float(rate)/100 * float(loan_amount)

		else:
			admin_charge= loan.loan.admin_charges
	else:
		admin_charge= loan.loan.default_admin_charges

	form = loan_request_approved_list_form_sales_form(request.POST or None)
	form.fields['amount'].initial=admin_charge

	if request.method == "POST":
		transaction_status=TransactionStatus.objects.get(title='TREATED')
		receipt_no_id = request.POST.get('receipt')
		if Receipts.objects.filter(receipt=receipt_no_id).exists():
			receipt_obj = Receipts.objects.get(receipt=receipt_no_id)
			receipt=receipt_obj.receipt
		else:
			messages.error(request,'Receipt do not exist')
			return HttpResponseRedirect(reverse('loan_request_approved_list_form_sales',args=(pk,)))

		record = LoanFormIssuance(applicant=loan,receipt=receipt,admin_charge=admin_charge)
		record.save()

		loan.transaction_status=transaction_status
		loan.save()

		receipt_status=ReceiptStatus.objects.get(title='USED')
		receipt_obj.status=receipt_status
		receipt_obj.save()
		return HttpResponseRedirect(reverse('loan_request_approved_list_load'))
	context={
	'form':form,
	'loan':loan,

	'DataCapture':DataCapture,
	}
	return render(request,'deskofficer_templates/loan_request_approved_list_form_sales.html',context)


def loan_application_list_load(request):
	DataCapture=DataCaptureManager.objects.first()
	processing_status=ProcessingStatus.objects.get(title="UNPROCESSED")
	applicants=LoanFormIssuance.objects.filter(processing_status=processing_status)

	context={
	'applicants':applicants,
	'DataCapture':DataCapture,
	}
	return render(request,'deskofficer_templates/loan_application_list_load.html',context)


def loan_application_processing(request,pk):
	DataCapture=DataCaptureManager.objects.first()
	status=MembershipStatus.objects.get(title="ACTIVE")
	applicant=LoanFormIssuance.objects.get(id=pk)
	total_guarantors=applicant.applicant.loan.guarantors

	noks=MembersNextOfKins.objects.filter(member_id=applicant.applicant.member_id)
	bank_accounts=MembersBankAccounts.objects.filter(member_id=applicant.applicant.member_id)
	guarantors=Members.objects.filter(status=status).exclude(id=applicant.applicant.member_id)
	

	loan_settings=LoanRequestSettings.objects.filter(applicant=applicant.applicant)

	seleected_guarantors=[]
	new_loan=[]
	new_amount=0
	loan_pk=0

	if LoanApplication.objects.filter(applicant=applicant).exists():
		
		new_loan=LoanApplication.objects.filter(applicant=applicant).first()
		
		new_amount=new_loan.loan_amount
		loan_pk=new_loan.pk

		seleected_guarantors=LoanApplicationGuarnators.objects.filter(applicant=new_loan)
		
		print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
		print(seleected_guarantors)
	

	if  request.method =='POST' and 'application' in request.POST:
		
		exist_amount=request.POST.get('loan_amount')
		new_amount=request.POST.get('loan_new_amount')
		
		if float(new_amount)<=0:
			messages.error(request,'Invalid Loan Amount Specification')
			return HttpResponseRedirect(reverse('loan_application_processing', args=(pk,)))

		if float(exist_amount) < float(new_amount):
			messages.error(request,'You cannot apply for Amount beyond your initial request')
			return HttpResponseRedirect(reverse('loan_application_processing', args=(pk,)))
		

		if LoanApplication.objects.filter(applicant=applicant).exists():
			record=LoanApplication.objects.get(applicant=applicant)
			record.loan_amount=new_amount
			record.save()
			return HttpResponseRedirect(reverse('loan_application_processing', args=(pk,)))

		record=LoanApplication(applicant=applicant,loan_amount=new_amount)
		record.save()
		return HttpResponseRedirect(reverse('loan_application_processing', args=(pk,)))

	
	if request.method=="POST" and 'btn_nok' in request.POST:
		record=LoanApplication.objects.get(applicant=applicant)
		nok_id=request.POST.get('nok')
		if nok_id == None:
			messages.info(request,'Please no Next of Kin found for this Applicant')
			return HttpResponseRedirect(reverse('loan_application_processing', args=(pk,)))

		nok=MembersNextOfKins.objects.get(id=nok_id)

		record.nok=nok
		record.save()
		messages.success(request,'Next of Kin Updated Successfully')
		return HttpResponseRedirect(reverse('loan_application_processing', args=(pk,)))

	
	if request.method=='POST' and 'btn_guarantor' in request.POST:
		
		if total_guarantors==0:
			messages.error(request,'Total numbers of Gaurantors not set')
			return HttpResponseRedirect(reverse('loan_application_processing', args=(pk,)))
	

		if LoanApplicationGuarnators.objects.filter(applicant=new_loan).count() >= total_guarantors:
			messages.error(request,'You Have added the required Guarantors')
			return HttpResponseRedirect(reverse('loan_application_processing', args=(pk,)))
		

		guarantor_id=request.POST.get('guarantor')
		guarantor=Members.objects.get(id=guarantor_id)

		if LoanApplicationGuarnators.objects.filter(applicant=new_loan,guarantor=guarantor).exists():
			messages.error(request,'This Member is already added as a Guarantors')
			return HttpResponseRedirect(reverse('loan_application_processing', args=(pk,)))
		
		if float(applicant.applicant.member.gross_pay)>float(guarantor.gross_pay):
			messages.info(request,"Guarantor Gross Pay cannot be less than the Applicant's Gross Pay")
			return HttpResponseRedirect(reverse('loan_application_processing', args=(pk,)))

		record=LoanApplicationGuarnators(applicant=new_loan,guarantor=guarantor)
		record.save()

		messages.success(request,'Guarantor added Successfully')
		return HttpResponseRedirect(reverse('loan_application_processing', args=(pk,)))

	if request.method=='POST' and 'btn_account' in request.POST:
		account_id=request.POST.get('account')
		account=MembersBankAccounts.objects.get(id=account_id)
		
		record=LoanApplication.objects.get(applicant=applicant)
		record.bank_account=account
		record.save()
		messages.success(request,'Bank Account Details Added Successfully')
		return HttpResponseRedirect(reverse('loan_application_processing', args=(pk,)))


	form=loan_application_processing_form(request.POST or None)
	form.fields['loan_type'].initial=applicant.applicant.loan.name
	form.fields['loan_amount'].initial=applicant.applicant.approved_amount
	form.fields['loan_new_amount'].initial=applicant.applicant.approved_amount

	if LoanApplication.objects.filter(applicant=applicant).exists():
		form.fields['loan_new_amount'].initial=new_amount
	context={
	'form':form,
	'applicant':applicant,
	'loan_settings':loan_settings,
	'loan_pk':loan_pk,
	'new_amount':new_amount,
	'new_loan':new_loan,
	'noks':noks,
	'guarantors':guarantors,
	'bank_accounts':bank_accounts,
	'seleected_guarantors':seleected_guarantors,
	'DataCapture':DataCapture,
	}
	return render(request,'deskofficer_templates/loan_application_processing.html',context)




def loan_application_preview(request,pk):
	DataCapture=DataCaptureManager.objects.first()
	submission_status=SubmissionStatus.objects.get(title="SUBMITTED")

	applicant=LoanApplication.objects.get(id=pk)
	gross_pay=applicant.applicant.applicant.member.gross_pay

	nok=LoanApplication.objects.exclude(Q(nok__isnull=True)).filter(id=pk)
	if nok:
		nok_status=True
	else:
		nok_status=False


	bank_account=LoanApplication.objects.exclude(Q(bank_account__isnull=True)).filter(id=pk)
	if bank_account:
		bank_account_status=True
	else:
		bank_account_status=False


	guarantor_list=[]
	try:
		guarantors=LoanApplicationGuarnators.objects.filter(applicant=applicant)
		for guarantor in guarantors:
			small_guarantor=(guarantor.id,guarantor.guarantor.admin.first_name + " " + guarantor.guarantor.admin.last_name + " " + guarantor.guarantor.middle_name)
			guarantor_list.append(small_guarantor)
	except:
		guarantor_list=[]

	total_guarantors=applicant.applicant.applicant.loan.guarantors

	if len(guarantor_list)==total_guarantors:
		guarnator_status=True
	else:
		guarnator_status=False


	loan_based_saving = LoanBasedSavings.objects.first()
	
	savings_saved=0
	if StandingOrderAccounts.objects.filter(transaction=loan_based_saving.savings,member=applicant.applicant.applicant.member).exists():
		account_id=StandingOrderAccounts.objects.get(transaction=loan_based_saving.savings,member=applicant.applicant.applicant.member)
	
		savings_ledger=PersonalLedger.objects.filter(account_number=account_id.account_number).last()
		savings_saved=savings_ledger.balance
		

	loan_based_saving_rating=applicant.applicant.applicant.loan.savings_rate

	
	

	loan_saving_relationship=float(int(loan_based_saving_rating)/100) * float(applicant.loan_amount)
	



	loan_savings_status=False
	if float(savings_saved) > float(loan_saving_relationship) :
		loan_savings_status=True

	
	total_savings=0
	savings_sum=StandingOrderAccounts.objects.filter(member_id=applicant.applicant.applicant.member_id).aggregate(total_amount=Sum('amount'))
	total_savings=savings_sum['total_amount']
	if total_savings==None:
		total_savings=0



	total_loans=0
	loans_sum=LoansRepaymentBase.objects.filter(Q(balance__lt=0) & Q(member_id=applicant.applicant.applicant.member_id)).aggregate(total_amount=Sum('repayment'))
	total_loans=loans_sum['total_amount']
	if total_loans==None:
		total_loans=0

	


	shop_balance=0
	shops =CooperativeShopLedger.objects.filter(Q(balance__lt=0) & Q(member_id=applicant.applicant.applicant.member_id)).order_by('-id').first()
	if shops:
		shop_balance=abs(shops.balance)

	ex_status=TransactionStatus.objects.get(title="UNTREATED")
	records_amount=0
	records_amount_sum=ExternalFascilitiesMain.objects.filter(member__member_id=applicant.applicant.applicant.member_id,status=ex_status).aggregate(total_amount=Sum('member__amount'))
	records_amount=records_amount_sum['total_amount']
	if records_amount==None:
		records_amount=0

	
	total_debit=float(total_savings)+float(total_loans)+float(shop_balance)+ float(records_amount)


	
	balance=float(gross_pay)-total_debit
		
	date_joined = applicant.applicant.applicant.member.date_joined
	now = datetime.datetime.now()
	

	same_type_loan=False
	if LoansDisbursed.objects.filter(Q(balance__gt=0) & Q(member_id=applicant.applicant.applicant.member_id) & Q(transaction_id=applicant.applicant.applicant.loan_id)).exists():
		same_type_loan=True


	loan_type=applicant.applicant.applicant.loan.name
	loan_amount=applicant.loan_amount
	duration = applicant.applicant.applicant.loan.duration


	salary_loan_relationship = applicant.applicant.applicant.loan.salary_loan_relationship
	salary_loan_relationship_computed= float(int(salary_loan_relationship)/100) * float(balance)

	interest_rate = applicant.applicant.applicant.loan.interest_rate
	interest= float(int(interest_rate)/100) * float(applicant.loan_amount)
	loan_age = applicant.applicant.applicant.loan.loan_age
	members_age = (now.year - date_joined.year) * 12 + (now.month - date_joined.month)
	interest_deduction=applicant.applicant.applicant.loan.interest_deduction

	if interest_deduction.title == "SOURCE":
		amount_scheduled = float(loan_amount)
	else:
		amount_scheduled = float(loan_amount)+ float(interest)

	part1= float(amount_scheduled)//float(duration)
	part2= float(amount_scheduled)%float(duration)

	if int(part2) >= 1:
		monthly_repayment='{0:.2f}'.format(float(part1)+ 1)
	else:
		monthly_repayment='{0:.2f}'.format(float(part1))
	

	salary_status=True
	if float(monthly_repayment)> float(salary_loan_relationship_computed):
		salary_status=False

	Member_Status = False
	if int(members_age)>int(loan_age):
		Member_Status = True

	exclusive=applicant.applicant.applicant.member.exclusive_status


	certification_officers=CertificationOfficers.objects.filter(transaction__transaction_id=applicant.applicant.applicant.loan_id)


	if request.method=="POST":
		
		comment=request.POST.get("comment")
		officer_id=request.POST.get("officer")
		officer=CertificationOfficers.objects.get(id=officer_id)
		
		applicant.certification_officer=officer
		applicant.comment=comment
		applicant.submission_status=submission_status
		applicant.save()

		description="GROSS PAY"
		value=gross_pay
		loan_setting=LoanApplicationSettings(applicant=applicant,description=description,value=value,category='ANALYSIS')
		loan_setting.save()
		

		description="SALARY BALANCE AFTER DEDUCTIONS"
		value=balance
		loan_setting=LoanApplicationSettings(applicant=applicant,description=description,value=value,category='ANALYSIS')
		loan_setting.save()

		description=loan_type
		value=loan_amount
		loan_setting=LoanApplicationSettings(applicant=applicant,description=description,value=value,category='ANALYSIS')
		loan_setting.save()

		description="MONTHLY DEDUCTIONS"
		value=total_savings
		loan_setting=LoanApplicationSettings(applicant=applicant,description=description,value=value,category='ANALYSIS')
		loan_setting.save()

		description="OUTSTANDING MONTHLY LOAN REPAYMENTS"		
		value='{0:.2f}'.format(total_loans) 
		loan_setting=LoanApplicationSettings(applicant=applicant,description=description,value=value,category='ANALYSIS')
		loan_setting.save()

		description="COOPERATIVE SHOP"
		value=shop_balance
		loan_setting=LoanApplicationSettings(applicant=applicant,description=description,value=value,category='ANALYSIS')
		loan_setting.save()

		description="EXTERNAL FASCILITIES"
		value=records_amount
		loan_setting=LoanApplicationSettings(applicant=applicant,description=description,value=value,category='ANALYSIS')
		loan_setting.save()

		description="LOAN DURATION"
		value=str(duration) + " MONTHS"
		loan_setting=LoanApplicationSettings(applicant=applicant,description=description,value=value,category='ANALYSIS')
		loan_setting.save()

		description="SALARY LOAN RELATIONSHIP"
		value=str(salary_loan_relationship) + "%"
		loan_setting=LoanApplicationSettings(applicant=applicant,description=description,value=value,category='ANALYSIS')
		loan_setting.save()


		description="SALARY LOAN RELATIONSHIP COMPUTED"
		value=salary_loan_relationship_computed
		loan_setting=LoanApplicationSettings(applicant=applicant,description=description,value=value,category='ANALYSIS')
		loan_setting.save()

		description="LOAN AGE"
		value=str(loan_age) + " MONTHS" 
		loan_setting=LoanApplicationSettings(applicant=applicant,description=description,value=value,category='ANALYSIS')
		loan_setting.save()	


		description="DATE JOINED"
		value=date_joined
		loan_setting=LoanApplicationSettings(applicant=applicant,description=description,value=value,category='ANALYSIS')
		loan_setting.save()

		description="MEMBER AGE"
		value=str(members_age) + "MONTH(S)"
		loan_setting=LoanApplicationSettings(applicant=applicant,description=description,value=value,category='ANALYSIS')
		loan_setting.save()

		description="LOAN INTEREST RATE"
		value=str(interest_rate) + "%"
		loan_setting=LoanApplicationSettings(applicant=applicant,description=description,value=value,category='ANALYSIS')
		loan_setting.save()		


		description="INTEREST DEDUCTION"
		value=interest_deduction
		loan_setting=LoanApplicationSettings(applicant=applicant,description=description,value=value,category='ANALYSIS')
		loan_setting.save()


		description="LOAN INTEREST"
		value=interest
		loan_setting=LoanApplicationSettings(applicant=applicant,description=description,value=value,category='ANALYSIS')
		loan_setting.save()

		description="AMOUNT SCHEDULED"
		value=amount_scheduled
		loan_setting=LoanApplicationSettings(applicant=applicant,description=description,value=value,category='ANALYSIS')
		loan_setting.save()


		description="MONTHLY REPAYMENT"
		value=round(float(monthly_repayment),2)
		loan_setting=LoanApplicationSettings(applicant=applicant,description=description,value=value,category='ANALYSIS')
		loan_setting.save()

		description="LOAN BASED SAVINGS"
		value=loan_based_saving.savings.name
		loan_setting=LoanApplicationSettings(applicant=applicant,description=description,value=value,category='ANALYSIS')
		loan_setting.save()

		description="LOAN BASED SAVINGS RATE"
		value=str(loan_based_saving_rating) + "%"
		loan_setting=LoanApplicationSettings(applicant=applicant,description=description,value=value,category='ANALYSIS')
		loan_setting.save()
		
		description="Guarantors"
		value=guarantor_list
		loan_setting=LoanApplicationSettings(applicant=applicant,description=description,value=value,category='ANALYSIS')
		loan_setting.save()

		

		description="Bank Details"
		value=applicant.bank_account.account_name + " - " + applicant.bank_account.account_number + ' - ' + applicant.bank_account.bank.title
		loan_setting=LoanApplicationSettings(applicant=applicant,description=description,value=value,category='ANALYSIS')
		loan_setting.save()

		description="Next of Kin"
		value=applicant.nok.name + " - " + applicant.nok.relationships.title
		loan_setting=LoanApplicationSettings(applicant=applicant,description=description,value=value,category='ANALYSIS')
		loan_setting.save()
		


		description="MEMBER STATUS"
		value=Member_Status
		loan_setting=LoanApplicationSettings(applicant=applicant,description=description,value=value,category='SUMMARY')
		loan_setting.save()


		description="EXCLUSIVE STATUS"
		value=exclusive
		loan_setting=LoanApplicationSettings(applicant=applicant,description=description,value=value,category='SUMMARY')
		loan_setting.save()

		description="SAME LOAN TYPE"
		value=same_type_loan
		loan_setting=LoanApplicationSettings(applicant=applicant,description=description,value=value,category='SUMMARY')
		loan_setting.save()

		description="SALARY STATUS"
		value=salary_status
		loan_setting=LoanApplicationSettings(applicant=applicant,description=description,value=value,category='SUMMARY')
		loan_setting.save()

		description="LOAN SAVINGS BASED STATUS"
		value=loan_savings_status
		loan_setting=LoanApplicationSettings(applicant=applicant,description=description,value=value,category='SUMMARY')
		loan_setting.save()
		
		description="NOK Status"
		value=nok_status
		loan_setting=LoanApplicationSettings(applicant=applicant,description=description,value=value,category='SUMMARY')
		loan_setting.save()
		
		description="Bank Account Status"
		value=bank_account_status
		loan_setting=LoanApplicationSettings(applicant=applicant,description=description,value=value,category='SUMMARY')
		loan_setting.save()

		description="Guarantors Status"
		value=guarnator_status
		loan_setting=LoanApplicationSettings(applicant=applicant,description=description,value=value,category='SUMMARY')
		loan_setting.save()



		processing_status=ProcessingStatus.objects.get(title="PROCESSED")
		applicant1=LoanFormIssuance.objects.get(id=applicant.applicant_id)
		applicant1.processing_status=processing_status
		applicant1.save()


		return HttpResponseRedirect(reverse('loan_application_list_load'))


	if exclusive.title=="NON EXCLUSIVE":
		button_enabled=False
		
		if Member_Status == True and same_type_loan==False and salary_status==True and loan_savings_status==True:
		
			if guarnator_status and  nok_status and bank_account_status:
				button_enabled=True
			else:
				button_enabled=False
	else:
		if guarnator_status and  nok_status and bank_account_status:
			button_enabled=True
		else:
			button_enabled=False


	context={
	'loan_type':loan_type,
	'exclusive':exclusive,
	'applicant':applicant,
	'loan_amount':loan_amount,
	'total_savings':total_savings,
	'total_loans':total_loans,
	'certification_officers':certification_officers,
	'shop_balance':shop_balance,
	'records_amount':records_amount,
	'gross_pay':gross_pay,
	'total_debit':total_debit,
	'balance':balance,
	'pk':pk,
	'duration':duration,
	'salary_loan_relationship':salary_loan_relationship,
	'salary_loan_relationship_computed':salary_loan_relationship_computed,
	'salary_status':salary_status,
	'interest_rate':interest_rate,
	'interest_deduction':interest_deduction,
	'interest':interest,
	'monthly_repayment':monthly_repayment,
	'loan_age':loan_age,
	'members_age':members_age,
	'date_joined':date_joined,
	'amount_scheduled':amount_scheduled,
	'same_type_loan':same_type_loan,
	'Member_Status':Member_Status,
	'loan_based_saving':loan_based_saving,
	'loan_based_saving_rating':loan_based_saving_rating,
	'loan_savings_status':loan_savings_status,
	'button_enabled':button_enabled,
	'guarantors':guarantors,
	'guarantor_list':guarantor_list,
	'guarnator_status':guarnator_status,
	'nok_status':nok_status,
	'bank_account_status':bank_account_status,
	'DataCapture':DataCapture,
	}

	return render(request,'deskofficer_templates/loan_application_preview.html',context)



def loan_application_approved_list_load(request):
	DataCapture=DataCaptureManager.objects.first()
	transaction_status=TransactionStatus.objects.get(title='UNTREATED')
	approval_status=ApprovalStatus.objects.get(title='APPROVED')
	applicants=LoanApplication.objects.filter(approval_status=approval_status,transaction_status=transaction_status)
	context={
	'applicants':applicants,
	'DataCapture':DataCapture,
	}
	return render(request,'deskofficer_templates/loan_application_approved_list_load.html',context)



def loan_application_approved_process_preview(request,pk):
	DataCapture=DataCaptureManager.objects.first()
	form=loan_application_approved_process_preview__form(request.POST or None)
	transaction_period=TransactionPeriods.objects.get(status__title='ACTIVE')

	applicant=LoanApplication.objects.get(id=pk)
	records=LoanApplicationSettings.objects.filter(applicant=applicant)

	loan_type=applicant.applicant.applicant.loan.name
	loan_amount=applicant.loan_amount
	duration = applicant.applicant.applicant.loan.duration

	interest_rate = applicant.applicant.applicant.loan.interest_rate
	interest= float(int(interest_rate)/100) * float(applicant.loan_amount)
	
	interest_deduction=applicant.applicant.applicant.loan.interest_deduction

	if interest_deduction.title == "SOURCE":
		amount_scheduled = float(loan_amount)
	else:
		amount_scheduled = float(loan_amount)+ float(interest) 

	part1= float(amount_scheduled)//float(duration)
	part2= float(amount_scheduled)%float(duration)

	if int(part2) >= 1:
		monthly_repayment='{0:.2f}'.format(float(part1)+ 1)
	else:
		monthly_repayment='{0:.2f}'.format(float(part1))

	now = datetime.datetime.now()

	member_id=list((applicant.applicant.applicant.member.member_id).split("/"))
	
	my_id=member_id[2]
	
	loan_code=applicant.applicant.applicant.loan.code
	loan_number_selector_id=LoanNumber.objects.first()
	loan_number_selector=loan_number_selector_id.code

	current_time= str(now.year) + str(now.month) + str(now.day) + str(now.hour) + str(now.minute)  
	loan_number=str(loan_code) + str(my_id) + str(current_time) + str(loan_number_selector).zfill(5)
	loan_number_selector_id.code=int(loan_number_selector)+1
	loan_number_selector_id.save()

	if request.method=="POST":
		member=applicant.applicant.applicant.member
		

		transaction_status=TransactionStatus.objects.get(title='TREATED')
		start_date=request.POST.get('effective_date')
	
		start_date=datetime.datetime.strptime(start_date, '%Y-%m-%d')
	
		stop_date = start_date+ relativedelta(months=int(duration))
		

		status=MembershipStatus.objects.get(title='ACTIVE')
		processed_by=CustomUser.objects.get(id=request.user.id)

		
		transaction=applicant.applicant.applicant.loan
		if LoansRepaymentBase.objects.filter(Q(balance__lt=0)).filter(member=member,transaction=transaction).exists():
			
			loan_exist=LoansRepaymentBase.objects.filter(Q(balance__lt=0)).filter(member=member,transaction=transaction).first()
			

			loan_exist_balance=loan_exist.balance
			loan_exist_repayment=loan_exist.repayment
			loan_exist_loan_number=loan_exist.loan_number
			
			loan_exist_ledger=PersonalLedger.objects.filter(account_number=loan_exist_loan_number).last()
			loan_exist_ledger_balance=loan_exist_ledger.balance
			
			particulars=  "MERGED WITH  "  + str(loan_number)  + " WITH A BALANCE OF " +  str(abs(amount_scheduled))
			debit=0
			credit=abs(float(loan_exist_ledger_balance))
			balance=0

			record=PersonalLedger(member=member,transaction=transaction,account_number=loan_exist_loan_number,particulars=particulars,debit=debit,credit=credit,balance=balance,transaction_period=now,status=status)
			record.save()

			particulars=transaction.name + " ADDITIONAL LOAN ISSUANCE"
			debit=abs(float(loan_amount)) #+float(interest))
			credit=0
			balance=-debit

			record=PersonalLedger(member=member,transaction=transaction,account_number=loan_number,particulars=particulars,debit=debit,credit=credit,balance=balance,transaction_period=now,status=status)
			record.save()		

			particulars=  "INTEREST ON "  + transaction.name
			debit=abs(float(interest))
			credit=0
			balance=-(abs(float(balance)) + abs(float(interest)))

			record=PersonalLedger(member=member,transaction=transaction,account_number=loan_number,particulars=particulars,debit=debit,credit=credit,balance=balance,transaction_period=now,status=status)
			record.save()

			if interest_deduction.title == "SOURCE":
				particulars= "INTEREST DEDUCTION AT SOURCE"
				debit=0
				credit=float(interest)
				balance=-abs(float(loan_amount))

				record=PersonalLedger(member=applicant.applicant.applicant.member,transaction=transaction,account_number=loan_number,particulars=particulars,debit=debit,credit=credit,balance=balance,transaction_period=now,status=status)
				record.save()

				record=LoansDisbursed(start_date=start_date,stop_date=stop_date,member=member,transaction=transaction,duration=duration,interest_rate=interest_rate,interest_deduction=interest_deduction.title,loan_number=loan_number,loan_amount=amount_scheduled,repayment=float(monthly_repayment),balance=-amount_scheduled,processed_by=processed_by,status=status)
				record.save()		

			else:

				record=LoansDisbursed(start_date=start_date,stop_date=stop_date,member=member,transaction=transaction,duration=duration,interest_rate=interest_rate,interest_deduction=interest_deduction.title,loan_number=loan_number,loan_amount=amount_scheduled,repayment=float(monthly_repayment),balance=-amount_scheduled,processed_by=processed_by,status=status)
				record.save()		

			particulars=  "MERGED WITH  "  + str(loan_exist_loan_number)  + " WITH A BALANCE OF " +  str(abs(loan_exist_ledger_balance))
			debit=0
			credit=abs(float(loan_amount))+ abs(float(interest))
			balance=0

			record=PersonalLedger(member=member,transaction=transaction,account_number=loan_number,particulars=particulars,debit=debit,credit=credit,balance=balance,transaction_period=now,status=status)
			record.save()

			record_status=MembershipStatus.objects.get(title='INACTIVE')
			PersonalLedger.objects.filter(account_number=loan_exist_loan_number).update(status=record_status)
			PersonalLedger.objects.filter(account_number=loan_number).update(status=record_status)
			
			loan_exist.status=record_status
			loan_exist.save()

			my_id=member_id[2]
		
			loan_code=applicant.applicant.applicant.loan.code
			loan_number_selector_id=LoanNumber.objects.first()
			loan_number_selector=loan_number_selector_id.code

			current_time= str(now.year) + str(now.month) + str(now.day) + str(now.hour) + str(now.minute)  
			loan_number1=str(loan_code) + str(my_id) + str(current_time) + str(loan_number_selector).zfill(5)
			
			loan_number_selector_id.code=int(loan_number_selector)+1
			loan_number_selector_id.save()


			new_repayment=float(loan_exist_repayment) + float(monthly_repayment)

			particulars=  "MERGED LOANS: " + str(loan_exist_loan_number) + '(' + str(abs(loan_exist_ledger_balance)) + ')'  + ' AND ' + str(loan_number) + '(' + str(abs(amount_scheduled)) + ')' 
			debit=abs(float(loan_exist_ledger_balance)) +  float(abs(amount_scheduled))
			credit=0
			balance=-(abs(float(loan_exist_ledger_balance)) +  float(abs(amount_scheduled)))

			record=PersonalLedger(member=member,transaction=transaction,account_number=loan_number1,particulars=particulars,debit=debit,credit=credit,balance=balance,transaction_period=now,status=status)
			record.save()

			record=LoansRepaymentBase(start_date=start_date,member=member,transaction=transaction,loan_number=loan_number1,loan_amount=abs(balance),repayment=float(new_repayment),balance=balance,processed_by=processed_by,status=status)
			record.save()

			merger_status=LoanMergeStatus.objects.get(title='MERGED')
			LoansDisbursed.objects.filter(loan_number=loan_exist.loan_number).update(loan_merge_status=merger_status,merge_account_number=loan_number1)
			LoansDisbursed.objects.filter(loan_number=loan_number).update(loan_merge_status=merger_status,merge_account_number=loan_number1)

			
			applicant.transaction_status=transaction_status
			applicant.save()
			return HttpResponseRedirect(reverse('loan_application_approved_list_load'))
		
		else:
			particulars=transaction.name + " LOAN ISSUANCE"
			debit=abs(float(loan_amount)) #+float(interest))
			credit=0
			balance=-debit

			record=PersonalLedger(member=member,transaction=transaction,account_number=loan_number,particulars=particulars,debit=debit,credit=credit,balance=balance,transaction_period=now,status=status)
			record.save()		

			particulars=  "INTEREST ON "  + transaction.name
			debit=abs(float(interest))
			credit=0
			balance=-(abs(float(balance)) + abs(float(interest)))

			record=PersonalLedger(member=member,transaction=transaction,account_number=loan_number,particulars=particulars,debit=debit,credit=credit,balance=balance,transaction_period=now,status=status)
			record.save()
			
			if interest_deduction.title == "SOURCE":
				particulars= "INTEREST DEDUCTION AT SOURCE"
				debit=0
				credit=float(interest)
				balance=-(abs(float(balance)) - float(interest))

				record=PersonalLedger(member=applicant.applicant.applicant.member,transaction=transaction,account_number=loan_number,particulars=particulars,debit=debit,credit=credit,balance=balance,transaction_period=now,status=status)
				record.save()

				record=LoansRepaymentBase(start_date=start_date,member=member,transaction=transaction,loan_number=loan_number,loan_amount=float(loan_amount) + abs(float(interest)),repayment=float(monthly_repayment),amount_paid=float(interest),balance=-amount_scheduled,processed_by=processed_by,status=status)
				record.save()

				record=LoansDisbursed(start_date=start_date,stop_date=stop_date,member=member,transaction=transaction,duration=duration,interest_rate=interest_rate,interest_deduction=interest_deduction.title,loan_number=loan_number,loan_amount=float(loan_amount) + abs(float(interest)),repayment=float(monthly_repayment),amount_paid=float(interest),balance=-amount_scheduled,processed_by=processed_by,status=status)
				record.save()	

			else:

				record=LoansRepaymentBase(start_date=start_date,member=member,transaction=transaction,loan_number=loan_number,loan_amount=amount_scheduled,repayment=float(monthly_repayment),balance=-amount_scheduled,processed_by=processed_by,status=status)
				record.save()

				record=LoansDisbursed(start_date=start_date,stop_date=stop_date,member=member,transaction=transaction,duration=duration,interest_rate=interest_rate,interest_deduction=interest_deduction.title,loan_number=loan_number,loan_amount=amount_scheduled,repayment=float(monthly_repayment),balance=-amount_scheduled,processed_by=processed_by,status=status)
				record.save()		

			applicant.transaction_status=transaction_status
			applicant.save()

			return HttpResponseRedirect(reverse('loan_application_approved_list_load'))

	form.fields['effective_date'].initial=transaction_period.transaction_period
	context={
	'loan_type':loan_type,
	'applicant':applicant,
	'loan_amount':loan_amount,
	'pk':pk,
	'duration':duration,
	'interest_rate':interest_rate,
	'interest_deduction':interest_deduction,
	'interest':interest,
	'monthly_repayment':monthly_repayment,
	'amount_scheduled':amount_scheduled,
	'records':records,
	'form':form,
	'DataCapture':DataCapture,
	}

	return render(request,'deskofficer_templates/loan_application_approved_process_preview.html',context)




#########################################################
############### TRANSACTION PERIOD MANAGER  ###############
#########################################################
def TransactionPeriodManager(request):
	DataCapture=DataCaptureManager.objects.first()
	status=MembershipStatus.objects.get(title='INACTIVE')
	records=TransactionPeriods.objects.all().order_by('transaction_period')
	form=TransactionPeriod_form(request.POST or None)
	if request.method=="POST":
		transaction_period=request.POST.get('transaction_period')
		record=TransactionPeriods(transaction_period=transaction_period,status=status)
		record.save()
		return HttpResponseRedirect(reverse('TransactionPeriodManager'))
	form.fields['transaction_period'].initial=now
	context={
	'form':form,
	'records':records,
	'DataCapture':DataCapture,
	}
	return render(request,'deskofficer_templates/TransactionPeriodManager.html',context)


def TransactionPeriodsUpdate(request,pk):
	status=MembershipStatus.objects.get(title='ACTIVE')
	status1=MembershipStatus.objects.get(title='INACTIVE')
	all_record_update=TransactionPeriods.objects.all().update(status=status1)
	
	record=TransactionPeriods.objects.get(id=pk)
	record.status=status
	record.save()
	return HttpResponseRedirect(reverse('TransactionPeriodManager'))


#########################################################
############### MONTHLY DEDUCTIONS SECTION  ###############
#########################################################
def Monthly_Deduction_Salary_Institution_Load(request):
	DataCapture=DataCaptureManager.objects.first()
	status=MembershipStatus.objects.get(title='ACTIVE')
	transaction_period=TransactionPeriods.objects.get(status=status)
	items=SalaryInstitution.objects.all()
	context={
	'items':items,
	'transaction_period':transaction_period,
	'DataCapture':DataCapture,
	}
	return render(request,'deskofficer_templates/Monthly_Deduction_Salary_Institution_Load.html',context)


def Monthly_Individual_Transactions_Load(request,pk):
	DataCapture=DataCaptureManager.objects.first()
	source1=TransactionSources.objects.get(title='SAVINGS')
	source2=TransactionSources.objects.get(title='LOAN')

	status=MembershipStatus.objects.get(title='ACTIVE')
	transaction_period=TransactionPeriods.objects.get(status=status)

	transactions1=TransactionTypes.objects.filter(source=source1)
	transactions2=TransactionTypes.objects.filter(source=source2)

	salary_institution=SalaryInstitution.objects.get(id=pk)
	
	generated_transactions=MonthlyGeneratedTransactions.objects.filter(transaction_period=transaction_period)

	context={
	'transactions1':transactions1,
	'transactions2':transactions2,
	'transaction_period':transaction_period,
	'salary_institution':salary_institution,
	'generated_transactions':generated_transactions,
	'DataCapture':DataCapture,
	}
	return render(request,'deskofficer_templates/Monthly_Individual_Transactions_Load.html',context)



def Monthly_Savings_Contribution_preview(request,pk, salary_inst_key):
	DataCapture=DataCaptureManager.objects.first()
	status=MembershipStatus.objects.get(title='ACTIVE')
	transaction_period=TransactionPeriods.objects.get(status=status)

	salary_institution=SalaryInstitution.objects.get(id=salary_inst_key)

	transaction=TransactionTypes.objects.get(id=pk)
	
	members=StandingOrderAccounts.objects.filter(transaction__transaction=transaction,status=status,transaction__member__salary_institution=salary_institution)
	if members.count() == 0:
		messages.info(request,'No record found for this transaction')
		return HttpResponseRedirect(reverse('Monthly_Individual_Transactions_Load', args=(salary_inst_key)))

	record_exist=False
	if MonthlyGeneratedTransactions.objects.filter(transaction=transaction,transaction_period=transaction_period).exists():
		record_exist=True
	
	context={
	'transaction':transaction,
	'members':members,
	'transaction_period':transaction_period,
	'pk':pk,
	'members':members,
	'salary_inst_key':salary_inst_key,
	'record_exist':record_exist,
	'DataCapture':DataCapture,
	}
	return render(request,'deskofficer_templates/Monthly_Savings_Contribution_preview.html',context)


def Monthly_Savings_Contribution_Generate(request,pk,salary_inst_key):
	status=MembershipStatus.objects.get(title='ACTIVE')
	transaction_period=TransactionPeriods.objects.get(status=status)

	salary_institution=SalaryInstitution.objects.get(id=salary_inst_key)
	
	transaction=TransactionTypes.objects.get(id=pk)
	members=StandingOrderAccounts.objects.filter(transaction=transaction,status=status,member__salary_institution=salary_institution)

	if MonthlyDeductionList.objects.filter(transaction_period=transaction_period,transaction=transaction,member__salary_institution=salary_institution).exists():
		messages.error(request,"Transaction already generated")
		return HttpResponseRedirect(reverse('Monthly_Savings_Contribution_preview',args=(pk,salary_inst_key)))


	for member in members:
		record=MonthlyDeductionList(transaction_period=transaction_period,member=member.member,account_number=member.account_number,amount=member.amount,transaction=transaction)
		record.save()

	if MonthlyDeductionList.objects.filter(transaction_period=transaction_period,transaction=transaction).exists():
		processed_by=CustomUser.objects.get(id=request.user.id)
		record=MonthlyGeneratedTransactions(transaction=transaction,transaction_period=transaction_period,processed_by=processed_by)
		record.save()
	return HttpResponseRedirect(reverse('Monthly_Individual_Transactions_Load',args=(salary_inst_key,)))



def Monthly_loan_repayement_preview(request,pk, salary_inst_key):
	DataCapture=DataCaptureManager.objects.first()
	status=MembershipStatus.objects.get(title='ACTIVE')
	transaction_period=TransactionPeriods.objects.get(status=status)

	salary_institution=SalaryInstitution.objects.get(id=salary_inst_key)

	transaction=TransactionTypes.objects.get(id=pk)
	members=LoansRepaymentBase.objects.filter(transaction=transaction,status=status,member__salary_institution=salary_institution).filter(Q(balance__lt=0))
	if members.count() == 0:
		messages.info(request,'No record found for this transaction')
		return HttpResponseRedirect(reverse('Monthly_Individual_Transactions_Load', args=(salary_inst_key)))


	# if LoansRepaymentBase.objects.exclude(transaction=transaction,status=status,member__salary_institution=salary_institution).filter(Q(balance__lt=0)).exists():
	# 	messages.error(request,"No Record Found for This Transaction")
	# 	return HttpResponseRedirect(reverse('Monthly_Individual_Transactions_Load',args=(salary_inst_key,)))


	record_exist=False
	if MonthlyGeneratedTransactions.objects.filter(transaction=transaction,transaction_period=transaction_period).exists():
		record_exist=True

	context={
	'transaction':transaction,
	'members':members,
	'transaction_period':transaction_period,
	'pk':pk,
	'salary_inst_key':salary_inst_key,
	'record_exist':record_exist,
	'DataCapture':DataCapture,
	}
	return render(request,'deskofficer_templates/Monthly_loan_repayement_preview.html',context)


def Monthly_loan_repayement_Generate(request,pk, salary_inst_key):
	status=MembershipStatus.objects.get(title='ACTIVE')
	transaction_period=TransactionPeriods.objects.get(status=status)

	salary_institution=SalaryInstitution.objects.get(id=salary_inst_key)

	transaction=TransactionTypes.objects.get(id=pk)
	members=LoansRepaymentBase.objects.filter(transaction=transaction,status=status,member__salary_institution=salary_institution).filter(Q(balance__lt=0))
	
	if MonthlyDeductionList.objects.filter(transaction_period=transaction_period,transaction=transaction).exists():
		messages.error(request,"Transaction already generated")
		return HttpResponseRedirect(reverse('Monthly_loan_repayement_preview',args=(pk, salary_inst_key)))

	for member in members:
		record=MonthlyDeductionList(transaction_period=transaction_period,member=member.member,account_number=member.loan_number,amount=member.repayment,transaction=transaction)
		record.save()

	if MonthlyDeductionList.objects.filter(transaction_period=transaction_period,transaction=transaction).exists():
		processed_by=CustomUser.objects.get(id=request.user.id)
		
		record=MonthlyGeneratedTransactions(transaction=transaction,transaction_period=transaction_period,processed_by=processed_by)
		record.save()

	return HttpResponseRedirect(reverse('Monthly_Individual_Transactions_Load',args=(salary_inst_key,)))




def Monthly_Group_transaction_Institution_Load(request):
	DataCapture=DataCaptureManager.objects.first()
	status=MembershipStatus.objects.get(title='ACTIVE')
	transaction_period=TransactionPeriods.objects.get(status=status)
	items=SalaryInstitution.objects.all()
	
	records=MonthlyGroupGeneratedTransactions.objects.filter(transaction_period=transaction_period)
	context={
	'items':items,
	'transaction_period':transaction_period,
	'records':records,
	'DataCapture':DataCapture,
	}
	return render(request,'deskofficer_templates/Monthly_Group_transaction_Institution_Load.html',context)




def Monthly_Group_Generated_Transaction(request,pk):
	DataCapture=DataCaptureManager.objects.first()
	status=MembershipStatus.objects.get(title="ACTIVE")	
	transaction_period=TransactionPeriods.objects.get(status=status)
	
	salary_institution=SalaryInstitution.objects.get(id=pk)	
	if MonthlyGroupGeneratedTransactions.objects.filter(salary_institution=salary_institution,transaction_period=transaction_period).exists():
		messages.error(request,"Transaction already generated")
		return HttpResponseRedirect(reverse('Monthly_Group_transaction_Institution_Load'))

	members=Members.objects.filter(salary_institution=salary_institution,status=status)

	record_exist=False
	if Members.objects.filter(salary_institution=salary_institution,status=status).exists():
		record_exist=True

	context={
	'members':members,
	'salary_institution':salary_institution,
	'transaction_period':transaction_period,
	'record_exist':record_exist,
	'DataCapture':DataCapture,
	}
	return render(request,'deskofficer_templates/Monthly_Group_Generated_Transaction.html',context)


def Monthly_Group_Transaction_preview(request,pk):
	DataCapture=DataCaptureManager.objects.first()
	status=MembershipStatus.objects.get(title="ACTIVE")
	
	transaction_period=TransactionPeriods.objects.get(status=status)
	member=Members.objects.get(id=pk)
	
	records=MonthlyDeductionList.objects.filter(transaction_period=transaction_period,member=member)


	total_deductions=0
	
	deduction_sum=MonthlyDeductionList.objects.filter(transaction_period=transaction_period,member=member).aggregate(total_amount=Sum('amount'))
	total_deductions=deduction_sum['total_amount']


	context={
	'records':records,
	'transaction_period':transaction_period,
	'total_deductions':total_deductions,
	'DataCapture':DataCapture,
	}
	return render(request,'deskofficer_templates/Monthly_Group_Transaction_preview.html',context)



def Monthly_Group_Transaction_generate(request,pk):
	processed_by=CustomUser.objects.get(id=request.user.id)
	status=MembershipStatus.objects.get(title="ACTIVE")

	transaction_status1=TransactionStatus.objects.get(title="UNTREATED")
	transaction_status=TransactionStatus.objects.get(title="TREATED")
	transaction_period=TransactionPeriods.objects.get(status=status)
	
	salary_institution=SalaryInstitution.objects.get(id=pk)
	members=Members.objects.filter(status=status,salary_institution=salary_institution)


	for member in members:
		total_deductions=0
		
		if MonthlyDeductionList.objects.filter(transaction_period=transaction_period,member=member,transaction_status=transaction_status1).exists():
			deduction_sum=MonthlyDeductionList.objects.filter(transaction_period=transaction_period,member=member,transaction_status=transaction_status1).aggregate(total_amount=Sum('amount'))
			amount=deduction_sum['total_amount']

			record=MonthlyDeductionListGenerated(salary_institution=salary_institution,transaction_period=transaction_period,member=member,amount=amount)
			record.save()

	all_record_update=MonthlyDeductionList.objects.filter(transaction_period=transaction_period).update(transaction_status=transaction_status)
	all_record_update=MonthlyGeneratedTransactions.objects.filter(transaction_period=transaction_period).update(transaction_status=transaction_status)
	
	record=MonthlyGroupGeneratedTransactions(salary_institution=salary_institution,transaction_period=transaction_period,processed_by=processed_by)
	record.save()

	return HttpResponseRedirect(reverse('Monthly_Group_transaction_Institution_Load'))



def Monthly_Group_Transaction_View(request,pk):
	DataCapture=DataCaptureManager.objects.first()
	salary_institution=SalaryInstitution.objects.get(id=pk)

	status=MembershipStatus.objects.get(title="ACTIVE")
	transaction_period=TransactionPeriods.objects.get(status=status)
	
	records=MonthlyDeductionListGenerated.objects.filter(salary_institution=salary_institution,transaction_period=transaction_period)
	context={
	'transaction_period':transaction_period,
	'records':records,
	'DataCapture':DataCapture,
	}
	return render(request,'deskofficer_templates/Monthly_Group_Transaction_View.html',context)





def Monthly_Deduction_excel_Export_Institution_Load(request):
	DataCapture=DataCaptureManager.objects.first()
	status=MembershipStatus.objects.get(title='ACTIVE')
	transaction_period=TransactionPeriods.objects.get(status=status)
	items=SalaryInstitution.objects.all()
	
	records=MonthlyGroupGeneratedTransactions.objects.filter(transaction_period=transaction_period)
	context={
	'items':items,
	'transaction_period':transaction_period,
	'records':records,
	'DataCapture':DataCapture,
	}
	return render(request,'deskofficer_templates/Monthly_Deduction_excel_Export_Institution_Load.html',context)





def Monthly_Deduction_excel_Export_load(request,pk):
	DataCapture=DataCaptureManager.objects.first()
	salary_institution=SalaryInstitution.objects.get(id=pk)

	status=MembershipStatus.objects.get(title="ACTIVE")
	transaction_period=TransactionPeriods.objects.get(status=status)
	
	records=MonthlyDeductionListGenerated.objects.filter(salary_institution=salary_institution,transaction_period=transaction_period)

	
	author =  CustomUser.objects.annotate(screen_name=Concat('first_name', V(' ') ,'last_name'))

		
	button_enabled=True
	if records.count()==0:
		button_enabled=False

	
	context={
	'transaction_period':transaction_period,
	'records':records,
	'pk':pk,
	'DataCapture':DataCapture,
	'button_enabled':button_enabled,
	}
	return render(request,'deskofficer_templates/Monthly_Deduction_excel_Export_load.html',context)


def export_norminal_roll_xls(request):
	
	response = HttpResponse(content_type='application/ms-excel')
	response['Content-Disposition'] = 'attachment; filename="users.xls"'

	wb = xlwt.Workbook(encoding='utf-8')
	ws = wb.add_sheet('Users Data') # this will make a sheet named Users Data

	row_num = 0  # Sheet header, first row

	font_style = xlwt.XFStyle()
	font_style.font.bold = True

	columns = ['File No', 'IPPIS No','Last Name', 'Fist_Name','Middle Name','Phone No','Year','Institute' ]

	for col_num in range(len(columns)):
		ws.write(row_num, col_num, columns[col_num], font_style) # at 0 row 0 column 
	
	font_style = xlwt.XFStyle()  # Sheet body, remaining rows
	

	rows = NorminalRoll.objects.all().values_list('file_no','ippis_no','last_name','first_name', 'middle_name','phone_no','year','salary_institution')

	for row in rows:
		row_num += 1
		for col_num in range(len(row)):
			ws.write(row_num, col_num, row[col_num], font_style)
	wb.save(response)
	
	return response


def export_users_xls(request,pk):
	salary_institution=SalaryInstitution.objects.get(id=pk)

	status=MembershipStatus.objects.get(title="ACTIVE")
	transaction_period=TransactionPeriods.objects.get(status=status)

	response = HttpResponse(content_type='application/ms-excel')
	response['Content-Disposition'] = 'attachment; filename="users.xls"'

	wb = xlwt.Workbook(encoding='utf-8')
	ws = wb.add_sheet('Users Data') # this will make a sheet named Users Data

	row_num = 0  # Sheet header, first row

	font_style = xlwt.XFStyle()
	font_style.font.bold = True

	columns = ['Member ID', 'File No', 'IPPIS No', 'Name','Amount' ]

	for col_num in range(len(columns)):
		ws.write(row_num, col_num, columns[col_num], font_style) # at 0 row 0 column 
	
	font_style = xlwt.XFStyle()  # Sheet body, remaining rows
	

	rows = MonthlyDeductionListGenerated.objects.filter(salary_institution=salary_institution,transaction_period=transaction_period).values_list('member__member_id','member__file_no','member__ippis_no','member__full_name', 'amount')

	for row in rows:
		row_num += 1
		for col_num in range(len(row)):
			ws.write(row_num, col_num, row[col_num], font_style)
	wb.save(response)
	
	return response


def Monthly_Account_deduction_Excel_import_Institution_Load(request):
	DataCapture=DataCaptureManager.objects.first()
	status=MembershipStatus.objects.get(title='ACTIVE')
	transaction_period=TransactionPeriods.objects.get(status=status)
	items=SalaryInstitution.objects.all()

	context={
	'items':items,
	'transaction_period':transaction_period,
	
	'DataCapture':DataCapture,
	}
	return render(request,'deskofficer_templates/Monthly_Account_deduction_Excel_import_Institution_Load.html',context)




def upload_AccountDeductionsResource(request,pk):
	DataCapture=DataCaptureManager.objects.first()
	status=MembershipStatus.objects.get(title='ACTIVE')
	transaction_period=TransactionPeriods.objects.get(status=status)
	
	salary_institution=SalaryInstitution.objects.get(id=pk)

	if request.method == 'POST':
		if  AccountDeductions.objects.filter(salary_institution=salary_institution,transaction_period=transaction_period).exists():
			messages.error(request,'Account Deduction for this Period Already Imported')
			return HttpResponseRedirect(reverse('upload_AccountDeductionsResource',args=(pk,)))	


		account_deduction_resource = AccountDeductionsResource()
		dataset = Dataset()
		new_account_deductions = request.FILES['myfile']

		if not new_account_deductions.name.endswith('xls'):
			messages.error(request,'Wrong format')
			return HttpResponseRedirect(reverse('upload_AccountDeductionsResource',args=(pk,)))	

		imported_data = dataset.load(new_account_deductions.read(),format='xls')
		for data in imported_data:
			value = AccountDeductions(salary_institution=salary_institution,
					transaction_period=transaction_period,			
					ippis_no=data[0],			
					name=data[1],			
					amount=data[2],	
				)
			value.save()
	context={
	'transaction_period':transaction_period,
	'DataCapture':DataCapture,
	}
	return render(request,'deskofficer_templates/upload.html',context)	


def Monthly_Account_deduction_Processing_Institution_Load(request):
	form = Monthly_Account_deduction_Processing_Institution_Load_form(request.POST or None)
	DataCapture=DataCaptureManager.objects.first()
	status=MembershipStatus.objects.get(title='ACTIVE')

	items=SalaryInstitution.objects.all()
	
	
		
	context={
	'form':form,
	'items':items,	
	'DataCapture':DataCapture,
	}
	return render(request,'deskofficer_templates/Monthly_Account_deduction_Processing_Institution_Load.html',context)



def Monthly_Account_deduction_Processing_Preview(request):
	
	transaction_period_id=request.POST.get('transaction_period')
	transaction_period=TransactionPeriods.objects.get(id=transaction_period_id)

	salary_institution_id = request.POST.get('salary_institution')
	salary_institution=SalaryInstitution.objects.get(id=salary_institution_id)

	DataCapture=DataCaptureManager.objects.first()
	transaction_status=TransactionStatus.objects.get(title='UNTREATED')
	status=MembershipStatus.objects.get(title='ACTIVE')
	
	


	records=AccountDeductions.objects.filter(salary_institution=salary_institution,transaction_period=transaction_period,transaction_status=transaction_status)
	context={
	'records':records,
	'transaction_period':transaction_period,
	'pk':salary_institution_id,
	'DataCapture':DataCapture,
	}
	return render(request,'deskofficer_templates/Monthly_Account_deduction_Processing_Preview.html',context)



def Monthly_Account_deduction_Process(request,pk,trans_id):
	transaction_status=TransactionStatus.objects.get(title='TREATED')
	
	status=MembershipStatus.objects.get(title='ACTIVE')
	transaction_period=TransactionPeriods.objects.get(id=trans_id)
	
	salary_institution=SalaryInstitution.objects.get(id=pk)

	records=AccountDeductions.objects.filter(salary_institution=salary_institution,transaction_period=transaction_period)

	for record in records:
		if MonthlyDeductionListGenerated.objects.filter(member__ippis_no=record.ippis_no,salary_institution=salary_institution,transaction_period=transaction_period).exists():
			coop_amount=MonthlyDeductionListGenerated.objects.get(member__ippis_no=record.ippis_no,salary_institution=salary_institution,transaction_period=transaction_period)
			record_update=MonthlyDeductionListGenerated.objects.filter(member__ippis_no=record.ippis_no,salary_institution=salary_institution,transaction_period=transaction_period).update(amount_deducted=record.amount,balance=float(record.amount)-float(coop_amount.amount))
		else:
			record=NonMemberAccountDeductions(salary_institution=salary_institution,transaction_period=transaction_period,ippis_no=record.ippis_no,name=record.name,amount=record.amount)
			record.save()

	record_update=AccountDeductions.objects.filter(salary_institution=salary_institution,transaction_period=transaction_period).update(transaction_status=transaction_status)
	return HttpResponseRedirect(reverse('Monthly_Account_deduction_Processing_Institution_Load'))	


def monthly_wrongful_deduction_transaction_period_load(request):
	DataCapture=DataCaptureManager.objects.first()
	form=TransactionPeriod_view_form(request.POST or None)
	records=[]
	if request.method=="POST":
		transaction_period_id=request.POST.get('transaction_period')
		transaction_period=TransactionPeriods.objects.get(id=transaction_period_id)
		records=NonMemberAccountDeductions.objects.filter(transaction_period=transaction_period)
		
	context={
	'form':form,
	'records':records,
	'DataCapture':DataCapture,
	}
	return render(request,'deskofficer_templates/monthly_wrongful_deduction_transaction_period_load.html',context)


def Monthly_Unbalanced_transactions(request):
	DataCapture=DataCaptureManager.objects.first()
	form=TransactionPeriod_view_form(request.POST or None)
	records=[]
	if request.method=="POST":
		transaction_period_id=request.POST.get('transaction_period')
		transaction_period=TransactionPeriods.objects.get(id=transaction_period_id)
		records=MonthlyDeductionListGenerated.objects.filter(transaction_period=transaction_period).filter(~Q(balance=0))
		
	context={
	'form':form,
	'records':records,
	'DataCapture':DataCapture,
	}
	return render(request,'deskofficer_templates/Monthly_Unbalanced_transactions.html',context)


def Monthly_deduction_ledger_posting_preview(request):
	DataCapture=DataCaptureManager.objects.first()
	form=deduction_ledger_posting_form(request.POST or None)
	records=[]
	process_status=False

	if request.method=="POST" and 'btnprocess' in request.POST:
		transaction_status=TransactionStatus.objects.get(title="UNTREATED")
		transaction_period_id=request.POST.get('transaction_period')
		transaction_period=TransactionPeriods.objects.get(id=transaction_period_id)
		
		salary_institution_id=request.POST.get('salary_institution')
		salary_institution=SalaryInstitution.objects.get(id=salary_institution_id)

		records=MonthlyDeductionListGenerated.objects.filter(transaction_period=transaction_period,salary_institution=salary_institution,transaction_status=transaction_status)
		transactions=TransactionTypes.objects.filter(~Q(source__title="GENERAL") | ~Q(source__title="UTILITIES")).order_by('rank')
		
		for record in records:
			total_amount=record.amount_deducted
			
			for transaction in transactions:

				if MonthlyDeductionList.objects.filter(member=record.member,transaction_period=transaction_period,transaction=transaction).exists():
					
					deduction=MonthlyDeductionList.objects.get(member=record.member,transaction_period=transaction_period,transaction=transaction)
					
					amount_due=deduction.amount

					if float(total_amount) > float(amount_due):
						record_update_status=TransactionStatus.objects.get(title="TREATED")
						record_update=MonthlyDeductionList.objects.filter(member=record.member,transaction_period=transaction_period,transaction=transaction).update(amount_deducted=amount_due,transaction_status=record_update_status)
						total_amount=float(total_amount)-float(amount_due)
						ledger_amount=amount_due
					elif float(total_amount) > 0 and float(total_amount) <= float(amount_due):
						record_update=MonthlyDeductionList.objects.filter(member=record.member,transaction_period=transaction_period,transaction=transaction).update(amount_deducted=total_amount,transaction_status=record_update_status)
						ledger_amount=total_amount

					if transaction.source.title == 'LOAN':
						
						if PersonalLedger.objects.filter(account_number=deduction.account_number).exists():
							ledger=PersonalLedger.objects.filter(account_number=deduction.account_number).last()
							balance=ledger.balance
							new_balance=float(balance) + float(ledger_amount)
							new_ledger=PersonalLedger(member=record.member,
													transaction=transaction,
													account_number=deduction.account_number,
													particulars="Loan Repayment for the Period of " + str(transaction_period.transaction_period),
													debit=0,credit=ledger_amount,
													balance=new_balance,
													transaction_period=transaction_period.transaction_period
								)
							new_ledger.save()
						else:
							
							new_balance= float(ledger_amount)
							new_ledger=PersonalLedger(member=record.member,
													transaction=transaction,
													account_number=deduction.account_number,
													particulars="Loan Repayment for the Period of " + str(transaction_period.transaction_period),
													debit=0,credit=ledger_amount,
													balance=new_balance,
													transaction_period=transaction_period.transaction_period
								)
							new_ledger.save()

						loan_record=LoansRepaymentBase.objects.get(loan_number=deduction.account_number)
						loan_balance=loan_record.balance
						loan_amount_paid=float(loan_record.amount_paid) +float(ledger_amount)
						record_update=LoansRepaymentBase.objects.filter(loan_number=deduction.account_number).update(amount_paid=loan_amount_paid,balance=float(loan_balance)+float(ledger_amount))
						
						loan_merge_status=LoanMergeStatus.objects.get(title='MERGED')
						if loan_record.loan_merge_status==loan_merge_status:
							loan_groups=LoansDisbursed.objects.filter(merge_account_number=loan_record.loan_number)
							merge_deduction_amount=ledger_amount

							for loan_group in loan_groups:
								entity_repayment=loan_group.repayment
								entity_balance=loan_group.balance
								
								if float(merge_deduction_amount) >= abs(float(entity_balance)):
									new_entity_amount_paid=float(entity_repayment)
									new_entity_balance=float(loan_group.balance)+(float(entity_repayment))
									merge_deduction_amount=float(merge_deduction_amount)-(float(entity_repayment))
								else:
									new_entity_amount_paid=float(merge_deduction_amount)
									new_entity_balance=float(loan_group.balance)+(float(merge_deduction_amount))
									merge_deduction_amount=0

								loan_group.amount_paid=float(loan_group.amount_paid)+ float(new_entity_amount_paid)
								loan_group.balance=float(new_entity_balance)
								loan_group.save()					


								if loan_group.balance >=0:
									loan_status=MembershipStatus.objects.get(title='INACTIVE')
									loan_group.status=loan_status
									loan_group.save()
									
									processed_by=CustomUser.objects	.get(id=request.user.id)
									transaction_status=TransactionStatus.objects.get(title='UNTREATED')
									
									record_cleared=LoansCleared(loan=loan_group,processed_by=processed_by,status=transaction_status)
									record_cleared.save()

						else:
							loan_group=LoansDisbursed.objects.filter(loan_number=deduction.account_number).update(amount_paid=loan_amount_paid,balance=float(loan_balance)+float(ledger_amount))
							
							if LoansDisbursed.objects.filter(loan_number=deduction.account_number).filter(Q(balance__gte=0)):
								loan_status=MembershipStatus.objects.get(title='INACTIVE')
								record_update=LoansDisbursed.objects.filter(loan_number=deduction.account_number).update(status=loan_status)
								
								processed_by=CustomUser.objects	.get(id=request.user.id)
								transaction_status=TransactionStatus.objects.get(title='UNTREATED')
								loan=LoansDisbursed.objects.get(loan_number=deduction.account_number)
								record_cleared=LoansCleared(loan=loan,processed_by=processed_by,status=transaction_status)
								record_cleared.save()

					elif transaction.source.title == 'SAVINGS':
						if PersonalLedger.objects.filter(account_number=deduction.account_number).exists():
							ledger=PersonalLedger.objects.filter(account_number=deduction.account_number).last()
							balance=ledger.balance
							new_balance=float(balance) + float(ledger_amount)
							new_ledger=PersonalLedger(member=record.member,
													transaction=transaction,
													account_number=deduction.account_number,
													particulars="Monthly Contribution for the Period of " +  str(transaction_period.transaction_period),
													debit=0,credit=ledger_amount,
													balance=new_balance,
													transaction_period=transaction_period.transaction_period
								)
							new_ledger.save()
						else:
							
							new_balance= float(ledger_amount)
							new_ledger=PersonalLedger(member=record.member,
													transaction=transaction,
													account_number=deduction.account_number,
													particulars="Monthly Contribution for the Period of " + str(transaction_period.transaction_period),
													debit=0,credit=ledger_amount,
													balance=new_balance,
													transaction_period=transaction_period.transaction_period
								)
							new_ledger.save()
		

		record_update_status=TransactionStatus.objects.get(title="TREATED")
		record_update=MonthlyDeductionListGenerated.objects.filter(transaction_period=transaction_period,salary_institution=salary_institution).update(transaction_status=record_update_status)		
		
		return HttpResponseRedirect(reverse('Monthly_deduction_ledger_posting_preview'))



	if request.method=="POST" and 'btnview' in request.POST:
		DataCapture=DataCaptureManager.objects.first()
		transaction_status=TransactionStatus.objects.get(title="UNTREATED")
		
		transaction_period_id=request.POST.get('transaction_period')
		transaction_period=TransactionPeriods.objects.get(id=transaction_period_id)
		
		salary_institution_id=request.POST.get('salary_institution')
		salary_institution=SalaryInstitution.objects.get(id=salary_institution_id)

		records=MonthlyDeductionListGenerated.objects.filter(transaction_period=transaction_period,salary_institution=salary_institution,transaction_status=transaction_status)
		
		
		if records.count()>0:
			process_status=True

	context={
	'form':form,
	'records':records,
	'process_status':process_status,
	'DataCapture':DataCapture,
	}
	return render(request,'deskofficer_templates/Monthly_deduction_ledger_posting_preview.html',context)



# def Monthly_deduction_ledger_posting_preview(request):
# 	DataCapture=DataCaptureManager.objects.first()
# 	form=deduction_ledger_posting_form(request.POST or None)
# 	records=[]
# 	process_status=False

# 	if request.method=="POST" and 'btnprocess' in request.POST:
# 		transaction_status=TransactionStatus.objects.get(title="UNTREATED")
# 		transaction_period_id=request.POST.get('transaction_period')
# 		transaction_period=TransactionPeriods.objects.get(id=transaction_period_id)
		
# 		salary_institution_id=request.POST.get('salary_institution')
# 		salary_institution=SalaryInstitution.objects.get(id=salary_institution_id)

# 		records=MonthlyDeductionListGenerated.objects.filter(transaction_period=transaction_period,salary_institution=salary_institution,transaction_status=transaction_status)
# 		transactions=TransactionTypes.objects.filter(~Q(source__title="GENERAL") | ~Q(source__title="UTILITIES")).order_by('rank')
		
# 		for record in records:
# 			total_amount=record.amount_deducted
			
# 			for transaction in transactions:

# 				if MonthlyDeductionList.objects.filter(member=record.member,transaction_period=transaction_period,transaction=transaction).exists():
					
# 					deduction=MonthlyDeductionList.objects.get(member=record.member,transaction_period=transaction_period,transaction=transaction)
					
# 					amount_due=deduction.amount

# 					if float(total_amount) > float(amount_due):
# 						# record_update_status=TransactionStatus.objects.get(title="TREATED")
# 						record_update=MonthlyDeductionList.objects.filter(member=record.member,transaction_period=transaction_period,transaction=transaction).update(amount_deducted=amount_due,transaction_status=record_update_status)
						
# 						total_amount=float(total_amount)-float(amount_due)
# 						ledger_amount=amount_due

# 					elif float(total_amount) <= float(amount_due) and float(total_amount) >0:
# 						# record_update=MonthlyDeductionList.objects.filter(member=record.member,transaction_period=transaction_period,transaction=transaction).update(amount_deducted=total_amount)
# 						ledger_amount=total_amount

# 					if transaction.source.title == 'LOAN':
						
# 						if PersonalLedger.objects.filter(account_number=deduction.account_number).exists():
# 							ledger=PersonalLedger.objects.filter(account_number=deduction.account_number).last()
# 							balance=ledger.balance
# 							new_balance=float(balance) + float(ledger_amount)
# 							new_ledger=PersonalLedger(member=record.member,
# 													transaction=transaction,
# 													account_number=deduction.account_number,
# 													particulars="Loan Repayment for the Period of " + str(transaction_period.transaction_period),
# 													debit=0,credit=ledger_amount,
# 													balance=new_balance,
# 													transaction_period=transaction_period.transaction_period
# 								)
# 							new_ledger.save()
# 						else:
							
# 							new_balance= float(ledger_amount)
# 							new_ledger=PersonalLedger(member=record.member,
# 													transaction=transaction,
# 													account_number=deduction.account_number,
# 													particulars="Loan Repayment for the Period of " + str(transaction_period.transaction_period),
# 													debit=0,credit=ledger_amount,
# 													balance=new_balance,
# 													transaction_period=transaction_period.transaction_period
# 								)
# 							new_ledger.save()

# 						loan_record=LoansRepaymentBase.objects.get(loan_number=deduction.account_number)
# 						loan_balance=loan_record.balance
# 						record_update=LoansRepaymentBase.objects.filter(loan_number=deduction.account_number).update(balance=float(abs(loan_balance))-float(ledger_amount))
						
# 						if LoansRepaymentBase.objects.filter(loan_number=deduction.account_number).filter(Q(balance__gte=0)):
# 							loan_status=MembershipStatus.objects.get(title='INACTIVE')
# 							record_update=LoansRepaymentBase.objects.filter(loan_number=deduction.account_number).update(status=loan_status)
							
# 							processed_by=CustomUser.objects	.get(id=request.user.id)
# 							transaction_status=TransactionStatus.objects.get(title='UNTREATED')
# 							loan=LoansRepaymentBase.objects.get(loan_number=deduction.account_number)
# 							record_cleared=LoansCleared(loan=loan,processed_by=processed_by,status=transaction_status)
# 							record_cleared.save()


# 					elif transaction.source.title == 'SAVINGS':
# 						if PersonalLedger.objects.filter(account_number=deduction.account_number).exists():
# 							ledger=PersonalLedger.objects.filter(account_number=deduction.account_number).last()
# 							balance=ledger.balance
# 							new_balance=float(balance) + float(ledger_amount)
# 							new_ledger=PersonalLedger(member=record.member,
# 													transaction=transaction,
# 													account_number=deduction.account_number,
# 													particulars="Monthly Contribution for the Period of " +  str(transaction_period.transaction_period),
# 													debit=0,credit=ledger_amount,
# 													balance=new_balance,
# 													transaction_period=transaction_period.transaction_period
# 								)
# 							new_ledger.save()
# 						else:
							
# 							new_balance= float(ledger_amount)
# 							new_ledger=PersonalLedger(member=record.member,
# 													transaction=transaction,
# 													account_number=deduction.account_number,
# 													particulars="Monthly Contribution for the Period of " + str(transaction_period.transaction_period),
# 													debit=0,credit=ledger_amount,
# 													balance=new_balance,
# 													transaction_period=transaction_period.transaction_period
# 								)
# 							new_ledger.save()

# 		record_update_status=TransactionStatus.objects.get(title="TREATED")
# 		record_update=MonthlyDeductionListGenerated.objects.filter(transaction_period=transaction_period,salary_institution=salary_institution).update(transaction_status=record_update_status)		
		
# 		return HttpResponseRedirect(reverse('Monthly_deduction_ledger_posting_preview'))



# 	if request.method=="POST" and 'btnview' in request.POST:
# 		DataCapture=DataCaptureManager.objects.first()
# 		transaction_status=TransactionStatus.objects.get(title="UNTREATED")
		
# 		transaction_period_id=request.POST.get('transaction_period')
# 		transaction_period=TransactionPeriods.objects.get(id=transaction_period_id)
		
# 		salary_institution_id=request.POST.get('salary_institution')
# 		salary_institution=SalaryInstitution.objects.get(id=salary_institution_id)

# 		records=MonthlyDeductionListGenerated.objects.filter(transaction_period=transaction_period,salary_institution=salary_institution,transaction_status=transaction_status)
		
		
# 		if records.count()>0:
# 			process_status=True

# 	context={
# 	'form':form,
# 	'records':records,
# 	'process_status':process_status,
# 	'DataCapture':DataCapture,
# 	}
# 	return render(request,'deskofficer_templates/Monthly_deduction_ledger_posting_preview.html',context)



#########################################################
############### EXTERNAL FASCILITY MANAGER###############
#########################################################
def external_fascility_update_search(request):
	DataCapture=DataCaptureManager.objects.first()
	title="Search Membership External Fascilities"
	form = searchForm(request.POST or None)
	return render(request,'deskofficer_templates/external_fascility_update_search.html',{'form':form,'title':title,'DataCapture':DataCapture,})


def external_fascility_update_list_load(request):
	DataCapture=DataCaptureManager.objects.first()
	title="Members Exclusiveness"
	form = searchForm(request.POST)
	if request.method == "POST":
		if request.POST.get("title")=="":
			return HttpResponseRedirect(reverse('members_exclusiveness_request_search'))

		status=MembershipStatus.objects.get(title="ACTIVE")
		form = searchForm(request.POST)
		members=Members.objects.filter(Q(member_id__icontains=form['title'].value()) |Q(phone_number__icontains=form['title'].value()) | Q(admin__first_name__icontains=form['title'].value()) | Q(admin__last_name__icontains=form['title'].value()) | Q(middle_name__icontains=form['title'].value())).filter(status=status)
		context={
		'members':members,
		'title':title,
		'DataCapture':DataCapture,
		}
		return render(request,'deskofficer_templates/external_fascility_update_list_load.html',context)




def external_fascility_update_process(request,pk):
	DataCapture=DataCaptureManager.objects.first()
	status=ApprovalStatus.objects.get(title='PENDING')
	member=Members.objects.get(pk=pk)
	form=external_fascility_form(request.POST or None)

	items=ExternalFascilitiesTemp.objects.filter(member=member,status=status)

	if request.method=="POST":
		approval_officer_id=request.POST.get('approval_officers')
		approval_officer=ApprovalOfficers.objects.get(id=approval_officer_id)

		description=request.POST.get('description')
		amount=request.POST.get('amount')

		
		if request.FILES.get('image', False):
			image = request.FILES['image']
			fs=FileSystemStorage()
			filename=fs.save(image.name,image)
			image_url=fs.url(filename)
		else:
			image_url=None

		
		if ExternalFascilitiesTemp.objects.filter(member=member,description=description,status=status).exists():
			record_exist=ExternalFascilitiesTemp.objects.get(member=member,description=description,status=status)
			record_exist.amount=amount
			record_exist.image=image_url
			record_exist.approval_officer=approval_officer
			record_exist.save()
			messages.success(request,'Record Updated Successfully')
			return HttpResponseRedirect(reverse('external_fascility_update_process',args=(pk,)))


		record=ExternalFascilitiesTemp(member=member,description=description,amount=amount,status=status,image=image_url,approval_officer=approval_officer)
		record.save()
		messages.success(request,'Record Added Successfully')
		return HttpResponseRedirect(reverse('external_fascility_update_process',args=(pk,)))
	
	context={
	'member':member,
	'form':form,
	'items':items,
	'pk':pk,
	'DataCapture':DataCapture,
	}
	return render(request,'deskofficer_templates/external_fascility_update_process.html',context)


def external_fascility_update_process_remove(request,pk, return_pk):
	item=ExternalFascilitiesTemp.objects.get(id=pk)
	item.delete()
	return HttpResponseRedirect(reverse('external_fascility_update_process',args=(return_pk,)))


def external_fascility_update_approved_list_load(request):
	DataCapture=DataCaptureManager.objects.first()
	status=ApprovalStatus.objects.get(title='APPROVED')
	transaction_status=TransactionStatus.objects.get(title='UNTREATED')
	members=ExternalFascilitiesTemp.objects.filter(transaction_status=transaction_status,status=status)

	context={
	'members':members,
	'DataCapture':DataCapture,
	}
	return render(request,'deskofficer_templates/external_fascility_update_approved_list_load.html',context)


def external_fascility_update_approved_processed(request,pk):
	
	status=TransactionStatus.objects.get(title='UNTREATED')
	status1=TransactionStatus.objects.get(title='TREATED')

	member=ExternalFascilitiesTemp.objects.get(id=pk)
	member.transaction_status=status1
	member.save()
	record=ExternalFascilitiesMain(member=member,status=status)
	record.save()
	return HttpResponseRedirect(reverse('external_fascility_update_approved_list_load'))




#########################################################
############### EXCLUSIVENESS #####################
#########################################################

def members_exclusiveness_request_search(request):
	DataCapture=DataCaptureManager.objects.first()
	title="Search Membership Exclusive Request"
	form = searchForm(request.POST or None)
	return render(request,'deskofficer_templates/members_exclusiveness_request_search.html',{'form':form,'title':title,'DataCapture':DataCapture,})


def members_exclusiveness_request_list_load(request):
	DataCapture=DataCaptureManager.objects.first()
	title="Members Exclusiveness"
	form = searchForm(request.POST)
	if request.method == "POST":
		if request.POST.get("title")=="":
			return HttpResponseRedirect(reverse('members_exclusiveness_request_search'))

		status=MembershipStatus.objects.get(title="ACTIVE")
		form = searchForm(request.POST)
		members=Members.objects.filter(Q(member_id__icontains=form['title'].value()) |Q(phone_number__icontains=form['title'].value()) | Q(admin__first_name__icontains=form['title'].value()) | Q(admin__last_name__icontains=form['title'].value()) | Q(middle_name__icontains=form['title'].value())).filter(status=status)
		context={
		'members':members,
		'title':title,
		'DataCapture':DataCapture,
		}
		return render(request,'deskofficer_templates/members_exclusiveness_request_list_load.html',context)


def members_exclusiveness_request_register(request,pk):
	DataCapture=DataCaptureManager.objects.first()
	status=TransactionStatus.objects.get(title='UNTREATED')
	approval_status=ApprovalStatus.objects.get(title='PENDING')
	form=members_exclusiveness_request_register_form(request.POST or None)
	member=Members.objects.get(id=pk)
	items=MembersExclusiveness.objects.filter(member=member,status=status,approval_status=approval_status)
	if request.method=="POST":
		transaction_id=request.POST.get('transactions')
		transaction=TransactionTypes.objects.get(id=transaction_id)

		officer_id=request.POST.get('approval_officers')
		approval_officer=ApprovalOfficers.objects.get(id=officer_id)

		if MembersExclusiveness.objects.filter(member=member,status=status,approval_status=approval_status,transaction=transaction).exists():
			record=MembersExclusiveness.objects.filter(member=member,status=status,approval_status=approval_status).first()
			record.approval_officer=approval_officer
			record.save()
			return HttpResponseRedirect(reverse('members_exclusiveness_request_register',args=(pk,)))


		record=MembersExclusiveness(member=member,approval_officer=approval_officer,status=status,transaction=transaction)
		record.save()
		return HttpResponseRedirect(reverse('members_exclusiveness_request_register',args=(pk,)))
	context={
	'form':form,
	'items':items,
	'return_pk':pk,
	'DataCapture':DataCapture,
	}
	return render(request,'deskofficer_templates/members_exclusiveness_request_register.html',context)


def members_exclusiveness_request_delete(request,pk,return_pk):
	record=MembersExclusiveness.objects.get(id=pk)
	record.delete()
	return HttpResponseRedirect(reverse('members_exclusiveness_request_register',args=(return_pk,)))


def members_exclusiveness_approved_list_load(request):
	DataCapture=DataCaptureManager.objects.first()
	approval_status=ApprovalStatus.objects.get(title="APPROVED")
	status=TransactionStatus.objects.get(title='UNTREATED')

	members=MembersExclusiveness.objects.filter(approval_status=approval_status,status=status)
	context={
	'members':members,
	'DataCapture':DataCapture,
	}
	return render(request,'deskofficer_templates/members_exclusiveness_approved_list_load.html',context)


def members_exclusiveness_approved_processed(request,pk):
	exclusive_status=ExclusiveStatus.objects.get(title="EXCLUSIVE")
	status=TransactionStatus.objects.get(title='TREATED')
	member=MembersExclusiveness.objects.get(id=pk)
	member.status=status
	member.save()

	member.member.exclusive_status=exclusive_status
	member.member.save()
	return HttpResponseRedirect(reverse('members_exclusiveness_approved_list_load'))





#########################################################
############### MEMBERS BANK INFO#####################
#########################################################

def MembersBankAccounts_list_search(request):
	DataCapture=DataCaptureManager.objects.first()
	title="Search Membership Account Creation"
	form = searchForm(request.POST or None)
	return render(request,'deskofficer_templates/MembersBankAccounts_list_search.html',{'form':form,'title':title,'DataCapture':DataCapture,})



def MembersBankAccounts_list_load(request):
	DataCapture=DataCaptureManager.objects.first()
	title="Bank Accoun Creation"
	form = searchForm(request.POST)
	if request.method == "POST":
		if request.POST.get("title")=="":
			return HttpResponseRedirect(reverse('MembersBankAccounts_list_search'))

		status=MembershipStatus.objects.get(title='ACTIVE')
		members=Members.objects.filter(Q(phone_number__icontains=form['title'].value()) | Q(admin__first_name__icontains=form['title'].value()) | Q(admin__last_name__icontains=form['title'].value()) | Q(middle_name__icontains=form['title'].value())).filter(status=status)
		context={
		'members':members,
		'title':title,
		'DataCapture':DataCapture,
		}
		return render(request,'deskofficer_templates/MembersBankAccounts_list_load.html',context)




def Members_Bank_Accounts(request,pk):
	DataCapture=DataCaptureManager.objects.first()
	form=MembersBankAccounts_form(request.POST or None)
	member=Members.objects.get(id=pk)
	accounts = MembersBankAccounts.objects.filter(member_id_id=pk)
	form.fields['account_name'].initial= member.admin.last_name + " " + member.admin.first_name + " " + member.middle_name
	if request.method=="POST":
		form=MembersBankAccounts_form(request.POST)
		

		if form.is_valid():
			member_id = Members.objects.get(id=pk)
			bank_id=form.cleaned_data['banks']
			bank=Banks.objects.get(id=bank_id)

			account_type_id = form.cleaned_data['account_types']
			account_type=AccountTypes.objects.get(id=account_type_id)

			account_name = form.cleaned_data['account_name']
			account_number = form.cleaned_data['account_number']

			if MembersBankAccounts.objects.filter(account_number=account_number).exists():
				messages.error(request,"Failed to add Account, Alreasy in Use")
				return HttpResponseRedirect(reverse('Members_Bank_Accounts',args=(pk,)))

			record=MembersBankAccounts(member_id=member_id,bank=bank,account_type=account_type,account_name=account_name,account_number=account_number)
			record.save()
			messages.success(request,"Account Added Successfully")
			return HttpResponseRedirect(reverse('Members_Bank_Accounts',args=(pk,)))

	context={
	'form':form,
	'member':member,
	'accounts':accounts,
	'return_pk':pk,
	'DataCapture':DataCapture,
	}
	return render(request,'deskofficer_templates/MembersBankAccounts.html',context)


def Members_Bank_Accounts_remove(request,pk):
	record=MembersBankAccounts.objects.get(id=pk)
	return_pk=record.member_id_id
	record.delete()
	return HttpResponseRedirect(reverse('Members_Bank_Accounts',args=(return_pk,)))


def Members_Bank_Accounts_lock(request,pk):
	member=Members.objects.get(id=pk)
	lock_status=LockedStatus.objects.get(title='LOCKED')
	record=MembersBankAccounts.objects.filter(member_id=member).update(lock_status=lock_status)


	return HttpResponseRedirect(reverse('Members_Bank_Accounts',args=(member.pk,)))


def Members_Bank_Accounts_edit_search(request):
	DataCapture=DataCaptureManager.objects.first()
	title="Search Membership Account Update"
	form = searchForm(request.POST or None)
	return render(request,'deskofficer_templates/Members_Bank_Accounts_edit_search.html',{'form':form,'title':title,'DataCapture':DataCapture,})


def Members_Bank_Accounts_edit_list_load(request):
	DataCapture=DataCaptureManager.objects.first()
	title="Bank Accoun update"
	form = searchForm(request.POST)
	if request.method == "POST":
		if request.POST.get("title")=="":
			return HttpResponseRedirect(reverse('Members_Bank_Accounts_edit_search'))

		status=MembershipStatus.objects.get(title='ACTIVE')
		members=Members.objects.filter(Q(phone_number__icontains=form['title'].value()) | Q(admin__first_name__icontains=form['title'].value()) | Q(admin__last_name__icontains=form['title'].value()) | Q(middle_name__icontains=form['title'].value())).filter(status=status)
		context={
		'members':members,
		'title':title,
		'DataCapture':DataCapture,
		}
		return render(request,'deskofficer_templates/Members_Bank_Accounts_edit_list_load.html',context)



def Members_Bank_Accounts_edit_details_load(request,pk):
	DataCapture=DataCaptureManager.objects.first()
	member=Members.objects.get(id=pk)
	accounts = MembersBankAccounts.objects.filter(member_id_id=pk)
	context={
		'member':member,
		'accounts':accounts,
		'return_pk':pk,
		'DataCapture':DataCapture,
		}
	return render(request,'deskofficer_templates/Members_Bank_Accounts_edit_details_load.html',context)


def Members_Bank_Accounts_update_form(request,pk,return_pk):
	DataCapture=DataCaptureManager.objects.first()
	form=MembersBankAccounts_form(request.POST or None)
	account = MembersBankAccounts.objects.get(id=pk)

	form.fields['banks'].initial= account.bank.id
	form.fields['account_types'].initial=account.account_type.id
	form.fields['account_name'].initial=account.account_name
	form.fields['account_number'].initial=account.account_number
	
	if request.method=="POST":
		form=MembersBankAccounts_form(request.POST)
		if form.is_valid():
			bank_id = form.cleaned_data['banks']
			bank=Banks.objects.get(id=bank_id)

			account_type_id = form.cleaned_data['account_types']
			account_type=AccountTypes.objects.get(id=account_type_id)

			account_name=form.cleaned_data['account_name']
			account_number=form.cleaned_data['account_number']

			account.bank=bank
			account.account_type=account_type
			account.account_name=account_name
			account.account_number=account_number
			account.save()
			messages.success(request,"Account updated Successfully")
			return HttpResponseRedirect(reverse('Members_Bank_Accounts_update_form',args=(pk,return_pk)))
	context={
		'account':account,
		'return_pk':pk,
		'form':form,
		'DataCapture':DataCapture,
		}
	return render(request,'deskofficer_templates/Members_Bank_Accounts_update_form.html',context)


def Members_Bank_Accounts_delete(request,pk,return_pk):
	account =MembersBankAccounts.objects.get(id=pk)
	account.delete()
	messages.success(request,"Account Deleted Successfully")
	return HttpResponseRedirect(reverse('Members_Bank_Accounts_edit_form',args=(return_pk,)))




#########################################################
############### NEXT OF KIN   ##########################
#########################################################

def Members_Next_Of_Kins_search(request):
	DataCapture=DataCaptureManager.objects.first()
	title="Search Membership for Next Of Kins"
	form = searchForm(request.POST or None)
	return render(request,'deskofficer_templates/Members_Next_Of_Kins_search.html',{'form':form,'title':title,'DataCapture':DataCapture,})


def Members_Next_Of_Kins_list_load(request):
	DataCapture=DataCaptureManager.objects.first()
	title="Members Next Of Kins"
	form = searchForm(request.POST)
	if request.method == "POST":
		if request.POST.get("title")=="":
			return HttpResponseRedirect(reverse('Members_Next_Of_Kins_search'))

		status=MembershipStatus.objects.get(title='ACTIVE')
		members=Members.objects.filter(Q(phone_number__icontains=form['title'].value()) | Q(admin__first_name__icontains=form['title'].value()) | Q(admin__last_name__icontains=form['title'].value()) | Q(middle_name__icontains=form['title'].value())).filter(status=status)
		context={
		'members':members,
		'title':title,
		'DataCapture':DataCapture,
		}
		return render(request,'deskofficer_templates/Members_Next_Of_Kins_list_load.html',context)




def addMembersNextOfKins(request,pk):
	DataCapture=DataCaptureManager.objects.first()
	member=Members.objects.get(id=pk)
	title="Add Next Of Kins"
	form=MembersNextOfKins_form(request.POST or None)
	records=MembersNextOfKins.objects.filter(member=member)

	if request.method=="POST":
		form=MembersNextOfKins_form(request.POST)
		status=MembershipStatus.objects.get(title='ACTIVE')
		if form.is_valid():
			nok_max=NextOfKinsMaximun.objects.first()

			relationships_id=form.cleaned_data['relationships']
			relationships=NOKRelationships.objects.get(id=relationships_id)
			name=form.cleaned_data['name']
			address=form.cleaned_data['address']
			phone_number=form.cleaned_data['phone_number']

			existing_record_count=MembersNextOfKins.objects.filter(member=member).count()
			if int(nok_max.maximun) < int(existing_record_count) + 1:
				messages.error(request,'Total number of allowed Next of Kins exceeded')
				return HttpResponseRedirect(reverse('addMembersNextOfKins',args=(pk,)))

			if MembersNextOfKins.objects.filter(member=member,relationships=relationships,name=name).exists():
				record_exist=MembersNextOfKins.objects.get(member=member,relationships=relationships,name=name)
				record_exist.address=address
				record_exist.phone_number=phone_number
				record_exist.status=status
				record_exist.save()
				messages.success(request,"Record Updates Successfully")
				return HttpResponseRedirect(reverse('addMembersNextOfKins',args=(pk,)))

			record=MembersNextOfKins(status=status,member=member,relationships=relationships,name=name,address=address,phone_number=phone_number)
			record.save()
			messages.success(request,"Record Added Successfully")
			return HttpResponseRedirect(reverse('addMembersNextOfKins',args=(pk,)))
	context={
	'form':form,
	'member':member,
	'title':title,
	'records':records,
	'DataCapture':DataCapture,
	}
	return render(request,'deskofficer_templates/addMembersNextOfKins.html',context)


def MembersNextOfKins_lock(request,pk):
	member=Members.objects.get(id=pk)
	lock_status=LockedStatus.objects.get(title='LOCKED')
	records=MembersNextOfKins.objects.filter(member=member).update(lock_status=lock_status)
	messages.success(request,"Record Locked Successfully")
	return HttpResponseRedirect(reverse('addMembersNextOfKins',args=(member.pk,)))


def MembersNextOfKins_remove(request,pk):
	record=MembersNextOfKins.objects.get(id=pk)
	return_pk=record.member_id
	record.delete()
	messages.success(request,"Record Deleted Successfully")
	return HttpResponseRedirect(reverse('addMembersNextOfKins',args=(return_pk,)))

def Members_Next_Of_Kins_Manage_search(request):
	DataCapture=DataCaptureManager.objects.first()
	title="Search Membership for Next Of Kins"
	form = searchForm(request.POST or None)
	return render(request,'deskofficer_templates/Members_Next_Of_Kins_Manage_search.html',{'form':form,'title':title,'DataCapture':DataCapture,})


def Members_Next_Of_Kins_Manage_list_load(request):
	DataCapture=DataCaptureManager.objects.first()
	title="Members Next Of Kins"
	form = searchForm(request.POST)
	if request.method == "POST":
		if request.POST.get("title")=="":
			return HttpResponseRedirect(reverse('Members_Next_Of_Kins_Manage_search'))

		status=MembershipStatus.objects.get(title='ACTIVE')
		members=Members.objects.filter(Q(phone_number__icontains=form['title'].value()) | Q(admin__first_name__icontains=form['title'].value()) | Q(admin__last_name__icontains=form['title'].value()) | Q(middle_name__icontains=form['title'].value())).filter(status=status)
		context={
		'members':members,
		'title':title,
		'DataCapture':DataCapture,
		}
		return render(request,'deskofficer_templates/Members_Next_Of_Kins_Manage_list_load.html',context)


def Members_Next_Of_Kins_Manage_NOK_Load(request,pk):
	DataCapture=DataCaptureManager.objects.first()
	member=Members.objects.get(id=pk)
	noks=MembersNextOfKins.objects.filter(member_id=pk)
	title="List of Next Of Kins"

	context={
	
	'member':member,
	'title':title,
	'noks':noks,
	'member_id':pk,
	'DataCapture':DataCapture,
	}
	return render(request,'deskofficer_templates/Members_Next_Of_Kins_Manage_NOK_Load.html',context)




def Members_Next_Of_Kins_Manage_NOK_Update(request,pk,member_id):
	DataCapture=DataCaptureManager.objects.first()
	form=MembersNextOfKins_form(request.POST or None)
	member=Members.objects.get(id=member_id)
	nok=MembersNextOfKins.objects.get(id=pk)
	title="Update Next Of Kins"

	form.fields['relationships'].initial= nok.relationships.id
	form.fields['name'].initial=nok.name
	form.fields['address'].initial=nok.address
	form.fields['phone_number'].initial=nok.phone_number

	if request.method=="POST":
		status=MembershipStatus.objects.get(title='ACTIVE')
		form=MembersNextOfKins_form(request.POST)
		if form.is_valid():
			relationships_id=form.cleaned_data['relationships']
			relationships=NOKRelationships.objects.get(id=relationships_id)
			name=form.cleaned_data['name']
			address=form.cleaned_data['address']
			phone_number=form.cleaned_data['phone_number']
			
			nok.status=status
			nok.relationships=relationships
			nok.name=name
			nok.address=address
			nok.phone_number=phone_number
			nok.save()
			messages.success(request,"Record Updated Successfully")
			return HttpResponseRedirect(reverse('Members_Next_Of_Kins_Manage_NOK_Load',args=(member_id,)))
	context={
	'form':form,
	'member':member,
	'title':title,
	'nok':nok,
	'DataCapture':DataCapture,
	}
	return render(request,'deskofficer_templates/Members_Next_Of_Kins_Manage_NOK_Update.html',context)





###########################################################
################## SALARY UPDATE ##########################
###########################################################

def Members_Salary_Update_request_search(request):
	DataCapture=DataCaptureManager.objects.first()
	title="Search Membership for Salary Update"
	form = searchForm(request.POST or None)
	return render(request,'deskofficer_templates/Members_Salary_Update_request_search.html',{'form':form,'title':title,'DataCapture':DataCapture,})


def Members_Salary_Update_Request_list_load(request):
	DataCapture=DataCaptureManager.objects.first()
	title="Members Salary Update"
	form = searchForm(request.POST)
	if request.method == "POST":
		if request.POST.get("title")=="":
			return HttpResponseRedirect(reverse('Members_Salary_Update_request_search'))

		status=MembershipStatus.objects.get(title='ACTIVE')
		members=Members.objects.filter(Q(phone_number__icontains=form['title'].value()) | Q(admin__first_name__icontains=form['title'].value()) | Q(admin__last_name__icontains=form['title'].value()) | Q(middle_name__icontains=form['title'].value())).filter(status=status)
		context={
		'members':members,
		'title':title,
		'DataCapture':DataCapture,
		}
		return render(request,'deskofficer_templates/Members_Salary_Update_Request_list_load.html',context)


def Members_Salary_Update_Request_Load(request,pk):
	DataCapture=DataCaptureManager.objects.first()
	form=Members_Salary_Update_Request_form(request.POST or None)
	member=Members.objects.get(id=pk)
	if request.method=="POST":
		status=ApprovalStatus.objects.get(title='PENDING')
		amount=request.POST.get('gross_pay')
		description=request.POST.get('description')
		approval_officer_id=request.POST.get('approval_officers')

		approved_officer=ApprovalOfficers.objects.get(id=approval_officer_id)
		if MembersSalaryUpdateRequest.objects.filter(member=member,status=status).exists():
			messages.error(request,"You still have Open Transaction")
			return HttpResponseRedirect(reverse('Members_Salary_Update_Request_Load',args=(pk,)))

		record=MembersSalaryUpdateRequest(member=member,description=description,amount=amount,approved_officer=approved_officer,status=status)
		record.save()
		return HttpResponseRedirect(reverse('Members_Salary_Update_Request_Load',args=(pk,)))
	context={
	'form':form,
	'member':member,
	'member_id':pk,
	'DataCapture':DataCapture,
	}
	return render(request,'deskofficer_templates/Members_Salary_Update_Request_Load.html',context)


def Members_Salary_Update_Request_approval_Load(request):
	DataCapture=DataCaptureManager.objects.first()
	status=ApprovalStatus.objects.get(title="APPROVED")
	processing_status=ProcessingStatus.objects.get(title='PROCESSED')
	members=MembersSalaryUpdateRequest.objects.filter(status=status).exclude(processing_status=processing_status)
	context={
	'members':members,
	'DataCapture':DataCapture,
	}
	return render(request,'deskofficer_templates/Members_Salary_Update_Request_approval_Load.html',context)


def Members_Salary_Update_Request_process(request,pk):
	processing_status=ProcessingStatus.objects.get(title='PROCESSED')
	member=MembersSalaryUpdateRequest.objects.get(id=pk)
	member.member.gross_pay=member.amount
	member.processing_status=processing_status
	member.save()
	member.member.save()

	return HttpResponseRedirect(reverse('Members_Salary_Update_Request_approval_Load'))




###########################################################
################## VALIDATION ##########################
###########################################################
@csrf_exempt
def check_membership_phone_no_exist(request):
    phone_no=request.POST.get("phone_no1")

    user_obj=Members.objects.filter(phone_number=phone_no).exists()
    if user_obj:
        return HttpResponse(True)
    else:
        return  HttpResponse(False)






###########################################################
################## CATALYST ### ##########################
###########################################################
def temporallyloan(request):
	members=Members.objects.all()
	context={
	'members':members,
	'DataCapture':DataCapture,
	}
	return render(request,'deskofficer_templates/temporallyloan.html',context)


def  temporally_loan_form(request,pk):
	member=Members.objects.get(id=pk)
	form=temporallyloan_form(request.POST or None)
	if request.method=="POST":
		form=temporallyloan_form(request.POST)
		if form.is_valid():
			loan_id = form.cleaned_data["loans"]
			loan=TransactionTypes.objects.get(id=loan_id)

			loan_amount= form.cleaned_data["amount"]
			duration=loan.duration
			interest_rate=loan.interest_rate
			interest=float(interest_rate)/100
			balance=float(loan_amount)-interest
			monthly_repayment=float(loan_amount)/float(duration)
			record=LoansDisbursed(member_id=member,loan_type=loan,loan_amount=loan_amount,repayment=monthly_repayment,balance=loan_amount)
			record.save()
			return HttpResponseRedirect(reverse('temporally_loan_form', args=(pk,)))
	context={
	'member':member,
	'form':form,
	'DataCapture':DataCapture,
	}
	return render(request,'deskofficer_templates/temporallyloan_form.html',context)


###########################################################
################ NORMIAL ROLL UPLOAD #####################
###########################################################

def upload_norminal_roll(request):
	DataCapture=DataCaptureManager.objects.first()
	if request.method == 'POST':
	
		norminal_resource = NorminalRollResource()
		dataset = Dataset()
		new_norminal_roll = request.FILES['myfile']

		if not new_norminal_roll.name.endswith('xlsx'):
			messages.error(request,'Wrong format')
			return HttpResponseRedirect(reverse('upload_norminal_roll',args=(pk,)))	

		imported_data = dataset.load(new_norminal_roll.read(),format='xlsx')
		for data in imported_data:
			name=list((data[1]).split())
			last_name=""
			first_name=""
			middle_name=""
			if len(name)==1:
				last_name=name[0]
			elif len(name) == 2:
				last_name=name[0]
				first_name=name[1]
			elif len(name) == 3:
				last_name=name[0]
				first_name=name[1]
				middle_name=name[2]
			elif len(name) == 4:
				last_name=name[0]
				first_name=name[1]
				middle_name=str(name[2]) + ' ' + str(name[3])
			
			value = NorminalRoll(member_id=data[0],
					file_no=data[0],			
					ippis_no=data[0],			
					last_name=last_name,			
					first_name=first_name,			
					middle_name=middle_name,			
					phone_no=data[2],	
					year=data[3],	
					salary_institution=data[4],	
				)
			value.save()
	context={
	
	'DataCapture':DataCapture,
	}
	return render(request,'deskofficer_templates/upload_norminal.html',context)	



def upload_distinct_norminal_roll(request):
	DataCapture=DataCaptureManager.objects.first()
	if request.method == 'POST':
	
		norminal_resource = NorminalRollResource()
		dataset = Dataset()
		new_norminal_roll = request.FILES['myfile']

		if not new_norminal_roll.name.endswith('xlsx'):
			messages.error(request,'Wrong format')
			return HttpResponseRedirect(reverse('upload_norminal_roll',args=(pk,)))	

		imported_data = dataset.load(new_norminal_roll.read(),format='xlsx')
		for data in imported_data:
			
			value = NorminalRoll(member_id=str(data[0]).zfill(5),
					file_no=str(data[0]).zfill(5),			
					ippis_no=str(data[1]).zfill(5),			
					last_name=data[2],			
					first_name=data[3],			
					middle_name=data[4],			
					phone_no=str(data[5]).zfill(11),	
					year=data[6],	
					salary_institution=data[7],	
				)
			value.save()
	context={
	
	'DataCapture':DataCapture,
	}
	return render(request,'deskofficer_templates/upload_norminal.html',context)	


def Norminal_Roll_Preview(request):
	DataCapture=DataCaptureManager.objects.first()
	transaction_status=TransactionStatus.objects.get(title="UNTREATED")
	records=NorminalRoll.objects.filter(transaction_status=transaction_status)
	context={
	'records':records,
	'DataCapture':DataCapture,
	}
	return render(request,'deskofficer_templates/Norminal_Roll_Preview.html',context)


def Norminal_Roll_Process(request):
	# records=NorminalRoll.objects.all()
	# records.delete()

	# records=MemberShipRequest.objects.filter(Q(id__gt=8))
	# records.delete()	

	# records=MemberShipFormSales.objects.filter(Q(id__gt=9))
	# records.delete()

	# return HttpResponse("Done")

	prefix=MembersIdManager.objects.first()

	certification_status=CertificationStatus.objects.get(title='CERTIFIED')
	approval_status=ApprovalStatus.objects.get(title='APPROVED')
	submission_status=SubmissionStatus.objects.get(title="SUBMITTED")
	transaction_status=TransactionStatus.objects.get(title="UNTREATED")
	transaction_status1=TransactionStatus.objects.get(title="TREATED")


	records=NorminalRoll.objects.filter(transaction_status=transaction_status)
	
	certification_officer=CertificationOfficers.objects.filter(transaction__transaction__name='MEMBERSHIP').first()
	
	approval_officer=ApprovalOfficers.objects.filter(transaction__transaction__name='MEMBERSHIP').first()
	

	for record in records:
		file_no = str(record.file_no).zfill(5)
		ippis_no = str(record.ippis_no).zfill(5)
		first_name=record.first_name
		last_name=record.last_name
		middle_name=record.middle_name
	
		phone_number = str(record.phone_no).zfill(11)
		year = record.year
		member_id = prefix.prefix_title + "/" +  str(year) + '/' + str(record.member_id).zfill(5)
		
		salary_institution = SalaryInstitution.objects.get(id=record.salary_institution)
		
		item=MemberShipRequest(submission_status=submission_status,
			certification_status=certification_status,
			first_name=first_name,last_name=last_name,
			middle_name=middle_name,phone_number=phone_number,
			certification_officer=certification_officer,
			approval_officer=approval_officer,
			approval_status=approval_status,
			salary_institution=salary_institution,
			file_no=file_no,
			ippis_no=ippis_no,
			member_id=member_id,
			year=year,
			)
		item.save()
		record.transaction_status=transaction_status1
		record.save()

	applicants = MemberShipRequest.objects.filter(transaction_status=transaction_status)
	
	processed_by=CustomUser.objects.get(id=request.user.id)
	
	
	for applicant in applicants:

		receipt_obj=AutoReceipt.objects.first()
		receipt='C-' + str(receipt_obj.receipt.zfill(5))

		record=MemberShipFormSalesRecord(applicant=applicant,receipt=receipt,processed_by=processed_by,status=transaction_status)
		record.save()

		applicant.transaction_status=transaction_status1
		applicant.save()

		receipt_obj.receipt=int(receipt_obj.receipt) + 1
		receipt_obj.save()

	applicants= MemberShipFormSalesRecord.objects.filter(status=transaction_status)

	default_password = DefaultPassword.objects.first()
	password=default_password.title
	user_type_obj = UserType.objects.get(title='MEMBERS')
	user_type=user_type_obj.code

	
	for applicant in applicants:	
		member_id= applicant.applicant.member_id
		file_no = applicant.applicant.file_no
		ippis_no = applicant.applicant.ippis_no
		first_name=applicant.applicant.first_name
		last_name=applicant.applicant.last_name
		middle_name=applicant.applicant.middle_name 
		phone_number=applicant.applicant.phone_number 
		username = applicant.applicant.first_name + applicant.applicant.last_name + str(file_no).zfill(5)
		email = applicant.applicant.first_name + str(file_no).zfill(5) + "@gmail.com"	
		salary_institution = applicant.applicant.salary_institution
		

		user = CustomUser.objects.create_user(username=username,password=password,email=email,last_name=last_name,first_name=first_name,user_type=int(user_type))
		user.members.applicant=applicant
		user.members.member_id=member_id
		user.members.middle_name=middle_name
		user.members.full_name=str(first_name) + ' ' + str(last_name) + ' ' + str(middle_name)
		user.members.phone_number=phone_number
		user.members.salary_institution=salary_institution
		user.members.file_no=file_no
		user.members.ippis_no=ippis_no
		user.save()

		applicant.status=transaction_status1
		applicant.save()

	return HttpResponseRedirect(reverse('Norminal_Roll_Preview'))


############################################################################
################# UPLOADING EXISTING SAVINGS ###############################
############################################################################

def Uploading_Existing_Savings(request):
	DataCapture=DataCaptureManager.objects.first()
	savings_status=SavingsUploadStatus.objects.get(title='PENDING')
	records=Members.objects.filter(savings_status=savings_status)

	context={
	'records':records,
	'DataCapture':DataCapture,
	}
	return render(request,'deskofficer_templates/Uploading_Existing_Savings.html',context)



def Uploading_Existing_Savings_Preview(request,pk):
	DataCapture=DataCaptureManager.objects.first()
	form=Uploading_Existing_Savings_form(request.POST or None)
	member_id=Members.objects.get(id=pk)

	records=SavingsUploaded.objects.filter(transaction__member=member_id)
	
	if request.method=="POST":
		transaction_status=TransactionStatus.objects.get(title='UNTREATED')
		status=MembershipStatus.objects.get(title='ACTIVE')
		
		if TransactionPeriods.objects.filter(status=status).exists():
			transaction_period=TransactionPeriods.objects.get(status=status)
		else:
			messages.error(request,"Please setup transaction Period")
			return HttpResponseRedirect(reverse('Uploading_Existing_Savings_Preview',args=(pk,)))

		balance=request.POST.get('balance')
		schedule_amount=request.POST.get('schedule_amount')
		processed_by=CustomUser.objects.get(id=request.user.id)

		transaction_id=request.POST.get('transactions')
		transaction=TransactionTypes.objects.get(id=transaction_id)
		formatted_date = defaultfilters.date(transaction_period.transaction_period, "SHORT_DATE_FORMAT")
		particulars="Balance Brought Forward as at " + str(formatted_date)
		
		if float(balance)<=0:
			messages.error(request,"Balance Brought Forward must be greater than zero")
			return HttpResponseRedirect(reverse('Uploading_Existing_Savings_Preview',args=(pk,)))

		member=MembersAccountsDomain.objects.get(member=member_id,transaction=transaction)

		if SavingsUploaded.objects.filter(transaction=member).exists():
			record=SavingsUploaded.objects.get(transaction=member)
			record.particulars=particulars
			record.balance=balance
			record.schedule_amount=schedule_amount,
			record.processed_by=processed_by
			record.status=transaction_status
			record.transaction_period=transaction_period
			record.save()
			messages.success(request,"Record Updated Successfully")
		else:
			record=SavingsUploaded(transaction=member,particulars=particulars,balance=balance,schedule_amount=schedule_amount,processed_by=processed_by,status=transaction_status,transaction_period=transaction_period)
			record.save()
			messages.success(request,"Record Addedd Successfully")
		
		return HttpResponseRedirect(reverse('Uploading_Existing_Savings_Preview',args=(pk,)))
	context={
	'member':member_id,
	'form':form,
	'records':records,
	'return_pk':pk,
	'DataCapture':DataCapture,
	}
	return render(request,'deskofficer_templates/Uploading_Existing_Savings_Preview.html',context)


def Uploading_Existing_Savings_validate(request,pk):
	DataCapture=DataCaptureManager.objects.first()
	lock_status=LockedStatus.objects.get(title='LOCKED')
	savings_status=SavingsUploadStatus.objects.get(title='UPLOADED')
	status=TransactionStatus.objects.get(title='UNTREATED')

	status1=MembershipStatus.objects.get(title='ACTIVE')
	transaction_period=TransactionPeriods.objects.get(status=status1)

	member=Members.objects.get(id=pk)

	if SavingsUploaded.objects.filter(transaction__member=member,status=status).exists():
		

		records=SavingsUploaded.objects.filter(transaction__member=member,status=status)

		for item in records:
			transaction_id=item.transaction.transaction_id
			transaction=TransactionTypes.objects.get(id=transaction_id)

			particulars=item.particulars
			debit=0
			credit=item.balance
			balance=item.balance
			schedule_amount=item.schedule_amount
			account_number=str(item.transaction.account_number)
			
			member_selected=MembersAccountsDomain.objects.get(account_number=account_number)

			if StandingOrderAccounts.objects.filter(transaction=member_selected).exists():
				standing_order=StandingOrderAccounts.objects.get(transaction=member_selected)
				standing_order.amount=schedule_amount
				standing_order.lock_status=lock_status
				standing_order.save()
			
			else:
				
				standing_order=StandingOrderAccounts(transaction=member_selected,amount=schedule_amount,lock_status=lock_status,status=status1)
				standing_order.save()


			if PersonalLedger.objects.filter(member=member,transaction=transaction,account_number=account_number).exists():
				pass
			else:
				ledger_posting=PersonalLedger(member=member,transaction=transaction,account_number=account_number,debit=debit,credit=credit,balance=balance,particulars=particulars,transaction_period=transaction_period.transaction_period)
				ledger_posting.save()
			
			
			
			transaction_status=TransactionStatus.objects.get(title='TREATED')
			
			item.status=transaction_status
			item.save()	


		
		member.savings_status=savings_status
		member.save()

		messages.success(request,"Record Validated Successfully")
	else:
		messages.error(request,"No Record Found")
	return HttpResponseRedirect(reverse('Uploading_Existing_Savings'))



def Uploading_Existing_Savings_delete(request,pk,return_pk):
	record=SavingsUploaded.objects.get(id=pk)
	record.delete()
	return HttpResponseRedirect(reverse('Uploading_Existing_Savings_Preview',args=(return_pk,)))




##################################################################
###################### Additional Savings Upload #################
###################################################################
def Uploading_Existing_Savings_Additional_search(request):
	DataCapture=DataCaptureManager.objects.first()
	title="Search Members for Savings Upload"
	form = searchForm(request.POST or None)
	return render(request,'deskofficer_templates/Uploading_Existing_Savings_Additional_search.html',{'form':form,'title':title,'DataCapture':DataCapture,})


def Uploading_Existing_Savings_Additional_list_load(request):
	DataCapture=DataCaptureManager.objects.first()
	title="LIST OF MEMBERS FOR SAVINGS UPLOAD"
	form = searchForm(request.POST)
	if request.method == "POST":
		if request.POST.get("title")=="":
			return HttpResponseRedirect(reverse('Uploading_Existing_Savings_Additional_search'))

		status=MembershipStatus.objects.get(title='ACTIVE')
		savings_status=SavingsUploadStatus.objects.get(title='PENDING')
		form = searchForm(request.POST)
		members=Members.objects.filter(Q(file_no__icontains=form['title'].value()) |Q(ippis_no__icontains=form['title'].value()) |Q(phone_number__icontains=form['title'].value()) | Q(admin__first_name__icontains=form['title'].value()) | Q(admin__last_name__icontains=form['title'].value()) | Q(middle_name__icontains=form['title'].value())).filter(status=status).filter(~Q(savings_status=savings_status))
		context={
		'members':members,
		'title':title,
		'DataCapture':DataCapture,
		}
		return render(request,'deskofficer_templates/Uploading_Existing_Savings_Additional_list_load.html',context)


def Uploading_Existing_Savings_Additional_Preview(request,pk):
	DataCapture=DataCaptureManager.objects.first()
	form=Uploading_Existing_Savings_form(request.POST or None)
	member=Members.objects.get(id=pk)
	records=SavingsUploaded.objects.filter(transaction__member=member)

	if request.method=="POST":
		transaction_status=TransactionStatus.objects.get(title='UNTREATED')
		status=MembershipStatus.objects.get(title='ACTIVE')
		
		if TransactionPeriods.objects.filter(status=status).exists():
			transaction_period=TransactionPeriods.objects.get(status=status)
		else:
			messages.error(request,"Please setup transaction Period")
			return HttpResponseRedirect(reverse('Uploading_Existing_Savings_Additional_Preview',args=(pk,)))

		balance=request.POST.get('balance')
		schedule_amount=request.POST.get('schedule_amount')
		processed_by=CustomUser.objects.get(id=request.user.id)

		transaction_id=request.POST.get('transactions')
		transaction_selected=TransactionTypes.objects.get(id=transaction_id)
		transaction=MembersAccountsDomain.objects.get(member=member,transaction=transaction_selected)
		
		formatted_date = defaultfilters.date(transaction_period.transaction_period, "SHORT_DATE_FORMAT")
		particulars="Balance Brought Forward as at " + str(formatted_date)
		
		if float(balance)<=0:
			messages.error(request,"Balance Brought Forward must be greater than zero")
			return HttpResponseRedirect(reverse('Uploading_Existing_Savings_Additional_Preview',args=(pk,)))

		
		if SavingsUploaded.objects.filter(transaction__member=member,transaction=transaction,status=transaction_status).exists():
		
			record=SavingsUploaded.objects.get(transaction__member=member,transaction=transaction,status=transaction_status)
			record.particulars=particulars
			record.balance=float(balance)
			record.schedule_amount=float(schedule_amount)
			record.processed_by=processed_by
			record.status=transaction_status
			record.transaction_period=transaction_period
			record.save()
			messages.success(request,"Record Updated Successfully")

		elif SavingsUploaded.objects.filter(transaction__member=member,transaction=transaction).filter(~Q(status=transaction_status)).exists():
			messages.error(request,"Record Cannot be Altered, It is already validated")

		else:
			record=SavingsUploaded(particulars=particulars,transaction=transaction,balance=balance,schedule_amount=schedule_amount,processed_by=processed_by,status=transaction_status,transaction_period=transaction_period)
			record.save()
			messages.success(request,"Record Addedd Successfully")
		
		return HttpResponseRedirect(reverse('Uploading_Existing_Savings_Additional_Preview',args=(pk,)))
	context={
	'member':member,
	'form':form,
	'records':records,
	'return_pk':pk,
	'DataCapture':DataCapture,
	}
	return render(request,'deskofficer_templates/Uploading_Existing_Savings_Additional_Preview.html',context)



def Uploading_Existing_Savings_Additional_delete(request,pk,return_pk):
	record=SavingsUploaded.objects.get(id=pk)
	record.delete()
	return HttpResponseRedirect(reverse('Uploading_Existing_Savings_Additional_Preview',args=(return_pk,)))


def Uploading_Existing_Savings_Additional_validate(request,pk):
	DataCapture=DataCaptureManager.objects.first()
	lock_status=LockedStatus.objects.get(title='LOCKED')
	savings_status=SavingsUploadStatus.objects.get(title='UPLOADED')
	status=TransactionStatus.objects.get(title='UNTREATED')

	status1=MembershipStatus.objects.get(title='ACTIVE')
	transaction_period=TransactionPeriods.objects.get(status=status1)


	member=Members.objects.get(id=pk)

	if SavingsUploaded.objects.filter(transaction__member=member,status=status).exists():
		

		records=SavingsUploaded.objects.filter(transaction__member=member,status=status)

		for item in records:
			transaction_id=item.transaction.transaction_id
			transaction=TransactionTypes.objects.get(id=transaction_id)

			particulars=item.particulars
			debit=0
			credit=item.balance
			balance=item.balance
			schedule_amount=item.schedule_amount
			account_number=str(item.transaction.account_number)
			
			member_selected=MembersAccountsDomain.objects.get(account_number=account_number)

			if StandingOrderAccounts.objects.filter(transaction=member_selected).exists():
				standing_order=StandingOrderAccounts.objects.get(transaction=member_selected)
				standing_order.amount=schedule_amount
				standing_order.lock_status=lock_status
				standing_order.save()
			
			else:
				
				standing_order=StandingOrderAccounts(transaction=member_selected,amount=schedule_amount,lock_status=lock_status,status=status1)
				standing_order.save()


			if PersonalLedger.objects.filter(member=member,transaction=transaction,account_number=account_number).exists():
				pass
			else:
				ledger_posting=PersonalLedger(member=member,transaction=transaction,account_number=account_number,debit=debit,credit=credit,balance=balance,particulars=particulars,transaction_period=transaction_period.transaction_period)
				ledger_posting.save()
			
			
			
			transaction_status=TransactionStatus.objects.get(title='TREATED')
			
			item.status=transaction_status
			item.save()	


		
		member.savings_status=savings_status
		member.save()

		messages.success(request,"Record Validated Successfully")
		return HttpResponseRedirect(reverse('Uploading_Existing_Savings_Additional_search'))
	else:
		messages.error(request,"No Record Found")
		return HttpResponseRedirect(reverse('Uploading_Existing_Savings_Additional_validate', args=(pk,)))


########################################################################
############################# UPLOADING EXISTING ADDITIONAL LOANS ######
#########################################################################
def Uploading_Existing_Aditional_Loans(request):
	DataCapture=DataCaptureManager.objects.first()
	loan_status=LoansUploadStatus.objects.get(title='PENDING')
	records=Members.objects.filter(~Q(loan_status=loan_status))

	context={
	'records':records,
	'DataCapture':DataCapture,
	}
	return render(request,'deskofficer_templates/Uploading_Existing_Aditional_Loans.html',context)


def Uploading_Existing_Additional_Loans_Preview(request,pk):
	DataCapture=DataCaptureManager.objects.first()
	form=Uploading_Existing_Loans_form(request.POST or None)
	member=Members.objects.get(id=pk)
	records=LoansUploaded.objects.filter(member=member)


	if request.method=="POST":
		transaction_status=TransactionStatus.objects.get(title='UNTREATED')
		status=MembershipStatus.objects.get(title='ACTIVE')
		transaction_period=TransactionPeriods.objects.get(status=status)

		formatted_date = defaultfilters.date(transaction_period.transaction_period, "SHORT_DATE_FORMAT")
		particulars="Balance Brought Forward as at " + str(formatted_date)
		
		transaction_id=request.POST.get('transactions')
		transaction=TransactionTypes.objects.get(id=transaction_id)

		interest_deduction_id=request.POST.get('interest_deductions')
		interest_deduction=InterestDeductionSource.objects.get(id=interest_deduction_id)


		loan_amount=request.POST.get('loan_amount')
		if float(loan_amount)<=0:
			messages.error(request,'Loan Amount cannot be zero')
			return HttpResponseRedirect(reverse('Uploading_Existing_Additional_Loans_Preview',args=(pk,)))

		balance=float(request.POST.get('balance'))
		if abs(float(balance))<=0:
			messages.error(request,'Balance Brought Forward cannot be zero')
			return HttpResponseRedirect(reverse('Uploading_Existing_Additional_Loans_Preview',args=(pk,)))

		amount_paid=float(loan_amount) - float(balance)
		repayment=request.POST.get('repayment')
		if float(repayment)<=0:
			messages.error(request,'Monthly Repayment cannot be zero')
			return HttpResponseRedirect(reverse('Uploading_Existing_Additional_Loans_Preview',args=(pk,)))


		interest_rate=request.POST.get('interest_rate')
		if int(interest_rate)<=0:
			messages.error(request,'Interest Rate cannot be zero')
			return HttpResponseRedirect(reverse('Uploading_Existing_Additional_Loans_Preview',args=(pk,)))


		duration=request.POST.get('duration')
		if int(duration)<=0:
			messages.error(request,'Duration cannot be zero')
			return HttpResponseRedirect(reverse('Uploading_Existing_Additional_Loans_Preview',args=(pk,)))

		if float(balance) > float(loan_amount):
			messages.error(request,'Loan Balance cannot be greater than Loan Amount')
			return HttpResponseRedirect(reverse('Uploading_Existing_Additional_Loans_Preview',args=(pk,)))

		if float(repayment) > abs(float(balance)) or float(repayment)>float(loan_amount):
			messages.error(request,'Monthly repayment cannot be greater than Loan Amount or Balance')
			return HttpResponseRedirect(reverse('Uploading_Existing_Additional_Loans_Preview',args=(pk,)))
		


		start_date_id=request.POST.get('start_date')
		start_date=datetime.datetime.strptime(start_date_id, '%Y-%m-%d')	
		stop_date = start_date+ relativedelta(months=int(duration))
		


		processed_by=CustomUser.objects.get(id=request.user.id)


		if LoansUploaded.objects.filter(member=member,transaction=transaction).exists():
			record=LoansUploaded.objects.get(member=member,transaction=transaction)
			record.particulars=particulars
			record.loan_amount=loan_amount
			record.amount_paid=amount_paid
			record.balance=balance
			record.repayment=repayment,
			record.interest_rate=interest_rate,
			record.duration=duration,
			record.interest_deduction=interest_deduction,
			record.start_date=start_date,
			record.stop_date=stop_date,
			record.processed_by=processed_by
			record.status=transaction_status
			record.transaction_period=transaction_period
			record.save()
			messages.success(request,"Record Updated Successfully")
		else:
			record=LoansUploaded(member=member,
				particulars=particulars,
				transaction=transaction,
				loan_amount=loan_amount,
				amount_paid=amount_paid,
				balance=balance,
				repayment=repayment,
				interest_rate=interest_rate,
				duration=duration,
				interest_deduction=interest_deduction,
				start_date=start_date,
				stop_date=stop_date,
				processed_by=processed_by,status=transaction_status,transaction_period=transaction_period)
			record.save()
			messages.success(request,"Record Addedd Successfully")
		
		return HttpResponseRedirect(reverse('Uploading_Existing_Additional_Loans_Preview',args=(pk,)))
	form.fields['start_date'].initial=now
	context={
	'member':member,
	'form':form,
	'records':records,
	'return_pk':pk,
	'DataCapture':DataCapture,
	}
	return render(request,'deskofficer_templates/Uploading_Existing_Additional_Loans_Preview.html',context)



def Uploading_Existing_Additional_Loans_validate(request,pk):
	DataCapture=DataCaptureManager.objects.first()
	member=Members.objects.get(id=pk)

	loan_status=LoansUploadStatus.objects.get(title='UPLOADED')
	status = TransactionStatus.objects.get(title='UNTREATED')
	status1=MembershipStatus.objects.get(title='ACTIVE')
		
	
	transaction_period=TransactionPeriods.objects.get(status=status1)
	formatted_date = defaultfilters.date(transaction_period.transaction_period, "SHORT_DATE_FORMAT")
	particulars="Balance Brought Forward as at " + str(formatted_date)



	if LoansUploaded.objects.filter(member=member,status=status).exists():
	
		loan_records=LoansUploaded.objects.filter(member=member,status=status)

		for record in loan_records:
			transaction_id=record.transaction_id
			transaction=TransactionTypes.objects.get(id=transaction_id)		

			member_id=list((member.member_id).split("/"))
			my_id=member_id[2]
			particulars=record.particulars
			debit=abs(record.balance)
			credit=0
			balance=-record.balance
			amount_paid=record.amount_paid
			
			repayment=record.repayment
			loan_amount=record.loan_amount
			repayment=record.repayment
			duration=record.duration
			
			interest_rate=record.interest_rate
			interest_deduction=record.interest_deduction
			start_date=record.start_date
			stop_date=record.stop_date
			processed_by=CustomUser.objects.get(id=request.user.id)

			
			now = datetime.datetime.now()
			

			loan_code=transaction.code
			if LoanNumber.objects.all().count() == 0:
				messages.error(request,"Loan Number not Set")
				return HttpResponseRedirect(reverse('Uploading_Existing_Loans_Preview',args=(pk,)))

			loan_number_selector_id=LoanNumber.objects.first()
			loan_number_selector=loan_number_selector_id.code

			current_time= str(now.year) + str(now.month) + str(now.day) + str(now.hour) + str(now.minute)  
			loan_number=str(loan_code) + str(my_id) + str(current_time) + str(loan_number_selector).zfill(5)

			loan_number_selector_id.code=int(loan_number_selector)+1
			loan_number_selector_id.save()

			if PersonalLedger.objects.filter(member=member,transaction=transaction).exists():
				pass
			else:
				ledger_posting=PersonalLedger(member=member,transaction=transaction,account_number=loan_number,debit=debit,credit=credit,balance=balance,particulars=particulars,transaction_period=transaction_period.transaction_period)
				ledger_posting.save()
				
				ledger_status=MembershipStatus.objects.get(title='ACTIVE')
				if LoansRepaymentBase.objects.filter(member=member,transaction=transaction,status=ledger_status).exists():
					pass
				else:
					loan_record=LoansRepaymentBase(member=member,transaction=transaction,loan_number=loan_number,
						loan_amount=loan_amount,
						repayment=repayment,
						balance=balance,
						amount_paid=amount_paid,
						start_date=start_date,
						stop_date=stop_date,
						processed_by=processed_by,
						status=status1)
					loan_record.save()
					
					loan_record=LoansDisbursed(member=member,transaction=transaction,loan_number=loan_number,
						loan_amount=loan_amount,
						interest_deduction=interest_deduction,
						interest_rate=interest_rate,
						duration=duration,
						repayment=repayment,
						balance=balance,
						amount_paid=amount_paid,
						start_date=start_date,
						stop_date=stop_date,
						processed_by=processed_by,
						status=status1)
					loan_record.save()
			
			transaction_status=TransactionStatus.objects.get(title='TREATED')
			
			record.status=transaction_status
			record.save()	

		member.loan_status=loan_status
		member.save()
		messages.success(request,"Record Validated Successfully")


	else:
		messages.error(request,"No Record Found")
	return HttpResponseRedirect(reverse('Uploading_Existing_Aditional_Loans'))



def Uploading_Existing_Additional_Loans_delete(request,pk,return_pk):
	record=LoansUploaded.objects.get(id=pk)
	record.delete()
	return HttpResponseRedirect(reverse('Uploading_Existing_Additional_Loans_Preview',args=(return_pk,)))


########################################################################
############################# UPLOADING EXISTING LOANS #################
#########################################################################


def Uploading_Existing_Loans(request):
	DataCapture=DataCaptureManager.objects.first()
	loan_status=LoansUploadStatus.objects.get(title='PENDING')
	records=Members.objects.filter(loan_status=loan_status)

	context={
	'records':records,
	'DataCapture':DataCapture,
	}
	return render(request,'deskofficer_templates/Uploading_Existing_Loans.html',context)


def Uploading_Existing_Loans_Preview(request,pk):
	DataCapture=DataCaptureManager.objects.first()
	form=Uploading_Existing_Loans_form(request.POST or None)
	member=Members.objects.get(id=pk)
	records=LoansUploaded.objects.filter(member=member)


	if request.method=="POST":
		transaction_status=TransactionStatus.objects.get(title='UNTREATED')
		status=MembershipStatus.objects.get(title='ACTIVE')
		transaction_period=TransactionPeriods.objects.get(status=status)

		formatted_date = defaultfilters.date(transaction_period.transaction_period, "SHORT_DATE_FORMAT")
		particulars="Balance Brought Forward as at " + str(formatted_date)
		
		transaction_id=request.POST.get('transactions')
		transaction=TransactionTypes.objects.get(id=transaction_id)

		interest_deduction_id=request.POST.get('interest_deductions')
		interest_deduction=InterestDeductionSource.objects.get(id=interest_deduction_id)


		loan_amount=request.POST.get('loan_amount')
		if float(loan_amount)<=0:
			messages.error(request,'Loan Amount cannot be zero')
			return HttpResponseRedirect(reverse('Uploading_Existing_Loans_Preview',args=(pk,)))

		balance=float(request.POST.get('balance'))
		if abs(float(balance))<=0:
			messages.error(request,'Balance Brought Forward cannot be zero')
			return HttpResponseRedirect(reverse('Uploading_Existing_Loans_Preview',args=(pk,)))

		amount_paid=float(loan_amount) - float(balance)
		repayment=request.POST.get('repayment')
		if float(repayment)<=0:
			messages.error(request,'Monthly Repayment cannot be zero')
			return HttpResponseRedirect(reverse('Uploading_Existing_Loans_Preview',args=(pk,)))


		interest_rate=request.POST.get('interest_rate')
		if int(interest_rate)<=0:
			messages.error(request,'Interest Rate cannot be zero')
			return HttpResponseRedirect(reverse('Uploading_Existing_Loans_Preview',args=(pk,)))


		duration=request.POST.get('duration')
		if int(duration)<=0:
			messages.error(request,'Duration cannot be zero')
			return HttpResponseRedirect(reverse('Uploading_Existing_Loans_Preview',args=(pk,)))

		if float(balance) > float(loan_amount):
			messages.error(request,'Loan Balance cannot be greater than Loan Amount')
			return HttpResponseRedirect(reverse('Uploading_Existing_Loans_Preview',args=(pk,)))

		if float(repayment) > abs(float(balance)) or float(repayment)>float(loan_amount):
			messages.error(request,'Monthly repayment cannot be greater than Loan Amount or Balance')
			return HttpResponseRedirect(reverse('Uploading_Existing_Loans_Preview',args=(pk,)))
		


		start_date_id=request.POST.get('start_date')
		start_date=datetime.datetime.strptime(start_date_id, '%Y-%m-%d')	
		stop_date = start_date+ relativedelta(months=int(duration))
		


		processed_by=CustomUser.objects.get(id=request.user.id)


		if LoansUploaded.objects.filter(member=member,transaction=transaction).exists():
			record=LoansUploaded.objects.get(member=member,transaction=transaction)
			record.particulars=particulars
			record.loan_amount=loan_amount
			record.amount_paid=amount_paid
			record.balance=balance
			record.repayment=repayment,
			record.interest_rate=interest_rate,
			record.duration=duration,
			record.interest_deduction=interest_deduction,
			record.start_date=start_date,
			record.stop_date=stop_date,
			record.processed_by=processed_by
			record.status=transaction_status
			record.transaction_period=transaction_period
			record.save()
			messages.success(request,"Record Updated Successfully")
		else:
			record=LoansUploaded(member=member,
				particulars=particulars,
				transaction=transaction,
				loan_amount=loan_amount,
				amount_paid=amount_paid,
				balance=balance,
				repayment=repayment,
				interest_rate=interest_rate,
				duration=duration,
				interest_deduction=interest_deduction,
				start_date=start_date,
				stop_date=stop_date,
				processed_by=processed_by,status=transaction_status,transaction_period=transaction_period)
			record.save()
			messages.success(request,"Record Addedd Successfully")
		
		return HttpResponseRedirect(reverse('Uploading_Existing_Loans_Preview',args=(pk,)))
	form.fields['start_date'].initial=now
	context={
	'member':member,
	'form':form,
	'records':records,
	'return_pk':pk,
	'DataCapture':DataCapture,
	}
	return render(request,'deskofficer_templates/Uploading_Existing_Loans_Preview.html',context)



def Uploading_Existing_Loans_validate(request,pk):
	DataCapture=DataCaptureManager.objects.first()
	member=Members.objects.get(id=pk)

	loan_status=LoansUploadStatus.objects.get(title='UPLOADED')
	status = TransactionStatus.objects.get(title='UNTREATED')
	status1=MembershipStatus.objects.get(title='ACTIVE')
		
	
	transaction_period=TransactionPeriods.objects.get(status=status1)
	formatted_date = defaultfilters.date(transaction_period.transaction_period, "SHORT_DATE_FORMAT")
	particulars="Balance Brought Forward as at " + str(formatted_date)



	if LoansUploaded.objects.filter(member=member,status=status).exists():
	
		loan_records=LoansUploaded.objects.filter(member=member,status=status)

		for record in loan_records:
			transaction_id=record.transaction_id
			transaction=TransactionTypes.objects.get(id=transaction_id)		

			member_id=list((member.member_id).split("/"))
			my_id=member_id[2]
			particulars=record.particulars
			debit=abs(record.balance)
			credit=0
			balance=-record.balance
			amount_paid=record.amount_paid
			
			repayment=record.repayment
			loan_amount=record.loan_amount
			repayment=record.repayment
			duration=record.duration
			
			interest_rate=record.interest_rate
			interest_deduction=record.interest_deduction
			start_date=record.start_date
			stop_date=record.stop_date
			processed_by=CustomUser.objects.get(id=request.user.id)

			
			now = datetime.datetime.now()
			

			loan_code=transaction.code
			if LoanNumber.objects.all().count() == 0:
				messages.error(request,"Loan Number not Set")
				return HttpResponseRedirect(reverse('Uploading_Existing_Loans_Preview',args=(pk,)))

			loan_number_selector_id=LoanNumber.objects.first()
			loan_number_selector=loan_number_selector_id.code

			current_time= str(now.year) + str(now.month) + str(now.day) + str(now.hour) + str(now.minute)  
			loan_number=str(loan_code) + str(my_id) + str(current_time) + str(loan_number_selector).zfill(5)

			loan_number_selector_id.code=int(loan_number_selector)+1
			loan_number_selector_id.save()

			if PersonalLedger.objects.filter(member=member,transaction=transaction).exists():
				pass
			else:
				ledger_posting=PersonalLedger(member=member,transaction=transaction,account_number=loan_number,debit=debit,credit=credit,balance=balance,particulars=particulars,transaction_period=transaction_period.transaction_period)
				ledger_posting.save()
				
				ledger_status=MembershipStatus.objects.get(title='ACTIVE')
				if LoansRepaymentBase.objects.filter(member=member,transaction=transaction,status=ledger_status).exists():
					pass
				else:
					loan_record=LoansRepaymentBase(member=member,transaction=transaction,loan_number=loan_number,
						loan_amount=loan_amount,
						repayment=repayment,
						balance=balance,
						amount_paid=amount_paid,
						start_date=start_date,
						stop_date=stop_date,
						processed_by=processed_by,
						status=status1)
					loan_record.save()
					
					loan_record=LoansDisbursed(member=member,transaction=transaction,loan_number=loan_number,
						loan_amount=loan_amount,
						interest_deduction=interest_deduction,
						interest_rate=interest_rate,
						duration=duration,
						repayment=repayment,
						balance=balance,
						amount_paid=amount_paid,
						start_date=start_date,
						stop_date=stop_date,
						processed_by=processed_by,
						status=status1)
					loan_record.save()
			
			transaction_status=TransactionStatus.objects.get(title='TREATED')
			
			record.status=transaction_status
			record.save()	

		member.loan_status=loan_status
		member.save()
		messages.success(request,"Record Validated Successfully")


	else:
		messages.error(request,"No Record Found")
	return HttpResponseRedirect(reverse('Uploading_Existing_Loans'))


def Uploading_Existing_Loans_delete(request,pk,return_pk):
	record=LoansUploaded.objects.get(id=pk)
	record.delete()
	return HttpResponseRedirect(reverse('Uploading_Existing_Loans_Preview',args=(return_pk,)))




########################################################################
############################# UPDATING SALARY GROSS PAY##################
#########################################################################
def Updating_Salary_Grosspay_list_load(request):
	DataCapture=DataCaptureManager.objects.first()
	status=MembershipStatus.objects.get(title="ACTIVE")
	salary_status=SavingsUploadStatus.objects.get(title='PENDING')
	# records=Members.objects.filter(status=status).filter(Q(gender__title__isnull=True) | Q(gender__title=""))
	records=Members.objects.filter(status=status).filter(Q(salary_status__title__isnull=True) | Q(salary_status__title=""))

	context={
	'records':records,
	'DataCapture':DataCapture,
	}
	return render(request,'deskofficer_templates/Updating_Salary_Grosspay_list_load.html',context)

########################################################################
############################# DATE JOINED  ######################
#########################################################################

def Updating_Date_Joined(request):
	DataCapture=DataCaptureManager.objects.first()
	status=MembershipStatus.objects.get(title="ACTIVE")
	date_joined_status=DateJoinedUploadStatus.objects.get(title='PENDING')
	records=Members.objects.filter(date_joined_status=date_joined_status,status=status)

	context={
	'records':records,
	'DataCapture':DataCapture,
	}
	return render(request,'deskofficer_templates/Updating_Date_Joined_List_load.html',context)


def Updating_Date_Joined_Preview(request,pk):
	DataCapture=DataCaptureManager.objects.first()
	form=Updating_Date_Joined__form(request.POST or None)
	date_joined_status=DateJoinedUploadStatus.objects.get(title='VERIFIED')

	member=Members.objects.get(id=pk)

	if request.method == "POST":
		date_joined=request.POST.get('date_joined')

		member.date_joined=date_joined
		member.date_joined_status=date_joined_status
		member.save()
		return HttpResponseRedirect(reverse('Updating_Date_Joined'))
	context={
	'member':member,
	'form':form,
	'DataCapture':DataCapture,
	}
	return render(request,'deskofficer_templates/Updating_Date_Joined_Preview.html',context)



def Updating_Date_Joined_Manage_List_load(request):
	DataCapture=DataCaptureManager.objects.first()
	status=MembershipStatus.objects.get(title="ACTIVE")
	date_joined_status=DateJoinedUploadStatus.objects.get(title='PENDING')
	records=Members.objects.filter(~Q(date_joined_status=date_joined_status)).filter(status=status)

	context={
	'records':records,
	'DataCapture':DataCapture,
	}
	return render(request,'deskofficer_templates/Updating_Date_Joined_Manage_List_load.html',context)

def Updating_Date_Joined_Manage_Preview(request,pk):
	form=Updating_Date_Joined__form(request.POST or None)
	date_joined_status=DateJoinedUploadStatus.objects.get(title='VERIFIED')

	member=Members.objects.get(id=pk)
	form.fields['date_joined'].initial= member.date_joined

	if request.method == "POST":
		date_joined=request.POST.get('date_joined')


		member.date_joined=date_joined
		member.date_joined_status=date_joined_status
		member.save()
		return HttpResponseRedirect(reverse('Updating_Date_Joined_Manage_List_load'))
	context={
	'member':member,
	'form':form,
	'DataCapture':DataCapture,
	}
	return render(request,'deskofficer_templates/Updating_Date_Joined_Manage_Preview.html',context)


########################################################################
############################# UPDATING GROSS PAY ######################
#########################################################################
def Updating_Gross_Pay_selected_search(request):
	DataCapture=DataCaptureManager.objects.first()
	title="Search Members for Salary Grosspay Upload"
	form = searchForm(request.POST or None)
	return render(request,'deskofficer_templates/Updating_Gross_Pay_selected_search.html',{'form':form,'title':title,'DataCapture':DataCapture,})


def Updating_Gross_Pay_selected_list_load(request):
	DataCapture=DataCaptureManager.objects.first()
	title="LIST OF MEMBERS FOR SAVINGS UPLOAD"
	form = searchForm(request.POST)
	if request.method == "POST":
		if request.POST.get("title")=="":
			return HttpResponseRedirect(reverse('Updating_Gross_Pay_selected_search'))

		status=MembershipStatus.objects.get(title='ACTIVE')
		savings_status=SavingsUploadStatus.objects.get(title='PENDING')
		form = searchForm(request.POST)
		members=Members.objects.filter(Q(file_no__icontains=form['title'].value()) |Q(ippis_no__icontains=form['title'].value()) |Q(phone_number__icontains=form['title'].value()) | Q(admin__first_name__icontains=form['title'].value()) | Q(admin__last_name__icontains=form['title'].value()) | Q(middle_name__icontains=form['title'].value())).filter(status=status)
		context={
		'members':members,
		'title':title,
		'DataCapture':DataCapture,
		}
		return render(request,'deskofficer_templates/Updating_Gross_Pay_selected_list_load.html',context)


def Updating_Gross_Pay_selected_Preview(request,pk):
	DataCapture=DataCaptureManager.objects.first()
	form=Updating_Gross_Pay_Preview_form(request.POST or None)
	gross_pay_status=ProcessingStatus.objects.get(title='PROCESSED')
	# status=MembershipStatus.objects.get(title='ACTIVE')
	# transaction_period=TransactionPeriods.objects.get(status=status)
	now = datetime.datetime.now()

	formatted_date = defaultfilters.date(now, "SHORT_DATE_FORMAT")
	# formatted_date = defaultfilters.date(transaction_period.transaction_period, "SHORT_DATE_FORMAT")
		
	member=Members.objects.get(id=pk)

	form.fields['description'].initial= "Salary as at " + str(formatted_date)
	form.fields['gross_pay'].initial= member.gross_pay
	

	if request.method == "POST":
		description=request.POST.get('description')
		gross_pay=request.POST.get('gross_pay')

		member.gross_pay=gross_pay
		member.gross_pay_as_at=description
		member.gross_pay_status=gross_pay_status
		member.save()
		return HttpResponseRedirect(reverse('Updating_Gross_Pay_selected_search'))
	context={
	'member':member,
	'form':form,
	'DataCapture':DataCapture,
	}
	return render(request,'deskofficer_templates/Updating_Gross_Pay_selected_Preview.html',context)



def Updating_Gross_Pay(request):
	DataCapture=DataCaptureManager.objects.first()
	status=MembershipStatus.objects.get(title="ACTIVE")
	gross_pay_status=ProcessingStatus.objects.get(title='UNPROCESSED')
	records=Members.objects.filter(gross_pay_status=gross_pay_status,status=status)

	context={
	'records':records,
	'DataCapture':DataCapture,
	}
	return render(request,'deskofficer_templates/Updating_Gross_Pay.html',context)


def Updating_Gross_Pay_Preview(request,pk):
	DataCapture=DataCaptureManager.objects.first()
	form=Updating_Gross_Pay_Preview_form(request.POST or None)
	gross_pay_status=ProcessingStatus.objects.get(title='PROCESSED')
	# status=MembershipStatus.objects.get(title='ACTIVE')
	# transaction_period=TransactionPeriods.objects.get(status=status)
	now = datetime.datetime.now()

	formatted_date = defaultfilters.date(now, "SHORT_DATE_FORMAT")
	# formatted_date = defaultfilters.date(transaction_period.transaction_period, "SHORT_DATE_FORMAT")
		
	member=Members.objects.get(id=pk)

	form.fields['description'].initial= "Salary as at " + str(formatted_date)
	

	if request.method == "POST":
		description=request.POST.get('description')
		gross_pay=request.POST.get('gross_pay')

		member.gross_pay=gross_pay
		member.gross_pay_as_at=description
		member.gross_pay_status=gross_pay_status
		member.save()
		return HttpResponseRedirect(reverse('Updating_Gross_Pay'))
	context={
	'member':member,
	'form':form,
	'DataCapture':DataCapture,
	}
	return render(request,'deskofficer_templates/Updating_Gross_Pay_Preview.html',context)




def Updating_Gross_Pay_Manage(request):
	DataCapture=DataCaptureManager.objects.first()
	gross_pay_status=ProcessingStatus.objects.get(title='PROCESSED')
	records=Members.objects.filter(gross_pay_status=gross_pay_status)

	context={
	'records':records,
	'DataCapture':DataCapture,
	}
	return render(request,'deskofficer_templates/Updating_Gross_Pay_Manage.html',context)


def Updating_Gross_Pay_Manage_Preview(request,pk):
	DataCapture=DataCaptureManager.objects.first()
	form=Updating_Gross_Pay_Preview_form(request.POST or None)
	gross_pay_status=ProcessingStatus.objects.get(title='PROCESSED')
	
	member=Members.objects.get(id=pk)

	form.fields['description'].initial= member.gross_pay_as_at
	form.fields['gross_pay'].initial= member.gross_pay
	

	if request.method == "POST":
		description=request.POST.get('description')
		gross_pay=request.POST.get('gross_pay')

		member.gross_pay=gross_pay
		member.gross_pay_as_at=description
		member.gross_pay_status=gross_pay_status
		member.save()
		return HttpResponseRedirect(reverse('Updating_Gross_Pay_Manage'))
	context={
	'member':member,
	'form':form,
	'DataCapture':DataCapture,
	}
	return render(request,'deskofficer_templates/Updating_Gross_Pay_Manage_Preview.html',context)


########################################################################
############################# UPDATING NORMINAL ROLL#####################
#########################################################################

def Norminal_Roll(request):
	DataCapture=DataCaptureManager.objects.first()
	status=MembershipStatus.objects.get(title="ACTIVE")
	members=Members.objects.filter(status=status)

	context={
	'members':members,
	'DataCapture':DataCapture,
	}
	return render(request,'deskofficer_templates/Norminal_Roll.html',context)


def Norminal_Roll_Update(request,pk):
	DataCapture=DataCaptureManager.objects.first()
	form = Norminal_Roll_Update_form(request.POST or None)
	member=Members.objects.get(pk=pk)

	if request.method=='POST':
		title_id=request.POST.get('title')
		member.title=Titles.objects.get(id=title_id)

		member.last_name=request.POST.get('last_name')
		member.first_name=request.POST.get('first_name')
		member.middle_name=request.POST.get('middle_name')

		gender_id=request.POST.get('gender')
		member.gender=Gender.objects.get(id=gender_id)

		member.phone_number=request.POST.get('phone_number')
		department_id=request.POST.get('department')
		member.department=Departments.objects.get(id=department_id)

		salary_institution_id=request.POST.get('salary_institution')
		member.salary_institution=SalaryInstitution.objects.get(id=salary_institution_id)

		member.residential_address=request.POST.get('residential_address')
		member.permanent_home_address=request.POST.get('permanent_home_address')

		member.file_no=request.POST.get('file_no')
		member.ippis_no=request.POST.get('ippis_no')
		member.date_joined=request.POST.get('date_joined')
		member.save()
		return HttpResponseRedirect(reverse('Norminal_Roll'))

	form.fields['title'].initial= member.title_id
	form.fields['last_name'].initial= member.admin.last_name
	form.fields['first_name'].initial= member.admin.first_name
	form.fields['middle_name'].initial= member.middle_name

	form.fields['gender'].initial= member.gender_id
	form.fields['phone_number'].initial= member.phone_number
	form.fields['department'].initial= member.department_id

	form.fields['salary_institution'].initial= member.salary_institution_id
	form.fields['residential_address'].initial= member.residential_address
	form.fields['permanent_home_address'].initial= member.permanent_home_address

	form.fields['file_no'].initial= member.file_no
	form.fields['ippis_no'].initial= member.ippis_no
	form.fields['date_joined'].initial= member.date_joined

	context={
	'form':form,
	'member':member,
	'DataCapture':DataCapture,
	}
	return render(request,'deskofficer_templates/Norminal_Roll_Update.html',context)



########################################################################
############################# UPDATING TITLE ######################
#########################################################################

def Updating_Title_list_load(request):
	DataCapture=DataCaptureManager.objects.first()
	status=MembershipStatus.objects.get(title='ACTIVE')
	records=Members.objects.filter(status=status)

	context={
	'records':records,
	'DataCapture':DataCapture,
	}
	return render(request,'deskofficer_templates/Updating_Title_list_load.html',context)


def Updating_Updating_Title_Preview(request,pk):
	DataCapture=DataCaptureManager.objects.first()
	form=Updating_Title_Preview_form(request.POST or None)
	member=Members.objects.get(id=pk)
	if member.title:
		form.fields['title'].initial= member.title.id

	if request.method == "POST":
		title_id=request.POST.get('title')
		title=Titles.objects.get(id=title_id)

		member.title=title
		member.save()
		return HttpResponseRedirect(reverse('Updating_Title_list_load'))
	context={
	'member':member,
	'form':form,
	'DataCapture':DataCapture,
	}
	return render(request,'deskofficer_templates/Updating_Title_Preview.html',context)


def Updating_Updating_Title_Preview1(request,pk):
	DataCapture=DataCaptureManager.objects.first()
	form=Updating_Title_Preview_form(request.POST or None)
	member=Members.objects.get(id=pk)
	
	if member.title:
		form.fields['title'].initial= member.title.id

	if request.method == "POST":
		title_id=request.POST.get('title')
		title=Titles.objects.get(id=title_id)

		member.title=title
		member.save()
		return HttpResponseRedirect(reverse('Updating_Title_selected_search'))
	context={
	'member':member,
	'form':form,
	'DataCapture':DataCapture,
	}
	return render(request,'deskofficer_templates/Updating_Title_Preview.html',context)


def Updating_Title_selected_search(request):
	DataCapture=DataCaptureManager.objects.first()
	title="Search Members for Title Update"
	form = searchForm(request.POST or None)
	return render(request,'deskofficer_templates/Updating_Title_selected_search.html',{'form':form,'title':title,'DataCapture':DataCapture,})


def Updating_Title_selected_list_load(request):
	DataCapture=DataCaptureManager.objects.first()
	title="LIST OF MEMBERS"
	form = searchForm(request.POST)
	if request.method == "POST":
		if request.POST.get("title")=="":
			return HttpResponseRedirect(reverse('Updating_Title_selected_search'))

		status=MembershipStatus.objects.get(title='ACTIVE')
		form = searchForm(request.POST)
		members=Members.objects.filter(Q(file_no__icontains=form['title'].value()) |Q(ippis_no__icontains=form['title'].value()) |Q(phone_number__icontains=form['title'].value()) | Q(admin__first_name__icontains=form['title'].value()) | Q(admin__last_name__icontains=form['title'].value()) | Q(middle_name__icontains=form['title'].value())).filter(status=status)
		context={
		'members':members,
		'title':title,
		'DataCapture':DataCapture,
		}
		return render(request,'deskofficer_templates/Updating_Title_selected_list_load.html',context)



########################################################################
############################# UPDATING DEPARTMENTS ######################
#########################################################################

def Updating_Department_list_load(request):
	DataCapture=DataCaptureManager.objects.first()
	status=MembershipStatus.objects.get(title='ACTIVE')
	records=Members.objects.filter(status=status)

	context={
	'records':records,
	'DataCapture':DataCapture,
	}
	return render(request,'deskofficer_templates/Updating_Department_list_load.html',context)


def Updating_Updating_Department_Preview(request,pk):
	DataCapture=DataCaptureManager.objects.first()
	form=Updating_Updating_Department_Preview_form(request.POST or None)
	member=Members.objects.get(id=pk)
	if member.department:
		form.fields['department'].initial= member.department.id
	if request.method == "POST":
		department_id=request.POST.get('department')
		department=Departments.objects.get(id=department_id)

		member.department=department
		member.save()
		return HttpResponseRedirect(reverse('Updating_Department_list_load'))
	context={
	'member':member,
	'form':form,
	'DataCapture':DataCapture,
	}
	return render(request,'deskofficer_templates/Updating_Updating_Department_Preview.html',context)


def Updating_Updating_Department_Preview1(request,pk):
	DataCapture=DataCaptureManager.objects.first()
	form=Updating_Updating_Department_Preview_form(request.POST or None)
	member=Members.objects.get(id=pk)

	if member.department:
		form.fields['department'].initial= member.department.id

	if request.method == "POST":
		department_id=request.POST.get('department')
		department=Departments.objects.get(id=department_id)

		member.department=department
		member.save()
		return HttpResponseRedirect(reverse('Updating_Department_selected_search'))
	context={
	'member':member,
	'form':form,
	'DataCapture':DataCapture,
	}
	return render(request,'deskofficer_templates/Updating_Updating_Department_Preview.html',context)


def Updating_Department_selected_search(request):
	DataCapture=DataCaptureManager.objects.first()
	title="Search Members for Department Update"
	form = searchForm(request.POST or None)
	return render(request,'deskofficer_templates/Updating_Department_selected_search.html',{'form':form,'title':title,'DataCapture':DataCapture,})


def Updating_Department_selected_list_load(request):
	DataCapture=DataCaptureManager.objects.first()
	title="LIST OF MEMBERS"
	form = searchForm(request.POST)
	if request.method == "POST":
		if request.POST.get("title")=="":
			return HttpResponseRedirect(reverse('Updating_Department_selected_search'))

		status=MembershipStatus.objects.get(title='ACTIVE')
		form = searchForm(request.POST)
		members=Members.objects.filter(Q(file_no__icontains=form['title'].value()) |Q(ippis_no__icontains=form['title'].value()) |Q(phone_number__icontains=form['title'].value()) | Q(admin__first_name__icontains=form['title'].value()) | Q(admin__last_name__icontains=form['title'].value()) | Q(middle_name__icontains=form['title'].value())).filter(status=status)
		context={
		'members':members,
		'title':title,
		'DataCapture':DataCapture,
		}
		return render(request,'deskofficer_templates/Updating_Department_selected_list_load.html',context)




########################################################################
############################# UPDATING GENDER ######################
#########################################################################

def Updating_Gender_list_load(request):
	DataCapture=DataCaptureManager.objects.first()
	status=MembershipStatus.objects.get(title='ACTIVE')
	# records=Members.objects.filter(status=status).filter(Q(gender__title__isnull=True) | Q(gender__title=""))
	records=Members.objects.filter(status=status) #.filter(Q(gender__title__isnull=True) | Q(gender__title=""))

	context={
	'records':records,
	'DataCapture':DataCapture,
	}
	return render(request,'deskofficer_templates/Updating_Gender_list_load.html',context)


def Updating_Gender_Preview(request,pk):
	DataCapture=DataCaptureManager.objects.first()
	form=Updating_Gender_Preview_form(request.POST or None)
	member=Members.objects.get(id=pk)
	
	if member.gender:
		form.fields['gender'].initial= member.gender.id

	if request.method == "POST":
		gender_id=request.POST.get('gender')
		gender=Gender.objects.get(id=gender_id)

		member.gender=gender
		member.save()
		return HttpResponseRedirect(reverse('Updating_Gender_list_load'))
	context={
	'member':member,
	'form':form,
	'DataCapture':DataCapture,
	}
	return render(request,'deskofficer_templates/Updating_Gender_Preview.html',context)


def Updating_Gender_Preview1(request,pk):
	DataCapture=DataCaptureManager.objects.first()
	form=Updating_Gender_Preview_form(request.POST or None)
	member=Members.objects.get(id=pk)
	
	if member.gender:
		form.fields['gender'].initial= member.gender.id

	if request.method == "POST":
		gender_id=request.POST.get('gender')
		gender=Gender.objects.get(id=gender_id)

		member.gender=gender
		member.save()
		return HttpResponseRedirect(reverse('Updating_Gender_selected_search'))
	context={
	'member':member,
	'form':form,
	'DataCapture':DataCapture,
	}
	return render(request,'deskofficer_templates/Updating_Gender_Preview.html',context)


def Updating_Gender_selected_search(request):
	DataCapture=DataCaptureManager.objects.first()
	title="Search Members for Gender Update"
	form = searchForm(request.POST or None)
	return render(request,'deskofficer_templates/Updating_Gender_selected_search.html',{'form':form,'title':title,'DataCapture':DataCapture,})


def Updating_Gender_selected_list_load(request):
	DataCapture=DataCaptureManager.objects.first()
	title="LIST OF MEMBERS"
	form = searchForm(request.POST)
	if request.method == "POST":
		if request.POST.get("title")=="":
			return HttpResponseRedirect(reverse('Updating_Gender_selected_search'))

		status=MembershipStatus.objects.get(title='ACTIVE')
		form = searchForm(request.POST)
		members=Members.objects.filter(Q(file_no__icontains=form['title'].value()) |Q(ippis_no__icontains=form['title'].value()) |Q(phone_number__icontains=form['title'].value()) | Q(admin__first_name__icontains=form['title'].value()) | Q(admin__last_name__icontains=form['title'].value()) | Q(middle_name__icontains=form['title'].value())).filter(status=status)
		context={
		'members':members,
		'title':title,
		'DataCapture':DataCapture,
		}
		return render(request,'deskofficer_templates/Updating_Gender_selected_list_load.html',context)



############################################################
##################### MEMBERS SHARE ########################
############################################################
def Members_Shares_Upload_list_load(request):
	DataCapture=DataCaptureManager.objects.first()
	status=MembershipStatus.objects.get(title='ACTIVE')
	shares_status = SharesUploadStatus.objects.get(title='PENDING')
	records=Members.objects.filter(status=status,shares_status=shares_status) #.filter(Q(gender__title__isnull=True) | Q(gender__title=""))

	context={
	'records':records,
	'DataCapture':DataCapture,
	}
	return render(request,'deskofficer_templates/Members_Shares_Upload_list_load.html',context)



def Members_Shares_Upload_Preview(request,pk):
	DataCapture=DataCaptureManager.objects.first()
	form=Existing_Shares_Upload_form(request.POST or None)
	member1=Members.objects.get(id=pk) 

	transaction=TransactionTypes.objects.get(code=700)
	member=[]
	if MembersAccountsDomain.objects.filter(member=member1,transaction=transaction).exists():
		member=MembersAccountsDomain.objects.get(member=member1,transaction=transaction)
	
	form.fields['effective_date'].initial= now
	if request.method=="POST":

		transaction_period=TransactionPeriods.objects.get(status__title='ACTIVE')
		
		status=TransactionStatus.objects.get(title='UNTREATED')
		status1=MembershipStatus.objects.get(title='ACTIVE')
		shares_amount=request.POST.get('shares_amount')
		unit_cost=request.POST.get('unit_cost')
		shares=request.POST.get('shares')
		effective_date=request.POST.get('effective_date')
		date = parse_date(effective_date)

	

		account_number=member.account_number
		

		processed_by=CustomUser.objects.get(id=request.user.id)
		if MembersShareAccounts.objects.filter(member=member).exists():
			messages.info(request,'Record Already Exist')
			return HttpResponseRedirect(reverse('Members_Shares_Upload_Preview',args=(pk,)))

		record=MembersShareAccounts(member=member,shares=shares,unit_cost=unit_cost,total_cost=shares_amount,effective_date=effective_date,year=date.year,status=status,processed_by=processed_by)
		record.save()

		debit=0
		credit=shares_amount
		balance=shares_amount

		particulars='Balance Broght Forward as at ' + str(transaction_period.transaction_period) + " with shares of " + str(shares)
		record=PersonalLedger(member=member1,transaction=transaction,account_number=account_number,particulars=particulars,debit=debit,credit=credit,balance=balance,transaction_period=transaction_period.transaction_period,status=status1)
		record.save()


		
		shares_status=SharesUploadStatus.objects.get(title='VERIFIED')
		member1.shares_status=shares_status
		member1.save()

		return HttpResponseRedirect(reverse('Members_Shares_Upload_list_load'))
	context={
	'member':member,
	'member1':member1,
	'form':form,
	'DataCapture':DataCapture,
	}
	return render(request,'deskofficer_templates/Members_Shares_Upload_Preview.html',context)



def Members_Initial_Shares_update_Search(request):
	DataCapture=DataCaptureManager.objects.first()
	title="Search Members for Initial Share Update"
	form = searchForm(request.POST or None)
	return render(request,'deskofficer_templates/Members_Initial_Shares_update_Search.html',{'form':form,'title':title,'DataCapture':DataCapture,})


def Members_Initial_Shares_update_list_load(request):
	DataCapture=DataCaptureManager.objects.first()
	title="LIST OF MEMBERS"
	form = searchForm(request.POST)
	if request.method == "POST":
		if request.POST.get("title")=="":
			return HttpResponseRedirect(reverse('Members_Initial_Shares_update_Search'))

		status=MembershipStatus.objects.get(title='ACTIVE')
		form = searchForm(request.POST)
	

		members=MembersShareAccounts.objects.filter(Q(member__member__file_no__icontains=form['title'].value()) 
													|Q(member__member__ippis_no__icontains=form['title'].value()) 
													|Q(member__member__phone_number__icontains=form['title'].value()) 
													|Q(member__member__admin__first_name__icontains=form['title'].value()) 
													|Q(member__member__admin__last_name__icontains=form['title'].value()) 
													|Q(member__member__middle_name__icontains=form['title'].value())).filter(Q(shares__lt=2))
		context={
		'members':members,
		'title':title,
		'DataCapture':DataCapture,
		}
		return render(request,'deskofficer_templates/Members_Initial_Shares_update_list_load.html',context)


def Members_Initial_Shares_update_preview(request,pk):
	form=MembersInitialShare_update_form(request.POST or None)

	if MembersShareConfigurations.objects.all().count()>0:
		record=MembersShareConfigurations.objects.first()
		form.fields['unit_cost'].initial=record.unit_cost


	member=MembersShareAccounts.objects.get(id=pk)

	if request.method=='POST':
		status=TransactionStatus.objects.get(title='UNTREATED')
		approval_officer_id=request.POST.get('approval_officers')
		approval_officer=ApprovalOfficers.objects.get(id=approval_officer_id)

		transaction_id=request.POST.get('transactions')
		transaction=SharesDeductionSavings.objects.get(id=transaction_id)
		# return HttpResponse(transaction.savings.name)
		
		amount=record.unit_cost
		processed_by=CustomUser.objects.get(id=request.user.id)
		if MembersShareInitialUpdateRequest.objects.filter(member=member,status=status).exists():
			messages.info(request,'There is still an open transaction for this member')
			return HttpResponseRedirect(reverse('Members_Initial_Shares_update_preview',args=(pk,)))

		record=MembersShareInitialUpdateRequest(member=member,transaction=transaction.savings,amount=amount,approval_officer=approval_officer,processed_by=processed_by,status=status)
		record.save()
		messages.success(request,'Transaction Completed Successfully')
		return HttpResponseRedirect(reverse('Members_Initial_Shares_update_Search'))

	
	context={
	'form':form,
	}
	return render(request,'deskofficer_templates/Members_Initial_Shares_update_preview.html',context)


def Members_Initial_Shares_update_approved_list_load(request):
	status=TransactionStatus.objects.get(title='UNTREATED')
	approval_status=ApprovalStatus.objects.get(title='APPROVED')
	members=MembersShareInitialUpdateRequest.objects.filter(status=status,approval_status=approval_status)

	context={
	'members':members,
	}
	return render(request,'deskofficer_templates/Members_Initial_Shares_update_approved_list_load.html',context)


def Members_Initial_Shares_update_approved_processed(request,pk):
	transaction_period=TransactionPeriods.objects.get(status__title='ACTIVE')
	status1=MembershipStatus.objects.get(title='ACTIVE')
	status=TransactionStatus.objects.get(title='TREATED')
	member=MembersShareInitialUpdateRequest.objects.get(id=pk)
	account_number=member.member.member.account_number

	ledger_balance=PersonalLedger.objects.filter(account_number=account_number).last()
	if request.method=="POST":
		savings_id=request.POST.get('savings')
		savings=TransactionTypes.objects.get(name=savings_id)

		amount=request.POST.get('amount')
		debit=0
		credit=amount
		balance=float(ledger_balance.balance) + float(amount)

		particulars='Initial Share Balance update as at ' + str(transaction_period.transaction_period) + " with shares: " + str(1) + " Deducted from " + str(savings.name)
		record=PersonalLedger(member=member.member.member.member,transaction=member.member.member.transaction,account_number=ledger_balance.account_number,particulars=particulars,debit=debit,credit=credit,balance=balance,transaction_period=transaction_period.transaction_period,status=status1)
		record.save()
		
		member.status=status
		member.save()

		return HttpResponseRedirect(reverse('Members_Initial_Shares_update_approved_list_load'))


	context={
	'member':member,
	'ledger_balance':ledger_balance.balance,
	}
	return render(request,'deskofficer_templates/Members_Initial_Shares_update_approved_processed.html',context)


def Members_Share_Purchase_Request_Search(request):
	DataCapture=DataCaptureManager.objects.first()
	title="Search Members for Share Purchase"
	form = searchForm(request.POST or None)
	return render(request,'deskofficer_templates/Members_Share_Purchase_Request_Search.html',{'form':form,'title':title,'DataCapture':DataCapture,})



def Members_Share_Purchase_Request_list_load(request):
	DataCapture=DataCaptureManager.objects.first()
	title="LIST OF MEMBERS"
	form = searchForm(request.POST)
	if request.method == "POST":
		if request.POST.get("title")=="":
			return HttpResponseRedirect(reverse('Members_Share_Purchase_Request_Search'))

		status=MembershipStatus.objects.get(title='ACTIVE')
		form = searchForm(request.POST)
		members=MembersShareAccounts.objects.filter(Q(member__member__file_no__icontains=form['title'].value()) |Q(member__member__ippis_no__icontains=form['title'].value()) |Q(member__member__phone_number__icontains=form['title'].value()) | Q(member__member__admin__first_name__icontains=form['title'].value()) | Q(member__member__admin__last_name__icontains=form['title'].value()) | Q(member__member__middle_name__icontains=form['title'].value())).filter(member__member__status=status)
		context={
		'members':members,
		'title':title,
		'DataCapture':DataCapture,
		}
		return render(request,'deskofficer_templates/Members_Share_Purchase_Request_list_load.html',context)


def Members_Share_Purchase_Request_View(request,pk):
	DataCapture=DataCaptureManager.objects.first()
	form = Members_Share_Purchase_Request_form(request.POST or None)
	member1=MembersShareAccounts.objects.get(id=pk)
	account_number=member1.member.account_number
	member=MembersAccountsDomain.objects.get(account_number=account_number)
	
	if request.method=="POST":
		status=TransactionStatus.objects.get(title="UNTREATED")
		max_unit = SharesUnits.objects.all().order_by('unit').last()

		existing_share = member1.shares
		approval_status=ApprovalStatus.objects.get(title='PENDING')
		approval_officer_id=request.POST.get('approval_officers')
		approval_officer=ApprovalOfficers.objects.get(id=approval_officer_id)
		units=request.POST.get('units')
	
		if int(max_unit.unit) < (int(units) + int(existing_share)):
			messages.error(request,"You have exceed the Maximum Units")
			return HttpResponseRedirect(reverse('Members_Share_Purchase_Request_View',args=(pk,)))

		if MembersSharePurchaseRequest.objects.filter(member=member,status=status).exists():
			messages.error(request,"You Still Have an Open Transaction")
			return HttpResponseRedirect(reverse('Members_Share_Purchase_Request_View',args=(pk,)))

		record=MembersSharePurchaseRequest(member=member,approval_officer=approval_officer,approval_status=approval_status,units=units,status=status)
		record.save()
		return HttpResponseRedirect(reverse('Members_Share_Purchase_Request_Search'))
	context={
	"form":form,
	"member":member,
	'DataCapture':DataCapture,
	'account_number':account_number,
	}
	return render(request,'deskofficer_templates/Members_Share_Purchase_Request_View.html',context)


def Members_Share_Purchase_Request_Process(request):
	approval_status=ApprovalStatus.objects.get(title='APPROVED')
	status=TransactionStatus.objects.get(title='UNTREATED')
	records=MembersSharePurchaseRequest.objects.filter(approval_status=approval_status,status=status)
	context={
	'records':records,
	}
	return render(request,'deskofficer_templates/Members_Share_Purchase_Request_Process.html',context)


def Members_Share_Purchase_Request_Process_View(request,pk):
	form=Members_Share_Purchase_Request_Process_View_Form(request.POST or None)
	record=MembersSharePurchaseRequest.objects.get(id=pk)
	member=MembersAccountsDomain.objects.get(account_number=record.member.account_number)
	transaction_receipt_category=TransactionTypes.objects.get(code='700')
	status1=MembershipStatus.objects.get(title='ACTIVE')
	status=TransactionStatus.objects.get(title='TREATED')
	

	if request.method=="POST":
		receipt_status=ReceiptStatus.objects.get(title='UNUSED')
		receipt_status1=ReceiptStatus.objects.get(title='USED')
		receipt_id=request.POST.get('receipt_no')
		
		if transaction_receipt_category.receipt_type.title=='MANUAL':
			if Receipts.objects.filter(receipt=receipt_id,status=receipt_status).exists():
				receipt_obj=Receipts.objects.get(receipt=receipt_id,status=receipt_status)
				receipt=receipt_obj.receipt
				receipt_obj.status=receipt_status1
				receipt_obj.save()
			else:
				messages.info(request,'Receipt Already in Use or Not Available')
				return HttpResponseRedirect(reverse('Members_Share_Purchase_Request_Process_View', args=(pk,)))
		else:
			receipt_obj=AutoReceipt.objects.first()
			receipt='C-' + str(receipt_obj.receipt).zfill(5)
			receipt_obj.receipt=int(receipt_obj.receipt)+1
			receipt_obj.save()

		

		account_number=record.member.account_number
		bank_id=request.POST.get('account')
		bank_account=CooperativeBankAccounts.objects.get(id=bank_id)

		unit_cost=request.POST.get('unit_cost')
		payment_reference=request.POST.get('payment_reference')
		units=request.POST.get('units')
		total_cost= float(unit_cost) * float(units)
		processed_by=CustomUser.objects.get(id=request.user.id)
		payment_date=request.POST.get('payment_date')

		
		if request.FILES.get('image', False):
			image = request.FILES['image']
			fs=FileSystemStorage()
			filename=fs.save(image.name,image)
			image_url=fs.url(filename)
		
		else:
			image_url=None


		purpose=str(units) + " share(s) at a unit cost " + str(unit_cost)
		record_add=MembersCashDeposits(transaction=transaction_receipt_category,account_number=account_number,payment_evidience=image_url,member=member.member,payment_reference=payment_reference,receipt=receipt,amount=total_cost,bank_accounts=bank_account,purpose=purpose,payment_date=payment_date,processed_by=processed_by)
		record_add.save()

		if MembersShareAccounts.objects.filter(member=member).exists():
			share_record=MembersShareAccounts.objects.filter(member=member).first()
			share_record.shares = int(share_record.shares) + int(units)
			share_record.unit_cost=unit_cost
			share_record.total_cost=float(share_record.total_cost) + float(total_cost)
			share_record.save()
		else:
			share_record=MembersShareAccounts(member=member,shares=units,unit_cost=unit_cost,total_cost=total_cost,effective_date=now,year=now.year,processed_by=processed_by)
			share_record.save()
		

		if PersonalLedger.objects.filter(account_number=account_number).exists():
			ledger=PersonalLedger.objects.filter(account_number=account_number).order_by('id').last()
			
			debit=0
			credit=total_cost
			balance=float(ledger.balance) + float(total_cost)
			particulars= str(units) + " Unit(s) Share Purchase, at unit cost of " + str(unit_cost) +  " as at " + str(now)

			
			ledger_record=PersonalLedger(member=member.member,transaction=member.transaction,account_number=account_number,particulars=particulars,debit=debit,credit=credit,balance=balance,transaction_period=now,status=status1)
			ledger_record.save()
		else:
			debit=0
			credit=total_cost
			balance=float(total_cost)
			particulars= str(units) + " Unit(s) Share Purchase, at unit cost of " + str(unit_cost) +  " as at " + str(now)

			
			ledger_record=PersonalLedger(member=member.member,transaction=member.transaction,account_number=account_number,particulars=particulars,debit=debit,credit=credit,balance=balance,transaction_period=now,status=status1)
			ledger_record.save()
		
		record.status=status
		record.save()

		return HttpResponseRedirect(reverse('Members_Share_Purchase_Request_Process'))


	if MembersShareConfigurations.objects.all().count()>0:
		share_cost=MembersShareConfigurations.objects.first()
		form.fields['payment_date'].initial=now
		form.fields['unit_cost'].initial=share_cost.unit_cost
		form.fields['units'].initial=record.units
		form.fields['total_cost'].initial= float(share_cost.unit_cost) * float(record.units)

	context={
	'record':record,
	'form':form,
	'transaction_receipt_category':transaction_receipt_category,
	}
	return render(request,'deskofficer_templates/Members_Share_Purchase_Request_Process_View.html',context)


############################################################
##################### MEMBERS WELFARE ######################
############################################################
def Members_salary_Upload_list_load(request):
	DataCapture=DataCaptureManager.objects.first()
	status=MembershipStatus.objects.get(title='ACTIVE')
	welfare_status = WelfareUploadStatus.objects.get(title='PENDING')
	records=Members.objects.filter(status=status,welfare_status=welfare_status) 

	context={
	'records':records,
	'DataCapture':DataCapture,
	}
	return render(request,'deskofficer_templates/Members_Welfare_Upload_list_load.html',context)



############################################################
##################### MEMBERS WELFARE ######################
############################################################
def Members_Welfare_Upload_list_load(request):
	DataCapture=DataCaptureManager.objects.first()
	status=MembershipStatus.objects.get(title='ACTIVE')
	welfare_status = WelfareUploadStatus.objects.get(title='PENDING')
	records=Members.objects.filter(status=status,welfare_status=welfare_status) 

	context={
	'records':records,
	'DataCapture':DataCapture,
	}
	return render(request,'deskofficer_templates/Members_Welfare_Upload_list_load.html',context)



def Members_Welfare_Upload_Preview(request,pk):
	DataCapture=DataCaptureManager.objects.first()
	form=Existing_Welfare_Upload_form(request.POST or None)

	transaction=TransactionTypes.objects.get(code=800)
	
	member=[]
	if MembersAccountsDomain.objects.filter(member_id=pk,transaction=transaction).exists():
		member=MembersAccountsDomain.objects.get(member_id=pk,transaction=transaction)
	
	if request.method=="POST":

		transaction_period=TransactionPeriods.objects.get(status__title='ACTIVE')
		
		status=TransactionStatus.objects.get(title='UNTREATED')
		status1=MembershipStatus.objects.get(title='ACTIVE')
		
		amount=request.POST.get('amount')
		
	

		account_number=member.account_number
		

		processed_by=CustomUser.objects.get(id=request.user.id)
		
		if MembersWelfareAccounts.objects.filter(member=member).exists():
			messages.info(request,'Record Already Upload for This Member')
			return HttpResponseRedirect(reverse('Members_Welfare_Upload_Preview',args=(pk,)))
		
		record=MembersWelfareAccounts(member=member,amount=amount,status=status,processed_by=processed_by)
		record.save()

	
		member1=Members.objects.get(id=pk) 
		welfare_status=WelfareUploadStatus.objects.get(title='VERIFIED')
		member1.welfare_status=welfare_status
		member1.save()

		return HttpResponseRedirect(reverse('Members_Welfare_Upload_list_load'))
	context={
	'member':member,
	'form':form,
	'DataCapture':DataCapture,
	}
	return render(request,'deskofficer_templates/Members_Welfare_Upload_Preview.html',context)



############################################################
##################### CASH DEPOSIT    ######################
############################################################
def Cash_Deposit_Shares_Search(request):
	DataCapture=DataCaptureManager.objects.first()
	title="Search Members for Cash Deposit for Shares"
	form = searchForm(request.POST or None)
	return render(request,'deskofficer_templates/Cash_Deposit_Shares_Search.html',{'form':form,'title':title,'DataCapture':DataCapture,})


def Cash_Deposit_Shares_list_load(request):
	DataCapture=DataCaptureManager.objects.first()
	title="LIST OF MEMBERS"
	form = searchForm(request.POST)
	if request.method == "POST":
		if request.POST.get("title")=="":
			return HttpResponseRedirect(reverse('Cash_Deposit_Welfare_Search'))

		transaction=TransactionTypes.objects.get(code='700')
		status=MembershipStatus.objects.get(title='ACTIVE')
		form = searchForm(request.POST)
		members=MembersAccountsDomain.objects.filter(Q(member__file_no__icontains=form['title'].value()) |Q(member__ippis_no__icontains=form['title'].value()) |Q(member__phone_number__icontains=form['title'].value()) | Q(member__admin__first_name__icontains=form['title'].value()) | Q(member__admin__last_name__icontains=form['title'].value()) | Q(member__middle_name__icontains=form['title'].value())).filter(transaction=transaction)
		context={
		'members':members,
		'title':title,
		'DataCapture':DataCapture,
		}
		return render(request,'deskofficer_templates/Cash_Deposit_Shares_list_load.html',context)


def Cash_Deposit_Shares_Preview(request,pk):
	form=Cash_Deposit_Shares_Preview_Form(request.POST or None)
	member=MembersAccountsDomain.objects.get(id=pk)
	transaction=TransactionTypes.objects.get(code='700')
	account_number=member.account_number
	max_share_obj=SharesUnits.objects.last()
	max_share=max_share_obj.unit
	status1=MembershipStatus.objects.get(title='ACTIVE')

	unit_cost_selected=0
	if MembersShareConfigurations.objects.all().exists():
		unit_cost_obj=MembersShareConfigurations.objects.first()
		unit_cost_selected=unit_cost_obj.unit_cost

	if request.method=="POST":
		receipt_status=ReceiptStatus.objects.get(title='UNUSED')
		receipt_status1=ReceiptStatus.objects.get(title='USED')
		receipt_id=request.POST.get('receipt_no')
		
		if transaction.receipt_type.title == 'MANUAL':
			if Receipts.objects.filter(receipt=receipt_id,status=receipt_status).exists():
				receipt_obj=Receipts.objects.get(receipt=receipt_id,status=receipt_status)
				receipt=receipt_obj.receipt
				receipt_obj.status=receipt_status1
				receipt_obj.save()
			else:
				messages.info(request,'Receipt Already in Use or Not Available')
				return HttpResponseRedirect(reverse('Cash_Deposit_Shares_Preview', args=(pk,)))
		else:
			receipt_obj=AutoReceipt.objects.first()
			receipt='C-' + str(receipt_obj.receipt).zfill(5)
			receipt_obj.receipt=int(receipt_obj.receipt)+1
			receipt_obj.save()


		units = request.POST.get('units')
		unit_cost = request.POST.get('unit_cost')
		total_amount = request.POST.get('total_amount')
		
		if float(total_amount) != float(unit_cost) * float(units):
			messages.info(request,'Invalid Amount Specification')
			return HttpResponseRedirect(reverse('Cash_Deposit_Shares_Preview', args=(pk,)))

		purpose = request.POST.get('narration')
		payment_date = request.POST.get('payment_date')
		payment_reference = request.POST.get('payment_reference')
		account_id = request.POST.get('account')
		bank_accounts=CooperativeBankAccounts.objects.get(id=account_id)
		processed_by=CustomUser.objects.get(id=request.user.id)

		if request.FILES.get('image', False):
			image = request.FILES['image']
			fs=FileSystemStorage()
			filename=fs.save(image.name,image)
			image_url=fs.url(filename)
		else:
			image_url=None


		
		if MembersShareAccounts.objects.filter(member=member).exists():
			record=MembersShareAccounts.objects.filter(member=member).first()
			if (int(record.shares) + int(units)) > int(max_share):
				messages.info(request,'You have exceeded maximum shares allowed')
				return HttpResponseRedirect(reverse('Cash_Deposit_Shares_Preview', args=(pk,)))
			
			record.shares=int(record.shares) + int(units)
			record.unit_cost=unit_cost
			record.total_cost=float(record.total_cost) + float(total_amount)
			record.save()
			
		else:
			messages.info(request,'Account Does not exist')
			return HttpResponseRedirect(reverse('Cash_Deposit_Shares_Preview', args=(pk,)))

		cash_record=MembersCashDeposits(receipt=receipt,payment_evidience=image_url,bank_accounts=bank_accounts,member=member.member,transaction=transaction,account_number=account_number,amount=total_amount,payment_reference=payment_reference,payment_date=payment_date,purpose=purpose,processed_by=processed_by)
		cash_record.save()	

		ledger=PersonalLedger.objects.filter(account_number=account_number).order_by('id').last()
		

		debit=0
		credit=total_amount
		balance=float(ledger.balance) + float(total_amount)
		particulars= str(units) + " Unit(s) Share Payment, at unit cost of " + str(unit_cost) +  " as at " + str(now)

		
		ledger_record=PersonalLedger(member=member.member,transaction=transaction,account_number=account_number,particulars=particulars,debit=debit,credit=credit,balance=balance,transaction_period=now,status=status1)
		ledger_record.save()


		messages.success(request,'Record Saved Successfully')
		return HttpResponseRedirect(reverse('Cash_Deposit_Shares_Preview', args=(pk,)))

	form.fields['unit_cost'].initial=unit_cost_selected
	form.fields['payment_date'].initial=now
	context={
	'member':member,
	'form':form,
	}
	return render(request,'deskofficer_templates/Cash_Deposit_Shares_Preview.html',context)



def Cash_Deposit_Welfare_Search(request):
	DataCapture=DataCaptureManager.objects.first()
	title="Search Members for Cash Deposit for Welfare"
	form = searchForm(request.POST or None)
	return render(request,'deskofficer_templates/Cash_Deposit_Welfare_Search.html',{'form':form,'title':title,'DataCapture':DataCapture,})

	
def Cash_Deposit_Welfare_list_load(request):
	DataCapture=DataCaptureManager.objects.first()
	title="LIST OF MEMBERS"
	form = searchForm(request.POST)
	if request.method == "POST":
		if request.POST.get("title")=="":
			return HttpResponseRedirect(reverse('Cash_Deposit_Welfare_Search'))

		transaction=TransactionTypes.objects.get(code='800')
		status=MembershipStatus.objects.get(title='ACTIVE')
		form = searchForm(request.POST)
		members=MembersAccountsDomain.objects.filter(Q(member__file_no__icontains=form['title'].value()) |Q(member__ippis_no__icontains=form['title'].value()) |Q(member__phone_number__icontains=form['title'].value()) | Q(member__admin__first_name__icontains=form['title'].value()) | Q(member__admin__last_name__icontains=form['title'].value()) | Q(member__middle_name__icontains=form['title'].value())).filter(transaction=transaction)
		context={
		'members':members,
		'title':title,
		'DataCapture':DataCapture,
		}
		return render(request,'deskofficer_templates/Cash_Deposit_Welfare_list_load.html',context)


def Cash_Deposit_Welfare_Preview(request,pk):
	form=Cash_Deposit_Welfare_Preview_Form(request.POST or None)
	member=MembersAccountsDomain.objects.get(id=pk)
	transaction=TransactionTypes.objects.get(code='800')


	if request.method=="POST":
		receipt_status=ReceiptStatus.objects.get(title='UNUSED')
		receipt_status1=ReceiptStatus.objects.get(title='USED')
		receipt_id=request.POST.get('receipt_no')
		
		if transaction.receipt_type.title=='MANUAL':
			if Receipts.objects.filter(receipt=receipt_id,status=receipt_status).exists():
				receipt_obj=Receipts.objects.get(receipt=receipt_id,status=receipt_status)
				receipt=receipt_obj.receipt
				receipt_obj.status=receipt_status1
				receipt_obj.save()
			else:
				messages.info(request,'Receipt Already in Use or Not Available')
				return HttpResponseRedirect(reverse('Cash_Deposit_Welfare_Preview', args=(pk,)))
		else:
			receipt_obj=AutoReceipt.objects.first()
			receipt='C-' + str(receipt_obj.receipt).zfill(5)
			receipt_obj.receipt=int(receipt_obj.receipt)+1
			receipt_obj.save()


		year = request.POST.get('year')
		purpose = request.POST.get('narration')
		payment_date = request.POST.get('payment_date')
		amount = request.POST.get('amount')
		payment_reference = request.POST.get('payment_reference')
		account_id = request.POST.get('account')
		bank_accounts=CooperativeBankAccounts.objects.get(id=account_id)
		processed_by=CustomUser.objects.get(id=request.user.id)

		if request.FILES.get('image', False):
			image = request.FILES['image']
			fs=FileSystemStorage()
			filename=fs.save(image.name,image)
			image_url=fs.url(filename)
		else:
			image_url=None

		cash_record=MembersCashDeposits(receipt=receipt,payment_evidience=image_url,bank_accounts=bank_accounts,member=member.member,transaction=transaction,account_number=member.account_number,amount=amount,payment_reference=payment_reference,payment_date=payment_date,purpose=purpose,processed_by=processed_by)
		cash_record.save()

		record=MembersWelfareAccounts(member=member,amount=amount,year=year,processed_by=processed_by)
		record.save()

		messages.success(request,'Record Saved Successfully')
		return HttpResponseRedirect(reverse('Cash_Deposit_Welfare_Preview', args=(pk,)))

	form.fields['payment_date'].initial=now
	context={
	'member':member,
	'form':form,
	}
	return render(request,'deskofficer_templates/Cash_Deposit_Welfare_Preview.html',context)


def Cash_Deposit_Savings_Search(request):
	DataCapture=DataCaptureManager.objects.first()
	title="Search Members for Cash Deposit"
	form = searchForm(request.POST or None)
	return render(request,'deskofficer_templates/Cash_Deposit_Savings_Search.html',{'form':form,'title':title,'DataCapture':DataCapture,})


	
def Cash_Deposit_Savings_list_load(request):
	DataCapture=DataCaptureManager.objects.first()
	title="LIST OF MEMBERS"
	form = searchForm(request.POST)
	if request.method == "POST":
		if request.POST.get("title")=="":
			return HttpResponseRedirect(reverse('Cash_Deposit_Savings_Search'))

		status=MembershipStatus.objects.get(title='ACTIVE')
		form = searchForm(request.POST)
		members=Members.objects.filter(Q(file_no__icontains=form['title'].value()) |Q(ippis_no__icontains=form['title'].value()) |Q(phone_number__icontains=form['title'].value()) | Q(admin__first_name__icontains=form['title'].value()) | Q(admin__last_name__icontains=form['title'].value()) | Q(middle_name__icontains=form['title'].value())).filter(status=status)
		context={
		'members':members,
		'title':title,
		'DataCapture':DataCapture,
		}
		return render(request,'deskofficer_templates/Cash_Deposit_Savings_list_load.html',context)


def Cash_Deposit_Savings_Load(request,pk):
	member=Members.objects.get(id=pk)
	records=MembersAccountsDomain.objects.filter(member=member,transaction__source__title="SAVINGS")
	context={
	'records':records,
	'member':member,
	}
	return render(request,'deskofficer_templates/Cash_Deposit_Savings_Load.html',context)


def Cash_Deposit_Savings_Preview(request,pk):
	form=Cash_Deposit_Savings_form(request.POST or None)
	DataCapture=DataCaptureManager.objects.first() 
	member=MembersAccountsDomain.objects.get(id=pk)
	
	# member=Members.objects.get(id=pk)
	
	if request.method=="POST":
		receipt_status=ReceiptStatus.objects.get(title='UNUSED')
		receipt_status1=ReceiptStatus.objects.get(title='USED')

	 

		if member.transaction.receipt_type.title == 'MANUAL':
			receipt_id = request.POST.get('receipt_no')
			if Receipts.objects.filter(receipt=receipt_id,status=receipt_status).exists():
				receipt_obj=Receipts.objects.get(receipt=receipt_id,status=receipt_status)
				receipt=receipt_obj.receipt
				receipt_obj.status=receipt_status1
				receipt_obj.save()
			else:
				messages.info(request,'Receipt Already in Use or Not Available')
				return HttpResponseRedirect(reverse('Cash_Deposit_Savings_Preview', args=(pk,)))
		else:
			receipt_obj=AutoReceipt.objects.first()
			receipt='C-' + str(receipt_obj.receipt).zfill(5)
			receipt_obj.receipt=int(receipt_obj.receipt)+1
			receipt_obj.save()


		status1=MembershipStatus.objects.get(title='ACTIVE')
		processed_by=CustomUser.objects.get(id=request.user.id)
		

		transaction=member.transaction
		account_number=member.account_number
		
		
		amount=request.POST.get('amount')
		payment_reference=request.POST.get('payment_reference')
		payment_date=request.POST.get('payment_date')
		
		purpose=request.POST.get('purpose')
		
		bank_accounts_id=request.POST.get("bank_accounts")
		bank_accounts=CooperativeBankAccounts.objects.get(id=bank_accounts_id)


		if request.FILES.get('payment_evidience', False):
			payment_evidience = request.FILES['payment_evidience']
			fs=FileSystemStorage()
			filename=fs.save(payment_evidience.name,payment_evidience)
			payment_evidience_url=fs.url(filename)
		else:
			payment_evidience_url=None

		if MembersCashDeposits.objects.filter(member=member.member,transaction=transaction,account_number=account_number,amount=amount,payment_reference=payment_reference).exists():
			messages.info(request,'This transaction has already been posted')
			return HttpResponseRedirect(reverse('Cash_Deposit_Savings_Preview',args=(pk,)))


		particulars=purpose
		transaction_period=now
		debit=0
		credit=amount
		balance=credit

		if PersonalLedger.objects.filter(member=member.member,transaction=transaction,account_number=account_number).exists():
			
			ledger=PersonalLedger.objects.filter(member=member.member,transaction=transaction,account_number=account_number).last()
			ledger_balance=ledger.balance
			balance=float(ledger_balance)+float(amount)

			cash_record=MembersCashDeposits(receipt=receipt,payment_evidience=payment_evidience_url,bank_accounts=bank_accounts,member=member.member,transaction=transaction,account_number=account_number,amount=amount,payment_reference=payment_reference,payment_date=payment_date,purpose=purpose,processed_by=processed_by)
			cash_record.save()


			record=PersonalLedger(member=member.member,transaction=transaction,account_number=account_number,particulars=particulars,debit=debit,credit=credit,balance=balance,transaction_period=transaction_period,status=status1)
			record.save()
			messages.success(request,'Payment Posted Successfully')
			return HttpResponseRedirect(reverse('Cash_Deposit_Savings_Load',args=(member.member.pk,)))
		else:		
			
			cash_record=MembersCashDeposits(receipt=receipt,payment_evidience=payment_evidience_url,bank_accounts=bank_accounts,member=member.member,transaction=transaction,account_number=account_number,amount=amount,payment_reference=payment_reference,payment_date=payment_date,purpose=purpose,processed_by=processed_by)
			cash_record.save()


			record=PersonalLedger(member=member.member,transaction=transaction,account_number=account_number,particulars=particulars,debit=debit,credit=credit,balance=balance,transaction_period=transaction_period,status=status1)
			record.save()

			messages.success(request,'Payment Posted Successfully')
			return HttpResponseRedirect(reverse('Cash_Deposit_Savings_Load',args=(member.member.pk,)))

	form.fields['payment_date'].initial= now
	context={
	'member':member,
	'form':form,
	'DataCapture':DataCapture,
	# 'transaction':transaction,
	}
	return render(request,'deskofficer_templates/Cash_Deposit_Savings_Preview.html',context)


def Cash_Deposit_Loans_Search(request):
	DataCapture=DataCaptureManager.objects.first()
	title="Search Members for Cash Deposit"
	form = searchForm(request.POST or None)
	return render(request,'deskofficer_templates/Cash_Deposit_Loans_Search.html',{'form':form,'title':title,'DataCapture':DataCapture,})

	
def Cash_Deposit_Loan_list_load(request):
	DataCapture=DataCaptureManager.objects.first()
	title="LIST OF MEMBERS"
	form = searchForm(request.POST)
	if request.method == "POST":
		if request.POST.get("title")=="":
			return HttpResponseRedirect(reverse('Cash_Deposit_Loans_Search'))

		status=MembershipStatus.objects.get(title='ACTIVE')
		form = searchForm(request.POST)
		members=Members.objects.filter(Q(file_no__icontains=form['title'].value()) |Q(ippis_no__icontains=form['title'].value()) |Q(phone_number__icontains=form['title'].value()) | Q(admin__first_name__icontains=form['title'].value()) | Q(admin__last_name__icontains=form['title'].value()) | Q(middle_name__icontains=form['title'].value())).filter(status=status)
		context={
		'members':members,
		'title':title,
		'DataCapture':DataCapture,
		}
		return render(request,'deskofficer_templates/Cash_Deposit_Loan_list_load.html',context)


def Cash_Deposit_Loans_Preview(request,pk):
	DataCapture=DataCaptureManager.objects.first()
	form=Cash_Deposit_Loans_form(request.POST or None)
	member=Members.objects.get(id=pk)
	loans=[]
	if request.method=="POST" and 'btn_display' in request.POST:
		transaction_id=request.POST.get("transactions")
		transaction=TransactionTypes.objects.get(id=transaction_id)

		loans=LoansRepaymentBase.objects.filter(member=member,transaction=transaction).filter(Q(balance__lt=0))
		
		payment_date=request.POST.get('payment_date')
		if payment_date:
			pass
		else:
			messages.info(request,'Payment Date is Missing')
			return HttpResponseRedirect(reverse('Cash_Deposit_Loans_Preview',args=(pk,)))

	
	if request.method=="POST" and 'btn_submit' in request.POST:
		processed_by=CustomUser.objects.get(id=request.user.id)
		
		loan_number_id=request.POST.get("account_number")
		loan_number=LoansRepaymentBase.objects.get(id=loan_number_id)
		

		transaction_id=request.POST.get("transactions")
		transaction=TransactionTypes.objects.get(id=transaction_id)
		
		# loan=LoansRepaymentBase.objects.get(loan_number=loan_number)

		amount=request.POST.get('amount')
		payment_reference=request.POST.get('payment_reference')
		payment_date=request.POST.get('payment_date')
		purpose=request.POST.get('purpose')
		
		# account_number_id=request.POST.get('account_number')
		# account_number=LoansRepaymentBase.objects.get(id=account_number_id)

		bank_accounts_id=request.POST.get("bank_accounts")
		bank_accounts=CooperativeBankAccounts.objects.get(id=bank_accounts_id)

		if request.FILES.get('payment_evidience', False):
			payment_evidience = request.FILES['payment_evidience']
			fs=FileSystemStorage()
			filename=fs.save(payment_evidience.name,payment_evidience)
			payment_evidience_url=fs.url(filename)
		else:
			payment_evidience_url=None


		account_number=loan_number.loan_number
		if payment_date:
			pass
		else:
			messages.info(request,'Payment Date is Missing')
			return HttpResponseRedirect(reverse('Cash_Deposit_Loans_Preview',args=(pk,)))

		if MembersCashDeposits.objects.filter(bank_accounts=bank_accounts,member=member,account_number=account_number,transaction=transaction,amount=amount,payment_reference=payment_reference).exists():
			messages.info(request,'This transaction has already been posted')
			return HttpResponseRedirect(reverse('Cash_Deposit_Loans_Preview',args=(pk,)))


		particulars=purpose
		transaction_period=now
		debit=0
		credit=amount

		if PersonalLedger.objects.filter(member=member,transaction=transaction,account_number=account_number).exists():
			status1=MembershipStatus.objects.get(title='ACTIVE')
			ledger=PersonalLedger.objects.filter(member=member,transaction=transaction,account_number=account_number).last()
			ledger_balance=ledger.balance
			balance=float(ledger_balance)+float(amount)

			cash_record=MembersCashDeposits(payment_evidience=payment_evidience_url,bank_accounts=bank_accounts,member=member,account_number=account_number,transaction=transaction,amount=amount,payment_reference=payment_reference,payment_date=payment_date,purpose=purpose,processed_by=processed_by)
			cash_record.save()

			loan_record=LoansRepaymentBase.objects.get(loan_number=account_number)
			loan_record.amount_paid=float(loan_record.amount_paid)+float(amount)
			loan_record.balance=float(loan_record.balance)+float(amount)
			loan_record.save()

			
			loan_merge_status=LoanMergeStatus.objects.get(title='MERGED')
			if loan_record.loan_merge_status==loan_merge_status:
				loan_groups=LoansDisbursed.objects.filter(merge_account_number=loan_record.loan_number)
				merge_paid_amount=float(amount)

				for loan_group in loan_groups:
					entity_balance=loan_group.balance
					
					if float(merge_paid_amount) >= abs(float(entity_balance)):
						new_entity_amount_paid= float(entity_balance) 
						
						new_entity_balance=float(entity_balance)+float(new_entity_amount_paid)

						merge_paid_amount=float(merge_paid_amount)-(float(new_entity_amount_paid))
					else:
						new_entity_amount_paid=float(merge_paid_amount)
						new_entity_balance=float(entity_balance.balance)+(float(merge_paid_amount))
						merge_paid_amount=0

					loan_group.amount_paid=float(loan_group.amount_paid)+ float(new_entity_amount_paid)
					loan_group.balance=float(new_entity_balance)
					loan_group.save()					


					if loan_group.balance >=0:
						loan_status=MembershipStatus.objects.get(title='INACTIVE')
						loan_group.status=loan_status
						loan_group.save()
						
						processed_by=CustomUser.objects	.get(id=request.user.id)
						transaction_status=TransactionStatus.objects.get(title='UNTREATED')
						
						record_cleared=LoansCleared(loan=loan_group,processed_by=processed_by,status=transaction_status)
						record_cleared.save()

			else:
				loan_group=LoansDisbursed.objects.filter(loan_number=account_number).update(amount_paid=float(loan_record.amount_paid)+float(amount),balance=float(loan_record.balance)+float(amount))
				
				if LoansDisbursed.objects.filter(loan_number=account_number).filter(Q(balance__gte=0)):
					loan_status=MembershipStatus.objects.get(title='INACTIVE')
					record_update=LoansDisbursed.objects.filter(loan_number=account_number).update(status=loan_status)
					
					processed_by=CustomUser.objects	.get(id=request.user.id)
					transaction_status=TransactionStatus.objects.get(title='UNTREATED')
					loan=LoansDisbursed.objects.get(loan_number=account_number)
					record_cleared=LoansCleared(loan=loan,processed_by=processed_by,status=transaction_status)
					record_cleared.save()





			if LoansRepaymentBase.objects.filter(loan_number=account_number).filter(Q(balance__gte=0)).exists():
				status=MembershipStatus.objects.get(title='INACTIVE')
				loan_record.status=status
				loan_record.save()

				# loan_clear_status=TransactionStatus.objects.get(title='TREATED')
				# loan_cleared=LoansCleared(loan=loan_record,processed_by=processed_by,status=loan_clear_status)
				# loan_cleared.save()

			record=PersonalLedger(member=member,transaction=transaction,account_number=account_number,particulars=particulars,debit=debit,credit=credit,balance=balance,transaction_period=transaction_period,status=status1)
			record.save()

			messages.success(request,'Transaction Completed Successfully')
			return HttpResponseRedirect(reverse('Cash_Deposit_Loans_Preview',args=(pk,)))
		else:
			messages.info(request,'This Account does not exist')
			return HttpResponseRedirect(reverse('Cash_Deposit_Loans_Preview',args=(pk,)))

	form.fields['payment_date'].initial=now
	context={
	'member':member,
	'form':form,
	'loans':loans,
	'DataCapture':DataCapture,
	}
	return render(request,'deskofficer_templates/Cash_Deposit_Loans_Preview.html',context)



############################################################
##################### CASH WITHDRAWALN######################
############################################################

def Cash_Withdrawal_Search(request):
	DataCapture=DataCaptureManager.objects.first()
	title="Search Members for Cash Withdrawal"
	form = searchForm(request.POST or None)
	return render(request,'deskofficer_templates/Cash_Withdrawal_Search.html',{'form':form,'title':title,'DataCapture':DataCapture,})

	
def Cash_Withdrawal_list_load(request):
	DataCapture=DataCaptureManager.objects.first()
	title="LIST OF MEMBERS FOR CASH WITHDRAWALS"
	form = searchForm(request.POST)
	if request.method == "POST":
		if request.POST.get("title")=="":
			return HttpResponseRedirect(reverse('Cash_Withdrawal_Search'))

		status=MembershipStatus.objects.get(title='ACTIVE')
		form = searchForm(request.POST)
		members=Members.objects.filter(Q(file_no__icontains=form['title'].value()) |Q(ippis_no__icontains=form['title'].value()) |Q(phone_number__icontains=form['title'].value()) | Q(admin__first_name__icontains=form['title'].value()) | Q(admin__last_name__icontains=form['title'].value()) | Q(middle_name__icontains=form['title'].value())).filter(status=status)
		context={
		'members':members,
		'title':title,
		'DataCapture':DataCapture,
		}
		return render(request,'deskofficer_templates/Cash_Withdrawal_list_load.html',context)


def Cash_Withdrawal_Transactions_load(request,pk):
	DataCapture=DataCaptureManager.objects.first()
	form=Cash_Withdrawal_form(request.POST or None)
	member=Members.objects.get(id=pk)
	ledger_blance=0
	account_number=""

	if request.method=="POST" and 'btn_fetch' in request.POST:
		transaction_id=request.POST.get('transactions')
		transaction=WithdrawableTransactions.objects.get(transaction_id=transaction_id)

		member_selected=MembersAccountsDomain.objects.get(member=member,transaction=transaction.transaction)

		current_date = datetime.date.today()
		maturity_date=current_date + relativedelta(months=transaction.maturity)

	
	
		if StandingOrderAccounts.objects.filter(transaction=member_selected).exists():
			record = StandingOrderAccounts.objects.filter(transaction=member_selected).first()
			ledger=PersonalLedger.objects.filter(member=member,account_number=member_selected.account_number).last()
			ledger_blance=ledger.balance
			account_number=member_selected.account_number
	


	if request.method=="POST" and 'btn_submit' in request.POST:
		transaction_id=request.POST.get('transactions')
		transaction=WithdrawableTransactions.objects.get(transaction_id=transaction_id)
		
		member_selected=MembersAccountsDomain.objects.get(member=member,transaction=transaction.transaction)
		
		current_date = datetime.date.today()
		maturity_date=current_date + relativedelta(months=transaction.maturity)



		approval_officer_id=request.POST.get('approval_officers')
		approval_officer=ApprovalOfficers.objects.get(id=approval_officer_id)

		if StandingOrderAccounts.objects.filter(transaction=member_selected).exists():
			record = StandingOrderAccounts.objects.filter(transaction=member_selected).first()
			ledger=PersonalLedger.objects.filter(member=member,account_number=member_selected.account_number).last()
			ledger_balance=ledger.balance
			account_number=member_selected.account_number


		withdrawal_amount=request.POST.get('amount')
		narration=request.POST.get('narration')

		if float(ledger_balance) < float(withdrawal_amount):
			messages.info(request,'Invalid Amount Specification')
			return HttpResponseRedirect(reverse('Cash_Withdrawal_Transactions_load',args=(pk,)))
		else:
			status=TransactionStatus.objects.get(title='UNTREATED')
			processed_by=CustomUser.objects.get(id=request.user.id)
			
			if MembersCashWithdrawalsApplication.objects.filter(member=member_selected,status=status).exists():
				messages.info(request,'You still have Open Transaction')
				return HttpResponseRedirect(reverse('Cash_Withdrawal_Transactions_load',args=(pk,)))




			record=MembersCashWithdrawalsApplication(member=member_selected,
				amount=withdrawal_amount,
				narration=narration,
				processed_by=processed_by,
				ledger_balance=ledger_balance,
				approval_officer=approval_officer,
				maturity_date=maturity_date,
				status=status
				)
			record.save()
			messages.success(request,'Transaction Completed Successfully')
			return HttpResponseRedirect(reverse('Cash_Withdrawal_Transactions_load',args=(pk,)))
	context={
	'form':form,
	'member':member,
	'ledger_blance':ledger_blance,
	'account_number':account_number,
	'DataCapture':DataCapture,
	}
	return render(request,'deskofficer_templates/Cash_Withdrawal_Transactions_load.html',context)



def Cash_Withdrawal_Transactions_Approved_list_Search(request):
	DataCapture=DataCaptureManager.objects.first()
	title="Search Members for Cash Withdrawal Status"
	form = search_with_date_Form(request.POST or None)
	form.fields['start_date'].initial=now
	form.fields['stop_date'].initial=now
	return render(request,'deskofficer_templates/Cash_Withdrawal_Transactions_Approved_list_Search.html',{'form':form,'title':title,'DataCapture':DataCapture,})




def Cash_Withdrawal_Transactions_Approved_list_Load(request):
	DataCapture=DataCaptureManager.objects.first()
	title="LIST OF MEMBERS FOR CASH WITHDRAWALS"
	form = search_with_date_Form(request.POST)
	if request.method == "POST":

		if request.POST.get("title")=="":
			return HttpResponseRedirect(reverse('Cash_Withdrawal_Transactions_Approved_list_Search'))

		status=MembershipStatus.objects.get(title='ACTIVE')
		form = search_with_date_Form(request.POST)
		members=MembersCashWithdrawalsApplication.objects.filter(Q(member__member__file_no__icontains=form['title'].value()) |Q(member__member__ippis_no__icontains=form['title'].value()) |Q(member__member__phone_number__icontains=form['title'].value()) | Q(member__member__admin__first_name__icontains=form['title'].value()) | Q(member__member__admin__last_name__icontains=form['title'].value()) | Q(member__member__middle_name__icontains=form['title'].value())).filter(Q(created_at__gte=form['start_date'].value()) & Q(created_at__lte=form['stop_date'].value()))
		context={
		'members':members,
		'title':title,
		'DataCapture':DataCapture,
		}
		return render(request,'deskofficer_templates/Cash_Withdrawal_Transactions_Approved_list_Load.html',context)

	

############################################################
##################### GENERAL REPORTS ######################
############################################################

def Cash_Deposit_Report_Date_Load(request):
	form=Cash_Deposit_Report_Date_Load_form(request.POST or None)

	form.fields['start_date'].initial=now
	form.fields['stop_date'].initial=now
	records=[]
	if request.method=='POST' and 'btn_display' in request.POST:
		start_date=request.POST.get('start_date')
		stop_date=request.POST.get('stop_date')
		records=MembersCashDeposits.objects.filter(Q(created_at__gte=start_date) & Q(created_at__lte=stop_date))
	
	context={
	'form':form,
	'records':records,
	}
	return render(request,'deskofficer_templates/Cash_Deposit_Report_Date_Load.html',context)


def Norminal_Roll_List_Load(request):
	DataCapture=DataCaptureManager.objects.first()
	records=Members.objects.all()
	context={
	'records':records,
	'DataCapture':DataCapture,
	}
	return render(request,'deskofficer_templates/Norminal_Roll_List_Load.html',context)


def Norminal_Roll_Personel_Detail(request,pk):
	member=Members.objects.get(id=pk)
	context={
	'member':member,
	}
	return render(request,'deskofficer_templates/Norminal_Roll_Personel_Detail.html',context)

############################################################
##################### ACTIVE LOANS ########################
############################################################
def Load_Active_loans(request):
	status=MembershipStatus.objects.get(title='ACTIVE')
	records=LoansDisbursed.objects.filter(status=status)
	context={
	'records':records,
	}
	return render(request,'deskofficer_templates/Load_Active_loans.html',context)


############################################################
##################### PERSONEL LEDGER ########################
############################################################

def PersonalLedger_Selected_Search(request):
	DataCapture=DataCaptureManager.objects.first()
	title="Search Members for Ledger Information"
	form = searchForm(request.POST or None)
	return render(request,'deskofficer_templates/PersonalLedger_Selected_Search.html',{'form':form,'title':title,'DataCapture':DataCapture,})

	

def PersonalLedger_Selected_list_load(request):
	DataCapture=DataCaptureManager.objects.first()
	title="LIST OF MEMBERS"
	form = searchForm(request.POST)
	if request.method == "POST":
		if request.POST.get("title")=="":
			messages.info(request,"Please Enter a search data")
			return HttpResponseRedirect(reverse('PersonalLedger_Selected_Search'))

		status=MembershipStatus.objects.get(title='ACTIVE')
		form = searchForm(request.POST)

		members=Members.objects.filter(Q(file_no__icontains=form['title'].value()) |Q(ippis_no__icontains=form['title'].value()) |Q(phone_number__icontains=form['title'].value()) | Q(admin__first_name__icontains=form['title'].value()) | Q(admin__last_name__icontains=form['title'].value()) | Q(middle_name__icontains=form['title'].value())).filter(status=status)
		if members.count() <= 0:
			messages.info(request,"No Record Found")
			return HttpResponseRedirect(reverse('PersonalLedger_Selected_Search'))
		context={
		'members':members,
		'title':title,
		'DataCapture':DataCapture,
		}
		return render(request,'deskofficer_templates/PersonalLedger_Selected_list_load.html',context)


def PersonalLedger_Transaction_Load(request,pk):
	DataCapture=DataCaptureManager.objects.first()
	form=PersonalLedger_Transaction_Load_form(request.POST or None)
	member=Members.objects.get(id=pk)
	


	if request.method=="POST":
		transaction_id=request.POST.get('transactions')
		transaction=TransactionTypes.objects.get(id=transaction_id)
		return HttpResponseRedirect(reverse('PersonalLedger_Transaction_Account_Load',args=(member.pk,transaction.pk,)))
	context={
	'form':form,
	'member':member,
	'DataCapture':DataCapture,
	}
	return render(request,'deskofficer_templates/PersonalLedger_Transaction_Load.html',context)


def PersonalLedger_Transaction_Account_Load(request,pk,trans_id):
	DataCapture=DataCaptureManager.objects.first()
	form=PersonalLedger_Transaction_Account_Load_form(request.POST or None)
	member=Members.objects.get(id=pk)
	status=MembershipStatus.objects.all()				
	transaction=TransactionTypes.objects.get(id=trans_id)
	p=[]
	# print("*************************************************")
	if request.method=="POST" and 'btn-fetch' in request.POST:
		transaction_status_id=request.POST.get('status')
		transaction_status=MembershipStatus.objects.get(title=transaction_status_id)
	
		transaction=TransactionTypes.objects.get(id=trans_id)
		p=PersonalLedger.objects.filter(member=member,transaction=transaction,status=transaction_status).order_by('account_number').values_list('account_number', flat=True).distinct()

	records=[]
	if request.method=="POST" and 'btn-display' in request.POST:
		start_date=request.POST.get('start_date')
		stop_date=request.POST.get('stop_date')
		if start_date and stop_date:
			pass
		else:
			return HttpResponseRedirect(reverse('PersonalLedger_Transaction_Account_Load',args=(pk,trans_id,)))
		account_number=request.POST.get('transaction')
		records=PersonalLedger.objects.filter(account_number=account_number).filter(Q(transaction_period__gte=start_date) & Q(transaction_period__lte=stop_date))
	
	


	form.fields['start_date'].initial= now - relativedelta(months=int(3))
	form.fields['stop_date'].initial= now
	context={
	'form':form,
	'transaction_list':p,
	'records':records,
	'member':member,
	'DataCapture':DataCapture,
	'status':status,
	'transaction':transaction,
	}
	return render(request,'deskofficer_templates/PersonalLedger_Transaction_Account_Load.html',context)




