from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, HttpResponseRedirect
from cooperative.models import *
from django.contrib import messages
from django.urls import reverse
from cooperative.forms import *
from django.db.models import Q
from django.db.models import Count, Sum
from django.utils import timezone
import datetime
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
from django.db.models import F


# now = datetime.datetime.now()
now = datetime.datetime.now(tz=timezone.utc) # you can use this value





def shop_home(request):
	title="SHOP"
	status=TransactionStatus.objects.get(title="UNTREATED")
	approval_status=ApprovalStatus.objects.get(title='APPROVED')
	members_credit_purchases=members_credit_purchase_summary.objects.filter(status=status,approval_status=approval_status).count()

	user_level=Staff.objects.get(admin=CustomUser.objects.get(id=request.user.id))

	context={
	'user_level':user_level.userlevel.title,
	'title':title,
	'members_credit_purchases':members_credit_purchases,
	}
	return render(request, "shop_templates/dashboard.html",context)


def basic_form(request):
	return render(request, 'shop_templates/basics/basic_form1.html')


def advance_form(request):
	return render(request, 'shop_templates/basics/advance_plugin_form.html')


def basic_table(request):
	return render(request, 'shop_templates/basics/basic_tables.html')

def datatable_table(request):
	return render(request, 'shop_templates/basics/datatable.html')


def editable_invoice(request):
	return render(request, 'shop_templates/basics/editable_invoice.html')


@csrf_exempt
def check_receipt_no_exist(request):
	status=ReceiptStatus.objects.get(title='USED')
	receipt_no=request.POST.get("receipt_no")
	receipt_no_obj=Receipts_Shop.objects.filter(receipt=receipt_no,status=status).exists()
	if receipt_no_obj:
		return HttpResponse(True)
	else:
		return  HttpResponse(False)

@csrf_exempt
def check_code_exist(request):
    code=request.POST.get("code")
    product_obj=Stock.objects.filter(code=code).exists()
    if product_obj:
        return HttpResponse(True)
    else:
        return  HttpResponse(False)



def Stock_Category_Load(request):
	categories=ProductCategory.objects.all()
	user_level=Staff.objects.get(admin=CustomUser.objects.get(id=request.user.id))

	context={
	'user_level':user_level.userlevel.title,
	'categories':categories,
	}
	return render(request,'shop_templates/Stock_Category_Load.html',context)


def Stock_add(request,pk):
	category=ProductCategory.objects.get(id=pk)
	form=Stock_form(request.POST or None)

	products = Stock.objects.filter(category_id=category)
	if request.method=="POST":
		code=request.POST.get('code')
		item_name=request.POST.get('item_name').upper()
		details=request.POST.get('details').upper()
		quantity=request.POST.get('quantity')
		re_order_level=request.POST.get('re_order_level')
		no_in_pack=request.POST.get('no_in_pack')
		unit_selling_price=request.POST.get('unit_selling_price')
		unit_cost_price=request.POST.get('unit_cost_price')
		record=Stock(category=category,code=code,item_name=item_name,details=details,quantity=quantity,re_order_level=re_order_level,no_in_pack=no_in_pack,unit_selling_price=unit_selling_price,unit_cost_price=unit_cost_price)
		record.save()
		messages.success(request,"Record Added Successfully")
		return HttpResponseRedirect(reverse('Stock_add',args=(pk,)))

	user_level=Staff.objects.get(admin=CustomUser.objects.get(id=request.user.id))

	context={
	'user_level':user_level.userlevel.title,
	'form':form,
	
	'category':category,
	'products':products,
	'return_pk':pk,
	}
	return render(request,'shop_templates/Stock_add.html',context)


def Update_Stock(request,pk,return_pk):
	form=Stock_Update_form(request.POST or None)

	product = Stock.objects.get(id=pk)

	form.fields['code'].initial=product.code
	form.fields['item_name'].initial=product.item_name
	form.fields['details'].initial=product.details
	form.fields['quantity'].initial=product.quantity
	form.fields['re_order_level'].initial=product.re_order_level
	form.fields['no_in_pack'].initial=product.no_in_pack
	form.fields['unit_selling_price'].initial=product.unit_selling_price
	form.fields['unit_cost_price'].initial=product.unit_cost_price
	form.fields['category'].initial=product.category.id



	if request.method=="POST":
		category_id=request.POST.get('category')
		category=ProductCategory.objects.get(id=category_id)
		code=request.POST.get('code')
		item_name=request.POST.get('item_name')
		details=request.POST.get('details')
		quantity=request.POST.get('quantity')
		re_order_level=request.POST.get('re_order_level')
		no_in_pack=request.POST.get('no_in_pack')
		unit_selling_price=request.POST.get('unit_selling_price')
		unit_cost_price=request.POST.get('unit_cost_price')
		product.category=category
		product.code=code
		product.item_name=item_name.upper()
		product.details=details.upper()
		product.quantity=quantity
		product.re_order_level=re_order_level
		product.no_in_pack=no_in_pack
		product.unit_selling_price=unit_selling_price
		product.unit_cost_price=unit_cost_price
		product.save()
		messages.success(request,"Record Updated Successfully")
		return HttpResponseRedirect(reverse('Stock_add',args=(return_pk,)))

	user_level=Staff.objects.get(admin=CustomUser.objects.get(id=request.user.id))

	context={
	'user_level':user_level.userlevel.title,
	'form':form,
	
	
	'product':product,
	'return_pk':pk,
	}
	return render(request,'shop_templates/Stock_Update.html',context)



def Manage_Stock_search(request):
	title="Search Stock"
	form = searchForm(request.POST or None)
	user_level=Staff.objects.get(admin=CustomUser.objects.get(id=request.user.id))
	return render(request,'shop_templates/Manage_Stock_search.html',{'form':form,'title':title,'user_level':user_level.userlevel.title,})


def Manage_Stock_Product_load(request):
	title="Product List"
	if request.method == "POST":
		form = searchForm(request.POST)
		stocks=Stock.objects.filter(Q(code__icontains=form['title'].value()) | Q(item_name__icontains=form['title'].value()))
		user_level=Staff.objects.get(admin=CustomUser.objects.get(id=request.user.id))

		context={
			'user_level':user_level.userlevel.title,
			'stocks':stocks,
			'title':title,
		}
		return render(request,'shop_templates/Manage_Stock_Product_load.html',context)

def Manage_Stock_Product_delete(request,pk):
	product=Stock.objects.get(id=pk)
	if request.method == "POST":
		if Purchases.objects.filter(product=product).exists():
			messages.error(request,'This Product cannot be Deleted, it is alrady in Use')
			return HttpResponseRedirect(reverse('Manage_Stock_Product_delete',args=(pk,)))
		else:
			# record.delete()
			return HttpResponseRedirect(reverse('Manage_Stock_search'))
	context={
	'product':product,
	}
	return render(request,'shop_templates/Manage_Stock_Product_delete.html',context)


def Manage_Stock_Product_Update(request,pk):
	user_level=Staff.objects.get(admin=CustomUser.objects.get(id=request.user.id))
	form=Stock_Update_form(request.POST or None)

	product = Stock.objects.get(id=pk)

	form.fields['code'].initial=product.code
	form.fields['item_name'].initial=product.item_name
	form.fields['quantity'].initial=product.quantity
	form.fields['re_order_level'].initial=product.re_order_level
	form.fields['no_in_pack'].initial=product.no_in_pack
	form.fields['unit_selling_price'].initial=product.unit_selling_price
	form.fields['category'].initial=product.category.id

	if request.method=="POST":
		category_id=request.POST.get('category')
		category=ProductCategory.objects.get(id=category_id)
		code=request.POST.get('code')
		item_name=request.POST.get('item_name')
		if product.lock_status.title == 'OPEN':
			quantity=request.POST.get('quantity')
		re_order_level=request.POST.get('re_order_level')
		no_in_pack=request.POST.get('no_in_pack')
		unit_selling_price=request.POST.get('unit_selling_price')
		product.category=category
		product.code=code
		product.item_name=item_name.upper()
		
		if product.lock_status.title == 'OPEN':
			product.quantity=quantity
		product.re_order_level=re_order_level
		product.no_in_pack=no_in_pack
		product.unit_selling_price=unit_selling_price
		product.save()
		messages.success(request,"Record Updated Successfully")
		return HttpResponseRedirect(reverse('Manage_Stock_Product_Update',args=(pk,)))
	context={
	'user_level':user_level.userlevel.title,
	'form':form,
	'product':product,
	}
	return render(request,'shop_templates/Manage_Stock_Product_Update.html',context)



def Manage_Stock_Product_Lock(request):
	user_level=Staff.objects.get(admin=CustomUser.objects.get(id=request.user.id))
	stocks = Stock.objects.all()
	context={
	'user_level':user_level.userlevel.title,
	'stocks':stocks,
	}
	return render(request,'shop_templates/Manage_Stock_Product_Lock.html',context)


def Manage_Stock_Product_Lock_Individuals(request,pk):
	locked_status=LockedStatus.objects.get(title='LOCKED')
	stock = Stock.objects.get(id=pk)
	stock.lock_status=locked_status
	stock.save()
	return HttpResponseRedirect(reverse('Manage_Stock_Product_Lock'))


def Manage_Stock_Product_UnLock_Individuals(request,pk):
	locked_status=LockedStatus.objects.get(title='OPEN')
	stock = Stock.objects.get(id=pk)
	stock.lock_status=locked_status
	stock.save()
	return HttpResponseRedirect(reverse('Manage_Stock_Product_Lock'))


def Manage_Stock_Product_Lock_Multiple(request):
	lock_status=LockedStatus.objects.get(title='LOCKED')
	stock_update=Stock.objects.all().update(lock_status=lock_status)

	return HttpResponseRedirect(reverse('Manage_Stock_Product_Lock'))


def Item_Write_off_search(request):
	title="Search Stock"
	form = searchForm(request.POST or None)
	user_level=Staff.objects.get(admin=CustomUser.objects.get(id=request.user.id))
	return render(request,'shop_templates/Item_Write_off_search.html',{'form':form,'title':title,'user_level':user_level.userlevel.title,})


def Item_Write_off_product_load(request):
	title="Product List"
	if request.method == "POST":
		form = searchForm(request.POST)
		if form['title'].value():
			stocks=Stock.objects.filter(Q(code__icontains=form['title'].value()) | Q(item_name__icontains=form['title'].value()))
			user_level=Staff.objects.get(admin=CustomUser.objects.get(id=request.user.id))
			if stocks:
				context={
					'user_level':user_level.userlevel.title,
					'stocks':stocks,
					'title':title,
				}
				return render(request,'shop_templates/Item_Write_off_product_load.html',context)
			else:
				messages.info(request,'Matching Records Not Found')
				return HttpResponseRedirect(reverse("Item_Write_off_search"))
		else:
			messages.info(request,'Please Enter for Search')
			return HttpResponseRedirect(reverse("Item_Write_off_search"))

def Item_Write_off_product_Preview(request,pk):
	context={

	}
	return render(request,'shop_templates/Item_Write_off_product_Preview.html',context)


def Members_Credit_sales_ledger_search(request):
	title="Search Members"
	form = searchForm(request.POST or None)
	user_level=Staff.objects.get(admin=CustomUser.objects.get(id=request.user.id))
	return render(request,'shop_templates/Members_Credit_sales_ledger_search.html',{'form':form,'title':title,'user_level':user_level.userlevel.title,})


def Members_Credit_sales_ledger_list_load(request):
	title="Membership Purchases"
	if request.method == "POST":
		form = searchForm(request.POST)
		status = MembershipStatus.objects.get(title='ACTIVE')
		members=Members.objects.filter(Q(phone_number__icontains=form['title'].value()) | Q(file_no__icontains=form['title'].value()) | Q(admin__first_name__icontains=form['title'].value()) | Q(admin__last_name__icontains=form['title'].value()) | Q(middle_name__icontains=form['title'].value())).filter(status=status)
		
		user_level=Staff.objects.get(admin=CustomUser.objects.get(id=request.user.id))

		context={
			'user_level':user_level.userlevel.title,
			'members':members,
			'title':title,
		}
		return render(request,'shop_templates/Members_Credit_sales_ledger.html',context)


def Members_Credit_sales_ledger_preview(request,pk):
	form=Members_Credit_sales_ledger_form(request.POST or None)
	member = Members.objects.get(id=pk)
	form.fields['start_date'].initial = now
	form.fields['stop_date'].initial = now
	
	user_level=Staff.objects.get(admin=CustomUser.objects.get(id=request.user.id))
	
	items=[]
	if request.method =="POST":
		start_date = request.POST.get("start_date")
		stop_date = request.POST.get("stop_date")
	

		items = CooperativeShopLedger.objects.filter(member__member=member).filter(Q(created_at__gte=start_date) & Q(created_at__lte=stop_date))
	

	context={
	'user_level':user_level.userlevel.title,
	'form':form,
	'items':items,
	}
	return render(request,'shop_templates/Members_Credit_sales_ledger_preview.html',context)



def Members_Credit_sales_ledger_details(request,pk):
	date_selected=CooperativeShopLedger.objects.get(receipt=pk)
	records=Daily_Sales.objects.filter(receipt=pk)
	user_level=Staff.objects.get(admin=CustomUser.objects.get(id=request.user.id))

	context={
	'user_level':user_level.userlevel.title,
	'records':records,
	'date_selected':date_selected,
	}
	return render(request,'shop_templates/Members_Credit_sales_ledger_details.html',context)

def Members_Credit_sales_list_search(request):
	title="Search Members for Shopping"
	form = searchForm(request.POST or None)
	user_level=Staff.objects.get(admin=CustomUser.objects.get(id=request.user.id))
	return render(request,'shop_templates/Members_Credit_sales_list_search.html',{'form':form,'title':title,'user_level':user_level.userlevel.title,})


def Members_Credit_sales_list_load(request):
	title="Membership Purchases"
	if request.method == "POST":
		form = searchForm(request.POST)
		status=MembershipStatus.objects.get(title="ACTIVE")
		members=Members.objects.filter(Q(phone_number__icontains=form['title'].value()) | Q(file_no__icontains=form['title'].value()) | Q(admin__first_name__icontains=form['title'].value()) | Q(admin__last_name__icontains=form['title'].value()) | Q(middle_name__icontains=form['title'].value())).filter(status=status)
		
		user_level=Staff.objects.get(admin=CustomUser.objects.get(id=request.user.id))

		context={
		'user_level':user_level.userlevel.title,
		'members':members,
		'title':title,
		}
		return render(request,'shop_templates/Members_Credit_sales_list_load.html',context)


def Members_Credit_sales_item_select(request,pk):
	processed_by_id=request.user.id
	processed_by=CustomUser.objects.get(id=processed_by_id)
	items=Stock.objects.filter(Q(quantity__gt=0))
	member=Members.objects.get(id=pk)
	user_level=Staff.objects.get(admin=CustomUser.objects.get(id=request.user.id))

	status=TransactionStatus.objects.get(title="UNTREATED")
	total_item=""
	total_amount=""
	ticket_holder=""
	select_items=[]
	if Members_Credit_Sales_Selected.objects.filter(member=member,status=status,processed_by=processed_by).exists():
		button_show=True
		select_items = Members_Credit_Sales_Selected.objects.filter(member=member,status=status,processed_by=processed_by)
		queryset=Members_Credit_Sales_Selected.objects.filter(ticket=select_items[0].ticket).aggregate(total_amount=Sum('total'),total_item=Sum('quantity'))
		total_item=queryset['total_item']
		total_amount=queryset['total_amount']
		ticket_holder=select_items[0].ticket
	else:
		button_show=False



	context={
	'user_level':user_level.userlevel.title,
	'items':items,
	'member':member,
	'select_items':select_items,
	'total_amount':total_amount,
	'total_item':total_item,
	'ticket':ticket_holder,
	'button_show':button_show,
	}
	return render(request,'shop_templates/Members_Credit_sales_item_select.html',context)



def members_credit_issue_item(request,pk,member_id):
	form=members_credit_issue_item_form(request.POST or None)
	product = Stock.objects.get(id=pk)
	member=Members.objects.get(id=member_id)
	
	form.fields['code'].initial=product.code
	form.fields['item_name'].initial=product.item_name
	form.fields['details'].initial=product.details
	form.fields['available_quantity'].initial=product.quantity
	form.fields['unit_selling_price'].initial=product.unit_selling_price

	if request.method=="POST":	
		
		status=TransactionStatus.objects.get(title="UNTREATED")
		quantity=request.POST.get('issue_quantity')
		if int(quantity)<=0:
			messages.error(request,"Quantity Selected cannot be Zero (0)")
			return HttpResponseRedirect(reverse('members_credit_issue_item', args=(pk,member_id)))
		
		if int(quantity)>int(product.quantity):
			messages.error(request,"Quantity Selected is more that Available Quantity")
			return HttpResponseRedirect(reverse('members_credit_issue_item', args=(pk,member_id)))
		

		unit_selling_price=product.unit_selling_price
		
		total=float(quantity) * float(unit_selling_price)
		processed_by=CustomUser.objects.get(id=request.user.id)

		if Members_Credit_Sales_Selected.objects.filter(member=member,status=status,processed_by=processed_by):
			ticket_id=Members_Credit_Sales_Selected.objects.filter(member=member,status=status).first()
			selected_ticket=ticket_id.ticket
		else:
			now = datetime.datetime.now()
			selected_ticket=str(now.year) +  str(now.month) +  str(now.day) + str(now.hour) +  str(now.minute) + str(now.second)


		if Members_Credit_Sales_Selected.objects.filter(member=member,product=product,status=status,processed_by=processed_by):
			record_exist=Members_Credit_Sales_Selected.objects.filter(member=member,product=product,status=status).first()
			record_exist.quantity=quantity
			record_exist.unit_selling_price=unit_selling_price
			record_exist.total=total
			record_exist.save()
			return HttpResponseRedirect(reverse('Members_Credit_sales_item_select',args=(member_id,)))

		record=Members_Credit_Sales_Selected(member=member,status=status,product=product,ticket=selected_ticket,quantity=quantity,unit_selling_price=unit_selling_price,total=total,processed_by=processed_by)
		record.save()
		return HttpResponseRedirect(reverse('Members_Credit_sales_item_select',args=(member_id,)))
	
	user_level=Staff.objects.get(admin=CustomUser.objects.get(id=request.user.id))

	context={
	'user_level':user_level.userlevel.title,
	'form':form,
	'member':member,
	}
	return render(request,'shop_templates/members_credit_issue_item.html',context)



def Members_Credit_sales_item_select_remove(request,pk,member_id):
	item = Members_Credit_Sales_Selected.objects.get(id=pk)
	item.delete()
	return HttpResponseRedirect(reverse('Members_Credit_sales_item_select',args=(member_id,)))



def members_credit_sales_item_select_preview(request,pk,ticket):
	form=Members_Credit_Sales_submit_form(request.POST or None)
	
	sales = Members_Credit_Sales_Selected.objects.filter(ticket=ticket)
	sum_sales=Members_Credit_Sales_Selected.objects.filter(ticket=ticket).aggregate(total_sales=Sum('total'))
	
	if sum_sales['total_sales']:
		sum_total=float(sum_sales['total_sales'])
	else:
		sum_total=0



	status=TransactionStatus.objects.get(title='UNTREATED')
	
	member=Members.objects.get(id=pk)
	credit=member.gross_pay


	if credit <= 0:
		messages.info(request,'Gross Pay is Missing')
		return HttpResponseRedirect(reverse('Members_Credit_sales_item_select',args=(pk,)))


	if CompulsorySavings.objects.all().exists:
		item = CompulsorySavings.objects.first()
		if StandingOrderAccounts.objects.filter(transaction__member_id=pk,transaction__transaction=item.transaction).count():
			pass
		else:
			messages.info(request,'Some Compulsory Savings are Missing')
			return HttpResponseRedirect(reverse('Members_Credit_sales_item_select',args=(pk,)))
		
	else:
		messages.info(request,'No  Compulsory savings fixed')
		return HttpResponseRedirect(reverse('Members_Credit_sales_item_select',args=(pk,)))
	

	monthly_contributions= StandingOrderAccounts.objects.filter(transaction__member_id=pk)
	sum_monthly_contributions = StandingOrderAccounts.objects.filter(transaction__member_id=pk).aggregate(total_contribution=Sum('amount'))
	
	if sum_monthly_contributions['total_contribution']:
		monthly_contribution_debit=float(sum_monthly_contributions['total_contribution'])
	else:
		monthly_contribution_debit=0



	loan_repayments=LoansRepaymentBase.objects.filter(member_id=pk,balance__lt=0)
	sum_loan_repayments=LoansRepaymentBase.objects.filter(member_id=pk,balance__lt=0).aggregate(total_loan=Sum('repayment'))
	
	if sum_loan_repayments['total_loan']:
		loan_repayment_debit=float(sum_loan_repayments['total_loan'])
	else:
		loan_repayment_debit=0


	
	external_fascilities_debit=0
	external_fascilities=[]
	

	if ExternalFascilitiesMain.objects.filter(status=status).exists():
		external_fascilities = ExternalFascilitiesMain.objects.filter(member__member=member,status=status)
		
		sum_external_fascilities=ExternalFascilitiesMain.objects.filter(member__member=member,status=status).aggregate(total_amount=Sum('member__amount'))
		
	
	
		if sum_external_fascilities['total_amount']:
			external_fascilities_debit=float(sum_external_fascilities['total_amount'])
		else:
			external_fascilities_debit=0


	ledger_balance=[]
	ledger_balance_debit=0
	if CooperativeShopLedger.objects.filter(member_id=pk).exists():
		ledger_balance=CooperativeShopLedger.objects.filter(member_id=pk,balance__lt=0).order_by('-id').first()
		if ledger_balance.balance:
			ledger_balance_debit=float(ledger_balance.balance)
		else:
			ledger_balance_debit=0
	

	debit =external_fascilities_debit+ loan_repayment_debit + monthly_contribution_debit + ledger_balance_debit + abs(sum_total)
	balance = float(credit)- float(debit)
	

	# Posting to Summary Table

	if request.method=="POST":
		trans_code = Members_Credit_Sales_Selected.objects.filter(ticket=ticket).first()
		
		status=TransactionStatus.objects.get(title='UNTREATED')
		status1=TransactionStatus.objects.get(title='TREATED')
		approval_status=ApprovalStatus.objects.get(title="PENDING")
		

		officer_id=request.POST.get('approval_officers')
		officer=ApprovalOfficers.objects.get(id=officer_id)

		approval_comment=request.POST.get('comment')

		if members_credit_purchase_summary.objects.filter(trans_code=trans_code).exists():
			credit_purchase_summary_record=members_credit_purchase_summary.objects.get(trans_code=trans_code)
			credit_purchase_summary_record.approval_officer=officer
			credit_purchase_summary_record.approval_status=approval_status
			credit_purchase_summary_record.approval_comment=approval_comment
			credit_purchase_summary_record.debit=debit
			credit_purchase_summary_record.credit=credit
			credit_purchase_summary_record.balance=balance
			credit_purchase_summary_record.trans_code=trans_code
			credit_purchase_summary_record.status=status
			credit_purchase_summary_record.save()
		else:
			credit_purchase_summary_record=members_credit_purchase_summary(approval_officer=officer,approval_status=approval_status,approval_comment=approval_comment,debit=debit,credit=credit,balance=balance,trans_code=trans_code,status=status)
			credit_purchase_summary_record.save()

		
		credit_purchase_analysis_record=members_credit_purchase_analysis(trans_code=trans_code,particulars=member.gross_pay_as_at,debit=0,credit=member.gross_pay,status=status)
		credit_purchase_analysis_record.save()

		for monthly_contribution in monthly_contributions:
			monthly_contribution_record=members_credit_purchase_analysis(trans_code=trans_code,particulars=monthly_contribution.transaction.transaction.name,debit=monthly_contribution.amount,credit=0,status=status)
			monthly_contribution_record.save()
		
		for external_fascility in external_fascilities:
			external_fascility_record=members_credit_purchase_analysis(trans_code=trans_code,particulars=external_fascility.member.description,debit=external_fascility.member.amount,credit=0,status=status)
			external_fascility_record.save()
		
		for loan_repayment in loan_repayments:
			loan_repayment_record=members_credit_purchase_analysis(trans_code=trans_code,particulars=loan_repayment.transaction.name,debit=loan_repayment.repayment,credit=0,status=status)
			loan_repayment_record.save()

		if float(abs(ledger_balance_debit)) > 0:
			record=members_credit_purchase_analysis(trans_code=trans_code,particulars="COOPERATIVE LEDGER BALANCE",debit=abs(ledger_balance_debit),credit=0,status=status)
			record.save()
		

	
		source_update=Members_Credit_Sales_Selected.objects.filter(ticket=ticket).update(status=status1)
		
		return HttpResponseRedirect(reverse('Members_Credit_sales_list_search'))


	user_level=Staff.objects.get(admin=CustomUser.objects.get(id=request.user.id))

	context={
	'user_level':user_level.userlevel.title,
	'member':member,
	'monthly_contributions':monthly_contributions,
	'loan_repayments':loan_repayments,
	'external_fascilities':external_fascilities,
	'ledger_balance':ledger_balance,
	'balance':balance,
	'credit':credit,
	'debit':debit,
	'form':form,
	'ticket':ticket,
	'sales':sales,
	'sum_total':sum_total,
	
	}
	return render(request,'shop_templates/members_credit_sales_item_select_preview.html',context)



# def Members_Credit_Sales_external_fascilities_add(request,pk):
# 	form=Members_Credit_Sales_external_fascilities_form(request.POST or None)
# 	member = Members.objects.get(id=pk)
# 	trans_code = Members_Credit_Sales_Selected.objects.filter(member_id=pk).first()

# 	if request.method=="POST":
# 		form=Members_Credit_Sales_external_fascilities_form(request.POST)
# 		if form.is_valid():
# 			status=TransactionStatus.objects.get(title='UNTREATED')
# 			description=form.cleaned_data['description']
# 			amount=form.cleaned_data['amount']

# 			record=Members_Credit_Sales_external_fascilities(trans_code=trans_code,description=description,amount=amount,status=status)
# 			record.save()
# 			return HttpResponseRedirect(reverse('members_credit_sales_item_select_preview',args=(pk,)))

# 	context={
# 	'form':form,
# 	'member':member,
# 	}
# 	return render(request,'shop_templates/Members_Credit_Sales_external_fascilities.html',context)


# def Members_Credit_Sales_external_fascilities_delete(request,pk):
# 	record=Members_Credit_Sales_external_fascilities.objects.get(id=pk)
# 	return_pk=record.trans_code.member_id
# 	record.delete()
# 	return HttpResponseRedirect(reverse('members_credit_sales_item_select_preview',args=(return_pk,)))


def members_credit_purchase_summary_add(request,member_id,debit,credit,balance,ticket):
	if request.method=="POST":
		trans_code = Members_Credit_Sales_Selected.objects.filter(ticket=ticket).first()
		status=TransactionStatus.objects.get(title='UNTREATED')
		approval_status=ApprovalStatus.objects.get(title="PENDING")
		member=Members.objects.get(id=member_id)

		officer_id=request.POST.get('approval_officers')
		officer=ApprovalOfficers.objects.get(id=officer_id)

		approval_comment=request.POST.get('comment')

		record=members_credit_purchase_summary(member=member,approval_officer=officer,approval_status=approval_status,approval_comment=approval_comment,debit=debit,credit=credit,balance=balance,trans_code=trans_code,status=status)
		record.save()
		return HttpResponseRedirect(reverse('Members_Credit_sales_list_search'))


def members_credit_purchase_manage(request):
	status=TransactionStatus.objects.get(title="UNTREATED")
	approval_status=ApprovalStatus.objects.get(title='PENDING')
	records=members_credit_purchase_summary.objects.filter(status=status,approval_status=approval_status)

	user_level=Staff.objects.get(admin=CustomUser.objects.get(id=request.user.id))

	context={
	'user_level':user_level.userlevel.title,
	'records':records,

	}
	return render(request,'shop_templates/members_credit_purchase_manage.html',context)


def members_credit_purchase_manage_preview(request,ticket):
	form=Members_Credit_Sales_submit_form(request.POST or None)
	records=members_credit_purchase_analysis.objects.filter(trans_code__ticket=ticket)
	
	if request.method=="POST":
		trans_code = Members_Credit_Sales_Selected.objects.filter(ticket=ticket).first()
		
		status=TransactionStatus.objects.get(title='UNTREATED')
		status1=TransactionStatus.objects.get(title='TREATED')
		approval_status=ApprovalStatus.objects.get(title="PENDING")
		

		officer_id=request.POST.get('approval_officers')
		officer=ApprovalOfficers.objects.get(id=officer_id)

		approval_comment=request.POST.get('comment')

		if members_credit_purchase_summary.objects.filter(trans_code=trans_code).exists():
			record=members_credit_purchase_summary.objects.get(trans_code=trans_code)
			record.approval_officer=officer
			record.approval_status=approval_status
			record.approval_comment=approval_comment
			record.save()	
			return HttpResponseRedirect(reverse('members_credit_purchase_manage'))


	user_level=Staff.objects.get(admin=CustomUser.objects.get(id=request.user.id))

	context={
	'user_level':user_level.userlevel.title,
	'records':records,
	'form':form,
	'ticket':ticket,
	}
	return render(request,'shop_templates/members_credit_purchase_manage_preview.html',context)


def members_credit_purchase_selection_reset_confirmation(request,ticket):
	user_level=Staff.objects.get(admin=CustomUser.objects.get(id=request.user.id))

	context={
	'user_level':user_level.userlevel.title,
	'ticket':ticket,
	
	}
	return render(request,'shop_templates/members_credit_purchase_selection_reset_confirmation.html',context)


def members_credit_purchase_selection_reset_update(request,ticket):
	status=TransactionStatus.objects.get(title='UNTREATED')
	record=members_credit_purchase_summary.objects.filter(trans_code__ticket=ticket)
	record.delete()
	record=members_credit_purchase_analysis.objects.filter(trans_code__ticket=ticket)
	record.delete()
	records=Members_Credit_Sales_Selected.objects.filter(ticket=ticket).update(status=status)
	return_pk=Members_Credit_Sales_Selected.objects.filter(ticket=ticket).first()

	return HttpResponseRedirect(reverse('Members_Credit_sales_item_select',args=(return_pk.member_id,)))



def members_credit_purchase_selection_discard_confirmation(request,ticket):
	user_level=Staff.objects.get(admin=CustomUser.objects.get(id=request.user.id))

	context={
	'user_level':user_level.userlevel.title,
	'ticket':ticket,
	}
	return render(request,'shop_templates/members_credit_purchase_selection_discard_confirmation.html',context)


def members_credit_purchase_selection_discard_update(request,ticket):
	records=Members_Credit_Sales_Selected.objects.filter(ticket=ticket)
	records.delete()
	return HttpResponseRedirect(reverse('members_credit_purchase_manage'))




def members_credit_purchases_approved_list(request):
	status=TransactionStatus.objects.get(title="UNTREATED")
	approval_status=ApprovalStatus.objects.get(title='PENDING')
	approval_status1=ApprovalStatus.objects.get(title='APPROVED')
	items=members_credit_purchase_summary.objects.filter(status=status).exclude(approval_status=approval_status)
	
	user_level=Staff.objects.get(admin=CustomUser.objects.get(id=request.user.id))

	context={
	'user_level':user_level.userlevel.title,
	'items':items,
	'approval_status1':approval_status1,

	}
	return render(request,'shop_templates/members_credit_purchases_approved_list.html',context)


def members_credit_purchases_approved_item_details(request,ticket):
	form=Shop_Issue_Receipt_form(request.POST or None)

	items=Members_Credit_Sales_Selected.objects.filter(ticket=ticket)

	amount_due=0

	total=Members_Credit_Sales_Selected.objects.filter(ticket=ticket).aggregate(total_amount=Sum('total'))
	
	if float(total['total_amount']):
		amount_due=float(total['total_amount'])
	

	if request.method=="POST":
		status=TransactionStatus.objects.get(title="TREATED")	
		item=members_credit_purchase_summary.objects.get(trans_code__ticket=ticket)
		transaction=TransactionTypes.objects.get(code=600)
	
		if MembersAccountsDomain.objects.filter(member=item.trans_code.member,transaction=transaction).exists():
			member=MembersAccountsDomain.objects.get(member=item.trans_code.member,transaction=transaction)
		else:
			messages.error(request,"This Transaction Has no Account Number")
			return HttpResponseRedirect(reverse('members_credit_purchases_approved_item_details', args=(ticket,)))

		status=TransactionStatus.objects.get(title="UNTREATED")
		receipt_types_id=request.POST.get('receipt_types')
		receipt_types=ReceiptTypes.objects.get(id=receipt_types_id)

		if receipt_types.title=="MANUAL":
			# return HttpResponse("MANUAL")
			receipt_status=ReceiptStatus.objects.get(title='USED')
			receipt_id=request.POST.get('receipt_no')		
			
			
			if Receipts_Shop.objects.filter(receipt=receipt_id,status=receipt_status).exists():
				messages.error(request,"This Receipt is Already in Use")
				return HttpResponseRedirect(reverse('members_credit_purchases_approved_item_details',args=(ticket,)))
				
			receipt_id=Receipts_Shop.objects.get(receipt=receipt_id)
			receipt=receipt_id.receipt
			receipt_id.status=receipt_status
			receipt_id.save()

		elif receipt_types.title=="AUTO":
			# return HttpResponse("Auto")
			receipt_id=AutoReceipt.objects.first()
			receipt= receipt_id.receipt
			receipt_id.receipt=int(receipt_id.receipt)+1
			receipt_id.save()


		else:
			# return HttpResponse("None")
			messages.error(request,'Invalid Receipt Type Selection')
			return HttpResponseRedirect(reverse('members_credit_purchases_approved_item_details',args=(ticket,)))

		
		for item in items:
			product_update=Stock.objects.get(code=item.product.code)
	
			if int(item.quantity) > (int(product_update.quantity)-int(item.quantity)):
				messages.error(request,"Insufficient Quantity for product with code " + str(item.product.code))
				return HttpResponseRedirect(reverse('members_credit_purchases_approved_item_details',args=(ticket,)))


		for item in items:	
			name = item.member.admin.first_name + " " + item.member.admin.last_name + " " + item.member.middle_name
			address=item.member.residential_address
			phone_no=item.member.phone_number
			item_name=item.product.item_name.upper()
			item_code=item.product.code
			quantity=item.quantity
			unit_selling_price=item.unit_selling_price
			total=item.total
			
			

			record=Daily_Sales(receipt=receipt,name=name,phone_no=phone_no,address=address,item_code=item_code,item_name=item_name,ticket=item.ticket,quantity=quantity,unit_selling_price=unit_selling_price,total=total,processed_by=item.processed_by,status=status)
			record.save()

			product_update=Stock.objects.get(code=item_code)
			product_update.quantity=int(product_update.quantity)-int(quantity)
			product_update.save()
		

		processed_by=CustomUser.objects.get(id=request.user.id)
		sales_category=SalesCategory.objects.get(title='CREDIT')
		
		selected=Daily_Sales.objects.filter(ticket=ticket).first()

		

		record=Daily_Sales_Summary(receipt=receipt,sale=selected,amount=amount_due,sales_category=sales_category,status=status)
		record.save()
		

		status=TransactionStatus.objects.get(title="TREATED")	
		item=members_credit_purchase_summary.objects.get(trans_code__ticket=ticket)
		item.status=status
		item.save()

		
		particulars="Purchases with receipt No " + str(receipt)
		balance_amount= -float(amount_due)
		debit_amount = amount_due
		

		
		if MembersAccountsDomain.objects.filter(member=item.trans_code.member,transaction=transaction).exists():
			member=MembersAccountsDomain.objects.get(member=item.trans_code.member,transaction=transaction)
		

		if CooperativeShopLedger.objects.filter(member=member).exists():
			ledger_balance = CooperativeShopLedger.objects.filter(member=member).order_by('id').last()
			
			balance_amount=float(ledger_balance.balance) - float(amount_due)
			debit_amount = amount_due
			
		record=CooperativeShopLedger(receipt=receipt,member=member,particulars=particulars,debit=debit_amount,credit=0,balance=balance_amount,processed_by=processed_by)
		record.save()

		return HttpResponseRedirect(reverse('members_credit_purchases_approved_list'))
	
	user_level=Staff.objects.get(admin=CustomUser.objects.get(id=request.user.id))

	context={
	'user_level':user_level.userlevel.title,
	'form':form,
	'items':items,
	'amount_due':amount_due,
	}
	return render(request,'shop_templates/members_credit_purchases_approved_item_details.html',context)



def members_cash_sales_search(request):
	title="Search Members for Cash Deposit"
	form = searchForm(request.POST or None)
	user_level=Staff.objects.get(admin=CustomUser.objects.get(id=request.user.id))
	return render(request,'shop_templates/members_cash_sales_search.html',{'form':form,'title':title,'user_level':user_level.userlevel.title,})


def members_cash_sales_list_load(request):
	title="Membership Purchases"
	if request.method == "POST":
		form = searchForm(request.POST)
		status=MembershipStatus.objects.get(title="ACTIVE")
		members=Members.objects.filter(Q(phone_number__icontains=form['title'].value()) | Q(admin__first_name__icontains=form['title'].value()) | Q(admin__last_name__icontains=form['title'].value()) | Q(middle_name__icontains=form['title'].value())).filter(status=status)
		
		user_level=Staff.objects.get(admin=CustomUser.objects.get(id=request.user.id))
		context={
		'user_level':user_level.userlevel.title,
		'members':members,
		'title':title,
		}
		return render(request,'shop_templates/members_cash_sales_list_load.html',context)






def members_cash_sales_product_load(request,pk):
	form=Shop_Issue_Receipt_form(request.POST or None)
	items=Stock.objects.filter(Q(quantity__gt=0))
	
	status=TransactionStatus.objects.get(title="UNTREATED")
	member=Members.objects.get(id=pk)
	select_items=[]
	total_item=0
	total_amount=0
	
	if Members_Cash_Sales_Selected.objects.filter(member=member,status=status).exists():
		button_show=True
		select_items = Members_Cash_Sales_Selected.objects.filter(member=member,status=status)
		queryset=Members_Cash_Sales_Selected.objects.filter(ticket=select_items[0].ticket).aggregate(total_amount=Sum('total'),total_item=Sum('quantity'))
		total_item=queryset['total_item']
		total_amount=queryset['total_amount']
		ticket_holder=select_items[0].ticket

	else:
		button_show=False


	if request.method=="POST":

		receipt_types_id=request.POST.get('receipt_types')
		receipt_types=ReceiptTypes.objects.get(id=receipt_types_id)

		if receipt_types.title=="MANUAL":
			
			receipt_status=ReceiptStatus.objects.get(title='USED')
			receipt_id=request.POST.get('receipt_no')		
			
			if Receipts_Shop.objects.filter(receipt=receipt_id,status=receipt_status).exists():
				messages.error(request,"This Receipt is Already in Use")
				return HttpResponseRedirect(reverse('members_cash_sales_product_load',args=(pk,)))
				
			receipt_id=Receipts_Shop.objects.get(receipt=receipt_id)
			receipt=receipt_id.receipt
			receipt_id.status=receipt_status
			receipt_id.save()
		
		elif receipt_types.title=="AUTO":
			receipt_id=AutoReceipt.objects.first()
			receipt= receipt_id.receipt
			receipt_id.receipt=int(receipt_id.receipt)+1
			receipt_id.save()


		else:
			messages.error(request,"Invalid Receipt Type")
			return HttpResponseRedirect(reverse('members_cash_sales_product_load', args=(pk,)))

		for item in select_items:
			product_update=Stock.objects.get(code=item.product.code)
	
			if int(item.quantity) > (int(product_update.quantity)-int(item.quantity)):
				messages.error(request,"Insufficient Quantity for product with code " + str(item.code))
				return HttpResponseRedirect(reverse('members_cash_sales_product_load',args=(pk,)))

		for item in select_items:	
			name = item.member.admin.first_name + " " + item.member.admin.last_name + " " + item.member.middle_name
			address=item.member.residential_address
			phone_no=item.member.phone_number
			item_name=item.product.item_name.upper()
			item_code=item.product.code
			quantity=item.quantity
			unit_selling_price=item.unit_selling_price
			total=item.total
			

			record=Daily_Sales(receipt=receipt,name=name,phone_no=phone_no,address=address,product=item.product,ticket=item.ticket,quantity=quantity,unit_selling_price=unit_selling_price,total=total,processed_by=item.processed_by,status=status)
			record.save()
			
			
			product_update=Stock.objects.get(code=item_code)
			product_update.quantity=int(product_update.quantity)-int(quantity)
			product_update.save()
		
		processed_by=CustomUser.objects.get(id=request.user.id)
		sales_category=SalesCategory.objects.get(title='CASH')
		
		selected=Daily_Sales.objects.filter(ticket=ticket_holder).first()

		record=Daily_Sales_Summary(receipt=receipt,sale=selected,amount=total,sales_category=sales_category,status=status)
		record.save()
		
		status=TransactionStatus.objects.get(title="TREATED")	
		item = Members_Cash_Sales_Selected.objects.filter(ticket=ticket_holder).update(status=status)
	
		return HttpResponseRedirect(reverse('members_cash_sales_search'))



	user_level=Staff.objects.get(admin=CustomUser.objects.get(id=request.user.id))
	
	context={
	'user_level':user_level.userlevel.title,
	'form':form,
	'items':items,
	'member':member,
	'select_items':select_items,
	'total_item':total_item,
	'total_amount':total_amount,
	'button_show':button_show,
	}
	return render(request,'shop_templates/members_cash_sales_product_load.html',context)


def members_cash_sales_item_issue(request,pk,member_id):
	form=members_credit_issue_item_form(request.POST or None)
	product = Stock.objects.get(id=pk)
	member=Members.objects.get(id=member_id)
	
	form.fields['code'].initial=product.code
	form.fields['item_name'].initial=product.item_name
	form.fields['available_quantity'].initial=product.quantity
	form.fields['unit_selling_price'].initial=product.unit_selling_price

	if request.method=="POST":	
		
		status=TransactionStatus.objects.get(title="UNTREATED")
		quantity=request.POST.get('issue_quantity')
		if int(quantity)<=0:
			messages.error(request,"Quantity Selected cannot be Zero (0)")
			return HttpResponseRedirect(reverse('members_cash_sales_item_issue', args=(pk,member_id)))
		
		if int(quantity)>int(product.quantity):
			messages.error(request,"Quantity Selected is more that Available Quantity")
			return HttpResponseRedirect(reverse('members_cash_sales_item_issue', args=(pk,member_id)))
		

		unit_selling_price=product.unit_selling_price
		
		total=float(quantity) * float(unit_selling_price)
		processed_by=CustomUser.objects.get(id=request.user.id)

		if Members_Cash_Sales_Selected.objects.filter(member=member,status=status,processed_by=processed_by):
			ticket_id=Members_Cash_Sales_Selected.objects.filter(member=member,status=status).first()
			selected_ticket=ticket_id.ticket
		else:
			now = datetime.datetime.now()
			selected_ticket=str(now.year) +  str(now.month) +  str(now.day) + str(now.hour) +  str(now.minute) + str(now.second)


		if Members_Cash_Sales_Selected.objects.filter(member=member,product=product,status=status,processed_by=processed_by):
			record_exist=Members_Credit_Sales_Selected.objects.filter(member=member,product=product,status=status).first()
			record_exist.quantity=quantity
			record_exist.unit_selling_price=unit_selling_price
			record_exist.total=total
			record_exist.save()
			return HttpResponseRedirect(reverse('members_cash_sales_product_load',args=(member_id,)))

		record=Members_Cash_Sales_Selected(member=member,status=status,product=product,ticket=selected_ticket,quantity=quantity,unit_selling_price=unit_selling_price,total=total,processed_by=processed_by)
		record.save()
		return HttpResponseRedirect(reverse('members_cash_sales_product_load',args=(member_id,)))
	

	user_level=Staff.objects.get(admin=CustomUser.objects.get(id=request.user.id))
	
	context={
	'user_level':user_level.userlevel.title,
	'form':form,
	'member':member,
	}
	return render(request,'shop_templates/members_cash_sales_item_issue.html',context)

def members_cash_sales_item_delete(request,pk):
	record=Members_Cash_Sales_Selected.objects.get(id=pk)
	member_id=record.member_id
	record.delete()
	return HttpResponseRedirect(reverse('members_cash_sales_product_load',args=(member_id,)))



def general_cash_sales_dashboard(request):

	user_level=Staff.objects.get(admin=CustomUser.objects.get(id=request.user.id))
	
	context={
	'user_level':user_level.userlevel.title,
	}
	return render(request,'shop_templates/general_cash_sales_dashboard.html',context)


def general_cash_sales_products_load_route(request):
	processed_by=CustomUser.objects.get(id=request.user.id)
	customer_obj=CustomerID.objects.first()
	customer_id='C' + str(customer_obj.title).zfill(5)

	ticket_status=TicketStatus.objects.get(title='OPEN')
	status=ReceiptStatus.objects.get(title="UNUSED")
	locked_status=LockedStatus.objects.get(title='OPEN')
	cust_status=MembershipStatus.objects.get(title='ACTIVE')

	record_drop = General_Cash_Sales_Selected.objects.filter(processed_by=processed_by)
	record_drop.delete()

	Customers.objects.filter(locked_status=locked_status,processed_by=processed_by).delete()

	customer=Customers(customer_id=customer_id,status=status,cust_status=cust_status,locked_status=locked_status,processed_by=processed_by)
	customer.save()

	customer_obj.title=str(int(customer_obj.title) + 1).zfill(5)
	customer_obj.save()
	return HttpResponseRedirect(reverse('general_cash_sales_products_load',args=(customer.pk,0)))



def general_cash_sales_products_load(request,pk,ticket):
	customer=Customers.objects.get(id=pk)
	items=Stock.objects.filter(Q(quantity__gt=0))
	select_items=General_Cash_Sales_Selected.objects.filter(ticket=ticket)


	if General_Cash_Sales_Selected.objects.filter(ticket=ticket).exists():
		button_show=True
		
		select_items = General_Cash_Sales_Selected.objects.filter(ticket=ticket)
		queryset=General_Cash_Sales_Selected.objects.filter(ticket=ticket).aggregate(total_amount=Sum('total'),total_item=Sum('quantity'))
		total_item=queryset['total_item']
		total_amount=queryset['total_amount']
		
	else:
		total_item=0
		total_amount=0
		select_items=[]
		button_show=False


	user_level=Staff.objects.get(admin=CustomUser.objects.get(id=request.user.id))
	
	context={
	'user_level':user_level.userlevel.title,
	'items':items,
	'customer':customer,
	'select_items':select_items,
	'total_item':total_item,
	'total_amount':total_amount,
	'button_show':button_show,
	'ticket':ticket,
	}
	return render(request,'shop_templates/general_cash_sales_products_load.html',context)


def general_cash_sales_select_remove(request,pk,cust_id,ticket):
	item = General_Cash_Sales_Selected.objects.get(id=pk)
	item.delete()
	if General_Cash_Sales_Selected.objects.exclude(ticket=ticket).exists():
		locked_status=LockedStatus.objects.get(title='LOCKED')
		Customers.objects.filter(id=pk).update(phone_no=None,active_ticket=None,ticket_status=None,locked_status=locked_status)
	return HttpResponseRedirect(reverse('general_cash_sales_products_load',args=(cust_id,ticket)))



def general_cash_issue_item(request,pk,cust_id):
	processed_by=CustomUser.objects.get(id=request.user.id)
	form =form=members_credit_issue_item_form(request.POST or None)
	customer=Customers.objects.get(id=cust_id)
	product = Stock.objects.get(id=pk)
	form.fields['code'].initial=product.code
	form.fields['item_name'].initial=product.item_name
	form.fields['available_quantity'].initial=product.quantity
	form.fields['unit_selling_price'].initial=product.unit_selling_price

	if request.method == "POST":
		ticket_status=TicketStatus.objects.get(title="OPEN")
		cust_status=MembershipStatus.objects.get(title='ACTIVE')


		status=TransactionStatus.objects.get(title="UNTREATED")
		status1=ReceiptStatus.objects.get(title='USED')

		quantity=request.POST.get("issue_quantity")
		
		unit_selling_price=product.unit_selling_price
	
		
		total=float(quantity) * float(unit_selling_price)
		if Customers.objects.filter(ticket_status=ticket_status,cust_status=cust_status,processed_by=processed_by).exists():
			select_customer=Customers.objects.get(ticket_status=ticket_status,processed_by=processed_by)
			selected_ticket=select_customer.active_ticket


		else:
			now = datetime.datetime.now()
			selected_ticket=str(now.year) +  str(now.month) +  str(now.day) + str(now.hour) +  str(now.minute) + str(now.second)

			customer.status=status1
			customer.ticket_status=ticket_status
			customer.active_ticket=selected_ticket
			customer.processed_by=processed_by
			customer.save()


		record=General_Cash_Sales_Selected(customer=customer,product=product,ticket=selected_ticket,quantity=quantity,unit_selling_price=unit_selling_price,total=total,processed_by=processed_by,status=status)
		record.save()

		return HttpResponseRedirect(reverse('general_cash_sales_products_load',args=(cust_id,selected_ticket)))
	
	user_level=Staff.objects.get(admin=CustomUser.objects.get(id=request.user.id))
	
	context={
	'user_level':user_level.userlevel.title,
	'form':form,
	'customer':customer,

	}
	return render(request,"shop_templates/general_cash_issue_item.html",context)


def general_cash_issue_item_preview(request,ticket):
	form=general_cash_issue_item_form(request.POST or None)
	select_items=General_Cash_Sales_Selected.objects.filter(ticket=ticket)
	customer=Customers.objects.get(active_ticket=ticket)

	form.fields['name'].initial=customer.name
	form.fields['address'].initial=customer.address
	form.fields['phone_no'].initial=customer.phone_no
	form.fields['receipt'].initial='00001'



	queryset=General_Cash_Sales_Selected.objects.filter(ticket=ticket).aggregate(total_amount=Sum('total'),total_item=Sum('quantity'))
	total_item=queryset['total_item']
	total_amount=queryset['total_amount']

	cash=False

	if request.method=='POST' and 'btn_fetch' in request.POST:
		channels_id=request.POST.get('channels')
		channels=SalesCategory.objects.get(id=channels_id)
		
	

		if channels.title=="CASH":
			cash=True

	if request.method=='POST' and 'btn_submit' in request.POST:
		processed_by=CustomUser.objects.get(id=request.user.id)
		status=TransactionStatus.objects.get(title='UNTREATED')
		status1=TransactionStatus.objects.get(title='TREATED')
		receipt_status=ReceiptStatus.objects.get(title="USED")
		locked_status=LockedStatus.objects.get(title='LOCKED')


		

		cust_name=request.POST.get('name')
		address=request.POST.get('address')
		phone_no=request.POST.get('phone_no')
		
		customer=Customers.objects.get(active_ticket=ticket)
		customer.name=cust_name
		customer.address=address
		customer.phone_no=phone_no
		customer.save()
	

		channels_id=request.POST.get('channels')
		channels=SalesCategory.objects.get(id=channels_id)

		if channels.title == 'CASH':
			receipt_types_id=request.POST.get('receipt_types')
			receipt_types=ReceiptTypes.objects.get(id=receipt_types_id)

			if receipt_types.title == 'AUTO':
				receipt_id=AutoReceipt.objects.first()
				receipt= receipt_id.receipt
				receipt_id.receipt=int(receipt_id.receipt)+1
				receipt_id.save()
			elif receipt_types.title == 'MANUAL':
				receipt_id=request.POST.get('receipt')
				if receipt_id:
					receipt=Receipts_Shop.objects.get(receipt=receipt_id)
				else:
					messages.error(request,"Receipt Missing")
					return HttpResponseRedirect(reverse('general_cash_issue_item_preview',args=(ticket,)))
			else:
				messages.error(request,"Invalid Receipt Format")
				return HttpResponseRedirect(reverse('general_cash_issue_item_preview',args=(ticket,)))



			
			for item in select_items:
				quantity=int(item.quantity)
				total=int(item.total)
				record=Stock.objects.get(code=item.product.code)
				record.quantity=int(record.quantity)-quantity
				record.save()



				sales_detail=Daily_Sales(receipt=receipt,name=cust_name,phone_no=phone_no,address=address,product=item.product,ticket=item.ticket,quantity=item.quantity,unit_selling_price=item.unit_selling_price,total=item.total,processed_by=item.processed_by,status=status)
				sales_detail.save()

		
			sale=Daily_Sales.objects.filter(ticket=ticket).first()

			summary=Daily_Sales_Summary(receipt=receipt,sale=sale,amount=total,sales_category=channels,status=status)
			summary.save()
					
			
			Customers.objects.filter(active_ticket=ticket).update(active_ticket=None,ticket_status=None,locked_status=locked_status)
			
			if receipt_types.title == 'MANUAL':
				Receipts_Shop.objects.filter(receipt=receipt_id).update(status=receipt_status)

			General_Cash_Sales_Selected.objects.filter(ticket=ticket).delete()



		return HttpResponseRedirect(reverse('general_cash_sales_dashboard'))
	
	user_level=Staff.objects.get(admin=CustomUser.objects.get(id=request.user.id))
	
	context={
	'user_level':user_level.userlevel.title,
	'select_items':select_items,
	'total_item':total_item,
	'total_amount':total_amount,
	'form':form,
	'cash':cash,

	}
	return render(request,'shop_templates/general_cash_issue_item_preview.html',context)


def general_cash_load_existing_customers_search(request):
	title="Search Existing Customers"
	form = searchForm(request.POST or None)
	user_level=Staff.objects.get(admin=CustomUser.objects.get(id=request.user.id))
	
	return render(request,'shop_templates/general_cash_load_existing_customers_search.html',{'form':form,'title':title,'user_level':user_level.userlevel.title,})


def general_cash_load_existing_customers(request):
	title="Existing Registered Customers"
	if request.method == "POST":
		form = searchForm(request.POST)
		# return HttpResponse(form['title'].value())
		members=Customers.objects.filter(Q(phone_no__icontains=form['title'].value()) | Q(name__icontains=form['title'].value()))
		
		user_level=Staff.objects.get(admin=CustomUser.objects.get(id=request.user.id))
	
		context={
		'user_level':user_level.userlevel.title,
		'customers':members,
		'title':title,
		'ticket':'0'
		}
		return render(request,'shop_templates/general_cash_load_existing_customers.html',context)






# def general_cash_load_existing_customers(request):
# 	# locked_status=LockedStatus.objects.get(title='OPEN')
# 	customers=Customers.objects.filter(~Q(name='Anonymous'))
# 	# Customers.objects.all().update(active_ticket=None,ticket_status=None,locked_status=locked_status)
			
# 	context={
# 	'customers':customers,
# 	'ticket':'0'
# 	}
# 	return render(request,'shop_templates/general_cash_load_existing_customers.html',context)


def monthly_deductions_salary_institution_select(request):
	records=SalaryInstitution.objects.all()
	
	user_level=Staff.objects.get(admin=CustomUser.objects.get(id=request.user.id))
	
	context={
	'user_level':user_level.userlevel.title,
	'records':records,
	}
	return render(request,'shop_templates/monthly_deductions_salary_institution_select.html',context)


def monthly_deductions_generate(request,pk):
	salary_institution=SalaryInstitution.objects.get(id=pk)
	members=CooperativeShopLedger.objects.filter(Q(balance__lt=0) & Q(member__member__salary_institution=salary_institution))
	user_level=Staff.objects.get(admin=CustomUser.objects.get(id=request.user.id))
	
	context={
	'user_level':user_level.userlevel.title,
	'members':members,
	'salary_institution':salary_institution,
	}
	return render(request,'shop_templates/monthly_deductions_generate.html',context)


def monthly_deductions_generate_process(request,pk):
	salary_institution=SalaryInstitution.objects.get(id=pk)
	members=CooperativeShopLedger.objects.filter(Q(balance__lt=0) & Q(member__member__salary_institution=salary_institution))
	transaction=TransactionTypes.objects.get(code=600)
	transaction_period=TransactionPeriods.objects.get(status__title='ACTIVE')

	if MonthlyDeductionList.objects.filter(transaction_period=transaction_period,transaction=transaction,member__salary_institution=salary_institution).exists():
		messages.error(request,"Transaction already generated")
		return HttpResponseRedirect(reverse('monthly_deductions_generate',args=(pk,)))

	
	for member in members:
		record=MonthlyDeductionList(transaction_period=transaction_period,member=member.member.member,account_number=member.member.account_number,amount=abs(member.balance),transaction=transaction)
		record.save()

	if MonthlyDeductionList.objects.filter(transaction_period=transaction_period,transaction=transaction).exists():
		processed_by=CustomUser.objects.get(id=request.user.id)
		record=MonthlyGeneratedTransactions(transaction=transaction,transaction_period=transaction_period,processed_by=processed_by)
		record.save()

	return HttpResponseRedirect(reverse('monthly_deductions_salary_institution_select'))





def Members_Credit_sales_Cash_Deposit_search(request):
	title="Search Members for Cash Deposit"
	form = searchForm(request.POST or None)
	user_level=Staff.objects.get(admin=CustomUser.objects.get(id=request.user.id))
	
	return render(request,'shop_templates/Members_Credit_sales_Cash_Deposit_search.html',{'form':form,'title':title,'user_level':user_level.userlevel.title,})


def Members_Credit_sales_Cash_Deposit_list_load(request):
	title="Membership Purchases"
	if request.method == "POST":
		form = searchForm(request.POST)
		status=MembershipStatus.objects.get(title="ACTIVE")
		members=Members.objects.filter(Q(phone_number__icontains=form['title'].value()) | Q(admin__first_name__icontains=form['title'].value()) | Q(admin__last_name__icontains=form['title'].value()) | Q(middle_name__icontains=form['title'].value())).filter(status=status)
		user_level=Staff.objects.get(admin=CustomUser.objects.get(id=request.user.id))
	
		context={
		'user_level':user_level.userlevel.title,
		'members':members,
		'title':title,
		}
		return render(request,'shop_templates/Members_Credit_sales_Cash_Deposit_list_load.html',context)


def Members_Credit_sales_Cash_Deposit_Details(request,pk):
	user_level=Staff.objects.get(admin=CustomUser.objects.get(id=request.user.id))
	
	context={
	'user_level':user_level.userlevel.title,

	}
	return render(request,'shop_templates/Members_Credit_sales_Cash_Deposit_Details.html',context)




def Daily_Sales_Summarization(request,pk):
	from datetime import datetime
	form=Daily_Sales_Summarization_form(request.POST or None)
	current_user=request.user.id
	records=[]
	items=[]
	total_credit_amount=0
	total_cash_amount=0
	total_amount=0
	button_show = False
	if request.method == 'POST' and 'btn_fetch' in request.POST:

		status = TransactionStatus.objects.get(title='UNTREATED')
		
		current_date=request.POST.get('current_date')
		date_format = '%Y-%m-%d'
		dtObj = datetime.strptime(current_date, date_format)
	
		# records=Daily_Sales_Summary.objects.filter(sale__processed_by=current_user,status=status).filter(Q(created_at__year=dtObj.year) & Q(created_at__month=dtObj.month) & Q(created_at__day=dtObj.day))
		records=Daily_Sales_Summary.objects.filter(Q(sale__processed_by=current_user) & Q(created_at__gte=current_date)).filter(status=status)
		
		
		if records.count():
			button_show=True


		queryset=Daily_Sales_Summary.objects.filter(Q(sale__processed_by=current_user) & Q(created_at__gte=current_date)).filter(sales_category__title='CREDIT',status=status).aggregate(total_credit=Sum('amount'))
		total_credit_amount=queryset['total_credit']
	
		
		queryset=Daily_Sales_Summary.objects.filter(Q(sale__processed_by=current_user) & Q(created_at__gte=current_date)).filter(sales_category__title='CASH',status=status).aggregate(total_cash=Sum('amount'))
		total_cash_amount=queryset['total_cash']
	

		queryset=Daily_Sales_Summary.objects.filter(Q(sale__processed_by=current_user) & Q(created_at__gte=current_date)).filter(status=status).aggregate(total_amount=Sum('amount'))
		total_amount=queryset['total_amount']
	


		items=Daily_Sales.objects.filter(Q(processed_by=current_user) & Q(created_at__lte=current_date)).order_by('receipt').values_list('receipt','item_code','item_name').distinct()
	
	if request.method == 'POST' and 'btn_submit' in request.POST:
		status = TransactionStatus.objects.get(title='UNTREATED')
		status1 = TransactionStatus.objects.get(title='TREATED')
		
		current_date=request.POST.get('current_date')
		records=Daily_Sales_Summary.objects.filter(Q(sale__processed_by=current_user) & Q(created_at__gte=current_date)).filter(status=status)
		
		
		queryset=Daily_Sales_Summary.objects.filter(Q(sale__processed_by=current_user) & Q(created_at__gte=current_date)).filter(sales_category__title='CREDIT',status=status).aggregate(total_credit=Sum('amount'))
		total_credit_amount=queryset['total_credit']
	
		
		queryset=Daily_Sales_Summary.objects.filter(Q(sale__processed_by=current_user) & Q(created_at__gte=current_date)).filter(sales_category__title='CASH',status=status).aggregate(total_cash=Sum('amount'))
		total_cash_amount=queryset['total_cash']
	

		queryset=Daily_Sales_Summary.objects.filter(Q(sale__processed_by=current_user) & Q(created_at__gte=current_date)).filter(status=status).aggregate(total_amount=Sum('amount'))
		total_amount=queryset['total_amount']
		
		sales_category1=SalesCategory.objects.get(title='CASH')
		sales_category2=SalesCategory.objects.get(title='CREDIT')
		
		processed_by=CustomUser.objects.get(id=request.user.id)
		record=Daily_Sales_Cash_Flow_Summary(description='CASH SALES',amount=total_cash_amount,sales_category=sales_category1,processed_by=processed_by,status=status)
		record.save()

		record=Daily_Sales_Cash_Flow_Summary(description='CREDIT SALES',amount=total_credit_amount,sales_category=sales_category2,processed_by=processed_by,status=status)
		record.save()
		

		Daily_Sales_Summary.objects.filter(Q(sale__processed_by=current_user) & Q(created_at__gte=current_date)).filter(status=status).update(status=status1)

		return HttpResponseRedirect(reverse('Daily_Sales_Summarization', args=(pk,)))

	form.fields['current_date'].initial=now
	user_level=Staff.objects.get(admin=CustomUser.objects.get(id=request.user.id))
	
	context={
	'user_level':user_level.userlevel.title,
	'form':form,
	'button_show':button_show,
	'records':records,
	'items':items,
	'total_cash_amount':total_cash_amount,
	'total_credit_amount':total_credit_amount,
	'total_amount':total_amount,
	}
	return render(request,'shop_templates/Daily_Sales_Summarization.html',context)


def Daily_Sales_Summary_Detail(request,pk):
	title="DETAILS OF SALES FOR RECEIPT"
	records=Daily_Sales.objects.filter(receipt=pk)

	user_level=Staff.objects.get(admin=CustomUser.objects.get(id=request.user.id))
	
	context={
	'user_level':user_level.userlevel.title,
	'receipt':pk,
	'title':title,
	'records':records,
	}
	return render(request,'shop_templates/Daily_Sales_Summary_Detail.html',context)



def Stock_Status(request):
	records=Stock.objects.filter(quantity__lt=F('re_order_level'))

	# Entry.objects.filter(number_of_comments__gt=F('number_of_pingbacks'))
	user_level=Staff.objects.get(admin=CustomUser.objects.get(id=request.user.id))
	
	context={
	'user_level':user_level.userlevel.title,
	'records':records,
	}
	return render(request,'shop_templates/Stock_Status.html',context)


def Supplier_add(request):
	form = Suppliers_add_form(request.POST or None)
	suppliers = Suppliers.objects.all()
	if request.method == 'POST':
		if form.is_valid():
			prefix = request.POST.get('prefix')
			name = request.POST.get('name')
			if Suppliers.objects.filter(name=name).exists():
				messages.info(request,'Record Already Exist')
				return HttpResponseRedirect(reverse('Supplier_add'))
			else:
				record=Suppliers(name=name,prefix=prefix)
				record.save()
				return HttpResponseRedirect(reverse('Supplier_add'))
	
	user_level=Staff.objects.get(admin=CustomUser.objects.get(id=request.user.id))
	
	context={
	'user_level':user_level.userlevel.title,
	'form':form,
	'suppliers':suppliers,
	}
	return render(request,'shop_templates/Supplier_add.html',context)


def Supplier_edit(request,pk):
	form = Suppliers_add_form(request.POST or None)
	supplier = Suppliers.objects.get(id=pk)
	if request.method == 'POST':
		if form.is_valid():
			prefix = request.POST.get('prefix')
			name = request.POST.get('name')
			
			supplier.prefix=prefix
			supplier.name=name
			supplier.save()
			messages.success(request,'Record Updated Successfully')
			return HttpResponseRedirect(reverse('Supplier_add'))
			
	form.fields['prefix'].initial=supplier.prefix
	form.fields['name'].initial=supplier.name
	user_level=Staff.objects.get(admin=CustomUser.objects.get(id=request.user.id))
	
	context={
	'user_level':user_level.userlevel.title,
	'form':form,
	'supplier':supplier,
	}
	return render(request,'shop_templates/Supplier_edit.html',context)


def Supplier_Branches_add(request,pk):
	form=Suppliers_Branches_form(request.POST or None)
	supplier=Suppliers.objects.get(id=pk)
	branches=Suppliers_Branches.objects.filter(supplier=supplier)
	if request.method == 'POST':
		if form.is_valid():
			address = request.POST.get('address')
			phone = request.POST.get('phone')
			record=Suppliers_Branches(address=address,phone=phone,supplier=supplier)
			record.save()
			messages.success(request,'Record Addedd Successfully')
			return HttpResponseRedirect(reverse('Supplier_Branches_add', args=(pk,)))
		else:
			messages.info(request,'Missing Record')
			return HttpResponseRedirect(reverse('Supplier_Branches_add', args=(pk,)))
	
	user_level=Staff.objects.get(admin=CustomUser.objects.get(id=request.user.id))
	
	context={
	'user_level':user_level.userlevel.title,
		'supplier':supplier,
		'form':form,
		'branches':branches,
	}
	return render(request,'shop_templates/Supplier_Branches_add.html',context)


def Supplier_Branches_edit(request,pk):
	form=Suppliers_Branches_form(request.POST or None)

	branch=Suppliers_Branches.objects.get(id=pk)
	if request.method == 'POST':
		if form.is_valid():
			address = request.POST.get('address')
			phone = request.POST.get('phone')
			branch.address=address
			branch.phone=phone
			branch.save()
			messages.success(request,'Record Updated Successfully')
			return HttpResponseRedirect(reverse('Supplier_Branches_add', args=(branch.supplier.id,)))
		else:
			messages.info(request,'Missing Record')
			return HttpResponseRedirect(reverse('Supplier_Branches_add', args=(pk,)))
	
	form.fields['address'].initial=branch.address
	form.fields['phone'].initial=branch.phone
	
	user_level=Staff.objects.get(admin=CustomUser.objects.get(id=request.user.id))
	
	context={
	'user_level':user_level.userlevel.title,
		'supplier':branch.supplier,
		'form':form,
		'branch':branch,
	}
	return render(request,'shop_templates/Supplier_Branches_edit.html',context)



def Supplier_Personnel_add(request,pk):
	form=Suppliers_Personnel_form(request.POST or None)
	supplier=Suppliers.objects.get(id=pk)
	personnels = Suppliers_Reps.objects.filter(suppliers=supplier)
	
	if request.method == 'POST':
		if form.is_valid():
			name = request.POST.get('name')
			phone = request.POST.get('phone')
			record=Suppliers_Reps(name=name,phone=phone,suppliers=supplier)
			record.save()
			messages.success(request,'Record Addedd Successfully')
			return HttpResponseRedirect(reverse('Supplier_Personnel_add', args=(pk,)))
		else:
			messages.info(request,'Missing Record')
			return HttpResponseRedirect(reverse('Supplier_Personnel_add', args=(pk,)))
	
	user_level=Staff.objects.get(admin=CustomUser.objects.get(id=request.user.id))
	
	context={
	'user_level':user_level.userlevel.title,
		'form':form,
		'supplier':supplier,
		'personnels':personnels,
	}
	return render(request,'shop_templates/Supplier_Personnel_add.html',context)


def Supplier_Personnel_Edit(request,pk):
	form=Suppliers_Personnel_form(request.POST or None)
	personnel = Suppliers_Reps.objects.get(id=pk)

	if request.method == 'POST':
		if form.is_valid():
			name = request.POST.get('name')
			phone = request.POST.get('phone')
			personnel.name=name
			personnel.phone=phone
			personnel.save()
			messages.success(request,'Record Addedd Successfully')
			return HttpResponseRedirect(reverse('Supplier_Personnel_add', args=(personnel.suppliers.pk,)))
		else:
			messages.info(request,'Missing Record')
			return HttpResponseRedirect(reverse('Supplier_Personnel_add', args=(personnel.suppliers.pk,)))
	
	user_level=Staff.objects.get(admin=CustomUser.objects.get(id=request.user.id))
	form.fields['name'].initial=personnel.name
	form.fields['phone'].initial=personnel.phone
	context={
	'user_level':user_level.userlevel.title,
		'form':form,
		'personnel':personnel,
		
	}
	return render(request,'shop_templates/Supplier_Personnel_Edit.html',context)


def Product_Purchase(request):
	status=TransactionStatus.objects.get(title='UNTREATED')
	form = Product_Purchase_form(request.POST or None)
	suppliers=Suppliers.objects.all()
	records = Purchase_Header.objects.filter(status=status)


	if request.method == "POST":
		status = TransactionStatus.objects.get(title='UNTREATED')
		processed_by=CustomUser.objects.get(id=request.user.id)
		branch_id=request.POST.get('branch')
		branch = Suppliers_Branches.objects.get(id=branch_id)
		prefix = branch.supplier.prefix

		invoice_id=request.POST.get('invoice')
		invoice=prefix + '-' + str(invoice_id)
		invoice_date=request.POST.get('invoice_date')
		record=Purchase_Header(status=status,branch=branch,invoice=invoice,invoice_date=invoice_date,processed_by=processed_by)
		record.save()
		return HttpResponseRedirect(reverse('Product_Purchase'))

	form.fields['invoice_date'].initial = now

	user_level=Staff.objects.get(admin=CustomUser.objects.get(id=request.user.id))
	context={
	'user_level':user_level.userlevel.title,
	'suppliers':suppliers,
	'records':records,
	'form':form,
	}
	return render(request,'shop_templates/Product_Purchase.html',context)



def Product_Purchase_Add_Supplier(request):
	form = Suppliers_add_form(request.POST or None)
	suppliers = Suppliers.objects.all()
	if request.method == 'POST':
		if form.is_valid():
			prefix = request.POST.get('prefix')
			name = request.POST.get('name')
			if Suppliers.objects.filter(name=name).exists():
				messages.info(request,'Record Already Exist')
				return HttpResponseRedirect(reverse('Product_Purchase_Add_Supplier'))
			else:
				record=Suppliers(name=name,prefix=prefix)
				record.save()
				return HttpResponseRedirect(reverse('Product_Purchase_Add_Supplier'))
	
	user_level=Staff.objects.get(admin=CustomUser.objects.get(id=request.user.id))
	
	context={
	'user_level':user_level.userlevel.title,
	'form':form,
	'suppliers':suppliers,
	
	}
	return render(request,'shop_templates/Product_Purchase_Add_Supplier.html',context)


def Product_Purchase_Add_Supplier_Personnel(request,pk,return_pk):
	form=Suppliers_Personnel_form(request.POST or None)
	supplier = Suppliers.objects.get(id=pk)
	personnels=Suppliers_Reps.objects.filter(suppliers=supplier)

	if request.method == 'POST':
		if form.is_valid():
			name = request.POST.get('name')
			phone = request.POST.get('phone')
			record=Suppliers_Reps(name=name,phone=phone,suppliers=supplier)
			record.save()
			messages.success(request,'Record Addedd Successfully')
			return HttpResponseRedirect(reverse('Product_Purchase_Details', args=(return_pk,)))
		else:
			messages.info(request,'Missing Record')
			return HttpResponseRedirect(reverse('Product_Purchase_Add_Supplier_Personnel', args=(pk,)))
	


	context={
	'supplier':supplier,
	'form':form,
	'personnels':personnels,
	}
	return render(request,'shop_templates/Supplier_Personnel_add.html',context)


def Product_Purchase_Details(request,pk):
	status=TransactionStatus.objects.get(title='TREATED')
	
	invoice=Purchase_Header.objects.get(id=pk)
	invoice_items = Purchases_Temp.objects.filter(purchase=invoice)
	
	queryset=Purchases_Temp.objects.filter(purchase=invoice).aggregate(total_cost=Sum('total_cost'),total_item=Sum('quantity'))
	total_cost=queryset['total_cost']
	total_item=queryset['total_item']
	
	products = Stock.objects.all()
	
	user_level=Staff.objects.get(admin=CustomUser.objects.get(id=request.user.id))

	personnels=Suppliers_Reps.objects.filter(suppliers=invoice.branch.supplier)





	if request.method == "POST":
		personnel_id=request.POST.get('personnel')
		personnel=Suppliers_Reps.objects.get(id=personnel_id)

		

		invoice.personnel=personnel
		invoice.total_amount=total_cost
		invoice.status=status
		invoice.save()
	
		# record_update=Purchases_Temp.objects.filter(purchase=invoice).update(status=status)
		return HttpResponseRedirect(reverse('Product_Purchase'))

	context={
	'user_level':user_level.userlevel.title,
	'invoice':invoice,
	'products':products,
	'items':invoice_items,
	'personnels':personnels,
	'total_cost':total_cost,
	'total_item':total_item,
	}
	return render(request,'shop_templates/Product_Purchase_Details.html',context)



def Product_Purchase_Details_Select(request,pk,invoice_id):
	status=TransactionStatus.objects.get(title='UNTREATED')
	form = Product_Purchase_Select_form(request.POST or None)
	invoice=Purchase_Header.objects.get(id=invoice_id)
	
	product = Stock.objects.get(id=pk)
	
	if request.method == 'POST':
		quantity=request.POST.get("quantity")
		unit_cost=request.POST.get('unit_cost')
		unit_selling_price=request.POST.get('unit_selling_price')
		total_cost=float(unit_cost) * float(quantity)

		if float(unit_cost) <= 0:
			messages.info(request,'Cost Price cannot be Zero')
			return HttpResponseRedirect(reverse("Product_Purchase_Details_Select",args=(pk,invoice_id,)))

		if float(unit_selling_price) <= 0:
			messages.info(request,'Unit Selling Price cannot be Zero')
			return HttpResponseRedirect(reverse("Product_Purchase_Details_Select",args=(pk,invoice_id,)))

		if float(unit_cost) > float(unit_selling_price):
			messages.info(request,'Cost Price cannot be less than unit selling price')
			return HttpResponseRedirect(reverse("Product_Purchase_Details_Select",args=(pk,invoice_id,)))
		else:
			record=Purchases_Temp(purchase=invoice,product=product,quantity=quantity,cost_price=unit_cost,total_cost=total_cost,selling_price=unit_selling_price)
			record.save()
			return HttpResponseRedirect(reverse('Product_Purchase_Details',args=(invoice_id,)))

	user_level=Staff.objects.get(admin=CustomUser.objects.get(id=request.user.id))

	form.fields['code'].initial=product.code
	form.fields['item_name'].initial=product.item_name
	form.fields['unit_selling_price'].initial=product.unit_selling_price

	context={
	'user_level':user_level.userlevel.title,
	'invoice':invoice,
	'product':product,
	'form':form,
	
	}
	return render(request,'shop_templates/Product_Purchase_Details_Select.html',context)


def Product_Purchase_Details_Select_Remove(request,pk):
	record=Purchases_Temp.objects.get(id=pk)
	return_pk=record.purchase.pk
	record.delete()
	return HttpResponseRedirect(reverse('Product_Purchase_Details',args=(return_pk,)))



def Product_Purchase_Details_Select_Edit(request,pk):
	form = Product_Purchase_Select_form(request.POST or None)
	
	product = Purchases_Temp.objects.get(id=pk)
	

	if request.method == 'POST':
		quantity=request.POST.get("quantity")
		unit_cost=request.POST.get('unit_cost')
		unit_selling_price=request.POST.get('unit_selling_price')
		total_cost=float(unit_cost) * float(quantity)

		if float(unit_cost) <= 0:
			messages.info(request,'Cost Price cannot be Zero')
			return HttpResponseRedirect(reverse("Product_Purchase_Details_Select",args=(pk,)))

		if float(unit_selling_price) <= 0:
			messages.info(request,'Unit Selling Price cannot be Zero')
			return HttpResponseRedirect(reverse("Product_Purchase_Details_Select",args=(pk,)))

		if float(unit_cost) > float(unit_selling_price):
			messages.info(request,'Cost Price cannot be less than unit selling price')
			return HttpResponseRedirect(reverse("Product_Purchase_Details_Select",args=(pk,)))
		else:
			product.quantity=quantity
			product.cost_price=unit_cost
			product.total_cost=total_cost
			product.selling_price=unit_selling_price
			product.save()
			return HttpResponseRedirect(reverse('Product_Purchase_Details',args=(product.purchase.pk,)))

	user_level=Staff.objects.get(admin=CustomUser.objects.get(id=request.user.id))

	form.fields['code'].initial=product.product.code
	form.fields['item_name'].initial=product.product.item_name
	form.fields['quantity'].initial=product.quantity
	form.fields['unit_cost'].initial=product.cost_price
	form.fields['unit_selling_price'].initial=product.selling_price

	context={
	'user_level':user_level.userlevel.title,
	'product':product,
	'form':form,
	
	}
	return render(request,'shop_templates/Product_Purchase_Details_Select_Edit.html',context)


def Product_Purchase_Addnew_Item(request,pk):
	form=Stock_Update_form(request.POST or None)
	if request.method=="POST":
		category_id=request.POST.get('category')
		category=ProductCategory.objects.get(id=category_id)
		code=request.POST.get('code')
		item_name=request.POST.get('item_name').upper()
		quantity=request.POST.get('quantity')
		re_order_level=request.POST.get('re_order_level')
		no_in_pack=request.POST.get('no_in_pack')
		unit_selling_price=request.POST.get('unit_selling_price')
		record=Stock(category=category,code=code,item_name=item_name,quantity=quantity,re_order_level=re_order_level,no_in_pack=no_in_pack,unit_selling_price=unit_selling_price)
		record.save()
		messages.success(request,"Record Added Successfully")
		return HttpResponseRedirect(reverse('Product_Purchase_Details',args=(pk,)))

	user_level=Staff.objects.get(admin=CustomUser.objects.get(id=request.user.id))
	context={
	'user_level':user_level.userlevel.title,
	'form':form,
	}
	return render(request,'shop_templates/Product_Purchase_Addnew_Item.html',context)


def Purchase_Certification_List_load(request):
	status=TransactionStatus.objects.get(title='TREATED')
	certification_status=CertificationStatus.objects.get(title='PENDING')
	records=Purchase_Header.objects.filter(status=status,certification_status=certification_status)
	user_level=Staff.objects.get(admin=CustomUser.objects.get(id=request.user.id))

	context={
	'user_level':user_level.userlevel.title,
	'records':records,
	}
	return render(request,'shop_templates/Purchase_Certification_List_load.html',context)


def Purchase_Certification_item_Preview(request,pk):
	record=Purchase_Header.objects.get(id=pk)
	items=Purchases_Temp.objects.filter(purchase=record)
	user_level=Staff.objects.get(admin=CustomUser.objects.get(id=request.user.id))
	
	queryset=Purchases_Temp.objects.filter(purchase=record).aggregate(total_cost=Sum('total_cost'),total_item=Sum('quantity'))
	total_cost=queryset['total_cost']
	total_item=queryset['total_item']



	context={
	'user_level':user_level.userlevel.title,
	'items':items,
	'record':record,
	'total_cost':total_cost,
	'total_item':total_item,
	}
	return render(request,'shop_templates/Purchase_Certification_item_Preview.html',context)


def Purchase_Certification_item_Preview_Processed(request,pk):
	status=TransactionStatus.objects.get(title='UNTREATED')
	status1=CertificationStatus.objects.get(title='CERTIFIED')
	record=Purchase_Header.objects.get(id=pk)
	items=Purchases_Temp.objects.filter(purchase=record)
	for item in items:
		stock_record = Purchases(purchase=item.purchase,
			product=item.product,
			quantity=item.quantity,
			cost_price=item.cost_price,
			total_cost=item.total_cost,
			selling_price=item.selling_price,
			status=status,
			)
		stock_record.save()

		stock_update=Stock.objects.get(code=item.product.code)
		stock_update.quantity=int(stock_update.quantity) + int(item.quantity)
		stock_update.save()
	
	Purchases_Temp.objects.filter(purchase=record).delete()
	record.certification_status=status1
	record.save()
	return HttpResponseRedirect(reverse('Purchase_Certification_List_load'))



def Purchase_Certification_item_Preview_Remove(request,pk):
	item=Purchases_Temp.objects.get(id=pk)
	return_pk=item.purchase.pk
	item.delete()
	return HttpResponseRedirect(reverse('Purchase_Certification_item_Preview',args=(return_pk,)))


def Purchase_Certification_item_Add_Item(request,pk):
	products=Stock.objects.all()
	invoice=Purchase_Header.objects.get(id=pk)
	items=Purchases_Temp.objects.filter(purchase=pk)
	user_level=Staff.objects.get(admin=CustomUser.objects.get(id=request.user.id))
	
	queryset=Purchases_Temp.objects.filter(purchase=pk).aggregate(total_cost=Sum('total_cost'),total_item=Sum('quantity'))
	total_cost=queryset['total_cost']
	total_item=queryset['total_item']

	context={
	'user_level':user_level.userlevel.title,
	'products':products,
	'invoice':invoice,
	'items':items,
	'total_cost':total_cost,
	'total_item':total_item,
	}
	return render(request,'shop_templates/Purchase_Certification_item_Add_Item.html',context)


#
def Purchase_Certification_Product_Purchase_Details_Select(request,pk,invoice_id):
	status=TransactionStatus.objects.get(title='UNTREATED')
	form = Product_Purchase_Select_form(request.POST or None)
	invoice=Purchase_Header.objects.get(id=invoice_id)
	
	product = Stock.objects.get(id=pk)
	
	if request.method == 'POST':
		quantity=request.POST.get("quantity")
		unit_cost=request.POST.get('unit_cost')
		unit_selling_price=request.POST.get('unit_selling_price')
		total_cost=float(unit_cost) * float(quantity)

		if float(unit_cost) <= 0:
			messages.info(request,'Cost Price cannot be Zero')
			return HttpResponseRedirect(reverse("Purchase_Certification_Product_Purchase_Details_Select",args=(pk,invoice_id,)))

		if float(unit_selling_price) <= 0:
			messages.info(request,'Unit Selling Price cannot be Zero')
			return HttpResponseRedirect(reverse("Purchase_Certification_Product_Purchase_Details_Select",args=(pk,invoice_id,)))

		if float(unit_cost) > float(unit_selling_price):
			messages.info(request,'Cost Price cannot be less than unit selling price')
			return HttpResponseRedirect(reverse("Purchase_Certification_Product_Purchase_Details_Select",args=(pk,invoice_id,)))
		else:
			if Purchases_Temp.objects.filter(purchase=invoice,product=product).exists:
				record=Purchases_Temp(purchase=invoice,product=product)
				record.quantity=quantity
				record.cost_price=unit_cost
				record.total_cost=total_cost
				record.selling_price=unit_selling_price
				record.save()
				return HttpResponseRedirect(reverse('Purchase_Certification_item_Add_Item',args=(invoice_id,)))
			else:
				record=Purchases_Temp(purchase=invoice,product=product,quantity=quantity,cost_price=unit_cost,total_cost=total_cost,selling_price=unit_selling_price)
				record.save()
				return HttpResponseRedirect(reverse('Purchase_Certification_item_Add_Item',args=(invoice_id,)))

	user_level=Staff.objects.get(admin=CustomUser.objects.get(id=request.user.id))

	form.fields['code'].initial=product.code
	form.fields['item_name'].initial=product.item_name
	form.fields['unit_selling_price'].initial=product.unit_selling_price

	context={
	'user_level':user_level.userlevel.title,
	'invoice':invoice,
	'product':product,
	'form':form,
	
	}
	return render(request,'shop_templates/Purchase_Certification_Product_Purchase_Details_Select.html',context)


def Purchase_Certification_item_Preview_Reload(request,pk):
	return HttpResponseRedirect(reverse('Purchase_Certification_item_Preview',args=(pk,)))


def Purchase_Certification_item_Add_Stock(request,pk):
	form=Stock_Update_form(request.POST or None)
	if request.method=="POST":
		category_id=request.POST.get('category')
		category=ProductCategory.objects.get(id=category_id)
		code=request.POST.get('code')
		item_name=request.POST.get('item_name').upper()
		details=request.POST.get('details').upper()
		quantity=request.POST.get('quantity')
		re_order_level=request.POST.get('re_order_level')
		no_in_pack=request.POST.get('no_in_pack')
		unit_selling_price=request.POST.get('unit_selling_price')
		record=Stock(category=category,code=code,item_name=item_name,details=details,quantity=quantity,re_order_level=re_order_level,no_in_pack=no_in_pack,unit_selling_price=unit_selling_price)
		record.save()
		messages.success(request,"Record Added Successfully")
		return HttpResponseRedirect(reverse('Purchase_Certification_item_Add_Item',args=(pk,)))

	user_level=Staff.objects.get(admin=CustomUser.objects.get(id=request.user.id))
	context={
	'user_level':user_level.userlevel.title,
	'form':form,
	}
	return render(request,'shop_templates/Product_Purchase_Addnew_Item.html',context)


def Purchase_Certification_item_Edit(request,pk):
	form = Product_Purchase_Select_form(request.POST or None)
	user_level=Staff.objects.get(admin=CustomUser.objects.get(id=request.user.id))
	product=Purchases_Temp.objects.get(id=pk)
	
	form.fields['code'].initial=product.product.code
	form.fields['item_name'].initial=product.product.item_name
	form.fields['quantity'].initial=product.quantity
	form.fields['unit_cost'].initial=product.cost_price
	form.fields['unit_selling_price'].initial=product.selling_price


	if request.method == 'POST':
		quantity=request.POST.get("quantity")
		unit_cost=request.POST.get('unit_cost')
		unit_selling_price=request.POST.get('unit_selling_price')
		
		total_cost=float(unit_cost) * float(quantity)

		if float(unit_cost) <= 0:
			messages.info(request,'Cost Price cannot be Zero')
			return HttpResponseRedirect(reverse("Purchase_Certification_item_Edit",args=(pk,)))

		if float(unit_selling_price) <= 0:
			messages.info(request,'Unit Selling Price cannot be Zero')
			return HttpResponseRedirect(reverse("Purchase_Certification_item_Edit",args=(pk,)))

		if float(unit_cost) > float(unit_selling_price):
			messages.info(request,'Cost Price cannot be less than unit selling price')
			return HttpResponseRedirect(reverse("Purchase_Certification_item_Edit",args=(pk,)))
		else:
			product.quantity=quantity
			product.cost_price=unit_cost
			product.total_cost=total_cost
			product.selling_price=unit_selling_price
			product.save()


			queryset=Purchases_Temp.objects.filter(purchase=product.purchase).aggregate(total_cost=Sum('total_cost'),total_item=Sum('quantity'))
			total_cost=queryset['total_cost']
			total_item=queryset['total_item']
		
			product.purchase.total_amount=total_cost
			product.purchase.save()

			
			return HttpResponseRedirect(reverse('Purchase_Certification_item_Preview',args=(product.purchase.pk,)))



	context={
	'user_level':user_level.userlevel.title,
	'form':form,
	'product':product,
	}
	return render(request,'shop_templates/Purchase_Certification_item_Edit.html',context)


def All_Stock_Status(request):
	records=Stock.objects.all()
	user_level=Staff.objects.get(admin=CustomUser.objects.get(id=request.user.id))

	context={
	'user_level':user_level.userlevel.title,
	'records':records,
	}
	return render(request,'shop_templates/All_Stock_Status.html',context)

def Purchase_Summary(request):
	form=Purchase_Summary_form(request.POST or None)

	form.fields['start_date'].initial=now
	form.fields['stop_date'].initial=now
	user_level=Staff.objects.get(admin=CustomUser.objects.get(id=request.user.id))
	records=[]
	total_cost=0
	if request.method == 'POST':
		status1=TransactionStatus.objects.get(title='TREATED')
		status2=CertificationStatus.objects.get(title='CERTIFIED')
		start_date=request.POST.get("start_date")
		stop_date=request.POST.get("stop_date")
		records=Purchase_Header.objects.filter(Q(invoice_date__gte=start_date) & Q(invoice_date__lte=stop_date)).filter(status=status1,certification_status=status2)
		
		queryset=Purchase_Header.objects.filter(Q(invoice_date__gte=start_date) & Q(invoice_date__lte=stop_date)).filter(status=status1,certification_status=status2).aggregate(total_cost=Sum('total_amount'))
		total_cost=queryset['total_cost']
		



	context={
	'user_level':user_level.userlevel.title,
	'form':form,
	'records':records,
	'total_cost':total_cost,
	}
	return render(request,'shop_templates/Purchase_Summary.html',context)


def Purchase_Summary_Details(request,pk):
	invoice=Purchase_Header.objects.get(invoice=pk)
	
	user_level=Staff.objects.get(admin=CustomUser.objects.get(id=request.user.id))
	records=Purchases.objects.filter(purchase__invoice=invoice.invoice)

	queryset=Purchases.objects.filter(purchase__invoice=invoice.invoice).aggregate(total_cost=Sum('total_cost'),total_item=Sum('quantity'))
	total_cost=queryset['total_cost']
	total_item=queryset['total_item']


	context={
	'user_level':user_level.userlevel.title,
	'total_cost':total_cost,
	'total_item':total_item,
	'records':records,
	}
	return render(request,'shop_templates/Purchase_Summary_Details.html',context)


def load_branches(request):
    print("ok")
    supplier_id = request.GET.get('supplier')
    branches = Suppliers_Branches.objects.filter(supplier=supplier_id).order_by('address')
    return render(request, 'shop_templates/branches_dropdown_list_options.html',{'branches':branches})
 