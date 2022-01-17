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

  
def SEO_home(request):
	approval_status=ApprovalStatus.objects.get(title='PENDING')
	member_purchase_request=members_credit_purchase_summary.objects.filter(approval_status=approval_status,approval_officer__officer_id=request.user.id).count()
	
	title="Secretary"
	context={
	'title':title,
	'member_purchase_request':member_purchase_request,
	}
	return render(request, "SEO_templates/dashboard.html",context)


def basic_form(request):
	return render(request, 'SEO_templates/basics/basic_form1.html')


def basic_table(request):
	return render(request, 'SEO_templates/basics/basic_tables.html')

def datatable_table(request):
	return render(request, 'SEO_templates/basics/datatable.html')


def members_credit_purchase_approval(request):
	approval_status=ApprovalStatus.objects.get(title='PENDING')
	status=TransactionStatus.objects.get(title="UNTREATED")
	records=members_credit_purchase_summary.objects.filter(approval_officer__officer_id=request.user.id,status=status,approval_status=approval_status)
	context = {
	'records':records,

	}
	return render(request,'SEO_templates/members_credit_purchase_approval.html',context)


def members_credit_purchase_approval_preview(request,ticket):
	form=approval_form(request.POST or None)
	records=members_credit_purchase_analysis.objects.filter(trans_code__ticket=ticket)
	sum_debit = members_credit_purchase_analysis.objects.filter(trans_code__ticket=ticket).aggregate(total_debit=Sum('debit'))
	sum_credit = members_credit_purchase_analysis.objects.filter(trans_code__ticket=ticket).aggregate(total_credit=Sum('credit'))

	if sum_debit['total_debit']:
		debit_amount=float(sum_debit['total_debit'])
		
	else:
		debit_amount=0
	
	if sum_credit['total_credit']:
		credit_amount=float(sum_credit['total_credit'])
		
	else:
		credit_amount=0


	balance_amount = float(credit_amount)-float(debit_amount)




	selected_items =Members_Credit_Sales_Selected.objects.filter(ticket=ticket)

	sum_selected_items = Members_Credit_Sales_Selected.objects.filter(ticket=ticket).aggregate(total_item_amount=Sum('total'), total_items=Sum('quantity'))
	
	if sum_selected_items['total_item_amount']:
		total_amount=float(sum_selected_items['total_item_amount'])
		total_item_count=int(sum_selected_items['total_items'])
	else:
		total_amount=0
		total_item_count=0

	balance1=credit_amount-debit_amount
	balance2=balance1-total_amount

	if request.method=="POST":		
		
		comment=request.POST.get('comment')
		status_id=request.POST.get('approval_status')
		approval_status=ApprovalStatus.objects.get(id=status_id)
		record=members_credit_purchase_summary.objects.get(trans_code__ticket=ticket)

		record.approval_comment=comment
		record.approval_status=approval_status
		record.save()
		return HttpResponseRedirect(reverse('members_credit_purchase_approval'))

	context = {
	'records':records,
	'form':form,
	'selected_items':selected_items,
	'total_amount':total_amount,
	'total_item_count':total_item_count,
	'debit_amount':debit_amount,
	'credit_amount':credit_amount,
	'balance_amount':balance_amount,
	'balance1':balance1,
	'balance2':balance2,
	}
	return render(request,'SEO_templates/members_credit_purchase_approval_preview.html',context)


def members_salary_update_request_approval_load_list(request):
	status=ApprovalStatus.objects.get(title="PENDING")
	members=MembersSalaryUpdateRequest.objects.filter(status=status)
	context={
	'members':members,
	}
	return render(request,'SEO_templates/members_salary_update_request_approval_load_list.html',context)

def members_salary_update_request_approval(request,pk):
	member=MembersSalaryUpdateRequest.objects.get(id=pk)
	form=members_salary_update_request_approval_form(request.POST or None)
	form.fields['member_id'].initial=member.member.member_id
	form.fields['name'].initial=member.member.admin.first_name + ' ' + member.member.admin.last_name + ' ' + member.member.middle_name
	form.fields['description'].initial=member.description
	form.fields['current_amount'].initial=member.amount
	form.fields['prev_amount'].initial=member.member.gross_pay
	form.fields['approval_status'].initial=member.status
	form.fields['approval_date'].initial=now
	if request.method=="POST":
		status_id=request.POST.get('approval_status')
		status=ApprovalStatus.objects.get(id=status_id)

		comment=request.POST.get('comment')
		approval_date=request.POST.get('approval_date')

		record=MembersSalaryUpdateRequest.objects.filter(id=pk).update(status=status,approval_comment=comment,approved_at=approval_date)
		# messages.success(request,'Record Successfully Updated')
		return HttpResponseRedirect(reverse('members_salary_update_request_approval_load_list'))
	context={
	'form':form,
	}
	return render(request,'SEO_templates/members_salary_update_request_approval.html',context)


def external_fascilities_update_request_approval_load_list(request):
	status=ApprovalStatus.objects.get(title="PENDING")
	members=ExternalFascilitiesTemp.objects.filter(status=status,approval_officer__officer_id=request.user.id)
	context={
	'members':members,
	}
	return render(request,'SEO_templates/external_fascilities_update_request_approval_load_list.html',context)


def external_fascilities_update_request_approval(request,pk):
	member=ExternalFascilitiesTemp.objects.get(id=pk)
	form=ExternalFascilitiesTemp_form(request.POST or None)
	if request.method=="POST":
		status_id=request.POST.get('approval_status')
		status=ApprovalStatus.objects.get(id=status_id)

		comment=request.POST.get('comment')
		approval_date=request.POST.get('approval_date')

		record=ExternalFascilitiesTemp.objects.filter(id=pk).update(status=status,approval_comment=comment,approved_at=approval_date)
		# messages.success(request,'Record Successfully Updated')
		return HttpResponseRedirect(reverse('external_fascilities_update_request_approval_load_list'))
	form.fields['approval_date'].initial=now
	context={
	'form':form,
	}
	return render(request,'SEO_templates/external_fascilities_update_request_approval.html',context)


def members_exclusiveness_request_approval_list_load(request):
	approval_status=ApprovalStatus.objects.get(title="PENDING")
	members=MembersExclusiveness.objects.filter(approval_status=approval_status,approval_officer__officer_id=request.user.id)
	context={
	'members':members,
	}
	return render(request,'SEO_templates/members_exclusiveness_request_approval_list_load.html',context)


def members_exclusiveness_request_approval_process(request,pk):
	form=members_exclusiveness_request_approval_process_form(request.POST or None)
	member=MembersExclusiveness.objects.get(id=pk)

	if request.method=="POST":
		status_id=request.POST.get('approval_status')
		approval_status=ApprovalStatus.objects.get(id=status_id)
		approval_comment=request.POST.get('comment')

		approved_at = datetime.now().date()
		member.approval_status=approval_status
		member.approval_comment=approval_comment
		member.approved_at=approved_at
		member.save()
		return HttpResponseRedirect(reverse('members_exclusiveness_request_approval_list_load'))
	context={
	'member':member,
	'form':form,
	}
	return render(request,'SEO_templates/members_exclusiveness_request_approval_process.html',context)


def Shop_Cheque_Sales_List_Load(request):
	approval_status=ApprovalStatus.objects.get(title='PENDING')
	status=TransactionStatus.objects.get(title='UNTREATED')
	records=Cheque_Table.objects.filter(status=status,approval_status=approval_status)
	context={
	'records':records,
	}
	return render(request,'SEO_templates/Shop_Cheque_Sales_List_Load.html',context)

def Shop_Cheque_Sales_process(request,pk):
	approval_status=ApprovalStatus.objects.get(title='APPROVED')
	record=Cheque_Table.objects.get(id=pk)
	record.approval_status=approval_status
	record.save()
	return HttpResponseRedirect(reverse('Shop_Cheque_Sales_List_Load'))



def Initial_Shares_Update_List_Load(request):
	approval_status=ApprovalStatus.objects.get(title='PENDING')
	status=TransactionStatus.objects.get(title='UNTREATED')
	members=MembersShareInitialUpdateRequest.objects.filter(status=status,approval_status=approval_status)
	context={
	'members':members,
	'now':now,
	}
	return render(request,'SEO_templates/Initial_Shares_Update_List_Load.html',context)

def Initial_Shares_Update_preview(request,pk):
	form=Initial_Shares_Update_preview_form(request.POST or None)
	member=MembersShareInitialUpdateRequest.objects.get(id=pk)
	form.fields['amount'].initial=member.amount

	if request.method=='POST':
		approval_status_id=request.POST.get('approval_status')
		approval_status=ApprovalStatus.objects.get(id=approval_status_id)

		comment=request.POST.get('comment')
		member.approval_status=approval_status
		member.approval_comment=comment
		member.approved_at=now
		member.save()
		return HttpResponseRedirect(reverse('Initial_Shares_Update_List_Load'))
	context={
	'form':form,
	'member':member,
	}
	return render(request,'SEO_templates/Initial_Shares_Update_preview.html',context)


def Transaction_Adjustment_Approval_list_Load(request):
	approval_status=ApprovalStatus.objects.get(title='PENDING')
	records=TransactionAjustmentRequest.objects.filter(approval_status=approval_status)

	context={
	'records':records,
	}
	return render(request,'SEO_templates/Transaction_Adjustment_Approval_list_Load.html',context)


def Transaction_Adjustment_Approval_Process(request,pk):
	approval_status=ApprovalStatus.objects.get(title='APPROVED')
	record=TransactionAjustmentRequest.objects.get(id=pk)
	record.approval_status=approval_status
	record.approved_at=now
	record.save()
	return HttpResponseRedirect(reverse('Transaction_Adjustment_Approval_list_Load'))

	
def Transaction_Loan_Adjustment_Approval_list_Load(request):
	approval_status=ApprovalStatus.objects.get(title='PENDING')
	records=TransactionLoanAjustmentRequest.objects.filter(approval_status=approval_status)

	context={
	'records':records,
	}
	return render(request,'SEO_templates/Transaction_Loan_Adjustment_Approval_list_Load.html',context)


def Transaction_Loan_Adjustment_Approval_list_Process(request,pk):
	approval_status=ApprovalStatus.objects.get(title='APPROVED')
	approved_at=now
	record=TransactionLoanAjustmentRequest.objects.get(id=pk)
	record.approval_status=approval_status
	record.approved_at=approved_at

	record.save()
	return HttpResponseRedirect(reverse('Transaction_Loan_Adjustment_Approval_list_Load'))