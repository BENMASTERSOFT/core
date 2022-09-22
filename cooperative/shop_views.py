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

from datetime import date
import datetime
from django.db.models import  F, CharField, Value as V
from django.db.models.functions import Concat
from cooperative.resources import NorminalRollResource, AccountDeductionsResource
from tablib import Dataset
from django.template import defaultfilters
from django.contrib import messages

from datetime import datetime
from datetime import date
import datetime

from django.utils.dateparse import parse_date
from dateutil.relativedelta import relativedelta

import xlwt
from django.db.models import F
import pandas as pd

# importing the necessary libraries
from django.http import HttpResponse
from django.views.generic import View
from .process import html_to_pdf
from django.template.loader import render_to_string
from .current_date import *
from django.http import FileResponse
import io
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter


from .members_search import *
from .shopTools import *
from .purchaseTools import *
from .loan_data import generate_number
from .load_ticket import get_ticket
from .cashbook_manager import *
from .receipt_manager import *
from .Stock_Code import *

now = datetime.now(tz=timezone.utc) # you can use this value
# now = datetime.datetime.now()



#Creating a class based view
class GeneratePdf(View):
     def get(self, request, *args, **kwargs):

        # getting the template
        pdf = html_to_pdf('shop_templates/result.html')

         # rendering the template
        return HttpResponse(pdf, content_type='application/pdf')

class GeneratePdf2(View):
     def get(self, request, *args, **kwargs):

        # getting the template
        pdf = html_to_pdf('shop_templates/result2.html')

         # rendering the template
        return HttpResponse(pdf, content_type='application/pdf')

#Creating a class based view
class GeneratePdf3(View):
     def get(self, request, *args, **kwargs):
        data = Staff.objects.all().order_by('admin__first_name')
        open('templates/temp.html', "w").write(render_to_string('shop_templates/result3.html', {'data': data}))

        # Converting the HTML template into a PDF file
        pdf = html_to_pdf('temp.html')

         # rendering the template
        return HttpResponse(pdf, content_type='application/pdf')

#Creating a class based view
class GeneratePdf4(View):
   def get(self, request, *args, **kwargs):
      data = Daily_Sales.objects.filter(receipt= 292).first()
      records = Daily_Sales.objects.filter(receipt= 293)
      open('templates/temp.html', "w").write(render_to_string('shop_templates/result4.html',{'data': data,'records':records} ))

        # Converting the HTML template into a PDF file
      pdf = html_to_pdf('temp.html')

         # rendering the template
      return HttpResponse(pdf, content_type='application/pdf')

def All_Stock_Status_Pdf(request):
	# Create Bytestream Buffer
	buf = io.BytesIO()

	# Create a Canvas
	c = canvas.Canvas(buf, pagesize=letter,bottomup=0)
	# Create a text object

	textob = c.beginText()
	textob.setTextOrigin(inch, inch)
	textob.setFont("Helvetica", 14)

	# Add some lines of Text
	# lines=[
	# "This is line 1",
	# "This is line 2",
	# "This is line 3",
	# "This is line 4",
	# ]
	products = Stock.objects.all()

	lines=[]
	for product in products:
		lines.append(product.code)
		lines.append(product.item_name)
		lines.append(str(product.quantity))
		lines.append(str(product.unit_selling_price))
		lines.append(" ")
	# loop

	for line in lines:
		textob.textLine(line)
	# Finish up

	c.drawText(textob)
	c.showPage()
	c.save()
	buf.seek(0)

	# Return something

	return FileResponse(buf, as_attachment=True,filename="Stock_list.pdf")


def shop_home(request):
	task_array=[]
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	for task in tasks:
		task_array.append(task.task.title)

	title="SHOP"
	status="UNTREATED"
	approval_status='APPROVED'
	members_credit_purchases=members_credit_sales_summary.objects.filter(status=status,approval_status=approval_status).count()



	context={
	'task_array':task_array,
	'task_array':task_array,
	'title':title,
	'members_credit_purchases':members_credit_purchases,
	}
	return render(request, "shop_templates/dashboard.html",context)

def Useraccount_manager_Shop(request):
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	task_array=[]
	for task in tasks:
		task_array.append(task.task.title)



	task_status='YES'
	task_enabler=TransactionEnabler.objects.filter(status=task_status)
	task_enabler_array=[]
	for item in task_enabler:
		task_enabler_array.append(item.title)


	form=Useraccount_manager_form(request.POST or None)
	user=CustomUser.objects.get(id=request.user.id)

	form.fields['username'].initial= user.username
	if request.method == 'POST':
		change_password=request.POST.get('changepassword')
		password1=request.POST.get('password1')
		password2=request.POST.get('password2')

		if password1 != password2:
			messages.info(request,"Password Mistmatch")
			return HttpResponseRedirect(reverse('Useraccount_manager'))

		user.username=username
		user.set_password(password1)
		user.save()
		return HttpResponseRedirect(reverse('Useraccount_manager'))

	context={
	'form':form,
	'task_array':task_array,
	'task_enabler_array':task_enabler_array,
	}
	return render(request,'shop_templates/Useraccount_manager_Shop.html',context)


def basic_form(request):
	return render(request, 'shop_templates/basics/basic_form1.html')


def advance_form(request):
	return render(request, 'shop_templates/basics/advance_plugin_form.html')

def editable_invoice(request):
	return render(request, 'shop_templates/basics/invoice_2.html')

def Item_Write_off_Reasons(request):
	task_array=[]
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	for task in tasks:
		task_array.append(task.task.title)

	form=addItemWriteOffReasonsForm(request.POST or None)
	items=ItemWriteOffReasons.objects.all()
	if request.method == 'POST':
		form = addItemWriteOffReasonsForm(request.POST)
		if form.is_valid():
			form.save()
			messages.success(request,'Record Successfully Added')
			return HttpResponseRedirect(reverse('Item_Write_off_Reasons'))

		messages.info(request,'Please enter title')
		return HttpResponseRedirect(reverse('Item_Write_off_Reasons'))
	context={
	'task_array':task_array,
	'form':form,
	'items':items,
	}
	return render(request,'shop_templates/Item_Write_off_Reasons.html',context)

def Item_Write_off_Reasons_delete(request,pk):
	item =ItemWriteOffReasons.objects.get(id=pk)

	item.delete()
	return HttpResponseRedirect(reverse('Item_Write_off_Reasons'))


@csrf_exempt
def check_receipt_no_exist(request):
	status='USED'
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
	task_array=[]
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	for task in tasks:
		task_array.append(task.task.title)

	categories=ProductCategory.objects.all()


	context={
	'task_array':task_array,
	'categories':categories,
	}
	return render(request,'shop_templates/Stock_Category_Load.html',context)


def Stock_add(request,pk):
	task_array=[]
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	for task in tasks:
		task_array.append(task.task.title)

	category=ProductCategory.objects.get(id=pk)
	form=Stock_form(request.POST or None)
	lock_status="OPEN"
	last_stock = Stock.objects.filter().last()

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
		record=Stock(lock_status=lock_status,category=category,code=code,item_name=item_name,details=details,quantity=quantity,re_order_level=re_order_level,no_in_pack=no_in_pack,unit_selling_price=unit_selling_price,unit_cost_price=unit_cost_price)
		record.save()
		messages.success(request,"Record Added Successfully")
		return HttpResponseRedirect(reverse('Stock_add',args=(pk,)))

	if last_stock:
		form.fields['code'].initial = int(last_stock.code) + 1
	context={
	'task_array':task_array,
	'form':form,

	'category':category,
	'products':products,
	'return_pk':pk,
	}
	return render(request,'shop_templates/Stock_add.html',context)


def Update_Stock(request,pk,return_pk):
	task_array=[]
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	for task in tasks:
		task_array.append(task.task.title)

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

	context={
	'task_array':task_array,
	'form':form,
	'product':product,
	'return_pk':pk,
	}
	return render(request,'shop_templates/Stock_Update.html',context)


def Manage_Stock_Product_load_All(request):
	task_array=[]
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	for task in tasks:
		task_array.append(task.task.title)

	title="Product List"
	stocks=Stock.objects.filter(Q(quantity__lte=0))

	context={
	'task_array':task_array,

	'stocks':stocks,
	'title':title,
	}
	return render(request,'shop_templates/Manage_Stock_Product_load_All.html',context)


def Manage_Stock_Product_Update_All(request,pk):
	task_array=[]
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	for task in tasks:
		task_array.append(task.task.title)

	form=Stock_Update_form(request.POST or None)

	product = Stock.objects.get(id=pk)

	form.fields['code'].initial=product.code
	form.fields['item_name'].initial=product.item_name
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
		if product.lock_status == 'OPEN':
			quantity=request.POST.get('quantity')
		re_order_level=request.POST.get('re_order_level')
		no_in_pack=request.POST.get('no_in_pack')
		unit_selling_price=request.POST.get('unit_selling_price')
		unit_cost_price=request.POST.get('unit_cost_price')
		product.category=category
		product.code=code
		product.item_name=item_name.upper()

		if product.lock_status == 'OPEN':
			product.quantity=quantity
		product.re_order_level=re_order_level
		product.no_in_pack=no_in_pack
		product.unit_selling_price=unit_selling_price
		product.unit_cost_price=unit_cost_price
		product.save()
		messages.success(request,"Record Updated Successfully")
		return HttpResponseRedirect(reverse('Manage_Stock_Product_load_All'))
	context={
	'task_array':task_array,
	'form':form,
	'product':product,
	}
	return render(request,'shop_templates/Manage_Stock_Product_Update_All.html',context)

def Manage_Stock_Product_delete_All(request,pk):
	task_array=[]
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	for task in tasks:
		task_array.append(task.task.title)

	product=Stock.objects.get(id=pk)
	if request.method == "POST":
		if Purchases.objects.filter(product=product).exists():
			messages.error(request,'This Product cannot be Deleted, it is alrady in Use')
			return HttpResponseRedirect(reverse('Manage_Stock_Product_load_All',args=(pk,)))
		else:
			# record.delete()
			return HttpResponseRedirect(reverse('Manage_Stock_search'))


	context={
	'task_array':task_array,
	'product':product,
	}
	return render(request,'shop_templates/Manage_Stock_Product_delete_All.html',context)



def Manage_Stock_search(request):
	task_array=[]
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	for task in tasks:
		task_array.append(task.task.title)

	title="Search Stock"
	form = searchForm(request.POST or None)

	return render(request,'shop_templates/Manage_Stock_search.html',{'form':form,'title':title,'task_array':task_array})


def Manage_Stock_Product_load(request):
	task_array=[]
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	for task in tasks:
		task_array.append(task.task.title)

	title="Product List"
	if request.method == "POST":
		form = searchForm(request.POST)
		if form['title'].value():
			stocks=Stock.objects.filter(Q(code__icontains=form['title'].value()) | Q(item_name__icontains=form['title'].value()))

			context={
			'task_array':task_array,

				'stocks':stocks,
				'title':title,
			}
			return render(request,'shop_templates/Manage_Stock_Product_load.html',context)
		messages.info(request,'Please Enter Search')
		return HttpResponseRedirect(reverse('Manage_Stock_search'))


def Manage_Stock_Product_delete(request,pk):
	task_array=[]
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	for task in tasks:
		task_array.append(task.task.title)

	product=Stock.objects.get(id=pk)
	if request.method == "POST":
		if Purchases.objects.filter(product=product).exists():
			messages.error(request,'This Product cannot be Deleted, it is alrady in Use')
			return HttpResponseRedirect(reverse('Manage_Stock_Product_delete',args=(pk,)))
		else:
			# record.delete()
			return HttpResponseRedirect(reverse('Manage_Stock_search'))


	context={
	'task_array':task_array,
	'product':product,
	}
	return render(request,'shop_templates/Manage_Stock_Product_delete.html',context)


def Manage_Stock_Product_Update(request,pk):
	task_array=[]
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	for task in tasks:
		task_array.append(task.task.title)

	form=Stock_Update_form(request.POST or None)

	product = Stock.objects.get(id=pk)

	form.fields['code'].initial=product.code
	form.fields['item_name'].initial=product.item_name
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
		if product.lock_status == 'OPEN':
			quantity=request.POST.get('quantity')
		re_order_level=request.POST.get('re_order_level')
		no_in_pack=request.POST.get('no_in_pack')
		unit_selling_price=request.POST.get('unit_selling_price')
		unit_cost_price=request.POST.get('unit_cost_price')
		product.category=category
		product.code=code
		product.item_name=item_name.upper()

		if product.lock_status== 'OPEN':
			product.quantity=quantity
		product.re_order_level=re_order_level
		product.no_in_pack=no_in_pack
		product.unit_selling_price=unit_selling_price
		product.unit_cost_price=unit_cost_price
		product.save()
		messages.success(request,"Record Updated Successfully")
		return HttpResponseRedirect(reverse('Manage_Stock_Product_Update',args=(pk,)))
	context={
	'task_array':task_array,
	'form':form,
	'product':product,
	}
	return render(request,'shop_templates/Manage_Stock_Product_Update.html',context)



def Manage_Stock_Product_Lock(request):
	task_array=[]
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	for task in tasks:
		task_array.append(task.task.title)

	stocks = Stock.objects.all()
	context={
	'task_array':task_array,
	'stocks':stocks,
	}
	return render(request,'shop_templates/Manage_Stock_Product_Lock.html',context)




def Manage_Stock_Product_Lock_Individuals(request,pk):
	locked_status='LOCKED'
	stock = Stock.objects.get(id=pk)
	stock.lock_status=locked_status
	stock.save()
	return HttpResponseRedirect(reverse('Manage_Stock_Product_Lock'))


def Manage_Stock_Product_UnLock_Individuals(request,pk):
	locked_status='OPEN'
	stock = Stock.objects.get(id=pk)
	stock.lock_status=locked_status
	stock.save()
	return HttpResponseRedirect(reverse('Manage_Stock_Product_Lock'))


def Manage_Stock_Product_Lock_Multiple(request):
	lock_status='LOCKED'
	stock_update=Stock.objects.all().update(lock_status=lock_status)

	return HttpResponseRedirect(reverse('Manage_Stock_Product_Lock'))


def Manage_Stock_Product_UNLock_Multiple(request):
	lock_status='OPEN'
	stock_update=Stock.objects.all().update(lock_status=lock_status)

	return HttpResponseRedirect(reverse('Manage_Stock_Product_Lock'))


def Item_Write_off_search(request):
	task_array=[]
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	for task in tasks:
		task_array.append(task.task.title)

	title="Search Stock"
	form = searchForm(request.POST or None)

	return render(request,'shop_templates/Item_Write_off_search.html',{'form':form,'title':title,'task_array':task_array})


def Item_Write_off_product_load(request):
	task_array=[]
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	for task in tasks:
		task_array.append(task.task.title)

	title="Product List"
	if request.method == "POST":
		form = searchForm(request.POST)
		if form['title'].value():
			stocks=Stock.objects.filter(Q(code__icontains=form['title'].value()) | Q(item_name__icontains=form['title'].value()))

			if stocks:
				context={
	'task_array':task_array,

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
	task_array=[]
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	for task in tasks:
		task_array.append(task.task.title)

	form = Item_Write_off_product_form(request.POST or None)
	item = Stock.objects.get(id=pk)



	if request.method =='POST':
		tdate=get_current_date(now)
		status="UNTREATED"
		approval_status='PENDING'
		processed_by=CustomUser.objects.get(id=request.user.id)
		processed_by=processed_by.username

		reason_id=request.POST.get('reasons')
		reason=ItemWriteOffReasons.objects.get(id=reason_id)
		available_quantity=item.quantity
		if item.unit_cost_price:
			cost_price = item.unit_cost_price
		else:
			cost_price=request.POST.get('unit_cost_price')

		quantity=request.POST.get('quantity')
		total_cost = float(quantity)* float(cost_price)
		details=request.POST.get('details')

		if not quantity:
			messages.info(request,'Quantity is Missing')
			return HttpResponseRedirect(reverse('Item_Write_off_product_Preview',args=(pk,)))

		if not details:
			messages.info(request,'Detail is Missing')
			return HttpResponseRedirect(reverse('Item_Write_off_product_Preview',args=(pk,)))

		if float(cost_price) <= 0:
			messages.info(request,'Please Update the Unit Cost Price')
			return HttpResponseRedirect(reverse('Item_Write_off_product_Preview',args=(pk,)))

		record = ItemWriteOffTemp(details=details,tdate=tdate,product=item,reason=reason,quantity=quantity,cost_price=cost_price,total_cost=total_cost,processed_by=processed_by,approval_status="PENDING",status="UNTREATED",route="MAIN")
		record.save()

		item.unit_cost_price=cost_price
		item.save()

		return HttpResponseRedirect(reverse('Item_Write_off_search'))


	form.fields['code'].initial = item.code
	form.fields['item_name'].initial = item.item_name
	form.fields['available_quantity'].initial = item.quantity
	form.fields['unit_selling_price'].initial = item.unit_selling_price

	context={
	'task_array':task_array,
	'form':form,
	}
	return render(request,'shop_templates/Item_Write_off_product_Preview.html',context)




def Item_Write_off_product_Auction_Preview(request,pk):
	task_array=[]
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	for task in tasks:
		task_array.append(task.task.title)

	processed_by=CustomUser.objects.get(id=request.user.id)
	processed_by=processed_by.username


	form = Item_Write_off_product_form(request.POST or None)
	item=[]
	if Stock_Auction.objects.filter(stock__code=pk).exists():
		item = Stock_Auction.objects.get(stock__code=pk)
	else:
		messages.error(request,"No record found")



	if request.method =='POST':
		tdate=get_current_date(now)

		reason_id=request.POST.get('reasons')
		reason=ItemWriteOffReasons.objects.get(id=reason_id)
		available_quantity=item.quantity
		if item.stock.unit_cost_price:
			cost_price = item.stock.unit_cost_price
		else:
			cost_price=request.POST.get('unit_cost_price')

		quantity=request.POST.get('quantity')
		total_cost = float(quantity)* float(cost_price)
		details=request.POST.get('details')

		if not quantity:
			messages.info(request,'Quantity is Missing')
			return HttpResponseRedirect(reverse('Item_Write_off_product_Preview',args=(pk,)))

		if not details:
			messages.info(request,'Detail is Missing')
			return HttpResponseRedirect(reverse('Item_Write_off_product_Preview',args=(pk,)))

		if float(cost_price) <= 0:
			messages.info(request,'Please Update the Unit Cost Price')
			return HttpResponseRedirect(reverse('Item_Write_off_product_Preview',args=(pk,)))

		record = ItemWriteOffTemp(details=details,tdate=tdate,product=item.stock,reason=reason,quantity=quantity,cost_price=cost_price,total_cost=total_cost,processed_by=processed_by,approval_status="PENDING",status="UNTREATED",route="AUCTION")
		record.save()

		item.stock.unit_cost_price=cost_price
		item.stock.save()

		return HttpResponseRedirect(reverse('Item_Write_off_search'))

	if item:
		form.fields['code'].initial = item.stock.code
		form.fields['item_name'].initial = item.stock.item_name
		form.fields['unit_cost_price'].initial = item.stock.unit_cost_price
		form.fields['available_quantity'].initial = item.quantity
		form.fields['unit_selling_price'].initial = item.unit_selling_price

	context={
	'task_array':task_array,
	'form':form,
	}
	return render(request,'shop_templates/Item_Write_off_product_Auction_Preview.html',context)


def Item_Write_off_manage(request):
	task_array=[]
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	for task in tasks:
		task_array.append(task.task.title)

	status='UNTREATED'
	approval_status='PENDING'
	records =ItemWriteOffTemp.objects.filter(approval_status=approval_status,status=status)

	context={
	'task_array':task_array,
	'records':records,

	}
	return render(request,'shop_templates/Item_Write_off_manage.html',context)


def Item_Write_off_manage_Preview(request,pk):
	task_array=[]
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	for task in tasks:
		task_array.append(task.task.title)
	
	processed_by=CustomUser.objects.get(id=request.user.id)
	processed_by=processed_by.username

	form = Item_Write_off_product_form(request.POST or None)
	item = ItemWriteOffTemp.objects.get(id=pk)

	form.fields['code'].initial = item.product.code
	form.fields['item_name'].initial = item.product.item_name
	form.fields['available_quantity'].initial = item.product.quantity
	form.fields['quantity'].initial = item.quantity
	form.fields['reasons'].initial = item.reason.id
	form.fields['details'].initial = item.details
	form.fields['unit_cost_price'].initial = item.cost_price

	if request.method =='POST':

		reason_id=request.POST.get('reasons')
		reason=ItemWriteOffReasons.objects.get(id=reason_id)
		available_quantity=item.product.quantity
		cost_price=request.POST.get('unit_cost_price')
		details=request.POST.get('details')
		quantity=request.POST.get('quantity')
		total_cost = float(quantity)* float(cost_price)

		item.details=details
		item.reason=reason
		item.quantity=quantity
		item.cost_price=cost_price
		item.total_cost=total_cost
		item.processed_by=processed_by
		item.save()
		item.product.unit_cost_price=cost_price
		item.product.save()
		return HttpResponseRedirect(reverse('Item_Write_off_manage'))
	context={
	'task_array':task_array,
	'form':form,
	}
	return render(request,'shop_templates/Item_Write_off_manage_Preview.html',context)


def Item_Write_off_manage_delete(request,pk):
	ItemWriteOffTemp.objects.filter(id=pk).delete()
	return HttpResponseRedirect(reverse("Item_Write_off_manage"))


def Item_Write_off_Approval(request):
	task_array=[]
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	for task in tasks:
		task_array.append(task.task.title)

	status='UNTREATED'
	approval_status='PENDING'
	records =ItemWriteOffTemp.objects.filter(approval_status=approval_status,status=status)

	context={
	'task_array':task_array,
	'records':records,

	}
	return render(request,'shop_templates/Item_Write_off_Approval.html',context)


def Item_Write_off_Approval_Preview(request,pk):
	task_array=[]
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	for task in tasks:
		task_array.append(task.task.title)

	form = Item_Write_off_Approval_form(request.POST or None)
	item = ItemWriteOffTemp.objects.get(id=pk)

	form.fields['code'].initial = item.product.code
	form.fields['item_name'].initial = item.product.item_name
	form.fields['quantity'].initial = item.quantity
	form.fields['reasons'].initial = item.reason.title
	form.fields['details'].initial = item.details



	if request.method =='POST':
		item.approval_status="APPROVED"
		item.save()
		return HttpResponseRedirect(reverse('Item_Write_off_Approval'))
	context={
	'task_array':task_array,
	'form':form,
	}
	return render(request,'shop_templates/Item_Write_off_Approval_Preview.html',context)



def Item_Write_off_Approved_List(request):
	task_array=[]
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	for task in tasks:
		task_array.append(task.task.title)

	status='UNTREATED'
	approval_status='APPROVED'
	records =ItemWriteOffTemp.objects.filter(approval_status=approval_status,status=status)
	print("")
	context={
	'task_array':task_array,
	'records':records,

	}
	return render(request,'shop_templates/Item_Write_off_Approved_List.html',context)


def Item_Write_off_Approved_Process(request,pk):
	task_array=[]
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	for task in tasks:
		task_array.append(task.task.title)
	
	processed_by=CustomUser.objects.get(id=request.user.id)
	processed_by=processed_by.username

	form = Item_Write_off_Approval_form(request.POST or None)
	item = ItemWriteOffTemp.objects.get(id=pk)

	form.fields['code'].initial = item.product.code
	form.fields['item_name'].initial = item.product.item_name
	form.fields['quantity'].initial = item.quantity
	form.fields['reasons'].initial = item.reason.title
	form.fields['details'].initial = item.details



	if request.method =='POST':
		tdate=get_current_date(now)

		record=ItemWriteOff(tdate=tdate,product=item,processed_by=processed_by,status="UNTREATED")
		record.save()

		if item.route == 'MAIN':
			stock=Stock.objects.get(id=item.product_id)
			stock.quantity=int(stock.quantity)-int(item.quantity)
			stock.save()
		elif item.route == 'AUCTION':
			stock=Stock_Auction.objects.get(stock_id=item.product_id)
			stock.quantity=int(stock.quantity)-int(item.quantity)
			stock.save()

		item.status="TREATED"
		item.save()
		return HttpResponseRedirect(reverse('Item_Write_off_Approved_List'))
	context={
	'task_array':task_array,
	'form':form,
	}
	return render(request,'shop_templates/Item_Write_off_Approved_Process.html',context)



def Item_Write_off_Daily_Summary(request):
	task_array=[]
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	for task in tasks:
		task_array.append(task.task.title)

	tdate=get_current_date(now)
	form=TransactionPeriod_form(request.POST or None)
	processed_by=CustomUser.objects.get(id=request.user.id)
	processed_by=processed_by.username

	records=[]
	total_amount=0
	total_item=0
	if request.method == 'POST' and 'btn-fetch' in request.POST:
		period=request.POST.get("transaction_period")

		date_format = '%Y-%m-%d'
		dtObj = datetime.strptime(period, date_format)
		tdate=get_current_date(dtObj)


		records = ItemWriteOff.objects.filter(status='UNTREATED',tdate=tdate)
		queryset=ItemWriteOff.objects.filter(status='UNTREATED',tdate=tdate).aggregate(total_amount=Sum('product__total_cost'),total_items=Sum('product__quantity'))
		total_amount=queryset['total_amount']
		total_item=queryset['total_items']

	if request.method == 'POST' and 'btn-process' in request.POST:
		period=request.POST.get("transaction_period")

		date_format = '%Y-%m-%d'
		dtObj = datetime.strptime(period, date_format)
		tdate=get_current_date(dtObj)


		records = ItemWriteOff.objects.filter(status='UNTREATED',tdate=tdate)
		queryset=ItemWriteOff.objects.filter(status='UNTREATED',tdate=tdate).aggregate(total_amount=Sum('product__total_cost'),total_items=Sum('product__quantity'))
		total_amount=queryset['total_amount']
		total_item=queryset['total_items']

		Daily_Item_Write_Off_Summary(description='ITEM WRITE-OFF',
									quantity=total_item,
									amount=total_amount,
									processed_by=processed_by,
									status='UNTREATED',
									tdate=tdate).save()
		ItemWriteOff.objects.filter(status='UNTREATED',tdate=tdate).update(status='TREATED')
		return HttpResponseRedirect(reverse('Item_Write_off_Daily_Summary'))

	button_show=False
	if records:
		button_show=True

	form.fields['transaction_period'].initial=now
	context={
	'task_array':task_array,
	'records':records,
	'form':form,
	'total_amount':total_amount,
	'total_item':total_item,
	'button_show':button_show,
	}
	return render(request,'shop_templates/Item_Write_off_Daily_Summary.html',context)


def Item_Write_off_Day_End_Transactions(request):
	task_array=[]
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	for task in tasks:
		task_array.append(task.task.title)

	tdate=get_current_date(now)
	form=TransactionPeriod_form(request.POST or None)
	processed_by=CustomUser.objects.get(id=request.user.id)
	processed_by=processed_by.username

	records=[]
	total_amount=0
	total_item=0
	if request.method == 'POST' and 'btn-fetch' in request.POST:
		period=request.POST.get("transaction_period")

		date_format = '%Y-%m-%d'
		dtObj = datetime.strptime(period, date_format)
		tdate=get_current_date(dtObj)


		records = Daily_Item_Write_Off_Summary.objects.filter(status='UNTREATED',tdate=tdate)
		queryset=Daily_Item_Write_Off_Summary.objects.filter(status='UNTREATED',tdate=tdate).aggregate(total_amount=Sum('amount'),total_items=Sum('quantity'))
		total_amount=queryset['total_amount']
		total_item=queryset['total_items']

	if request.method == 'POST' and 'btn-process' in request.POST:
		period=request.POST.get("transaction_period")

		date_format = '%Y-%m-%d'
		dtObj = datetime.strptime(period, date_format)
		tdate=get_current_date(dtObj)


		records = Daily_Item_Write_Off_Summary.objects.filter(status='UNTREATED',tdate=tdate)
		queryset=Daily_Item_Write_Off_Summary.objects.filter(status='UNTREATED',tdate=tdate).aggregate(total_amount=Sum('amount'),total_items=Sum('quantity'))
		total_amount=queryset['total_amount']
		total_item=queryset['total_items']

		ticket=get_ticket()
		Item_Write_Off_Day_End_Transactions(quantity=total_item,
									amount=total_amount,
									cash_book=ticket,
									processed_by=processed_by,
									status='UNTREATED',
									tdate=tdate).save()

		cash_book_balance=shop_cashbook_balance()
		particulars="Items Write-off on " + str(tdate)
		debit=total_amount
		credit=0
		balance=float(cash_book_balance)-float(debit)
		ref_no=ticket
		source="ITEM WRITE-OFF"
		shop_cashbook_posting(particulars,debit,credit,balance,ref_no,'ACTIVE',tdate,processed_by,source)
		Daily_Item_Write_Off_Summary.objects.filter(status='UNTREATED',tdate=tdate).update(status='TREATED',cash_book=ticket)
		return HttpResponseRedirect(reverse('Item_Write_off_Day_End_Transactions'))

	button_show=False
	if records:
		button_show=True

	form.fields['transaction_period'].initial=now
	context={
	'task_array':task_array,
	'records':records,
	'form':form,
	'total_amount':total_amount,
	'total_item':total_item,
	'button_show':button_show,
	}
	return render(request,'shop_templates/Item_Write_off_Day_End_Transactions.html',context)


def Item_Write_off_Month_End_Transactions(request):
	task_array=[]
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	for task in tasks:
		task_array.append(task.task.title)

	tdate=get_current_date(now)
	form=TransactionPeriod_form(request.POST or None)
	processed_by=CustomUser.objects.get(id=request.user.id)
	processed_by=processed_by.username

	records=[]
	total_amount=0
	total_item=0
	if request.method == 'POST' and 'btn-fetch' in request.POST:
		period=request.POST.get("transaction_period")

		date_format = '%Y-%m-%d'
		dtObj = datetime.strptime(period, date_format)
		tdate=get_current_date(dtObj)


		records = Item_Write_Off_Day_End_Transactions.objects.filter(status='UNTREATED').filter(Q(tdate__year=tdate.year) & Q(tdate__month=tdate.month))
		queryset=Item_Write_Off_Day_End_Transactions.objects.filter(status='UNTREATED').filter(Q(tdate__year=tdate.year) & Q(tdate__month=tdate.month)).aggregate(total_amount=Sum('amount'),total_items=Sum('quantity'))
		total_amount=queryset['total_amount']
		total_item=queryset['total_items']


	if request.method == 'POST' and 'btn-process' in request.POST:
		period=request.POST.get("transaction_period")

		date_format = '%Y-%m-%d'
		dtObj = datetime.strptime(period, date_format)
		tdate=get_current_date(dtObj)


		records = Item_Write_Off_Day_End_Transactions.objects.filter(status='UNTREATED').filter(Q(tdate__year=tdate.year) & Q(tdate__month=tdate.month))
		queryset=Item_Write_Off_Day_End_Transactions.objects.filter(status='UNTREATED').filter(Q(tdate__year=tdate.year) & Q(tdate__month=tdate.month)).aggregate(total_amount=Sum('amount'),total_items=Sum('quantity'))
		total_amount=queryset['total_amount']
		total_item=queryset['total_items']

		ticket=get_ticket()
		Item_Write_Off_Month_End_Transactions(quantity=total_item,
									amount=total_amount,
									month_key=ticket,
									processed_by=processed_by,
									status='UNTREATED',
									tdate=tdate).save()

		Item_Write_Off_Day_End_Transactions.objects.filter(status='UNTREATED').filter(Q(tdate__year=tdate.year) & Q(tdate__month=tdate.month)).update(status='TREATED',month_key=ticket)
		return HttpResponseRedirect(reverse('Item_Write_off_Month_End_Transactions'))

	button_show=False
	if records:
		button_show=True

	form.fields['transaction_period'].initial=now
	context={
	'task_array':task_array,
	'records':records,
	'form':form,
	'total_amount':total_amount,
	'total_item':total_item,
	'button_show':button_show,
	}
	return render(request,'shop_templates/Item_Write_off_Month_End_Transactions.html',context)





def Item_Write_off_Year_End_Transactions(request):
	task_array=[]
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	for task in tasks:
		task_array.append(task.task.title)

	tdate=get_current_date(now)
	form=TransactionPeriod_form(request.POST or None)
	processed_by=CustomUser.objects.get(id=request.user.id)
	processed_by=processed_by.username

	records=[]
	total_amount=0
	total_item=0
	if request.method == 'POST' and 'btn-fetch' in request.POST:
		period=request.POST.get("transaction_period")

		date_format = '%Y-%m-%d'
		dtObj = datetime.strptime(period, date_format)
		tdate=get_current_date(dtObj)


		records = Item_Write_Off_Month_End_Transactions.objects.filter(status='UNTREATED').filter(Q(tdate__year=tdate.year))
		queryset=Item_Write_Off_Month_End_Transactions.objects.filter(status='UNTREATED').filter(Q(tdate__year=tdate.year)).aggregate(total_amount=Sum('amount'),total_items=Sum('quantity'))
		total_amount=queryset['total_amount']
		total_item=queryset['total_items']


	if request.method == 'POST' and 'btn-process' in request.POST:
		period=request.POST.get("transaction_period")

		date_format = '%Y-%m-%d'
		dtObj = datetime.strptime(period, date_format)
		tdate=get_current_date(dtObj)


		records = Item_Write_Off_Month_End_Transactions.objects.filter(status='UNTREATED').filter(Q(tdate__year=tdate.year))
		queryset=Item_Write_Off_Month_End_Transactions.objects.filter(status='UNTREATED').filter(Q(tdate__year=tdate.year)).aggregate(total_amount=Sum('amount'),total_items=Sum('quantity'))
		total_amount=queryset['total_amount']
		total_item=queryset['total_items']

		ticket=get_ticket()
		Item_Write_Off_Year_End_Transactions(quantity=total_item,
									amount=total_amount,
									year_key=ticket,
									processed_by=processed_by,
									status='UNTREATED',
									tdate=tdate).save()

		Item_Write_Off_Month_End_Transactions.objects.filter(status='UNTREATED').filter(Q(tdate__year=tdate.year)).update(status='TREATED',year_key=ticket)
		return HttpResponseRedirect(reverse('Item_Write_off_Year_End_Transactions'))

	button_show=False
	if records:
		button_show=True

	form.fields['transaction_period'].initial=now
	context={
	'task_array':task_array,
	'records':records,
	'form':form,
	'total_amount':total_amount,
	'total_item':total_item,
	'button_show':button_show,
	}
	return render(request,'shop_templates/Item_Write_off_Year_End_Transactions.html',context)






def Expiring_Date_Tracking_search(request):
	task_array=[]
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	for task in tasks:
		task_array.append(task.task.title)

	title="Search Stock"
	form = searchForm(request.POST or None)

	return render(request,'shop_templates/Expiring_Date_Tracking_search.html',{'form':form,'title':title,'task_array':task_array})


def Expiring_Date_Tracking_Product_Load(request):
	task_array=[]
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	for task in tasks:
		task_array.append(task.task.title)

	title="Product List"
	if request.method == "POST":
		form = searchForm(request.POST)
		if form['title'].value():
			stocks=Stock.objects.filter(Q(code__icontains=form['title'].value()) | Q(item_name__icontains=form['title'].value()))

			if stocks:
				context={
				'task_array':task_array,
				'stocks':stocks,
				'title':title,
				}
				return render(request,'shop_templates/Expiring_Date_Tracking_Product.html',context)
			else:
				messages.info(request,'Matching Records Not Found')
				return HttpResponseRedirect(reverse("Expiring_Date_Tracking_search"))
		else:
			messages.info(request,'Please Enter for Search')
			return HttpResponseRedirect(reverse("Expiring_Date_Tracking_search"))


def Expiring_Date_Tracking_Product_Preview(request,pk):
	task_array=[]
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	for task in tasks:
		task_array.append(task.task.title)

	form=stock_status_list_details_Form(request.POST or None)
	stock=Stock.objects.get(id=pk)

	if request.method == "POST":
		start_date=request.POST.get('start_date')

		date_format = '%Y-%m-%d'
		dtObj = datetime.strptime(start_date, date_format)
		expiring_date=get_current_date(dtObj)

		stock.expiring_date=expiring_date
		stock.save()
		return HttpResponseRedirect(reverse('Expiring_Date_Tracking_search'))

	form.fields['start_date'].initial=stock.expiring_date
	context={
	'task_array':task_array,
	'form':form,
	'stock':stock,

	}
	return render(request,'shop_templates/Expiring_Date_Tracking_Product_Preview.html',context)


def Expiring_Products_Tracking_Load(request):
	task_array=[]
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	for task in tasks:
		task_array.append(task.task.title)

	expiry_date_interval=0
	if ExpiringDateInterval.objects.all().exists():
		expiry_date_interval_id=ExpiringDateInterval.objects.first()
		expiry_date_interval=expiry_date_interval_id.title

	if not expiry_date_interval:
		# messages.error(request,'Missing Expiry Date Interval')
		return HttpResponseRedirect(reverse('shop_home'))
	stocks=Stock.objects.filter(Q(quantity__gt=0))
	stock_array=[]
	for stock in stocks:
		stock_array.append((stock.code,stock.item_name,stock.details,stock.quantity,stock.expiring_date))

	new_stocks=[]
	if stock_array:

		for item in stock_array:
			if pd.notnull(item[4]):
				current_date=get_current_date(now)
				expiring_date=get_current_date(item[4])
				date_difference_key=expiring_date-current_date

				if date_difference_key:
					date_difference=abs(int(str(date_difference_key)[0:-13]))

					if expiring_date != current_date:

						if abs(int(str(expiring_date-current_date)[0:-13])) <= int(expiry_date_interval):
							new_stocks.append((item[0],item[1],item[2],item[3],item[4],date_difference))

	context={
	'task_array':task_array,
	'stocks':stocks,
	'new_stocks':new_stocks,
	}
	return render(request,'shop_templates/Expiring_Products_Tracking_Load.html',context)


def Expiring_Products_Tracking_Auction_Product_select(request,pk):
	task_array=[]
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	for task in tasks:
		task_array.append(task.task.title)

	processed_by=CustomUser.objects.get(id=request.user.id)
	processed_by=processed_by.username

	form=Expired_Products_Main_Tracking_Write_Off_Form(request.POST or None)

	stock=Stock.objects.get(code=pk)

	if request.method== 'POST':

		date_format = '%Y-%m-%d'
		quantity=request.POST.get('expiry_quantity')
		unit_selling_price=request.POST.get('unit_selling_price')
		expiry_date_id=request.POST.get('expiry_date')

		dtObj = datetime.strptime(expiry_date_id, date_format)
		expiry_date=get_current_date(dtObj)

		if not quantity:
			messages.error(request,'Quantity Expiry is missing')
			return HttpResponseRedirect(reverse('Expiring_Products_Tracking_Auction_Product_select',args=(pk,)))

			if int(quantity)>=int(stock.quantity):
				messages.error(request,'Quantity selected cannot be more than the avaialable quantity')
				return HttpResponseRedirect(reverse('Expiring_Products_Tracking_Auction_Product_select',args=(pk,)))

		if Stock_Auction.objects.filter(stock=stock).exists():
			record_exist=Stock_Auction.objects.filter(stock=stock).first()
			if int(record_exist.quantity)>0:
				record_exist.quantity=int(record_exist.quantity)+int(quantity)
				record_exist.expiry_date2=stock.expiring_date
				record_exist.unit_selling_price=unit_selling_price
				record_exist.processed_by=processed_by
			else:
				record_exist.quantity=quantity
				record_exist.expiry_date=stock.expiring_date
				record_exist.expiry_date2=stock.expiring_date
				record_exist.unit_selling_price=unit_selling_price
				record_exist.processed_by=processed_by
			record_exist.save()
		else:
			Stock_Auction(stock=stock,quantity=quantity,expiry_date=stock.expiring_date,expiry_date2=stock.expiring_date,unit_selling_price=unit_selling_price,processed_by=processed_by).save()


		stock.expiring_date=expiry_date
		stock.quantity=int(stock.quantity)-int(quantity)
		stock.save()
		return HttpResponseRedirect(reverse('Expiring_Products_Tracking_Load'))

	form.fields['available_quantity'].initial=stock.quantity
	form.fields['unit_selling_price'].initial=stock.unit_selling_price
	form.fields['expiry_date'].initial=get_current_date(now)
	context={
	'task_array':task_array,
	'stock':stock,
	'form':form,
	}
	return render(request,'shop_templates/Expiring_Products_Tracking_Auction_Product_select.html',context)


def Expired_Products_Main_Tracking_Load(request):
	task_array=[]
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	for task in tasks:
		task_array.append(task.task.title)

	current_date=get_current_date(now)

	expiry_date_interval=0
	if ExpiringDateInterval.objects.all().exists():
		expiry_date_interval_id=ExpiringDateInterval.objects.first()
		expiry_date_interval=expiry_date_interval_id.title

	if not expiry_date_interval:
		return HttpResponseRedirect(reverse('shop_home'))
	stocks=Stock.objects.filter(Q(quantity__gt=0))
	stock_array=[]
	for stock in stocks:
		stock_array.append((stock.code,stock.item_name,stock.details,stock.quantity,stock.expiring_date))

	new_stocks=[]
	if stock_array:
		for item in stock_array:
			if pd.notnull(item[4]):

				expiring_date=get_current_date(item[4])
				date_difference_key=expiring_date-current_date


				date_difference=date_difference_key

				if expiring_date <= current_date:
					new_stocks.append((item[0],item[1],item[2],item[3],item[4],str(date_difference)[0:-9]))

	context={
	'task_array':task_array,
	'stocks':stocks,
	'new_stocks':new_stocks,
	'current_date':current_date,
	}
	return render(request,'shop_templates/Expired_Products_Main_Tracking_Load.html',context)


def Expired_Products_Main_Tracking_Write_Off(request,pk):
	task_array=[]
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	for task in tasks:
		task_array.append(task.task.title)

	current_date=get_current_date(now)
	reason=ItemWriteOffReasons.objects.get(title='EXPIRED')
	approval_status='PENDING'
	processed_by=CustomUser.objects.get(id=request.user.id)
	processed_by=processed_by.username


	details="Sent through Expiring date module"
	status='UNTREATED'
	tdate=get_current_date(now)

	form=Expired_Products_Main_Tracking_Write_Off_Form(request.POST or None)

	stock=Stock.objects.get(code=pk)
	if request.method == 'POST':
		acceptance=request.POST.get('accept')

		if acceptance:
			new_expiry_date=request.POST.get('expiry_date')
			date_format = '%Y-%m-%d'
			new_expiry_date = datetime.strptime(new_expiry_date, date_format)
			# stop_date = datetime.strptime(stop_date, date_format)
			new_expiry_date=get_current_date(new_expiry_date)


		quantity=request.POST.get("expiry_quantity")
		unit_cost_price=request.POST.get("unit_cost_price")

		if not quantity or int(quantity)<0:
			messages.error(request,'Quantity is missing')
			return HttpResponseRedirect(reverse('Expired_Products_Main_Tracking_Write_Off',args=(pk,)))
		elif int(quantity)>int(stock.quantity):
			messages.error(request,'Expired Quantity cannot be more that Stock Quantity')
			return HttpResponseRedirect(reverse('Expired_Products_Main_Tracking_Write_Off',args=(pk,)))

		if not unit_cost_price or float(unit_cost_price)<=0:
			messages.error(request,'Cost price is missing')
			return HttpResponseRedirect(reverse('Expired_Products_Main_Tracking_Write_Off',args=(pk,)))
		else:
			if float(stock.unit_cost_price)>0:
				if float(unit_cost_price) != float(stock.unit_cost_price):
					messages.error(request,'Cost Price Variation')
					return HttpResponseRedirect(reverse('Expired_Products_Main_Tracking_Write_Off',args=(pk,)))
		if not ItemWriteOffReasons.objects.filter(title='EXPIRED').exists():
			messages.error(request,'Item Item Write-off Reason missing, consult the Administrator')
			return HttpResponseRedirect(reverse('Expired_Products_Main_Tracking_Write_Off',args=(pk,)))

		if ItemWriteOffTemp.objects.filter(product=stock,expiry_date=stock.expiring_date,approval_status=approval_status,status=status).exists():
			messages.error(request,'You still have incomplete transaction for this Product')
			return HttpResponseRedirect(reverse('Expired_Products_Main_Tracking_Write_Off',args=(pk,)))

		ItemWriteOffTemp(product=stock,
						reason=reason,
						quantity=quantity,
						cost_price=unit_cost_price,
						total_cost=float(unit_cost_price)*float(quantity),
						processed_by=processed_by,
						approval_status=approval_status,
						details=details,
						status=status,
						expiry_date=stock.expiring_date,
						tdate=tdate
						).save()
		if acceptance:
			stock.expiring_date=new_expiry_date
			stock.save()


		return HttpResponseRedirect(reverse('Expired_Products_Main_Tracking_Load'))

	form.fields['available_quantity'].initial=stock.quantity
	form.fields['unit_selling_price'].initial=stock.unit_selling_price

	if stock.unit_cost_price:
		form.fields['unit_cost_price'].initial=stock.unit_cost_price
	else:
		form.fields['unit_cost_price'].initial=stock.unit_selling_price

	form.fields['expiry_date'].initial=stock.expiring_date
	context={
	'task_array':task_array,
	'stock':stock,
	'form':form,
	'current_date':current_date,
	}
	return render(request,'shop_templates/Expired_Products_Main_Tracking_Write_Off.html',context)





def Expired_Products_Auction_Tracking_Load(request):
	task_array=[]
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	for task in tasks:
		task_array.append(task.task.title)

	current_date=get_current_date(now)

	stocks=Stock_Auction.objects.filter(Q(quantity__gt=0))
	stock_array=[]
	for stock in stocks:
		stock_array.append((stock.stock.code,stock.stock.item_name,stock.stock.details,stock.quantity,stock.expiry_date,stock.id))

	new_stocks=[]
	if stock_array:
		for item in stock_array:
			if pd.notnull(item[4]):

				expiring_date=get_current_date(item[4])
				date_difference_key=expiring_date-current_date


				date_difference=date_difference_key

				if expiring_date <= current_date:
					new_stocks.append((item[0],item[1],item[2],item[3],item[4],str(date_difference)[0:-9],item[5]))

	context={
	'task_array':task_array,
	'stocks':stocks,
	'new_stocks':new_stocks,
	'current_date':current_date,
	}
	return render(request,'shop_templates/Expired_Products_Auction_Tracking_Load.html',context)


def Expired_Products_Auction_Tracking_Write_Off(request,pk):
	task_array=[]
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	for task in tasks:
		task_array.append(task.task.title)

	current_date=get_current_date(now)
	reason=ItemWriteOffReasons.objects.get(title='EXPIRED')
	approval_status='PENDING'
	processed_by=CustomUser.objects.get(id=request.user.id)
	processed_by=processed_by.username

	details="Sent through Expiring date module"
	status='UNTREATED'
	tdate=get_current_date(now)

	form=Expired_Products_Auction_Tracking_Write_Off_Form(request.POST or None)

	stock=Stock_Auction.objects.get(id=pk)
	if request.method == 'POST':

		quantity=request.POST.get("available_quantity")
		unit_cost_price=stock.stock.unit_cost_price

		if not quantity or int(quantity)<0:
			messages.error(request,'Quantity is missing')
			return HttpResponseRedirect(reverse('Expired_Products_Auction_Tracking_Write_Off',args=(pk,)))
		elif int(quantity)>int(stock.quantity):
			messages.error(request,'Expired Quantity cannot be more that Stock Quantity')
			return HttpResponseRedirect(reverse('Expired_Products_Auction_Tracking_Write_Off',args=(pk,)))

		if not unit_cost_price or float(unit_cost_price)<=0:
			messages.error(request,'Cost price is missing')
			return HttpResponseRedirect(reverse('Expired_Products_Auction_Tracking_Write_Off',args=(pk,)))
		else:
			if float(stock.stock.unit_cost_price)>0:
				if float(unit_cost_price) != float(stock.stock.unit_cost_price):
					messages.error(request,'Cost Price Variation')
					return HttpResponseRedirect(reverse('Expired_Products_Auction_Tracking_Write_Off',args=(pk,)))
		if not ItemWriteOffReasons.objects.filter(title='EXPIRED').exists():
			messages.error(request,'Item Item Write-off Reason missing, consult the Administrator')
			return HttpResponseRedirect(reverse('Expired_Products_Auction_Tracking_Write_Off',args=(pk,)))

		if ItemWriteOffTemp.objects.filter(product=stock.stock,expiry_date=stock.expiry_date,approval_status=approval_status,status=status).exists():
			messages.error(request,'You still have incomplete transaction for this Product')
			return HttpResponseRedirect(reverse('Expired_Products_Auction_Tracking_Write_Off',args=(pk,)))

		ItemWriteOffTemp(product=stock.stock,
						reason=reason,
						quantity=quantity,
						cost_price=unit_cost_price,
						total_cost=float(unit_cost_price)*float(quantity),
						processed_by=processed_by,
						approval_status=approval_status,
						details=details,
						status=status,
						expiry_date=stock.expiry_date,
						route="AUCTION",
						transaction_key=stock.id,
						tdate=tdate
						).save()
		return HttpResponseRedirect(reverse('Expired_Products_Auction_Tracking_Load'))

	form.fields['available_quantity'].initial=stock.quantity
	form.fields['unit_selling_price'].initial=stock.unit_selling_price

	if stock.stock.unit_cost_price:
		form.fields['unit_cost_price'].initial=stock.stock.unit_cost_price
	else:
		form.fields['unit_cost_price'].initial=stock.unit_selling_price

	form.fields['expiry_date'].initial=stock.expiry_date


	context={
	'task_array':task_array,
	'stock':stock,
	'pk':pk,
	'form':form,
	'current_date':current_date,
	}
	return render(request,'shop_templates/Expired_Products_Auction_Tracking_Write_Off.html',context)



def Members_Credit_sales_ledger_search(request):
	task_array=[]
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	for task in tasks:
		task_array.append(task.task.title)

	title="Search Members"
	form = searchForm(request.POST or None)

	return render(request,'shop_templates/Members_Credit_sales_ledger_search.html',{'form':form,'title':title,'task_array':task_array})



def Members_Credit_sales_ledger_list_load(request):
	task_array=[]
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	for task in tasks:
		task_array.append(task.task.title)

	title="Membership Purchases"
	if request.method == "POST":
		form = searchForm(request.POST)
		status ='ACTIVE'

		members=searchMembers(form['title'].value(),status)

		context={
	'task_array':task_array,

			'members':members,
			'title':title,
		}
		return render(request,'shop_templates/Members_Credit_sales_ledger.html',context)


def Members_Credit_sales_ledger_preview(request,pk):
	task_array=[]
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	for task in tasks:
		task_array.append(task.task.title)

	form=Members_Credit_sales_ledger_form(request.POST or None)
	member = Members.objects.get(id=pk)
	form.fields['start_date'].initial = now
	form.fields['stop_date'].initial = now


	items=[]


	if request.method =="POST" and 'btn_submit' in request.POST:
		start_date = request.POST.get("start_date")
		stop_date = request.POST.get("stop_date")


		date_format = '%Y-%m-%d'
		tdate1 = datetime.strptime(start_date, date_format)

		tdate2 = datetime.strptime(stop_date, date_format)
		account_number=str(600)+ str(member.get_member_Id)
		items = coopshopledger(account_number,tdate1,tdate2)

	if request.method =="POST" and 'btn_print' in request.POST:
		return HttpResponse("Printing")

	context={
	'task_array':task_array,
	'form':form,
	'items':items,
	}
	return render(request,'shop_templates/Members_Credit_sales_ledger_preview.html',context)



def Members_Credit_sales_ledger_details(request,pk):
	task_array=[]
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	for task in tasks:
		task_array.append(task.task.title)

	date_selected=CooperativeShopLedger.objects.get(receipt=pk)
	records=Daily_Sales.objects.filter(receipt=pk)


	context={
	'task_array':task_array,
	'records':records,
	'date_selected':date_selected,
	}
	return render(request,'shop_templates/Members_Credit_sales_ledger_details.html',context)

def Members_Credit_sales_list_search(request):
	task_array=[]
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	for task in tasks:
		task_array.append(task.task.title)

	title="Search Members for Shopping"
	form = searchForm(request.POST or None)

	return render(request,'shop_templates/Members_Credit_sales_list_search.html',{'form':form,'title':title,'task_array':task_array})


def Members_Credit_sales_list_load(request):
	task_array=[]
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	for task in tasks:
		task_array.append(task.task.title)

	title="Membership Purchases"
	if request.method == "POST":
		form = searchForm(request.POST)
		status="ACTIVE"
		if not form['title'].value():
			messages.info(request,'Not Matchimg Record Found')
			return HttpResponseRedirect(reverse('Members_Credit_sales_list_search'))

		members=searchMembers(form['title'].value(),status)

		context={
		'task_array':task_array,

		'members':members,
		'title':title,
		}
		return render(request,'shop_templates/Members_Credit_sales_list_load.html',context)


def Members_Credit_sales_item_select(request,pk):
	task_array=[]
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	for task in tasks:
		task_array.append(task.task.title)

	status='UNTREATED'
	processed_by=request.user.id
	processed_by=CustomUser.objects.get(id=processed_by)
	items=Stock.objects.filter(Q(quantity__gt=0))
	member=Members.objects.get(id=pk)

	Members_Credit_Sales_Selected.objects.filter(~Q(member=member)).filter(status=status,processed_by=processed_by).delete()



	status="UNTREATED"

	total_item=""
	total_amount=""
	ticket_holder=0
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
	'task_array':task_array,
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
	task_array=[]
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	for task in tasks:
		task_array.append(task.task.title)

	form=members_credit_issue_item_form(request.POST or None)
	member=Members.objects.get(id=member_id)
	approval_status='PENDING'
	status = 'UNTREATED'

	if members_credit_sales_summary.objects.filter(trans_code__member=member,approval_status=approval_status,status=status).exists():
		messages.info(request,"You still have incomplete transaction, please discard or complete the existing transaction")
		return HttpResponseRedirect(reverse('Members_Credit_sales_item_select', args=(member_id,)))



	product = Stock.objects.get(id=pk)

	form.fields['code'].initial=product.code
	form.fields['item_name'].initial=product.item_name
	form.fields['details'].initial=product.details
	form.fields['available_quantity'].initial=product.quantity
	form.fields['unit_selling_price'].initial=product.unit_selling_price

	if request.method=="POST":
		tdate =  get_current_date(now)

		status="UNTREATED"
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
		processed_by=processed_by.username

		if Members_Credit_Sales_Selected.objects.filter(member=member,status=status,processed_by=processed_by):
			ticket_id=Members_Credit_Sales_Selected.objects.filter(member=member,status=status).first()
			selected_ticket=ticket_id.ticket
		else:
			# _ticket=GeneralTicket.objects.first()
			# selected_ticket=_ticket.ticket
			selected_ticket=get_ticket()


			# _ticket.ticket = int(_ticket.ticket) + 1
			# _ticket.save()

			# selected_ticket=str(now.year) +  str(now.month) +  str(now.day) + str(now.hour) +  str(now.minute) + str(now.second)


		if Members_Credit_Sales_Selected.objects.filter(sources='MAIN',member=member,product=product,status=status,processed_by=processed_by):
			record_exist=Members_Credit_Sales_Selected.objects.filter(sources='MAIN',member=member,product=product,status=status).first()
			record_exist.quantity=quantity
			record_exist.unit_selling_price=unit_selling_price
			record_exist.total=total
			record_exist.save()
			return HttpResponseRedirect(reverse('Members_Credit_sales_item_select',args=(member_id,)))

		record=Members_Credit_Sales_Selected(sources='MAIN',tdate=tdate,member=member,status=status,product=product,ticket=selected_ticket,quantity=quantity,unit_selling_price=unit_selling_price,total=total,processed_by=processed_by)
		record.save()
		return HttpResponseRedirect(reverse('Members_Credit_sales_item_select',args=(member_id,)))



	context={
	'task_array':task_array,
	'form':form,
	'member':member,
	}
	return render(request,'shop_templates/members_credit_issue_item.html',context)




def members_credit_issue_auction_item(request,pk,member_id):
	task_array=[]
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	for task in tasks:
		task_array.append(task.task.title)

	form=members_credit_issue_item_form(request.POST or None)
	member=Members.objects.get(id=member_id)
	approval_status='PENDING'
	status = 'UNTREATED'

	if members_credit_sales_summary.objects.filter(trans_code__member=member,approval_status=approval_status,status=status).exists():
		messages.info(request,"You still have incomplete transaction, please discard or complete the existing transaction")
		return HttpResponseRedirect(reverse('Members_Credit_sales_item_select', args=(member_id,)))


	if not Stock_Auction.objects.filter(Q(quantity__gt=0) & Q(stock__code=pk)).exists():
		messages.info(request,"No record found")
		return HttpResponseRedirect(reverse('Members_Credit_sales_item_select',args=(member_id,)))

	product = Stock_Auction.objects.get(stock__code=pk)

	form.fields['code'].initial=product.stock.code
	form.fields['item_name'].initial=product.stock.item_name
	form.fields['details'].initial=product.stock.details
	form.fields['available_quantity'].initial=product.quantity
	form.fields['unit_selling_price'].initial=product.unit_selling_price

	if request.method=="POST":
		tdate =  get_current_date(now)

		status="UNTREATED"
		quantity=request.POST.get('issue_quantity')
		if int(quantity)<=0:
			messages.error(request,"Quantity Selected cannot be Zero (0)")
			return HttpResponseRedirect(reverse('members_credit_issue_auction_item', args=(pk,member_id)))

		if int(quantity)>int(product.quantity):
			messages.error(request,"Quantity Selected is more that Available Quantity")
			return HttpResponseRedirect(reverse('members_credit_issue_auction_item', args=(pk,member_id)))


		unit_selling_price=product.unit_selling_price

		total=float(quantity) * float(unit_selling_price)
		processed_by=CustomUser.objects.get(id=request.user.id)
		processed_by=processed_by.username

		if Members_Credit_Sales_Selected.objects.filter(member=member,status=status,processed_by=processed_by):
			ticket_id=Members_Credit_Sales_Selected.objects.filter(member=member,status=status).first()
			selected_ticket=ticket_id.ticket
		else:
			_ticket=GeneralTicket.objects.first()
			selected_ticket=_ticket.ticket


			_ticket.ticket = int(_ticket.ticket) + 1
			_ticket.save()

		if Members_Credit_Sales_Selected.objects.filter(sources='AUCTION',member=member,product=product.stock,status=status,processed_by=processed_by):
			record_exist=Members_Credit_Sales_Selected.objects.filter(sources='AUCTION',member=member,product=product.stock,status=status).first()
			record_exist.quantity=quantity
			record_exist.unit_selling_price=unit_selling_price
			record_exist.total=total
			record_exist.save()
			return HttpResponseRedirect(reverse('Members_Credit_sales_item_select',args=(member_id,)))

		record=Members_Credit_Sales_Selected(sources='AUCTION',tdate=tdate,member=member,status=status,product=product.stock,ticket=selected_ticket,quantity=quantity,unit_selling_price=unit_selling_price,total=total,processed_by=processed_by)
		record.save()
		return HttpResponseRedirect(reverse('Members_Credit_sales_item_select',args=(member_id,)))



	context={
	'task_array':task_array,
	'form':form,
	'member':member,
	}
	return render(request,'shop_templates/members_credit_issue_auction_item.html',context)


def Members_Credit_sales_item_select_remove(request,pk,member_id):
	item = Members_Credit_Sales_Selected.objects.get(id=pk)
	item.delete()
	return HttpResponseRedirect(reverse('Members_Credit_sales_item_select',args=(member_id,)))


def members_credit_sales_item_select_preview(request,pk,ticket):
	task_array=[]
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	for task in tasks:
		task_array.append(task.task.title)

	form=Members_Credit_Sales_submit_form(request.POST or None)

	sales = Members_Credit_Sales_Selected.objects.filter(ticket=ticket)
	sum_sales=Members_Credit_Sales_Selected.objects.filter(ticket=ticket).aggregate(total_sales=Sum('total'))

	if sum_sales['total_sales']:
		sum_total=float(sum_sales['total_sales'])
	else:
		sum_total=0

	status='UNTREATED'
	processing_status='UNPROCESSED'

	member=Members.objects.get(id=pk)

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

	new_credit_sales = members_credit_sales_summary.objects.filter(trans_code__member=member,processing_status=processing_status)
	sum_new_credit_sales=members_credit_sales_summary.objects.filter(trans_code__member=member,processing_status=processing_status).aggregate(total_sales=Sum('amount'))

	if sum_new_credit_sales['total_sales']:
		credit_sales_total=float(sum_new_credit_sales['total_sales'])
	else:
		credit_sales_total=0


	amount = credit_sales_total + loan_repayment_debit + monthly_contribution_debit + abs(sum_total)

	# Posting to Summary Table

	if request.method=="POST":
		tdate =  get_current_date(now)

		trans_code = Members_Credit_Sales_Selected.objects.filter(ticket=ticket).first()

		status='UNTREATED'
		status1='TREATED'
		approval_status="PENDING"

		comment=request.POST.get('comment')
		payment_date=request.POST.get('payment_date')
		net_pay=request.POST.get('net_pay')

		if not net_pay or float(net_pay) <= 0:
			messages.info(request,'Net Pay is missing')
			return HttpResponseRedirect(reverse('members_credit_sales_item_select_preview',args=(pk,ticket,)))


		if members_credit_sales_summary.objects.filter(trans_code=trans_code).exists():
			credit_sales_summary_record=members_credit_sales_summary.objects.get(trans_code=trans_code)

			credit_sales_summary_record.approval_status=approval_status
			credit_sales_summary_record.comment=comment
			credit_sales_summary_record.amount=sum_total
			credit_sales_summary_record.amount_paid=0
			credit_sales_summary_record.balance=-float(sum_total)
			credit_sales_summary_record.trans_code=trans_code
			credit_sales_summary_record.status=status
			credit_sales_summary_record.payment_date=payment_date
			credit_sales_summary_record.net_pay=net_pay
			credit_sales_summary_record.save()
		else:
			credit_sales_summary_record=members_credit_sales_summary(net_pay=net_pay,payment_date=payment_date,tdate=tdate,approval_status=approval_status,comment=comment,amount=sum_total,amount_paid=0,balance=-float(sum_total),trans_code=trans_code,status=status)
			credit_sales_summary_record.save()

		particulars="Payment as at: " + str(payment_date)
		credit_sales_analysis_record=members_credit_sales_analysis(tdate=tdate,trans_code=trans_code,particulars=particulars,debit=0,credit=net_pay,status=status)
		credit_sales_analysis_record.save()


		for monthly_contribution in monthly_contributions:
			monthly_contribution_record=members_credit_sales_analysis(tdate=tdate,trans_code=trans_code,particulars=monthly_contribution.transaction.transaction.name,debit=monthly_contribution.amount,credit=0,status=status)
			monthly_contribution_record.save()

		for loan_repayment in loan_repayments:
			loan_repayment_record=members_credit_sales_analysis(tdate=tdate,trans_code=trans_code,particulars=loan_repayment.transaction.name,debit=loan_repayment.repayment,credit=0,status=status)
			loan_repayment_record.save()

		if credit_sales_total:
			new_credit_sale=members_credit_sales_analysis(tdate=tdate,trans_code=trans_code,particulars='COOPERATIVE SHOP',debit=credit_sales_total,credit=0,status=status)
			new_credit_sale.save()

		member.last_used_net_pay=net_pay
		member.save()

		source_update=Members_Credit_Sales_Selected.objects.filter(ticket=ticket).update(status=status1)
		return HttpResponseRedirect(reverse('shop_home'))

	# return HttpResponse(credit_sales_total)
	form.fields['comment'].initial="FOR YOUR APPROVAL"
	form.fields['payment_date'].initial=now
	form.fields['net_pay'].initial=member.last_used_net_pay
	context={
	'task_array':task_array,
	'member':member,
	'monthly_contributions':monthly_contributions,
	'loan_repayments':loan_repayments,
	'credit_sales_total':credit_sales_total,
	'amount':amount,
	'new_purchase':sum_total,
	'form':form,
	'ticket':ticket,
	'sales':sales,
	'sum_total':sum_total,
	}
	return render(request,'shop_templates/members_credit_sales_item_select_preview.html',context)


def members_credit_sales_summary_add(request,member_id,debit,credit,balance,ticket):
	if request.method=="POST":
		trans_code = Members_Credit_Sales_Selected.objects.filter(ticket=ticket).first()
		status='UNTREATED'
		approval_status="PENDING"
		member=Members.objects.get(id=member_id)

		officer_id=request.POST.get('approval_officers')
		officer=ApprovalOfficers.objects.get(id=officer_id)

		approval_comment=request.POST.get('comment')

		record=members_credit_sales_summary(member=member,approval_officer=officer,approval_status=approval_status,approval_comment=approval_comment,debit=debit,credit=credit,balance=balance,trans_code=trans_code,status=status)
		record.save()
		return HttpResponseRedirect(reverse('Members_Credit_sales_list_search'))


def members_credit_purchase_manage(request):
	task_array=[]
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	for task in tasks:
		task_array.append(task.task.title)

	status="UNTREATED"
	approval_status='PENDING'
	records=members_credit_sales_summary.objects.filter(status=status,approval_status=approval_status)


	context={
	'task_array':task_array,
	'records':records,

	}
	return render(request,'shop_templates/members_credit_purchase_manage.html',context)


def members_credit_sales_manage_preview(request,ticket):
	task_array=[]
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	for task in tasks:
		task_array.append(task.task.title)

	form=Members_Credit_Sales_submit_form(request.POST or None)
	records=members_credit_sales_analysis.objects.filter(trans_code__ticket=ticket)

	item=[]
	if members_credit_sales_summary.objects.filter(trans_code__ticket=ticket).exists:
		item=members_credit_sales_summary.objects.get(trans_code__ticket=ticket)

	if request.method=="POST":
		trans_code = Members_Credit_Sales_Selected.objects.filter(ticket=ticket).first()

		status='UNTREATED'
		status1='TREATED'
		approval_status="PENDING"

		net_pay=request.POST.get('net_pay')
		officer=CustomUser.objects.get(id=request.user.id).username
		processed_by=processed_by.username

		approval_comment=request.POST.get('comment')

		payment_date=request.POST.get('payment_date')
		date_format = '%Y-%m-%d'
		dtObj = datetime.strptime(payment_date, date_format)

		payment_date=get_current_date(dtObj)

		if not net_pay or float(net_pay)<=0:
			messages.info(request,'net_pay is Missing')
			return HttpResponseRedirect(reverse('members_credit_sales_manage_preview',args=(ticket,)))


		if members_credit_sales_summary.objects.filter(trans_code=trans_code).exists():
			record=members_credit_sales_summary.objects.get(trans_code=trans_code)
			record.approval_officer=officer
			record.approval_status=approval_status
			record.approval_comment=approval_comment
			record.payment_date=payment_date
			record.net_pay=net_pay
			record.save()
			return HttpResponseRedirect(reverse('members_credit_purchase_manage'))

	form.fields['comment'].initial=item.comment
	form.fields['net_pay'].initial=item.net_pay
	form.fields['payment_date'].initial=item.payment_date
	context={
	'task_array':task_array,
	'records':records,
	'form':form,
	'ticket':ticket,
	}
	return render(request,'shop_templates/members_credit_sales_manage_preview.html',context)


def members_credit_purchase_selection_reset_confirmation(request,ticket):
	task_array=[]
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	for task in tasks:
		task_array.append(task.task.title)

	context={
	'task_array':task_array,
	'ticket':ticket,

	}
	return render(request,'shop_templates/members_credit_purchase_selection_reset_confirmation.html',context)


def members_credit_purchase_selection_reset_update(request,ticket):
	status='UNTREATED'
	record=members_credit_sales_summary.objects.filter(trans_code__ticket=ticket)
	record.delete()
	record=members_credit_sales_analysis.objects.filter(trans_code__ticket=ticket)
	record.delete()
	records=Members_Credit_Sales_Selected.objects.filter(ticket=ticket).update(status=status)
	return_pk=Members_Credit_Sales_Selected.objects.filter(ticket=ticket).first()

	return HttpResponseRedirect(reverse('Members_Credit_sales_item_select',args=(return_pk.member_id,)))


def members_credit_purchase_selection_discard_confirmation(request,ticket):
	task_array=[]
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	for task in tasks:
		task_array.append(task.task.title)

	context={
	'task_array':task_array,
	'ticket':ticket,
	}
	return render(request,'shop_templates/members_credit_purchase_selection_discard_confirmation.html',context)


def members_credit_purchase_selection_discard_update(request,ticket):
	records=Members_Credit_Sales_Selected.objects.filter(ticket=ticket)
	records.delete()
	return HttpResponseRedirect(reverse('members_credit_purchase_manage'))

def members_credit_sales_approved_list(request):
	task_array=[]
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	for task in tasks:
		task_array.append(task.task.title)

	status="UNTREATED"
	approval_status='PENDING'
	approval_status1='APPROVED'
	items=members_credit_sales_summary.objects.filter(status=status).exclude(approval_status=approval_status)


	context={
	'task_array':task_array,
	'items':items,
	'approval_status1':approval_status1,

	}
	return render(request,'shop_templates/members_credit_sales_approved_list.html',context)


def members_credit_sales_approved_item_details(request,ticket):
	# current_user=Shop_Tasks_Models.objects.get(user=request.user.id)
	task_array=[]
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	for task in tasks:
		task_array.append(task.task.title)

	form=Shop_Issue_Receipt_form(request.POST or None)

	status="TREATED"
	status2="UNTREATED"

	items=Members_Credit_Sales_Selected.objects.filter(ticket=ticket)
	if not items:
		return HttpResponseRedirect(reverse('members_credit_sales_approved_list'))
	amount_due=0

	total=Members_Credit_Sales_Selected.objects.filter(ticket=ticket).aggregate(total_amount=Sum('total'))

	if float(total['total_amount']):
		amount_due=float(total['total_amount'])


	item=members_credit_sales_summary.objects.get(trans_code__ticket=ticket)
	transaction=TransactionTypes.objects.get(code=600)


	if request.method=="POST":

		tdate =  get_current_date(now)

		if MembersAccountsDomain.objects.filter(member=item.trans_code.member,transaction=transaction).exists():
			member=MembersAccountsDomain.objects.get(member=item.trans_code.member,transaction=transaction)
		else:
			messages.error(request,"This Transaction Has no Account Number")
			return HttpResponseRedirect(reverse('members_credit_sales_approved_item_details', args=(ticket,)))

		receipt_types=request.POST.get('receipt_types')


		if receipt_types=="MANUAL":
			# return HttpResponse("MANUAL")
			receipt_status='USED'
			receipt_id=request.POST.get('receipt_no')


			if Receipts_Shop.objects.filter(receipt=receipt_id,status=receipt_status).exists():
				messages.error(request,"This Receipt is Already in Use")
				return HttpResponseRedirect(reverse('members_credit_sales_approved_item_details',args=(ticket,)))

			receipt_id=Receipts_Shop.objects.get(receipt=receipt_id)
			receipt=receipt_id.receipt
			receipt_id.status=receipt_status
			receipt_id.save()

		elif receipt_types=="AUTO":
			# return HttpResponse("Auto")
			receipt_id=AutoReceipt.objects.first()
			receipt="AUT-" + str(receipt_id.receipt.zfill(5))
			receipt_id.receipt=int(receipt_id.receipt)+1
			receipt_id.save()


		else:
			# return HttpResponse("None")
			messages.error(request,'Invalid Receipt Type Selection')
			return HttpResponseRedirect(reverse('members_credit_sales_approved_item_details',args=(ticket,)))


		for item in items:
			if item.sources == "MAIN":
				product_update=Stock.objects.get(code=item.product.code)

				if int(item.quantity) > int(product_update.quantity):
					messages.error(request,"Insufficient Quantity for product with code " + str(item.product.code))
					return HttpResponseRedirect(reverse('members_credit_sales_approved_item_details',args=(ticket,)))

			elif item.sources=="AUCTION":
				product_update=Stock_Auction.objects.get(stock__code=item.product.code)

				if int(item.quantity) > int(product_update.quantity):
					messages.error(request,"Insufficient Quantity for product with code " + str(item.product.code))
					return HttpResponseRedirect(reverse('members_credit_sales_approved_item_details',args=(ticket,)))


		processed_by=CustomUser.objects.get(id=request.user.id)
		processed_by=processed_by.username

		sales_category='CREDIT'

		for item in items:
			name = item.member.get_full_name
			if item.member.residential_address:
				address=item.member.residential_address
			else:
				address="FETHA II CTCS"
			phone_no=item.member.phone_number
			item_name=item.product.item_name.upper()
			item_code=item.product.code
			quantity=item.quantity
			unit_selling_price=item.unit_selling_price
			total=item.total




			record=Daily_Sales(sources=item.sources,sales_category=sales_category,tdate=tdate,receipt=receipt,name=name,phone_no=phone_no,address=address,product=item.product,ticket=item.ticket,quantity=quantity,unit_selling_price=unit_selling_price,total=total,processed_by=item.processed_by,status=status)
			record.save()

			if item.sources == "MAIN":
				product_update=Stock.objects.get(code=item_code)
				product_update.quantity=int(product_update.quantity)-int(quantity)
				product_update.save()
			elif item.sources == "AUCTION":
				product_update=Stock_Auction.objects.get(stock__code=item_code)
				product_update.quantity=int(product_update.quantity)-int(quantity)
				product_update.save()

		selected=Daily_Sales.objects.filter(ticket=ticket).first()


		record=Daily_Sales_Summary(tdate=tdate,receipt=receipt,sale=selected,amount=amount_due,status=status,processed_by=processed_by)
		record.save()


		particulars="Purchases with receipt No " + str(receipt)
		balance_amount= -float(amount_due)
		debit_amount = amount_due



		if CooperativeShopLedger.objects.filter(member=member.member).exists():
			ledger_balance = CooperativeShopLedger.objects.filter(member=member.member).order_by('id').last()

			balance_amount=float(ledger_balance.balance) - float(amount_due)


		record=CooperativeShopLedger(account_number=str(600) + str(member.member.get_member_Id),status=status2,tdate=tdate,receipt=receipt,member=member.member,particulars=particulars,debit=debit_amount,credit=0,balance=balance_amount,processed_by=processed_by)
		record.save()


		item=members_credit_sales_summary.objects.get(trans_code__ticket=ticket)
		item.status=status
		item.save()

		return HttpResponseRedirect(reverse('general_cash_issue_item_print_receipt',args=(ticket,)))

	form.fields["receipt_types"].initial="AUTO"
	context={
	'task_array':task_array,
	'form':form,
	'items':items,
	'full_name':items[0].member.get_full_name,
	'amount_due':amount_due,

	'transaction':transaction,
	}
	return render(request,'shop_templates/members_credit_sales_approved_item_details.html',context)


def members_credit_sales_debt_recovery_cash_payment_search(request):
	task_array=[]
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	for task in tasks:
		task_array.append(task.task.title)

	title="Search Members for Cash Sales"
	form = searchForm(request.POST or None)

	return render(request,'shop_templates/members_credit_sales_debt_recovery_cash_payment_search.html',{'form':form,'title':title,'task_array':task_array})


def members_credit_sales_debt_recovery_cash_payment_list_load(request):
	task_array=[]
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	for task in tasks:
		task_array.append(task.task.title)

	title="Membership Purchases"
	if request.method == "POST":
		form = searchForm(request.POST)

		if not form['title'].value():
			messages.info(request,'No Matching Record Found')
			return HttpResponseRedirect(reverse('members_cash_sales_search'))

		status="ACTIVE"

		members=searchMembers(form['title'].value(),status)


	context={
	'task_array':task_array,
	'members':members,
	'title':title,
	}
	return render(request,'shop_templates/members_credit_sales_debt_recovery_cash_payment_list_load.html',context)

def members_credit_sales_debt_recovery_cash_payment_levels(request,pk):
	task_array=[]
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	for task in tasks:
		task_array.append(task.task.title)

	member=Members.objects.get(id=pk)


	context={
	'task_array':task_array,
	'member':member,
	}
	return render(request,'shop_templates/members_credit_sales_debt_recovery_cash_payment_levels.html',context)


def members_credit_sales_debt_recovery_cash_payment_current_day(request,pk):
	task_array=[]
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	for task in tasks:
		task_array.append(task.task.title)
	processing_status='UNPROCESSED'
	transaction_status='UNTREATED'
	tdate=get_current_date(now)
	processed_by=CustomUser.objects.get(id=request.user.id)
	processed_by=processed_by.username

	form=members_credit_sales_debt_recovery_cash_payment_current_day_form(request.POST or None)
	autoFormPrint=FormAutoPrints.objects.get(title='SHOP SALES')

	member=Members.objects.get(id=pk)
	record=[]
	amount_paid=0
	amount_due=0
	if members_credit_sales_summary.objects.filter(Q(balance__lt=0) & Q(trans_code__member=member,processing_status=processing_status)).exists():
		record=members_credit_sales_summary.objects.get(Q(balance__lt=0) & Q(trans_code__member=member,processing_status=processing_status))
		amount_due=abs(record.balance)

	if request.method == 'POST':
		receipt_types_id=request.POST.get('receipt_type')
		receipt_types=ReceiptTypes.objects.get(id=receipt_types_id)

		amount_paid=request.POST.get('amount_paid')

		if receipt_types=="MANUAL":
			receipt_status='USED'
			try:
				receipt_id=request.POST.get('receipt_no')
			except:
				messages.info(request,'Invalid receipt no')
				return HttpResponseRedirect(reverse('members_credit_sales_debt_recovery_cash_payment_current_day',args=(pk,)))

			if receipt_id and int(receipt_id) != 0:
				if Receipts_Shop.objects.filter(receipt=receipt_id).exists():

					if Receipts_Shop.objects.filter(receipt=receipt_id,status=receipt_status).exists():
						messages.info(request,"This Receipt is Already in Use")
						return HttpResponseRedirect(reverse('members_credit_sales_debt_recovery_cash_payment_current_day',args=(pk,)))


					receipt_id=Receipts_Shop.objects.get(receipt=receipt_id)
					receipt=receipt_id.receipt
					receipt_id.status=receipt_status
					receipt_id.save()
				else:
					messages.info(request,"This Receipt not do not exist")
					return HttpResponseRedirect(reverse('members_credit_sales_debt_recovery_cash_payment_current_day',args=(pk,)))

			else:
				messages.info(request,'Invalid receipt no')
				return HttpResponseRedirect(reverse('members_credit_sales_debt_recovery_cash_payment_current_day',args=(pk,)))


		elif receipt_types=="AUTO":
			receipt_id=AutoReceipt.objects.first()
			receipt="AUT-" + str(receipt_id.receipt.zfill(5))
			receipt_id.receipt=int(receipt_id.receipt)+1
			receipt_id.save()
		else:
			messages.info(request,'Invalid Receipt Type Selection')
			return HttpResponseRedirect(reverse('members_credit_sales_approved_item_details',args=(ticket,)))

		if  float(amount_paid) > float(amount_due):
			ledger_balance=get_cooperative_shop_balance(str("600") + str(member.get_member_Id))

			particulars="Cash payment for purchases with receipt no " + str(record.trans_code.ticket)
			debit=0
			credit=amount_due
			balance=float(ledger_balance) + float(amount_due)
			cooperative_shop_ledger_posting(str("600") + str(member.get_member_Id),transaction_status,member,particulars,debit,credit,balance,tdate,processed_by)

			record.amount_paid=float(record.amount_paid)+float(amount_due)
			record.balance=float(record.balance)+float(amount_due)
			record.save()

			description="Cash payment return for purcahse with receipt no: " + str(record.trans_code.ticket)
			members_credit_loans_Cash_Receipt(member=member,description=description,amount=amount_paid,receipt=receipt,status=transaction_status,processed_by=processed_by,tdate=tdate).save()


			ledger_balance=get_cooperative_shop_balance(str("500") + str(member.get_member_Id))

			particulars="Outstanding balance for cash payment for purchases with receipt no " + str(record.trans_code.ticket)
			debit=0
			credit=float(amount_paid)-float(amount_due)
			balance=float(ledger_balance) + float(credit)

			cooperative_shop_ledger_posting(str("500") + str(member.get_member_Id),transaction_status,member,particulars,debit,credit,balance,tdate,processed_by)
			return HttpResponseRedirect(reverse('members_credit_sales_debt_recovery_cash_payment_levels',args=(member.pk,)))

		else:
			ledger_balance=get_cooperative_shop_balance(str("600") + str(member.get_member_Id))

			particulars="Cash payment for purchases with receipt no " + str(record.trans_code.ticket)
			debit=0
			credit=amount_paid
			balance=float(ledger_balance) + float(amount_paid)
			cooperative_shop_ledger_posting(str("600") + str(member.get_member_Id),transaction_status,member,particulars,debit,credit,balance,tdate,processed_by)

			record.amount_paid=float(record.amount_paid)+float(amount_paid)
			record.balance=float(record.balance)+float(amount_paid)
			record.save()

			description="Cash payment return for purcahse with receipt no: " + str(record.trans_code.ticket)
			members_credit_loans_Cash_Receipt(member=member,description=description,amount=amount_paid,receipt=receipt,status=transaction_status,processed_by=processed_by,tdate=tdate).save()
			return HttpResponseRedirect(reverse('members_credit_sales_debt_recovery_cash_payment_levels',args=(member.pk,)))


	button_show=False
	if record:
		form.fields['amount_due'].initial=abs(record.balance)
		button_show=True

	context={
	'task_array':task_array,
	'member':member,
	'record':record,
	'form':form,
	'button_show':button_show,
	}
	return render(request,'shop_templates/members_credit_sales_debt_recovery_cash_payment_current_day.html',context)


def members_credit_sales_debt_recovery_cash_payment_daily_summary_list_load(request):
	task_array=[]
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	for task in tasks:
		task_array.append(task.task.title)

	form=Product_Purchase_Day_End_Transaction_form(request.POST or None)
	status='UNTREATED'
	status2='TREATED'
	status1='ACTIVE'
	tdate=get_current_date(now)
	processed_by=CustomUser.objects.get(id=request.user.id)
	processed_by=processed_by.username

	records=[]
	total_amount=0
	if request.method == 'POST' and 'btn-fetch' in request.POST:
		period=request.POST.get('period')

		date_format = '%Y-%m-%d'
		dtObj = datetime.strptime(period, date_format)
		current_date=get_current_date(dtObj)


		records=members_credit_loans_Cash_Receipt.objects.filter(Q(tdate=current_date) & Q(status=status)).filter(processed_by=processed_by)
		queryset=members_credit_loans_Cash_Receipt.objects.filter(Q(tdate=current_date) & Q(status=status)).filter(processed_by=processed_by).aggregate(total_amount=Sum('amount'))
		total_amount=queryset['total_amount']



	if request.method == 'POST' and 'btn-process' in request.POST:
		period=request.POST.get('period')

		date_format = '%Y-%m-%d'
		dtObj = datetime.strptime(period, date_format)
		current_date=get_current_date(dtObj)


		# records=members_credit_loans_Cash_Receipt.objects.filter(Q(tdate=current_date) & Q(status=status))
		queryset=members_credit_loans_Cash_Receipt.objects.filter(Q(tdate=current_date) & Q(status=status)).filter(processed_by=processed_by).aggregate(total_amount=Sum('amount'))
		total_amount=queryset['total_amount']

		cash_book_balance=shop_cashbook_balance()
		reference=get_ticket()

		balance=float(cash_book_balance)+float(total_amount)

		shop_cashbook_posting('Cash Payment Return',total_amount,0,balance,'CASH-' + str(reference),status1,tdate,processed_by,'CASH PAYMENT')

		members_credit_loans_Cash_Receipt_Daily_Summary(amount=total_amount,tdate=tdate,processed_by=processed_by,cash_book='CASH-' + str(reference),status=status).save()

		members_credit_loans_Cash_Receipt.objects.filter(Q(tdate=current_date) & Q(status=status)).filter(processed_by=processed_by).update(status=status2)
		return HttpResponseRedirect(reverse('members_credit_sales_debt_recovery_cash_payment_daily_summary_list_load'))


	button_show=False
	if records:
		button_show=True

	form.fields['period'].initial=now
	context={
	'task_array':task_array,
	'records':records,
	'form':form,
	'button_show':button_show,
	'total_amount':total_amount,
	}
	return render(request,'shop_templates/members_credit_sales_debt_recovery_cash_payment_daily_summary_list_load.html',context)




def members_credit_sales_debt_recovery_cash_payment_Day_End_Transaction_list_load(request):
	task_array=[]
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	for task in tasks:
		task_array.append(task.task.title)

	form=Product_Purchase_Day_End_Transaction_form(request.POST or None)
	status='UNTREATED'
	status2='TREATED'
	status1='ACTIVE'
	tdate=get_current_date(now)
	processed_by=CustomUser.objects.get(id=request.user.id)
	processed_by=processed_by.username

	records=[]
	total_amount=0
	if request.method == 'POST' and 'btn-fetch' in request.POST:
		period=request.POST.get('period')

		date_format = '%Y-%m-%d'
		dtObj = datetime.strptime(period, date_format)
		current_date=get_current_date(dtObj)


		records=members_credit_loans_Cash_Receipt_Daily_Summary.objects.filter(Q(tdate=current_date) & Q(status=status))
		queryset=members_credit_loans_Cash_Receipt_Daily_Summary.objects.filter(Q(tdate=current_date) & Q(status=status)).aggregate(total_amount=Sum('amount'))
		total_amount=queryset['total_amount']



	if request.method == 'POST' and 'btn-process' in request.POST:
		period=request.POST.get('period')

		date_format = '%Y-%m-%d'
		dtObj = datetime.strptime(period, date_format)
		current_date=get_current_date(dtObj)


		# records=members_credit_loans_Cash_Receipt_Daily_Summary.objects.filter(Q(tdate=current_date) & Q(status=status))
		queryset=members_credit_loans_Cash_Receipt_Daily_Summary.objects.filter(Q(tdate=current_date) & Q(status=status)).aggregate(total_amount=Sum('amount'))
		total_amount=queryset['total_amount']


		reference=get_ticket()

		members_credit_loans_Cash_Receipt_Day_End_Transaction(amount=total_amount,tdate=tdate,processed_by=processed_by,day_end_code=reference,status=status).save()
		members_credit_loans_Cash_Receipt_Daily_Summary.objects.filter(Q(tdate=current_date) & Q(status=status)).update(status=status2,day_end_code=reference)
		return HttpResponseRedirect(reverse('members_credit_sales_debt_recovery_cash_payment_Day_End_Transaction_list_load'))


	button_show=False
	if records:
		button_show=True

	form.fields['period'].initial=now
	context={
	'task_array':task_array,
	'records':records,
	'form':form,
	'button_show':button_show,
	'total_amount':total_amount,
	}
	return render(request,'shop_templates/members_credit_sales_debt_recovery_cash_payment_Day_End_Transaction_list_load.html',context)



def members_credit_sales_debt_recovery_cash_payment_Month_End_Transaction_list_load(request):
	task_array=[]
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	for task in tasks:
		task_array.append(task.task.title)

	form=Product_Purchase_Day_End_Transaction_form(request.POST or None)
	status='UNTREATED'
	status2='TREATED'
	status1='ACTIVE'
	tdate=get_current_date(now)
	processed_by=CustomUser.objects.get(id=request.user.id)
	processed_by=processed_by.username

	records=[]
	total_amount=0
	if request.method == 'POST' and 'btn-fetch' in request.POST:
		period=request.POST.get('period')

		date_format = '%Y-%m-%d'
		dtObj = datetime.strptime(period, date_format)
		current_date=get_current_date(dtObj)


		records=members_credit_loans_Cash_Receipt_Day_End_Transaction.objects.filter(Q(tdate__month=current_date.month)  & Q(tdate__year=current_date.year) & Q(status=status))
		queryset=members_credit_loans_Cash_Receipt_Day_End_Transaction.objects.filter(Q(tdate__month=current_date.month)  & Q(tdate__year=current_date.year) & Q(status=status)).aggregate(total_amount=Sum('amount'))
		total_amount=queryset['total_amount']



	if request.method == 'POST' and 'btn-process' in request.POST:
		period=request.POST.get('period')

		date_format = '%Y-%m-%d'
		dtObj = datetime.strptime(period, date_format)
		current_date=get_current_date(dtObj)



		queryset=members_credit_loans_Cash_Receipt_Day_End_Transaction.objects.filter(Q(tdate__month=current_date.month)  & Q(tdate__year=current_date.year) & Q(status=status)).aggregate(total_amount=Sum('amount'))
		total_amount=queryset['total_amount']


		reference=get_ticket()

		members_credit_loans_Cash_Receipt_Month_End_Transaction(amount=total_amount,tdate=tdate,processed_by=processed_by,month_end_code=reference,status=status).save()
		members_credit_loans_Cash_Receipt_Day_End_Transaction.objects.filter(Q(tdate__month=current_date.month)  & Q(tdate__year=current_date.year) & Q(status=status)).update(status=status2,month_end_code=reference)
		return HttpResponseRedirect(reverse('members_credit_sales_debt_recovery_cash_payment_Month_End_Transaction_list_load'))


	button_show=False
	if records:
		button_show=True

	form.fields['period'].initial=now
	context={
	'task_array':task_array,
	'records':records,
	'form':form,
	'button_show':button_show,
	'total_amount':total_amount,
	}
	return render(request,'shop_templates/members_credit_sales_debt_recovery_cash_payment_Day_End_Transaction_list_load.html',context)




def members_credit_sales_debt_recovery_cash_payment_Year_End_Transaction_list_load(request):
	task_array=[]
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	for task in tasks:
		task_array.append(task.task.title)

	form=Product_Purchase_Day_End_Transaction_form(request.POST or None)
	status='UNTREATED'
	status2='TREATED'
	status1='ACTIVE'
	tdate=get_current_date(now)
	processed_by=CustomUser.objects.get(id=request.user.id)
	processed_by=processed_by.username

	records=[]
	total_amount=0
	if request.method == 'POST' and 'btn-fetch' in request.POST:
		period=request.POST.get('period')

		date_format = '%Y-%m-%d'
		dtObj = datetime.strptime(period, date_format)
		current_date=get_current_date(dtObj)


		records=members_credit_loans_Cash_Receipt_Month_End_Transaction.objects.filter(Q(tdate__year=current_date.year) & Q(status=status))
		queryset=members_credit_loans_Cash_Receipt_Month_End_Transaction.objects.filter(Q(tdate__year=current_date.year) & Q(status=status)).aggregate(total_amount=Sum('amount'))
		total_amount=queryset['total_amount']



	if request.method == 'POST' and 'btn-process' in request.POST:
		period=request.POST.get('period')

		date_format = '%Y-%m-%d'
		dtObj = datetime.strptime(period, date_format)
		current_date=get_current_date(dtObj)



		queryset=members_credit_loans_Cash_Receipt_Month_End_Transaction.objects.filter(Q(tdate__year=current_date.year) & Q(status=status)).aggregate(total_amount=Sum('amount'))
		total_amount=queryset['total_amount']


		reference=get_ticket()

		members_credit_loans_Cash_Receipt_Year_End_Transaction(amount=total_amount,tdate=tdate,processed_by=processed_by,year_end_code=reference,status=status).save()
		members_credit_loans_Cash_Receipt_Month_End_Transaction.objects.filter(Q(tdate__year=current_date.year) & Q(status=status)).update(status=status2,year_end_code=reference)
		return HttpResponseRedirect(reverse('members_credit_sales_debt_recovery_cash_payment_Year_End_Transaction_list_load'))


	button_show=False
	if records:
		button_show=True

	form.fields['period'].initial=now
	context={
	'task_array':task_array,
	'records':records,
	'form':form,
	'button_show':button_show,
	'total_amount':total_amount,
	}
	return render(request,'shop_templates/members_credit_sales_debt_recovery_cash_payment_Year_End_Transaction_list_load.html',context)


def members_credit_sales_debt_recovery_cash_payment_after_transaction_list_load(request,pk):
	task_array=[]
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	for task in tasks:
		task_array.append(task.task.title)


	tdate=get_current_date(now)
	processed_by=CustomUser.objects.get(id=request.user.id)
	processed_by=processed_by.username

	schedule_status='UNSCHEDULED'
	status='UNTREATED'
	status2='TREATED'
	status1='ACTIVE'

	form=members_credit_sales_debt_recovery_cash_payment_current_day_form(request.POST or None)
	member=Members.objects.get(id=pk)

	if request.method == 'POST' and 'submit' in request.POST:
		amount_paid=request.POST.get('amount_paid')
		transaction_id=request.POST.get('transaction')
		transaction=members_shop_credit_loans.objects.get(id=transaction_id)

		amount_due=abs(transaction.balance)

		if float(amount_paid) > float(amount_due):
			messages.info(request,'Invalid Payment Amounts Specification')
			return HttpResponseRedirect(reverse('members_credit_sales_debt_recovery_cash_payment_after_transaction_list_load',args=(pk,)))
		elif  float(amount_paid) <= float(amount_due):
			if members_credit_sales_debt_recovery_after_temp.objects.filter(loan_number=transaction.loan_number).exists():
				messages.info(request,'You still have incomplete transaction')
				return HttpResponseRedirect(reverse('members_credit_sales_debt_recovery_cash_payment_after_transaction_list_load',args=(pk,)))

			members_credit_sales_debt_recovery_after_temp(member=member,loan_number=transaction.loan_number,amount_due=abs(transaction.balance),amount_paid=amount_paid,processed_by=processed_by,tdate=tdate).save()
			return HttpResponseRedirect(reverse('members_credit_sales_debt_recovery_cash_payment_after_transaction_list_load',args=(pk,)))

	if request.method == 'POST' and 'btn-process' in request.POST:
		receipt_types_id=request.POST.get('receipt_type')
		receipt_types=ReceiptTypes.objects.get(id=receipt_types_id)

		data_records=members_credit_sales_debt_recovery_after_temp.objects.filter(member=member)

		queryset=members_credit_sales_debt_recovery_after_temp.objects.filter(member=member).aggregate(total_amount=Sum('amount_paid'))
		total_amount=queryset['total_amount']

		for item in data_records:
			record=members_shop_credit_loans.objects.get(loan_number=item.loan_number)
			record.amount_paid=float(record.amount_paid) + float(item.amount_paid)
			record.balance=float(record.balance)+float(item.amount_paid)
			record.save()

		reference=get_ticket()
		balance=shop_cashbook_balance()
		balance=float(balance)+float(total_amount)
		shop_cashbook_posting('Cash Payment Return',total_amount,0,balance,'CASH-' + str(reference),status1,tdate,processed_by,'CASH PAYMENT')


		if receipt_types=="MANUAL":
			receipt_status='USED'
			try:
				receipt_id=request.POST.get('receipt_no')
			except:
				messages.info(request,'Invalid receipt no')
				return HttpResponseRedirect(reverse('members_credit_sales_debt_recovery_cash_payment_after_transaction_list_load',args=(pk,)))

			if receipt_id and int(receipt_id) != 0:

				if Receipts_Shop.objects.filter(receipt=receipt_id).exists():

					if Receipts_Shop.objects.filter(receipt=receipt_id,status=receipt_status).exists():
						messages.info(request,"This Receipt is Already in Use")
						return HttpResponseRedirect(reverse('members_credit_sales_debt_recovery_cash_payment_after_transaction_list_load',args=(pk,)))


					receipt_id=Receipts_Shop.objects.get(receipt=receipt_id)
					receipt=receipt_id.receipt
					receipt_id.status=receipt_status
					receipt_id.save()
				else:

					messages.info(request,"This Receipt not do not exist")
					return HttpResponseRedirect(reverse('members_credit_sales_debt_recovery_cash_payment_after_transaction_list_load',args=(pk,)))

			else:
				messages.info(request,'Invalid receipt no')
				return HttpResponseRedirect(reverse('members_credit_sales_debt_recovery_cash_payment_after_transaction_list_load',args=(pk,)))


		elif receipt_types=="AUTO":
			receipt_id=AutoReceipt.objects.first()
			receipt="AUT-" + str(receipt_id.receipt.zfill(5))
			receipt_id.receipt=int(receipt_id.receipt)+1
			receipt_id.save()
		else:
			messages.info(request,'Invalid Receipt Type Selection')
			return HttpResponseRedirect(reverse('members_credit_sales_debt_recovery_cash_payment_after_transaction_list_load',args=(ticket,)))

		description="Cash payment return for purchase"
		members_credit_loans_Cash_Receipt(member=member,
										description=description,
										amount=total_amount,
										receipt=receipt,
										status=status,
										processed_by=processed_by,
										tdate=tdate
										).save()


		members_credit_sales_debt_recovery_after_temp.objects.filter(member=member).delete()
		return HttpResponseRedirect(reverse('members_credit_sales_debt_recovery_cash_payment_levels',args=(member.pk,)))

	records=members_shop_credit_loans.objects.filter(Q(balance__lt=0) & Q(member=member,schedule_status=schedule_status,status=status))

	items=members_credit_sales_debt_recovery_after_temp.objects.filter(member=member)
	queryset=members_credit_sales_debt_recovery_after_temp.objects.filter(member=member).aggregate(total_amount=Sum('amount_paid'))
	total_amount=queryset['total_amount']

	button_show=False
	if items:
		button_show=True

	button_enabled=False
	if records:
		button_enabled=True

	context={
	'button_show':button_show,
	'button_enabled':button_enabled,
	'task_array':task_array,
	'member':member,
	'records':records,
	'form':form,
	'items':items,
	'total_amount':total_amount,
	}
	return render(request,'shop_templates/members_credit_sales_debt_recovery_cash_payment_after_transaction_list_load.html',context)


def members_credit_sales_debt_recovery_cash_payment_after_transaction_delete(request,pk):
	record=members_credit_sales_debt_recovery_after_temp.objects.get(id=pk)
	return_pk=record.member_id
	record.delete()
	return HttpResponseRedirect(reverse('members_credit_sales_debt_recovery_cash_payment_after_transaction_list_load',args=(return_pk,)))



def members_cash_sales_manage_list_load(request):
	task_array=[]
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	for task in tasks:
		task_array.append(task.task.title)
	processed_by=CustomUser.objects.get(id=request.user.id)
	processed_by=processed_by.username

	status = 'UNTREATED'
	records = Members_Cash_Sales_Selected.objects.filter(status=status,processed_by=processed_by).order_by('ticket').values_list('member__member_id','member__admin__last_name','member__admin__first_name','member__middle_name','tdate','ticket','member_id').distinct()
	record_array=[]
	for record in records:
		record_array.append((record[0],record[1] + ' ' + record[2] +' ' +record[3],record[4],record[5],record[6]))

	context={
	'task_array':task_array,
	'record_array':record_array,
	}
	return render(request,'shop_templates/members_cash_sales_manage_list_load.html',context)


def members_cash_sales_manage_delete_single_record(request,pk):
	Members_Cash_Sales_Selected.objects.filter(ticket=pk).delete()
	Daily_Sales.objects.filter(ticket=pk).delete()
	return HttpResponseRedirect(reverse('members_cash_sales_manage_list_load'))


def members_cash_sales_search(request):
	task_array=[]
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	for task in tasks:
		task_array.append(task.task.title)

	title="Search Members for Cash Sales"
	form = searchForm(request.POST or None)

	return render(request,'shop_templates/members_cash_sales_search.html',{'form':form,'title':title,'task_array':task_array})


def members_cash_sales_list_load(request):
	task_array=[]
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	for task in tasks:
		task_array.append(task.task.title)

	title="Membership Purchases"
	if request.method == "POST":
		form = searchForm(request.POST)

		if not form['title'].value():
			messages.info(request,'No Matching Record Found')
			return HttpResponseRedirect(reverse('members_cash_sales_search'))

		status="ACTIVE"

		members=searchMembers(form['title'].value(),status)


	context={
	'task_array':task_array,
	'members':members,
	'title':title,
	}
	return render(request,'shop_templates/members_cash_sales_list_load.html',context)


def members_cash_sales_product_load(request,pk,ticket):
	task_array=[]
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	for task in tasks:
		task_array.append(task.task.title)

	form=Shop_Issue_Receipt_form(request.POST or None)
	items=Stock.objects.filter(Q(quantity__gt=0))

	status="UNTREATED"
	status1="TREATED"
	member=Members.objects.get(id=pk)


	select_items=[]
	total_item=0
	total_amount=0
	ticket_holder=0
	submission_status=[]
	if Members_Cash_Sales_Selected.objects.filter(ticket=ticket).exists():
		button_show=True
		select_items = Members_Cash_Sales_Selected.objects.filter(ticket=ticket)
		queryset=Members_Cash_Sales_Selected.objects.filter(ticket=select_items[0].ticket).aggregate(total_amount=Sum('total'),total_item=Sum('quantity'))
		total_item=queryset['total_item']
		total_amount=queryset['total_amount']

		submission_status=select_items[0].submission_status

	else:
		button_show=False

	processed_by=CustomUser.objects.get(id=request.user.id)
	processed_by=processed_by.username

	sales_category='CASH'


	if request.method=="POST" and 'btn-submit'in request.POST:
		tdate =  get_current_date(now)
		cash_only=request.POST.get('cash_only')
		pay_status=False
		if cash_only:
			pay_status=True

		if Daily_Sales_Summary.objects.filter(ticket=ticket).exists():

			receipt_id=Daily_Sales_Summary.objects.get(ticket=ticket)
			receipt=receipt_id.receipt
			if cash_only:
				receipt_id.pos=0
				receipt_id.transfer=0
				receipt_id.submission_status='NOT SUBMITTED'
				receipt_id.cash=receipt_id.amount
				receipt_id.save()
		else:

			receipt_types=request.POST.get('receipt_types')
			

			if receipt_types=="MANUAL":

				receipt_status='USED'
				receipt_id=request.POST.get('receipt_no')

				if Receipts_Shop.objects.filter(receipt=receipt_id,status=receipt_status).exists():
					messages.error(request,"This Receipt is Already in Use")
					return HttpResponseRedirect(reverse('members_cash_sales_product_load',args=(pk,ticket,)))

				receipt_id=Receipts_Shop.objects.get(receipt=receipt_id)
				receipt=receipt_id.receipt.zfill(5)
				receipt_id.status=receipt_status
				receipt_id.save()

			elif receipt_types=="AUTO":

				receipt_id=AutoReceipt.objects.first()
				receipt= 'AUT-' + str(receipt_id.receipt).zfill(5)
				receipt_id.receipt=int(receipt_id.receipt)+1
				receipt_id.save()


			else:
				messages.error(request,"Invalid Receipt Type")
				return HttpResponseRedirect(reverse('members_cash_sales_product_load', args=(pk,ticket,)))

			for item in select_items:

				if item.sources=='MAIN':
					product_update=Stock.objects.get(code=item.product.code)

					if int(item.quantity) > int(product_update.quantity):
						messages.error(request,"Insufficient Quantity for product with code(MAIN) " + str(item.product.code))
						return HttpResponseRedirect(reverse('members_cash_sales_product_load',args=(pk,ticket,)))
				elif item.sources == "AUCTION":
					product_update=Stock_Auction.objects.get(stock__code=item.product.code)
					if int(item.quantity) > int(product_update.quantity):
						messages.error(request,"Insufficient Quantity for product with code(AUCTION) " + str(item.product.code))
						return HttpResponseRedirect(reverse('members_cash_sales_product_load',args=(pk,ticket,)))

			grand_total=0
			for item in select_items:
				name = item.member.admin.first_name + " " + item.member.admin.last_name + " " + item.member.middle_name
				if item.member.residential_address:
					address=item.member.residential_address
				else:
					address="FETHAII CTCS"
				phone_no=item.member.phone_number
				# item_name=item.product.item_name.upper()
				item_code=item.product.code
				quantity=item.quantity
				unit_selling_price=item.unit_selling_price
				total=item.total

				grand_total=grand_total + float(item.total)

				record=Daily_Sales(sources=item.sources,sales_category=sales_category,tdate=tdate,receipt=receipt,name=name,phone_no=phone_no,address=address,product=item.product,ticket=item.ticket,quantity=quantity,unit_selling_price=unit_selling_price,total=total,processed_by=item.processed_by,status=status1)
				record.save()



			selected=Daily_Sales.objects.filter(ticket=ticket).first()

			record=Daily_Sales_Summary(processed_by=processed_by,ticket=ticket,tdate=tdate,receipt=receipt,sale=selected,pos=0,transfer=0,cash=grand_total,amount=grand_total,status=status1)
			record.save()



			Members_Cash_Sales_Selected.objects.filter(ticket=ticket).update(submission_status='SUBMITTED')
		return HttpResponseRedirect(reverse('members_cash_sales_processing',args=(receipt,pay_status,)))

	form.fields['receipt_types'].initial='AUTO'
	context={
	'task_array':task_array,
	
	'form':form,
	'items':items,
	'member':member,
	'select_items':select_items,
	'total_item':total_item,
	'total_amount':total_amount,
	'button_show':button_show,
	'ticket_holder':ticket,
	'submission_status':submission_status,
	}
	return render(request,'shop_templates/members_cash_sales_product_load.html',context)



def members_cash_sales_processing(request,pk,pay_status):
	task_array=[]
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	for task in tasks:
		task_array.append(task.task.title)


	form=Daily_Sales_Summar_Form(request.POST or None)
	receipt_print_form=Final_Members_Cash_Sales_Processing_form(request.POST or None)

	record=Daily_Sales_Summary.objects.get(receipt=pk)

	ticket=record.ticket

	if pay_status == 'True':
		button_show=True
	elif pay_status == 'False':
		button_show=False

		if record.submission_status=='SUBMITTED':
			button_show=True

		if request.method =='POST' and 'btn-add' in request.POST:
			channel=request.POST.get('channel')
			bank_id=request.POST.get('banks')
			bank=Banks.objects.get(id=bank_id)
			account_name=request.POST.get('account_name')
			other_details=request.POST.get('other_details')
			amount=request.POST.get('amount')
			coop_account_id=request.POST.get('coop_accounts')
			coop_account=CooperativeBankAccounts.objects.get(id=coop_account_id)

			if channel=='POS':
				if (float(record.transfer)+float(amount)) > float(record.amount):
					messages.error(request,'Invalid Amount Specification' + str(float(record.transfer)+float(amount)))
					return HttpResponseRedirect(reverse('members_cash_sales_processing',args=(pk,pay_status,)))

				record.pos=amount
				record.cash=float(record.amount)-(float(record.transfer)+float(amount))

			elif channel=='TRANSFER':
				if (float(record.pos)+float(amount)) > float(record.amount):
					messages.error(request,'Invalid Amount Specification ' + str(float(record.pos)+float(amount)))
					return HttpResponseRedirect(reverse('members_cash_sales_processing',args=(pk,pay_status,)))

				record.transfer=amount
				record.cash=float(record.amount)-(float(record.pos)+float(amount))

			record.source_bank=bank
			record.account_name=account_name
			record.other_details=other_details
			record.coop_account=coop_account
			record.submission_status="SUBMITTED"
			record.save()


			return HttpResponseRedirect(reverse('members_cash_sales_processing',args=(pk,pay_status,)))

	if request.method == 'POST' and 'btn-process' in request.POST:
		autoprint = request.POST.get('receipt_print')
		
		select_items = Members_Cash_Sales_Selected.objects.filter(ticket=ticket)

		grand_total=0
		for item in select_items:
			item_code=item.product.code
			quantity=item.quantity
			unit_selling_price=item.unit_selling_price


			if item.sources=='MAIN':
				product_update=Stock.objects.get(code=item_code)
				product_update.quantity=int(product_update.quantity)-int(quantity)
				product_update.save()
			elif item.sources == "AUCTION":
				product_update=Stock_Auction.objects.get(stock__code=item_code)
				product_update.quantity=int(product_update.quantity)-int(quantity)
				product_update.save()


		item = Members_Cash_Sales_Selected.objects.filter(ticket=ticket).delete()

		if autoprint == "NO":

			return HttpResponseRedirect(reverse('shop_home'))
		elif autoprint == 'YES':
			return HttpResponseRedirect(reverse('general_cash_issue_item_print_receipt',args=(ticket,)))



	context={
	'task_array':task_array,
	'form':form,
	'record':record,
	'pay_status':pay_status,
	'button_show':button_show,
	'receipt_print_form':receipt_print_form,
	}
	return render(request,'shop_templates/members_cash_sales_processing.html',context)


def members_cash_sales_item_issue(request,pk,member_id):
	task_array=[]
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	for task in tasks:
		task_array.append(task.task.title)

	form=members_credit_issue_item_form(request.POST or None)
	product = Stock.objects.get(id=pk)
	member=Members.objects.get(id=member_id)

	form.fields['code'].initial=product.code
	form.fields['item_name'].initial=product.item_name
	form.fields['available_quantity'].initial=product.quantity
	form.fields['unit_selling_price'].initial=product.unit_selling_price

	if request.method=="POST":
		tdate =  get_current_date(now)


		status="UNTREATED"
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
		processed_by=processed_by.username

		if Members_Cash_Sales_Selected.objects.filter(member=member,status=status,processed_by=processed_by).exists():
			ticket_id=Members_Cash_Sales_Selected.objects.filter(member=member,status=status).first()
			selected_ticket=ticket_id.ticket
		else:
			_ticket=GeneralTicket.objects.first()
			selected_ticket=_ticket.ticket

			_ticket.ticket = int(_ticket.ticket) + 1
			_ticket.save()

			# selected_ticket=str(now.year) +  str(now.month) +  str(now.day) + str(now.hour) +  str(now.minute) + str(now.second)

		if Members_Cash_Sales_Selected.objects.filter(sources='MAIN',member=member,product=product,status=status,processed_by=processed_by).exists():

			record_exist=Members_Cash_Sales_Selected.objects.get(sources='MAIN',member=member,product=product,status=status,processed_by=processed_by) #.first()
			record_exist.quantity=int(quantity)
			record_exist.unit_selling_price=unit_selling_price
			record_exist.total=total
			record_exist.save()
			return HttpResponseRedirect(reverse('members_cash_sales_product_load',args=(member_id,selected_ticket,)))

		record=Members_Cash_Sales_Selected(sources='MAIN',tdate=tdate,member=member,status=status,product=product,ticket=selected_ticket,quantity=quantity,unit_selling_price=unit_selling_price,total=total,processed_by=processed_by)
		record.save()
		return HttpResponseRedirect(reverse('members_cash_sales_product_load',args=(member_id,selected_ticket,)))

	context={
	'task_array':task_array,
	'form':form,
	'member':member,
	}
	return render(request,'shop_templates/members_cash_sales_item_issue.html',context)


def members_cash_sales_auction_item_issue(request,pk,member_id,ticket):
	task_array=[]
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	for task in tasks:
		task_array.append(task.task.title)

	form=members_credit_issue_item_form(request.POST or None)

	if not Stock_Auction.objects.filter(Q(stock__code=pk) & Q(quantity__gt=0)).exists():
		messages.error(request,'No record found')
		return HttpResponseRedirect(reverse('members_cash_sales_product_load',args=(member_id,ticket,)))

	product = Stock_Auction.objects.get(stock__code=pk)
	member=Members.objects.get(id=member_id)

	form.fields['code'].initial=product.stock.code
	form.fields['item_name'].initial=product.stock.item_name
	form.fields['available_quantity'].initial=product.quantity
	form.fields['unit_selling_price'].initial=product.unit_selling_price

	if request.method=="POST":
		tdate =  get_current_date(now)


		status="UNTREATED"
		quantity=request.POST.get('issue_quantity')
		if int(quantity)<=0:
			messages.error(request,"Quantity Selected cannot be Zero (0)")
			return HttpResponseRedirect(reverse('members_cash_sales_auction_item_issue', args=(pk,member_id,ticket)))

		if int(quantity)>int(product.quantity):
			messages.error(request,"Quantity Selected is more that Available Quantity")
			return HttpResponseRedirect(reverse('members_cash_sales_auction_item_issue', args=(pk,member_id,ticket)))


		unit_selling_price=product.unit_selling_price

		total=float(quantity) * float(unit_selling_price)
		processed_by=CustomUser.objects.get(id=request.user.id)
		processed_by=processed_by.username

		if Members_Cash_Sales_Selected.objects.filter(member=member,status=status,processed_by=processed_by).exists():
			ticket_id=Members_Cash_Sales_Selected.objects.filter(member=member,status=status).first()
			selected_ticket=ticket_id.ticket
		else:
			_ticket=GeneralTicket.objects.first()
			selected_ticket=_ticket.ticket


			_ticket.ticket = int(_ticket.ticket) + 1
			_ticket.save()

		if Members_Cash_Sales_Selected.objects.filter(sources='AUCTION',member=member,product=product.stock,status=status,processed_by=processed_by).exists():
			record_exist=Members_Cash_Sales_Selected.objects.filter(sources='AUCTION',member=member,product=product.stock,status=status).first()
			record_exist.quantity=quantity
			record_exist.unit_selling_price=unit_selling_price
			record_exist.total=total
			record_exist.save()
			return HttpResponseRedirect(reverse('members_cash_sales_product_load',args=(member_id,selected_ticket)))

		record=Members_Cash_Sales_Selected(sources='AUCTION',tdate=tdate,member=member,status=status,product=product.stock,ticket=selected_ticket,quantity=quantity,unit_selling_price=unit_selling_price,total=total,processed_by=processed_by)
		record.save()
		return HttpResponseRedirect(reverse('members_cash_sales_product_load',args=(member_id,selected_ticket)))

	context={
	'task_array':task_array,
	'form':form,
	'member':member,
	}
	return render(request,'shop_templates/members_cash_sales_auction_item_issue.html',context)


def members_cash_sales_item_delete(request,pk):
	record=Members_Cash_Sales_Selected.objects.get(id=pk)
	ticket=record.ticket
	member_id=record.member_id
	record.delete()
	return HttpResponseRedirect(reverse('members_cash_sales_product_load',args=(member_id,ticket)))


def general_cash_sales_dashboard(request):
	task_array=[]
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	for task in tasks:
		task_array.append(task.task.title)

	context={
	'task_array':task_array,
	}
	return render(request,'shop_templates/general_cash_sales_dashboard.html',context)


def general_cash_sales_products_load_routes(request):
	processed_by=CustomUser.objects.get(id=request.user.id)
	processed_by=processed_by.username

	if CustomerID.objects.all().exists():
		customer_obj=CustomerID.objects.first()
		customer_value=customer_obj.title
		customer_obj.title=str(int(customer_value) + 1).zfill(5)
		customer_obj.save()
	else:
		customer_value = 1
		CustomerID(title=2).save()

	customer_id='C' + str(customer_value).zfill(5)

	ticket_status='OPEN'
	status="UNUSED"
	locked_status='OPEN'
	cust_status='ACTIVE'

	record_drop = General_Cash_Sales_Selected.objects.filter(processed_by=processed_by)
	record_drop.delete()
	Customers.objects.filter(locked_status=locked_status,processed_by=processed_by).delete()

	customer=Customers(customer_id=customer_id,status=status,cust_status=cust_status,locked_status=locked_status,ticket_status='CLOSED',processed_by=processed_by)
	customer.save()


	return HttpResponseRedirect(reverse('general_cash_sales_products_load',args=(customer.pk,0)))


def general_cash_sales_products_load(request,pk,ticket):
	task_array=[]
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	for task in tasks:
		task_array.append(task.task.title)

	form=general_cash_issue_item_form(request.POST or None)
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

	form.fields['name'].initial=customer.name
	form.fields['address'].initial=customer.address
	form.fields['phone_no'].initial=customer.phone_no
	form.fields['receipt'].initial='00001'
	form.fields['receipt_types'].initial='AUTO'

	context={
	'task_array':task_array,
	'items':items,
	'customer':customer,
	'select_items':select_items,
	'total_item':total_item,
	'total_amount':total_amount,
	'button_show':button_show,
	'ticket':ticket,
	'form':form,
	}
	return render(request,'shop_templates/general_cash_sales_products_load.html',context)


def general_cash_sales_select_remove(request,pk,cust_id,ticket):
	item = General_Cash_Sales_Selected.objects.get(id=pk)
	item.delete()
	if General_Cash_Sales_Selected.objects.exclude(ticket=ticket).exists():
		locked_status='LOCKED'
		Customers.objects.filter(id=pk).update(phone_no=None,active_ticket=None,ticket_status=None,locked_status=locked_status)
	return HttpResponseRedirect(reverse('general_cash_sales_products_load',args=(cust_id,ticket)))



def general_cash_issue_item(request,pk,cust_id):
	task_array=[]
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	for task in tasks:
		task_array.append(task.task.title)

	processed_by=CustomUser.objects.get(id=request.user.id)
	processed_by=processed_by.username

	form =form=members_credit_issue_item_form(request.POST or None)
	customer=Customers.objects.get(id=cust_id)
	product = Stock.objects.get(id=pk)
	form.fields['code'].initial=product.code
	form.fields['item_name'].initial=product.item_name
	form.fields['available_quantity'].initial=product.quantity
	form.fields['unit_selling_price'].initial=product.unit_selling_price
	form.fields['issue_quantity'].initial=1

	if request.method == "POST":
		tdate =  get_current_date(now)


		code_id =request.POST.get('code')

		item=Stock.objects.get(code=request.POST.get('code'))

		# return HttpResponse(item.code)

		ticket_status="OPEN"
		cust_status='ACTIVE'


		status="UNTREATED"
		status1='USED'

		quantity=request.POST.get("issue_quantity")
		if int(item.quantity) < int(quantity):
			messages.error(request,"Quantity Selected is more Than Available Stock")
			return HttpResponseRedirect(reverse('general_cash_issue_item',args=(pk,cust_id)))

		unit_selling_price=product.unit_selling_price

		total=float(quantity) * float(unit_selling_price)
		
		if Customers.objects.filter(ticket_status=ticket_status,cust_status=cust_status,processed_by=processed_by).exists():
			select_customer=Customers.objects.get(ticket_status=ticket_status,processed_by=processed_by)
			selected_ticket=select_customer.active_ticket
			
		else:
			# now = datetime.now()
			
			_ticket=GeneralTicket.objects.first()
			selected_ticket=_ticket.ticket
			customer.status=status1
			customer.ticket_status=ticket_status
			customer.active_ticket=selected_ticket
			customer.processed_by=processed_by
			customer.save()

			_ticket.ticket = int(_ticket.ticket) + 1
			_ticket.save()

		if not selected_ticket:
			messages.error(request,"Ticket not Available")
			return HttpResponseRedirect(reverse('general_cash_issue_item',args=(pk,cust_id)))


		if General_Cash_Sales_Selected.objects.filter(sources='MAIN',product=product,ticket=selected_ticket).exists():
			record=General_Cash_Sales_Selected.objects.get(sources='MAIN',product=product,ticket=selected_ticket)
			record.quantity=quantity
			record.save()
			return HttpResponseRedirect(reverse('general_cash_sales_products_load',args=(cust_id,selected_ticket)))

		record=General_Cash_Sales_Selected(sources='MAIN',tdate=tdate,customer=customer,product=product,ticket=selected_ticket,quantity=quantity,unit_selling_price=unit_selling_price,total=total,processed_by=processed_by,status=status)
		record.save()

		return HttpResponseRedirect(reverse('general_cash_sales_products_load',args=(cust_id,selected_ticket)))
	context={
	'task_array':task_array,
	'form':form,
	'customer':customer,
	}
	return render(request,"shop_templates/general_cash_issue_item.html",context)


def general_cash_issue_auction_item(request,pk,cust_id,ticket):
	task_array=[]
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	for task in tasks:
		task_array.append(task.task.title)

	processed_by=CustomUser.objects.get(id=request.user.id)
	processed_by=processed_by.username

	form =form=members_credit_issue_item_form(request.POST or None)
	customer=Customers.objects.get(id=cust_id)
	if not Stock_Auction.objects.filter(stock__code=pk).exists():
		messages.error(request, 'No record found')
		return HttpResponseRedirect(reverse('general_cash_sales_products_load',args=(cust_id,ticket)))

	product = Stock_Auction.objects.get(stock__code=pk)
	form.fields['code'].initial=product.stock.code
	form.fields['item_name'].initial=product.stock.item_name
	form.fields['available_quantity'].initial=product.quantity
	form.fields['unit_selling_price'].initial=product.unit_selling_price

	if request.method == "POST":
		tdate =  get_current_date(now)


		code_id =request.POST.get('code')

		item=Stock_Auction.objects.get(stock__code=request.POST.get('code'))

		# return HttpResponse(item.code)

		ticket_status="OPEN"
		cust_status='ACTIVE'


		status="UNTREATED"
		status1='USED'

		quantity=request.POST.get("issue_quantity")
		if int(item.quantity) < int(quantity):
			messages.error(request,"Quantity Selected is more Than Available Stock")
			return HttpResponseRedirect(reverse('general_cash_issue_auction_item',args=(pk,cust_id,ticket)))

		unit_selling_price=product.unit_selling_price

		total=float(quantity) * float(unit_selling_price)
		if Customers.objects.filter(ticket_status=ticket_status,cust_status=cust_status,processed_by=processed_by).exists():
			select_customer=Customers.objects.get(ticket_status=ticket_status,processed_by=processed_by)
			selected_ticket=select_customer.active_ticket
		else:
			# now = datetime.now()
			# return HttpResponse("ok")
			_ticket=GeneralTicket.objects.first()
			selected_ticket=_ticket.ticket
			customer.status=status1
			customer.ticket_status=ticket_status
			customer.active_ticket=selected_ticket
			customer.processed_by=processed_by
			customer.save()

			_ticket.ticket = int(_ticket.ticket) + 1
			_ticket.save()

		if General_Cash_Sales_Selected.objects.filter(sources='AUCTION',product=product.stock,ticket=selected_ticket).exists():
			record=General_Cash_Sales_Selected.objects.get(sources='AUCTION',product=product.stock,ticket=selected_ticket)
			record.quantity=quantity
			record.save()
			return HttpResponseRedirect(reverse('general_cash_sales_products_load',args=(cust_id,selected_ticket)))

		record=General_Cash_Sales_Selected(sources='AUCTION',tdate=tdate,customer=customer,product=product.stock,ticket=selected_ticket,quantity=quantity,unit_selling_price=unit_selling_price,total=total,processed_by=processed_by,status=status)
		record.save()

		return HttpResponseRedirect(reverse('general_cash_sales_products_load',args=(cust_id,selected_ticket)))

	context={
	'task_array':task_array,
	'form':form,
	'customer':customer,

	}
	return render(request,"shop_templates/general_cash_issue_item.html",context)


def auction_stock_item_list(request):
	task_array=[]
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	for task in tasks:
		task_array.append(task.task.title)

	records=Stock_Auction.objects.filter(Q(quantity__gt=0))
	context={
	'task_array':task_array,
	'records':records,
	}
	return render(request,"shop_templates/auction_stock_item_list.html",context)


def general_cash_issue_item_preview(request,ticket):
	task_array=[]
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	for task in tasks:
		task_array.append(task.task.title)

	form=Daily_Sales_Summar_Form(request.POST or None)
	receipt_print_form=Final_Members_Cash_Sales_Processing_form(request.POST or None)

	processed_by=CustomUser.objects.get(id=request.user.id)
	processed_by=processed_by.username

	tdate =  get_current_date(now)
	status='UNTREATED'
	status1='TREATED'
	receipt_status="USED"
	locked_status='LOCKED'
	sales_category='CASH'

	button_show=False
	record=[]
	if Daily_Sales_Summary.objects.filter(ticket=ticket).exists():
		record=Daily_Sales_Summary.objects.get(ticket=ticket)
		if record.submission_status == 'SUBMITTED':
			button_show=True

	customer=Customers.objects.get(active_ticket=ticket)
	# autoprint=YesNo.objects.all()
	# autoFormPrint=FormAutoPrints.objects.get(title='SHOP SALES')

	total_amount=0
	total_item=0
	cash_only=[]
	if not record:
		queryset=General_Cash_Sales_Selected.objects.filter(ticket=ticket).aggregate(total_amount=Sum('total'),total_item=Sum('quantity'))
		total_item=queryset['total_item']
		total_amount=queryset['total_amount']

	select_items=General_Cash_Sales_Selected.objects.filter(ticket=ticket)

	cash=False
	if request.method=='POST' and 'btn_fetch' in request.POST:
		cash_only=request.POST.get('cash_only')
		button_show=False
		if cash_only:
			button_show=True
		else:
			button_show=False
			if record:
				if record.submission_status == 'SUBMITTED':
					button_show=True

		if Daily_Sales_Summary.objects.filter(ticket=ticket).exists():
			record=Daily_Sales_Summary.objects.get(ticket=ticket)
			if cash_only:
				record.cash=float(record.amount)
				record.pos=0
				record.transfer=0
				record.save()
		else:
			cust_name=request.POST.get('name')
			address=request.POST.get('address')
			phone_no=request.POST.get('phone_no')
			customer=Customers.objects.get(active_ticket=ticket)
			cust_pk=customer.id
			customer.name=cust_name
			customer.address=address
			customer.phone_no=phone_no
			customer.save()

			if Customers.objects.filter(phone_no=phone_no).count()>1:
				record_drop=Customers.objects.filter(phone_no=phone_no).first()
				record_drop.delete()

			receipt_types=request.POST.get('receipt_types')
			

			if receipt_types == 'AUTO':
				receipt_id=AutoReceipt.objects.first()
				receipt= "AUT-" + str(receipt_id.receipt.zfill(5))
				receipt_id.receipt=int(receipt_id.receipt)+1
				receipt_id.save()
			elif receipt_types == 'MANUAL':
				receipt_id=request.POST.get('receipt')
				if receipt_id:
					receipt_obj=Receipts_Shop.objects.get(receipt=receipt_id)
					receipt=receipt_obj.receipt
				else:
					messages.error(request,"Receipt Missing")
					return HttpResponseRedirect(reverse('general_cash_issue_item_preview',args=(ticket,)))
			else:
				messages.error(request,"Invalid Receipt Format")
				return HttpResponseRedirect(reverse('general_cash_issue_item_preview',args=(ticket,)))

			grand_total=0
			for item in select_items:
				quantity=int(item.quantity)
				total=float(item.total)
				grand_total=grand_total +float(item.total)
				sales_detail=Daily_Sales(sources=item.sources,sales_category=sales_category,tdate=tdate,receipt=receipt,name=cust_name,phone_no=phone_no,address=address,product=item.product,ticket=item.ticket,quantity=item.quantity,unit_selling_price=item.unit_selling_price,total=item.total,processed_by=item.processed_by,status=status1)
				sales_detail.save()

			sale=Daily_Sales.objects.filter(ticket=ticket).first()
			summary=Daily_Sales_Summary(ticket=ticket,tdate=tdate,receipt=receipt,sale=sale,amount=grand_total,cash=grand_total,pos=0,transfer=0,status=status1,processed_by=processed_by)
			summary.save()

			record=Daily_Sales_Summary.objects.get(ticket=ticket)

			if receipt_types == 'MANUAL':
				Receipts_Shop.objects.filter(receipt=receipt_id).update(status=receipt_status)


	if request.method=='POST' and 'btn-add' in request.POST:
		channel=request.POST.get('channel')
		bank_id=request.POST.get('banks')
		bank=Banks.objects.get(id=bank_id)
		account_name=request.POST.get('account_name')
		other_details=request.POST.get('other_details')
		amount=request.POST.get('amount')
		coop_account_id=request.POST.get('coop_accounts')
		coop_account=CooperativeBankAccounts.objects.get(id=coop_account_id)

		if channel=='POS':
			if (float(record.transfer)+float(amount)) > float(record.amount):
				messages.error(request,'Invalid Amount Specification' + str(float(record.transfer)+float(amount)))
				return HttpResponseRedirect(reverse('general_cash_issue_item_preview',args=(ticket,)))

			record.pos=amount
			record.cash=float(record.amount)-(float(record.transfer)+float(amount))
		elif channel=='TRANSFER':
			if (float(record.pos)+float(amount)) > float(record.amount):
				messages.error(request,'Invalid Amount Specification ' + str(float(record.pos)+float(amount)))
				return HttpResponseRedirect(reverse('general_cash_issue_item_preview',args=(ticket,)))

			record.transfer=amount
			record.cash=float(record.amount)-(float(record.pos)+float(amount))

		record.source_bank=bank
		record.account_name=account_name
		record.other_details=other_details
		record.coop_account=coop_account
		record.submission_status="SUBMITTED"
		record.save()

		button_show=True
		return HttpResponseRedirect(reverse('general_cash_issue_item_preview',args=(ticket,)))

	if request.method=='POST' and 'btn-submit' in request.POST:
		autoprint=request.POST.get('receipt_print')
		

		if Customers.objects.filter(active_ticket=ticket).exists():
			active_cust = Customers.objects.get(active_ticket=ticket)
		else:
			messages.error(request,'Customer do not exists')
			return HttpResponseRedirect(reverse('general_cash_issue_item_preview',args=(ticket,)))

		for item in select_items:
			quantity=int(item.quantity)
			total=float(item.total)

			if item.sources=='MAIN':
				record=Stock.objects.get(code=item.product.code)
				record.quantity=int(record.quantity)-quantity
				record.save()
			elif item.sources == 'AUCTION':
				record=Stock_Auction.objects.get(stock__code=item.product.code)
				record.quantity=int(record.quantity)-quantity
				record.save()

		if active_cust.name == "Anonymous":
			Customers.objects.filter(active_ticket=ticket).delete()
		else:
			Customers.objects.filter(active_ticket=ticket).update(active_ticket=None,ticket_status=None,locked_status=locked_status)


		General_Cash_Sales_Selected.objects.filter(ticket=ticket).delete()

		if autoprint == "NO":
			return HttpResponseRedirect(reverse('general_cash_sales_dashboard'))
		elif autoprint == 'YES':
			return HttpResponseRedirect(reverse('general_cash_issue_item_print_receipt',args=(ticket,)))

	context={
	'task_array':task_array,
	'select_items':select_items,
	'form':form,
	'ticket':ticket,
	'record':record,
	'cash_only':cash_only,
	'button_show':button_show,
	
	'receipt_print_form':receipt_print_form,

	}
	return render(request,'shop_templates/general_cash_issue_item_preview.html',context)



def general_cash_issue_item_discard_payment(request,pk,ticket):
	record=Daily_Sales_Summary.objects.get(ticket=ticket)
	if pk=='POS':
		amount=float(record.pos)
		record.cash=float(record.cash)+float(amount)
		record.pos=0

	elif pk=='TRANSFER':
		amount=record.transfer
		record.cash=float(record.cash)+float(amount)
		record.transfer=0

	record.save()

	if record.pos == 0 and record.transfer == 0:
		record.submission_status="NOT SUBMITTED"
		record.save()
	return HttpResponseRedirect(reverse('general_cash_issue_item_preview',args=(ticket,)))




def general_cash_issue_item_print_receipt(request,ticket):
	task_array=[]
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	for task in tasks:
		task_array.append(task.task.title)

	select_items=Daily_Sales.objects.filter(ticket=ticket)

	# customer=Customers.objects.get(id=cust_id)

	sales_data=Daily_Sales.objects.filter(ticket=ticket).first()

	queryset=Daily_Sales.objects.filter(ticket=ticket).aggregate(total_amount=Sum('total'),total_item=Sum('quantity'))
	total_item=queryset['total_item']
	total_amount=queryset['total_amount']

	processed_by=CustomUser.objects.get(id=request.user.id)
	processed_by=processed_by.username

	if InvoiceHeader.objects.all().count()>0:
		record=InvoiceHeader.objects.first()
	else:
		record="FETHAII CTCS"

	context={
	'task_array':task_array,
	'record':record,
	'select_items':select_items,
	# 'customer':customer,
	'total_item':total_item,
	'total_amount':total_amount,
	'processed_by':processed_by,
	'sales_data':sales_data,

	}
	return render(request,'shop_templates/general_cash_issue_item_print_receipt.html',context)


def general_cash_load_existing_customers_search(request):
	task_array=[]
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	for task in tasks:
		task_array.append(task.task.title)

	title="Search Existing Customers"
	form = searchForm(request.POST or None)


	return render(request,'shop_templates/general_cash_load_existing_customers_search.html',{'form':form,'title':title,'task_array':task_array})


def general_cash_load_existing_customers(request):
	task_array=[]
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	for task in tasks:
		task_array.append(task.task.title)

	title="Existing Registered Customers"
	if request.method == "POST":
		form = searchForm(request.POST)
		if not form['title'].value():
			messages.info(request,'No Matching Record Found')
			return HttpResponseRedirect(reverse('general_cash_load_existing_customers_search'))

		members=Customers.objects.filter(Q(phone_no__icontains=form['title'].value()) | Q(name__icontains=form['title'].value())).exclude(name__icontains='Anonymous')
		if not members:
			messages.info(request,'No Matching Record Found')
			return HttpResponseRedirect(reverse('general_cash_load_existing_customers_search'))



		context={
		'task_array':task_array,

		'customers':members,
		'title':title,
		'ticket':'0'
		}
		return render(request,'shop_templates/general_cash_load_existing_customers.html',context)

def Daily_Sales_Summarization(request,pk):
	task_array=[]
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	for task in tasks:
		task_array.append(task.task.title)

	from datetime import datetime
	form=Daily_Sales_Summarization_form(request.POST or None)
	processed_by= CustomUser.objects.get(id=request.user.id)
	processed_by=processed_by.username

	status='UNTREATED'
	status1='TREATED'

	processing_status='UNPROCESSED'
	processing_status1='PROCESSED'

	records=[]
	total_credit_amount=0
	total_cash_amount=0
	total_amount=0
	button_show = False

	if request.method == 'POST' and 'btn_fetch' in request.POST:

		current_date=request.POST.get('current_date')
		date_format = '%Y-%m-%d'
		dtObj = datetime.strptime(current_date, date_format)

		year=int(dtObj.year)
		month=int(dtObj.month)
		day=int(dtObj.day)

		Members_Cash_Sales_Selected.objects.filter(processed_by=processed_by,status=status).delete()
		records=Daily_Sales_Summary.objects.filter(sale__processed_by=processed_by,tdate__year=year,tdate__month= month,tdate__day= day).filter(processing_status=processing_status)

		if records.count():
			button_show=True


		queryset=Daily_Sales.objects.filter(processed_by=processed_by,tdate__year=year,tdate__month= month,tdate__day= day).filter(sales_category='CREDIT',processing_status=processing_status).aggregate(total_credit=Sum('total'))
		total_credit_amount=queryset['total_credit']


		queryset=Daily_Sales.objects.filter(processed_by=processed_by,tdate__year=year,tdate__month= month,tdate__day= day).filter(sales_category='CASH',processing_status=processing_status).aggregate(total_cash=Sum('total'))
		total_cash_amount=queryset['total_cash']


		queryset=Daily_Sales.objects.filter(processed_by=processed_by,tdate__year=year,tdate__month= month,tdate__day= day).filter(processing_status=processing_status).aggregate(total_amount=Sum('total'))
		total_amount=queryset['total_amount']



		# items=Daily_Sales.objects.filter(processed_by=processed_by,created_at__year=year,created_at__month= month,created_at__day= day).order_by('receipt').values_list('receipt','item_code','item_name').distinct()


	if request.method == 'POST' and 'btn_details' in request.POST:
		current_date=request.POST.get('current_date')
		date_format = '%Y-%m-%d'
		dtObj = datetime.strptime(current_date, date_format)

		year=int(dtObj.year)
		month=int(dtObj.month)
		day=int(dtObj.day)

		tdate=date(year,month,day)

		records=Daily_Sales.objects.filter(processed_by=processed_by,tdate__year=year,tdate__month= month,tdate__day= day).filter(processing_status=processing_status)

		queryset=Daily_Sales.objects.filter(processed_by=processed_by,tdate__year=year,tdate__month= month,tdate__day= day).filter(processing_status=processing_status).aggregate(total_amount=Sum('total'))
		total_amount=queryset['total_amount']

		# return HttpResponse(total_amount)
		return render(request,'shop_templates/Full_Sales_List.html',{'records':records,'total_amount':total_amount,'task_array':task_array,})



	if request.method == 'POST' and 'btn_submit' in request.POST:
		current_date=request.POST.get('current_date')
		date_format = '%Y-%m-%d'
		dtObj = datetime.strptime(current_date, date_format)

		year=int(dtObj.year)
		month=int(dtObj.month)
		day=int(dtObj.day)

		tdate=get_current_date(dtObj)

		queryset=Daily_Sales.objects.filter(processed_by=processed_by,tdate__year=year,tdate__month= month,tdate__day= day).filter(sales_category='CREDIT',processing_status=processing_status).aggregate(total_credit=Sum('total'))
		total_credit_amount=queryset['total_credit']


		queryset=Daily_Sales.objects.filter(processed_by=processed_by,tdate__year=year,tdate__month= month,tdate__day= day).filter(sales_category='CASH',processing_status=processing_status).aggregate(total_cash=Sum('total'))
		total_cash_amount=queryset['total_cash']


		queryset=Daily_Sales.objects.filter(processed_by=processed_by,tdate__year=year,tdate__month= month,tdate__day= day).filter(processing_status=processing_status).aggregate(total_amount=Sum('total'))
		total_amount=queryset['total_amount']

		sales_category1='CASH'
		sales_category2='CREDIT'

		processed_by=CustomUser.objects.get(id=request.user.id)
		processed_by=processed_by.username

		if total_cash_amount:
			record=Daily_Sales_Cash_Flow_Summary(tdate=tdate,description='CASH SALES',amount=total_cash_amount,sales_category=sales_category1,processed_by=processed_by,status=status)
			record.save()

		if total_credit_amount:
			record=Daily_Sales_Cash_Flow_Summary(tdate=tdate,description='CREDIT SALES',amount=total_credit_amount,sales_category=sales_category2,processed_by=processed_by,status=status)
			record.save()


		Daily_Sales_Summary.objects.filter(sale__processed_by=processed_by,tdate__year=year,tdate__month= month,tdate__day= day).filter(processing_status=processing_status).update(processing_status=processing_status1)
		Daily_Sales.objects.filter(processed_by=processed_by,tdate__year=year,tdate__month= month,tdate__day= day).filter(processing_status=processing_status).update(processing_status=processing_status1)

		return HttpResponseRedirect(reverse('Daily_Sales_Summarization', args=(pk,)))

	form.fields['current_date'].initial=now


	context={
	'task_array':task_array,
	'form':form,
	'button_show':button_show,
	'records':records,
	# 'items':items,
	'total_cash_amount':total_cash_amount,
	'total_credit_amount':total_credit_amount,
	'total_amount':total_amount,
	}
	return render(request,'shop_templates/Daily_Sales_Summarization.html',context)


def Daily_Sales_Summary_Detail(request,pk):
	task_array=[]
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	for task in tasks:
		task_array.append(task.task.title)

	title="DETAILS OF SALES FOR RECEIPT"
	records=Daily_Sales.objects.filter(receipt=pk)
	queryset=Daily_Sales.objects.filter(receipt=pk).aggregate(total_cash=Sum('total'))
	total_amount=queryset['total_cash']


	context={
	'task_array':task_array,
	'receipt':pk,
	'title':title,
	'records':records,
	'total_amount':total_amount,
	}
	return render(request,'shop_templates/Daily_Sales_Summary_Detail.html',context)



def Day_End_Transaction_Summary(request):
	task_array=[]
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	for task in tasks:
		task_array.append(task.task.title)

	form=Daily_Sales_Summary_Form(request.POST or None)
	form.fields['sales_date'].initial=now
	status = 'UNTREATED'
	status1 = 'TREATED'
	tdate=get_current_date(now)
	cashbook_status='ACTIVE'
	processed_by = CustomUser.objects.get(id=request.user.id)
	processed_by=processed_by.username

	year=[]
	month=[]
	day=[]
	records=[]
	cash=[]
	credits=[]
	total_amount=0
	total_credit_amount=0
	total_cash_amount=0
	total_deposit=0
	button_show=False


	if request.method == 'POST' and 'btn_fetch' in request.POST:
		current_date=request.POST.get('sales_date')

		date_format = '%Y-%m-%d'
		dtObj = datetime.strptime(current_date, date_format)

		year=int(dtObj.year)
		month=int(dtObj.month)
		day=int(dtObj.day)

		records = Daily_Sales_Cash_Flow_Summary.objects.filter(tdate__year=year,tdate__month= month,tdate__day= day,status="UNTREATED")
		queryset=Daily_Sales_Cash_Flow_Summary.objects.filter(tdate__year=year,tdate__month= month,tdate__day= day,status="UNTREATED").aggregate(total_amount=Sum('amount'))
		total_amount=queryset['total_amount']



		credits=Daily_Sales_Cash_Flow_Summary.objects.filter(tdate__year=year,tdate__month= month,tdate__day= day,status="UNTREATED",sales_category='CREDIT')
		queryset=Daily_Sales_Cash_Flow_Summary.objects.filter(tdate__year=year,tdate__month= month,tdate__day= day,status="UNTREATED",sales_category='CREDIT').aggregate(total_credit=Sum('amount'))
		total_credit_amount=queryset['total_credit']


		cash=Daily_Sales_Cash_Flow_Summary.objects.filter(tdate__year=year,tdate__month= month,tdate__day= day,status="UNTREATED",sales_category='CASH')
		queryset=Daily_Sales_Cash_Flow_Summary.objects.filter(tdate__year=year,tdate__month= month,tdate__day= day,status="UNTREATED",sales_category='CASH').aggregate(total_cash=Sum('amount'))
		total_cash_amount=queryset['total_cash']


		if records.count() > 0:
			button_show=True


	if request.method == "POST" and 'btn_submit' in request.POST:
		current_date=request.POST.get('sales_date')

		date_format = '%Y-%m-%d'
		dtObj = datetime.strptime(current_date, date_format)

		year=int(dtObj.year)
		month=int(dtObj.month)
		day=int(dtObj.day)



		sales_category='CASH'

		cash_sales=Daily_Sales_Cash_Flow_Summary.objects.filter(tdate__year=year,tdate__month= month,tdate__day= day,status="UNTREATED",sales_category='CASH')
		queryset=Daily_Sales_Cash_Flow_Summary.objects.filter(tdate__year=year,tdate__month= month,tdate__day= day,status="UNTREATED",sales_category='CASH').aggregate(total_cash=Sum('amount'))
		total_cash_amount=queryset['total_cash']

		cash_book_array=[]
		if total_cash_amount:
			ticket=get_ticket()

			Daily_Sales_Cash_Flow_Summary.objects.filter(tdate__year=year,tdate__month= month,tdate__day= day,status="UNTREATED",sales_category='CASH').update(cash_book=ticket)
			cash_book_array.append(('CASH SALES',total_cash_amount,0,sales_category,ticket))
			record=Day_End_Sales_Transactions(description='CASH SALES',
												amount=total_cash_amount,
												sales_category=sales_category,
												processed_by=processed_by,
												status=status,
												cash_book=ticket,
												tdate=dtObj,
												)
			record.save()


		sales_category='CREDIT'
		credit_sales=Daily_Sales_Cash_Flow_Summary.objects.filter(tdate__year=year,tdate__month= month,tdate__day= day,status="UNTREATED",sales_category='CREDIT')
		queryset=Daily_Sales_Cash_Flow_Summary.objects.filter(tdate__year=year,tdate__month= month,tdate__day= day,status="UNTREATED",sales_category='CREDIT').aggregate(total_credit=Sum('amount'))
		total_credit_amount=queryset['total_credit']



		if total_credit_amount:
			ticket=get_ticket()
			Daily_Sales_Cash_Flow_Summary.objects.filter(tdate__year=year,tdate__month= month,tdate__day= day,status="UNTREATED",sales_category='CREDIT').update(cash_book=ticket)
			cash_book_array.append(('CREDIT SALES',0,total_credit_amount,sales_category,ticket))
			record=Day_End_Sales_Transactions(description='CREDIT SALES',
												amount=total_credit_amount,
												sales_category=sales_category,
												processed_by=processed_by,
												status="UNTREATED",
												cash_book=ticket,
												tdate=dtObj,
												)
			record.save()



		balance=0
		for item in cash_book_array:
			if CashBook_Shop.objects.all().exists():

				balance=shop_cashbook_balance()

				if item[3] == "CASH":
					balance=float(balance)+float(item[1])
					source='SALES'
				elif item[3] == "CREDIT":
					balance=float(balance)-float(item[2])
					source='SALES'

				shop_cashbook_posting(item[0],item[1],item[2],balance,'CA-' + str(item[4]),cashbook_status,tdate,processed_by,source)
			else:
				if item[3] == "CASH":
					source='SALES'
					balance=float(item[1])
				elif item[3] == "CREDIT":
					source='SALES'
					balance=-float(item[2])

			
				shop_cashbook_posting(item[0],item[1],item[2],balance,'CR-' + str(item[4]),cashbook_status,tdate,processed_by,source)


		Daily_Sales_Cash_Flow_Summary.objects.filter(tdate__year=year,tdate__month= month,tdate__day= day,status="UNTREATED").update(status="TREATED")

		return HttpResponseRedirect(reverse('Day_End_Transaction_Summary'))

	context={
	'task_array':task_array,
	'form':form,
	'cash':cash,
	'credits':credits,
	'total_credit_amount':total_credit_amount,
	'total_cash_amount':total_cash_amount,
	'total_amount':total_amount,
	'button_show':button_show,
	'tday':day,
	'tmonth':month,
	'tyear':year,
	}
	return render(request,'shop_templates/Day_End_Transaction_Summary.html',context)


def Day_End_Transaction_Summary_Details(request,pk,tday,tmonth,tyear):
	task_array=[]
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	for task in tasks:
		task_array.append(task.task.title)

	status = 'UNTREATED'

	records=Daily_Sales_Cash_Flow_Summary.objects.filter(tdate__year=tyear,tdate__month= tmonth,tdate__day= tday,status=status,sales_category=pk)
	queryset=Daily_Sales_Cash_Flow_Summary.objects.filter(tdate__year=tyear,tdate__month= tmonth,tdate__day= tday,status=status,sales_category=pk).aggregate(total_amount=Sum('amount'))
	total_cash=queryset['total_amount']


	context={
	'task_array':task_array,
	'records':records,
	'total_cash':total_cash,
	'title':pk,
	}
	return render(request,'shop_templates/Day_End_Transaction_Summary_Details.html',context)


def Month_End_Transaction_Summary(request):
	task_array=[]
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	for task in tasks:
		task_array.append(task.task.title)

	form=Daily_Sales_Summary_Form(request.POST or None)
	form.fields['sales_date'].initial=now
	status = 'UNTREATED'
	status1 = 'TREATED'
	processed_by = CustomUser.objects.get(id=request.user.id)
	processed_by=processed_by.username

	records=[]
	cash=[]
	credits=[]
	total_amount=0
	total_credit_amount=0
	total_cash_amount=0
	button_show=False
	tday=[]
	tmonth=[]
	tyear=[]

	if request.method == 'POST' and 'btn_fetch' in request.POST:


		current_date=request.POST.get('sales_date')

		date_format = '%Y-%m-%d'
		current_date = datetime.strptime(current_date, date_format)

		tday=current_date.day
		tmonth=current_date.month
		tyear=current_date.year

		records = Day_End_Sales_Transactions.objects.filter(Q(tdate__lte=current_date)).filter(status=status)
		queryset=Day_End_Sales_Transactions.objects.filter(Q(tdate__lte=current_date)).filter(status=status).aggregate(total_amount=Sum('amount'))
		total_amount=queryset['total_amount']

		credits=Day_End_Sales_Transactions.objects.filter(Q(tdate__lte=current_date)).filter(status=status,sales_category='CREDIT')
		queryset=Day_End_Sales_Transactions.objects.filter(Q(tdate__lte=current_date)).filter(status=status,sales_category='CREDIT').aggregate(total_credit=Sum('amount'))
		total_credit_amount=queryset['total_credit']


		cash=Day_End_Sales_Transactions.objects.filter(Q(tdate__lte=current_date)).filter(status=status,sales_category='CASH')
		queryset=Day_End_Sales_Transactions.objects.filter(Q(tdate__lte=current_date)).filter(status=status,sales_category='CASH').aggregate(total_cash=Sum('amount'))
		total_cash_amount=queryset['total_cash']

		if records.count() > 0:
			button_show=True


	if request.method == "POST" and 'btn_submit' in request.POST:
		current_date=request.POST.get('sales_date')

		date_format = '%Y-%m-%d'
		tdate = datetime.strptime(current_date, date_format)

		tday=tdate.day
		tmonth=tdate.month
		tyear=tdate.year

		sales_category='CASH'

		cash_sales=Day_End_Sales_Transactions.objects.filter(Q(tdate__lte=current_date)).filter(status=status,sales_category='CASH')
		queryset=Day_End_Sales_Transactions.objects.filter(Q(tdate__lte=current_date)).filter(status=status,sales_category='CASH').aggregate(total_cash=Sum('amount'))
		total_cash_amount=queryset['total_cash']

		if total_cash_amount:
			ticket=get_ticket()

			Day_End_Sales_Transactions.objects.filter(Q(tdate__lte=current_date)).filter(status=status,sales_category='CASH').update(month_key=ticket)
			record=Month_End_Sales_Transactions(description='CASH SALES',
												amount=total_cash_amount,
												sales_category=sales_category,
												processed_by=processed_by,
												month_key=ticket,
												status=status,
												tdate=current_date,
												)
			record.save()


		sales_category='CREDIT'

		credit_sales=Day_End_Sales_Transactions.objects.filter(Q(tdate__lte=current_date)).filter(status=status,sales_category='CREDIT')
		queryset=Day_End_Sales_Transactions.objects.filter(Q(tdate__lte=current_date)).filter(status=status,sales_category='CREDIT').aggregate(total_credit=Sum('amount'))
		total_credit_amount=queryset['total_credit']

		if total_credit_amount:
			ticket=get_ticket()
			Day_End_Sales_Transactions.objects.filter(Q(tdate__lte=current_date)).filter(status=status,sales_category='CREDIT').update(month_key=ticket)
			record=Month_End_Sales_Transactions(description='CREDIT SALES',
												amount=total_credit_amount,
												sales_category=sales_category,
												processed_by=processed_by,
												status=status,
												month_key=ticket,
												tdate=current_date,
												)
			record.save()

		Day_End_Sales_Transactions.objects.filter(Q(tdate__lte=current_date)).filter(status=status).update(status=status1)

		return HttpResponseRedirect(reverse('Month_End_Transaction_Summary'))


	context={
	'tday':tday,
	'tmonth':tmonth,
	'tyear':tyear,
	'task_array':task_array,
	'cash':cash,
	'credits':credits,
	'total_credit_amount':total_credit_amount,
	'total_cash_amount':total_cash_amount,
	'total_amount':total_amount,
	'form':form,
	'button_show':button_show,
	}
	return render(request,'shop_templates/Month_End_Transaction_Summary.html',context)


def Year_End_Transaction_Summary(request):
	task_array=[]
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	for task in tasks:
		task_array.append(task.task.title)

	form=Daily_Sales_Summary_Form(request.POST or None)
	form.fields['sales_date'].initial=now
	status = 'UNTREATED'
	status1 ='TREATED'
	tdate=get_current_date(now)
	processed_by = CustomUser.objects.get(id=request.user.id)
	processed_by=processed_by.username


	records=[]
	cash=[]
	credits=[]
	total_amount=0
	total_credit_amount=0
	total_cash_amount=0
	button_show=False


	if request.method == 'POST' and 'btn_fetch' in request.POST:

		current_date=request.POST.get('sales_date')

		date_format = '%Y-%m-%d'
		current_date = datetime.strptime(current_date, date_format)

		# year=int(current_date.year)
		# month=int(current_date.month)
		# day=int(current_date.day)

		records = Month_End_Sales_Transactions.objects.filter(Q(tdate__lte=current_date)).filter(status=status)
		queryset=Month_End_Sales_Transactions.objects.filter(Q(tdate__lte=current_date)).filter(status=status).aggregate(total_amount=Sum('amount'))
		total_amount=queryset['total_amount']



		credits=Month_End_Sales_Transactions.objects.filter(Q(tdate__lte=current_date)).filter(status=status,sales_category='CREDIT')
		queryset=Month_End_Sales_Transactions.objects.filter(Q(tdate__lte=current_date)).filter(status=status,sales_category='CREDIT').aggregate(total_credit=Sum('amount'))
		total_credit_amount=queryset['total_credit']


		cash=Month_End_Sales_Transactions.objects.filter(Q(tdate__lte=current_date)).filter(status=status,sales_category='CASH')
		queryset=Month_End_Sales_Transactions.objects.filter(Q(tdate__lte=current_date)).filter(status=status,sales_category='CASH').aggregate(total_cash=Sum('amount'))
		total_cash_amount=queryset['total_cash']

		if records.count() > 0:
			button_show=True

	if request.method == "POST" and 'btn_submit' in request.POST:
		current_date=request.POST.get('sales_date')

		date_format = '%Y-%m-%d'
		current_date = datetime.strptime(current_date, date_format)

		sales_category='CASH'

		cash_sales=Month_End_Sales_Transactions.objects.filter(Q(tdate__lte=current_date)).filter(status=status,sales_category='CASH')
		queryset=Month_End_Sales_Transactions.objects.filter(Q(tdate__lte=current_date)).filter(status=status,sales_category='CASH').aggregate(total_cash=Sum('amount'))
		total_cash_amount=queryset['total_cash']

		if total_cash_amount:
			ticket=get_ticket()

			Month_End_Sales_Transactions.objects.filter(Q(tdate__lte=current_date)).filter(status=status,sales_category='CASH').update(year_key=ticket)
			record=Year_End_Sales_Transactions(description='CASH SALES',
												amount=total_cash_amount,
												sales_category=sales_category,
												processed_by=processed_by,
												year_key=ticket,
												status=status,
												tdate=tdate,
												)
			record.save()


		sales_category='CREDIT'

		credit_sales=Month_End_Sales_Transactions.objects.filter(Q(tdate__lte=current_date)).filter(status=status,sales_category='CREDIT')
		queryset=Month_End_Sales_Transactions.objects.filter(Q(tdate__lte=current_date)).filter(status=status,sales_category='CREDIT').aggregate(total_credit=Sum('amount'))
		total_credit_amount=queryset['total_credit']

		if total_credit_amount:
			ticket=get_ticket()
			Month_End_Sales_Transactions.objects.filter(Q(tdate__lte=current_date)).filter(status=status,sales_category='CREDIT').update(year_key=ticket)
			record=Year_End_Sales_Transactions(description='CREDIT SALES',
												amount=total_credit_amount,
												sales_category=sales_category,
												processed_by=processed_by,
												status=status,
												year_key=ticket,
												tdate=tdate,
												)
			record.save()

		Month_End_Sales_Transactions.objects.filter(Q(tdate__lte=current_date)).filter(status=status).update(status=status1)

		return HttpResponseRedirect(reverse('Year_End_Transaction_Summary'))


	context={
	'task_array':task_array,
	'cash':cash,
	'credits':credits,
	'total_credit_amount':total_credit_amount,
	'total_cash_amount':total_cash_amount,
	'total_amount':total_amount,
	'form':form,
	'button_show':button_show,
	}
	return render(request,'shop_templates/Year_End_Transaction_Summary.html',context)





def members_credit_sales_status_search(request):
	task_array=[]
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	for task in tasks:
		task_array.append(task.task.title)

	title="Search Members"
	form = searchForm(request.POST or None)

	return render(request,'shop_templates/members_credit_sales_status_search.html',{'form':form,'title':title,'task_array':task_array})



def members_credit_sales_status_list_load(request):
	task_array=[]
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	for task in tasks:
		task_array.append(task.task.title)

	title="Membership Purchases"
	if request.method == "POST":
		form = searchForm(request.POST)
		status = 'ACTIVE'

		members=searchMembers(form['title'].value(),status)

		context={
		'task_array':task_array,
		'members':members,
		'title':title,
		}
		return render(request,'shop_templates/members_credit_sales_status_list_load.html',context)



def members_credit_sales_status_details(request,pk):
	task_array=[]
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	for task in tasks:
		task_array.append(task.task.title)

	title="Membership Purchases"

	processing_status = 'UNPROCESSED'

	member=Members.objects.get(id=pk)
	schedule_status='UNSCHEDULED'
	record_array=[]
	records=members_credit_sales_summary.objects.filter(trans_code__member=member,processing_status=processing_status)
	for item in records:
		record_array.append((item.tdate,item.amount,item.trans_code.ticket))

	context={
	'task_array':task_array,
	'member':member,
	'title':title,
	'records':records,
	'record_array':record_array,
	}
	return render(request,'shop_templates/members_credit_sales_status_details.html',context)

def members_credit_sales_status_details_preview(request,pk):
	task_array=[]
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	for task in tasks:
		task_array.append(task.task.title)

	title="Membership Purchases"


	records=Members_Credit_Sales_Selected.objects.filter(ticket=pk)

	context={
	'task_array':task_array,
	'member':records[0].member.get_full_name,
	'title':title,
	'records':records,
	'ticket':pk,
	}
	return render(request,'shop_templates/members_credit_sales_status_details_preview.html',context)


def members_shop_credit_loan_salary_institution_select(request):
	task_array=[]
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	for task in tasks:
		task_array.append(task.task.title)

	status='ACTIVE'
	records=SalaryInstitution.objects.all()
	transaction_period=TransactionPeriods.objects.get(status=status)
	transaction_period=transaction_period.transaction_period

	context={
	'task_array':task_array,
	'records':records,
	'transaction_period':transaction_period,
	}
	return render(request,'shop_templates/members_shop_credit_loan_salary_institution_select.html',context)


def members_shop_sales_credit_generate(request,pk):
	form=members_shop_sales_credit_generate_form(request.POST or None)
	task_array=[]
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	for task in tasks:
		task_array.append(task.task.title)

	transaction=TransactionTypes.objects.get(name='SHOP')
	loan_code=transaction.code

	status1='ACTIVE'

	status="TREATED"
	status2="UNTREATED"
	processing_status='UNPROCESSED'
	processing_status2='PROCESSED'
	salary_institution=SalaryInstitution.objects.get(id=pk)
	schedule_status='UNSCHEDULED'

	if not members_credit_sales_summary.objects.filter(processing_status=processing_status,trans_code__member__salary_institution=salary_institution,status=status).exists():
		messages.error(request,'No record found')
		return HttpResponseRedirect(reverse('members_shop_credit_loan_salary_institution_select'))

	members=members_credit_sales_summary.objects.filter(processing_status=processing_status,trans_code__member__salary_institution=salary_institution,status=status).order_by('trans_code__member_id').values_list('trans_code__member_id','trans_code__member__member_id','trans_code__member__ippis_no','trans_code__member__admin__last_name','trans_code__member__admin__first_name','trans_code__member__middle_name').distinct()


	queryset=  members_credit_sales_summary.objects.filter(processing_status=processing_status,trans_code__member__salary_institution=salary_institution,status=status).aggregate(total_cash=Sum('amount'))
	grand_total=queryset['total_cash']

	if grand_total:
		grand_total=grand_total
	else:
		grand_total=0

	deduction_array=[]
	for member in members:

		queryset=  members_credit_sales_summary.objects.filter(trans_code__member__member_id=member[1],processing_status=processing_status,trans_code__member__salary_institution=salary_institution,status=status).aggregate(total_cash=Sum('amount'))
		total_amount=queryset['total_cash']

		deduction_array.append((member[1][13:],member[3] + " " + member[4]+ " " + member[5],member[2],total_amount))


	if request.method == 'POST':
		tdate=request.POST.get('period')
		date_format = '%Y-%m-%d'
		dtObj = datetime.strptime(tdate, date_format)

		tdate=get_current_date(dtObj)

		processed_by=CustomUser.objects.get(id=request.user.id)
		processed_by=processed_by.username

		deduction_array=[]
		for member in members:
			record=Members.objects.get(member_id=member[1])

			queryset=  members_credit_sales_summary.objects.filter(trans_code__member__member_id=member[1],processing_status=processing_status,trans_code__member__salary_institution=salary_institution,status=status).aggregate(total_cash=Sum('balance'))
			total_amount=abs(queryset['total_cash'])
			my_id=member[1][13:]

			loan_number = generate_number(loan_code,my_id,now)
			# deduction_array.append((member[1][13:],member[3] + " " + member[4]+ " " + member[5],member[2],total_amount,loan_number))

			members_shop_credit_loans(member=record,account_name=transaction,loan_number=loan_number,
											loan_amount=total_amount,amount_paid=0,balance=-total_amount,status=status2,processed_by=processed_by,schedule_status=schedule_status,tdate=tdate).save()

			members_credit_sales_summary.objects.filter(trans_code__member__member_id=member[1],processing_status=processing_status,trans_code__member__salary_institution=salary_institution,status=status).update(loan_number=loan_number,processing_status=processing_status2)


		# queryset=  members_credit_sales_summary.objects.filter(processing_status=processing_status,trans_code__member__salary_institution=salary_institution,status=status).update(processing_status=processing_status2)
		return HttpResponseRedirect(reverse('members_shop_credit_loan_salary_institution_select'))

	form.fields['period'].initial=now
	context={
	'form':form,
	'task_array':task_array,
	'members':members,
	'salary_institution':salary_institution,
	'deduction_array':deduction_array,
	'grand_total':grand_total,
	}
	return render(request,'shop_templates/members_shop_sales_credit_generate.html',context)


def Item_Return_Search_Page(request):
	task_array=[]
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	for task in tasks:
		task_array.append(task.task.title)

	title="Search Product for return"
	form = searchForm(request.POST or None)

	return render(request,'shop_templates/Item_Return_Search_Page.html',{'form':form,'title':title,'task_array':task_array})




def Item_Return_list_load(request):
	task_array=[]
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	for task in tasks:
		task_array.append(task.task.title)


	if request.method == "POST":
		form = searchForm(request.POST)
		status = 'ACTIVE'

		records=Stock.objects.filter(Q(code__icontains=form['title'].value()) | Q(item_name__icontains=form['title'].value()) | Q(details__icontains=form['title'].value()))

		context={
		# 'task_array':task_array,
		'records':records,

		}
		return render(request,'shop_templates/Item_Return_list_load.html',context)


def Item_Return_Select(request,pk):
	task_array=[]
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	for task in tasks:
			task_array.append(task.task.title)

	form=stock_status_list_details_Form(request.POST or None)
	record=records=Stock.objects.get(id=pk)
	records=[]
	if request.method == 'POST':
		start_date=request.POST.get("start_date")
		stop_date=request.POST.get("stop_date")
		records=Daily_Sales.objects.filter(tdate__range=[start_date,stop_date],product__code=record.code)



	form.fields['start_date'].initial=now
	form.fields['stop_date'].initial=now
	context={
	'task_array':task_array,
	'record':record,
	'records':records,
	'form':form,
	}
	return render(request,'shop_templates/Item_Return_Select.html',context)


def Item_Return_Process(request,pk):
	task_array=[]
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	for task in tasks:
			task_array.append(task.task.title)
	processed_by=CustomUser.objects.get(id=request.user.id)
	processed_by=processed_by.username

	tdate=get_current_date(now)

	form=Item_Return_form(request.POST or None)
	record=Daily_Sales.objects.get(id=pk)


	profile_show=False
	if record.name == 'Anonymous':
		profile_show=True


	if request.method == 'POST':
		if profile_show:
			name=request.POST.get('name')
			phone_no=request.POST.get('phone_no')
			address=request.POST.get('address')

			if name == "Anonymous" or phone_no == 'Anonymous':
				messages.error(request,'Please update the Customer Profile')
				return HttpResponseRedirect(reverse('Item_Return_Process',args=(pk,)))

		returned_quantity=request.POST.get('quantity_returned')
		reasons=request.POST.get('reasons')
		if not returned_quantity or int(returned_quantity) <=0:
			messages.error(request,'Quantity Returned Missing')
			return HttpResponseRedirect(reverse('Item_Return_Process',args=(pk,)))

		if int(returned_quantity) + float(record.quantity_returned)>int(record.quantity):
			messages.error(request,'Quantity Specified cannot be more than the quantity purchased')
			return HttpResponseRedirect(reverse('Item_Return_Process',args=(pk,)))

		if not reasons:
			messages.error(request,'Reasons Missing')
			return HttpResponseRedirect(reverse('Item_Return_Process',args=(pk,)))

		if profile_show:
			record.name=name
			record.address=address
			record.phone_no=phone_no
			record.save()
		if Daily_Sales_Item_Return.objects.filter(sales=record).exists():
			item=Daily_Sales_Item_Return.objects.get(sales=record)
			pass

		else:
			item=Daily_Sales_Item_Return(sales=record,
									quantity=returned_quantity,
									total=float(returned_quantity)*float(record.product.unit_selling_price),
									status="UNTREATED",
									processing_status='UNPROCESSED',
									processed_by=processed_by,
									reasons=reasons,
									tdate=tdate)
			item.save()
			stock_update=Stock.objects.filter(code=record.product.code).update(quantity=F('quantity')+returned_quantity)
			record=Daily_Sales.objects.filter(id=pk).update(quantity_returned=F('quantity_returned')+returned_quantity,date_returned=tdate)
		return HttpResponseRedirect(reverse('Item_Return_Process_Type',args=(item.pk,)))


	form.fields['name'].initial=record.name
	form.fields['phone_no'].initial=record.phone_no
	form.fields['address'].initial=record.address
	form.fields['code'].initial=record.product.code
	form.fields['item_name'].initial=record.product.item_name
	form.fields['details'].initial=record.product.details
	form.fields['quantity'].initial=record.quantity
	form.fields['unit_selling_price'].initial=record.unit_selling_price
	form.fields['total'].initial=record.total
	context={
	'task_array':task_array,
	'record':record,
	'form':form,
	'profile_show':profile_show,
	}
	return render(request,'shop_templates/Item_Return_Process.html',context)


def Item_Return_Process_Type(request,pk):
	task_array=[]
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	for task in tasks:
			task_array.append(task.task.title)

	record=Daily_Sales_Item_Return.objects.get(id=pk)

	context={
	'task_array':task_array,
	'record':record,

	}
	return render(request,'shop_templates/Item_Return_Process_Type.html',context)


def Item_Return_Process_Stock_List_Load(request,pk):
	task_array=[]
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	for task in tasks:
			task_array.append(task.task.title)

	record=Daily_Sales_Item_Return.objects.get(id=pk)
	records=Stock.objects.filter(Q(quantity__gt=0) & ~Q(code=record.sales.product.code))
	items=Daily_Sales_Item_Return_Selection.objects.filter(customer=record,status='UNTREATED')
	queryset=Daily_Sales_Item_Return_Selection.objects.filter(customer=record,status='UNTREATED').aggregate(total_cost=Sum('total'),total_item=Sum('quantity'))

	total_cost=queryset['total_cost']
	total_item=queryset['total_item']

	button_show=False
	if items:
		button_show=True

	context={
	'task_array':task_array,
	'record':record,
	'records':records,
	'items':items,
	'total_item':total_item,
	'total_cost':total_cost,
	'button_show':button_show,
	}
	return render(request,'shop_templates/Item_Return_Process_Stock_List_Load.html',context)


def Item_Return_Process_issue_item(request,pk,item_return):
	task_array=[]
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	for task in tasks:
			task_array.append(task.task.title)
	tdate=get_current_date(now)
	processed_by=CustomUser.objects.get(id=request.user.id)
	processed_by=processed_by.username

	form=members_credit_issue_item_form(request.POST or None)

	product=Stock.objects.get(id=pk)
	item_returned=Daily_Sales_Item_Return.objects.get(id=item_return)


	if request.method == 'POST':
		issue_quantity=request.POST.get('issue_quantity')
		total=float(product.unit_selling_price)* float(issue_quantity)


		Daily_Sales_Item_Return_Selection(customer=item_returned,
										product=product,
										quantity=issue_quantity,
										unit_selling_price=product.unit_selling_price,
										total=total,
										processed_by=processed_by,
										status='UNTREATED',
										tdate=tdate).save()
		return HttpResponseRedirect(reverse('Item_Return_Process_Stock_List_Load',args=(item_returned.pk,)))

	form.fields['code'].initial=product.code
	form.fields['item_name'].initial=product.item_name
	form.fields['details'].initial=product.details
	form.fields['available_quantity'].initial=product.quantity
	form.fields['unit_selling_price'].initial=product.unit_selling_price
	form.fields['issue_quantity'].initial=1

	context={
	'task_array':task_array,
	'record':product,
	'item_returned':item_returned,
	'form':form,
	}
	return render(request,'shop_templates/Item_Return_Process_issue_item.html',context)


def Item_Return_Process_issue_item_Delete(request,pk,item_return):
	Daily_Sales_Item_Return_Selection.objects.filter(id=pk).delete()
	return HttpResponseRedirect(reverse('Item_Return_Process_Stock_List_Load',args=(item_return,)))


def Item_Return_Process_issue_item_Preview(request,pk):
	task_array=[]
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	for task in tasks:
			task_array.append(task.task.title)

	tdate=get_current_date(now)
	processed_by=CustomUser.objects.get(id=request.user.id)
	processed_by=processed_by.username


	form=Item_Return_Process_issue_item_Preview_Form(request.POST or None)
	record=Daily_Sales_Item_Return.objects.get(id=pk)
	records=Daily_Sales_Item_Return_Selection.objects.filter(customer__sales=record.sales)
	queryset=Daily_Sales_Item_Return_Selection.objects.filter(customer__sales=record.sales).aggregate(total_cost=Sum('total'),total_item=Sum('quantity'))

	total_cost=queryset['total_cost']
	total_item=queryset['total_item']

	prev_amount=float(record.total)
	current_amount=float(total_cost)
	balance_amount=float(total_cost)-float(record.total)

	if request.method == 'POST' and 'btn-positive' in request.POST:
		channel=request.POST.get('channel')
		receipt_type_id=request.POST.get('receipt_type')
		receipt_type=ReceiptTypes.objects.get(id=receipt_type_id)

		return HttpResponseRedirect(reverse('Item_Return_Process_issue_item_processing',args=(pk,channel,receipt_type)))

	if request.method == 'POST' and 'btn-negative' in request.POST:
		item=Daily_Sales_Item_Return_Summary(sale=records[0],
										receipt=0,
										prev_amount=prev_amount,
										current_amount=current_amount,
										balance_amount=balance_amount,
										channel="NONE",
										submission_status="NOT SUBMITTED",
										processing_status="UNPROCESSED",
										tdate=tdate,
										status="UNTREATED",
										processed_by=processed_by,
										)
		item.save()
		Daily_Sales_Item_Return_Left_Over_Fund(sale=item,amount=abs(balance_amount),status='UNTREATED',processing_status="UNPROCESSED",processed_by=processed_by,tdate=tdate).save()
		Daily_Sales_Item_Return_Selection.objects.filter(customer__sales=record.sales).update(receipt=0,status='TREATED')
		record.status='TREATED'
		record.save()
		return HttpResponseRedirect(reverse('Item_Return_Manage_List_Load'))

	form.fields['prev_amount'].initial=record.total
	form.fields['current_amount'].initial=total_cost
	form.fields['balance_amount'].initial=balance_amount

	context={
	'task_array':task_array,
	'record':record,
	'form':form,
	'records':records,
	'balance_amount':balance_amount,
	}
	return render(request,'shop_templates/Item_Return_Process_issue_item_Preview.html',context)




def Item_Return_Process_issue_item_processing(request,pk,channel,receipt_type):
	task_array=[]
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	for task in tasks:
			task_array.append(task.task.title)
	tdate=get_current_date(now)
	processed_by=CustomUser.objects.get(id=request.user.id)
	processed_by=processed_by.username


	form=Item_Return_Process_issue_item_Preview_Form(request.POST or None)
	record=Daily_Sales_Item_Return.objects.get(id=pk)
	records=Daily_Sales_Item_Return_Selection.objects.filter(customer__sales=record.sales)
	queryset=Daily_Sales_Item_Return_Selection.objects.filter(customer__sales=record.sales).aggregate(total_cost=Sum('total'),total_item=Sum('quantity'))

	total_cost=queryset['total_cost']
	total_item=queryset['total_item']

	ticket=record.sales.ticket


	prev_amount=float(record.total)
	current_amount=float(total_cost)
	balance_amount=float(total_cost)-float(record.total)


	if request.method == 'POST' and 'btn-process' in request.POST:

		if receipt_type == 'AUTO':
			receipt_id=AutoReceipt.objects.first()
			receipt= "AUT-" + str(receipt_id.receipt.zfill(5))
			receipt_id.receipt=int(receipt_id.receipt)+1
			receipt_id.save()
		elif receipt_type == 'MANUAL':

			receipt_id=request.POST.get('receipt_no')
			if receipt_id:
				if Receipts_Shop.objects.filter(receipt=receipt_id,status='UNUSED').exists():

					receipt_obj=Receipts_Shop.objects.get(receipt=receipt_id)
					receipt=receipt_obj.receipt
				else:

					messages.error(request,"Receipt not Available")
					return HttpResponseRedirect(reverse('Item_Return_Process_issue_item_processing',args=(pk,channel,receipt_type,)))
			else:
				messages.error(request,"Receipt Missing")
				return HttpResponseRedirect(reverse('Item_Return_Process_issue_item_processing',args=(pk,channel,receipt_type,)))
		else:
			messages.error(request,"Invalid Receipt Format")
			return HttpResponseRedirect(reverse('Item_Return_Process_issue_item_processing',args=(pk,channel,receipt_type,)))




		Daily_Sales_Item_Return_Summary(sale=records[0],
										receipt=receipt,
										prev_amount=prev_amount,
										current_amount=current_amount,
										balance_amount=balance_amount,
										channel=channel,
										submission_status="NOT SUBMITTED",
										processing_status="UNPROCESSED",
										tdate=tdate,
										status="UNTREATED",
										processed_by=processed_by,
										).save()
		Daily_Sales_Item_Return_Selection.objects.filter(customer__sales__ticket=ticket).update(receipt=receipt,status='TREATED')
		record.status='TREATED'
		record.save()
		return HttpResponseRedirect(reverse('Item_Return_Manage_List_Load'))

	if request.method == 'POST' and 'btn-add' in request.POST:
		bank_id=request.POST.get('banks')
		source_bank=Banks.objects.get(id=bank_id)

		account_id=request.POST.get("coop_accounts")
		coop_account=CooperativeBankAccounts.objects.get(id=account_id)

		account_name=request.POST.get('account_name')
		other_details=request.POST.get('other_details')

		if not account_name:
			messages.error(request,'Account Name Missing')
			return HttpResponseRedirect(reverse('Item_Return_Process_issue_item_processing',args=(pk,channel,receipt_type,)))

		if not other_details:
			messages.error(request,'Other Details Missing')
			return HttpResponseRedirect(reverse('Item_Return_Process_issue_item_processing',args=(pk,channel,receipt_type,)))

		if receipt_type == 'AUTO':
			receipt_id=AutoReceipt.objects.first()
			receipt= "AUT-" + str(receipt_id.receipt.zfill(5))
			receipt_id.receipt=int(receipt_id.receipt)+1
			receipt_id.save()
		elif receipt_type == 'MANUAL':
			receipt_id=request.POST.get('receipt')
			if receipt_id:
				receipt_obj=Receipts_Shop.objects.get(receipt=receipt_id)
				receipt=receipt_obj.receipt
			else:
				messages.error(request,"Receipt Missing")
				return HttpResponseRedirect(reverse('Item_Return_Process_issue_item_processing',args=(pk,channel,receipt_type,)))
		else:
			messages.error(request,"Invalid Receipt Format")
			return HttpResponseRedirect(reverse('Item_Return_Process_issue_item_processing',args=(pk,channel,receipt_type,)))

		Daily_Sales_Item_Return_Summary(sale=records[0],
								receipt=receipt,
								prev_amount=prev_amount,
								current_amount=current_amount,
								balance_amount=balance_amount,
								channel=channel,
								source_bank=source_bank,
								account_name=account_name,
								other_details=other_details,
								coop_account=coop_account,
								submission_status="NOT SUBMITTED",
								processing_status="UNPROCESSED",
								tdate=tdate,
								status="UNTREATED",
								processed_by=processed_by,
								).save()
		Daily_Sales_Item_Return_Selection.objects.filter(customer__sales__ticket=ticket).update(receipt=receipt,status='TREATED')
		record.status='TREATED'
		record.save()
		return HttpResponseRedirect(reverse('Item_Return_Manage_List_Load'))

	pay_status=True
	if channel !="CASH":
		pay_status=False

	form.fields['balance_amount'].initial=balance_amount
	context={
	'task_array':task_array,
	'record':record,
	'form':form,
	'records':records,
	'channel':channel,
	'pay_status':pay_status,
	'receipt_type':receipt_type,
	}
	return render(request,'shop_templates/Item_Return_Process_issue_item_processing.html',context)



def Item_Return_Process_issue_item_processing_Daily_Summary(request):
	task_array=[]
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	for task in tasks:
			task_array.append(task.task.title)

	processed_by=CustomUser.objects.get(id=request.user.id)
	processed_by=processed_by.username

	tdate=get_current_date(now)
	records=Daily_Sales_Item_Return_Summary.objects.filter(processed_by=processed_by,status='UNTREATED').filter(Q(tdate=tdate))

	queryset=  Daily_Sales_Item_Return_Summary.objects.filter(processed_by=processed_by,status='UNTREATED').filter(Q(tdate=tdate)).aggregate(total_prev_amount=Sum('prev_amount'),total_current_amount=Sum('current_amount'))
	queryset_pos=  Daily_Sales_Item_Return_Summary.objects.filter(processed_by=processed_by,status='UNTREATED').filter(Q(tdate=tdate) & Q(balance_amount__gt=0)).aggregate(total_balance_amount=Sum('balance_amount'))
	queryset_neg=  Daily_Sales_Item_Return_Summary.objects.filter(processed_by=processed_by,status='UNTREATED').filter(Q(tdate=tdate) & Q(balance_amount__lt=0)).aggregate(total_balance_amount=Sum('balance_amount'))

	total_prev=queryset['total_prev_amount']
	total_current=queryset['total_current_amount']
	total_positive=queryset_pos['total_balance_amount']
	total_negative=queryset_neg['total_balance_amount']
	if not total_prev:
		total_prev=0

	if not total_current:
		total_current=0

	if not total_positive:
		total_positive=0

	if not total_negative:
		total_negative=0


	if request.method == 'POST':

		record=Daily_Sales_Item_Return_Cash_Flow_Summary(tdate=tdate,description='ITEMS RETURN',prev_amount=total_prev,
															current_amount=total_current,
															postive_balance=total_positive,
															negative_balance=total_negative,
															processed_by=processed_by,
															status="UNTREATED").save()




		Daily_Sales_Item_Return_Summary.objects.filter(processed_by=processed_by,status='UNTREATED').filter(Q(tdate=tdate)).update(status="TREATED")

		return HttpResponseRedirect(reverse('shop_home'))

	button_show=False
	if total_prev > 0 or total_current > 0 or total_positive > 0 or total_negative < 0:
		button_show=True

	context={
	'task_array':task_array,
	'records':records,
	'total_prev':total_prev,
	'total_current':total_current,
	'total_positive':total_positive,
	'total_negative':total_negative,
	'button_show':button_show,
	}
	return render(request,'shop_templates/Item_Return_Process_issue_item_processing_Daily_Summary.html',context)



def Item_Return_Process_issue_item_processing_Day_End_Transaction(request):
	task_array=[]
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	for task in tasks:
			task_array.append(task.task.title)

	processed_by=CustomUser.objects.get(id=request.user.id)
	processed_by=processed_by.username


	form=TransactionPeriod_form(request.POST or None)

	total_prev=0
	total_current=0
	total_positive=0
	total_negative=0
	records=[]
	if request.method == 'POST' and 'btn-fetch' in request.POST:
		period=request.POST.get('transaction_period')

		date_format = '%Y-%m-%d'
		dtObj = datetime.strptime(period, date_format)
		tdate=get_current_date(dtObj)


		records=Daily_Sales_Item_Return_Cash_Flow_Summary.objects.filter(status='UNTREATED').filter(Q(tdate=tdate))

		queryset=  Daily_Sales_Item_Return_Cash_Flow_Summary.objects.filter(status='UNTREATED').filter(Q(tdate=tdate)).aggregate(total_prev_amount=Sum('prev_amount'),total_current_amount=Sum('current_amount'))
		queryset_pos=  Daily_Sales_Item_Return_Cash_Flow_Summary.objects.filter(status='UNTREATED').filter(Q(tdate=tdate) & Q(postive_balance__gt=0)).aggregate(total_balance_amount=Sum('postive_balance'))
		queryset_neg=  Daily_Sales_Item_Return_Cash_Flow_Summary.objects.filter(status='UNTREATED').filter(Q(tdate=tdate) & Q(negative_balance__lt=0)).aggregate(total_balance_amount=Sum('negative_balance'))

		total_prev=queryset['total_prev_amount']
		total_current=queryset['total_current_amount']
		total_positive=queryset_pos['total_balance_amount']
		total_negative=queryset_neg['total_balance_amount']

		if not total_prev:
			total_prev=0

		if not total_current:
			total_current=0

		if not total_positive:
			total_positive=0

		if not total_negative:
			total_negative=0


	if request.method == 'POST' and 'btn-process' in request.POST:
		period=request.POST.get('transaction_period')

		date_format = '%Y-%m-%d'
		dtObj = datetime.strptime(period, date_format)
		tdate=get_current_date(dtObj)


		records=Daily_Sales_Item_Return_Cash_Flow_Summary.objects.filter(status='UNTREATED').filter(Q(tdate=tdate))

		queryset=  Daily_Sales_Item_Return_Cash_Flow_Summary.objects.filter(status='UNTREATED').filter(Q(tdate=tdate)).aggregate(total_prev_amount=Sum('prev_amount'),total_current_amount=Sum('current_amount'))
		queryset_pos=  Daily_Sales_Item_Return_Cash_Flow_Summary.objects.filter(status='UNTREATED').filter(Q(tdate=tdate) & Q(postive_balance__gt=0)).aggregate(total_balance_amount=Sum('postive_balance'))
		queryset_neg=  Daily_Sales_Item_Return_Cash_Flow_Summary.objects.filter(status='UNTREATED').filter(Q(tdate=tdate) & Q(negative_balance__lt=0)).aggregate(total_balance_amount=Sum('negative_balance'))

		total_prev=queryset['total_prev_amount']
		total_current=queryset['total_current_amount']
		total_positive=queryset_pos['total_balance_amount']
		total_negative=queryset_neg['total_balance_amount']

		if not total_prev:
			total_prev=0

		if not total_current:
			total_current=0

		if not total_positive:
			total_positive=0

		if not total_negative:
			total_negative=0


		ticket=get_ticket()
		record=Daily_Sales_Item_Return_Day_End_Transaction(tdate=tdate,description='ITEMS RETURN',prev_amount=total_prev,
															current_amount=total_current,
															postive_balance=total_positive,
															negative_balance=total_negative,
															cash_book=ticket,
															processed_by=processed_by,
															status="UNTREATED").save()




		Daily_Sales_Item_Return_Cash_Flow_Summary.objects.filter(status='UNTREATED').filter(Q(tdate=tdate)).update(status="TREATED",cash_book=ticket)

		balance=shop_cashbook_balance()
		# shop_cashbook_balance
		# shop_cashbook_posting

		particulars="Item returnrd as at " + str(get_current_date(now))
		debit=0
		credit=total_prev
		balance=balance+credit
		ref_no=ticket
		status='ACTIVE'
		tdate=get_current_date(now)
		
		source='ITEM RETURN'

		shop_cashbook_posting(particulars,debit,credit,balance,ref_no,status,tdate,processed_by,source)

		balance=shop_cashbook_balance()
		particulars="Items Purchased as exchange to Items Returned " + str(get_current_date(now))
		debit=total_current
		credit=0
		balance=balance-debit
		ref_no=ticket
		status='ACTIVE'
		tdate=get_current_date(now)
		source='ITEM RETURN'

		shop_cashbook_posting(particulars,debit,credit,balance,ref_no,status,tdate,processed_by,source)
		return HttpResponseRedirect(reverse('shop_home'))

	button_show=False
	if total_prev > 0 or total_current > 0 or total_positive > 0 or total_negative < 0:
		button_show=True

	form.fields['transaction_period'].initial=now
	context={
	'task_array':task_array,
	'records':records,
	'total_prev':total_prev,
	'total_current':total_current,
	'total_positive':total_positive,
	'total_negative':total_negative,
	'button_show':button_show,
	'form':form,
	}
	return render(request,'shop_templates/Daily_Sales_Item_Return_Day_End_Transaction.html',context)


def Item_Return_Process_issue_item_processing_Month_End_Transaction(request):
	task_array=[]
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	for task in tasks:
			task_array.append(task.task.title)

	processed_by=CustomUser.objects.get(id=request.user.id)
	processed_by=processed_by.username


	form=TransactionPeriod_form(request.POST or None)

	total_prev=0
	total_current=0
	total_positive=0
	total_negative=0
	records=[]
	if request.method == 'POST' and 'btn-fetch' in request.POST:
		period=request.POST.get('transaction_period')

		date_format = '%Y-%m-%d'
		dtObj = datetime.strptime(period, date_format)
		tdate=get_current_date(dtObj)


		records=Daily_Sales_Item_Return_Day_End_Transaction.objects.filter(status='UNTREATED').filter(Q(tdate__year=tdate.year) & Q(tdate__month=tdate.month))

		queryset=  Daily_Sales_Item_Return_Day_End_Transaction.objects.filter(status='UNTREATED').filter(Q(tdate__year=tdate.year) & Q(tdate__month=tdate.month)).aggregate(total_prev_amount=Sum('prev_amount'),total_current_amount=Sum('current_amount'))
		queryset_pos=  Daily_Sales_Item_Return_Day_End_Transaction.objects.filter(status='UNTREATED').filter(Q(tdate__year=tdate.year) & Q(tdate__month=tdate.month) & Q(postive_balance__gt=0)).aggregate(total_balance_amount=Sum('postive_balance'))
		queryset_neg=  Daily_Sales_Item_Return_Day_End_Transaction.objects.filter(status='UNTREATED').filter(Q(tdate__year=tdate.year) & Q(tdate__month=tdate.month) & Q(negative_balance__lt=0)).aggregate(total_balance_amount=Sum('negative_balance'))

		total_prev=queryset['total_prev_amount']
		total_current=queryset['total_current_amount']
		total_positive=queryset_pos['total_balance_amount']
		total_negative=queryset_neg['total_balance_amount']

		if not total_prev:
			total_prev=0

		if not total_current:
			total_current=0

		if not total_positive:
			total_positive=0

		if not total_negative:
			total_negative=0


	if request.method == 'POST' and 'btn-process' in request.POST:
		period=request.POST.get('transaction_period')

		date_format = '%Y-%m-%d'
		dtObj = datetime.strptime(period, date_format)
		tdate=get_current_date(dtObj)


		records=Daily_Sales_Item_Return_Day_End_Transaction.objects.filter(status='UNTREATED').filter(Q(tdate=tdate))

		queryset=  Daily_Sales_Item_Return_Day_End_Transaction.objects.filter(status='UNTREATED').filter(Q(tdate__year=tdate.year) & Q(tdate__month=tdate.month)).aggregate(total_prev_amount=Sum('prev_amount'),total_current_amount=Sum('current_amount'))
		queryset_pos=  Daily_Sales_Item_Return_Day_End_Transaction.objects.filter(status='UNTREATED').filter(Q(tdate__year=tdate.year) & Q(tdate__month=tdate.month) & Q(postive_balance__gt=0)).aggregate(total_balance_amount=Sum('postive_balance'))
		queryset_neg=  Daily_Sales_Item_Return_Day_End_Transaction.objects.filter(status='UNTREATED').filter(Q(tdate__year=tdate.year) & Q(tdate__month=tdate.month) & Q(negative_balance__lt=0)).aggregate(total_balance_amount=Sum('negative_balance'))

		total_prev=queryset['total_prev_amount']
		total_current=queryset['total_current_amount']
		total_positive=queryset_pos['total_balance_amount']
		total_negative=queryset_neg['total_balance_amount']

		if not total_prev:
			total_prev=0

		if not total_current:
			total_current=0

		if not total_positive:
			total_positive=0

		if not total_negative:
			total_negative=0


		ticket=get_ticket()
		record=Daily_Sales_Item_Return_Month_End_Transaction(tdate=tdate,description='ITEMS RETURN',prev_amount=total_prev,
															current_amount=total_current,
															postive_balance=total_positive,
															negative_balance=total_negative,
															month_key=ticket,
															processed_by=processed_by,
															status="UNTREATED").save()




		Daily_Sales_Item_Return_Day_End_Transaction.objects.filter(status='UNTREATED').filter(Q(tdate__year=tdate.year) & Q(tdate__month=tdate.month)).update(status="TREATED",month_key=ticket)


		return HttpResponseRedirect(reverse('shop_home'))

	button_show=False
	if total_prev > 0 or total_current > 0 or total_positive > 0 or total_negative < 0:
		button_show=True

	form.fields['transaction_period'].initial=now
	context={
	'task_array':task_array,
	'records':records,
	'total_prev':total_prev,
	'total_current':total_current,
	'total_positive':total_positive,
	'total_negative':total_negative,
	'button_show':button_show,
	'form':form,
	}
	return render(request,'shop_templates/Item_Return_Process_issue_item_processing_Month_End_Transaction.html',context)



def Item_Return_Process_issue_item_processing_Year_End_Transaction(request):
	task_array=[]
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	for task in tasks:
			task_array.append(task.task.title)

	processed_by=CustomUser.objects.get(id=request.user.id)
	processed_by=processed_by.username


	form=TransactionPeriod_form(request.POST or None)

	total_prev=0
	total_current=0
	total_positive=0
	total_negative=0
	records=[]
	if request.method == 'POST' and 'btn-fetch' in request.POST:
		period=request.POST.get('transaction_period')

		date_format = '%Y-%m-%d'
		dtObj = datetime.strptime(period, date_format)
		tdate=get_current_date(dtObj)


		records=Daily_Sales_Item_Return_Month_End_Transaction.objects.filter(status='UNTREATED').filter(Q(tdate__year=tdate.year))

		queryset=  Daily_Sales_Item_Return_Month_End_Transaction.objects.filter(status='UNTREATED').filter(Q(tdate__year=tdate.year)).aggregate(total_prev_amount=Sum('prev_amount'),total_current_amount=Sum('current_amount'))
		queryset_pos=  Daily_Sales_Item_Return_Month_End_Transaction.objects.filter(status='UNTREATED').filter(Q(tdate__year=tdate.year) & Q(postive_balance__gt=0)).aggregate(total_balance_amount=Sum('postive_balance'))
		queryset_neg=  Daily_Sales_Item_Return_Month_End_Transaction.objects.filter(status='UNTREATED').filter(Q(tdate__year=tdate.year) & Q(negative_balance__lt=0)).aggregate(total_balance_amount=Sum('negative_balance'))

		total_prev=queryset['total_prev_amount']
		total_current=queryset['total_current_amount']
		total_positive=queryset_pos['total_balance_amount']
		total_negative=queryset_neg['total_balance_amount']

		if not total_prev:
			total_prev=0

		if not total_current:
			total_current=0

		if not total_positive:
			total_positive=0

		if not total_negative:
			total_negative=0


	if request.method == 'POST' and 'btn-process' in request.POST:
		period=request.POST.get('transaction_period')

		date_format = '%Y-%m-%d'
		dtObj = datetime.strptime(period, date_format)
		tdate=get_current_date(dtObj)


		records=Daily_Sales_Item_Return_Month_End_Transaction.objects.filter(status='UNTREATED').filter(Q(tdate=tdate))

		queryset=  Daily_Sales_Item_Return_Month_End_Transaction.objects.filter(status='UNTREATED').filter(Q(tdate__year=tdate.year)).aggregate(total_prev_amount=Sum('prev_amount'),total_current_amount=Sum('current_amount'))
		queryset_pos=  Daily_Sales_Item_Return_Month_End_Transaction.objects.filter(status='UNTREATED').filter(Q(tdate__year=tdate.year) & Q(postive_balance__gt=0)).aggregate(total_balance_amount=Sum('postive_balance'))
		queryset_neg=  Daily_Sales_Item_Return_Month_End_Transaction.objects.filter(status='UNTREATED').filter(Q(tdate__year=tdate.year) & Q(negative_balance__lt=0)).aggregate(total_balance_amount=Sum('negative_balance'))

		total_prev=queryset['total_prev_amount']
		total_current=queryset['total_current_amount']
		total_positive=queryset_pos['total_balance_amount']
		total_negative=queryset_neg['total_balance_amount']

		if not total_prev:
			total_prev=0

		if not total_current:
			total_current=0

		if not total_positive:
			total_positive=0

		if not total_negative:
			total_negative=0


		ticket=get_ticket()
		record=Daily_Sales_Item_Return_Year_End_Transaction(tdate=tdate,description='ITEMS RETURN',prev_amount=total_prev,
															current_amount=total_current,
															postive_balance=total_positive,
															negative_balance=total_negative,
															year_key=ticket,
															processed_by=processed_by,
															status="UNTREATED").save()




		Daily_Sales_Item_Return_Month_End_Transaction.objects.filter(status='UNTREATED').filter(Q(tdate__year=tdate.year)).update(status="TREATED",year_key=ticket)


		return HttpResponseRedirect(reverse('shop_home'))

	button_show=False
	if total_prev > 0 or total_current > 0 or total_positive > 0 or total_negative < 0:
		button_show=True

	form.fields['transaction_period'].initial=now
	context={
	'task_array':task_array,
	'records':records,
	'total_prev':total_prev,
	'total_current':total_current,
	'total_positive':total_positive,
	'total_negative':total_negative,
	'button_show':button_show,
	'form':form,
	}
	return render(request,'shop_templates/Item_Return_Process_issue_item_processing_Year_End_Transaction.html',context)


def Item_Return_Manage_List_Load(request):
	task_array=[]
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	for task in tasks:
			task_array.append(task.task.title)

	records=Daily_Sales_Item_Return.objects.filter(status='UNTREATED')

	context={
	'task_array':task_array,
	'records':records,

	}
	return render(request,'shop_templates/Item_Return_Manage_List_Load.html',context)



def Item_Return_Manage_List_Delete(request,pk):
	record=Daily_Sales_Item_Return.objects.get(id=pk)
	code=record.sales.product.code
	sale_id=record.sales_id
	stock_update=Stock.objects.filter(code=code).update(quantity=F('quantity')-record.quantity)
	sales=Daily_Sales.objects.filter(id=sale_id).update(quantity_returned=F('quantity_returned')-record.quantity)
	record.delete()
	return HttpResponseRedirect(reverse('Item_Return_Manage_List_Load'))



def stock_status_search(request):
	task_array=[]
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	for task in tasks:
		task_array.append(task.task.title)

	title="Search Stock"
	form = searchForm(request.POST or None)

	return render(request,'shop_templates/stock_status_search.html',{'form':form,'title':title,'task_array':task_array})



def stock_status_list_load(request):
	task_array=[]
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	for task in tasks:
		task_array.append(task.task.title)


	if request.method == "POST":
		form = searchForm(request.POST)
		status = 'ACTIVE'

		records=Stock.objects.filter(Q(code__icontains=form['title'].value()) | Q(item_name__icontains=form['title'].value()) | Q(details__icontains=form['title'].value()))

		context={
		'task_array':task_array,
		'records':records,

		}
		return render(request,'shop_templates/stock_status_list_load.html',context)



def stock_status_list_details(request,pk):
	form=stock_status_list_details_Form(request.POST or None)
	task_array=[]
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	for task in tasks:
		task_array.append(task.task.title)

	product = Stock.objects.get(id=pk)

	records=[]
	if request.method == "POST":
		start_date=request.POST.get("start_date")
		stop_date=request.POST.get("stop_date")


		date_format = '%Y-%m-%d'
		start_date = datetime.strptime(start_date, date_format)
		stop_date = datetime.strptime(stop_date, date_format)

		# records=Daily_Sales.objects.filter(tdate__range=[start_date,stop_date])

		records=Daily_Sales.objects.filter(product=product,tdate__range=[start_date,stop_date]).order_by('tdate')

	form.fields['start_date'].initial=now
	form.fields['stop_date'].initial=now
	context={
	'task_array':task_array,
	'records':records,
	'product':product,
	'form':form,
	}
	return render(request,'shop_templates/stock_status_list_details.html',context)


def monthly_deductions_salary_institution_select_Aux(request):
	task_array=[]
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	for task in tasks:
		task_array.append(task.task.title)

	status='ACTIVE'
	records=SalaryInstitution.objects.all()
	transaction_period=TransactionPeriods.objects.get(status=status)
	transaction_period=transaction_period.transaction_period

	context={
	'task_array':task_array,
	'records':records,
	'transaction_period':transaction_period,
	}
	return render(request,'shop_templates/monthly_deductions_salary_institution_select_Aux.html',context)


def monthly_individual_deductions_generate_Aux(request,pk):

	processed_by=CustomUser.objects.get(id=request.user.id)
	processed_by=processed_by.username


	tdate=get_current_date(now)


	form=shop_monthly_deductions_generate_form(request.POST or None)
	task_array=[]
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	for task in tasks:
		task_array.append(task.task.title)

	transaction=TransactionTypes.objects.get(name='SHOP')
	transaction_period=TransactionPeriods.objects.get(status='ACTIVE')
	transaction_period=transaction_period.transaction_period

	processing_status="UNPROCESSED"
	status='UNTREATED'
	salary_institution=SalaryInstitution.objects.get(id=pk)
	schedule_status='UNSCHEDULED'
	schedule_status1='SCHEDULED'


	if MonthlyGeneratedTransactions.objects.filter(salary_institution=salary_institution,transaction_period=transaction_period,transaction=transaction).exists():
		messages.error(request,'Transactions already Generated for this Period')
		return HttpResponseRedirect(reverse('monthly_deductions_salary_institution_select'))

	# members=members_credit_sales_summary.objects.filter(processing_status=processing_status,trans_code__member__salary_institution=salary_institution,status=status)
	members=members_shop_credit_loans.objects.filter(member__salary_institution=salary_institution,schedule_status=schedule_status).filter(Q(balance__lt=0))

	if not members:
		messages.error(request,'No Available Record for this Transactions')
		return HttpResponseRedirect(reverse('monthly_deductions_salary_institution_select'))


	queryset=  members_shop_credit_loans.objects.filter(member__salary_institution=salary_institution,schedule_status=schedule_status).filter(Q(balance__lt=0)).aggregate(total_cash=Sum('balance'))
	grand_total=queryset['total_cash']

	if grand_total:
		grand_total=grand_total
	else:
		grand_total=0



	if request.method == 'POST':

		for member in members:
			MonthlyShopdeductionList(member=member.member,
											transaction_period=transaction_period,
											transaction=transaction,
											account_number=member.loan_number,
											amount=member.loan_amount,
											amount_deducted=0,balance=member.loan_amount,
											status=status,
											processing_status=processing_status,
											salary_institution=salary_institution,
											processed_by=processed_by,
											tdate=tdate
											).save()

			schedule_status="SCHEDULED"

			members_shop_credit_loans.objects.filter(loan_number=member.loan_number).update(schedule_status=schedule_status1)

		MonthlyGeneratedTransactions(tdate=tdate,processed_by=processed_by,salary_institution=salary_institution,transaction_period=transaction_period,transaction=transaction,transaction_status=status).save()

		return HttpResponseRedirect(reverse('monthly_deductions_salary_institution_select'))


	date_time_obj = get_current_date(transaction_period)


	form.fields['transaction_period'].initial=date_time_obj.strftime("%a,%d %b, %Y")
	context={
	'task_array':task_array,
	'members':members,
	'transaction_period':transaction_period,
	'salary_institution':salary_institution,
	'form':form,
	'grand_total':abs(grand_total),
	}
	return render(request,'shop_templates/monthly_individual_deductions_generate_Aux.html',context)





def monthly_grouped_deductions_salary_institution_select_Aux(request):
	task_array=[]
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	for task in tasks:
		task_array.append(task.task.title)

	status='ACTIVE'
	records=SalaryInstitution.objects.all()
	transaction_period=TransactionPeriods.objects.get(status=status)
	transaction_period=transaction_period.transaction_period
	context={
	'task_array':task_array,
	'records':records,
	'transaction_period':transaction_period,
	}
	return render(request,'shop_templates/monthly_grouped_deductions_salary_institution_select_Aux.html',context)


def monthly_grouped_deductions_generated_Aux(request,pk):
	task_array=[]
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	for task in tasks:
		task_array.append(task.task.title)

	status='ACTIVE'

	salary_institution=SalaryInstitution.objects.get(id=pk)
	transaction_period=TransactionPeriods.objects.get(status=status)
	transaction_period=transaction_period.transaction_period


	
	tdate=get_current_date(now)
	processed_by=CustomUser.objects.get(id=request.user.id)
	processed_by=processed_by.username

	transaction=TransactionTypes.objects.get(code=600)
	
	MonthlyShopdeductionList_Aux.objects.filter(transaction_period=transaction_period,member__salary_institution=salary_institution,processing_status='UNPROCESSED',status='TREATED').update(status='UNTREATED')
	records=MonthlyShopdeductionList_Aux.objects.filter(transaction_period=transaction_period,salary_institution=salary_institution,processing_status='UNPROCESSED',status='UNTREATED').order_by('member__member_id').values_list('member__member_id','member__ippis_no','member__admin__last_name','member__admin__first_name','member__middle_name').distinct()
	
	if not records:
		messages.error(request,"No Record Found for this Transaction or It's Already Generated")
		return HttpResponseRedirect(reverse('monthly_grouped_deductions_salary_institution_select_Aux'))

	deduction_array=[]
	grand_total=0
	for record in records:

		queryset=  MonthlyShopdeductionList_Aux.objects.filter(member__member_id=record[0],transaction_period=transaction_period).aggregate(total_cash=Sum('amount'))
		total_amount=queryset['total_cash']
		grand_total=float(grand_total) + float(total_amount)
		deduction_array.append((record[0][13:],record[2] + " " + record[3]+ " " + record[4],record[1],total_amount))


	if request.method == 'POST':
		if MonthlyShopGroupGeneratedTransactions.objects.filter(transaction=transaction,salary_institution=salary_institution,transaction_period=transaction_period).exists():
			messages.error(request,"This Transaction is Already Generated")
			return HttpResponseRedirect(reverse('monthly_grouped_deductions_generated_Aux',args=(pk,)))

		for record in records:
			member=Members.objects.get(member_id=record[0])

			queryset=  MonthlyShopdeductionList_Aux.objects.filter(member__member_id=record[0],transaction_period=transaction_period).aggregate(total_cash=Sum('amount'))
			total_amount=queryset['total_cash']


			MonthlyShopdeductionListGenerated(member=member,
															coop_amount=total_amount,
															account_amount=0,balance=0,
															transaction_period=transaction_period,
															processing_status='UNPROCESSED',
															processed_by=processed_by,
															status='UNTREATED',
															salary_institution=salary_institution,
															tdate=tdate).save()

		MonthlyShopGroupGeneratedTransactions(transaction=transaction,
										salary_institution=salary_institution,
										transaction_period=transaction_period,
										processed_by=processed_by,
										transaction_status='UNTREATED',
										tdate=tdate
										).save()

		MonthlyDeductionGenerationHeading(salary_institution=salary_institution,transaction_period=transaction_period,heading="SHOP",status='UNTREATED').save()

		MonthlyShopdeductionList_Aux.objects.filter(transaction_period=transaction_period,salary_institution=salary_institution,processing_status='UNPROCESSED',status='UNTREATED').update(status='TREATED')

		return HttpResponseRedirect(reverse('monthly_grouped_deductions_salary_institution_select_Aux'))

	context={
	'task_array':task_array,
	'records':deduction_array,
	'transaction_period':transaction_period,
	'salary_institution':salary_institution,
	'grand_total':grand_total,
	}
	return render(request,'shop_templates/monthly_grouped_deductions_generated_Aux.html',context)



def monthly_deductions_salary_institution_select(request):
	task_array=[]
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	for task in tasks:
		task_array.append(task.task.title)

	status='ACTIVE'
	records=SalaryInstitution.objects.all()
	transaction_period=TransactionPeriods.objects.get(status=status)
	transaction_period=transaction_period.transaction_period

	context={
	'task_array':task_array,
	'records':records,
	'transaction_period':transaction_period,
	}
	return render(request,'shop_templates/monthly_deductions_salary_institution_select.html',context)


def monthly_individual_deductions_generate(request,pk):

	processed_by=CustomUser.objects.get(id=request.user.id)
	processed_by=processed_by.username


	tdate=get_current_date(now)


	form=shop_monthly_deductions_generate_form(request.POST or None)
	task_array=[]
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	for task in tasks:
		task_array.append(task.task.title)

	transaction=TransactionTypes.objects.get(name='SHOP')
	transaction_period=TransactionPeriods.objects.get(status='ACTIVE')
	transaction_period=transaction_period.transaction_period

	processing_status="UNPROCESSED"
	status='UNTREATED'
	salary_institution=SalaryInstitution.objects.get(id=pk)
	schedule_status='UNSCHEDULED'
	schedule_status1='SCHEDULED'


	if MonthlyGeneratedTransactions.objects.filter(salary_institution=salary_institution,transaction_period=transaction_period,transaction=transaction).exists():
		messages.error(request,'Transactions already Generated for this Period')
		return HttpResponseRedirect(reverse('monthly_deductions_salary_institution_select'))

	# members=members_credit_sales_summary.objects.filter(processing_status=processing_status,trans_code__member__salary_institution=salary_institution,status=status)
	members=members_shop_credit_loans.objects.filter(member__salary_institution=salary_institution,schedule_status=schedule_status).filter(Q(balance__lt=0))

	if not members:
		messages.error(request,'No Available Record for this Transactions')
		return HttpResponseRedirect(reverse('monthly_deductions_salary_institution_select'))


	queryset=  members_shop_credit_loans.objects.filter(member__salary_institution=salary_institution,schedule_status=schedule_status).filter(Q(balance__lt=0)).aggregate(total_cash=Sum('balance'))
	grand_total=queryset['total_cash']

	if grand_total:
		grand_total=grand_total
	else:
		grand_total=0



	if request.method == 'POST':

		for member in members:
			MonthlyShopdeductionList(member=member.member,
											transaction_period=transaction_period,
											transaction=transaction,
											account_number=member.loan_number,
											amount=member.loan_amount,
											amount_deducted=0,balance=member.loan_amount,
											status=status,
											processing_status=processing_status,
											salary_institution=salary_institution,
											processed_by=processed_by,
											tdate=tdate
											).save()

			schedule_status="SCHEDULED"

			members_shop_credit_loans.objects.filter(loan_number=member.loan_number).update(schedule_status=schedule_status1)

		MonthlyGeneratedTransactions(tdate=tdate,processed_by=processed_by,salary_institution=salary_institution,transaction_period=transaction_period,transaction=transaction,transaction_status=status).save()

		return HttpResponseRedirect(reverse('monthly_deductions_salary_institution_select'))


	date_time_obj = get_current_date(transaction_period)


	form.fields['transaction_period'].initial=date_time_obj.strftime("%a,%d %b, %Y")
	context={
	'task_array':task_array,
	'members':members,
	'transaction_period':transaction_period,
	'salary_institution':salary_institution,
	'form':form,
	'grand_total':abs(grand_total),
	}
	return render(request,'shop_templates/monthly_individual_deductions_generate.html',context)




def monthly_grouped_deductions_salary_institution_select(request):
	task_array=[]
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	for task in tasks:
		task_array.append(task.task.title)

	status='ACTIVE'
	records=SalaryInstitution.objects.all()
	transaction_period=TransactionPeriods.objects.get(status=status)
	transaction_period=transaction_period.transaction_period
	context={
	'task_array':task_array,
	'records':records,
	'transaction_period':transaction_period,
	}
	return render(request,'shop_templates/monthly_grouped_deductions_salary_institution_select.html',context)


def monthly_grouped_deductions_generated(request,pk):
	task_array=[]
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	for task in tasks:
		task_array.append(task.task.title)

	status='ACTIVE'
	transaction_status='UNTREATED'
	transaction_status1='TREATED'
	salary_institution=SalaryInstitution.objects.get(id=pk)
	transaction_period=TransactionPeriods.objects.get(status=status)
	transaction_period=transaction_period.transaction_period

	processing_status='UNPROCESSED'
	processing_status1='PROCESSED'
	transaction=TransactionTypes.objects.get(name='SHOP')
	tdate=get_current_date(now)
	processed_by=CustomUser.objects.get(id=request.user.id)
	processed_by=processed_by.username


	records=MonthlyShopdeductionList.objects.filter(transaction_period=transaction_period,transaction=transaction,member__salary_institution=salary_institution,processing_status=processing_status,status=transaction_status).order_by('member__member_id').values_list('member__member_id','member__ippis_no','member__admin__last_name','member__admin__first_name','member__middle_name').distinct()

	if not records:
		messages.error(request,"No Record Found for this Transaction or It's Already Generated")
		return HttpResponseRedirect(reverse('monthly_grouped_deductions_salary_institution_select'))

	deduction_array=[]
	grand_total=0
	for record in records:

		queryset=  MonthlyShopdeductionList.objects.filter(member__member_id=record[0],transaction_period=transaction_period,transaction=transaction).aggregate(total_cash=Sum('amount'))
		total_amount=queryset['total_cash']
		grand_total=float(grand_total) + float(total_amount)
		deduction_array.append((record[0][13:],record[2] + " " + record[3]+ " " + record[4],record[1],total_amount))


	if request.method == 'POST':
		if MonthlyShopGroupGeneratedTransactions.objects.filter(transaction=transaction,salary_institution=salary_institution,transaction_period=transaction_period).exists():
			messages.error(request,"This Transaction is Already Generated")
			return HttpResponseRedirect(reverse('monthly_grouped_deductions_generated',args=(pk,)))

		for record in records:
			member=Members.objects.get(member_id=record[0])

			queryset=  MonthlyShopdeductionList.objects.filter(member__member_id=record[0],transaction_period=transaction_period,transaction=transaction).aggregate(total_cash=Sum('amount'))
			total_amount=queryset['total_cash']


			MonthlyShopdeductionListGenerated(member=member,
															coop_amount=total_amount,
															account_amount=0,balance=0,
															transaction_period=transaction_period,
															processing_status=processing_status,
															processed_by=processed_by,
															status=transaction_status,
															salary_institution=salary_institution,
															tdate=tdate).save()

		MonthlyShopGroupGeneratedTransactions(transaction=transaction,
										salary_institution=salary_institution,
										transaction_period=transaction_period,
										processed_by=processed_by,
										transaction_status=transaction_status,
										tdate=tdate
										).save()

		MonthlyDeductionGenerationHeading(salary_institution=salary_institution,transaction_period=transaction_period,heading="SHOP",status=transaction_status).save()

		MonthlyShopdeductionList.objects.filter(transaction_period=transaction_period,transaction=transaction,member__salary_institution=salary_institution,processing_status=processing_status,status=transaction_status).update(status=transaction_status1)

		return HttpResponseRedirect(reverse('monthly_grouped_deductions_salary_institution_select'))

	context={
	'task_array':task_array,
	'records':deduction_array,
	'transaction_period':transaction_period,
	'salary_institution':salary_institution,
	'grand_total':grand_total,
	}
	return render(request,'shop_templates/monthly_grouped_deductions_generated.html',context)



def Shop_Account_Deductions_Upload_salary_institution_select(request):
	task_array=[]
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	for task in tasks:
		task_array.append(task.task.title)


	status='ACTIVE'
	records=SalaryInstitution.objects.all()
	transaction_period=TransactionPeriods.objects.get(status=status)
	transaction_period=transaction_period.transaction_period

	context={
	'task_array':task_array,
	'records':records,
	'transaction_period':transaction_period,
	}
	return render(request,'shop_templates/Shop_Account_Deductions_Upload_salary_institution_select.html',context)



def Shop_Account_Deductions_Upload_Load(request,pk):
	task_array=[]
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	for task in tasks:
		task_array.append(task.task.title)

	processed_by=CustomUser.objects.get(id=request.user.id)
	processed_by=processed_by.username


	status='ACTIVE'
	salary_institution=SalaryInstitution.objects.get(id=pk)
	transaction_period=TransactionPeriods.objects.get(status=status)
	transaction_period=transaction_period.transaction_period

	processing_status='UNPROCESSED'
	processing_status1='PROCESSED'
	schedule_status='SCHEDULED'
	schedule_status1='UNSCHEDULED'
	transaction_status='UNTREATED'
	transaction_status1='TREATED'
	tdate=get_current_date(now)

	records=MonthlyShopdeductionListGenerated.objects.filter(transaction_period=transaction_period,salary_institution=salary_institution,processing_status=processing_status)

	if not records:
		messages.error(request,'No record found')
		return HttpResponseRedirect(reverse('Shop_Account_Deductions_Upload_salary_institution_select'))


	if request.method == 'POST':

		for record in records:

			total_amount_deducted=record.account_amount

			items=members_shop_credit_loans.objects.filter(member__ippis_no=record.member.ippis_no,member__salary_institution=salary_institution,schedule_status=schedule_status).filter(Q(balance__lt=0)).order_by('id')

			for item in items:
				if MonthlyShopdeductionList.objects.filter(account_number=item.loan_number).exists():
					item1=MonthlyShopdeductionList.objects.get(account_number=item.loan_number)


					if float(total_amount_deducted) <= float(item1.amount):

						item.amount_paid=float(item.amount_paid) + float(total_amount_deducted)
						item.balance=float(item.balance) + float(total_amount_deducted)
						item.schedule_status=schedule_status1
						item.save()


						if float(item.balance) == 0:
							item.status=transaction_status1
							item.save()


						item1.amount_deducted=total_amount_deducted
						item1.balance=float(item1.amount)-float(total_amount_deducted)
						item1.processing_status=processing_status1
						total_amount_deducted=float(total_amount_deducted)-float(item1.amount)
						item1.save()



					elif float(total_amount_deducted) > float(item1.amount):
						item.amount_paid=float(item.amount_paid) + float(item1.amount)
						item.balance=float(item.balance) + float(item1.amount)
						item.schedule_status=schedule_status1
						item.save()


						if float(item.balance) == 0:
							item.status=transaction_status1
							item.save()

						item1.amount_deducted=item1.amount
						item1.balance=0
						item1.processing_status=processing_status1
						total_amount_deducted=float(total_amount_deducted)-float(item1.amount)
						item1.save()


			ledger_balance=get_cooperative_shop_balance(record.member)


			particulars=str(transaction_period.transaction_period) + " Month's Deduction"
			debit=0
			credit=record.account_amount
			balance=float(ledger_balance) + float(record.account_amount)


			cooperative_shop_ledger_posting(transaction_status,record.member,particulars,debit,credit,balance,tdate,processed_by)

			# CooperativeShopLedger(status=transaction_status,member=record.member,particulars=particulars,debit=debit,credit=credit,balance=balance,tdate=tdate,processed_by=processed_by).save()

		MonthlyShopdeductionListGenerated.objects.filter(transaction_period=transaction_period,salary_institution=salary_institution,processing_status=processing_status).update(processing_status=processing_status1)
		messages.success(request,'Transaction Complete Successfully')
		return HttpResponseRedirect(reverse('Shop_Account_Deductions_Upload_salary_institution_select'))


	context={
	'task_array':task_array,
	'records':records,
	'salary_institution':salary_institution,
	'transaction_period':transaction_period,
	}
	return render(request,'shop_templates/Shop_Account_Deductions_Upload_Load.html',context)


def Members_Credit_sales_Cash_Deposit_search(request):
	task_array=[]
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	for task in tasks:
		task_array.append(task.task.title)

	title="Search Members for Cash Deposit"
	form = searchForm(request.POST or None)
	return render(request,'shop_templates/Members_Credit_sales_Cash_Deposit_search.html',{'form':form,'title':title,'task_array':task_array})


def Members_Credit_sales_Cash_Deposit_list_load(request):
	task_array=[]
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	for task in tasks:
		task_array.append(task.task.title)

	title="Membership Purchases"
	if request.method == "POST":
		form = searchForm(request.POST)
		status="ACTIVE"
		if not form['title'].value():
			messages.error(request,'Please enter search')
			return HttpResponseRedirect(reverse('Members_Credit_sales_Cash_Deposit_search'))

		members=searchMembers(form['title'].value(),status)

		if not members:
			messages.error(request,'No record found')
			return HttpResponseRedirect(reverse('Members_Credit_sales_Cash_Deposit_search'))

		context={
		'task_array':task_array,

		'members':members,
		'title':title,
		}
		return render(request,'shop_templates/Members_Credit_sales_Cash_Deposit_list_load.html',context)


def Members_Credit_sales_Cash_Deposit_Details(request,pk):
	task_array=[]
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	for task in tasks:
		task_array.append(task.task.title)

	form = Members_Credit_sales_Cash_Deposit_Details_form(request.POST or None)
	status = 'ACTIVE'
	status1 = 'TREATED'
	processing_status="UNPROCESSED"

	member=Members.objects.get(id=pk)
	transaction=TransactionTypes.objects.get(code='903')

	if request.method == "POST":

		current_date=request.POST.get('payment_date')
		date_format = '%Y-%m-%d'
		tdate = get_current_date(now)

		processed_by=CustomUser.objects.get(id=request.user.id)
		processed_by=processed_by.username


		payment_reference=request.POST.get('payment_reference')
		amount_paid = request.POST.get("amount_paid")
		amount_distributed=0
		amount_balance= float(amount_paid)

		particulars="CASH DEPOSIT/" + str(payment_reference) + " ON " + str(tdate)

		narrations=request.POST.get('narrations')
		bank_id=request.POST.get('bank')
		bank = Banks.objects.get(id=bank_id)


		coop_account_id=request.POST.get('account')
		coop_account = CooperativeBankAccounts.objects.get(id=coop_account_id)


		if float(amount_paid) <=0:
			messages.error(request,"Invalid Amount Specification")
			return HttpResponseRedirect(reverse('Members_Credit_sales_Cash_Deposit_Details',args=(pk,)))


		if transaction.receipt_type == 'AUTO':
			receipt=generate_shop_receipt('AUTO',0)
		elif transaction.receipt_type == 'MANUAL':
			receipt_id=request.POST.get('receipt')
			if receipt_id:
				receipt=generate_shop_receipt('AUTO',receipt_id)
			else:
				messages.error(request,"Receipt Missing")
				return HttpResponseRedirect(reverse('Members_Credit_sales_Cash_Deposit_Details',args=(pk,)))
		else:
			messages.error(request,"Invalid Receipt Format")
			return HttpResponseRedirect(reverse('Members_Credit_sales_Cash_Deposit_Details',args=(pk,)))

		record=Cooperative_Shop_Cash_Deposit(processing_status=processing_status,bank=bank,coop_account=coop_account,member=member,narrations=particulars,payment_reference=payment_reference,amount_paid=amount_paid,amount_distributed=amount_distributed,amount_balance=amount_balance,receipt=receipt,processed_by=processed_by,status=status,tdate=tdate)
		record.save()


		return HttpResponseRedirect(reverse('Members_Credit_sales_Cash_Deposit_search'))

	form.fields['payment_date'].initial=now
	context={
	'task_array':task_array,
	'form':form,
	'member':member,
	'transaction':transaction,
	}
	return render(request,'shop_templates/Members_Credit_sales_Cash_Deposit_Details.html',context)


def Members_Credit_sales_Cash_Deposit_Distributions_list_load(request):
	task_array=[]
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	for task in tasks:
		task_array.append(task.task.title)

	status='ACTIVE'

	members=Cooperative_Shop_Cash_Deposit.objects.filter(Q(amount_paid__gt=F("amount_distributed"))).filter(status=status)

	context={
	'task_array':task_array,

	'members':members,

	}
	return render(request,'shop_templates/Members_Credit_sales_Cash_Deposit_Distributions_list_load.html',context)


def Members_Credit_sales_Cash_Deposit_Distributions_Process(request,pk):
	form=Members_Credit_sales_Cash_Deposit_Distributions_Process_form(request.POST or None)
	task_array=[]
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	for task in tasks:
		task_array.append(task.task.title)

	processing_status="PROCESSED"
	status="UNTREATED"
	status2="TREATED"
	status1 = "INACTIVE"
	processed_by=CustomUser.objects.get(id=request.user.id)
	processed_by=processed_by.username


	member=Cooperative_Shop_Cash_Deposit.objects.get(id=pk)
	receipt=member.receipt
	selected_member=Members.objects.get(id=member.member_id)

	records=Cooperative_Shop_Cash_Deposit_Distributions.objects.filter(member=member.member,receipt=member,status=status)

	amount=member.amount_paid
	if request.method == 'POST':

		tdate=get_current_date(now)
		amount_distributed=0

		if not records:
			messages.error(request,'No Transaction selected for Distribution for this Member')
			return HttpResponseRedirect(reverse('Members_Credit_sales_Cash_Deposit_Distributions_Process',args=(pk,)))


		if CooperativeShopLedger.objects.filter(account_number=str(600)+str(selected_member.get_member_Id)).exists():
			pass
		else:
			messages.error(request,'No record found in the Shop ledger for this Member')
			return HttpResponseRedirect(reverse('Members_Credit_sales_Cash_Deposit_Distributions_Process',args=(pk,)))

		for record in records:

			if record.amount_due < amount:

				record.amount_distributed = record.amount_due
				record.status = status2
				amount_distributed=amount_distributed+record.amount_due
				amount=amount-record.amount_due
				record.save()

				if record.source == "FIRST":
					loan_update=members_shop_credit_loans.objects.get(loan_number=record.loan_number.loan_number)
					loan_update.amount_paid=amount_distributed
					loan_update.balance=loan_update.balance + amount_distributed
					loan_update.status=status2
					loan_update.save()
				elif record.source == 'SECOND':
					loan_update=members_credit_sales_summary.objects.get(trans_code__ticket=record.loan_number)

					loan_update.amount_paid=amount_distributed
					loan_update.balance=loan_update.balance + amount_distributed
					loan_update.save()

					if loan_update.balance >=0:
						loan_update.status=processing_status
						loan_update.save()

				ledger = CooperativeShopLedger.objects.filter(account_number=str(600)+str(selected_member.get_member_Id)).last()
				balance=ledger.balance+amount_distributed
				ledger.status=status2
				ledger.save()

				particulars="Cash Deposit for transaction with: " + str(record.loan_number.loan_number)
				queryset = CooperativeShopLedger(tdate=tdate,member=selected_member,account_number=str(600)+str(selected_member.get_member_Id),particulars=particulars,debit=0,credit=amount_distributed,balance=balance,receipt=receipt,processed_by=processed_by,status=status)
				queryset.save()

			elif record.amount_due >= amount:

				record.amount_distributed = amount
				record.status = status2
				amount_distributed=amount_distributed+amount
				amount=amount-amount
				record.save()

				if record.source == "FIRST":
					loan_update=members_shop_credit_loans.objects.get(loan_number=record.loan_number)
					loan_update.amount_paid=amount_distributed
					loan_update.balance=loan_update.balance + amount_distributed
					loan_update.save()

					if loan_update.balance >=0:
						loan_update.status=status2
						loan_update.save()



				elif record.source == 'SECOND':
					loan_update=members_credit_sales_summary.objects.get(trans_code__ticket=record.loan_number)

					loan_update.amount_paid=amount_distributed
					loan_update.balance=loan_update.balance + amount_distributed
					loan_update.save()

					if loan_update.balance >=0:
						loan_update.processing_status=processing_status
						loan_update.save()

				ledger = CooperativeShopLedger.objects.filter(account_number=str(600)+str(selected_member.get_member_Id)).last()
				balance=ledger.balance+amount_distributed
				ledger.status=status2
				ledger.save()

				particulars="Cash Deposit for transaction with: " + str(record.loan_number)
				queryset = CooperativeShopLedger(tdate=tdate,member=selected_member,account_number=str(600)+str(selected_member.get_member_Id), particulars=particulars,debit=0,credit=amount_distributed,balance=balance,receipt=receipt,processed_by=processed_by,status=status)
				queryset.save()



		if member.amount_paid==amount_distributed:
			member.status=status1

		member.amount_distributed=amount_distributed
		member.amount_balance=member.amount_paid-amount_distributed
		member.save()


		Cooperative_Shop_Cash_Deposit.objects.filter(Q(amount_paid=F("amount_distributed")) & Q(id=pk)).update(processing_status=processing_status)
		return HttpResponseRedirect(reverse('Members_Credit_sales_Cash_Deposit_Distributions_list_load'))


	button_show=False
	if records:
		button_show=True

	form.fields['amount_paid'].initial=member.amount_paid
	form.fields['amount_distributed'].initial=member.amount_distributed
	form.fields['balance_amount'].initial=member.amount_balance
	context={
	'task_array':task_array,
	'form':form,
	'member':member,
	'records':records,
	'button_show':button_show,
	}
	return render(request,'shop_templates/Members_Credit_sales_Cash_Deposit_Distributions_Process.html',context)


def Members_Credit_sales_Cash_Deposit_Distributions_Add(request,pk):
	task_array=[]
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	for task in tasks:
		task_array.append(task.task.title)


	schedule_status='UNSCHEDULED'

	member=Cooperative_Shop_Cash_Deposit.objects.get(id=pk)
	records=members_shop_credit_loans.objects.filter(member=member.member,schedule_status=schedule_status).filter(Q(balance__lt=0))

	context={
	'task_array':task_array,
	'records':records,
	'member':member,

	}
	return render(request,'shop_templates/Members_Credit_sales_Cash_Deposit_Distributions_Add.html',context)


def Members_Credit_sales_Cash_Deposit_Distributions_Transaction_Select(request,pk,member_id):
	task_array=[]
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	for task in tasks:
		task_array.append(task.task.title)

	member=Cooperative_Shop_Cash_Deposit.objects.get(id=member_id)
	#
	record=members_shop_credit_loans.objects.get(id=pk)
	status='UNTREATED'
	processed_by=CustomUser.objects.get(id=request.user.id)
	processed_by=processed_by.username
	tdate=get_current_date(now)

	if Cooperative_Shop_Cash_Deposit_Distributions.objects.filter(member=record.member,
												loan_number=record,
												receipt=member,
												status=status).exists():
		pass
	else:
		Cooperative_Shop_Cash_Deposit_Distributions(member=record.member,
													loan_number=record,
													amount_due=abs(record.balance),
													amount_distributed=0,
													receipt=member,
													status=status,
													processed_by=processed_by,tdate=tdate).save()
	return HttpResponseRedirect(reverse('Members_Credit_sales_Cash_Deposit_Distributions_Process',args=(member_id,)))


def Members_Credit_sales_Cash_Deposit_Distributions_Transaction_Drop(request,pk,member_id):
	task_array=[]
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	for task in tasks:
		task_array.append(task.task.title)

	member=Cooperative_Shop_Cash_Deposit.objects.get(id=member_id)

	Cooperative_Shop_Cash_Deposit_Distributions.objects.get(id=pk).delete()

	return HttpResponseRedirect(reverse('Members_Credit_sales_Cash_Deposit_Distributions_Process',args=(member_id,)))



def Members_Credit_sales_Cash_Deposit_Distributions_Add_2nd_level(request,pk):
	task_array=[]
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	for task in tasks:
		task_array.append(task.task.title)


	processing_status='UNPROCESSED'

	member=Cooperative_Shop_Cash_Deposit.objects.get(id=pk)
	records=members_credit_sales_summary.objects.filter(trans_code__member=member.member,processing_status=processing_status)

	context={
	'task_array':task_array,
	'records':records,
	'member':member,

	}
	return render(request,'shop_templates/Members_Credit_sales_Cash_Deposit_Distributions_Add_2nd_level.html',context)



def Members_Credit_sales_Cash_Deposit_Distributions_Transaction_2nd_Level_Select(request,pk,member_id):
	task_array=[]
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	for task in tasks:
		task_array.append(task.task.title)

	member=Cooperative_Shop_Cash_Deposit.objects.get(id=member_id)
	#
	record=members_credit_sales_summary.objects.get(id=pk)
	status='UNTREATED'
	processed_by=CustomUser.objects.get(id=request.user.id)
	processed_by=processed_by.username

	tdate=get_current_date(now)

	if Cooperative_Shop_Cash_Deposit_Distributions.objects.filter(member=record.trans_code.member,
												loan_number=record.trans_code.ticket,
												receipt=member,
												source='SECOND',
												status=status).exists():
		pass
	else:


		Cooperative_Shop_Cash_Deposit_Distributions(member=record.trans_code.member,
													loan_number=record.trans_code.ticket,
													amount_due=abs(record.balance),
													amount_distributed=0,
													receipt=member,
													status=status,
													source='SECOND',
													processed_by=processed_by,tdate=tdate).save()
	return HttpResponseRedirect(reverse('Members_Credit_sales_Cash_Deposit_Distributions_Add_2nd_level',args=(member_id,)))


def Cash_Deposit_Summary(request):
	task_array=[]
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	for task in tasks:
		task_array.append(task.task.title)

	form=Cash_Deposit_Summary_form(request.POST or None)
	processed_by = CustomUser.objects.get(id=request.user.id)
	processed_by=processed_by.username

	status = 'UNTREATED'
	status1 = 'TREATED'
	status2 = 'ACTIVE'

	records=[]
	total_amount=0
	button_show=False
	if request.method == "POST" and 'btn_fetch' in request.POST:

		current_date=request.POST.get('current_date')
		date_format = '%Y-%m-%d'
		tdate = datetime.strptime(current_date, date_format)

		tyear=int(tdate.year)
		tmonth=int(tdate.month)
		tday=int(tdate.day)

		# records=Cooperative_Shop_Cash_Deposit.objects.filter(tdate__year=tyear,tdate__month=tmonth,tdate__day=tday,processed_by=processed_by,status=status)

		records=shopCashDepositFilter(tdate,processed_by,"UNTREATED")
		total_amount=calculateTotalCashDeposit(tdate,processed_by,"UNTREATED")


		if records:
			button_show=True


	if request.method == 'POST' and 'btn_submit' in request.POST:
		current_date=request.POST.get('current_date')

		date_format = '%Y-%m-%d'
		tdate = datetime.strptime(current_date, date_format)

		tyear=int(tdate.year)
		tmonth=int(tdate.month)
		tday=int(tdate.day)

		records=shopCashDepositFilter(tdate,processed_by,"UNTREATED")
		total_amount=calculateTotalCashDeposit(tdate,processed_by,"UNTREATED")


		sales_category='BANK DEPOSIT'

		processed_by=CustomUser.objects.get(id=request.user.id)
		processed_by=processed_by.username

		record=Daily_Cash_Deposit_Summary(tdate=tdate,description='BANK DEPOSIT',amount=total_amount,processed_by=processed_by,status=status)
		record.save()

		Cooperative_Shop_Cash_Deposit.objects.filter(tdate__year=tyear,tdate__month=tmonth,tdate__day=tday,processed_by=processed_by,status2="UNTREATED").update(status2="TREATED")

		return HttpResponseRedirect(reverse('Cash_Deposit_Summary'))


	form.fields['current_date'].initial=now


	context={
	'task_array':task_array,
	'form':form,
	'records':records,
	'button_show':button_show,
	'total_amount':total_amount,
	}
	return render(request,'shop_templates/Cash_Deposit_Summary.html',context)



def Cash_Deposit_Day_End_Transactions(request):
	task_array=[]
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	for task in tasks:
		task_array.append(task.task.title)

	form=Cash_Deposit_Summary_form(request.POST or None)
	processed_by = CustomUser.objects.get(id=request.user.id)
	processed_by=processed_by.username

	status = 'UNTREATED'
	status1 = 'TREATED'
	status2 = 'ACTIVE'

	records=[]
	total_amount=0
	button_show=False
	if request.method == "POST" and 'btn_fetch' in request.POST:

		current_date=request.POST.get('current_date')
		date_format = '%Y-%m-%d'
		tdate = datetime.strptime(current_date, date_format)

		tyear=int(tdate.year)
		tmonth=int(tdate.month)
		tday=int(tdate.day)

		records=Daily_Cash_Deposit_Summary.objects.filter(tdate__year=tyear,tdate__month=tmonth,tdate__day=tday,status=status)
		queryset=Daily_Cash_Deposit_Summary.objects.filter(tdate__year=tyear,tdate__month=tmonth,tdate__day=tday,status=status).aggregate(total_cost=Sum('amount'))
		total_amount=queryset['total_cost']


		if records:
			button_show=True


	if request.method == 'POST' and 'btn_submit' in request.POST:
		current_date=request.POST.get('current_date')

		date_format = '%Y-%m-%d'
		tdate = datetime.strptime(current_date, date_format)

		tyear=int(tdate.year)
		tmonth=int(tdate.month)
		tday=int(tdate.day)

		records=Daily_Cash_Deposit_Summary.objects.filter(tdate__year=tyear,tdate__month=tmonth,tdate__day=tday,status=status)
		queryset=Daily_Cash_Deposit_Summary.objects.filter(tdate__year=tyear,tdate__month=tmonth,tdate__day=tday,status=status).aggregate(total_cost=Sum('amount'))
		total_amount=queryset['total_cost']


		sales_category='BANK DEPOSIT'

		ticket=get_ticket()

		cash_book_balance=shop_cashbook_balance()

		particulars="Cash Deposit on  " + str(tdate)
		debit=total_amount
		credit=0
		balance=float(cash_book_balance)+float(total_amount)
		ref_no=ticket
		source="BANK DEPOSIT"

		shop_cashbook_posting(particulars,debit,credit,balance,ref_no,status2,tdate,processed_by,source)

		record=Daily_Cash_Deposit_Day_End_Transaction(tdate=tdate,description='BANK DEPOSIT',amount=total_amount,processed_by=processed_by,status=status,cash_book=ticket)
		record.save()

		Daily_Cash_Deposit_Summary.objects.filter(tdate__year=tyear,tdate__month=tmonth,tdate__day=tday,status=status).update(status=status1,cash_book=ticket)

		return HttpResponseRedirect(reverse('Cash_Deposit_Day_End_Transactions'))

	form.fields['current_date'].initial=now

	context={
	'task_array':task_array,
	'form':form,
	'records':records,
	'button_show':button_show,
	'total_amount':total_amount,
	}
	return render(request,'shop_templates/Cash_Deposit_Day_End_Transactions.html',context)



def Cash_Deposit_Month_End_Transactions(request):
	task_array=[]
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	for task in tasks:
		task_array.append(task.task.title)

	form=Cash_Deposit_Summary_form(request.POST or None)
	processed_by = CustomUser.objects.get(id=request.user.id)
	processed_by=processed_by.username

	status = 'UNTREATED'
	status1 = 'TREATED'
	status2 = 'ACTIVE'

	records=[]
	total_amount=0
	button_show=False
	if request.method == "POST" and 'btn_fetch' in request.POST:

		current_date=request.POST.get('current_date')
		date_format = '%Y-%m-%d'
		tdate = datetime.strptime(current_date, date_format)

		tyear=int(tdate.year)
		tmonth=int(tdate.month)
		tday=int(tdate.day)

		records=Daily_Cash_Deposit_Day_End_Transaction.objects.filter(tdate__year=tyear,tdate__month=tmonth,status=status)
		queryset=Daily_Cash_Deposit_Day_End_Transaction.objects.filter(tdate__year=tyear,tdate__month=tmonth,status=status).aggregate(total_cost=Sum('amount'))
		total_amount=queryset['total_cost']

		if records:
			button_show=True


	if request.method == 'POST' and 'btn_submit' in request.POST:
		current_date=request.POST.get('current_date')

		date_format = '%Y-%m-%d'
		tdate = datetime.strptime(current_date, date_format)

		tyear=int(tdate.year)
		tmonth=int(tdate.month)
		tday=int(tdate.day)

		records=Daily_Cash_Deposit_Day_End_Transaction.objects.filter(tdate__year=tyear,tdate__month=tmonth,status=status)
		queryset=Daily_Cash_Deposit_Day_End_Transaction.objects.filter(tdate__year=tyear,tdate__month=tmonth,status=status).aggregate(total_cost=Sum('amount'))
		total_amount=queryset['total_cost']


		sales_category='BANK DEPOSIT'

		ticket=get_ticket()


		record=Daily_Cash_Deposit_Month_End_Transaction(tdate=tdate,description='BANK DEPOSIT',amount=total_amount,processed_by=processed_by,status=status,month_end_code=ticket)
		record.save()

		Daily_Cash_Deposit_Day_End_Transaction.objects.filter(tdate__year=tyear,tdate__month=tmonth,status=status).update(status=status1,month_end_code=ticket)

		return HttpResponseRedirect(reverse('Cash_Deposit_Month_End_Transactions'))


	form.fields['current_date'].initial=now


	context={
	'task_array':task_array,
	'form':form,
	'records':records,
	'button_show':button_show,
	'total_amount':total_amount,
	}
	return render(request,'shop_templates/Cash_Deposit_Month_End_Transactions.html',context)



def Cash_Deposit_Year_End_Transactions(request):
	task_array=[]
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	for task in tasks:
		task_array.append(task.task.title)

	form=Cash_Deposit_Summary_form(request.POST or None)
	processed_by = CustomUser.objects.get(id=request.user.id)
	processed_by=processed_by.username


	status = 'UNTREATED'
	status1 = 'TREATED'
	status2 = 'ACTIVE'

	records=[]
	total_amount=0
	button_show=False
	if request.method == "POST" and 'btn_fetch' in request.POST:

		current_date=request.POST.get('current_date')
		date_format = '%Y-%m-%d'
		tdate = datetime.strptime(current_date, date_format)

		tyear=int(tdate.year)
		tmonth=int(tdate.month)
		tday=int(tdate.day)

		records=Daily_Cash_Deposit_Month_End_Transaction.objects.filter(tdate__year=tyear,status=status)
		queryset=Daily_Cash_Deposit_Month_End_Transaction.objects.filter(tdate__year=tyear,status=status).aggregate(total_cost=Sum('amount'))
		total_amount=queryset['total_cost']

		if records:
			button_show=True


	if request.method == 'POST' and 'btn_submit' in request.POST:
		current_date=request.POST.get('current_date')

		date_format = '%Y-%m-%d'
		tdate = datetime.strptime(current_date, date_format)

		tyear=int(tdate.year)
		tmonth=int(tdate.month)
		tday=int(tdate.day)

		records=Daily_Cash_Deposit_Month_End_Transaction.objects.filter(tdate__year=tyear,status=status)
		queryset=Daily_Cash_Deposit_Month_End_Transaction.objects.filter(tdate__year=tyear,status=status).aggregate(total_cost=Sum('amount'))
		total_amount=queryset['total_cost']


		sales_category='BANK DEPOSIT'

		ticket=get_ticket()

		record=Daily_Cash_Deposit_Year_End_Transaction(tdate=tdate,description='BANK DEPOSIT',amount=total_amount,processed_by=processed_by,status=status,year_end_code=ticket)
		record.save()

		Daily_Cash_Deposit_Month_End_Transaction.objects.filter(tdate__year=tyear,status=status).update(status=status1,year_end_code=ticket)

		return HttpResponseRedirect(reverse('Cash_Deposit_Year_End_Transactions'))


	form.fields['current_date'].initial=now
	context={
	'task_array':task_array,
	'form':form,
	'records':records,
	'button_show':button_show,
	'total_amount':total_amount,
	}
	return render(request,'shop_templates/Cash_Deposit_Year_End_Transactions.html',context)



def Stock_Status(request):
	task_array=[]
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	for task in tasks:
		task_array.append(task.task.title)

	records=Stock.objects.filter(quantity__lt=F('re_order_level'))

	# Entry.objects.filter(number_of_comments__gt=F('number_of_pingbacks'))


	context={
	'task_array':task_array,
	'records':records,
	}
	return render(request,'shop_templates/Stock_Status.html',context)


def Supplier_add(request):
	task_array=[]
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	for task in tasks:
		task_array.append(task.task.title)

	form = Suppliers_add_form(request.POST or None)
	suppliers = Suppliers.objects.all()
	tdate=get_current_date(now)
	if request.method == 'POST':
		if form.is_valid():
			prefix = request.POST.get('prefix')
			name = request.POST.get('name')
			if Suppliers.objects.filter(name=name).exists():
				messages.info(request,'Record Already Exist')
				return HttpResponseRedirect(reverse('Supplier_add'))
			else:
				record=Suppliers(tdate=tdate,name=name,prefix=prefix)
				record.save()
				return HttpResponseRedirect(reverse('Supplier_add'))



	context={
	'task_array':task_array,
	'form':form,
	'suppliers':suppliers,
	}
	return render(request,'shop_templates/Supplier_add.html',context)


def Supplier_edit(request,pk):
	task_array=[]
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	for task in tasks:
		task_array.append(task.task.title)

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


	context={
	'task_array':task_array,
	'form':form,
	'supplier':supplier,
	}
	return render(request,'shop_templates/Supplier_edit.html',context)


def Supplier_Branches_add(request,pk):
	task_array=[]
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	for task in tasks:
		task_array.append(task.task.title)

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



	context={
	'task_array':task_array,
		'supplier':supplier,
		'form':form,
		'branches':branches,
	}
	return render(request,'shop_templates/Supplier_Branches_add.html',context)


def Supplier_Branches_edit(request,pk):
	task_array=[]
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	for task in tasks:
		task_array.append(task.task.title)

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



	context={
	'task_array':task_array,
		'supplier':branch.supplier,
		'form':form,
		'branch':branch,
	}
	return render(request,'shop_templates/Supplier_Branches_edit.html',context)



def Supplier_Personnel_add(request,pk):
	task_array=[]
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	for task in tasks:
		task_array.append(task.task.title)

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



	context={
	'task_array':task_array,
		'form':form,
		'supplier':supplier,
		'personnels':personnels,
	}
	return render(request,'shop_templates/Supplier_Personnel_add.html',context)


def Supplier_Personnel_Edit(request,pk):
	task_array=[]
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	for task in tasks:
		task_array.append(task.task.title)

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


	form.fields['name'].initial=personnel.name
	form.fields['phone'].initial=personnel.phone
	context={
	'task_array':task_array,
		'form':form,
		'personnel':personnel,

	}
	return render(request,'shop_templates/Supplier_Personnel_Edit.html',context)


def Stock_Taken(request):
	task_array=[]
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	for task in tasks:
		task_array.append(task.task.title)

	tdate=get_current_date(now)
	processed_by=CustomUser.objects.get(id=request.user.id)
	processed_by=processed_by.username

	records = Stock.objects.filter(Q(quantity__gt=0)).order_by('code').values_list('code','item_name','details','quantity','unit_cost_price','category').distinct()
	record_array=[]
	total_amount=0
	total_item=0
	for record in records:
		record_array.append((record[0],record[1],record[2],record[3],record[4],float(record[3])*float(record[4]),record[5],"MAIN"))
		total_amount=float(total_amount)+(float(record[3])*float(record[4]))
		total_item=int(total_item)+int(record[3])

	records = Stock_Auction.objects.filter(Q(quantity__gt=0)).order_by('stock__code').values_list('stock__code','stock__item_name','stock__details','quantity','stock__unit_cost_price','stock__category').distinct()

	for record in records:
		record_array.append((record[0],record[1],record[2],record[3],record[4],float(record[3])*float(record[4]),record[5],'AUCTION'))
		total_amount=float(total_amount)+(float(record[3])*float(record[4]))
		total_item=int(total_item)+int(record[3])

	if request.method == "POST":

		for record in record_array:
			if float(record[4]) <= 0 and float(record[3]) > 0:
				messages.error(request,'Please Some Product do not have Cost price while they have quantity, please Update')
				return HttpResponseRedirect(reverse('Stock_Taken'))


		if Stock_History.objects.all().exists():
			pass
		else:

			cash_book_balance=shop_cashbook_balance()
			particulars="Initial Stock Taken as at " + str(get_current_date(now))
			debit=0
			credit=total_amount
			balance=float(cash_book_balance) + credit
			ref_no=get_ticket()
			status='ACTIVE'
			shop_cashbook_posting(particulars,debit,credit,balance,ref_no,"ACTIVE",tdate,processed_by,"STOCK TAKEN")


		for record in record_array:
			category= record[6]
			Stock_History(category=category,
						code=record[0],
						item_name=record[1],
						details=record[2],
						quantity=record[3],
						unit_cost_price=record[4],
						total=record[5],
						sources=record[7],
						processed_by=processed_by,
						tdate=tdate).save()
		return HttpResponseRedirect(reverse('shop_home'))

	context={
	'task_array':task_array,
	'record_array':record_array,
	'total_item':total_item,
	'total_amount':total_amount,
	}
	return render(request,'shop_templates/Stock_Taken.html',context)



def Stock_Without_Prices(request):
	task_array=[]
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	for task in tasks:
		task_array.append(task.task.title)

	records = Stock.objects.filter(Q(unit_cost_price__lte=0))
	context={
	'task_array':task_array,
	'records':records,

	}
	return render(request,'shop_templates/Stock_Without_Prices.html',context)

def Stock_Without_Prices_Update(request,pk):
	task_array=[]
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	for task in tasks:
		task_array.append(task.task.title)

	form=Stock_Without_Prices_Update_Form(request.POST or None)
	record = Stock.objects.get(id=pk)

	if request.method == 'POST':
		price=request.POST.get("unit_cost_price")
		record.unit_cost_price=price
		record.save()

		return HttpResponseRedirect(reverse('Stock_Without_Prices'))

	form.fields['unit_selling_price'].initial=record.unit_selling_price
	context={
	'task_array':task_array,
	'record':record,
	'form':form,
	}
	return render(request,'shop_templates/Stock_Without_Prices_Update.html',context)



def Product_Purchase(request):
	task_array=[]
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	for task in tasks:
		task_array.append(task.task.title)

	status='UNTREATED'
	form = Product_Purchase_form(request.POST or None)
	suppliers=Suppliers.objects.all()
	records = Purchase_Header.objects.filter(status=status)


	if request.method == "POST":
		status = 'UNTREATED'
		approval_status='PENDING'
		processed_by=CustomUser.objects.get(id=request.user.id)
		processed_by=processed_by.username

		branch_id=request.POST.get('branch')
		branch = Suppliers_Branches.objects.get(id=branch_id)
		prefix = branch.supplier.prefix

		invoice_id=request.POST.get('invoice')
		invoice=prefix + '-' + str(invoice_id)
		invoice_date=request.POST.get('invoice_date')
		record=Purchase_Header(approval_status=approval_status,status=status,branch=branch,invoice=invoice,invoice_date=invoice_date,processed_by=processed_by)
		record.save()
		return HttpResponseRedirect(reverse('Product_Purchase'))

	form.fields['invoice_date'].initial = now


	context={
	'task_array':task_array,
	'suppliers':suppliers,
	'records':records,
	'form':form,
	}
	return render(request,'shop_templates/Product_Purchase.html',context)



def Product_Purchase_Add_Supplier(request):
	task_array=[]
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	for task in tasks:
		task_array.append(task.task.title)

	form = Suppliers_add_form(request.POST or None)
	suppliers = Suppliers.objects.all()

	if request.method == 'POST':
		tdate=get_current_date(now)
		if form.is_valid():
			prefix = request.POST.get('prefix')
			name = request.POST.get('name')
			if Suppliers.objects.filter(name=name).exists():
				messages.info(request,'Record Already Exist')
				return HttpResponseRedirect(reverse('Product_Purchase_Add_Supplier'))
			else:
				record=Suppliers(tdate=tdate,name=name,prefix=prefix)
				record.save()
				return HttpResponseRedirect(reverse('Product_Purchase_Add_Supplier'))



	context={
	'task_array':task_array,
	'form':form,
	'suppliers':suppliers,

	}
	return render(request,'shop_templates/Product_Purchase_Add_Supplier.html',context)


def Product_Purchase_Add_Supplier_Personnel(request,pk,return_pk):
	task_array=[]
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	for task in tasks:
		task_array.append(task.task.title)

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
	'task_array':task_array,
	'supplier':supplier,
	'form':form,
	'personnels':personnels,
	}
	return render(request,'shop_templates/Supplier_Personnel_add.html',context)


def Product_Purchase_Details(request,pk):
	task_array=[]
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	for task in tasks:
		task_array.append(task.task.title)

	status='TREATED'

	invoice=Purchase_Header.objects.get(id=pk)
	invoice_items = Purchases_Temp.objects.filter(purchase=invoice)

	queryset=Purchases_Temp.objects.filter(purchase=invoice).aggregate(total_cost=Sum('total_cost'),total_item=Sum('quantity'))
	total_cost=queryset['total_cost']
	total_item=queryset['total_item']

	products = Stock.objects.all()



	personnels=Suppliers_Reps.objects.filter(suppliers=invoice.branch.supplier)

	if request.method == "POST":

		if request.POST.get('personnel'):
			personnel_id=request.POST.get('personnel')
			personnel=Suppliers_Reps.objects.get(id=personnel_id)


			invoice.personnel=personnel
			invoice.total_amount=total_cost
			# invoice.tdate=tdate
			invoice.status=status
			invoice.save()

			# record_update=Purchases_Temp.objects.filter(purchase=invoice).update(tdate=tdate)
			return HttpResponseRedirect(reverse('Product_Purchase'))

		messages.info(request,'Please select Personnel')
		return HttpResponseRedirect(reverse('Product_Purchase_Details',args=(pk,)))


	context={
	'task_array':task_array,
	'invoice':invoice,
	'products':products,
	'items':invoice_items,
	'personnels':personnels,
	'total_cost':total_cost,
	'total_item':total_item,
	# 'form':form,
	}
	return render(request,'shop_templates/Product_Purchase_Details.html',context)



def Product_Purchase_Details_Select(request,pk,invoice_id):
	task_array=[]
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	for task in tasks:
		task_array.append(task.task.title)

	status='UNTREATED'
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



	form.fields['quantity'].initial=1
	form.fields['code'].initial=product.code
	form.fields['item_name'].initial=product.item_name
	form.fields['unit_selling_price'].initial=product.unit_selling_price
	form.fields['unit_cost'].initial=product.unit_cost_price

	context={
	'task_array':task_array,
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
	task_array=[]
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	for task in tasks:
		task_array.append(task.task.title)

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



	form.fields['code'].initial=product.product.code
	form.fields['item_name'].initial=product.product.item_name
	form.fields['quantity'].initial=product.quantity
	form.fields['unit_cost'].initial=product.cost_price
	form.fields['unit_selling_price'].initial=product.selling_price

	context={
	'task_array':task_array,
	'product':product,
	'form':form,

	}
	return render(request,'shop_templates/Product_Purchase_Details_Select_Edit.html',context)


def Product_Purchase_Addnew_Item(request,pk):
	task_array=[]
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	for task in tasks:
		task_array.append(task.task.title)

	form=Stock_Update_form(request.POST or None)
	if request.method=="POST":
		lock_status='LOCKED'
		code=get_stock_code()
		category_id=request.POST.get('category')
		category=ProductCategory.objects.get(id=category_id)

		details=request.POST.get('details').upper()
		item_name=request.POST.get('item_name').upper()
		quantity=request.POST.get('quantity')
		re_order_level=request.POST.get('re_order_level')
		no_in_pack=request.POST.get('no_in_pack')
		unit_selling_price=request.POST.get('unit_selling_price')

		if not item_name:
			messages.error(request,'Missing Product Name')
			return HttpResponseRedirect(reverse('Product_Purchase_Addnew_Item',args=(pk,)))

		if not item_name:
			messages.error(request,'Missing Product Name')
			return HttpResponseRedirect(reverse('Product_Purchase_Addnew_Item',args=(pk,)))

		if not quantity:
			messages.error(request,'Missing quantity')
			return HttpResponseRedirect(reverse('Product_Purchase_Addnew_Item',args=(pk,)))

		if not re_order_level:
			messages.error(request,'Missing Re-Order Level')
			return HttpResponseRedirect(reverse('Product_Purchase_Addnew_Item',args=(pk,)))

		if not no_in_pack:
			messages.error(request,'Missing Mumber in Pack')
			return HttpResponseRedirect(reverse('Product_Purchase_Addnew_Item',args=(pk,)))

		if not unit_selling_price:
			messages.error(request,'Missing Selling Price')
			return HttpResponseRedirect(reverse('Product_Purchase_Addnew_Item',args=(pk,)))


		record=Stock(category=category,code=code,item_name=item_name,details=details,quantity=quantity,re_order_level=re_order_level,no_in_pack=no_in_pack,unit_selling_price=unit_selling_price,lock_status=lock_status)
		record.save()
		messages.success(request,"Record Added Successfully")
		return HttpResponseRedirect(reverse('Product_Purchase_Details',args=(pk,)))


	context={
	'task_array':task_array,
	'form':form,
	}
	return render(request,'shop_templates/Product_Purchase_Addnew_Item.html',context)

def Purchase_Tracking_Manage(request):
	task_array=[]
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	for task in tasks:
		task_array.append(task.task.title)

	processed_by=CustomUser.objects.get(id=request.user.id)
	processed_by=processed_by.username


	approval_status="PENDING"
	status="TREATED"
	records=Purchase_Header.objects.filter(approval_status=approval_status,status=status,processed_by=processed_by)

	context={
	'task_array':task_array,
	'records':records,
	}
	return render(request,'shop_templates/Purchase_Tracking_Manage.html',context)


def Purchase_Tracking_Details(request,pk):
	task_array=[]
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	for task in tasks:
		task_array.append(task.task.title)

	records = Purchases_Temp.objects.filter(purchase=pk)
	queryset=purchaseTempTotal(pk)
	total_cost=queryset[0]
	total_item=queryset[1]

	cost={
	'total_cost':total_cost,
	'total_item':total_item,
	}

	invoice=[]
	if records:
		invoice=records[0].purchase.invoice

	context={
	'task_array':task_array,
	'records':records,
	'invoice':invoice,
	'cost':cost,
	}
	return render(request,'shop_templates/Purchase_Tracking_Details.html',context)


def Purchase_Tracking_Details_Update(request,pk):
	task_array=[]
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	for task in tasks:
		task_array.append(task.task.title)

	form=Product_Purchase_Select_form(request.POST or None)
	record=Purchases_Temp.objects.get(id=pk)

	form.fields['quantity'].initial=record.quantity
	form.fields['unit_cost'].initial=record.cost_price
	form.fields['unit_selling_price'].initial=record.selling_price



	if request.method == 'POST':
		quantity = request.POST.get('quantity')
		cost_price = request.POST.get('unit_cost')
		selling_price = request.POST.get('unit_selling_price')
		total_cost= float(quantity) * float(cost_price)

		record.quantity=quantity
		record.cost_price=cost_price
		record.selling_price=selling_price
		record.total_cost=total_cost
		record.save()

		queryset=purchaseTempTotal(record.purchase)
		# Purchases_Temp.objects.filter(purchase__invoice=record.purchase.invoice).aggregate(total_cost=Sum('total_cost'),total_item=Sum('quantity'))

		total_cost=queryset[0]
		total_item=queryset[1]

		Purchase_Header.objects.filter(invoice=record.purchase.invoice).update(total_amount=total_cost)

		return HttpResponseRedirect(reverse('Purchase_Tracking_Details',args=(record.purchase_id,)))
	context={
	'task_array':task_array,
	'form':form,
	'record':record,
	}
	return render(request,'shop_templates/Purchase_Tracking_Details_Update.html',context)


def Purchase_Tracking_Invoice_Date_Update(request,pk):
	task_array=[]
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	for task in tasks:
		task_array.append(task.task.title)

	form=Purchase_Tracking_Invoice_Date_Update_form(request.POST or None)
	record = Purchase_Header.objects.get(id=pk)
	if request.method == 'POST':
		invoice=request.POST.get('invoice')
		purchase_date=request.POST.get('purchase_date')


		date_format = '%Y-%m-%d'
		tdate = datetime.strptime(purchase_date, date_format)


		record.invoice=invoice
		record.invoice_date=tdate
		record.save()

		return HttpResponseRedirect(reverse('Purchase_Tracking_Manage'))

	form.fields['invoice'].initial=record.invoice
	form.fields['purchase_date'].initial =record.invoice_date



	context={
	'task_array':task_array,
	'form':form,
	}
	return render(request,'shop_templates/Purchase_Tracking_Invoice_Date_Update.html',context)



def Purchase_Tracking_Invoice_Delete(request,pk):
	record = Purchase_Header.objects.get(id=pk)
	record.delete()
	return HttpResponseRedirect(reverse('Purchase_Tracking_Manage'))

def Purchase_Certification_List_load(request):
	task_array=[]
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	for task in tasks:
		task_array.append(task.task.title)

	processed_by=CustomUser.objects.get(id=request.user.id)
	processed_by=processed_by.username

	status='TREATED'
	approval_status='PENDING'
	records=Purchase_Header.objects.filter(~Q(processed_by=processed_by)).filter(status=status,approval_status=approval_status)


	context={
	'task_array':task_array,
	'records':records,
	}
	return render(request,'shop_templates/Purchase_Certification_List_load.html',context)


def Purchase_Certification_item_Preview(request,pk):
	task_array=[]
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	for task in tasks:
		task_array.append(task.task.title)

	record=Purchase_Header.objects.get(id=pk)
	items=Purchases_Temp.objects.filter(purchase=record)


	queryset= purchaseTempTotal(record) #Purchases_Temp.objects.filter(purchase=record).aggregate(total_cost=Sum('total_cost'),total_item=Sum('quantity'))
	total_cost=queryset[0]
	total_item=queryset[1]

	button_show	=False
	if items:
		button_show=True

	context={
	'task_array':task_array,
	'items':items,
	'record':record,
	'total_cost':total_cost,
	'total_item':total_item,
	'button_show':button_show,
	}
	return render(request,'shop_templates/Purchase_Certification_item_Preview.html',context)


def Purchase_Certification_item_Preview_Processed(request,pk):
	task_array=[]
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	for task in tasks:
		task_array.append(task.task.title)

	tdate=get_current_date(now)
	status='UNTREATED'
	status1='APPROVED'
	record=Purchase_Header.objects.get(id=pk)
	items=Purchases_Temp.objects.filter(purchase=record)
	for item in items:
		stock_record = Purchases(purchase=item.purchase,
			product=item.product,
			quantity=item.quantity,
			cost_price=item.cost_price,
			total_cost=item.total_cost,
			selling_price=item.selling_price,
			tdate=tdate,
			status=status,
			)
		stock_record.save()

		stock_update=Stock.objects.get(code=item.product.code)
		stock_update.quantity=int(stock_update.quantity) + int(item.quantity)
		stock_update.unit_selling_price=item.selling_price
		stock_update.unit_cost_price=item.cost_price
		stock_update.save()

	Purchases_Temp.objects.filter(purchase=record).delete()
	record.approval_status=status1
	record.save()
	return HttpResponseRedirect(reverse('Purchase_Certification_List_load'))



def Purchase_Certification_item_Preview_Remove(request,pk):
	item=Purchases_Temp.objects.get(id=pk)
	return_pk=item.purchase.pk
	item.delete()
	return HttpResponseRedirect(reverse('Purchase_Certification_item_Preview',args=(return_pk,)))


def Purchase_Certification_item_Add_Item(request,pk):
	task_array=[]
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	for task in tasks:
		task_array.append(task.task.title)

	products=Stock.objects.all()
	invoice=Purchase_Header.objects.get(id=pk)
	items=Purchases_Temp.objects.filter(purchase=pk)


	queryset=Purchases_Temp.objects.filter(purchase=pk).aggregate(total_cost=Sum('total_cost'),total_item=Sum('quantity'))

	total_cost=queryset['total_cost']
	total_item=queryset['total_item']

	context={
	'task_array':task_array,
	'products':products,
	'invoice':invoice,
	'items':items,
	'total_cost':total_cost,
	'total_item':total_item,
	}
	return render(request,'shop_templates/Purchase_Certification_item_Add_Item.html',context)



def Purchase_Certification_Product_Purchase_Details_Select(request,pk,invoice_id):
	task_array=[]
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	for task in tasks:
		task_array.append(task.task.title)

	status='UNTREATED'
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



	form.fields['code'].initial=product.code
	form.fields['item_name'].initial=product.item_name
	form.fields['unit_selling_price'].initial=product.unit_selling_price

	context={
	'task_array':task_array,
	'invoice':invoice,
	'product':product,
	'form':form,

	}
	return render(request,'shop_templates/Purchase_Certification_Product_Purchase_Details_Select.html',context)


def Purchase_Certification_item_Preview_Reload(request,pk):
	return HttpResponseRedirect(reverse('Purchase_Certification_item_Preview',args=(pk,)))


def Purchase_Certification_item_Add_Stock(request,pk):
	task_array=[]
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	for task in tasks:
		task_array.append(task.task.title)

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


	context={
	'task_array':task_array,
	'form':form,
	}
	return render(request,'shop_templates/Product_Purchase_Addnew_Item.html',context)


def Purchase_Certification_item_Edit(request,pk):
	task_array=[]
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	for task in tasks:
		task_array.append(task.task.title)

	form = Product_Purchase_Select_form(request.POST or None)

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
	'task_array':task_array,
	'form':form,
	'product':product,
	}
	return render(request,'shop_templates/Purchase_Certification_item_Edit.html',context)



def Product_Purchase_Day_End_Transaction(request):
	task_array=[]
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	for task in tasks:
		task_array.append(task.task.title)

	status='UNTREATED'
	status1='TREATED'
	status2='ACTIVE'
	processed_by=CustomUser.objects.get(id=request.user.id)
	processed_by=processed_by.username

	tdate=get_current_date(now)

	form=Product_Purchase_Day_End_Transaction_form(request.POST or None)
	records=[]
	total_cost=[]
	total_item=[]
	if request.method == 'POST' and 'btn-fetch' in request.POST:
		period=request.POST.get('period')

		date_format = '%Y-%m-%d'
		dtObj = datetime.strptime(period, date_format)
		current_date=get_current_date(dtObj)


		records=Purchases.objects.filter(Q(tdate=current_date) & Q(status=status))

		queryset=Purchases.objects.filter(Q(tdate=current_date) & Q(status=status)).aggregate(total_cost=Sum('total_cost'),total_item=Sum('quantity'))
		total_cost=queryset['total_cost']
		total_item=queryset['total_item']

	if request.method == 'POST' and 'btn-process' in request.POST:
		period=request.POST.get('period')

		date_format = '%Y-%m-%d'
		dtObj = datetime.strptime(period, date_format)
		current_date=get_current_date(dtObj)


		records=Purchases.objects.filter(Q(tdate=current_date) & Q(status=status))
		queryset=Purchases.objects.filter(Q(tdate=current_date) & Q(status=status)).aggregate(total_cost=Sum('total_cost'),total_item=Sum('quantity'))
		total_cost=queryset['total_cost']
		total_item=queryset['total_item']

		ticket=get_ticket()

		cash_book_balance=shop_cashbook_balance()

		particulars="Purchases on " + str(tdate)
		debit=0
		credit=total_cost
		balance=float(cash_book_balance)+float(total_cost)
		ref_no=ticket
		source="PURCHASES"


		Purchases_Day_End_Transaction(quantity=total_item,total_cost=total_cost,status=status,tdate=tdate,cash_book=ticket).save()
		shop_cashbook_posting(particulars,debit,credit,balance,ref_no,status2,tdate,processed_by,source)
		Purchases.objects.filter(Q(tdate=current_date) & Q(status=status)).update(status=status1,cash_book=ticket)

		return HttpResponseRedirect(reverse('Product_Purchase_Day_End_Transaction'))

	button_show=False
	if records:
		button_show=True

	form.fields['period'].initial=now
	context={
	'task_array':task_array,
	'records':records,
	'form':form,
	'button_show':button_show,
	'total_cost':total_cost,
	'total_item':total_item,
	}
	return render(request,'shop_templates/Product_Purchase_Day_End_Transaction.html',context)





def Product_Purchase_Month_End_Transaction(request):
	task_array=[]
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	for task in tasks:
		task_array.append(task.task.title)

	status='UNTREATED'
	status1='TREATED'
	status2='ACTIVE'
	processed_by=CustomUser.objects.get(id=request.user.id)
	processed_by=processed_by.username

	tdate=get_current_date(now)

	form=Product_Purchase_Day_End_Transaction_form(request.POST or None)
	records=[]
	total_cost=[]
	total_item=[]
	if request.method == 'POST' and 'btn-fetch' in request.POST:
		period=request.POST.get('period')

		date_format = '%Y-%m-%d'
		dtObj = datetime.strptime(period, date_format)
		current_date=get_current_date(dtObj)


		records=Purchases_Day_End_Transaction.objects.filter(Q(tdate__month=current_date.month) & Q(tdate__year=current_date.year) & Q(status=status))

		queryset=Purchases_Day_End_Transaction.objects.filter(Q(tdate__month=current_date.month) & Q(tdate__year=current_date.year) & Q(status=status)).aggregate(total_cost=Sum('total_cost'),total_item=Sum('quantity'))
		total_cost=queryset['total_cost']
		total_item=queryset['total_item']

	if request.method == 'POST' and 'btn-process' in request.POST:
		period=request.POST.get('period')

		date_format = '%Y-%m-%d'
		dtObj = datetime.strptime(period, date_format)
		current_date=get_current_date(dtObj)


		records=Purchases_Day_End_Transaction.objects.filter(Q(tdate__month=current_date.month) & Q(tdate__year=current_date.year) & Q(status=status))
		queryset=Purchases_Day_End_Transaction.objects.filter(Q(tdate__month=current_date.month) & Q(tdate__year=current_date.year) & Q(status=status)).aggregate(total_cost=Sum('total_cost'),total_item=Sum('quantity'))
		total_cost=queryset['total_cost']
		total_item=queryset['total_item']

		ticket=get_ticket()



		Purchases_Month_End_Transaction(quantity=total_item,total_cost=total_cost,status=status,tdate=tdate,month_key=ticket).save()

		Purchases_Day_End_Transaction.objects.filter(Q(tdate__month=current_date.month) & Q(tdate__year=current_date.year) & Q(status=status)).update(status=status1,month_key=ticket)

		return HttpResponseRedirect(reverse('Product_Purchase_Month_End_Transaction'))

	button_show=False
	if records:
		button_show=True

	form.fields['period'].initial=now
	context={
	'task_array':task_array,
	'records':records,
	'form':form,
	'button_show':button_show,
	'total_cost':total_cost,
	'total_item':total_item,
	}
	return render(request,'shop_templates/Product_Purchase_Month_End_Transaction.html',context)



def Product_Purchase_Year_End_Transaction(request):
	task_array=[]
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	for task in tasks:
		task_array.append(task.task.title)

	status='UNTREATED'
	status1='TREATED'
	status2='ACTIVE'
	processed_by=CustomUser.objects.get(id=request.user.id)
	processed_by=processed_by.username

	tdate=get_current_date(now)

	form=Product_Purchase_Day_End_Transaction_form(request.POST or None)
	records=[]
	total_cost=[]
	total_item=[]
	if request.method == 'POST' and 'btn-fetch' in request.POST:
		period=request.POST.get('period')

		date_format = '%Y-%m-%d'
		dtObj = datetime.strptime(period, date_format)
		current_date=get_current_date(dtObj)


		records=Purchases_Month_End_Transaction.objects.filter(Q(tdate__year=current_date.year) & Q(status=status))

		queryset=Purchases_Month_End_Transaction.objects.filter(Q(tdate__year=current_date.year) & Q(status=status)).aggregate(total_cost=Sum('total_cost'),total_item=Sum('quantity'))
		total_cost=queryset['total_cost']
		total_item=queryset['total_item']


	if request.method == 'POST' and 'btn-process' in request.POST:
		period=request.POST.get('period')

		date_format = '%Y-%m-%d'
		dtObj = datetime.strptime(period, date_format)
		current_date=get_current_date(dtObj)


		records=Purchases_Month_End_Transaction.objects.filter(Q(tdate__year=current_date.year) & Q(status=status))
		queryset=Purchases_Month_End_Transaction.objects.filter(Q(tdate__year=current_date.year) & Q(status=status)).aggregate(total_cost=Sum('total_cost'),total_item=Sum('quantity'))
		total_cost=queryset['total_cost']
		total_item=queryset['total_item']

		ticket=get_ticket()



		Purchases_Year_End_Transaction(quantity=total_item,total_cost=total_cost,status=status,tdate=tdate,year_key=ticket).save()

		Purchases_Month_End_Transaction.objects.filter(Q(tdate__year=current_date.year) & Q(status=status)).update(status=status1,year_key=ticket)

		return HttpResponseRedirect(reverse('Product_Purchase_Year_End_Transaction'))

	button_show=False
	if records:
		button_show=True

	form.fields['period'].initial=now
	context={
	'task_array':task_array,
	'records':records,
	'form':form,
	'button_show':button_show,
	'total_cost':total_cost,
	'total_item':total_item,
	}
	return render(request,'shop_templates/Product_Purchase_Year_End_Transaction.html',context)


def All_Stock_Status(request):
	task_array=[]
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	for task in tasks:
		task_array.append(task.task.title)

	records=Stock.objects.all()


	context={
	'task_array':task_array,
	'records':records,
	}
	return render(request,'shop_templates/All_Stock_Status.html',context)


def All_Auction_Stock_Status(request):
	task_array=[]
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	for task in tasks:
		task_array.append(task.task.title)

	records=Stock_Auction.objects.all()


	context={
	'task_array':task_array,
	'records':records,
	}
	return render(request,'shop_templates/All_Auction_Stock_Status.html',context)



def Purchase_Summary(request):
	task_array=[]
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	for task in tasks:
		task_array.append(task.task.title)

	form=Purchase_Summary_form(request.POST or None)

	form.fields['start_date'].initial=now
	form.fields['stop_date'].initial=now

	records=[]
	total_cost=0
	if request.method == 'POST':
		status1='TREATED'
		status2='APPROVED'



		start_date=request.POST.get("start_date")
		stop_date=request.POST.get("stop_date")


		date_format = '%Y-%m-%d'
		start_date = datetime.strptime(start_date, date_format)
		stop_date = datetime.strptime(stop_date, date_format)



		records=Purchase_Header.objects.filter(Q(invoice_date__gte=start_date) & Q(invoice_date__lte=stop_date)).filter(status=status1,approval_status=status2)

		queryset=Purchase_Header.objects.filter(Q(invoice_date__gte=start_date) & Q(invoice_date__lte=stop_date)).filter(status=status1,approval_status=status2).aggregate(total_cost=Sum('total_amount'))
		total_cost=queryset['total_cost']

	context={
	'task_array':task_array,
	'form':form,
	'records':records,
	'total_cost':total_cost,
	}
	return render(request,'shop_templates/Purchase_Summary.html',context)


def Purchase_Summary_Details(request,pk):
	task_array=[]
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	for task in tasks:
		task_array.append(task.task.title)

	invoice=Purchase_Header.objects.get(invoice=pk)


	records=Purchases.objects.filter(purchase__invoice=invoice.invoice)

	queryset=Purchases.objects.filter(purchase__invoice=invoice.invoice).aggregate(total_cost=Sum('total_cost'),total_item=Sum('quantity'))
	total_cost=queryset['total_cost']
	total_item=queryset['total_item']


	context={
	'task_array':task_array,
	'total_cost':total_cost,
	'total_item':total_item,
	'records':records,
	}
	return render(request,'shop_templates/Purchase_Summary_Details.html',context)


def Daily_Sales_Report(request):
	task_array=[]
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	for task in tasks:
		task_array.append(task.task.title)

	form=Purchase_Summary_form(request.POST or None)


	form.fields['start_date'].initial=now
	form.fields['stop_date'].initial=now

	records=[]
	total_amount=0
	total_item=0
	if request.method == 'POST' and 'btn_fetch' in request.POST:
		start_date=request.POST.get("start_date")
		stop_date=request.POST.get("stop_date")


		date_format = '%Y-%m-%d'
		start_date = datetime.strptime(start_date, date_format)
		stop_date = datetime.strptime(stop_date, date_format)

		# records=Daily_Sales.objects.filter(tdate__range=[start_date,stop_date])

		# records=Daily_Sales_Cash_Flow_Summary.objects.filter(Q(tdate__gte=start_date) & Q(tdate__lte=stop_date))
		records=Daily_Sales.objects.filter(tdate__range=[start_date,stop_date]).order_by('tdate')

		queryset=Daily_Sales.objects.filter(tdate__range=[start_date,stop_date]).aggregate(total_amount=Sum('total'),total_item=Sum('quantity'))
		total_amount=queryset['total_amount']
		total_item=queryset['total_item']



	context={
	'task_array':task_array,
	'form':form,
	'records':records,
	'total_item':total_item,
	'total_amount':total_amount,
	}
	return render(request,'shop_templates/Daily_Sales_Report.html',context)









def Daily_Sales_Report_Summary(request):
	task_array=[]
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	for task in tasks:
		task_array.append(task.task.title)

	form=Purchase_Summary_form(request.POST or None)


	form.fields['start_date'].initial=now
	form.fields['stop_date'].initial=now

	records=[]
	total_amount=0
	if request.method == 'POST' and 'btn_fetch' in request.POST:
		start_date=request.POST.get("start_date")
		stop_date=request.POST.get("stop_date")


		date_format = '%Y-%m-%d'
		start_date = datetime.strptime(start_date, date_format)
		stop_date = datetime.strptime(stop_date, date_format)

		# records=Daily_Sales.objects.filter(tdate__range=[start_date,stop_date])

		# records=Daily_Sales_Cash_Flow_Summary.objects.filter(Q(tdate__gte=start_date) & Q(tdate__lte=stop_date))
		records=Daily_Sales_Cash_Flow_Summary.objects.filter(tdate__range=[start_date,stop_date])

		queryset=Daily_Sales_Cash_Flow_Summary.objects.filter(tdate__range=[start_date,stop_date]).aggregate(total_amount=Sum('amount'))
		total_amount=queryset['total_amount']



	if request.method == 'POST' and 'btn_view' in request.POST:
		start_date=request.POST.get("start_date")
		stop_date=request.POST.get("stop_date")

		date_format = '%Y-%m-%d'
		start_date = datetime.strptime(start_date, date_format)
		stop_date = datetime.strptime(stop_date, date_format)

		tdate={
		'day1':start_date.day,
		'month1':start_date.month,
		'year1':start_date.year,
		'day2':stop_date.day,
		'month2':stop_date.month,
		'year2':stop_date.year,
		}
		records=Daily_Sales_Summary.objects.filter(tdate__range=[start_date,stop_date])

		queryset=Daily_Sales_Summary.objects.filter(tdate__range=[start_date,stop_date]).aggregate(total_amount=Sum('amount'))
		total_amount=queryset['total_amount']

		return render(request,'shop_templates/Daily_Sales_Report_All_Cat_Details.html',{'records':records,'tdate':tdate,'task_array':task_array,'total_amount':total_amount,})


	context={
	'task_array':task_array,
	'form':form,
	'records':records,
	'total_amount':total_amount,
	}
	return render(request,'shop_templates/Daily_Sales_Report_Summary.html',context)


def Daily_Sales_All_Category_Report_Details(request,d1,m1,y1, d2,m2,y2):
	task_array=[]
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	for task in tasks:
		task_array.append(task.task.title)

	start_date=datetime(int(y1), int(m1), int(d1))
	stop_date=datetime(int(y2),int(m2),int(d2))

	records=Daily_Sales.objects.filter(tdate__range=[start_date,stop_date])

	queryset=Daily_Sales.objects.filter(tdate__range=[start_date,stop_date]).aggregate(total_amount=Sum('total'),total_item=Sum('quantity'))
	total_amount=queryset['total_amount']
	total_item=queryset['total_item']

	context={
	'task_array':task_array,
	'records':records,
	'total_amount':total_amount,
	'total_item':total_item,
	}
	return render(request,'shop_templates/Daily_Sales_All_Category_Report_Details.html',context)



def Daily_Sales_Report_Details(request,pk):
	task_array=[]
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	for task in tasks:
		task_array.append(task.task.title)

	record=Daily_Sales_Cash_Flow_Summary.objects.get(id=pk)
	items=Daily_Sales_Summary.objects.filter(tdate=record.tdate,sale__sales_category=record.sales_category)

	context={
	'task_array':task_array,
	'items':items,
	'tdate':record.tdate,
	'sales_category':record.sales_category,
	}
	return render(request,'shop_templates/Daily_Sales_Report_Details.html',context)


def Daily_Sales_Report_Receipt_Details(request,pk):
	task_array=[]
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	for task in tasks:
		task_array.append(task.task.title)

	records=Daily_Sales.objects.filter(receipt=pk)

	queryset=Daily_Sales.objects.filter(receipt=pk).aggregate(total_amount=Sum('total'),total_item=Sum('quantity'))
	total_amount=queryset['total_amount']
	total_item=queryset['total_item']

	context={
	'task_array':task_array,
	'records':records,
	'total_amount':total_amount,
	'total_item':total_item,
	}
	return render(request,'shop_templates/Daily_Sales_Report_Receipt_Details.html',context)


def Daily_Sales_Report_All_Details(request,year, month, day, sales_category):
	task_array=[]
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	for task in tasks:
		task_array.append(task.task.title)

	tdate = date(int(year), int(month), int(day))

	tyear=tdate.year
	tmonth=tdate.month
	tday=tdate.day
	records=Daily_Sales.objects.filter(tdate=tdate,sales_category=sales_category)

	queryset=Daily_Sales.objects.filter(tdate=tdate,sales_category=sales_category).aggregate(total_amount=Sum('total'),total_item=Sum('quantity'))
	total_item=queryset['total_item']
	total_amount=queryset['total_amount']

	context={
	'task_array':task_array,
	'records':records,
	'total_item':total_item,
	'total_amount':total_amount,
	}
	return render(request,'shop_templates/Daily_Sales_Report_All_Details.html',context)



def load_branches(request):
	task_array=[]
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	for task in tasks:
		task_array.append(task.task.title)

	supplier_id = request.GET.get('supplier')
	branches = Suppliers_Branches.objects.filter(supplier=supplier_id).order_by('address')
	return render(request, 'shop_templates/branches_dropdown_list_options.html',{'branches':branches,'task_array':task_array})

def Expenditure_Manager(request):
	task_array=[]
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	for task in tasks:
		task_array.append(task.task.title)
	tdate=get_current_date(now)
	processed_by=CustomUser.objects.get(id=request.user.id)
	processed_by=processed_by.username

	form=Expenditure_Manager_form(request.POST or None)

	total_amount=0
	records=Expenditures.objects.filter(processed_by=processed_by,tdate=tdate,status='UNTREATED')
	queryset=Expenditures.objects.filter(processed_by=processed_by,tdate=tdate,status='UNTREATED').aggregate(total_amount=Sum('amount'))

	total_amount=queryset['total_amount']

	if request.method ==	'POST':
		amount=request.POST.get("amount")
		details=request.POST.get("details")
		reference=request.POST.get("reference")

		if not amount:
			messages.error(request,'Amount is missing')
			return HttpResponseRedirect(reverse('Expenditure_Manager'))

		if not details:
			messages.error(request,'Detail is missing')
			return HttpResponseRedirect(reverse('Expenditure_Manager'))

		if not reference:
			messages.error(request,'reference is missing')
			return HttpResponseRedirect(reverse('Expenditure_Manager'))

		Expenditures(details=details,amount=amount,reference=reference,tdate=tdate,status='UNTREATED',processed_by=processed_by).save()
		messages.success(request,'Record submitted Successfully')
		return HttpResponseRedirect(reverse('Expenditure_Manager'))

	context={
	'task_array':task_array,
	'form':form,
	'records':records,
	'total_amount':total_amount,
	}
	return render(request,'shop_templates/Expenditure_Manager.html',context)


def Expenditure_Discard(request,pk):
	Expenditures.objects.filter(id=pk).delete()
	return HttpResponseRedirect(reverse('Expenditure_Manager'))


def Expenditure_Daily_Summary(request):
	task_array=[]
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	for task in tasks:
		task_array.append(task.task.title)
	tdate=get_current_date(now)
	processed_by=CustomUser.objects.get(id=request.user.id)
	processed_by=processed_by.username

	form=Expenditure_Manager_form(request.POST or None)

	total_amount=0
	records=Expenditures.objects.filter(processed_by=processed_by,tdate=tdate,status='UNTREATED')
	queryset=Expenditures.objects.filter(processed_by=processed_by,tdate=tdate,status='UNTREATED').aggregate(total_amount=Sum('amount'))

	total_amount=queryset['total_amount']

	if request.method ==	'POST':
		reference=get_ticket()
		Expenditures_Dialy_Summary(amount=total_amount,status="UNTREATED",processed_by=processed_by,tdate=tdate,summary_code="DE-" + str(reference)).save()
		Expenditures.objects.filter(tdate=tdate,status='UNTREATED',processed_by=processed_by).update(status='TREATED',summary_code="DS-" + str(reference))
		return HttpResponseRedirect(reverse('shop_home'))

	context={
	'task_array':task_array,
	'form':form,
	'records':records,
	'total_amount':total_amount,
	}
	return render(request,'shop_templates/Expenditure_Daily_Summary.html',context)


def Expenditure_Day_End_Summary(request):
	task_array=[]
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	for task in tasks:
		task_array.append(task.task.title)

	processed_by=CustomUser.objects.get(id=request.user.id)
	processed_by=processed_by.username

	status='ACTIVE'
	form=members_shop_sales_credit_generate_form(request.POST or None)

	total_amount=0
	records=[]
	button_show=False
	if request.method =='POST' and 'btn-fetch' in request.POST:
		tdate=request.POST.get("period")
		# tdate=get_current_date(tdate_id)
		records=Expenditures_Dialy_Summary.objects.filter(tdate=tdate,status='UNTREATED')
		queryset=Expenditures_Dialy_Summary.objects.filter(tdate=tdate,status='UNTREATED').aggregate(total_amount=Sum('amount'))

		total_amount=queryset['total_amount']
		if records:
			button_show=True

	if request.method ==	'POST' and 'btn-process' in request.POST:
		tdate=request.POST.get("period")
		if Expenditures_Dialy_Summary.objects.filter(tdate=tdate,status='UNTREATED').exists():
			reference=get_ticket()
			queryset=Expenditures_Dialy_Summary.objects.filter(tdate=tdate,status='UNTREATED').aggregate(total_amount=Sum('amount'))

			total_amount=queryset['total_amount']

			Expenditures_Day_End_Summary(amount=total_amount,status="UNTREATED",processed_by=processed_by,tdate=tdate,day_end_code="DE-" + str(reference)).save()
			Expenditures_Dialy_Summary.objects.filter(tdate=tdate,status='UNTREATED').update(status='TREATED',day_end_code="DE-" + str(reference))

			balance=shop_cashbook_balance()
			balance=float(balance)+float(total_amount)
			# shop_cashbook_posting(particulars,debeit,crdit,balance,ref_no,status,tdate)
			shop_cashbook_posting('Miscellaneous Expenditures',0,total_amount,balance,'EXP-' + str(reference),status,tdate,processed_by,'EXPENDITURE')

			return HttpResponseRedirect(reverse('shop_home'))
		else:
			messages.error(request,'Please verify if the date has changed')
			return HttpResponseRedirect(reverse('Expenditure_Day_End_Summary'))

	form.fields['period'].initial=now
	context={
	'task_array':task_array,
	'form':form,
	'records':records,
	'total_amount':total_amount,
	'button_show':button_show,
	}
	return render(request,'shop_templates/Expenditure_Day_End_Summary.html',context)


def Expenditure_Month_End_Summary(request):
	task_array=[]
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	for task in tasks:
		task_array.append(task.task.title)

	processed_by=CustomUser.objects.get(id=request.user.id)
	processed_by=processed_by.username

	form=members_shop_sales_credit_generate_form(request.POST or None)

	total_amount=0
	records=[]
	button_show=False
	if request.method =='POST' and 'btn-fetch' in request.POST:
		tdate=request.POST.get("period")
		# tdate=get_current_date(tdate_id)
		records=Expenditures_Day_End_Summary.objects.filter(Q(tdate__lte=tdate)).filter(status='UNTREATED')
		queryset=Expenditures_Day_End_Summary.objects.filter(Q(tdate__lte=tdate)).filter(status='UNTREATED').aggregate(total_amount=Sum('amount'))

		total_amount=queryset['total_amount']
		if records:
			button_show=True

	if request.method ==	'POST' and 'btn-process' in request.POST:
		tdate=request.POST.get("period")
		if Expenditures_Day_End_Summary.objects.filter(Q(tdate__lte=tdate)).filter(status='UNTREATED').exists():
			reference=get_ticket()

			queryset=Expenditures_Day_End_Summary.objects.filter(Q(tdate__lte=tdate)).filter(status='UNTREATED').aggregate(total_amount=Sum('amount'))

			total_amount=queryset['total_amount']

			Expenditures_Month_End_Summary(amount=total_amount,status="UNTREATED",processed_by=processed_by,tdate=tdate,month_end_code="ME-" + str(reference)).save()
			Expenditures_Day_End_Summary.objects.filter(Q(tdate__lte=tdate)).filter(status='UNTREATED').update(status='TREATED',month_end_code="ME-" + str(reference))
			return HttpResponseRedirect(reverse('shop_home'))
		else:
			messages.error(request,'Please verify if the date has changed')
			return HttpResponseRedirect(reverse('Expenditure_Day_End_Summary'))

	form.fields['period'].initial=now
	context={
	'task_array':task_array,
	'form':form,
	'records':records,
	'total_amount':total_amount,
	'button_show':button_show,
	}
	return render(request,'shop_templates/Expenditure_Month_End_Summary.html',context)


def Expenditure_Year_End_Summary(request):
	task_array=[]
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	for task in tasks:
		task_array.append(task.task.title)

	processed_by=CustomUser.objects.get(id=request.user.id)
	processed_by=processed_by.username

	form=members_shop_sales_credit_generate_form(request.POST or None)

	total_amount=0
	records=[]
	button_show=False
	if request.method =='POST' and 'btn-fetch' in request.POST:
		tdate=request.POST.get("period")
		# tdate=get_current_date(tdate_id)
		records=Expenditures_Month_End_Summary.objects.filter(Q(tdate__lte=tdate)).filter(status='UNTREATED')
		queryset=Expenditures_Month_End_Summary.objects.filter(Q(tdate__lte=tdate)).filter(status='UNTREATED').aggregate(total_amount=Sum('amount'))

		total_amount=queryset['total_amount']
		if records:
			button_show=True

	if request.method ==	'POST' and 'btn-process' in request.POST:
		tdate=request.POST.get("period")
		if Expenditures_Month_End_Summary.objects.filter(Q(tdate__lte=tdate)).filter(status='UNTREATED').exists():
			reference=get_ticket()

			queryset=Expenditures_Month_End_Summary.objects.filter(Q(tdate__lte=tdate)).filter(status='UNTREATED').aggregate(total_amount=Sum('amount'))

			total_amount=queryset['total_amount']

			Expenditures_Year_End_Summary(amount=total_amount,status="UNTREATED",processed_by=processed_by,tdate=tdate,year_end_code="YE-" + str(reference)).save()
			Expenditures_Month_End_Summary.objects.filter(Q(tdate__lte=tdate)).filter(status='UNTREATED').update(status='TREATED',year_end_code="YE-" + str(reference))
			return HttpResponseRedirect(reverse('shop_home'))
		else:
			messages.error(request,'Please verify if the date has changed')
			return HttpResponseRedirect(reverse('Expenditure_Year_End_Summary'))

	form.fields['period'].initial=now
	context={
	'task_array':task_array,
	'form':form,
	'records':records,
	'total_amount':total_amount,
	'button_show':button_show,
	}
	return render(request,'shop_templates/Expenditure_Year_End_Summary.html',context)



def CashBook_Shop_Display(request):
	task_array=[]
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	for task in tasks:
		task_array.append(task.task.title)
	form=stock_status_list_details_Form(request.POST or None)

	records=[]
	if request.method == 'POST' and 'btn-fetch' in request.POST:
		start_date=request.POST.get("start_date")
		stop_date=request.POST.get("stop_date")
		records=CashBook_Shop.objects.filter(tdate__range=[start_date,stop_date])

	form.fields['start_date'].initial=now
	form.fields['stop_date'].initial=now
	context={
	'task_array':task_array,
	'records':records,
	'form':form,
	}
	return render(request,'shop_templates/CashBook_Shop_Display.html',context)






def Deduction_Upload_Period_Load(request):
	task_array=[]
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	for task in tasks:
		task_array.append(task.task.title)

	form=Monthly_Deductions_Transaction_Period_Institution_load_Form(request.POST or None)
	items=ItemWriteOffReasons.objects.all()
	if request.method == 'POST':
		salary_institution_id=request.POST.get("salary_institution")
		salary_institution=SalaryInstitution.objects.get(id=salary_institution_id)

		transaction_period=request.POST.get('transaction_period')
		return HttpResponseRedirect(reverse('Deduction_Upload_Member_Search',args=(transaction_period,salary_institution.pk)))
	
	form.fields['transaction_period'].initial=get_current_date(now)
	context={
	'task_array':task_array,
	'form':form,
	'items':items,
	}
	return render(request,'shop_templates/Deduction_Upload_Period_Load.html',context)




def Deduction_Upload_Member_Search(request,period_pk,salary_pk):
	task_array=[]
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	for task in tasks:
		task_array.append(task.task.title)
	transaction_period = datetime.strptime(period_pk, '%Y-%m-%d')
	transaction_period=get_current_date(transaction_period)
	salary_institution=SalaryInstitution.objects.get(id=salary_pk)
	records=MonthlyShopdeductionList_Aux.objects.filter(salary_institution=salary_institution,transaction_period=transaction_period)
	title="Shop Deduction Update"
	form = searchForm(request.POST or None)
	return render(request,'shop_templates/Deduction_Upload_Member_Search.html',{'records':records,'form':form,'title':title,'period_pk':period_pk,'salary_pk':salary_pk,'task_array':task_array,'salary_institution':salary_institution,})




def Deduction_Upload_Member_list_load(request,period_pk,salary_pk):
	task_array=[]
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	for task in tasks:
		task_array.append(task.task.title)

	title="Membership Deduction"
	if request.method == "POST":
		form = searchForm(request.POST)
		status="ACTIVE"
		if not form['title'].value():
			messages.error(request,'Please enter search')
			return HttpResponseRedirect(reverse('Deduction_Upload_Member_Search'))

		members=searchMembersForShopDeduction(form['title'].value(),status,salary_pk)

		if not members:
			messages.error(request,'No record found')
			return HttpResponseRedirect(reverse('Deduction_Upload_Member_Search',args=(period_pk,salary_pk,)))

	context={
	'period_pk':period_pk,
	'task_array':task_array,
	'salary_pk':salary_pk,
	'members':members,
	'title':title,
	}
	return render(request,'shop_templates/Deduction_Upload_Member_list_load.html',context)


def Deduction_Upload_Member_Deduction_Upload(request,pk,period_pk,salary_pk):
	task_array=[]
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	for task in tasks:
		task_array.append(task.task.title)

	form=Monthly_Deduction_Generated_Update_Details_Process_Form(request.POST or None)
	member=Members.objects.get(id=pk)
	
	transaction_period = datetime.strptime(period_pk, '%Y-%m-%d')
	transaction_period=get_current_date(transaction_period)

	salary_institution=SalaryInstitution.objects.get(id=salary_pk)
	tdate=get_current_date(now)
	processed_by=CustomUser.objects.get(id=request.user.id)
	processed_by=processed_by.username

	if request.method ==  'POST':
		amount=request.POST.get('amount')
		if not amount or float(amount)<=0:
			messages.error(request,'Invalid Amount Specification')
			return HttpResponseRedirect(reverse('Deduction_Upload_Member_Deduction_Upload',args=(pk,period_pk,salary_pk,)))
		
		loan_number=generate_number(600,member.coop_no,now)

		MonthlyShopdeductionList_Aux(member=member,
								transaction_period=transaction_period,
								account_number=loan_number,
								amount=amount,
								amount_deducted=0,
								balance=-float(amount),
								status='UNTREATED',
								processing_status='UNPROCESSED',
								salary_institution=salary_institution,
								processed_by=processed_by,
								tdate=tdate
								).save()
		return HttpResponseRedirect(reverse('Deduction_Upload_Member_Search',args=(period_pk,salary_pk,)))

	context={
	'period_pk':period_pk,
	'task_array':task_array,
	'salary_pk':salary_pk,
	'salary_institution':salary_institution,
	'member':member,
	'form':form,
	}
	return render(request,'shop_templates/Deduction_Upload_Member_Deduction_Upload.html',context)



def Deduction_Upload_Member_Deduction_Upload_Delete(request,pk,period_pk,salary_pk):
	MonthlyShopdeductionList_Aux.objects.filter(id=pk).delete()
	return HttpResponseRedirect(reverse('Deduction_Upload_Member_Search',args=(period_pk,salary_pk,)))






def Delete_Daily_Sales(request):
	Members_Credit_Sales_Selected.objects.all().delete()
	CooperativeShopLedger.objects.all().delete()
	Daily_Sales.objects.all().delete()
	Daily_Sales_Cash_Flow_Summary.objects.all().delete()
	Cooperative_Shop_Cash_Deposit.objects.all().delete()
	General_Cash_Sales_Selected.objects.all().delete()
	Day_End_Sales_Transactions.objects.all().delete()
	Daily_Cash_Deposit_Summary.objects.all().delete()
	members_shop_credit_loans.objects.all().delete()
	CashBook_Shop.objects.all().delete()
	return HttpResponseRedirect(reverse('shop_home'))

def Delete_Daily_Sales1(request):

	MonthlyShopdeductionListGenerated.objects.all().delete()
	MonthlyShopdeductionList.objects.all().delete()
	MonthlyShopGroupGeneratedTransactions.objects.all().delete()
	MonthlyJointDeductionList.objects.all().delete()
	MonthlyJointDeductionGeneratedTransactions.objects.all().delete()
	MonthlyJointDeductionGenerated.objects.all().delete()
	MonthlyDeductionList.objects.all().delete()
	MonthlyGeneratedTransactions.objects.all().delete()
	MonthlyDeductionListGenerated.objects.all().delete()
	MonthlyGroupGeneratedTransactions.objects.all().delete()
	MonthlyDeductionGenerationHeading.objects.all().delete()
	AccountDeductions.objects.all().delete()
	NonMemberAccountDeductions.objects.all().delete()
	MonthlyOverdeductionsRefund.objects.all().delete()


	return HttpResponseRedirect(reverse('shop_home'))
