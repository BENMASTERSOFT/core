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
  
def treasurer_home(request):
		
	title="Treasurer"
	context={
	'title':title,
	
	}
	return render(request, "treasurer_templates/dashboard.html",context)


def basic_form(request):
	return render(request, 'treasurer_templates/basics/basic_form1.html')


def basic_table(request):
	return render(request, 'treasurer_templates/basics/basic_tables.html')

def datatable_table(request):
	return render(request, 'treasurer_templates/basics/datatable.html')

def withdrawal_confirmation_list_load(request):
	status=TransactionStatus.objects.get(title='UNTREATED')
	disbursement_status=ApprovalStatus.objects.get(title='PENDING')
	records=MembersCashWithdrawalsMain.objects.filter(status=status,disbursement_status=disbursement_status)
	
	context={
	'records':records,
	}
	return render(request,'treasurer_templates/withdrawal_confirmation_list_load.html',context)


def withdrawal_confirmation_details(request,pk):
	status1=MembershipStatus.objects.get(title='ACTIVE')

	
	disbursement_officer=DisbursementOfficers.objects.get(officer_id=request.user.id)
	disbursement_status=ApprovalStatus.objects.get(title='APPROVED')

	record=MembersCashWithdrawalsMain.objects.get(id=pk)
	
	account_number=record.member.member.account_number
	ledger=PersonalLedger.objects.filter(account_number=account_number).last()
	
	debit=record.member.approved_amount
	credit=0
	balance= float(ledger.balance) - float(debit)


	transaction_period=now

	if record.channel.title == 'CHEQUE':
		particulars="Withdrawal through CHEQUE, with No "  + str(record.cheque_number) + ', ' + str(record.coop_account.account_name) + '(' + record.coop_account.bank.title + ')'		
	elif record.channel.title == 'CASH':
		particulars="Withdrawal through CASH" 
	elif record.channel.title == 'TRANSFER':
		particulars="Withdrawal through TRANSFER from " + str(record.coop_account.account_name) + '(' + record.coop_account.bank.title + ') into ' + record.member_account.account_name + '(' + str(record.member_account.account_number)  + ')'
		# particulars="Withdrawal through TRANSFER from " + str(record.coop_account.account_name) + '(' + record.coop_account.bank.title + ') into ' + str(record.member_account.account_number) 

	transaction=record.member.member.transaction
	member=record.member.member.member

	ledger_record=PersonalLedger(member=member,transaction=transaction,account_number=account_number,particulars=particulars,debit=debit,credit=credit,balance=balance,transaction_period=transaction_period,status=status1)
	ledger_record.save()


	
	record.disbursement_status=disbursement_status
	record.disbursement_officer=disbursement_officer
	record.disbursement_date=now
	record.save()

	return HttpResponseRedirect(reverse('withdrawal_confirmation_list_load'))

####################################################################
###################### RECEIPT AND ID MANAGER ######################
####################################################################

def tre_AutoReceipt_Setup(request):
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
        return HttpResponseRedirect(reverse('tre_AutoReceipt_Setup'))
    context={
    'record':record,
    }
    return render(request,'treasurer_templates/AutoReceipt_Setup.html',context)



def tre_receipt_manager(request):
	form = receipt_manager_form(request.POST or None)
	receipts=Receipts.objects.all()
	if request.method=="POST":
		start_point = request.POST.get('start_point')
		stop_point = request.POST.get('stop_point')
		
		for i in  range(int(start_point),int(stop_point)+1): 
			record=Receipts(receipt=str(i).zfill(5))
			record.save()
		return HttpResponseRedirect(reverse('tre_receipt_manager'))
	context={
	'form':form,
	'receipts':receipts,
	}
	return render(request,'treasurer_templates/receipt_manager.html',context)


#######################################################################
################## COOPERATIVE ACCOUNTS ################################
#######################################################################
def tre_CooperativeBankAccounts_add(request):
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
            return HttpResponseRedirect(reverse('tre_CooperativeBankAccounts_add'))

        record=CooperativeBankAccounts(bank=bank,account_type=account_type,account_name=account_name,account_number=account_number)
        record.save()

        messages.success(request,"Record Added Successfully")
        return HttpResponseRedirect(reverse('tre_CooperativeBankAccounts_add'))

    context={
    'form':form,
    'banks':banks,
    }
    return render(request,'treasurer_templates/CooperativeBankAccounts_add.html',context)


def tre_CooperativeBankAccounts_Remove(request,pk):
    record=CooperativeBankAccounts.objects.get(id=pk)
    record.delete()
    return HttpResponseRedirect(reverse('tre_CooperativeBankAccounts_add'))


def tre_CooperativeBankAccounts_Update(request,pk):
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
    	return HttpResponseRedirect(reverse('tre_CooperativeBankAccounts_add'))
    	
    context={
    'form':form,
    }
    return render(request,'treasurer_templates/CooperativeBankAccounts_Update.html',context)
