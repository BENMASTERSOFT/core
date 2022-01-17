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


  
def FINSEC_home(request):
		
	title="Fin. Secretary"
	context={
	'title':title,
	
	}
	return render(request, "finsec_templates/dashboard.html",context)


def basic_form(request):
	return render(request, 'finsec_templates/basics/basic_form1.html')


def basic_table(request):
	return render(request, 'finsec_templates/basics/basic_tables.html')

def datatable_table(request):
	return render(request, 'finsec_templates/basics/datatable.html')



def Cash_Withdrawal_Approved_list_load(request):
	status=TransactionStatus.objects.get(title="UNTREATED")
	approval_status=ApprovalStatus.objects.get(title='APPROVED')
	applicants=MembersCashWithdrawalsApplication.objects.filter(status=status,approval_status=approval_status)
	
	context={
	'applicants':applicants,
	}
	return render(request,'finsec_templates/Cash_Withdrawal_Approved_list_load.html',context)


def Cash_Withdrawal_Approved_Details(request,pk):
	form=Cash_Withdrawal_Approved_Details_form(request.POST or None)
	applicant=MembersCashWithdrawalsApplication.objects.get(id=pk)
	member_accounts=MembersBankAccounts.objects.filter(member_id=applicant.member.member)

	form.fields['amount'].initial=applicant.approved_amount
	form.fields['payment_date'].initial=now

	cheque=False
	cash=False
	transfer=False
	if request.method=="POST" and 'btn_fetch' in request.POST:
		
		channel_id=request.POST.get('channels')
		channel = PaymentChannels.objects.get(id=channel_id)

		cheque=False
		if channel.title=="CHEQUE":
			cheque=True
		elif channel.title=="CASH":
			cash=True
		elif channel.title=="TRANSFER":
			transfer=True
		
	if request.method=="POST" and 'btn_submit' in request.POST:
		status=TransactionStatus.objects.get(title="UNTREATED")
		processed_by=CustomUser.objects.get(id=request.user.id)

		channel_id=request.POST.get('channels')
		channel = PaymentChannels.objects.get(id=channel_id)
		
		amount =request.POST.get('amount')
		payment_date =request.POST.get('payment_date')
		
		officer_id =request.POST.get('officers')
		disbursement_officer=DisbursementOfficers.objects.get(id=officer_id)
		
		channels_id =request.POST.get('channels')
		channels=PaymentChannels.objects.get(id=channels_id)

		if channel.title=="CHEQUE":
			coop_account_id =request.POST.get('account')
			coop_account=CooperativeBankAccounts.objects.get(id=coop_account_id)
			cheque_number=request.POST.get('cheque_number')
			
			if cheque_number=="":
				messages.error(request,'Cheque Number Missing')
				return HttpResponseRedirect(reverse('Cash_Withdrawal_Approved_Details',args=(pk,)))
			
			record=MembersCashWithdrawalsMain(member=applicant,
				channel=channel,
				payment_date=payment_date,
				coop_account=coop_account,
				cheque_number=cheque_number,
				processed_by=processed_by,
				disbursement_officer=disbursement_officer,
				status=status,
				)
			record.save()
		elif channel.title=="CASH":
			
			record=MembersCashWithdrawalsMain(member=applicant,
				channel=channel,
				payment_date=payment_date,
				processed_by=processed_by,
				disbursement_officer=disbursement_officer,
				status=status,
				)
			record.save()
		elif channel.title=="TRANSFER":
			coop_account_id =request.POST.get('account')
			coop_account=CooperativeBankAccounts.objects.get(id=coop_account_id)

			member_account_id=request.POST.get('member_account')
			member_account=MembersBankAccounts.objects.get(id=member_account_id)
			record=MembersCashWithdrawalsMain(member=applicant,
				channel=channel,
				payment_date=payment_date,
				coop_account=coop_account,
				member_account=member_account,
				processed_by=processed_by,
				disbursement_officer=disbursement_officer,
				status=status,
				)
			record.save()
			
		certification_date=now		
		status=TransactionStatus.objects.get(title="TREATED")
		certification_status=CertificationStatus.objects.get(title='CERTIFIED')
		
		applicant.status=status
		applicant.certification_status=certification_status
		applicant.certification_date=certification_date
		applicant.save()
		return HttpResponseRedirect(reverse('Cash_Withdrawal_Approved_list_load'))
			
	context={
	'member_accounts':member_accounts,
	'applicant':applicant,
	'form':form,
	'cheque':cheque,
	'cash':cash,
	'transfer':transfer,
	}
	return render(request,'finsec_templates/Cash_Withdrawal_Approved_Details.html',context)


####################################################################
###################### RECEIPT AND ID MANAGER ######################
####################################################################

def finsec_AutoReceipt_Setup(request):
    record=[]
    if AutoReceipt.objects.all().exists():
        record=AutoReceipt.objects.first()

    if request.method=="POST":
        receipt=request.POST.get("receipt")
        if AutoReceipt.objects.all().exists():
            record=AutoReceipt.objects.first()
            record.receipt=receipt
            record.save()
        else:
            record=AutoReceipt(receipt=receipt)
            record.save()
        return HttpResponseRedirect(reverse('finsec_AutoReceipt_Setup'))
    context={
    'record':record,
    }
    return render(request,'finsec_templates/AutoReceipt_Setup.html',context)



def finsec_receipt_manager(request):
	form = receipt_manager_form(request.POST or None)
	receipts=Receipts.objects.all()
	if request.method=="POST":
		start_point = request.POST.get('start_point')
		stop_point = request.POST.get('stop_point')
		
		for i in  range(int(start_point),int(stop_point)+1): 
			record=Receipts(receipt=str(i).zfill(5))
			record.save()
		return HttpResponseRedirect(reverse('finsec_receipt_manager'))
	context={
	'form':form,
	'receipts':receipts,
	}
	return render(request,'finsec_templates/receipt_manager.html',context)


#######################################################################
################## COOPERATIVE ACCOUNTS ################################
#######################################################################
def finsec_CooperativeBankAccounts_add(request):
    form=CooperativeBankAccounts_form(request.POST or None)
    banks=CooperativeBankAccounts.objects.all()
    if request.method == 'POST':
        bank_id=request.POST.get('bank')
        bank=Banks.objects.get(id=bank_id)

        account_type_id=request.POST.get('account_type')
        account_type=AccountTypes.objects.get(id=account_type_id)

        account_name=request.POST.get('account_name')
        account_number=request.POST.get('account_number')

        if CooperativeBankAccounts.objects.filter(bank=bank,account_number=account_number).exists():
            messages.error(request,'This account Number is already in Use')
            return HttpResponseRedirect(reverse('finsec_CooperativeBankAccounts_add'))

        record=CooperativeBankAccounts(bank=bank,account_type=account_type,account_name=account_name,account_number=account_number)
        record.save()

        messages.success(request,"Record Added Successfully")
        return HttpResponseRedirect(reverse('finsec_CooperativeBankAccounts_add'))

    context={
    'form':form,
    'banks':banks,
    }
    return render(request,'finsec_templates/CooperativeBankAccounts_add.html',context)


def finsec_CooperativeBankAccounts_Remove(request,pk):
    record=CooperativeBankAccounts.objects.get(id=pk)
    record.delete()
    return HttpResponseRedirect(reverse('finsec_CooperativeBankAccounts_add'))


def finsec_CooperativeBankAccounts_Update(request,pk):
    form=CooperativeBankAccounts_form(request.POST or None)
    record=CooperativeBankAccounts.objects.get(id=pk)

    form.fields['account_name'].initial=record.account_name
    form.fields['account_number'].initial=record.account_number
    form.fields['bank'].initial=record.bank.id
    form.fields['account_type'].initial=record.account_type.id
    if request.method=="POST":
    	bank_id=request.POST.get('bank')
    	bank=Banks.objects.get(id=bank_id)

    	account_type_id = request.POST.get('account_type')
    	account_type=AccountTypes.objects.get(id=account_type_id)

    	account_name=request.POST.get('account_name')
    	account_number=request.POST.get('account_number')

    	record.bank=bank
    	record.account_type=account_type
    	record.account_name=account_name
    	record.account_number=account_number
    	record.save()
    	return HttpResponseRedirect(reverse('finsec_CooperativeBankAccounts_add'))
    	
    context={
    'form':form,
    }
    return render(request,'finsec_templates/CooperativeBankAccounts_Update.html',context)
