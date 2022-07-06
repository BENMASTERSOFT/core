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

from .personnal_ledger_diplay import Display_PersonalLedger,Display_PersonalLedger_All_Records
from .current_date import get_current_date,get_print_date
from .loan_data import *
from .members_search import *
import math
from .load_ticket import get_ticket
from .ledger_posting import *
from .Savings_Data import *
from .cashbook_manager import *
import time
from . receipt_manager import *

now = datetime.datetime.now()

from io import BytesIO
from django.template.loader import get_template
from xhtml2pdf import pisa
from . utils import render_to_pdf



month_list =['JANUARY','FEBRUARY','MARCH','APRIL','MAY','JUNE','JULY','AUGUST','SEPTEMBER','OCTOBER','NOVEMBER','DECEMBER']


############################################################
########## REPORT LAB IMPORT ##############################
############################################################

from django.http import FileResponse
import io
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter, A4, landscape
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.enums import TA_JUSTIFY, TA_LEFT, TA_CENTER, TA_RIGHT
from . program import  generatePDF
from reportlab.platypus import Table, Image, Paragraph

from . report_deduction_cover import deductionCoverDateTable, addressTable,deductionOrderBodyTable,bankTable,signatureTable
from . Loan_Application_Issueance import loanApplicationIssueanceMainHeaderTitle,Loan_Application_Issueance_dateTable, Loan_Application_IssueanceSectionATable, \
											Loan_Application_IssueanceSectionBTable,Loan_Application_IssueanceSectionCTable, Loan_Application_IssueanceSectionApprovalTable
from . report_membership import _membershipMainHeaderTitle,_membershipGenHeaderTable,_membershipReceiptSection,_membershipGenBodyTable,_membershipGenFooterTable
from . report_membership_deduction_order import _membershipDeductionOrderHeader, _membershipDeductionOrderGetLogoTable, _membershipDeductionOrderReceiptSection, \
													_membershipDeductionOrderDeductionGenBodyTable,_membershipDeductionOrderGenFooterTable
from . report_loan_application_certicate import _loanApplicationCerticateHeader, _loanApplicationCerticateGetLogoTable, _loanApplicationCerticatePersonnelSection \
												,_loanApplicationCerticateMembershipGenFooterTable,_loanApplicationCerticateGenSignatureTable,_loanApplicationCerticateGenGurantorTable,_loanApplicationCerticateGenBodyTable, _loanApplicationCerticateGenNextOfKinTable

from . report_commodity_trending_product import _trendingProductHeader, _trendingProductGetLogoTable, _trendingProductBodyTable


def commodity_trending_product_Print(request,pk):
	applicant=Members.objects.get(id=pk)
	operator=request.user.username
	buf = io.BytesIO()

	pdf = canvas.Canvas(buf, pagesize = A4)
	# pdf = canvas.Canvas(buf, pagesize = landscape(A4))
	pdf.setTitle("FETHA II CTCS")

	# for font in pdf.getAvailableFonts():
	# 	print(font)


	width, height = A4
	# width, height =landscape(A4)
	width=width-20
	heightList = [
		height * 8 / 100,
		height * 10 / 100,
		height * 8 / 100,
		height * 3 / 100,
		height * 30 / 100,
		height * 2 / 100,
		height * 13 / 100,
		height * 1 / 100,
		height * 12 / 100,
		height * 13 / 100,
		height * 1 / 100,
	]

	tdate=get_print_date(now)
	receipt_id=pk



	mainTable = Table([
			[_trendingProductHeader()],
			[_trendingProductGetLogoTable(width,heightList[1])],
			[''],
			[''],
			[_trendingProductBodyTable(width,heightList[4])],
			[''],
			[''],
			[''],
			[''],
			[''],
			[''],

		],
		colWidths= width-40,
		rowHeights= heightList
		)

	mainTable.setStyle([
		# ('GRID', (0, 0), (-1, -1), 1, 'red'),
		# ('TEXTCOLOR',(0,0),(0,0),'black'),
		# ('FONTSIZE', (0,0), (0,0), 16),
		# ('FONTNAME', (0,0), (0,0), 'Helvetica-Bold'),

		# ('ALIGN', (0,0), (0,0), 'CENTER'),
		# ('VALIGN', (0,0), (0,0), 'MIDDLE'),


		('LEFTPADDING', (0, 0), (-1, -1), 5),
		('BOTTOMPADDING', (0, 0), (0, 0), 10),
		# ('BOTTOMPADDING', (0, 0), (1, 0), 10),
		# ('RIGHTADDING', (0, 0), (-1, -1), 15),
		])

	mainTable.wrapOn(pdf, 0, 0)
	mainTable.drawOn(pdf, 0, 0)
	pdf.showPage()
	pdf.save()

	buf.seek(0)

	# Return something
	# return FileResponse(buf, as_attachment=True, filename='loan_certificate.pdf')
	return HttpResponse(buf,   content_type='application/pdf')



def Loan_application_processing_Form_Print(request,pk):
	applicant=LoansRepaymentBase.objects.get(loan_number=pk)
	operator=request.user.username
	buf = io.BytesIO()

	pdf = canvas.Canvas(buf, pagesize = A4)
	# pdf = canvas.Canvas(buf, pagesize = landscape(A4))
	pdf.setTitle("FETHA II CTCS")

	# for font in pdf.getAvailableFonts():
	# 	print(font)


	width, height = A4
	# width, height =landscape(A4)

	heightList = [
		height * 8 / 100,
		height * 10 / 100,
		height * 8 / 100,
		height * 3 / 100,
		height * 30 / 100,
		height * 2 / 100,
		height * 13 / 100,
		height * 1 / 100,
		height * 12 / 100,
		height * 7 / 100,
		height * 5 / 100,
		height * 1 / 100,
	]

	tdate=get_print_date(now)
	receipt_id=pk

	style = ParagraphStyle('sectionb')
	style.fontName = 'Helvetica'
	style.fontSize = 12
	style.alignment = TA_CENTER

	titlePara = Paragraph(f'<u><b>SECTION B</b><i>(Loan Details)</i></u>',style)



	mainTable = Table([
			[_loanApplicationCerticateHeader()],
			[_loanApplicationCerticateGetLogoTable(width,heightList[1])],
			[_loanApplicationCerticatePersonnelSection(width,heightList[2],pk)],
			[titlePara],
			[_loanApplicationCerticateGenBodyTable(width,heightList[4],pk)],
			[''],
			[_loanApplicationCerticateGenNextOfKinTable(width,heightList[6],pk)],
			[''],
			[_loanApplicationCerticateGenGurantorTable(width,heightList[8],pk)],
			[_loanApplicationCerticateGenSignatureTable(width,heightList[9])],
			[_loanApplicationCerticateMembershipGenFooterTable(width, heightList[10],operator)],
			[''],
		],
		colWidths= width-40,
		rowHeights= heightList
		)

	mainTable.setStyle([
		# ('GRID', (0, 0), (-1, -1), 1, 'red'),
		# ('TEXTCOLOR',(0,0),(0,0),'black'),
		# ('FONTSIZE', (0,0), (0,0), 16),
		# ('FONTNAME', (0,0), (0,0), 'Helvetica-Bold'),

		# ('ALIGN', (0,0), (0,0), 'CENTER'),
		# ('VALIGN', (0,0), (0,0), 'MIDDLE'),


		('LEFTPADDING', (0, 0), (-1, -1), 5),
		('BOTTOMPADDING', (0, 0), (0, 0), 10),
		# ('BOTTOMPADDING', (0, 0), (1, 0), 10),
		# ('RIGHTADDING', (0, 0), (-1, -1), 15),
		])

	mainTable.wrapOn(pdf, 0, 0)
	mainTable.drawOn(pdf, 0, 0)
	pdf.showPage()
	pdf.save()

	buf.seek(0)

	# Return something
	return FileResponse(buf, as_attachment=True, filename='loan_certificate.pdf')



def Loan_application_processing_confirmation(request,pk):
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	task_array=[]
	for task in tasks:
		task_array.append(task.task.title)


	task_enabler=TransactionEnabler.objects.filter(status="YES")
	task_enabler_array=[]
	for item in task_enabler:
		task_enabler_array.append(item.title)

	default_password="NO"
	if Staff.objects.filter(admin=request.user,default_password='YES'):
		default_password="YES"


	applicant=LoansRepaymentBase.objects.get(loan_number=pk)
	context={
	'task_array':task_array,
	'task_enabler_array':task_enabler_array,
	'default_password':default_password,
	'applicant':applicant,
	}
	return render(request, 'deskofficer_templates/Loan_application_processing_confirmation.html',context)


def Loan_Application_Issueance_Form_Print(request,pk):
	record=LoanFormIssuance.objects.get(receipt=pk)
	operator=request.user.username
	buf = io.BytesIO()

	pdf = canvas.Canvas(buf, pagesize = A4)
	# pdf = canvas.Canvas(buf, pagesize = landscape(A4))
	pdf.setTitle("FETHA II CTCS")

	# for font in pdf.getAvailableFonts():
	# 	print(font)


	width, height = A4
	# width, height =landscape(A4)

	heightList = [
		height * 8 / 100,
		height * 4 / 100,
		height * 1 / 100,
		height * 40 / 100,
		height * 19 / 100,
		height * 24 / 100,
		height * 2 / 100,
		height * 2 / 100,
	]

	tdate=get_print_date(now)
	receipt_id=pk
	mainTable = Table([
			[loanApplicationIssueanceMainHeaderTitle()],
			[Loan_Application_Issueance_dateTable(width,heightList[1],pk,tdate)],
			[''],
			[Loan_Application_IssueanceSectionATable(width,heightList[3],pk)],
			[Loan_Application_IssueanceSectionBTable(width,heightList[4])],
			[Loan_Application_IssueanceSectionCTable(width,heightList[5],pk)],
			[Loan_Application_IssueanceSectionApprovalTable(width,heightList[6])],
			['']
		],
		colWidths= width,
		rowHeights= heightList
		)

	mainTable.setStyle([
		# ('GRID', (0, 0), (-1, -1), 1, 'red'),
		# ('TEXTCOLOR',(0,0),(0,0),'black'),
		# ('FONTSIZE', (0,0), (0,0), 16),
		# ('FONTNAME', (0,0), (0,0), 'Helvetica-Bold'),

		# ('ALIGN', (0,0), (0,0), 'CENTER'),
		# ('VALIGN', (0,0), (0,0), 'MIDDLE'),


		('LEFTPADDING', (0, 0), (-1, -1), 16),
		('BOTTOMPADDING', (0, 0), (-1, -1), 0),
		('BOTTOMPADDING', (0, 0), (1, 0), 10),
		# ('RIGHTADDING', (0, 0), (-1, -1), 15),
		])

	mainTable.wrapOn(pdf, 0, 0)
	mainTable.drawOn(pdf, 0, 0)
	pdf.showPage()
	pdf.save()

	buf.seek(0)

	# Return something
	# return FileResponse(buf, as_attachment=True, filename='deduction.pdf')
	return HttpResponse(buf,   content_type='application/pdf')




def Monthly_Deduction_Covering_Note(request):
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	task_array=[]
	for task in tasks:
		task_array.append(task.task.title)


	task_enabler=TransactionEnabler.objects.filter(status="YES")
	task_enabler_array=[]
	for item in task_enabler:
		task_enabler_array.append(item.title)

	default_password="NO"
	if Staff.objects.filter(admin=request.user,default_password='YES'):
		default_password="YES"

	form = Monthly_Deduction_Covering_Note_Form(request.POST or None)


	if request.method == 'POST':
		staff1_id = request.POST.get('staff1')
		staff1 = Executives.objects.get(id=staff1_id)


		account = request.POST.get('account')
		# account = CooperativeBankAccounts.objects.get(id=account_id)

		staff2_id = request.POST.get('staff2')
		staff2 = Executives.objects.get(id=staff2_id)

		if staff1_id == staff2_id:
			messages.error(request,'Duplicate Selection Not Allowed')
			return HttpResponseRedirect(reverse('Monthly_Deduction_Covering_Note'))


		print_date_id = request.POST.get('print_date')
		transaction_date_id = request.POST.get('transaction_date')

		date_format = '%Y-%m-%d'


		dtObj = datetime.datetime.strptime(print_date_id, date_format)
		print_date=get_print_date(dtObj)

		dtObj = datetime.datetime.strptime(transaction_date_id, date_format)
		transaction_date=get_current_date(dtObj)
		month = month_list[transaction_date.month-1]

		transaction_period = '{} {}'.format(month,transaction_date.year)


		return HttpResponseRedirect(reverse('Monthly_Deduction_Covering_Note_Print',args=(print_date,transaction_period,staff1.name,staff1.position.title,staff2.name,staff2.position.title,account)))

	form.fields['print_date'].initial = now
	form.fields['transaction_date'].initial = now
	context={
	'task_array':task_array,
	'task_enabler_array':task_enabler_array,
	'default_password':default_password,
	'form':form,
	}
	return render(request, 'deskofficer_templates/Monthly_Deduction_Covering_Note.html',context)





def Monthly_Deduction_Covering_Note_Print(request,print_date,transaction_period,staff1,position1,staff2,position2,account):
	operator=request.user.username


	buf = io.BytesIO()

	pdf = canvas.Canvas(buf, pagesize = A4)
	# pdf = canvas.Canvas(buf, pagesize = landscape(A4))
	pdf.setTitle("FETHA II CTCS")

	# for font in pdf.getAvailableFonts():
	# 	print(font)


	width, height = A4
	# width, height =landscape(A4)

	heightList = [
		height * 25 / 100,
		height * 3 / 100,
		height * 13 / 100,
		height * 18 / 100,
		height * 23 / 100,
		height * 13 / 100,
		height * 7 / 100,
	]

	tdate=get_print_date(now)

	stafList = [
	staff1,
	staff2,
	position1,
	position2,
	]
	mainTable = Table([
			[''],
			[deductionCoverDateTable(width,heightList[1],tdate)], #
			[addressTable(width,heightList[2])],
			[deductionOrderBodyTable(width,heightList[3],transaction_period)],

			[bankTable(width,heightList[4],account)],
			[signatureTable(width,heightList[5],stafList)],
			['']
		],
		colWidths= width,
		rowHeights= heightList
		)

	mainTable.setStyle([
		# ('GRID', (0, 0), (-1, -1), 1, 'red'),
		# ('TEXTCOLOR',(0,0),(0,0),'black'),
		# ('FONTSIZE', (0,0), (0,0), 16),
		# ('FONTNAME', (0,0), (0,0), 'Helvetica-Bold'),

		('ALIGN', (0,1), (1,1), 'RIGHT'),
		# ('VALIGN', (0,0), (0,0), 'MIDDLE'),


		('LEFTPADDING', (0, 0), (-1, -1), 50),
		('BOTTOMPADDING', (0, 0), (-1, -1), 0),
		# ('TOPADDING', (0, 3), (0, -1), 15),
		])

	mainTable.wrapOn(pdf, 0, 0)
	mainTable.drawOn(pdf, 0, 0)
	pdf.showPage()
	pdf.save()

	buf.seek(0)

	# Return something
	# return FileResponse(buf, as_attachment=True, filename='deduction.pdf')
	return HttpResponse(buf,   content_type='application/pdf')





def Membership_Front_Form_Print(request,pk):
	record=MemberShipFormSalesRecord.objects.get(receipt=pk)
	operator=request.user.username
	buf = io.BytesIO()

	pdf = canvas.Canvas(buf, pagesize = A4)
	# pdf = canvas.Canvas(buf, pagesize = landscape(A4))
	pdf.setTitle("FETHA II CTCS")

	# for font in pdf.getAvailableFonts():
	# 	print(font)


	width, height = A4
	# width, height =landscape(A4)

	heightList = [
		height * 6 / 100,
		height * 15 / 100,
		height * 3 / 100,
		height * 71 / 100,
		height * 3 / 100,
		height * 2 / 100,
	]


	mainTable = Table([
			[_membershipMainHeaderTitle()],#_registeredMembersMainHeaderTitle()
			[_membershipGenHeaderTable(width, heightList[1])], #
			[_membershipReceiptSection(width,heightList[2],pk)],#
			[_membershipGenBodyTable(width, heightList[3],pk)],#
			[_membershipGenFooterTable(width, heightList[4],operator)],#
			['']
		],
		colWidths= width,
		rowHeights= heightList
		)

	mainTable.setStyle([
		# ('GRID', (0, 0), (-1, -1), 1, 'red'),
		('TEXTCOLOR',(0,0),(0,0),'black'),
		('FONTSIZE', (0,0), (0,0), 16),
		('FONTNAME', (0,0), (0,0), 'Helvetica-Bold'),

		('ALIGN', (0,0), (0,0), 'CENTER'),
		('VALIGN', (0,0), (0,0), 'MIDDLE'),


		('LEFTPADDING', (0, 0), (0, 2), 0),
		('BOTTOMPADDING', (0, 0), (-1, -1), 0),
		])

	mainTable.wrapOn(pdf, 0, 0)
	mainTable.drawOn(pdf, 0, 0)
	pdf.showPage()
	pdf.save()

	buf.seek(0)

	# Return something
	# return FileResponse(buf, as_attachment=True, filename='venue.pdf')
	return HttpResponse(buf,   content_type='application/pdf')

def Membership_Deduction_Order_Form_Print(request,pk):
	record=MemberShipFormSalesRecord.objects.get(receipt=pk)
	operator=request.user.username
	buf = io.BytesIO()

	pdf = canvas.Canvas(buf, pagesize = A4)
	# pdf = canvas.Canvas(buf, pagesize = landscape(A4))
	pdf.setTitle("FETHA II CTCS")

	# for font in pdf.getAvailableFonts():
	# 	print(font)


	width, height = A4
	# width, height =landscape(A4)

	heightList = [
		height * 6 / 100,
		height * 10 / 100,
		height * 2 / 100,
		height * 78 / 100,
		height * 2 / 100,
		height * 2 / 100,
	]


	mainTable = Table([
			[_membershipDeductionOrderHeader()],#
			[_membershipDeductionOrderGetLogoTable(width,heightList[1])],#
			[_membershipDeductionOrderReceiptSection(width,heightList[2],pk)],#
			[_membershipDeductionOrderDeductionGenBodyTable(width,heightList[3],pk)],#
			[_membershipDeductionOrderGenFooterTable(width,heightList[4],operator)],#
			['']
		],
		colWidths= width,
		rowHeights= heightList
		)

	mainTable.setStyle([
		# ('GRID', (0, 0), (-1, -1), 1, 'red'),
		# ('TEXTCOLOR',(0,0),(0,0),'black'),
		# ('FONTSIZE', (0,0), (0,0), 16),
		# ('FONTNAME', (0,0), (0,0), 'Helvetica-Bold'),

		# ('ALIGN', (0,0), (0,0), 'CENTER'),
		# ('VALIGN', (0,0), (0,0), 'MIDDLE'),


		('LEFTPADDING', (0, 0), (-1, -1), 0),
		('BOTTOMPADDING', (0, 0), (-1, -1), 0),
		# ('TOPADDING', (0, 3), (0, -1), 15),
		])

	mainTable.wrapOn(pdf, 0, 0)
	mainTable.drawOn(pdf, 0, 0)
	pdf.showPage()
	pdf.save()

	buf.seek(0)

	# Return something
	# return FileResponse(buf, as_attachment=True, filename='deduction.pdf')
	return HttpResponse(buf,   content_type='application/pdf')



# def index(request):
#     # current_datetime = datetime.datetime.now()
#     # html = "<html><body><b>Current Date and Time Value:</b> %s</body></html>" % current_datetime
#     # return HttpResponse(html)

#     # current_time = datetime.datetime.now().strftime('%H:%M:%S')
#     # html = "<html><body><b>Current Time Value:</b> %s</body></html>" % current_time
#     # return HttpResponse(html)

#     # current_time = datetime.datetime.now().strftime('%H:%M')
#     # html = "<html><body><b>Current Time Value:</b> %s</body></html>" % current_time
#     # return HttpResponse(html)

#     # current_time = datetime.datetime.now().time()
#     # html = "<html><body><b>Current Time Value:</b> %s</body></html>" % current_time
#     # return HttpResponse(html)

#     t = time.localtime()
#     current_time = time.strftime("%H:%M", t)
#     html = "<html><body><b>Current Time Value:</b> %s</body></html>" % current_time
#     return HttpResponse(html)

def deskofficer_home(request):
	# status="ACTIVE"
	# Members.objects.all().update(status=status)
	# LoanRequest.objects.all().delete()
	# PersonalLedger.objects.all().delete()
	# CooperativeShopLedger.objects.all().delete()

	# # Members.objects.all().update(loan_status=loan_status,savings_status=savings_status)
	# Stock.objects.all().update(quantity=0,unit_cost_price=0)
	# Stock_Auction.objects.all().delete()
	# Companies.objects.all().delete()
	# Daily_Sales.objects.all().delete()
	# Daily_Sales_Item_Return.objects.all().delete()
	# Daily_Sales_Cash_Flow_Summary.objects.all().delete()
	# Day_End_Sales_Transactions.objects.all().delete()
	# ItemWriteOffTemp.objects.all().delete()
	# LoansRepaymentBase.objects.all().delete()
	# LoansUploaded.objects.all().delete()
	# MembersCashDeposits.objects.all().delete()
	# Members_Commodity_Loan_Application.objects.all().delete()
	# MonthlyDeductionGenerationHeading.objects.all().delete()
	# MonthlyGroupGeneratedTransactions.objects.all().delete()
	# MonthlyGeneratedTransactions.objects.all().delete()
	# MonthlyDeductionGenerationHeading.objects.all().delete()
	# MonthlyJointDeductionList.objects.all().delete()
	# MonthlyJointDeductionGeneratedTransactions.objects.all().delete()
	# MonthlyJointDeductionGenerated.objects.all().delete()
	# NonMemberAccountDeductions.objects.all().delete()
	# MonthlyShopGroupGeneratedTransactions.objects.all().delete()
	# Purchases.objects.all().delete()
	# Customers.objects.all().delete()
	# Xmas_Savings_Generated.objects.all().delete()
	# Expenditures.objects.all().delete()
	# Expenditures_Dialy_Summary.objects.all().delete()
	# Expenditures_Day_End_Summary.objects.all().delete()
	# Expenditures_Month_End_Summary.objects.all().delete()
	# Expenditures_Year_End_Summary.objects.all().delete()
	# Daily_Cash_Deposit_Year_End_Transaction.objects.all().delete()
	# Daily_Cash_Deposit_Month_End_Transaction.objects.all().delete()
	# Daily_Cash_Deposit_Day_End_Transaction.objects.all().delete()
	# Daily_Cash_Deposit_Summary.objects.all().delete()
	# Purchases_Year_End_Transaction.objects.all().delete()
	# Purchases_Day_End_Transaction.objects.all().delete()
	# Purchases_Month_End_Transaction.objects.all().delete()
	# members_credit_loans_Cash_Receipt_Month_End_Transaction.objects.all().delete()
	# members_credit_loans_Cash_Receipt_Year_End_Transaction.objects.all().delete()
	# members_credit_loans_Cash_Receipt_Day_End_Transaction.objects.all().delete()
	# Cooperative_Shop_Cash_Deposit.objects.all().delete()
	# Cooperative_Shop_Cash_Deposit_Distributions.objects.all().delete()
	# ItemWriteOff.objects.all().delete()
	# members_credit_loans_Cash_Receipt.objects.all().delete()
	# members_credit_loans_Cash_Receipt_Daily_Summary.objects.all().delete()
	# members_credit_loans_Cash_Receipt_Day_End_Transaction.objects.all().delete()
	# members_credit_loans_Cash_Receipt_Month_End_Transaction.objects.all().delete()
	# members_credit_loans_Cash_Receipt_Year_End_Transaction.objects.all().delete()
	# Members_Credit_Sales_Selected.objects.all().delete()
	# members_shop_credit_loans.objects.all().delete()
	# Month_End_Sales_Transactions.objects.all().delete()
	# Purchase_Header.objects.all().delete()
	# Daily_Sales_Item_Return_Selection.objects.all().delete()
	# Daily_Sales_Item_Return_Year_End_Transaction.objects.all().delete()
	# Daily_Sales_Item_Return_Month_End_Transaction.objects.all().delete()
	# Daily_Sales_Item_Return_Day_End_Transaction.objects.all().delete()
	# Daily_Sales_Item_Return_Cash_Flow_Summary.objects.all().delete()



	# CooperativeBankAccounts.objects.all().delete()
	# Commodity_Period_Batch.objects.all().delete()
	# Commodity_Period.objects.all().delete()
	# Commodity_Categories.objects.all().delete()
	# CashBook_Shop.objects.all().delete()
	# CashBook_Main.objects.all().delete()
	# Receipts_Shop.objects.all().update(status='UNUSED')
	# Receipts.objects.all().update(status='UNUSED')
	# MembersIdManager.objects.all().update(member_id=1)
	# LoanNumber.objects.all().update(code=1)
	# AutoReceipt.objects.all().update(receipt=1)
	# AccountDeductions.objects.filter().delete()
	# NorminalRoll.objects.all().delete()
	# MemberShipRequest.objects.all().delete()
	# CustomUser.objects.filter(user_type='5').delete()
	# return HttpResponse("ok")

# System_Users_Tasks_Model user

	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	task_array=[]
	for task in tasks:
		task_array.append(task.task.title)


	task_enabler=TransactionEnabler.objects.filter(status='YES')
	task_enabler_array=[]
	for item in task_enabler:
		task_enabler_array.append(item.title)

	default_password="NO"
	if Staff.objects.filter(admin=request.user,default_password='YES'):
		default_password="YES"

	member_count=Members.objects.filter(status='ACTIVE').count()



	applicants=MemberShipRequest.objects.filter(transaction_status='UNTREATED',approval_status='APPROVED').count()

	title="System User"

	context={
	'task_enabler_array':task_enabler_array,
	'default_password':default_password,
	'task_array':task_array,
	'applicants':applicants,
	'title':title,
	'member_count':member_count,
	}
	return render(request, "deskofficer_templates/dashboard.html",context)


def desk_basic_form(request):
	return render(request, 'deskofficer_templates/basics/basic_form1.html')

def desk_advanced_form(request):
	return render(request, 'deskofficer_templates/basics/advanced_form.html')


def desk_basic_table(request):
	return render(request, 'deskofficer_templates/basics/basic_tables.html')

def desk_datatable_table(request):
	return render(request, 'deskofficer_templates/basics/datatable.html')


# def desk_form_validation(request):
# 	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
# 	task_array=[]
# 	for task in tasks:
# 		task_array.append(task.task.title)


# 	task_enabler=TransactionEnabler.objects.filter(status="YES")
# 	task_enabler_array=[]
# 	for item in task_enabler:
# 		task_enabler_array.append(item.title)

# 	context={
# 	'task_array':task_array,
# 	'task_enabler_array':task_enabler_array,
	# 'default_password':default_password,
# 	}

# 	return render(request, 'deskofficer_templates/basics/form_validation.html',context)


@csrf_exempt
def check_receipt_no_already_used(request):
	receipt_no=request.POST.get("receipt_no")
	receipt_no_obj=Receipts.objects.filter(receipt=receipt_no,status='USED').exists()
	if receipt_no_obj:
		return HttpResponse(True)
	else:
		return  HttpResponse(False)


#########################################################
############### PROFILE MANAGER #########################
#########################################################
def Useraccount_manager(request):
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	task_array=[]
	for task in tasks:
		task_array.append(task.task.title)

	task_enabler=TransactionEnabler.objects.filter(status='YES')
	task_enabler_array=[]
	for item in task_enabler:
		task_enabler_array.append(item.title)

	default_password="NO"
	if Staff.objects.filter(admin=request.user,default_password='YES'):
		default_password="YES"

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

		Staff.objects.filter(admin=request.user).update(default_password='NO')

		user.set_password(password1)
		user.save()
		return HttpResponseRedirect(reverse('Useraccount_manager'))

	context={
	'form':form,
	'task_array':task_array,
	'task_enabler_array':task_enabler_array,
	'default_password':default_password,
	}
	return render(request,'deskofficer_templates/Useraccount_manager.html',context)


#########################################################
############### MEMBERSHIP TASK #########################
#########################################################

def membership_request(request):
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	task_array=[]
	for task in tasks:
		task_array.append(task.task.title)


	task_enabler=TransactionEnabler.objects.filter(status='YES')
	task_enabler_array=[]
	for item in task_enabler:
		task_enabler_array.append(item.title)

	default_password="NO"
	if Staff.objects.filter(admin=request.user,default_password='YES'):
		default_password="YES"


	form=MembershipRequest_form(request.POST or None)
	if request.method=="POST":

		tdate=get_current_date(now)

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
		record=MemberShipRequest(transaction_status='UNTREATED',
								submission_status='PENDING',
								approval_status='PENDING',
								tdate=tdate,title=title,
								first_name=first_name,
								last_name=last_name,
								middle_name=middle_name,
								phone_number=phone_no,
								gender=gender,
								department=department,
								processed_by=processed_by.username)
		record.save()


		return HttpResponseRedirect(reverse('membership_request_additional_info',args=(record.pk,)))

	context={
	'form':form,
	'task_array':task_array,
	'task_enabler_array':task_enabler_array,
	'default_password':default_password,
	}
	return render(request, 'deskofficer_templates/membership_request.html',context)


def membership_request_complete_search(request):
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	task_array=[]
	for task in tasks:
		task_array.append(task.task.title)



	task_enabler=TransactionEnabler.objects.filter(status='YES')
	task_enabler_array=[]
	for item in task_enabler:
		task_enabler_array.append(item.title)

	default_password="NO"
	if Staff.objects.filter(admin=request.user,default_password='YES'):
		default_password="YES"

	title="Search Membership Request Completion"
	form = searchForm(request.POST or None)

	return render(request,'deskofficer_templates/membership_request_complete_search.html',{'form':form,'title':title,'task_array':task_array})


def membership_request_complete_load(request):
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	task_array=[]
	for task in tasks:
		task_array.append(task.task.title)



	task_enabler=TransactionEnabler.objects.filter(status='YES')
	task_enabler_array=[]
	for item in task_enabler:
		task_enabler_array.append(item.title)

	default_password="NO"
	if Staff.objects.filter(admin=request.user,default_password='YES'):
		default_password="YES"

	title="Complete Membership Request"
	form = searchForm(request.POST)

	if request.method == "POST":
		if request.POST.get("title")=="":
			return HttpResponseRedirect(reverse('membership_request_complete_search'))

		members=MemberShipRequest.objects.filter(Q(phone_number__icontains=form['title'].value()) | Q(first_name__icontains=form['title'].value()) | Q(last_name__icontains=form['title'].value()) | Q(middle_name__icontains=form['title'].value())).filter(submission_status='PENDING')

	context={
	'members':members,
	'title':title,
	'task_array':task_array,
	'task_enabler_array':task_enabler_array,
	'default_password':default_password,
	}
	return render(request,'deskofficer_templates/membership_request_complete_list_load.html',context)


def membership_request_additional_info(request,pk):
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	task_array=[]
	for task in tasks:
		task_array.append(task.task.title)


	task_enabler=TransactionEnabler.objects.filter(status='YES')
	task_enabler_array=[]
	for item in task_enabler:
		task_enabler_array.append(item.title)

	default_password="NO"
	if Staff.objects.filter(admin=request.user,default_password='YES'):
		default_password="YES"

	applicant=MemberShipRequest.objects.get(id=pk)
	officer=CustomUser.objects.get(id=request.user.id)

	records=MemberShipRequestAdditionalInfo.objects.filter(officer=officer,applicant=applicant)

	attached_infos=MemberShipRequestAdditionalAttachment.objects.filter(officer=officer,applicant=applicant)

	comment_form =MemberShipRequestAdditionalInfo_form(request.POST or None)
	attachment_form =MemberShipRequestAdditionalAttachment_form(request.POST or None)

	context={
	'comment_form':comment_form,
	'attachment_form':attachment_form,
	'pk':pk,
	'records':records,
	'attached_infos':attached_infos,
	'task_array':task_array,
	'task_enabler_array':task_enabler_array,
	'default_password':default_password,
	}
	return render(request,'deskofficer_templates/membership_request_additional_info.html',context)


def membership_request_additional_info_save(request,pk):
	applicant=MemberShipRequest.objects.get(id=pk)
	officer=CustomUser.objects.get(id=request.user.id)

	comment = request.POST.get('comment')
	if not comment:
		messages.error(request,'Please Enter Comment')
		return HttpResponseRedirect(reverse('membership_request_additional_info',args=(pk,)))

	record=MemberShipRequestAdditionalInfo(comment=comment,officer=officer,applicant=applicant)
	record.save()
	messages.success(request,"Record Added Successfully")
	return HttpResponseRedirect(reverse('membership_request_additional_info',args=(pk,)))


def membership_request_additional_info_update(request,pk):
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	task_array=[]
	for task in tasks:
		task_array.append(task.task.title)


	task_enabler=TransactionEnabler.objects.filter(status='YES')
	task_enabler_array=[]
	for item in task_enabler:
		task_enabler_array.append(item.title)

	default_password="NO"
	if Staff.objects.filter(admin=request.user,default_password='YES'):
		default_password="YES"

	form=MemberShipRequestAdditionalInfo_form(request.POST or None)
	record=MemberShipRequestAdditionalInfo.objects.get(id=pk)
	form.fields['comment'].initial=record.comment

	if request.method == "POST":
		comment=request.POST.get('comment')
		record.comment=comment
		record.save()
		return HttpResponseRedirect(reverse('membership_request_additional_info',args=(record.applicant.pk,)))
	context={
	'form':form,
	'record':record,
	}
	return render(request,'deskofficer_templates/membership_request_additional_info_update.html',context)




def membership_request_additional_info_delete_confirm(request,pk,return_pk):
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	task_array=[]
	for task in tasks:
		task_array.append(task.task.title)



	task_enabler=TransactionEnabler.objects.filter(status="task_status")
	task_enabler_array=[]
	for item in task_enabler:
		task_enabler_array.append(item.title)

	default_password="NO"
	if Staff.objects.filter(admin=request.user,default_password='YES'):
		default_password="YES"

	comment=MemberShipRequestAdditionalInfo.objects.get(id=pk)


	context={
	'comment':comment,
	'pk':pk,
	'return_pk':return_pk,
	'task_array':task_array,
	'task_enabler_array':task_enabler_array,
	'default_password':default_password,
	}
	return render(request,'deskofficer_templates/membership_request_additional_info_delete_confirm.html',context)




def membership_request_additional_info_delete(request,pk,return_pk):
	comment=MemberShipRequestAdditionalInfo.objects.get(id=pk)
	comment.delete()
	return HttpResponseRedirect(reverse('membership_request_additional_info',args=(return_pk,)))


def MemberShipRequestAdditionalAttachment_save(request,pk):
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	task_array=[]
	for task in tasks:
		task_array.append(task.task.title)



	task_enabler=TransactionEnabler.objects.filter(status="YES")
	task_enabler_array=[]
	for item in task_enabler:
		task_enabler_array.append(item.title)

	default_password="NO"
	if Staff.objects.filter(admin=request.user,default_password='YES'):
		default_password="YES"

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
	if not caption:
		messages.error(request,'Please Enter attachment caption')
		return HttpResponseRedirect(reverse('membership_request_additional_info',args=(pk,)))

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




def MemberShipRequestAdditionalAttachment_info_delete_confirm(request,pk,return_pk):
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	task_array=[]
	for task in tasks:
		task_array.append(task.task.title)



	task_enabler=TransactionEnabler.objects.filter(status="YES")
	task_enabler_array=[]
	for item in task_enabler:
		task_enabler_array.append(item.title)

	default_password="NO"
	if Staff.objects.filter(admin=request.user,default_password='YES'):
		default_password="YES"

	comment=MemberShipRequestAdditionalAttachment.objects.get(id=pk)
	title="Delete Records for " + comment.applicant.get_full_name

	context={
	'comment':comment,
	'pk':pk,
	'return_pk':return_pk,
	'title':title,
	'task_array':task_array,
	'task_enabler_array':task_enabler_array,
	'default_password':default_password,
	}
	return render(request,'deskofficer_templates/MemberShipRequestAdditionalAttachment_info_delete_confirm.html',context)




def MemberShipRequestAdditionalAttachment_info_delete(request,pk,return_pk):
	comment=MemberShipRequestAdditionalAttachment.objects.get(id=pk)
	comment.delete()
	return HttpResponseRedirect(reverse('membership_request_additional_info',args=(return_pk,)))


def MemberShipRequest_Delete_confirmation(request,pk):
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	task_array=[]
	for task in tasks:
		task_array.append(task.task.title)



	task_enabler=TransactionEnabler.objects.filter(status="YES")
	task_enabler_array=[]
	for item in task_enabler:
		task_enabler_array.append(item.title)

	default_password="NO"
	if Staff.objects.filter(admin=request.user,default_password='YES'):
		default_password="YES"

	title="Delete Applicant"
	applicant=MemberShipRequest.objects.get(id=pk)


	context={
	'title':title,
	'applicant':applicant,
	}
	return render(request,'deskofficer_templates/MemberShipRequest_Delete_confirmation.html',context)


def MemberShipRequest_Delete(request,pk):
	applicant=MemberShipRequest.objects.get(id=pk)
	applicant.delete()
	return HttpResponseRedirect(reverse('membership_request_complete_search'))


def MemberShipRequest_submit(request,pk):
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	task_array=[]
	for task in tasks:
		task_array.append(task.task.title)



	task_enabler=TransactionEnabler.objects.filter(status="YES")
	task_enabler_array=[]
	for item in task_enabler:
		task_enabler_array.append(item.title)

	default_password="NO"
	if Staff.objects.filter(admin=request.user,default_password='YES'):
		default_password="YES"

	submission_status="SUBMITTED"
	record=MemberShipRequest.objects.get(id=pk)
	record.submission_status=submission_status
	record.save()
	messages.success(request,"Record Successfully Updated")
	return HttpResponseRedirect(reverse('deskofficer_home'))


def membership_request_manage_search(request):
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	task_array=[]
	for task in tasks:
		task_array.append(task.task.title)



	task_enabler=TransactionEnabler.objects.filter(status="YES")
	task_enabler_array=[]
	for item in task_enabler:
		task_enabler_array.append(item.title)

	default_password="NO"
	if Staff.objects.filter(admin=request.user,default_password='YES'):
		default_password="YES"


	title="Search Membership Request for Update"
	form = searchForm(request.POST or None)

	return render(request,'deskofficer_templates/membership_request_manage_search.html',{'form':form,'title':title,'task_array':task_array,
	'task_enabler_array':task_enabler_array,
	'default_password':default_password,})


def membership_request_manage_list_load(request):
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	task_array=[]
	for task in tasks:
		task_array.append(task.task.title)



	task_enabler=TransactionEnabler.objects.filter(status="YES")
	task_enabler_array=[]
	for item in task_enabler:
		task_enabler_array.append(item.title)

	default_password="NO"
	if Staff.objects.filter(admin=request.user,default_password='YES'):
		default_password="YES"

	title="Update Membership Request"
	form = searchForm(request.POST)

	if request.method == "POST":
		if request.POST.get("title")=="":
			return HttpResponseRedirect(reverse('membership_request_manage_search'))


		members=MemberShipRequest.objects.filter(Q(phone_number__icontains=form['title'].value()) | Q(first_name__icontains=form['title'].value()) | Q(last_name__icontains=form['title'].value()) | Q(middle_name__icontains=form['title'].value())).filter(submission_status='SUBMITTED',approval_status='PENDING')
		if not members:
			messages.error(request,'No Record Found')
			return HttpResponseRedirect(reverse('membership_request_manage_search'))

	context={
	'members':members,
	'title':title,
	'task_array':task_array,
	'task_enabler_array':task_enabler_array,
	'default_password':default_password,
	}
	return render(request,'deskofficer_templates/membership_request_manage_list_load.html',context)


def membership_request_manage_details(request,pk):
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	task_array=[]
	for task in tasks:
		task_array.append(task.task.title)



	task_enabler=TransactionEnabler.objects.filter(status="YES")
	task_enabler_array=[]
	for item in task_enabler:
		task_enabler_array.append(item.title)

	default_password="NO"
	if Staff.objects.filter(admin=request.user,default_password='YES'):
		default_password="YES"


	form=MembershipRequest_form(request.POST or None)
	record=MemberShipRequest.objects.get(id=pk)

	attachment=MemberShipRequestAdditionalAttachment.objects.filter(applicant_id=pk)
	comment=MemberShipRequestAdditionalInfo.objects.filter(applicant_id=pk)
	form.fields['titles'].initial=record.title.id
	form.fields['first_name'].initial=record.first_name
	form.fields['last_name'].initial=record.last_name
	form.fields['middle_name'].initial=record.middle_name
	form.fields['phone_no'].initial=record.phone_number
	form.fields['gender'].initial=record.gender.id
	form.fields['department'].initial=record.department.id

	if request.method == "POST":
		title_id=request.POST.get("titles")
		title=Titles.objects.get(id=title_id)

		first_name=request.POST.get("first_name").upper()
		last_name=request.POST.get("last_name").upper()
		middle_name=request.POST.get("middle_name").upper()
		phone_number=request.POST.get("phone_no")

		gender_id=request.POST.get("gender")
		gender=Gender.objects.get(id=gender_id)

		department_id=request.POST.get("department")
		department=Departments.objects.get(id=department_id)
		record.title=title
		record.first_name=first_name
		record.last_name=last_name
		record.middle_name=middle_name
		record.phone_number=phone_number
		record.gender=gender
		record.department=department
		record.save()
		messages.success(request,'Personnel Record Updated Successfully')
		return HttpResponseRedirect(reverse('membership_request_manage_details',args=(pk,)))

	context={
	'form':form,
	'attachment':attachment,
	'comment':comment,
	'record':record,
	'task_array':task_array,
	'task_enabler_array':task_enabler_array,
	'default_password':default_password,
	}
	return render(request,'deskofficer_templates/membership_request_manage_details.html',context)


def membership_request_manage_details_edit_comment(request,pk):
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	task_array=[]
	for task in tasks:
		task_array.append(task.task.title)



	task_enabler=TransactionEnabler.objects.filter(status="YES")
	task_enabler_array=[]
	for item in task_enabler:
		task_enabler_array.append(item.title)

	default_password="NO"
	if Staff.objects.filter(admin=request.user,default_password='YES'):
		default_password="YES"


	form=MemberShipRequestAdditionalInfo_form(request.POST or None)
	record=MemberShipRequestAdditionalInfo.objects.get(id=pk)
	title='Update Comment'
	button_text="Update"
	form.fields['comment'].initial=record.comment
	if request.method == 'POST':
		comment=request.POST.get('comment')
		record.comment=comment
		record.save()
		messages.success(request,'Comment Updated Successfully')
		return HttpResponseRedirect(reverse('membership_request_manage_details',args=(record.applicant_id,)))
	context={
	'form':form,
	'record':record,
	'title':title,
	'button_text':button_text,

	'task_array':task_array,
	'task_enabler_array':task_enabler_array,
	'default_password':default_password,
	}
	return render(request,'deskofficer_templates/membership_request_manage_details_edit_comment.html',context)



def membership_request_manage_details_delete_comment(request,pk):
	record=MemberShipRequestAdditionalInfo.objects.get(id=pk)
	return_pk=record.applicant_id
	record.delete()
	messages.info(request,'Comment Deleted Successfully')
	return HttpResponseRedirect(reverse('membership_request_manage_details',args=(return_pk,)))


def membership_request_manage_details_add_comment(request,pk):
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	task_array=[]
	for task in tasks:
		task_array.append(task.task.title)



	task_enabler=TransactionEnabler.objects.filter(status="YES")
	task_enabler_array=[]
	for item in task_enabler:
		task_enabler_array.append(item.title)

	default_password="NO"
	if Staff.objects.filter(admin=request.user,default_password='YES'):
		default_password="YES"


	form=MemberShipRequestAdditionalInfo_form(request.POST or None)
	title="Add Comment"
	button_text="Add"
	applicant=MemberShipRequest.objects.get(id=pk)
	officer=CustomUser.objects.get(id=request.user.id)
	if request.method == 'POST':
		comment=request.POST.get('comment')
		MemberShipRequestAdditionalInfo(comment=comment,applicant=applicant,officer=officer).save()

		messages.success(request,'Comment added Successfully')
		return HttpResponseRedirect(reverse('membership_request_manage_details',args=(pk,)))
	context={
	'form':form,
	'title':title,
	'button_text':button_text,
	'task_array':task_array,
	'task_enabler_array':task_enabler_array,
	'default_password':default_password,

	}
	return render(request,'deskofficer_templates/membership_request_manage_details_edit_comment.html',context)



def membership_request_manage_details_edit_attachment(request,pk):
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	task_array=[]
	for task in tasks:
		task_array.append(task.task.title)



	task_enabler=TransactionEnabler.objects.filter(status="YES")
	task_enabler_array=[]
	for item in task_enabler:
		task_enabler_array.append(item.title)

	default_password="NO"
	if Staff.objects.filter(admin=request.user,default_password='YES'):
		default_password="YES"


	form =MemberShipRequestAdditionalAttachment_form(request.POST or None)
	record=MemberShipRequestAdditionalAttachment.objects.get(id=pk)
	button_text="Update"
	form.fields['caption'].initial=record.caption

	if request.method=="POST":
		if request.FILES.get('image', False):
			image = request.FILES['image']
			fs=FileSystemStorage()
			filename=fs.save(image.name,image)
			image_url=fs.url(filename)

		else:
			image_url=None

		caption=request.POST.get('caption')

		edit_image = request.POST.get('edit_image')
		if edit_image:
			record.image=image_url
		record.caption=caption
		record.save()
		messages.success(request,'Attachment Updated Successfully')
		return HttpResponseRedirect(reverse('membership_request_manage_details',args=(record.applicant_id,)))
	context={
	'form':form,
	'button_text':button_text,
	'record':record,

	'task_array':task_array,
	'task_enabler_array':task_enabler_array,
	'default_password':default_password,

	}
	return render(request,'deskofficer_templates/membership_request_manage_details_edit_attachment.html',context)


def membership_request_manage_details_edit_attachment_delete(request,pk):
	record=MemberShipRequestAdditionalAttachment.objects.get(id=pk)
	return_pk=record.applicant_id
	record.delete()
	messages.info(request,'Attachment Deleted Successfully')
	return HttpResponseRedirect(reverse('membership_request_manage_details',args=(return_pk,)))


def membership_request_manage_details_edit_attachment_add(request,pk):
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	task_array=[]
	for task in tasks:
		task_array.append(task.task.title)



	task_enabler=TransactionEnabler.objects.filter(status="YES")
	task_enabler_array=[]
	for item in task_enabler:
		task_enabler_array.append(item.title)


	default_password="NO"
	if Staff.objects.filter(admin=request.user,default_password='YES'):
		default_password="YES"

	form =MemberShipRequestAdditionalAttachment_form(request.POST or None)
	applicant=MemberShipRequest.objects.get(id=pk)
	officer=CustomUser.objects.get(id=request.user.id)
	if request.method=="POST":
		if request.FILES.get('image', False):
			image = request.FILES['image']
			fs=FileSystemStorage()
			filename=fs.save(image.name,image)
			image_url=fs.url(filename)

		else:
			image_url=None

		caption=request.POST.get('caption')
		MemberShipRequestAdditionalAttachment(officer=officer,caption=caption,image=image_url,applicant=applicant).save()
		messages.info(request,'Attachment added Successfully')
		return HttpResponseRedirect(reverse('membership_request_manage_details',args=(pk,)))
	context={
	'form':form,

	'task_array':task_array,
	'task_enabler_array':task_enabler_array,
	'default_password':default_password,

	}
	return render(request,'deskofficer_templates/membership_request_manage_details_edit_attachment_add.html',context)


def membership_request_delete_confirmation(request,pk):
	title='Are you sure you want to delete the request'
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	task_array=[]
	for task in tasks:
		task_array.append(task.task.title)



	task_enabler=TransactionEnabler.objects.filter(status="YES")
	task_enabler_array=[]
	for item in task_enabler:
		task_enabler_array.append(item.title)

	default_password="NO"
	if Staff.objects.filter(admin=request.user,default_password='YES'):
		default_password="YES"

	member=MemberShipRequest.objects.get(id=pk)

	context={
	'title':title,
	'member':member,

	'task_array':task_array,
	'task_enabler_array':task_enabler_array,
	'default_password':default_password,

	}
	return render(request,'deskofficer_templates/membership_request_delete_confirmation.html',context)


def membership_request_delete(request,pk):
	member=MemberShipRequest.objects.get(id=pk)
	member.delete()

	return HttpResponseRedirect(reverse('membership_request_manage_search'))

def membership_form_sales_Search(request):
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	task_array=[]
	for task in tasks:
		task_array.append(task.task.title)



	task_enabler=TransactionEnabler.objects.filter(status="YES")
	task_enabler_array=[]
	for item in task_enabler:
		task_enabler_array.append(item.title)

	default_password="NO"
	if Staff.objects.filter(admin=request.user,default_password='YES'):
		default_password="YES"

	title="Search Applicants for Form Sales"
	form = searchForm(request.POST or None)

	return render(request,'deskofficer_templates/membership_form_sales_Search.html',{'form':form,'title':title,'task_array':task_array,
	'task_enabler_array':task_enabler_array,
	'default_password':default_password,})


def membership_form_sales_list_load(request):
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	task_array=[]
	for task in tasks:
		task_array.append(task.task.title)



	task_enabler=TransactionEnabler.objects.filter(status="YES")
	task_enabler_array=[]
	for item in task_enabler:
		task_enabler_array.append(item.title)

	default_password="NO"
	if Staff.objects.filter(admin=request.user,default_password='YES'):
		default_password="YES"


	form = searchForm(request.POST)
	applicants=[]
	if request.method == "POST":
		if not form['title'].value():
			return HttpResponseRedirect(reverse('membership_form_sales_Search'))

		applicants=MemberShipRequest.objects.filter(Q(phone_number__icontains=form['title'].value()) | Q(first_name__icontains=form['title'].value()) | Q(last_name__icontains=form['title'].value()) | Q(middle_name__icontains=form['title'].value())).filter(transaction_status='UNTREATED',approval_status='APPROVED')

		if not applicants:
			messages.error(request,'No Record Found')
			return HttpResponseRedirect(reverse('membership_form_sales_Search'))



	context={
	'applicants':applicants,
	'task_array':task_array,
	'task_enabler_array':task_enabler_array,
	'default_password':default_password,
	}
	return render(request,'deskofficer_templates/membership_form_sales_list_load.html',context)




def membership_form_sales_preview(request,pk):
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	task_array=[]
	for task in tasks:
		task_array.append(task.task.title)



	task_enabler=TransactionEnabler.objects.filter(status="YES")
	task_enabler_array=[]
	for item in task_enabler:
		task_enabler_array.append(item.title)

	default_password="NO"
	if Staff.objects.filter(admin=request.user,default_password='YES'):
		default_password="YES"

	applicant=MemberShipRequest.objects.get(pk=pk)
	comments=MemberShipRequestAdditionalInfo.objects.filter(applicant_id=pk)
	attachments=MemberShipRequestAdditionalAttachment.objects.filter(applicant_id=pk)

	context={
	'applicant':applicant,
	'comments':comments,
	'attachments':attachments,
	'task_array':task_array,
	'task_enabler_array':task_enabler_array,
	'default_password':default_password,
	}
	return render(request,'deskofficer_templates/membership_form_sales_preview.html',context)


def membership_form_sales_issue(request,pk):
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	task_array=[]
	for task in tasks:
		task_array.append(task.task.title)

	task_enabler=TransactionEnabler.objects.filter(status="YES")
	task_enabler_array=[]
	for item in task_enabler:
		task_enabler_array.append(item.title)

	default_password="NO"
	if Staff.objects.filter(admin=request.user,default_password='YES'):
		default_password="YES"

	form=membership_form_sales_issue_form(request.POST or None)
	tdate = get_current_date(now)

	applicant=MemberShipRequest.objects.get(id=pk)
	account=[]
	account_name=[]
	if CooperativeBankAccountsOperationalDesignations.objects.filter(transaction__code='100').exists():
		account = CooperativeBankAccountsOperationalDesignations.objects.get(transaction__code='100')
		account_name = account.account.account_name + ' - ' + str(account.account.account_number) + ' - ' + str(account.account.bank)

	shares_uint_cost=0
	if MembersShareConfigurations.objects.all().exists():
		shares = MembersShareConfigurations.objects.first()
		if shares:
			shares_uint_cost=shares.unit_cost
		else:
			messages.error(request,'Shares Unit Cost Not Set')
			return HttpResponseRedirect(reverse('membership_form_sales_preview',args=(pk,)))
	else:
		messages.error(request,'Shares Unit Cost Not Set')
		return HttpResponseRedirect(reverse('membership_form_sales_preview',args=(pk,)))

	welfare=0
	if MembersWelfare.objects.all().exists():
		welfare_obj=MembersWelfare.objects.first()
		welfare=welfare_obj.amount
	else:
		messages.error(request,'Welfare Amount Not Set')
		return HttpResponseRedirect(reverse('membership_form_sales_preview',args=(pk,)))

	admin_charge = TransactionTypes.objects.get(code='100')
	registration_fees=admin_charge.admin_charges

	if not registration_fees:
		messages.error(request,'Registration Fees Not Set')
		return HttpResponseRedirect(reverse('membership_form_sales_preview',args=(pk,)))

	receipt_type='MANUAL'

	receipt_types_status=False
	if admin_charge.receipt_type == receipt_type:
		receipt_types_status=True


	if request.method=="POST":

		processed_by=CustomUser.objects.get(id=request.user.id)

		date_paid=request.POST.get("date_paid")


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
			if Receipts.objects.filter(receipt=receipt_id).exists():

				receipt_obj=Receipts.objects.get(receipt=receipt_id)
				receipt=receipt_obj.receipt
			else:
				messages.error(request,"Receipt Number Not Found")
				return HttpResponseRedirect(reverse('membership_form_sales_issue',args=(pk,)))


			if Receipts.objects.filter(receipt=receipt_id,status='USED').exists():
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

		record=MemberShipFormSalesRecord(date_paid=date_paid,total_amount=amount_due,tdate=tdate,payment_reference=payment_reference,image=image_url,bank_ccount=account.account,welfare_amount=welfare,receipt=receipt,applicant=applicant,shares=share_unit,share_amount=total_shares,admin_charge=registration_fees,processed_by=processed_by.username,status="UNTREATED",new_registration=True,cashbook_status='UNPOSTED')
		record.save()

		if receipt_types_status==True:
			receipt_obj.status='USED'
			receipt_obj.save()
		else:
			receipt_id.receipt= int(receipt_id.receipt) + 1
			receipt_id.save()

		applicant.transaction_status='TREATED'
		applicant.save()


		return HttpResponseRedirect(reverse('membership_form_sales_validation', args=(receipt,)))



	form.fields['account_name'].initial=account_name
	form.fields['share_unit_cost'].initial=shares_uint_cost
	form.fields['welfare'].initial=welfare
	form.fields['registration_fees'].initial=registration_fees
	form.fields['amount_paid'].initial=float(shares_uint_cost)+float(registration_fees)+float(welfare)
	form.fields['receipt'].initial=0
	form.fields['form_print'].initial=0
	form.fields['date_paid'].initial=now

	context={
	'form':form,
	'applicant':applicant,
	'receipt_types_status':receipt_types_status,
	'shares_uint_cost':shares_uint_cost,
	'task_array':task_array,
	'task_enabler_array':task_enabler_array,
	'default_password':default_password,
	}
	return render(request,'deskofficer_templates/membership_form_sales_issue.html',context)




def membership_form_sales_validation(request,pk):
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	task_array=[]
	for task in tasks:
		task_array.append(task.task.title)


	task_enabler=TransactionEnabler.objects.filter(status="YES")
	task_enabler_array=[]
	for item in task_enabler:
		task_enabler_array.append(item.title)

	default_password="NO"
	if Staff.objects.filter(admin=request.user,default_password='YES'):
		default_password="YES"

	record=MemberShipFormSalesRecord.objects.get(receipt=pk)
	context={
	'record':record,
	'task_array':task_array,
	'task_enabler_array':task_enabler_array,
	'default_password':default_password,
	}

	return render(request,'deskofficer_templates/membership_form_sales_validation.html',context)


def membership_registration_applicant_search(request):
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	task_array=[]
	for task in tasks:
		task_array.append(task.task.title)



	task_enabler=TransactionEnabler.objects.filter(status="YES")
	task_enabler_array=[]
	for item in task_enabler:
		task_enabler_array.append(item.title)


	default_password="NO"
	if Staff.objects.filter(admin=request.user,default_password='YES'):
		default_password="YES"

	title="Search Membership Request for Update"
	form = searchForm(request.POST or None)
	return render(request,'deskofficer_templates/membership_registration_applicant_search.html',{'form':form,'title':title,'task_array':task_array,
	'task_enabler_array':task_enabler_array,
	'default_password':default_password,})



def membership_registration_applicant_list_load(request):
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	task_array=[]
	for task in tasks:
		task_array.append(task.task.title)



	task_enabler=TransactionEnabler.objects.filter(status="YES")
	task_enabler_array=[]
	for item in task_enabler:
		task_enabler_array.append(item.title)

	default_password="NO"
	if Staff.objects.filter(admin=request.user,default_password='YES'):
		default_password="YES"


	title="Update Membership Request"
	form = searchForm(request.POST)

	if request.method == "POST":
		if not request.POST.get("title"):
			return HttpResponseRedirect(reverse('membership_registration_applicant_search'))

		applicants=MemberShipFormSalesRecord.objects.filter(Q(applicant__phone_number__icontains=form['title'].value()) | Q(applicant__first_name__icontains=form['title'].value()) | Q(applicant__last_name__icontains=form['title'].value()) | Q(applicant__middle_name__icontains=form['title'].value())).filter(status='UNTREATED')
		if not applicants:
			messages.error(request,'No Record Found')
			return HttpResponseRedirect(reverse('membership_registration_applicant_search'))

	context={
	'applicants':applicants,
	'title':title,
	'task_array':task_array,
	'task_enabler_array':task_enabler_array,
	'default_password':default_password,
	}
	return render(request,'deskofficer_templates/membership_registration_applicant_list_load.html',context)




def membership_registration_register_confirmation(request,pk):
	record=Members.objects.get(ippis_no=pk)
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	task_array=[]
	for task in tasks:
		task_array.append(task.task.title)



	task_enabler=TransactionEnabler.objects.filter(status="YES")
	task_enabler_array=[]
	for item in task_enabler:
		task_enabler_array.append(item.title)

	default_password="NO"
	if Staff.objects.filter(admin=request.user,default_password='YES'):
		default_password="YES"

	context={
	'record':record,
	# 'title':title,
	'task_array':task_array,
	'task_enabler_array':task_enabler_array,
	'default_password':default_password,
	}
	return render(request,'deskofficer_templates/membership_registration_register_confirmation.html',context)


def membership_registration_register(request,pk):
	applicant=MemberShipFormSalesRecord.objects.get(id=pk)
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	task_array=[]
	for task in tasks:
		task_array.append(task.task.title)



	task_enabler=TransactionEnabler.objects.filter(status="YES")
	task_enabler_array=[]
	for item in task_enabler:
		task_enabler_array.append(item.title)

	default_password="NO"
	if Staff.objects.filter(admin=request.user,default_password='YES'):
		default_password="YES"

	form= membership_registration_register_form(request.POST or None)

	if request.method == 'POST':
		tdate=get_current_date(now)
		processed_by = CustomUser.objects.get(id=request.user.id)
		applicant=MemberShipFormSalesRecord.objects.get(id=pk)

		shares=applicant.shares
		unit_cost=math.ceil(float(applicant.share_amount)/float(applicant.shares))
		total_cost=applicant.share_amount
		welfare_amount=applicant.welfare_amount

		status1='TREATED'
		status2='UNTREATED'
		loan_lock='YES'
		account_status='ACTIVE'
		status='ACTIVE'
		savings_status='PENDING'
		loan_status='PENDING'
		shares_status='PENDING'
		welfare_status='PENDING'
		date_joined_status='PENDING'
		date_joined_status1='UPLOADED'
		dob_status='PENDING'
		dob_status1='UPLOADED'
		date_of_first_appointment_status='PENDING'
		date_of_first_appointment_status1='UPLOADED'

		form_print = request.POST.get('form_print')

		title_id = request.POST.get("title")
		title = Titles.objects.get(id=title_id)

		last_name=request.POST.get('last_name')
		first_name=request.POST.get('first_name')
		middle_name=request.POST.get('middle_name')

		dob=request.POST.get('dob')

		gender_id = request.POST.get("gender")
		gender = Gender.objects.get(id=gender_id)

		phone_number=request.POST.get('phone_number')
		residential_address=request.POST.get('residential_address')
		permanent_home_address=request.POST.get('permanent_home_address')

		department_id = request.POST.get("department")
		department = Departments.objects.get(id=department_id)

		dob_add=request.POST.get('dob_add')
		date_of_first_appointment_add=request.POST.get('date_of_first_appointment_add')


		salary_institution_id = request.POST.get("salary_institution")
		salary_institution = SalaryInstitution.objects.get(id=salary_institution_id)

		file_no=request.POST.get('file_no')
		ippis_no=request.POST.get('ippis_no')

		email=request.POST.get('email')
		username=request.POST.get('username')
		date_of_first_appointment=request.POST.get('date_of_first_appointment')
		date_joined=request.POST.get('date_joined')

		if request.FILES.get('profile_pic', False):
			profile_pic = request.FILES['profile_pic']
			fs=FileSystemStorage()
			filename=fs.save(profile_pic.name,profile_pic)
			profile_pic_url=fs.url(filename)
		else:
			profile_pic_url=None


		if not last_name:
			messages.error(request,"Missing Last Name")
			return HttpResponseRedirect(reverse('membership_registration_register',args=(pk,)))

		if not first_name:
			messages.error(request,"First Name Missing")
			return HttpResponseRedirect(reverse('membership_registration_register',args=(pk,)))

		if dob_add and not dob:
			messages.error(request,"Missing Date of Birth")
			return HttpResponseRedirect(reverse('membership_registration_register',args=(pk,)))

		if not phone_number:
			messages.error(request,"Missing Phone No")
			return HttpResponseRedirect(reverse('membership_registration_register',args=(pk,)))

		if not file_no:
			messages.error(request,"Missing File No")
			return HttpResponseRedirect(reverse('membership_registration_register',args=(pk,)))

		if not ippis_no:
			messages.error(request,"Missing IPPIS No or Salary Code")
			return HttpResponseRedirect(reverse('membership_registration_register',args=(pk,)))


		if not email:
			messages.error(request,"Missing Email Address")
			return HttpResponseRedirect(reverse('membership_registration_register',args=(pk,)))

		if not username:
			messages.error(request,"Missing Username")
			return HttpResponseRedirect(reverse('membership_registration_register',args=(pk,)))


		if date_of_first_appointment_add and not date_of_first_appointment:
			messages.error(request,"Missing Date of First Appointment")
			return HttpResponseRedirect(reverse('membership_registration_register',args=(pk,)))

		if CustomUser.objects.filter(Q(username=username)).exists():
			messages.error(request,"Username Already in Use")
			return HttpResponseRedirect(reverse('membership_registration_register',args=(pk,)))

		if CustomUser.objects.filter(Q(email=email)).exists():
			messages.error(request,"Email Already in Use")
			return HttpResponseRedirect(reverse('membership_registration_register',args=(pk,)))

		if Members.objects.filter(phone_number=phone_number).exists():
			if Members.objects.filter(phone_number=phone_number,status='ACTIVE').exists():
				messages.error(request,"Phone Number Already in Use")
				return HttpResponseRedirect(reverse('membership_registration_register',args=(pk,)))

		if Members.objects.filter(file_no=file_no).exists():
			if Members.objects.filter(file_no=file_no,status='ACTIVE').exists():
				messages.error(request,"File Number Already in Use")
				return HttpResponseRedirect(reverse('membership_registration_register',args=(pk,)))


		if Members.objects.filter(ippis_no=ippis_no).exists():
			if Members.objects.filter(ippis_no=ippis_no,status='ACTIVE').exists():
				messages.error(request,'Salary Code Already in Use')
				return HttpResponseRedirect(reverse('membership_registration_register',args=(pk,)))

		member_id_obj=[]
		if MembersIdManager.objects.all().exists():
			member_id_obj = MembersIdManager.objects.first()
		else:
			messages.error(request,"Membership ID Missing")
			return HttpResponseRedirect(reverse('membership_registration_register',args=(pk,)))

		default_password=[]
		if DefaultPassword.objects.all().exists():
			default_password = DefaultPassword.objects.first()
			password=default_password.title
		else:
			messages.error(request,"Default Password Missing")
			return HttpResponseRedirect(reverse('membership_registration_register',args=(pk,)))

		user_type_obj = UserType.objects.get(title='MEMBERS')
		user_type=user_type_obj.code


		share_transaction=[]
		if TransactionTypes.objects.filter(code=700).exists():
			share_transaction=TransactionTypes.objects.get(code=700)
			share_account=str(share_transaction.code) + str(member_id_obj.member_id).zfill(5)
		else:
			messages.error(request,"Transaction Type(Shares) with Code 700 Missing")
			return HttpResponseRedirect(reverse('membership_registration_register',args=(pk,)))

		welfare_transaction=[]
		if TransactionTypes.objects.filter(code=800).exists():
			welfare_transaction=TransactionTypes.objects.get(code=800)
			welfare_account=str(welfare_transaction.code) + str(member_id_obj.member_id).zfill(5)
		else:
			messages.error(request,"Transaction Type(Welfare) with Code 800 Missing")
			return HttpResponseRedirect(reverse('membership_registration_register',args=(pk,)))

		member_id = member_id_obj.prefix_title + "/" +  str(member_id_obj.prefix_year) + "/" + str(member_id_obj.member_id).zfill(5)

		if Members.objects.filter(member_id=member_id).exists():
			messages.error(request,"Sorry The Member ID Found is already in use")
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
		user.members.salary_institution=salary_institution
		user.members.file_no=file_no
		user.members.ippis_no=ippis_no

		if dob_add:
			user.members.dob=dob
			user.members.dob_status=dob_status1

		if date_of_first_appointment_add:
			user.members.date_of_first_appointment=date_of_first_appointment
			user.members.date_of_first_appointment_status=date_of_first_appointment_status1

		user.members.date_joined=date_joined
		user.members.date_joined_status=date_joined_status1
		user.members.status=account_status
		user.members.savings_status=savings_status
		user.members.loan_status=loan_status
		user.members.shares_status=shares_status
		user.members.welfare_status=welfare_status
		user.members.date_joined_status=date_joined_status
		user.members.member_category='NEW'


		if profile_pic_url!=None:
			user.members.profile_pic=profile_pic_url

		user.members.save()

		member_id_obj.member_id=int(member_id_obj.member_id) + 1
		member_id_obj.save()

		share_account=MembersAccountsDomain(loan_lock=loan_lock,status=account_status,member=user.members,transaction=share_transaction,account_number=share_account)
		share_account.save()

		share_record=MembersShareAccounts(tdate=tdate,status=status2,member=share_account,shares=shares,unit_cost=unit_cost,total_cost=total_cost,effective_date=tdate,year=now.year,processed_by=processed_by.username)
		share_record.save()

		particulars=share_transaction.name + " INITIAL PURCHASE OF " + str(shares) + ' BY ' + str(unit_cost) + " PER A UNIT"
		debit=0
		credit=float(total_cost)
		balance=credit

		ledger_status='ACTIVE'
		post_to_ledger(
					user.members,
					share_transaction,
					share_account.account_number,
					particulars,
					debit,
					credit,
					abs(balance),
					get_current_date(now),
					ledger_status,
					tdate,
					)


		welfare_account=MembersAccountsDomain(loan_lock=loan_lock,status=account_status,member=user.members,transaction=welfare_transaction,account_number=welfare_account)
		welfare_account.save()

		welfare_record=MembersWelfareAccounts(tdate=tdate,processed_by=processed_by.username,status=status2,member=welfare_account,amount=welfare_amount,year=now.year)
		welfare_record.save()

		applicant.status=status1
		applicant.save()

		return HttpResponseRedirect(reverse('membership_registration_register_confirmation', args=(ippis_no,)))





	form.fields['first_name'].initial=applicant.applicant.first_name
	form.fields['last_name'].initial=applicant.applicant.last_name
	form.fields['middle_name'].initial=applicant.applicant.middle_name
	form.fields['title'].initial=applicant.applicant.title_id
	form.fields['gender'].initial=applicant.applicant.gender.id
	form.fields['phone_number'].initial=applicant.applicant.phone_number
	form.fields['department'].initial=applicant.applicant.department.id
	form.fields['date_joined'].initial=now

	context={
	'task_array':task_array,
	'task_enabler_array':task_enabler_array,
	'default_password':default_password,
	'form':form,
	}
	return render(request,'deskofficer_templates/membership_registration_register.html',context)



#########################################################
############### MEMBERS ACCOUNT CRERATIONS###############
#########################################################
def Members_Account_Creation_Search(request):
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	task_array=[]
	for task in tasks:
		task_array.append(task.task.title)



	task_enabler=TransactionEnabler.objects.filter(status="YES")
	task_enabler_array=[]
	for item in task_enabler:
		task_enabler_array.append(item.title)

	default_password="NO"
	if Staff.objects.filter(admin=request.user,default_password='YES'):
		default_password="YES"


	title="Search Membership for Account Creation"
	form = searchForm(request.POST or None)

	return render(request,'deskofficer_templates/Members_Account_Creation_Search.html',{'form':form,'title':title,'task_array':task_array,
	'task_enabler_array':task_enabler_array,
	'default_password':default_password,})


def Members_Account_Creation_list_load(request):
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	task_array=[]
	for task in tasks:
		task_array.append(task.task.title)



	task_enabler=TransactionEnabler.objects.filter(status="YES")
	task_enabler_array=[]
	for item in task_enabler:
		task_enabler_array.append(item.title)

	default_password="NO"
	if Staff.objects.filter(admin=request.user,default_password='YES'):
		default_password="YES"

	title="Loan Request order"

	form = searchForm(request.POST)
	if request.method == "POST":
		if not form['title'].value():
			return HttpResponseRedirect(reverse('Members_Account_Creation_Search'))
		members=searchMembers(form['title'].value(),'ACTIVE')

		if not members:
			return HttpResponseRedirect(reverse('Members_Account_Creation_Search'))

	context={
	'members':members,
	'title':title,
	'task_array':task_array,
	'task_enabler_array':task_enabler_array,
	'default_password':default_password,
	}
	return render(request,'deskofficer_templates/Members_Account_Creation_list_load.html',context)

def Members_Account_Creation_preview(request,pk):
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	task_array=[]
	for task in tasks:
		task_array.append(task.task.title)



	task_enabler=TransactionEnabler.objects.filter(status="YES")
	task_enabler_array=[]
	for item in task_enabler:
		task_enabler_array.append(item.title)

	default_password="NO"
	if Staff.objects.filter(admin=request.user,default_password='YES'):
		default_password="YES"


	member=Members.objects.get(id=pk)
	transactions=TransactionTypes.objects.filter(~Q(source__title="LOAN") & ~Q(source__title='GENERAL')  & ~Q(code='701'))
	records=MembersAccountsDomain.objects.filter(member=member)

	context={
	'member':member,
	'transactions':transactions,
	'task_array':task_array,
	'task_enabler_array':task_enabler_array,
	'default_password':default_password,
	'records':records,
	}
	return render(request,'deskofficer_templates/Members_Account_Creation_process.html',context)

def Members_Account_Creation_process_Delete(request,pk):
	member=MembersAccountsDomain.objects.get(id=pk)
	MembersAccountsDomain.objects.filter(id=pk).delete()
	return HttpResponseRedirect(reverse('Members_Account_Creation_preview',args=(member.member.pk,)))


def Members_Account_Creation_preview_remove_duplicate(request):
	records=MembersAccountsDomain.objects.filter().order_by('account_number').values_list('account_number').distinct()

	for record in records:
		for tag in MembersAccountsDomain.objects.filter(account_number=record[0])[1:]:
			tag.delete()
	return HttpResponseRedirect(reverse('Members_Account_Creation_preview_all'))


def Members_Account_Creation_preview_all(request):
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	task_array=[]
	for task in tasks:
		task_array.append(task.task.title)



	task_enabler=TransactionEnabler.objects.filter(status="YES")
	task_enabler_array=[]
	for item in task_enabler:
		task_enabler_array.append(item.title)

	default_password="NO"
	if Staff.objects.filter(admin=request.user,default_password='YES'):
		default_password="YES"

		
	

	transactions=TransactionTypes.objects.filter(~Q(source__title="LOAN") & ~Q(source__title='GENERAL')  & ~Q(code='701'))
	records=MembersAccountsDomain.objects.all().order_by('member_id')

	context={
	# 'member':member,
	'transactions':transactions,
	'task_array':task_array,
	'task_enabler_array':task_enabler_array,
	'default_password':default_password,
	'records':records,
	}
	return render(request,'deskofficer_templates/Members_Account_Creation_process_all.html',context)

def Members_Account_Creation_process(request,pk):

	loan_lock="YES"
	member=Members.objects.get(id=pk)
	transactions=TransactionTypes.objects.filter(~Q(source__title="LOAN") & ~Q(source__title='GENERAL'))
	member_id=list((member.member_id).split("/"))

	count=0
	count1=0
	my_id=member_id[2]
	for transaction in transactions:
		account_number=str(transaction.code) + str(my_id)
		if MembersAccountsDomain.objects.filter(member=member,transaction=transaction,account_number=account_number).exists():
			MembersAccountsDomain.objects.filter(member=member,transaction=transaction,account_number=account_number).update(loan_lock='NO')
			count1=count1+1
		else:
			count +=1
			record=MembersAccountsDomain(loan_lock='NO',status='ACTIVE',member=member,transaction=transaction,account_number=account_number)
			record.save()
	messages.success(request,str(count) + ' Account(s) Successfully Created' + ' and '+ str(count1) + " Updated" )
	return HttpResponseRedirect(reverse('Members_Account_Creation_preview',args=(member.pk,)))



def Members_Multiple_Account_Creation_preview(request):
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	task_array=[]
	for task in tasks:
		task_array.append(task.task.title)

	task_enabler=TransactionEnabler.objects.filter(status="YES")
	task_enabler_array=[]
	for item in task_enabler:
		task_enabler_array.append(item.title)

	default_password="NO"
	if Staff.objects.filter(admin=request.user,default_password='YES'):
		default_password="YES"

	status="ACTIVE"
	members=Members.objects.filter(status=status)
	transactions=TransactionTypes.objects.filter(~Q(source__title="LOAN") & ~Q(source__title='GENERAL')  & ~Q(code='701'))

	context={
	'members':members,
	'transactions':transactions,
	'task_array':task_array,
	'task_enabler_array':task_enabler_array,
	'default_password':default_password,
	}
	return render(request,'deskofficer_templates/Members_Multiple_Account_Creation_preview.html',context)


def Members_Multiple_Account_Creation_process(request):

	members=Members.objects.filter(status='ACTIVE')
	transactions=TransactionTypes.objects.filter(~Q(source__title="LOAN") & ~Q(source__title='GENERAL'))


	count=0
	for member in members:
		member_id=list((member.member_id).split("/"))
		my_id=member_id[2]

		for transaction in transactions:
			account_number=str(transaction.code) + str(my_id)
			if MembersAccountsDomain.objects.filter(account_number=account_number).exists():
			# 	account_number=str(account_number) + "_A"

			# if MembersAccountsDomain.objects.filter(member=member,transaction=transaction,account_number=account_number).exists():
				pass
			else:
				count +=1
				MembersAccountsDomain(loan_lock='YES',status='ACTIVE',member=member,transaction=transaction,account_number=account_number).save()
	messages.success(request,str(count) + ' Account(s) Successfully Created')
	return HttpResponseRedirect(reverse('Members_Multiple_Account_Creation_preview'))


def Members_account_details_list(request,pk):
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	task_array=[]
	for task in tasks:
		task_array.append(task.task.title)



	task_enabler=TransactionEnabler.objects.filter(status="YES")
	task_enabler_array=[]
	for item in task_enabler:
		task_enabler_array.append(item.title)

	default_password="NO"
	if Staff.objects.filter(admin=request.user,default_password='YES'):
		default_password="YES"

	transaction=TransactionTypes.objects.get(id=pk)
	records=MembersAccountsDomain.objects.filter(transaction=transaction)

	context={
	'task_array':task_array,
	'task_enabler_array':task_enabler_array,
	'default_password':default_password,
	'records':records,
	'transaction':transaction,
	}
	return render(request,'deskofficer_templates/Members_account_details_list.html',context)



#########################################################
############### STANDING ORDER #########################
#########################################################
def standing_order_reactivate_account_search(request):
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	task_array=[]
	for task in tasks:
		task_array.append(task.task.title)



	task_enabler=TransactionEnabler.objects.filter(status="YES")
	task_enabler_array=[]
	for item in task_enabler:
		task_enabler_array.append(item.title)

	default_password="NO"
	if Staff.objects.filter(admin=request.user,default_password='YES'):
		default_password="YES"

	title="Search Membership for Standing Order"
	form = searchForm(request.POST or None)

	return render(request,'deskofficer_templates/standing_order_reactivate_account_search.html',{'form':form,'title':title,'task_array':task_array,
	'task_enabler_array':task_enabler_array,
	'default_password':default_password,})


def standing_order_reactivate_account_list_load(request):
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	task_array=[]
	for task in tasks:
		task_array.append(task.task.title)



	task_enabler=TransactionEnabler.objects.filter(status="YES")
	task_enabler_array=[]
	for item in task_enabler:
		task_enabler_array.append(item.title)

	default_password="NO"
	if Staff.objects.filter(admin=request.user,default_password='YES'):
		default_password="YES"

	title="Loan Request order"
	form = searchForm(request.POST)

	if request.method == "POST":
		if request.POST.get("title")=="":
			return HttpResponseRedirect(reverse('standing_order_reactivate_account_search'))
		members=StandingOrderDeactivatedAccounts.objects.filter(Q(transaction__transaction__member__phone_number__icontains=form['title'].value()) | Q(transaction__transaction__member__file_no__icontains=form['title'].value()) | Q(transaction__transaction__member__ippis_no__icontains=form['title'].value())  | Q(transaction__transaction__member__admin__first_name__icontains=form['title'].value()) | Q(transaction__transaction__member__admin__last_name__icontains=form['title'].value()) | Q(transaction__transaction__member__middle_name__icontains=form['title'].value())).filter(transaction__transaction__member__status='ACTIVE',status='UNTREATED')

	context={
	'members':members,
	'title':title,
	'task_array':task_array,
	'task_enabler_array':task_enabler_array,
	'default_password':default_password,
	}
	return render(request,'deskofficer_templates/standing_order_reactivate_account_list_load.html',context)




def standing_order_reactivate_account(request,pk):
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	task_array=[]
	for task in tasks:
		task_array.append(task.task.title)



	task_enabler=TransactionEnabler.objects.filter(status="YES")
	task_enabler_array=[]
	for item in task_enabler:
		task_enabler_array.append(item.title)

	default_password="NO"
	if Staff.objects.filter(admin=request.user,default_password='YES'):
		default_password="YES"

	form=standing_order_reactivate_account_form(request.POST or None)

	record=StandingOrderDeactivatedAccounts.objects.get(id=pk)

	if request.method == 'POST':
		transaction=record.transaction.transaction.account_number
		amount=request.POST.get('amount')
		StandingOrderAccounts.objects.filter(transaction__account_number=transaction).update(amount=amount,status="ACTIVE")

		record.status='TREATED'
		record.save()
		return HttpResponseRedirect(reverse('standing_order_reactivate_account_search'))

	form.fields['existing_amount'].initial=record.transaction.amount
	form.fields['amount'].initial=record.transaction.amount
	context={
	'form':form,
	'record':record,
	'task_array':task_array,
	'task_enabler_array':task_enabler_array,
	'default_password':default_password,
	}
	return render(request,'deskofficer_templates/standing_order_reactivate_account.html',context)


def standing_order_drop_account(request,pk):

	record=StandingOrderDeactivatedAccounts.objects.get(id=pk)
	record.status='TREATED'
	record.save()
	return HttpResponseRedirect(reverse('standing_order_reactivate_account_search'))


def standing_order_selected_search(request):
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	task_array=[]
	for task in tasks:
		task_array.append(task.task.title)



	task_enabler=TransactionEnabler.objects.filter(status="YES")
	task_enabler_array=[]
	for item in task_enabler:
		task_enabler_array.append(item.title)

	default_password="NO"
	if Staff.objects.filter(admin=request.user,default_password='YES'):
		default_password="YES"

	title="Search Membership for Standing Order"
	form = searchForm(request.POST or None)

	return render(request,'deskofficer_templates/standing_order_selected_search.html',{'form':form,'title':title,'task_array':task_array,
	'task_enabler_array':task_enabler_array,
	'default_password':default_password,})


def standing_order_selected_list_load(request):
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	task_array=[]
	for task in tasks:
		task_array.append(task.task.title)



	task_enabler=TransactionEnabler.objects.filter(status="YES")
	task_enabler_array=[]
	for item in task_enabler:
		task_enabler_array.append(item.title)

	default_password="NO"
	if Staff.objects.filter(admin=request.user,default_password='YES'):
		default_password="YES"

	title="Loan Request order"
	form = searchForm(request.POST)

	if request.method == "POST":
		if request.POST.get("title")=="":
			return HttpResponseRedirect(reverse('standing_order_selected_search'))

		members=searchMembers(form['title'].value(),'ACTIVE')

	context={
	'members':members,
	'title':title,
	'task_array':task_array,
	'task_enabler_array':task_enabler_array,
	'default_password':default_password,
	}
	return render(request,'deskofficer_templates/standing_order_selected_list_load.html',context)


def standing_order_selected_form(request,pk):
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	task_array=[]
	for task in tasks:
		task_array.append(task.task.title)



	task_enabler=TransactionEnabler.objects.filter(status="YES")
	task_enabler_array=[]
	for item in task_enabler:
		task_enabler_array.append(item.title)

	default_password="NO"
	if Staff.objects.filter(admin=request.user,default_password='YES'):
		default_password="YES"


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
			StandingOrderAccounts(member=applicant,
										transaction=saving,
										amount=amount,
										lock_status='YES',
										account_number=account_number).save()

			return HttpResponseRedirect(reverse('standing_order_selected_form', args=(pk,)))


	context={

	'applicant':applicant,
	'form':form,
	'standing_orders':standing_orders,
	'task_array':task_array,
	'task_enabler_array':task_enabler_array,
	'default_password':default_password,
	}
	return render(request,'deskofficer_templates/standing_order_selected_form.html',context)


def standing_order_list_load(request):
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	task_array=[]
	for task in tasks:
		task_array.append(task.task.title)



	task_enabler=TransactionEnabler.objects.filter(status="YES")
	task_enabler_array=[]
	for item in task_enabler:
		task_enabler_array.append(item.title)


	default_password="NO"
	if Staff.objects.filter(admin=request.user,default_password='YES'):
		default_password="YES"

	applicants=Members.objects.filter(status='ACTIVE')


	context={
	'applicants':applicants,
	'task_array':task_array,
	'task_enabler_array':task_enabler_array,
	'default_password':default_password,
	}
	return render(request,'deskofficer_templates/standing_order_list_load.html',context)


def standing_order_form(request,pk):
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	task_array=[]
	for task in tasks:
		task_array.append(task.task.title)



	task_enabler=TransactionEnabler.objects.filter(status="YES")
	task_enabler_array=[]
	for item in task_enabler:
		task_enabler_array.append(item.title)

	default_password="NO"
	if Staff.objects.filter(admin=request.user,default_password='YES'):
		default_password="YES"

	applicant=Members.objects.get(id=pk)
	form=standing_orderform(request.POST or None)
	standing_orders=StandingOrderAccounts.objects.filter(transaction__member=applicant)
	account_number=[]



	if request.method=="POST" and 'btn_submit' in request.POST:

		form=standing_orderform(request.POST)

		saving_id=request.POST.get("savings")
		saving = TransactionTypes.objects.get(id=saving_id)

		if MembersAccountsDomain.objects.filter(member=applicant,transaction=saving).exists():
			account_number=MembersAccountsDomain.objects.get(member=applicant,transaction=saving)
		if account_number:
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


			member=StandingOrderAccounts(lock_status='OPEN',status='ACTIVE',transaction=account_number,amount=amount)
			member.save()
			return HttpResponseRedirect(reverse('standing_order_form', args=(pk,)))

		else:
			messages.error(request,"Account Number not Found")
			return HttpResponseRedirect(reverse('standing_order_form', args=(pk,)))


	context={

	'applicant':applicant,
	'form':form,
	'standing_orders':standing_orders,
	'task_array':task_array,
	'task_enabler_array':task_enabler_array,
	'default_password':default_password,
	'account_number':account_number,
	}
	return render(request,'deskofficer_templates/standing_order_form.html',context)


def standing_order_locked(request,pk):
	status="LOCKED"
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

def Standing_Order_Suspension_search(request):
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	task_array=[]
	for task in tasks:
		task_array.append(task.task.title)



	task_enabler=TransactionEnabler.objects.filter(status="YES")
	task_enabler_array=[]
	for item in task_enabler:
		task_enabler_array.append(item.title)

	default_password="NO"
	if Staff.objects.filter(admin=request.user,default_password='YES'):
		default_password="YES"


	title="Search Membership for Standing Order Suspension"
	form = searchForm(request.POST or None)

	return render(request,'deskofficer_templates/Standing_Order_Suspension_search.html',{'form':form,'title':title,'task_array':task_array,
	'task_enabler_array':task_enabler_array,
	'default_password':default_password,})


def Standing_Order_Suspension_List_load(request):
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	task_array=[]
	for task in tasks:
		task_array.append(task.task.title)



	task_enabler=TransactionEnabler.objects.filter(status="YES")
	task_enabler_array=[]
	for item in task_enabler:
		task_enabler_array.append(item.title)

	default_password="NO"
	if Staff.objects.filter(admin=request.user,default_password='YES'):
		default_password="YES"


	title="Loan Request order"
	form = searchForm(request.POST)
	status="ACTIVE"
	if request.method == "POST":
		if request.POST.get("title")=="":
			return HttpResponseRedirect(reverse('Standing_Order_Suspension_search'))

		members=searchMembers(form['title'].value(),status)
	context={
	'members':members,
	'title':title,
	'task_array':task_array,
	'task_enabler_array':task_enabler_array,
	'default_password':default_password,
	}
	return render(request,'deskofficer_templates/Standing_Order_Suspension_List_load.html',context)




def Standing_Order_Suspension_Transaction_Load(request,pk):
	form=Standing_Order_Suspension_Form(request.POST or None)
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	task_array=[]
	for task in tasks:
		task_array.append(task.task.title)



	task_enabler=TransactionEnabler.objects.filter(status="YES")
	task_enabler_array=[]
	for item in task_enabler:
		task_enabler_array.append(item.title)

	default_password="NO"
	if Staff.objects.filter(admin=request.user,default_password='YES'):
		default_password="YES"


	member=Members.objects.get(id=pk)

	approval_status='PENDING'
	status='UNTREATED'

	records = StandingOrderAccountsSuspensionRequest.objects.filter(status=status,transaction__transaction__member=member,approval_status=approval_status)

	if request.method == 'POST':
		processed_by=CustomUser.objects.get(id=request.user.id)
		tdate=get_current_date(now)

		purpose = request.POST.get("reasons")
		transaction_id=request.POST.get('saving')
		transaction=TransactionTypes.objects.get(id=transaction_id)

		if not purpose:
			messages.error(request,'Please purpose cannot be empty')
			return HttpResponseRedirect(reverse('Standing_Order_Suspension_Transaction_Load',args=(pk,)))

		if CompulsorySavings.objects.filter(transaction=transaction).exists():
			messages.error("This is a compulsory savings, it cannot be suspended")
			return HttpResponseRedirect(reverse('Standing_Order_Suspension_Transaction_Load',args=(pk,)))

		if StandingOrderAccounts.objects.filter(transaction__member=member,transaction__transaction=transaction).exists():
			record = StandingOrderAccounts.objects.get(transaction__member=member,transaction__transaction=transaction)
			StandingOrderAccountsSuspensionRequest(processed_by=processed_by.username,status=status,transaction=record,purpose=purpose,approval_status=approval_status,tdate=tdate).save()
			messages.success(request,'Record Added Successfully')
			return HttpResponseRedirect(reverse('Standing_Order_Suspension_Transaction_Load',args=(pk,)))

		else:

			messages.error(request,"No Standing Order Record Found, its either Locked or Doesn't Exist")
			return HttpResponseRedirect(reverse('Standing_Order_Suspension_Transaction_Load',args=(pk,)))

	context={
	'records':records,
	'member':member,
	'form':form,
	'task_array':task_array,
	'task_enabler_array':task_enabler_array,
	'default_password':default_password,
	}
	return render(request,'deskofficer_templates/Standing_Order_Suspension_Transaction_Load.html',context)


def Standing_Order_Suspension_Transaction_Delete(request,pk):
	record = StandingOrderAccountsSuspensionRequest.objects.get(id=pk)
	return_pk = record.transaction.transaction.member_id
	record.delete()
	messages.success(request,'Record Deleted Successfully')
	return HttpResponseRedirect(reverse('Standing_Order_Suspension_Transaction_Load',args=(return_pk,)))

def Standing_Order_Suspension_Transaction_Approval_Load(request):
	processed_by=CustomUser.objects.get(id=request.user.id)
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	task_array=[]
	for task in tasks:
		task_array.append(task.task.title)



	task_enabler=TransactionEnabler.objects.filter(status="YES")
	task_enabler_array=[]
	for item in task_enabler:
		task_enabler_array.append(item.title)

	default_password="NO"
	if Staff.objects.filter(admin=request.user,default_password='YES'):
		default_password="YES"

	records = StandingOrderAccountsSuspensionRequest.objects.filter(status='UNTREATED',approval_status="PENDING").exclude(processed_by=processed_by.username)

	context={
	'records':records,
	'task_array':task_array,
	'task_enabler_array':task_enabler_array,
	'default_password':default_password,
	}
	return render(request,'deskofficer_templates/Standing_Order_Suspension_Transaction_Approval_Load.html',context)


def Standing_Order_Suspension_Transaction_Approvals_Load_Details(request,pk):
	form = Standing_Order_Suspension_Transaction_Approvals_Load_Details_form(request.POST or None)
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	task_array=[]
	for task in tasks:
		task_array.append(task.task.title)



	task_enabler=TransactionEnabler.objects.filter(status="YES")
	task_enabler_array=[]
	for item in task_enabler:
		task_enabler_array.append(item.title)

	default_password="NO"
	if Staff.objects.filter(admin=request.user,default_password='YES'):
		default_password="YES"


	record = StandingOrderAccountsSuspensionRequest.objects.get(id=pk)

	if request.method == 'POST':
		tdate=get_current_date(now)
		approval_officer=CustomUser.objects.get(id=request.user.id).username
		comment=request.POST.get("comment")

		approval_status=request.POST.get("approval_status")

		record.approval_status=approval_status
		record.approval_officer=approval_officer
		record.approval_comment=comment
		record.approval_date=tdate
		record.save()

		return HttpResponseRedirect(reverse('Standing_Order_Suspension_Transaction_Approval_Load'))

	form.fields['purpose'].initial=record.purpose
	context={
	'form':form,
	'record':record,
	'task_array':task_array,
	'task_enabler_array':task_enabler_array,
	'default_password':default_password,
	}
	return render(request,'deskofficer_templates/Standing_Order_Suspension_Transaction_Approvals_Load_Details.html',context)


def Standing_Order_Suspension_Transaction_Approval_Processing_Load(request):
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	task_array=[]
	for task in tasks:
		task_array.append(task.task.title)



	task_enabler=TransactionEnabler.objects.filter(status="YES")
	task_enabler_array=[]
	for item in task_enabler:
		task_enabler_array.append(item.title)


	default_password="NO"
	if Staff.objects.filter(admin=request.user,default_password='YES'):
		default_password="YES"

	records = StandingOrderAccountsSuspensionRequest.objects.filter(status='UNTREATED',approval_status='APPROVED')

	context={
	'records':records,
	'task_array':task_array,
	'task_enabler_array':task_enabler_array,
	'default_password':default_password,
	}
	return render(request,'deskofficer_templates/Standing_Order_Suspension_Transaction_Approval_Processing_Load.html',context)


def Standing_Order_Suspension_Transaction_Approval_Processing(request,pk):
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	task_array=[]
	for task in tasks:
		task_array.append(task.task.title)



	task_enabler=TransactionEnabler.objects.filter(status="YES")
	task_enabler_array=[]
	for item in task_enabler:
		task_enabler_array.append(item.title)

	default_password="NO"
	if Staff.objects.filter(admin=request.user,default_password='YES'):
		default_password="YES"


	record = StandingOrderAccountsSuspensionRequest.objects.get(id=pk)

	record.transaction.status='INACTIVE'
	record.transaction.save()

	record.status='TREATED'
	record.save()

	return HttpResponseRedirect(reverse('Standing_Order_Suspension_Transaction_Approval_Processing_Load'))


def Standing_Order_Suspension_Transaction_Releasing_search(request):
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	task_array=[]
	for task in tasks:
		task_array.append(task.task.title)



	task_enabler=TransactionEnabler.objects.filter(status="YES")
	task_enabler_array=[]
	for item in task_enabler:
		task_enabler_array.append(item.title)

	default_password="NO"
	if Staff.objects.filter(admin=request.user,default_password='YES'):
		default_password="YES"

	title="Search Membership for Standing Order Release"
	form = searchForm(request.POST or None)

	return render(request,'deskofficer_templates/Standing_Order_Suspension_Transaction_Releasing_search.html',{'form':form,'title':title,'task_array':task_array,
	'task_enabler_array':task_enabler_array,
	'default_password':default_password,})


def Standing_Order_Suspension_Transaction_Releasing_list_load(request):
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	task_array=[]
	for task in tasks:
		task_array.append(task.task.title)



	task_enabler=TransactionEnabler.objects.filter(status="YES")
	task_enabler_array=[]
	for item in task_enabler:
		task_enabler_array.append(item.title)

	default_password="NO"
	if Staff.objects.filter(admin=request.user,default_password='YES'):
		default_password="YES"

	title="Loan Request order"
	form = searchForm(request.POST)

	members=[]
	if request.method == "POST":
		if request.POST.get("title")=="":
			return HttpResponseRedirect(reverse('Standing_Order_Suspension_Transaction_Releasing_search'))
		members=StandingOrderAccounts.objects.filter(Q(transaction__member__phone_number__icontains=form['title'].value()) | Q(transaction__member__file_no__icontains=form['title'].value()) | Q(transaction__member__ippis_no__icontains=form['title'].value())  | Q(transaction__member__admin__first_name__icontains=form['title'].value()) | Q(transaction__member__admin__last_name__icontains=form['title'].value()) | Q(transaction__member__middle_name__icontains=form['title'].value())).filter(transaction__member__status='ACTIVE',status='INACTIVE')

	context={
	'members':members,
	'title':title,
	'task_array':task_array,
	'task_enabler_array':task_enabler_array,
	'default_password':default_password,
	}
	return render(request,'deskofficer_templates/Standing_Order_Suspension_Transaction_Releasing_list_load.html',context)




def Standing_Order_Suspension_Transactions_Releasing_Details(request,pk):
	form=Standing_Order_Suspension_Transaction_Releasing_Details_form(request.POST or None)
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	task_array=[]
	for task in tasks:
		task_array.append(task.task.title)



	task_enabler=TransactionEnabler.objects.filter(status="YES")
	task_enabler_array=[]
	for item in task_enabler:
		task_enabler_array.append(item.title)

	default_password="NO"
	if Staff.objects.filter(admin=request.user,default_password='YES'):
		default_password="YES"


	record = StandingOrderAccounts.objects.get(id=pk)
	approval_status='PENDING'
	status='UNTREATED'


	item=[]
	if StandingOrderAccountsSuspensionReleaseRequest.objects.filter(transaction=record,approval_status=approval_status,status=status).exists():
		item = StandingOrderAccountsSuspensionReleaseRequest.objects.get(transaction=record,approval_status=approval_status,status=status)

	if request.method == 'POST':
		tdate=get_current_date(now)
		processed_by=CustomUser.objects.get(id=request.user.id)
		comment=request.POST.get('comment')

		if not comment:
			messages.error(request,'Comment cannot be empty')
			return HttpResponseRedirect(reverse('Standing_Order_Suspension_Transactions_Releasing_Details',args=(pk,)))

		if StandingOrderAccountsSuspensionReleaseRequest.objects.filter(transaction=record,approval_status=approval_status,status=status).exists():
			item.purpose=comment
			item.status=status
			item.save()
			return HttpResponseRedirect(reverse('Standing_Order_Suspension_Transaction_Releasing_search'))

		StandingOrderAccountsSuspensionReleaseRequest(purpose=comment,transaction=record,approval_status=approval_status,processed_by=processed_by.username,tdate=tdate,status=status).save()

		return HttpResponseRedirect(reverse('Standing_Order_Suspension_Transaction_Releasing_search'))


	if item:
		form.fields['comment'].initial = item.purpose
	context={
	'item':item,
	'form':form,
	'record':record,
	'task_array':task_array,
	'task_enabler_array':task_enabler_array,
	'default_password':default_password,
	}
	return render(request,'deskofficer_templates/Standing_Order_Suspension_Transactions_Releasing_Details.html',context)


def Standing_Order_Suspension_Transaction_Releasing_Approval_Load(request):
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	task_array=[]
	for task in tasks:
		task_array.append(task.task.title)



	task_enabler=TransactionEnabler.objects.filter(status="YES")
	task_enabler_array=[]
	for item in task_enabler:
		task_enabler_array.append(item.title)

	default_password="NO"
	if Staff.objects.filter(admin=request.user,default_password='YES'):
		default_password="YES"

	processed_by=CustomUser.objects.get(id=request.user.id)

	records = StandingOrderAccountsSuspensionReleaseRequest.objects.filter(status='UNTREATED',approval_status='PENDING').exclude(processed_by=processed_by.username)

	context={
	'records':records,
	'task_array':task_array,
	'task_enabler_array':task_enabler_array,
	'default_password':default_password,
	}
	return render(request,'deskofficer_templates/Standing_Order_Suspension_Transaction_Releasing_Approval_Load.html',context)


def Standing_Order_Suspension_Transaction_Releasing_Approval_Details(request,pk):
	form=Loan_unscheduling_approval_preview_form(request.POST or None)
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	task_array=[]
	for task in tasks:
		task_array.append(task.task.title)



	task_enabler=TransactionEnabler.objects.filter(status="YES")
	task_enabler_array=[]
	for item in task_enabler:
		task_enabler_array.append(item.title)

	default_password="NO"
	if Staff.objects.filter(admin=request.user,default_password='YES'):
		default_password="YES"

	record = StandingOrderAccountsSuspensionReleaseRequest.objects.get(id=pk)


	if request.method == 'POST':
		approval_officer=CustomUser.objects.get(id=request.user.id).username
		approval_status=request.POST.get('approval_status')

		approval_date=get_current_date(now)


		processed_by=CustomUser.objects.get(id=request.user.id)
		comment=request.POST.get('comment')

		if not comment:
			messages.error(request,'Comment cannot be empty')
			return HttpResponseRedirect(reverse('Standing_Order_Suspension_Transaction_Releasing_Approval_Details',args=(pk,)))


		record.approval_comment=comment
		record.approval_status=approval_status
		record.approval_date=approval_date
		record.approval_officer=approval_officer
		record.save()
		return HttpResponseRedirect(reverse('Standing_Order_Suspension_Transaction_Releasing_Approval_Load'))


	form.fields['comment_exist'].initial = record.purpose
	context={
	# 'item':item,
	'form':form,
	'record':record,
	'task_array':task_array,
	'task_enabler_array':task_enabler_array,
	'default_password':default_password,
	}
	return render(request,'deskofficer_templates/Standing_Order_Suspension_Transaction_Releasing_Approval_Details.html',context)




def Standing_Order_Suspension_Transaction_Activation_Approval_Processing_Load(request):
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	task_array=[]
	for task in tasks:
		task_array.append(task.task.title)



	task_enabler=TransactionEnabler.objects.filter(status="YES")
	task_enabler_array=[]
	for item in task_enabler:
		task_enabler_array.append(item.title)

	default_password="NO"
	if Staff.objects.filter(admin=request.user,default_password='YES'):
		default_password="YES"

	records = StandingOrderAccountsSuspensionReleaseRequest.objects.filter(status='UNTREATED',approval_status='APPROVED')

	context={
	'records':records,
	'task_array':task_array,
	'task_enabler_array':task_enabler_array,
	'default_password':default_password,

	}
	return render(request,'deskofficer_templates/Standing_Order_Suspension_Transaction_Activation_Approval_Processing_Load.html',context)


def Standing_Order_Suspension_Transaction_Activation_Approval_Processing_Processed(request,pk):
	record = StandingOrderAccountsSuspensionReleaseRequest.objects.get(id=pk)
	item=[]
	if StandingOrderAccounts.objects.filter(transaction=record.transaction.transaction).exists():
		item = StandingOrderAccounts.objects.get(transaction=record.transaction.transaction)

		item.status='ACTIVE'
		item.save()

		record.status='TREATED'
		record.save()
	return HttpResponseRedirect(reverse('Standing_Order_Suspension_Transaction_Activation_Approval_Processing_Load'))


def Transaction_adjustment_search(request):
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	task_array=[]
	for task in tasks:
		task_array.append(task.task.title)



	task_enabler=TransactionEnabler.objects.filter(status="YES")
	task_enabler_array=[]
	for item in task_enabler:
		task_enabler_array.append(item.title)

	default_password="NO"
	if Staff.objects.filter(admin=request.user,default_password='YES'):
		default_password="YES"

	title="Search Membership for Adjustment"
	form = searchForm(request.POST or None)

	return render(request,'deskofficer_templates/Transaction_adjustment_search.html',{'form':form,'title':title,'task_array':task_array,
	'task_enabler_array':task_enabler_array,
	'default_password':default_password,})


def Transaction_adjustment_List_load(request):
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	task_array=[]
	for task in tasks:
		task_array.append(task.task.title)



	task_enabler=TransactionEnabler.objects.filter(status="YES")
	task_enabler_array=[]
	for item in task_enabler:
		task_enabler_array.append(item.title)

	default_password="NO"
	if Staff.objects.filter(admin=request.user,default_password='YES'):
		default_password="YES"

	title="Loan Request order"
	form = searchForm(request.POST)

	if request.method == "POST":
		if request.POST.get("title")=="":
			return HttpResponseRedirect(reverse('Transaction_adjustment_search'))

		members=searchMembers(form['title'].value(),'ACTIVE')

	context={
	'members':members,
	'title':title,
	'task_array':task_array,
	'task_enabler_array':task_enabler_array,
	'default_password':default_password,
	}
	return render(request,'deskofficer_templates/Transaction_adjustment_List_load.html',context)


def Transaction_adjustment_Transactions_load(request,pk):
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	task_array=[]
	for task in tasks:
		task_array.append(task.task.title)



	task_enabler=TransactionEnabler.objects.filter(status="YES")
	task_enabler_array=[]
	for item in task_enabler:
		task_enabler_array.append(item.title)

	default_password="NO"
	if Staff.objects.filter(admin=request.user,default_password='YES'):
		default_password="YES"

	form=Transaction_adjustment_Transactions_form(request.POST or None)
	member=Members.objects.get(id=pk)
	member_selected=MembersAccountsDomain.objects.filter(member=member).first()
	records=TransactionAjustmentRequest.objects.filter(member__member=member_selected.member_id,status='UNTREATED')

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
	'task_array':task_array,
	'task_enabler_array':task_enabler_array,
	'default_password':default_password,
	'records':records,
	}
	return render(request,'deskofficer_templates/Transaction_adjustment_Transactions_load.html',context)


def Transaction_adjustment_Transactions_Accounts_load(request,pk, return_pk):
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	task_array=[]
	for task in tasks:
		task_array.append(task.task.title)



	task_enabler=TransactionEnabler.objects.filter(status="YES")
	task_enabler_array=[]
	for item in task_enabler:
		task_enabler_array.append(item.title)


	default_password="NO"
	if Staff.objects.filter(admin=request.user,default_password='YES'):
		default_password="YES"


	processed_by=CustomUser.objects.get(id=request.user.id)

	transaction=TransactionTypes.objects.get(id=pk)
	minimum_amount=transaction.minimum_amount
	member=Members.objects.get(id=return_pk)

	form=Transaction_adjustment_selection_form(request.POST or None)
	member_selected=MembersAccountsDomain.objects.get(member=member,transaction=transaction)


	if request.method=="POST":
		tdate=get_current_date(now)
		account_number=request.POST.get("account_number")
		transaction=StandingOrderAccounts.objects.get(transaction__account_number=account_number)
		amount = request.POST.get('amount')
		effective_date=request.POST.get('effective_date')

		if TransactionAjustmentRequest.objects.filter(member=member_selected,status='UNTREATED').exists():
			messages.info(request,'You still have an Incomplete Transactions')
			return HttpResponseRedirect(reverse('Transaction_adjustment_Transactions_Accounts_load',args=(pk, return_pk,)))

		if float(amount) == 0:
			if CompulsorySavings.objects.filter(transaction=transaction.transaction.transaction).exists():
				messages.info(request,'This is a compulsory savings, it canot be Zero(0)')
				return HttpResponseRedirect(reverse('Transaction_adjustment_Transactions_Accounts_load',args=(pk, return_pk,)))

			pass

		elif float(amount) < float(minimum_amount):
			messages.info(request,'The amount specified is less then the Minimum Amount of ' +  str(minimum_amount) + ' allowed')
			return HttpResponseRedirect(reverse('Transaction_adjustment_Transactions_Accounts_load',args=(pk, return_pk,)))


		record=TransactionAjustmentRequest(processed_by=processed_by.username,approval_status='PENDING',tdate=tdate,status='UNTREATED',member=member_selected,amount=amount,effective_date=effective_date)
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
		'task_array':task_array,
		'task_enabler_array':task_enabler_array,
	'default_password':default_password,
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
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	task_array=[]
	for task in tasks:
		task_array.append(task.task.title)



	task_enabler=TransactionEnabler.objects.filter(status="YES")
	task_enabler_array=[]
	for item in task_enabler:
		task_enabler_array.append(item.title)

	default_password="NO"
	if Staff.objects.filter(admin=request.user,default_password='YES'):
		default_password="YES"

	records=TransactionAjustmentRequest.objects.filter(approval_status='APPROVED',status='UNTREATED')

	context={
	'task_array':task_array,
	'task_enabler_array':task_enabler_array,
	'default_password':default_password,
	'records':records,
	}
	return render(request,'deskofficer_templates/Transaction_Adjustment_Approved_List_Load.html',context)


def Transaction_Adjustment_Approved_Processed(request,pk):
	tdate=get_current_date(now)
	status='TREATED'
	record=TransactionAjustmentRequest.objects.get(id=pk)
	amount=record.amount
	member=record.member

	amount_exist=record.member.standingorderaccounts.amount
	start_date=record.member.standingorderaccounts.updated_at
	stop_date=tdate
	TransactionAjustmentHistory(member=member,amount=amount_exist,start_date=start_date,stop_date=stop_date).save()

	if float(amount) == 0:
		record.member.standingorderaccounts.delete()
	else:
		record.member.standingorderaccounts.amount=amount
		record.member.standingorderaccounts.save()
	record.status=status
	record.save()
	return HttpResponseRedirect(reverse('Transaction_Adjustment_Approved_List_Load'))


def Transaction_Loan_adjustment_search(request):
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	task_array=[]
	for task in tasks:
		task_array.append(task.task.title)



	task_enabler=TransactionEnabler.objects.filter(status="YES")
	task_enabler_array=[]
	for item in task_enabler:
		task_enabler_array.append(item.title)


	default_password="NO"
	if Staff.objects.filter(admin=request.user,default_password='YES'):
		default_password="YES"

	title="Search Membership for Loan Adjustment"
	form = searchForm(request.POST or None)

	return render(request,'deskofficer_templates/Transaction_Loan_adjustment_search.html',{'form':form,'title':title,'task_array':task_array,
	'task_enabler_array':task_enabler_array,
	'default_password':default_password,})


def Transaction_Loan_adjustment_List_load(request):
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	task_array=[]
	for task in tasks:
		task_array.append(task.task.title)



	task_enabler=TransactionEnabler.objects.filter(status="YES")
	task_enabler_array=[]
	for item in task_enabler:
		task_enabler_array.append(item.title)


	default_password="NO"
	if Staff.objects.filter(admin=request.user,default_password='YES'):
		default_password="YES"

	title="Loan Request order"
	form = searchForm(request.POST)

	if request.method == "POST":
		if request.POST.get("title")=="":
			return HttpResponseRedirect(reverse('Transaction_Loan_adjustment_search'))

		members=searchMembers(form['title'].value(),'ACTIVE')

		context={
		'members':members,
		'title':title,
		'task_array':task_array,
	'task_enabler_array':task_enabler_array,
	'default_password':default_password,
		}
		return render(request,'deskofficer_templates/Transaction_Loan_adjustment_List_load.html',context)


def Transaction_Loan_adjustment_Transaction_load(request,pk):
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	task_array=[]
	for task in tasks:
		task_array.append(task.task.title)



	task_enabler=TransactionEnabler.objects.filter(status="YES")
	task_enabler_array=[]
	for item in task_enabler:
		task_enabler_array.append(item.title)


	default_password="NO"
	if Staff.objects.filter(admin=request.user,default_password='YES'):
		default_password="YES"

	member=Members.objects.get(id=pk)
	records=LoansRepaymentBase.objects.filter(member=member,balance__lt=0)

	existing_requests=TransactionLoanAjustmentRequest.objects.filter(member__member=member,status='UNTREATED')

	context={
	'task_array':task_array,
	'task_enabler_array':task_enabler_array,
	'default_password':default_password,
	'records':records,
	'member':member,
	'existing_requests':existing_requests,
	}
	return render(request,'deskofficer_templates/Transaction_Loan_adjustment_Transaction_load.html',context)


def Transaction_Loan_adjustment_Transaction_Preview(request,pk,loan_code):
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	task_array=[]
	for task in tasks:
		task_array.append(task.task.title)



	task_enabler=TransactionEnabler.objects.filter(status="YES")
	task_enabler_array=[]
	for item in task_enabler:
		task_enabler_array.append(item.title)

	default_password="NO"
	if Staff.objects.filter(admin=request.user,default_password='YES'):
		default_password="YES"

	form=Transaction_Loan_adjustment_selection_form(request.POST or None)

	member=Members.objects.get(id=pk)
	loan=[]
	if request.method=='POST':

		loan_id=request.POST.get('loan')
		loan=LoansRepaymentBase.objects.get(id=loan_id)
	else:
		loan=LoansRepaymentBase.objects.get(id=loan_code)

	context={
	'task_array':task_array,
	'task_enabler_array':task_enabler_array,
	'default_password':default_password,
	'member':member,
	'loan':loan,
	'form':form,
	}
	return render(request,'deskofficer_templates/Transaction_Loan_adjustment_Transaction_Preview.html',context)


def Transaction_Loan_adjustment_Transaction_Process(request,pk,loan_code):
	# member=Members.objects.get(id=pk)

	loan=LoansRepaymentBase.objects.get(id=loan_code)
	loan_amount=loan.loan_amount
	amount_paid=loan.amount_paid
	balance=loan.balance
	transaction=loan.transaction
	default_duration=transaction.duration
	tdate=get_current_date(now)

	monthly_repayment=math.ceil(float(loan_amount)/float(default_duration))
	months_paid=math.ceil(float(amount_paid)/float(monthly_repayment))
	remaining_months=int(default_duration)-int(months_paid)

	expected_repayment=math.ceil(float(abs(balance))/float(remaining_months))

	if request.method =="POST":
		purpose=request.POST.get('purpose')
		repayment=request.POST.get('repayment')
		amount=request.POST.get('amount')
		effective_date=now

		if float(amount) < float(expected_repayment):
			messages.info(request,"The Amount Specified is not Allowed, you have Minimum of " + str(expected_repayment) + " to pay off this loan in " +  str(remaining_months) + " month(s) interval" )
			return HttpResponseRedirect(reverse('Transaction_Loan_adjustment_Transaction_Preview',args=(pk,loan_code,)))

		if float(amount) == float(expected_repayment):
			messages.info(request,"No Change Made in " + str(expected_repayment) + " to pay off this loan in " +  str(remaining_months) + " month(s) interval" )
			return HttpResponseRedirect(reverse('Transaction_Loan_adjustment_Transaction_Preview',args=(pk,loan_code,)))



		if TransactionLoanAjustmentRequest.objects.filter(member=loan,status='UNTREATED'):
			messages.info(request,'You still have an Incomplete Transactions')
			return HttpResponseRedirect(reverse('Transaction_Loan_adjustment_Transaction_Preview',args=(pk,loan_code,)))

		record=TransactionLoanAjustmentRequest(member=loan,
			amount=amount,approval_status='PENDING',effective_date=effective_date,tdate=tdate,status='UNTREATED')
		record.save()

		return HttpResponseRedirect(reverse('Transaction_Loan_adjustment_Transaction_load',args=(pk,)))


def Transaction_Loan_adjustment_Transaction_Cancel(request,pk):
	record=TransactionLoanAjustmentRequest(id=pk)
	return_pk=record.member.member.id
	record.delete()
	return HttpResponseRedirect(reverse('Transaction_Loan_adjustment_Transaction_load',args=(return_pk,)))


def Transaction_Loan_adjustment_Transaction_Approved_List_Load(request):
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	task_array=[]
	for task in tasks:
		task_array.append(task.task.title)



	task_enabler=TransactionEnabler.objects.filter(status="YES")
	task_enabler_array=[]
	for item in task_enabler:
		task_enabler_array.append(item.title)

	default_password="NO"
	if Staff.objects.filter(admin=request.user,default_password='YES'):
		default_password="YES"

	records=TransactionLoanAjustmentRequest.objects.filter(status='UNTREATED',approval_status='APPROVED')

	context={
	'task_array':task_array,
	'task_enabler_array':task_enabler_array,
	'default_password':default_password,
	'records':records,
	}
	return render(request,'deskofficer_templates/Transaction_Loan_adjustment_Transaction_Approved_List_Load.html',context)


def Transaction_Loan_adjustment_Transaction_Approved_details_Processed(request,pk):
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	task_array=[]
	for task in tasks:
		task_array.append(task.task.title)


	task_enabler=TransactionEnabler.objects.filter(status="YES")
	task_enabler_array=[]
	for item in task_enabler:
		task_enabler_array.append(item.title)

	default_password="NO"
	if Staff.objects.filter(admin=request.user,default_password='YES'):
		default_password="YES"

	record=TransactionLoanAjustmentRequest.objects.get(id=pk)
	LoansRepaymentBase.objects.filter(loan_number=record.member.loan_number).update(repayment=record.amount)
	record.status='TREATED'
	record.save()
	return HttpResponseRedirect(reverse('Transaction_Loan_adjustment_Transaction_Approved_List_Load'))






#########################################################
############### LOAN TRANSACTION ########################
#########################################################
def loan_request_order_discard(request):
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	task_array=[]
	for task in tasks:
		task_array.append(task.task.title)



	task_enabler=TransactionEnabler.objects.filter(status="YES")
	task_enabler_array=[]
	for item in task_enabler:
		task_enabler_array.append(item.title)

	default_password="NO"
	if Staff.objects.filter(admin=request.user,default_password='YES'):
		default_password="YES"


	records = LoanRequest.objects.filter(submission_status='PENDING')


	context={
	'records':records,
	'task_array':task_array,
	'task_enabler_array':task_enabler_array,
	'default_password':default_password,
	}
	return render(request,'deskofficer_templates/loan_request_order_discard.html',context)


def loan_request_order_discard_delete(request,pk):
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	task_array=[]
	for task in tasks:
		task_array.append(task.task.title)



	task_enabler=TransactionEnabler.objects.filter(status="YES")
	task_enabler_array=[]
	for item in task_enabler:
		task_enabler_array.append(item.title)

	default_password="NO"
	if Staff.objects.filter(admin=request.user,default_password='YES'):
		default_password="YES"

	LoanRequest.objects.filter(id=pk).delete()
	return HttpResponseRedirect(reverse('loan_request_order_discard'))


def loan_request_search(request):
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	task_array=[]
	for task in tasks:
		task_array.append(task.task.title)



	task_enabler=TransactionEnabler.objects.filter(status="YES")
	task_enabler_array=[]
	for item in task_enabler:
		task_enabler_array.append(item.title)


	default_password="NO"
	if Staff.objects.filter(admin=request.user,default_password='YES'):
		default_password="YES"

	title="Search Membership Loan Request"
	form = searchForm(request.POST or None)

	return render(request,'deskofficer_templates/loan_request_search.html',{'form':form,'title':title,'task_array':task_array,
	'task_enabler_array':task_enabler_array,
	'default_password':default_password,})


def loan_request_list_load(request):

	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	task_array=[]
	for task in tasks:
		task_array.append(task.task.title)



	task_enabler=TransactionEnabler.objects.filter(status="YES")
	task_enabler_array=[]
	for item in task_enabler:
		task_enabler_array.append(item.title)


	default_password="NO"
	if Staff.objects.filter(admin=request.user,default_password='YES'):
		default_password="YES"

	title="Loan Request order"
	form = searchForm(request.POST)

	if request.method == "POST":
		if request.POST.get("title")=="":
			return HttpResponseRedirect(reverse('loan_request_search'))

		members=searchMembers(form['title'].value(),'ACTIVE')

		context={
		'members':members,
		'title':title,
		'task_array':task_array,
	'task_enabler_array':task_enabler_array,
	'default_password':default_password,
		}
		return render(request,'deskofficer_templates/loan_request_list_load.html',context)


def loan_request_order(request,pk):
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	task_array=[]
	for task in tasks:
		task_array.append(task.task.title)



	task_enabler=TransactionEnabler.objects.filter(status="YES")
	task_enabler_array=[]
	for item in task_enabler:
		task_enabler_array.append(item.title)

	default_password="NO"
	if Staff.objects.filter(admin=request.user,default_password='YES'):
		default_password="YES"

	submission_status="PENDING"
	transaction_status='UNTREATED'
	form=loan_request_order_form(request.POST or None)
	member=Members.objects.get(id=pk)

	exist_loans = LoanRequest.objects.filter(member_id=member,submission_status='PENDING',transaction_status='UNTREATED',approval_status='PENDING')


	loan_based_saving=[]
	if LoanBasedSavings.objects.all().exists():
		loan_based_saving=LoanBasedSavings.objects.all().first()
		loan_based_code=loan_based_saving.savings.code
		# return HttpResponse(loan_based_code)

	if request.method=="POST":
		if TransactionSources.objects.filter(title='LOAN').exists():
			queryset=TransactionSources.objects.get(title='LOAN')

			if queryset.maximum_amount<=0:
				messages.error(request,'Overall Maximum Loan Amount not Set')
				return HttpResponseRedirect(reverse('loan_request_order',args=(pk,)))

			if queryset.salary_loan_relationship<=0:
				messages.error(request,'Salary Loan Relationship not Set')
				return HttpResponseRedirect(reverse('loan_request_order',args=(pk,)))
		else:
			messages.error(request,'Please configuration Sources')
			return HttpResponseRedirect(reverse('loan_request_order',args=(pk,)))

		tdate=get_current_date(now)


		if form.is_valid():
			approval_status='PENDING'
			category='MONETARY'

			processed_by=CustomUser.objects.get(id=request.user.id)

			period_obj = form.cleaned_data["period"]
			period=Commodity_Period.objects.get(id=period_obj)

			batch_obj = form.cleaned_data["batch"]
			batch=Commodity_Period_Batch.objects.get(id=batch_obj)

			loan_obj = form.cleaned_data["loans"]

			loan=TransactionTypes.objects.get(id=loan_obj)

			amount = form.cleaned_data["amount"]
			maximum_amount = loan.maximum_amount
			multiple_loan_status=loan.multiple_loan_status

			desired_duration=request.POST.get('duration')

			selected_trannsaction_rate=0
			if loan.savings_rate == "YES":
				selected_trannsaction_rate=loan.saving_rating
				# print(selected_trannsaction_rate)
				# print("+++++++++++++++++++++++++++++++++++++++")
				# print("+++++++++++++++++++++++++++++++++++++++")
				# print("+++++++++++++++++++++++++++++++++++++++")
				# print("+++++++++++++++++++++++++++++++++++++++")
				if selected_trannsaction_rate > 0:
					percentage_amount=(float(selected_trannsaction_rate)/100)*float(amount)
					loan_based_account_number=str(loan_based_code) + str(member.get_member_Id)
					# print(percentage_amount)
					# print("=================================")
					# print("=================================")
					saved_amount=0
					if PersonalLedger.objects.filter(account_number=loan_based_account_number).exists():
						ledger_balance=PersonalLedger.objects.filter(account_number=loan_based_account_number).last()
						saved_amount=ledger_balance.balance
					if not saved_amount:
						messages.error(request,'You do not have any savings for this Amount')
						return HttpResponseRedirect(reverse('loan_request_order',args=(pk,)))

					if float(percentage_amount) > float(saved_amount):
						balance_remainer=float(percentage_amount)-float(saved_amount)
						messages.error(request,'You do not have required savings for this Loan Amount, Please top up your account with ' + str(balance_remainer))
						return HttpResponseRedirect(reverse('loan_request_order',args=(pk,)))

			if desired_duration and int(desired_duration)>0:
				if int(desired_duration) > int(loan.duration):
					messages.error(request,'The Desired Duration cannot be greater than the Default')
					return HttpResponseRedirect(reverse('loan_request_order',args=(pk,)))
				else:
					duration=desired_duration
			else:
				duration=int(loan.duration)


			if not amount:
				messages.error(request,'Loan Amount Missing')
				return HttpResponseRedirect(reverse('loan_request_order',args=(pk,)))

			total_loan=0

			if LoansRepaymentBase.objects.filter(member=member,transaction=loan).filter(Q(balance__lt=0)).exists():
				if multiple_loan_status == 'NOT ALLOWED':
					messages.info(request,"Additional Loan not allowed for the Transaction")
					return HttpResponseRedirect(reverse('loan_request_order', args=(pk,)))

				loans=LoansRepaymentBase.objects.filter(member=member,transaction=loan).filter(Q(balance__lt=0))
				loans_sum=LoansRepaymentBase.objects.filter(member=member,transaction=loan).filter(Q(balance__lt=0)).aggregate(total_repayment=Sum('repayment'),total_amount=Sum('balance'))
				total_loan=loans_sum['total_amount']
				repayment_total=loans_sum['total_repayment']
				grand_total=float(abs(total_loan)) + float(amount)


				max_amount=queryset.maximum_amount
				salary_rate=queryset.salary_loan_relationship

				if float(grand_total) > float(max_amount):
					amount_due = float(max_amount)-float(abs(total_loan))
					messages.error(request,'You have Exceeded the Maximum Amount Allowed, you are qualified for '+ str(amount_due))
					return HttpResponseRedirect(reverse('loan_request_order', args=(pk,)))

			if loan.category==category:
				if float(amount)>float(maximum_amount):
					messages.error(request,"Amount Specified is More than " + str(maximum_amount) + " Maximum Amount allowed for this Transaction")
					return HttpResponseRedirect(reverse('loan_request_order', args=(pk,)))


			if LoanRequest.objects.filter(member=member,loan=loan,transaction_status='UNTREATED').exists():
				messages.error(request,"You still have Open Transaction")
				return HttpResponseRedirect(reverse('loan_request_order', args=(pk,)))

			record=LoanRequest(duration=duration,period=period,batch=batch,tdate=tdate,member=member,loan_amount=amount,loan=loan,submission_status=submission_status,approval_status='PENDING',transaction_status=transaction_status,processed_by=processed_by.username)
			record.save()
			return HttpResponseRedirect(reverse('loan_request_order', args=(pk,)))

		else:
			messages.error(request,"One or more record is missing")
			return HttpResponseRedirect(reverse('loan_request_order', args=(pk,)))

	context={

	'form':form,

	'member':member,
	'exist_loans':exist_loans,
	'pk':pk,
	'task_array':task_array,
	'task_enabler_array':task_enabler_array,
	'default_password':default_password,
	}
	return render(request,'deskofficer_templates/loan_request_order.html',context)



def loan_request_order_delete(request,pk,return_pk):
	record=LoanRequest.objects.get(id=pk)
	LoanRequestAttachments.objects.filter(applicant=record).delete()
	record.delete()
	return HttpResponseRedirect(reverse('loan_request_order', args=(return_pk,)))


def loan_request_criteria_Loading(request,pk):
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	task_array=[]
	for task in tasks:
		task_array.append(task.task.title)



	task_enabler=TransactionEnabler.objects.filter(status="YES")
	task_enabler_array=[]
	for item in task_enabler:
		task_enabler_array.append(item.title)

	default_password="NO"
	if Staff.objects.filter(admin=request.user,default_password='YES'):
		default_password="YES"

	applicant=LoanRequest.objects.get(id=pk)

	total_savings=0
	savings=[]

	if StandingOrderAccounts.objects.filter(transaction__member_id=applicant.member_id).exists():

		if CompulsorySavings.objects.all().exists():
			compulsory_savings=CompulsorySavings.objects.first()
			compulsory_savings_record=get_compulsory_savings(compulsory_savings.transaction,applicant.member_id)

			if not compulsory_savings_record:
				messages.error(request,'No record for Compulsary Savings')
				return HttpResponseRedirect(reverse('loan_request_order',args=(applicant.member_id,)))
		else:
			messages.error(request,'Compulsary Savings Not Set')
			return HttpResponseRedirect(reverse('loan_request_order',args=(applicant.member_id,)))

		if LoanBasedSavings.objects.all().exists():
			loan_base_savings=LoanBasedSavings.objects.first()
			loan_base_savings_record=get_loan_based_savings(loan_base_savings.savings,applicant.member_id)


			if not loan_base_savings_record:
				messages.error(request,'No record for Loan Based Savings')
				return HttpResponseRedirect(reverse('loan_request_order',args=(applicant.member_id,)))

		else:
			messages.error(request,'Loan Based Savings Not Set')
			return HttpResponseRedirect(reverse('loan_request_order',args=(applicant.member_id,)))


		savings = get_standing_orders(applicant.member_id)
		total_savings=get_standing_orders_sum(applicant.member_id)

	else:
		messages.error(request,'No Available Savings Standing Order')
		return HttpResponseRedirect(reverse('loan_request_order',args=(applicant.member_id,)))


	total_loans=0
	loans=[]

	if LoansRepaymentBase.objects.filter(Q(balance__lt=0) & Q(member_id=applicant.member_id,status='ACTIVE')).exists():
		loans=LoansRepaymentBase.objects.filter(Q(balance__lt=0) & Q(member_id=applicant.member_id))
		loans_sum=LoansRepaymentBase.objects.filter(Q(balance__lt=0) & Q(member_id=applicant.member_id)).aggregate(total_amount=Sum('repayment'))
		total_loans=loans_sum['total_amount']


	shop_balance=0
	shops=[]
	if CooperativeShopLedger.objects.filter(member_id=applicant.member_id).exists():
		shops =CooperativeShopLedger.objects.filter(Q(balance__lt=0) & Q(member_id=applicant.member_id)).order_by('-id').first()
		shop_balance=abs(shops.balance)


	total_debit=float(total_savings)+float(total_loans)+float(shop_balance)

	attachment_form=loan_request_document_attachment_form(request.POST or None)


	if request.method=="POST" and 'attachment' in request.POST:

		description = request.POST.get("payment_as_at")
		date_format = '%Y-%m-%d'
		dtObj = datetime.datetime.strptime(description, date_format)
		description=get_current_date(dtObj)

		net_pay=request.POST.get('net_pay')
		if request.FILES.get('image', False):
			image = request.FILES['image']
			fs=FileSystemStorage()
			filename=fs.save(image.name,image)
			image_url=fs.url(filename)
		else:
			image_url=None

		if not description:
			messages.error(request,'Description Missing')
			return HttpResponseRedirect(reverse('loan_request_criteria_Loading',args=(pk,)))

		if not net_pay or float(net_pay) == 0:
			messages.error(request,'Net Pay Missing')
			return HttpResponseRedirect(reverse('loan_request_criteria_Loading',args=(pk,)))

		applicant.description=description
		applicant.net_pay=net_pay
		applicant.image=image_url
		applicant.save()

		applicant.member.last_used_net_pay=net_pay
		applicant.member.net_pay_as_at=description
		applicant.member.save()

		return HttpResponseRedirect(reverse('loan_request_criteria_Loading',args=(pk,)))


	# return HttpResponse("OPOOO")
	attachment_form.fields['net_pay'].initial=applicant.member.last_used_net_pay
	if applicant.member.net_pay_as_at:
		attachment_form.fields['payment_as_at'].initial=applicant.member.net_pay_as_at
	else:
		attachment_form.fields['payment_as_at'].initial=now
	context={


	'applicant':applicant,
	'savings':savings,
	'loans':loans,
	'shops':shops,
	'shop_balance':shop_balance,
	'total_debit':total_debit,
	'pk':pk,
	'attachment_form':attachment_form,
	'task_array':task_array,
	'task_enabler_array':task_enabler_array,
	'default_password':default_password,
	}
	return render(request,'deskofficer_templates/loan_request_criteria_Loading.html',context)


def LoanRequestAttachments_delete(request,pk,return_pk):
	item=LoanRequest.objects.get(id=pk)

	item.image=None
	item.gross_pay=0
	item.net_pay=0
	item.description=""
	item.save()
	return HttpResponseRedirect(reverse('loan_request_criteria_Loading',args=(return_pk,)))



def loan_request_preview(request,pk):
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	task_array=[]
	for task in tasks:
		task_array.append(task.task.title)



	task_enabler=TransactionEnabler.objects.filter(status="YES")
	task_enabler_array=[]
	for item in task_enabler:
		task_enabler_array.append(item.title)

	default_password="NO"
	if Staff.objects.filter(admin=request.user,default_password='YES'):
		default_password="YES"

	form=MemberShipRequestAdditionalInfo_form(request.POST or None)


	apex_loan=TransactionSources.objects.get(title='LOAN')

	applicant=LoanRequest.objects.get(id=pk)

	net_pay=applicant.net_pay
	loan_type=applicant.loan.name
	loan_amount=applicant.loan_amount
	duration = applicant.duration

	membership_waver=False
	savings_made_waver=False
	multiple_loans_waver=False
	salary_status_waver=False

	if MembersExclusiveness.objects.filter(transaction=applicant.loan,period=applicant.period,batch=applicant.batch,processing_status='UNPROCESSED',approval_status='APPROVED').exists():
		wavers=MembersExclusiveness.objects.filter(transaction=applicant.loan,period=applicant.period,batch=applicant.batch,processing_status='UNPROCESSED',approval_status='APPROVED')
		for item in wavers:
			if item.task.title == 'MEMBERSHIP AGE':
				membership_waver=True
			elif item.task.title == 'SAVINGS MADE':
				multiple_loans_waver=True
			elif item.task.title == 'SALARY STATUS':
				salary_status_waver=True


	loan_savings_status=False
	loan_based_saving=[]
	savings_saved=0
	loan_saving_relationship=[]


	if applicant.loan.savings_rate == 'YES':

		# Computing Savings Made
		# ==============================

		if LoanBasedSavings.objects.all().exists():
			loan_based_saving = LoanBasedSavings.objects.first()
		else:
			messages.error(request,'Loan Based Savings not Set')
			return HttpResponseRedirect(reverse('loan_request_criteria_Loading', args=(pk,)))

		loans_anchored=TransactionTypes.objects.filter(savings_rate='YES')


		loans_anchored_sum=LoansRepaymentBase.objects.filter(transaction__savings_rate='YES').filter(Q(balance__lt=0) & Q(member_id=applicant.member_id)).aggregate(total_amount=Sum('balance'))
		total_loans_anchored=loans_anchored_sum['total_amount']
		if not total_loans_anchored:
			total_loans_anchored=0

		expected_total_loans=abs(float(total_loans_anchored)) + float(loan_amount)

		savings_saved=0
		if StandingOrderAccounts.objects.filter(transaction__transaction=loan_based_saving.savings,transaction__member=applicant.member).exists():
			account_id=StandingOrderAccounts.objects.get(transaction__transaction=loan_based_saving.savings,transaction__member=applicant.member)

			savings_saved=0
			if PersonalLedger.objects.filter(account_number=account_id.transaction.account_number).exists():
				savings_ledger=PersonalLedger.objects.filter(account_number=account_id.transaction.account_number).last()
				savings_saved=savings_ledger.balance
			else:
				messages.error(request,'No Savings Available for Loan Based Savings')
				return HttpResponseRedirect(reverse('loan_request_criteria_Loading', args=(pk,)))

		else:
			messages.error(request,'No account for Loan Based Savings')
			return HttpResponseRedirect(reverse('loan_request_criteria_Loading', args=(pk,)))


		loan_based_saving_rating=apex_loan.loan_based_saving

		if not float(loan_based_saving_rating):
			messages.error(request,'Loan Based Saving Rating not set')
			return HttpResponseRedirect(reverse('loan_request_criteria_Loading', args=(pk,)))


		loan_saving_relationship=float(int(loan_based_saving_rating)/100) * float(expected_total_loans)

		if savings_made_waver:
			loan_savings_status=True
		else:
			if float(savings_saved) > float(loan_saving_relationship):
				loan_savings_status=True

		if not loan_savings_status:

			messages.error(request,'You do not Have Expected Savings for this Loan Amount, You have  ' + str(savings_saved) + ' while you need ' + str(loan_saving_relationship) )
			return HttpResponseRedirect(reverse('loan_request_criteria_Loading', args=(pk,)))
	else:
		loan_savings_status=True

	total_savings=0
	total_savings=get_standing_orders_sum(applicant.member_id)
	if total_savings==None:
		total_savings=0


	# Computing Outstanding Fascilities
	# ==============================
	total_loans=0
	loans_sum=LoansRepaymentBase.objects.filter(Q(balance__lt=0) & Q(member_id=applicant.member_id)).aggregate(total_amount=Sum('repayment'))
	total_loans=loans_sum['total_amount']
	if total_loans==None:
		total_loans=0

	shop_balance=0
	shops =CooperativeShopLedger.objects.filter(Q(balance__lt=0) & Q(member_id=applicant.member_id)).order_by('-id').first()
	if shops:
		shop_balance=abs(shops.balance)



	total_debit=float(total_savings)+float(total_loans)+float(shop_balance)


	balance=float(net_pay)-total_debit


	# Computin Date Joined
	# ==============================
	date_joined = applicant.member.date_joined
	now = datetime.datetime.now()

	# Computing Salary Loan Relationship
	# =============================
	salary_loan_relationship = apex_loan.salary_loan_relationship

	if not float(salary_loan_relationship):
		messages.error(request,'Salary Loan Relationship not set')
		return HttpResponseRedirect(reverse('loan_request_criteria_Loading', args=(pk,)))


	salary_loan_relationship_computed= float(int(salary_loan_relationship)/100) * float(balance)



	# Computinh Interest Rate
	# ==============================

	interest_rate = applicant.loan.interest_rate

	if not float(interest_rate):
		messages.error(request,'Interest Rate not set')
		return HttpResponseRedirect(reverse('loan_request_criteria_Loading', args=(pk,)))

	interest= float(int(interest_rate)/100) * float(applicant.loan_amount)




	# Computing Maturity Age

	loan_age = int(applicant.loan.loan_age)

	if not int(loan_age):
		messages.error(request,'Members Loan Age not set')
		return HttpResponseRedirect(reverse('loan_request_criteria_Loading', args=(pk,)))


	# Computing Member's Age
	members_age = (now.year - date_joined.year) * 12 + (now.month - date_joined.month)

	if members_age == 0:
		d_date=get_current_date(date_joined)
		p_date=get_current_date(now)
		member_age_pick=str(p_date-d_date) + " DAY(s)"
	else:
		members_age=members_age
		# member_age_pick=str(date_joined.day) + "MONTH(S)"
		member_age_pick=str(members_age) + " MONTH(S)"



	# Computing Interest Deduction
	# ==============================
	interest_deduction=applicant.loan.interest_deduction

	if not interest_deduction:
		messages.error(request,'Interest deduction source not set')
		return HttpResponseRedirect(reverse('loan_request_criteria_Loading', args=(pk,)))


	if interest_deduction == "SOURCE":
		amount_scheduled = float(loan_amount)

	else:
		amount_scheduled = float(loan_amount)+ float(interest)

	if int(duration) == 0:
		messages.error(request,'Please set the Loan Duration')
		return HttpResponseRedirect(reverse('loan_request_criteria_Loading', args=(pk,)))


	# Computing Admin Chages
	# ==============================
	admin_charges_minimum = applicant.loan.admin_charges_minimum

	if float(admin_charges_minimum) >= float(loan_amount):
		admin_charge=applicant.loan.default_admin_charges
	else:
		if applicant.loan.admin_charges_rating == "PERCENTAGE":
			admin_charge=(float(applicant.loan.admin_charges) / 100) * float(loan_amount)
		else:
			admin_charge=applicant.loan.admin_charges


	# Computing Monthly Repayment
	# ==============================
	monthly_repayment=math.ceil(float(amount_scheduled)/float(duration))


	# Computing Button Enabler
	# ==============================
	salary_status=True
	if salary_status_waver:
		salary_status=False
	else:
		if float(monthly_repayment)> float(salary_loan_relationship_computed):
			salary_status=False


	Member_Status = False
	if membership_waver:
		Member_Status = True
	else:
		if int(members_age)>int(loan_age):
			Member_Status = True

	record_array=[]

	if request.method=="POST":

		comment=request.POST.get("comment")

		applicant.comment=comment
		applicant.submission_status='SUBMITTED'
		applicant.admin_charge=admin_charge
		applicant.interest=interest
		applicant.save()

		description="NET PAY"
		value=net_pay
		category='ANALYSIS'
		waver=False
		Loan_Request_Posting(applicant,description,value,category,'UNTREATED',waver)

		description="SALARY BALANCE AFTER DEDUCTIONS"
		value=balance
		category='ANALYSIS'
		waver=False
		Loan_Request_Posting(applicant,description,value,category,'UNTREATED',waver)

		description=loan_type
		value=loan_amount
		category='ANALYSIS'
		waver=False
		Loan_Request_Posting(applicant,description,value,category,'UNTREATED',waver)

		description="MONTHLY DEDUCTIONS"
		value=total_savings
		category='ANALYSIS'
		waver=False
		Loan_Request_Posting(applicant,description,value,category,'UNTREATED',waver)

		description="MONTHLY LOAN REPAYMENTS"
		value=total_loans
		category='ANALYSIS'
		waver=False
		Loan_Request_Posting(applicant,description,value,category,'UNTREATED',waver)

		description="COOPERATIVE SHOP"
		value=shop_balance
		category='ANALYSIS'
		waver=False
		Loan_Request_Posting(applicant,description,value,category,'UNTREATED',waver)

		description="LOAN DURATION"
		value=str(duration) + " MONTHS"
		category='ANALYSIS'
		waver=False
		Loan_Request_Posting(applicant,description,value,category,'UNTREATED',waver)

		description="SALARY LOAN RELATIONSHIP"
		value=str(salary_loan_relationship) + "%"
		category='ANALYSIS'
		waver=False
		Loan_Request_Posting(applicant,description,value,category,'UNTREATED',waver)

		description="SALARY LOAN RELATIONSHIP COMPUTED"
		value=salary_loan_relationship_computed
		category='ANALYSIS'
		waver=False
		Loan_Request_Posting(applicant,description,value,category,'UNTREATED',waver)

		description="MATURITY AGE"
		value=str(loan_age) + " MONTHS"
		category='ANALYSIS'
		waver=False
		Loan_Request_Posting(applicant,description,value,category,'UNTREATED',waver)

		description="DATE JOINED"
		value=date_joined
		category='ANALYSIS'
		waver=False
		Loan_Request_Posting(applicant,description,value,category,'UNTREATED',waver)

		description="MEMBERS AGE"
		value=member_age_pick
		category='ANALYSIS'
		waver=False
		Loan_Request_Posting(applicant,description,value,category,'UNTREATED',waver)

		description="LOAN INTEREST RATE"
		value=str(interest_rate) + "%"
		category='ANALYSIS'
		waver=False
		Loan_Request_Posting(applicant,description,value,category,'UNTREATED',waver)

		description="INTEREST DEDUCTION"
		value=interest_deduction
		category='ANALYSIS'
		waver=False
		Loan_Request_Posting(applicant,description,value,category,'UNTREATED',waver)

		description="LOAN INTEREST"
		value=interest
		category='ANALYSIS'
		waver=False
		Loan_Request_Posting(applicant,description,value,category,'UNTREATED',waver)

		description="AMOUNT SCHEDULED"
		value=amount_scheduled
		category='ANALYSIS'
		waver=False
		Loan_Request_Posting(applicant,description,value,category,'UNTREATED',waver)

		description="MONTHLY REPAYMENT"
		value= monthly_repayment
		category='ANALYSIS'
		waver=False
		Loan_Request_Posting(applicant,description,value,category,'UNTREATED',waver)

		description="ADMIN CHARGE"
		value= admin_charge
		category='ANALYSIS'
		waver=False
		Loan_Request_Posting(applicant,description,value,category,'UNTREATED',waver)

		if loan_based_saving:
			description="LOAN BASED SAVINGS"
			value=loan_based_saving.savings.name
			category='ANALYSIS'
			waver=False
			Loan_Request_Posting(applicant,description,value,category,'UNTREATED',waver)


			description="AMOUNT SAVED"
			value='#' + str(savings_saved)
			category='ANALYSIS'
			waver=False
			Loan_Request_Posting(applicant,description,value,category,'UNTREATED',waver)


			description="LOAN BASED SAVINGS RATE"
			value=str(loan_based_saving_rating) + "%"
			category='ANALYSIS'
			waver=False
			Loan_Request_Posting(applicant,description,value,category,'UNTREATED',waver)


		description="MEMBERSHIP STATUS"
		value=Member_Status
		category='SUMMARY'
		waver=membership_waver
		Loan_Request_Posting(applicant,description,value,category,'UNTREATED',waver)

		description="SALARY STATUS"
		value=salary_status
		category='SUMMARY'
		waver=salary_status_waver
		Loan_Request_Posting(applicant,description,value,category,'UNTREATED',waver)

		if applicant.loan.savings_rate == "YES":
			description="LOAN SAVINGS BASED STATUS"
			value=loan_savings_status
			category='SUMMARY'
			waver=savings_made_waver
			Loan_Request_Posting(applicant,description,value,category,'UNTREATED',waver)

		return HttpResponseRedirect(reverse('loan_request_search'))

	if membership_waver:
		membership_button_enabled=True
	else:
		membership_button_enabled=False
		if Member_Status == True:
			membership_button_enabled=True

	if savings_made_waver:
		savings_made_button_enabled=True
	else:
		savings_made_button_enabled=False
		if loan_savings_status == True:
			savings_made_button_enabled=True

	if salary_status_waver:
		salary_status_button_enabled=True
	else:
		salary_status_button_enabled=False
		if salary_status == True:
			salary_status_button_enabled=True



	button_enabled=False


	# if membership_button_enabled and savings_made_button_enabled and salary_status_button_enabled:
	if membership_button_enabled and savings_made_button_enabled and salary_status_button_enabled:
		button_enabled=True
	record_array.append(('Net Pay',net_pay))
	record_array.append(('Monthly Contributions',total_savings))
	record_array.append(('Existing Loan Monthly Repayment',total_loans))
	record_array.append(('Cooperative Shop',shop_balance))
	record_array.append(('Salary Balance After Deductions',balance))
	record_array.append((loan_type,loan_amount))
	record_array.append(('Loan Duration',str(duration) + " Month(s)"))
	record_array.append(('Salary Loan Relationship',str(salary_loan_relationship) + "%"))
	record_array.append(('Salary Loan Relationship Computed',salary_loan_relationship_computed))
	record_array.append(('Maturity Age',str(loan_age) + " Month(s)"))
	record_array.append(('Date Joined',date_joined))
	record_array.append(('Members Age',member_age_pick))
	record_array.append(('Loan Interest Rate',str(interest_rate) + "%"))
	record_array.append(('Interest Deduction',interest_deduction))
	record_array.append(('Loan Interest',interest))
	record_array.append(('Amount Scheduled',amount_scheduled))
	record_array.append(('Monthly Repayment',monthly_repayment))
	record_array.append(('Admin Charge',admin_charge))
	if loan_based_saving:
		record_array.append(('Loan Based Savings',loan_based_saving.savings.name))
		record_array.append(('Amount Saved (' + loan_based_saving.savings.name + ")",savings_saved))
		record_array.append(('Loan Based Savings Rate',str(loan_based_saving_rating) + "%"))

	form.fields['comment'].initial="For Your Consideration and Kind Approval"

	context={
	'record_array':record_array,
	'form':form,
	'savings_anchored':applicant.loan.savings_rate,
	'membership_waver':membership_waver,
	'salary_status_waver':salary_status_waver,
	'savings_made_waver':savings_made_waver,
	'multiple_loans_waver':multiple_loans_waver,
	'applicant':applicant,
	'pk':pk,
	'salary_status':salary_status,
	'Member_Status':Member_Status,
	'loan_savings_status':loan_savings_status,
	'button_enabled':button_enabled,
	'task_array':task_array,
	'task_enabler_array':task_enabler_array,
	'default_password':default_password,
	'savings_saved':savings_saved,
	}

	return render(request,'deskofficer_templates/loan_request_preview.html',context)


def loan_request_manage_period_load(request):
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	task_array=[]
	for task in tasks:
		task_array.append(task.task.title)



	task_enabler=TransactionEnabler.objects.filter(status="YES")
	task_enabler_array=[]
	for item in task_enabler:
		task_enabler_array.append(item.title)

	default_password="NO"
	if Staff.objects.filter(admin=request.user,default_password='YES'):
		default_password="YES"


	form=loan_request_order_form(request.POST or None)
	exist_loans=[]
	if request.method == 'POST':
		period_id=request.POST.get("period")
		period = Commodity_Period.objects.get(id=period_id)

		batch_id=request.POST.get('batch')
		batch=Commodity_Period_Batch.objects.get(id=batch_id)

		loan_id = request.POST.get('loans')
		loan = TransactionTypes.objects.get(id=loan_id)

		exist_loans = LoanRequest.objects.filter(loan=loan,period=period,batch=batch,submission_status='SUBMITTED',transaction_status='UNTREATED',approval_status='PENDING')

	context={
	'exist_loans':exist_loans,
	'form':form,
	'task_array':task_array,
	'task_enabler_array':task_enabler_array,
	'default_password':default_password,
	}
	return render(request,'deskofficer_templates/loan_request_manage_period_load.html',context)

def loan_request_manage_transaction_delete(request,pk):
	LoanRequest.objects.get(id=pk).delete()
	return HttpResponseRedirect(reverse('loan_request_manage_period_load'))


def loan_request_approved_Issue_form_period_load(request):
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	task_array=[]
	for task in tasks:
		task_array.append(task.task.title)



	task_enabler=TransactionEnabler.objects.filter(status="YES")
	task_enabler_array=[]
	for item in task_enabler:
		task_enabler_array.append(item.title)

	default_password="NO"
	if Staff.objects.filter(admin=request.user,default_password='YES'):
		default_password="YES"

	applicants=[]
	form=loan_request_order_form(request.POST or None)

	if request.method == 'POST':
		period_id=request.POST.get("period")
		period = Commodity_Period.objects.get(id=period_id)

		batch_id=request.POST.get('batch')
		batch=Commodity_Period_Batch.objects.get(id=batch_id)

		loan_id = request.POST.get('loans')
		loan = TransactionTypes.objects.get(id=loan_id)

		applicants = LoanRequest.objects.filter(loan=loan,period=period,batch=batch,approval_status='APPROVED',transaction_status='UNTREATED')
	context={
	'form':form,
	'applicants':applicants,
	'task_array':task_array,
	'task_enabler_array':task_enabler_array,
	'default_password':default_password,
	}
	return render(request,'deskofficer_templates/loan_request_approved_Issue_form_period_load.html',context)



def loan_request_approved_list_form_sales(request,pk):

	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	task_array=[]
	for task in tasks:
		task_array.append(task.task.title)



	task_enabler=TransactionEnabler.objects.filter(status="YES")
	task_enabler_array=[]
	for item in task_enabler:
		task_enabler_array.append(item.title)

	default_password="NO"
	if Staff.objects.filter(admin=request.user,default_password='YES'):
		default_password="YES"

	form = loan_request_approved_list_form_sales_form(request.POST or None)

	processed_by=CustomUser.objects.get(id=request.user.id)

	loan=LoanRequest.objects.get(id=pk)
	loan_amount=loan.approved_amount
	admin_charge=loan.admin_charge

	receipt_type = loan.loan.receipt_type

	tdate=get_current_date(now)


	form.fields['amount'].initial=admin_charge
	form.fields['loan_amount'].initial=loan_amount


	if request.method == "POST":



		if receipt_type == "MANUAL":
			receipt_no_id = request.POST.get('receipt')
			if Receipts.objects.filter(receipt=receipt_no_id).exists():
				receipt_obj = Receipts.objects.get(receipt=receipt_no_id)
				receipt=receipt_obj.receipt
			else:
				messages.error(request,'Receipt do not exist')
				return HttpResponseRedirect(reverse('loan_request_approved_list_form_sales',args=(pk,)))

		elif receipt_type == "AUTO":
			receipt_obj=AutoReceipt.objects.first()
			receipt='C-' + str(receipt_obj.receipt).zfill(5)
			receipt_obj.receipt=int(receipt_obj.receipt)+1
			receipt_obj.save()
		else:
			messages.error(request,'Receipt Format No Set')
			return HttpResponseRedirect(reverse('loan_request_approved_list_form_sales',args=(pk,)))

		record = LoanFormIssuance(processing_status='UNPROCESSED',
								tdate=tdate,
								applicant=loan,
								receipt=receipt,
								admin_charge=admin_charge,
								processed_by=processed_by.username,
								status='UNTREATED')
		record.save()


		loan.transaction_status='TREATED'
		loan.save()

		if receipt_type == "MANUAL":
			receipt_obj.status='USED'
			receipt_obj.save()

		return HttpResponseRedirect(reverse('loan_application_request_form_issuanace_confirmation',args=(receipt,)))


	context={

	'form':form,
	'loan':loan,
	'receipt_type':receipt_type,
	'task_array':task_array,
	'task_enabler_array':task_enabler_array,
	'default_password':default_password,
	}
	return render(request,'deskofficer_templates/loan_request_approved_list_form_sales.html',context)



def loan_application_request_form_issuanace_confirmation(request,pk):

	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	task_array=[]
	for task in tasks:
		task_array.append(task.task.title)



	task_enabler=TransactionEnabler.objects.filter(status="YES")
	task_enabler_array=[]
	for item in task_enabler:
		task_enabler_array.append(item.title)


	default_password="NO"
	if Staff.objects.filter(admin=request.user,default_password='YES'):
		default_password="YES"

	form=loan_request_order_form(request.POST or None)

	applicant = LoanFormIssuance.objects.get(receipt=pk)

	if request.method == 'POST':
		pass

	context={
	'form':form,
	# 'period':period,
	# 'batch':batch,
	# 'transaction':loan,
	'applicant':applicant,
	'task_array':task_array,
	'task_enabler_array':task_enabler_array,
	'default_password':default_password,
	}
	return render(request,'deskofficer_templates/loan_application_request_form_issuanace_confirmation.html',context)


def loan_application_approved_period_load(request):

	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	task_array=[]
	for task in tasks:
		task_array.append(task.task.title)



	task_enabler=TransactionEnabler.objects.filter(status="YES")
	task_enabler_array=[]
	for item in task_enabler:
		task_enabler_array.append(item.title)

	default_password="NO"
	if Staff.objects.filter(admin=request.user,default_password='YES'):
		default_password="YES"

	applicants=[]
	form=loan_request_order_form(request.POST or None)
	period=[]
	batch=[]
	transaction=[]
	loan=[]

	if request.method == 'POST':
		period_id=request.POST.get("period")
		period = Commodity_Period.objects.get(id=period_id)

		batch_id=request.POST.get('batch')
		batch=Commodity_Period_Batch.objects.get(id=batch_id)

		loan_id = request.POST.get('loans')
		loan = TransactionTypes.objects.get(id=loan_id)


		applicants = LoanFormIssuance.objects.filter(applicant__loan=loan,applicant__period=period,applicant__batch=batch,processing_status='UNPROCESSED',status='UNTREATED')
	context={
	'form':form,
	'period':period,
	'batch':batch,
	'transaction':loan,
	'applicants':applicants,
	'task_array':task_array,
	'task_enabler_array':task_enabler_array,
	'default_password':default_password,
	}
	return render(request,'deskofficer_templates/loan_application_approved_period_load.html',context)



def loan_application_form_processing(request,pk):
	form=loan_application_processing_form(request.POST or None)
	net_form=loan_request_document_attachment_form(request.POST or None)

	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	task_array=[]
	for task in tasks:
		task_array.append(task.task.title)


	default_password="NO"
	if Staff.objects.filter(admin=request.user,default_password='YES'):
		default_password="YES"

	task_enabler=TransactionEnabler.objects.filter(status="YES")
	task_enabler_array=[]
	for item in task_enabler:
		task_enabler_array.append(item.title)

	tdate = get_current_date(now)

	applicant=LoanFormIssuance.objects.get(id=pk)
	total_guarantors=applicant.applicant.loan.guarantors

	bank_accounts=MembersBankAccounts.objects.filter(member_id=applicant.applicant.member_id)

	processed_by = CustomUser.objects.get(id=request.user.id)

	loan_settings=LoanRequestSettings.objects.filter(applicant=applicant.applicant)

	seleected_guarantors=[]
	new_loan=[]
	new_amount=0
	loan_pk=0


	loan_based_saving=[]
	if LoanBasedSavings.objects.all().exists():
		loan_based_saving=LoanBasedSavings.objects.all().first()
		loan_based_code=loan_based_saving.savings.code


	if LoanApplication.objects.filter(applicant=applicant).exists():
		new_loan=LoanApplication.objects.get(applicant=applicant)

		new_amount=new_loan.loan_amount
		loan_pk=new_loan.pk

		seleected_guarantors=LoanApplicationGuarnators.objects.filter(applicant=new_loan)


	if  request.method =='POST' and 'application' in request.POST:
		exist_amount=applicant.applicant.approved_amount
		new_amount=request.POST.get('loan_new_amount')

		if float(new_amount)<=0:
			messages.error(request,'Invalid Loan Amount Specification')
			return HttpResponseRedirect(reverse('loan_application_form_processing', args=(pk,)))

		if float(exist_amount) < float(new_amount):
			messages.error(request,'You cannot apply for Amount beyond the already approved amount of ' + str(exist_amount))
			return HttpResponseRedirect(reverse('loan_application_form_processing', args=(pk,)))


		selected_trannsaction_rate=0
		saved_amount=0
		if applicant.applicant.loan.savings_rate == "YES":

			selected_trannsaction_rate=applicant.applicant.loan.saving_rating


			if selected_trannsaction_rate > 0:
				percentage_amount=(float(selected_trannsaction_rate)/100)*float(new_amount)

				loan_based_account_number=str(loan_based_code) + str(applicant.applicant.member.get_member_Id)

				saved_amount=0
				if PersonalLedger.objects.filter(account_number=loan_based_account_number).exists():
					ledger_balance=PersonalLedger.objects.filter(account_number=loan_based_account_number).last()
					saved_amount=ledger_balance.balance

				if not saved_amount:
					messages.error(request,'You do not have any savings for this Amount')
					return HttpResponseRedirect(reverse('loan_application_form_processing',args=(pk,)))

				if float(percentage_amount) > float(saved_amount):
					messages.error(request,'You do not have required savings for this Amount')
					return HttpResponseRedirect(reverse('loan_application_form_processing',args=(pk,)))



		desired_duration=request.POST.get("duration")

		if desired_duration and int(desired_duration)>0:
			if int(desired_duration) > int(applicant.applicant.duration):
				messages.error(request,'The Desired Duration cannot be greater than the Default')
				return HttpResponseRedirect(reverse('loan_application_form_processing', args=(pk,)))
			else:
				duration=desired_duration
		else:
			duration=int(applicant.applicant.duration)


		if LoanApplication.objects.filter(applicant=applicant).exists():
			record=LoanApplication.objects.get(applicant=applicant)
			record.loan_amount=new_amount
			record.save()
			return HttpResponseRedirect(reverse('loan_application_form_processing', args=(pk,)))

		record=LoanApplication(submission_status='PENDING',
								transaction_status='UNTREATED',
								approval_status='PENDING',
								duration=duration,
								tdate=tdate,applicant=applicant,
								loan_amount=new_amount,processed_by=processed_by.username)
		record.save()
		return HttpResponseRedirect(reverse('loan_application_form_processing', args=(pk,)))



	if request.method=='POST' and 'btn_account' in request.POST:
		account_id=request.POST.get('account')
		account=MembersBankAccounts.objects.get(id=account_id)

		record=LoanApplication.objects.get(applicant=applicant)
		record.bank_account=account
		record.save()
		messages.success(request,'Bank Account Details Added Successfully')
		return HttpResponseRedirect(reverse('loan_application_form_processing', args=(pk,)))


	if request.method=='POST' and 'btn_net_pay' in request.POST:
		payment_as_at=request.POST.get('payment_as_at')
		net_pay=request.POST.get('net_pay')

		if request.FILES.get('image', False):
			image = request.FILES['image']
			fs=FileSystemStorage()
			filename=fs.save(image.name,image)
			image_url=fs.url(filename)

		else:
			image_url=None

		if not payment_as_at:
			messages.error(request,'Description is Missing')
			return HttpResponseRedirect(reverse('loan_application_form_processing', args=(pk,)))


		if not net_pay or float(net_pay) <=0:
			messages.error(request,'Net Pay Missing')
			return HttpResponseRedirect(reverse('loan_application_form_processing', args=(pk,)))

		record=LoanApplication.objects.get(applicant=applicant)
		record.payment_as_at=payment_as_at
		record.net_pay=net_pay
		record.image=image_url
		record.save()



		record.applicant.applicant.member.last_used_net_pay=net_pay
		record.applicant.applicant.member.net_pay_as_at=payment_as_at
		record.applicant.applicant.member.save()

		messages.success(request,'Net Pay Added Successfully')
		return HttpResponseRedirect(reverse('loan_application_form_processing', args=(pk,)))


	form.fields['loan_type'].initial=applicant.applicant.loan.name
	form.fields['loan_amount'].initial=applicant.applicant.approved_amount
	form.fields['duration'].initial=applicant.applicant.duration

	form.fields['loan_new_amount'].initial=applicant.applicant.approved_amount
	net_form.fields['net_pay'].initial=applicant.applicant.member.last_used_net_pay
	net_form.fields['payment_as_at'].initial=applicant.applicant.member.net_pay_as_at
	image_link=[]
	new_loan_pk=0
	if new_loan:
		image_link=new_loan.image
		new_loan_pk=new_loan.pk

	if LoanApplication.objects.filter(applicant=applicant).exists():
		form.fields['loan_new_amount'].initial=new_amount

	context={
	'form':form,
	'image_link':image_link,
	'net_form':net_form,
	'applicant':applicant,
	'loan_settings':loan_settings,
	'loan_pk':loan_pk,
	'new_amount':new_amount,
	'new_loan':new_loan,
	'new_loan_pk':new_loan_pk,
	'bank_accounts':bank_accounts,
	'seleected_guarantors':seleected_guarantors,
	'task_array':task_array,
	'task_enabler_array':task_enabler_array,
	'default_password':default_password,
	'return_pk':pk,
	}
	return render(request,'deskofficer_templates/loan_application_form_processing.html',context)



def loan_application_form_processing_guarantor_search(request,pk):
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	task_array=[]
	for task in tasks:
		task_array.append(task.task.title)



	task_enabler=TransactionEnabler.objects.filter(status="YES")
	task_enabler_array=[]
	for item in task_enabler:
		task_enabler_array.append(item.title)

	default_password="NO"
	if Staff.objects.filter(admin=request.user,default_password='YES'):
		default_password="YES"

	title="Search Membership (Only Cooperative or IPPIS No is Allowed"
	form = searchForm(request.POST or None)
	record=LoanApplication.objects.get(id=pk)
	return_pk=record.applicant_id
	return render(request,'deskofficer_templates/loan_application_form_processing_guarantor_search.html',{'task_array':task_array,
	'task_enabler_array':task_enabler_array,
	'default_password':default_password,'form':form,'title':title,'pk':pk,'return_pk':return_pk,})


def loan_application_form_processing_guarantor_add_list_load(request,pk):
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	task_array=[]
	for task in tasks:
		task_array.append(task.task.title)



	task_enabler=TransactionEnabler.objects.filter(status="YES")
	task_enabler_array=[]
	for item in task_enabler:
		task_enabler_array.append(item.title)

	default_password="NO"
	if Staff.objects.filter(admin=request.user,default_password='YES'):
		default_password="YES"

	title="Commodity Loan"
	form = searchForm(request.POST)
	record=LoanApplication.objects.get(id=pk)
	member=Members.objects.get(id=record.applicant.applicant.member_id)
	member_id=Members.objects.get(id=record.applicant.applicant.member_id)

	members=[]
	if request.method == "POST":
		if request.POST.get("title")=="":
			return HttpResponseRedirect(reverse('membership_commodity_loan_search'))

		members=searchGuarantorMembers(form['title'].value(),'ACTIVE',member)

	context={
	'members':members,
	'title':title,
	'task_array':task_array,
	'task_enabler_array':task_enabler_array,
	'default_password':default_password,
	'pk':pk,
	}
	return render(request,'deskofficer_templates/loan_application_form_processing_guarantor_add_list_load.html',context)




def loan_application_form_processing_guarantor_add(request,pk,loan_pk):
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	task_array=[]
	for task in tasks:
		task_array.append(task.task.title)



	task_enabler=TransactionEnabler.objects.filter(status="YES")
	task_enabler_array=[]
	for item in task_enabler:
		task_enabler_array.append(item.title)

	default_password="NO"
	if Staff.objects.filter(admin=request.user,default_password='YES'):
		default_password="YES"

	guarantor=Members.objects.get(id=pk)
	applicant=LoanApplication.objects.get(id=loan_pk)
	total_guarantors=applicant.applicant.applicant.loan.guarantors

	if LoanApplicationGuarnators.objects.filter(applicant=applicant).count() >= total_guarantors:
		messages.info(request,'You Have added the required Guarantors')
		return HttpResponseRedirect(reverse('loan_application_form_processing_guarantor_search',args=(loan_pk,)))

	if LoanApplicationGuarnators.objects.filter(applicant=applicant,guarantor=guarantor).exists():
		messages.info(request,'This Member is already Added as guarantor to this Applicant')
		return HttpResponseRedirect(reverse('loan_application_form_processing_guarantor_search',args=(loan_pk,)))

	LoanApplicationGuarnators(applicant=applicant,guarantor=guarantor,status='UNTREATED').save()
	return HttpResponseRedirect(reverse('loan_application_form_processing_guarantor_search',args=(loan_pk,)))


def loan_application_form_processing_guarantor_delete(request,pk,return_pk):
	LoanApplicationGuarnators.objects.get(id=pk).delete()
	return HttpResponseRedirect(reverse('loan_application_form_processing',args=(return_pk,)))


def loan_application_form_processing_bank_account_delete(request,pk,return_pk):
	LoanApplication.objects.filter(id=pk).update(bank_account=None)
	return HttpResponseRedirect(reverse('loan_application_form_processing',args=(return_pk,)))




def loan_application_preview(request,pk, return_pk):
	form=MemberShipRequestAdditionalInfo_form(request.POST or None)

	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	task_array=[]
	for task in tasks:
		task_array.append(task.task.title)

	task_enabler=TransactionEnabler.objects.filter(status="YES")
	task_enabler_array=[]
	for item in task_enabler:
		task_enabler_array.append(item.title)

	default_password="NO"
	if Staff.objects.filter(admin=request.user,default_password='YES'):
		default_password="YES"

	applicant=LoanApplication.objects.get(id=pk)

	nok_list=[]
	if MembersNextOfKins.objects.filter(member=applicant.applicant.applicant.member).exists():
		nok_record = MembersNextOfKins.objects.filter(member=applicant.applicant.applicant.member).first()
		nok_list.append(nok_record.name)
		nok_list.append(nok_record.relationships.title)
		nok_list.append(nok_record.address)
		nok_list.append(nok_record.phone_number)

		applicant.nok_name=nok_record.name
		applicant.nok_Relationship=nok_record.relationships.title
		applicant.nok_address=nok_record.address
		applicant.nok_phone_no=nok_record.phone_number
		applicant.save()
	else:
		messages.error(request,'There is no registered Next of Kin for this Member')
		return HttpResponseRedirect(reverse('loan_application_form_processing',args=(return_pk,)))

	net_pay=applicant.net_pay

	if not net_pay and float(net_pay)<=0:
		messages.error(request,'Please add Net Pay')
		return HttpResponseRedirect(reverse('loan_application_form_processing',args=(return_pk,)))


	status = 'UNTREATED'

	apex_loan=TransactionSources.objects.get(title='LOAN')
	maximum_loan = apex_loan.maximum_amount

	loan_type=applicant.applicant.applicant.loan.name
	loan_amount=applicant.loan_amount
	duration = applicant.duration


	admin_charges_minimum = applicant.applicant.applicant.loan.admin_charges_minimum

	if float(admin_charges_minimum) >= float(loan_amount):
		admin_charge=applicant.applicant.applicant.loan.default_admin_charges
	else:
		if applicant.applicant.applicant.loan.admin_charges_rating == "PERCENTAGE":
			admin_charge=(float(applicant.applicant.applicant.loan.admin_charges) / 100) * float(loan_amount)
		else:
			admin_charge=applicant.applicant.applicant.loan.admin_charges

	membership_waver=False
	savings_made_waver=False
	multiple_loans_waver=False
	salary_status_waver=False
	standing_order_status =False

	if MembersExclusiveness.objects.filter(transaction=applicant.applicant.applicant.loan,period=applicant.applicant.applicant.period,batch=applicant.applicant.applicant.batch,processing_status='UNPROCESSED',approval_status='APPROVED').exists():
		wavers=MembersExclusiveness.objects.filter(transaction=applicant.applicant.applicant.loan,period=applicant.applicant.applicant.period,batch=applicant.applicant.applicant.batch,processing_status='UNPROCESSED',approval_status='APPROVED')

		for item in wavers:
			if item.task.title == 'MEMBERSHIP AGE':
				membership_waver=True
			elif item.task.title == 'SAVINGS MADE':
				savings_made_waver=True
			elif item.task.title == 'SALARY STATUS':
				salary_status_waver=True


	bank_account=LoanApplication.objects.exclude(Q(bank_account__isnull=True)).filter(id=pk)
	if bank_account:
		bank_account_status=True
	else:
		bank_account_status=False
		messages.error(request,'Bank Details missing')
		return HttpResponseRedirect(reverse('loan_application_form_processing',args=(return_pk,)))

	guarantor_list=[]
	try:
		guarantors=LoanApplicationGuarnators.objects.filter(applicant=applicant)
		for guarantor in guarantors:
			small_guarantor=(guarantor.id,guarantor.guarantor.admin.first_name + " " + guarantor.guarantor.admin.last_name + " " + guarantor.guarantor.middle_name)
			guarantor_list.append(small_guarantor[1])
	except:
		guarantor_list=[]
	# for i in range(len(guarantor_list)):
	# 	print(guarantor_list[i])

	total_guarantors=applicant.applicant.applicant.loan.guarantors

	if int(guarantors.count())==int(total_guarantors):
		guarnator_status=True
	else:
		guarnator_status=False
		messages.error(request,'Guarantors missing')
		return HttpResponseRedirect(reverse('loan_application_form_processing',args=(return_pk,)))

	loan_savings_status=False
	loan_based_saving=[]
	savings_saved=0
	loan_saving_relationship=[]

	if applicant.applicant.applicant.loan.savings_rate == 'YES':
		if LoanBasedSavings.objects.all().exists():
			loan_based_saving = LoanBasedSavings.objects.first()
		else:
			messages.error(request,'Loan Based Savings not Set')
			return HttpResponseRedirect(reverse('loan_application_form_processing',args=(return_pk,)))

		loans_anchored=TransactionTypes.objects.filter(savings_rate='YES')

		loans_anchored_sum=LoansRepaymentBase.objects.filter(transaction__savings_rate='YES').filter(Q(balance__lt=0) & Q(member_id=applicant.applicant.applicant.member_id)).aggregate(total_amount=Sum('balance'))
		total_loans_anchored=loans_anchored_sum['total_amount']
		if not total_loans_anchored:
			total_loans_anchored=0

		expected_total_loans=abs(float(total_loans_anchored)) + float(loan_amount)


		savings_saved=0

		if StandingOrderAccounts.objects.filter(transaction__transaction=loan_based_saving.savings,transaction__member=applicant.applicant.applicant.member).exists():
			account_id=StandingOrderAccounts.objects.get(transaction__transaction=loan_based_saving.savings,transaction__member=applicant.applicant.applicant.member)

			if PersonalLedger.objects.filter(account_number=account_id.transaction.account_number).exists():
				savings_ledger=PersonalLedger.objects.filter(account_number=account_id.transaction.account_number).last()
				savings_saved=savings_ledger.balance
			else:
				messages.error(request,'No Savings Available for Loan Based Savings')
				return HttpResponseRedirect(reverse('loan_application_form_processing',args=(return_pk,)))
		else:
			messages.error(request,'No account for Loan Based Savings')
			return HttpResponseRedirect(reverse('loan_application_form_processing',args=(return_pk,)))

		loan_based_saving_rating=apex_loan.loan_based_saving

		if not float(loan_based_saving_rating):
			messages.error(request,'Loan Based Saving Rating not set')
			return HttpResponseRedirect(reverse('loan_application_form_processing',args=(return_pk,)))


		loan_saving_relationship=float(int(loan_based_saving_rating)/100) * float(expected_total_loans)
		if savings_made_waver:
			loan_savings_status=True
		else:

			if float(savings_saved) >= float(loan_saving_relationship):
				loan_savings_status=True

		if not loan_savings_status:

			messages.error(request,'You do not Have Expected Savings for this Loan Amount, You have  ' + str(savings_saved) + ' while you need ' + str(loan_saving_relationship) )
			return HttpResponseRedirect(reverse('loan_application_form_processing',args=(return_pk,)))


	total_savings=0
	savings_sum=get_standing_orders_sum(applicant.applicant.applicant.member_id)
	if savings_sum==None:
		total_savings=0
		standing_order_status=False
	else:
		total_savings=savings_sum
		standing_order_status=True

	total_loans=0
	balance_total=0
	loans_sum=LoansRepaymentBase.objects.filter(Q(balance__lt=0) & Q(member_id=applicant.applicant.applicant.member_id)).aggregate(total_amount=Sum('repayment'),total_balance=Sum('balance'))
	total_loans=loans_sum['total_amount']
	balance_total= loans_sum['total_balance']
	if total_loans==None:
		total_loans=0
	if balance_total == None:
		balance_total=0

	shop_balance=0
	shops =CooperativeShopLedger.objects.filter(Q(balance__lt=0) & Q(member_id=applicant.applicant.applicant.member_id)).order_by('-id').first()
	if shops:
		shop_balance=abs(shops.balance)


	total_debit=float(total_savings)+float(total_loans)+float(shop_balance)


	balance=float(net_pay)-total_debit

	date_joined = applicant.applicant.applicant.member.date_joined
	now = datetime.datetime.now()

	salary_loan_relationship = apex_loan.salary_loan_relationship
	if not float(salary_loan_relationship):
		messages.error(request,'Salary Loan Relationship not set')
		return HttpResponseRedirect(reverse('loan_application_form_processing',args=(return_pk,)))


	salary_loan_relationship_computed= float(int(salary_loan_relationship)/100) * float(balance)

	interest_rate = applicant.applicant.applicant.loan.interest_rate

	if not float(interest_rate):
		messages.error(request,'Interest Rate not set')
		return HttpResponseRedirect(reverse('loan_application_form_processing',args=(return_pk,)))


	interest= float(int(interest_rate)/100) * float(applicant.loan_amount)

	loan_age = applicant.applicant.applicant.loan.loan_age
	if not float(loan_age):
		messages.error(request,'Members Loan Age not set')
		return HttpResponseRedirect(reverse('loan_application_form_processing',args=(return_pk,)))


	members_age = (now.year - date_joined.year) * 12 + (now.month - date_joined.month)
	interest_deduction=applicant.applicant.applicant.loan.interest_deduction
	if not interest_deduction:
		messages.error(request,'Interest deduction source not set')
		return HttpResponseRedirect(reverse('loan_application_form_processing',args=(return_pk,)))



	if interest_deduction == "SOURCE":
		amount_scheduled = float(loan_amount)
	else:
		amount_scheduled = float(loan_amount)+ float(interest)

	if int(duration) == 0:
		messages.error(request,'Please set the Loan Duration')
		return HttpResponseRedirect(reverse('loan_application_form_processing',args=(return_pk,)))

	monthly_repayment=math.ceil(float(amount_scheduled)/float(duration))

	salary_status=True
	if salary_status_waver:
		salary_status=False
	else:
		if float(monthly_repayment)> float(salary_loan_relationship_computed):
			salary_status=False

	Member_Status = False
	if membership_waver:
		Member_Status = True
	else:
		if int(members_age)>int(loan_age):
			Member_Status = True



	record_array=[]

	if request.method=="POST":
		comment=request.POST.get("comment")
		applicant.comment=comment
		applicant.submission_status='SUBMITTED'
		applicant.admin_charge=admin_charge
		applicant.save()

		description="NET PAY"
		value=net_pay
		category='ANALYSIS'
		waver=0
		tag=0
		Loan_Application_Posting(applicant,description,value,category,'UNTREATED',tag,waver)


		description="SALARY BALANCE AFTER DEDUCTIONS"
		value=balance
		category='ANALYSIS'
		waver=0
		tag=0
		Loan_Application_Posting(applicant,description,value,category,'UNTREATED',tag,waver)

		description=loan_type
		value=loan_amount
		category='ANALYSIS'
		waver=0
		tag=0
		Loan_Application_Posting(applicant,description,value,category,'UNTREATED',tag,waver)

		description="MONTHLY DEDUCTIONS"
		value=total_savings
		category='ANALYSIS'
		waver=0
		tag=0
		Loan_Application_Posting(applicant,description,value,category,'UNTREATED',tag,waver)

		description="OUTSTANDING MONTHLY LOAN REPAYMENTS"
		value='{0:.2f}'.format(total_loans)
		category='ANALYSIS'
		waver=0
		tag=0
		Loan_Application_Posting(applicant,description,value,category,'UNTREATED',tag,waver)

		description="COOPERATIVE SHOP"
		value=shop_balance
		category='ANALYSIS'
		waver=0
		tag=0
		Loan_Application_Posting(applicant,description,value,category,'UNTREATED',tag,waver)

		description="LOAN DURATION"
		value=str(duration) + " MONTHS"
		category='ANALYSIS'
		waver=0
		tag=0
		Loan_Application_Posting(applicant,description,value,category,'UNTREATED',tag,waver)


		description="SALARY LOAN RELATIONSHIP"
		value=str(salary_loan_relationship) + "%"
		category='ANALYSIS'
		waver=0
		tag=0
		Loan_Application_Posting(applicant,description,value,category,'UNTREATED',tag,waver)


		description="SALARY LOAN RELATIONSHIP COMPUTED"
		value=salary_loan_relationship_computed
		category='ANALYSIS'
		waver=0
		tag=0
		Loan_Application_Posting(applicant,description,value,category,'UNTREATED',tag,waver)

		description="MATURITY AGE"
		value=str(loan_age) + " MONTHS"
		category='ANALYSIS'
		waver=0
		tag=0
		Loan_Application_Posting(applicant,description,value,category,'UNTREATED',tag,waver)


		description="DATE JOINED"
		value=date_joined
		category='ANALYSIS'
		waver=0
		tag=0
		Loan_Application_Posting(applicant,description,value,category,'UNTREATED',tag,waver)

		description="MEMBER AGE"
		value=str(members_age) + "MONTH(S)"
		category='ANALYSIS'
		waver=0
		tag=0
		Loan_Application_Posting(applicant,description,value,category,'UNTREATED',tag,waver)

		description="LOAN INTEREST RATE"
		value=str(interest_rate) + "%"
		category='ANALYSIS'
		waver=0
		tag=0
		Loan_Application_Posting(applicant,description,value,category,'UNTREATED',tag,waver)


		description="INTEREST DEDUCTION"
		value=interest_deduction
		category='ANALYSIS'
		waver=0
		tag=0
		Loan_Application_Posting(applicant,description,value,category,'UNTREATED',tag,waver)


		description="LOAN INTEREST"
		value=interest
		category='ANALYSIS'
		waver=0
		tag=0
		Loan_Application_Posting(applicant,description,value,category,'UNTREATED',tag,waver)

		description="AMOUNT SCHEDULED"
		value=amount_scheduled
		category='ANALYSIS'
		waver=0
		tag=0
		Loan_Application_Posting(applicant,description,value,category,'UNTREATED',tag,waver)


		description="MONTHLY REPAYMENT"
		value=round(float(monthly_repayment),2)
		category='ANALYSIS'
		waver=0
		tag=0
		Loan_Application_Posting(applicant,description,value,category,'UNTREATED',tag,waver)

		if savings_saved:
			description="LOAN BASED SAVINGS"
			value=loan_based_saving.savings.name
			category='ANALYSIS'
			waver=0
			tag=0
			Loan_Application_Posting(applicant,description,value,category,'UNTREATED',tag,waver)

			description="SAVED AMOUNT"
			value=savings_saved
			category='ANALYSIS'
			waver=0
			tag=0
			Loan_Application_Posting(applicant,description,value,category,'UNTREATED',tag,waver)

			description="LOAN BASED SAVINGS RATE"
			value=str(loan_based_saving_rating) + "%"
			category='ANALYSIS'
			waver=0
			tag=0
			Loan_Application_Posting(applicant,description,value,category,'UNTREATED',tag,waver)

		description="GUARANTORS"
		value=guarantor_list
		category='ANALYSIS'
		waver=0
		tag=0
		Loan_Application_Posting(applicant,description,value,category,'UNTREATED',tag,waver)


		description="NEXT OF KIN"
		value=nok_list
		category='ANALYSIS'
		waver=0
		tag=0
		Loan_Application_Posting(applicant,description,value,category,'UNTREATED',tag,waver)



		description="BANK DETAILS"
		value=applicant.bank_account.account_name + " - " + applicant.bank_account.account_number + ' - ' + applicant.bank_account.bank.title
		category='ANALYSIS'
		waver=0
		tag=0
		Loan_Application_Posting(applicant,description,value,category,'UNTREATED',tag,waver)

		description="ADMIN CHARGES"
		value=admin_charge
		waver=0
		tag=0
		category='ANALYSIS'
		Loan_Application_Posting(applicant,description,value,category,'UNTREATED',tag,waver)

		description="MEMBER STATUS"
		value=Member_Status
		waver=membership_waver
		tag=0
		if value:
			tag=1
		category='ANALYSIS'
		Loan_Application_Posting(applicant,description,value,category,'UNTREATED',tag,waver)

		description="SALARY STATUS"
		value=salary_status
		waver=salary_status_waver
		tag=0
		if value:
			tag=1
		category='SUMMARY'
		Loan_Application_Posting(applicant,description,value,category,'UNTREATED',tag,waver)

		if savings_saved:
			description="LOAN SAVINGS BASED STATUS"
			value=loan_savings_status
			waver=savings_made_waver
			tag=0
			if value:
				tag=1
			category='SUMMARY'
			Loan_Application_Posting(applicant,description,value,category,'UNTREATED',tag,waver)


		description="Bank Account Status"
		value=bank_account_status
		waver=0
		tag=0
		if value:
			tag=1
		category='SUMMARY'
		Loan_Application_Posting(applicant,description,value,category,'UNTREATED',tag,waver)

		description="Guarantors Status"
		value=guarnator_status
		waver=0
		tag=0
		if value:
			tag=1
		category='SUMMARY'
		Loan_Application_Posting(applicant,description,value,category,'UNTREATED',tag,waver)



		applicant1=LoanFormIssuance.objects.get(id=applicant.applicant_id)
		applicant1.processing_status='PROCESSED'
		applicant1.save()


		return HttpResponseRedirect(reverse('loan_application_approved_period_load'))

	compulsory_saving_status = False
	if CompulsorySavings.objects.all().exists():
		compulsory_saving = CompulsorySavings.objects.first()

		if StandingOrderAccounts.objects.filter(transaction__member=applicant.applicant.applicant.member,transaction__transaction=compulsory_saving.transaction).exists():
			compulsory_saving_status = True

	maximum_loan_status = False
	compound_loan =float(abs(balance_total)) + float(applicant.loan_amount)

	if float(compound_loan)<= float(maximum_loan):
		maximum_loan_status =True



	if maximum_loan_status and guarnator_status and bank_account_status and compulsory_saving_status and standing_order_status:

		if membership_waver:
			button_enabled=True
		else:
			button_enabled=False
			if Member_Status == True:
				button_enabled=True

		if savings_made_waver:
			button_enabled=True
		else:
			button_enabled=False
			if loan_savings_status == True:
				button_enabled=True

		if salary_status_waver:
			button_enabled=True
		else:
			button_enabled=False
			if salary_status == True:
				button_enabled=True
	else:
		button_enabled=False

	record_array.append(("Net Pay",net_pay))
	record_array.append(("Salary Balance After Deductions",balance))
	record_array.append((loan_type,loan_amount))
	record_array.append(('Monthly Contributions',total_savings))
	record_array.append(('Loan Monthly Repayment',total_loans))
	record_array.append(('Cooperative Shop',shop_balance))
	record_array.append(('Loan Duration',str(duration) + " Months"))
	record_array.append(('Salary Loan Relationshipp',salary_loan_relationship))
	record_array.append(('Salary Loan Relationship Computed',salary_loan_relationship_computed))
	record_array.append(('Maturity Age',str(loan_age)[:-3] + " Months"))
	record_array.append(('Date Joined',date_joined))
	record_array.append(('Members Age',str(members_age) + " Months"))
	record_array.append(('Loan Interest Rate',str(interest_rate) + "%"))
	record_array.append(('Interest Deduction',interest_deduction))
	record_array.append(('Loan Interest','=N=' +str(interest)))
	record_array.append(('Amount Scheduled','=N=' +str(amount_scheduled)))
	record_array.append(('Monthly Repayment',"=N=" + str(monthly_repayment)))
	record_array.append(('Admin Charges',"=N=" + str(admin_charge)))

	if savings_saved:
		record_array.append(('Loan Based Savings',loan_based_saving.savings.name))
		record_array.append(('Saved Amount (' + str(loan_based_saving.savings.name) +")",savings_saved))
		record_array.append(('Loan Based Savings Rate',str(loan_based_saving_rating) + "%"))

	record_array.append(('Guarantors',guarantor_list))

	record_array.append(('Bank Details',applicant.bank_account.account_name + " - " + str(applicant.bank_account.account_number) + ' - ' +  applicant.bank_account.bank.title))
	record_array.append(('Next of Kin',f'{nok_list[0]}, {nok_list[1]}, {nok_list[2]}'))

	form.fields['comment'].initial="FOR YOUR CONSIDERATION"
	context={
	'form':form,
	'savings_anchored':applicant.applicant.applicant.loan.savings_rate,
	'record_array':record_array,
	'membership_waver':membership_waver,
	'pk':pk,
	'salary_status':salary_status,
	'Member_Status':Member_Status,
	'loan_savings_status':loan_savings_status,
	'button_enabled':button_enabled,
	'guarnator_status':guarnator_status,
	'bank_account_status':bank_account_status,
	'task_array':task_array,
	'task_enabler_array':task_enabler_array,
	'default_password':default_password,
	}

	return render(request,'deskofficer_templates/loan_application_preview.html',context)


def Loan_application_processing_period_load(request):
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	task_array=[]
	for task in tasks:
		task_array.append(task.task.title)



	task_enabler=TransactionEnabler.objects.filter(status="YES")
	task_enabler_array=[]
	for item in task_enabler:
		task_enabler_array.append(item.title)


	default_password="NO"
	if Staff.objects.filter(admin=request.user,default_password='YES'):
		default_password="YES"

	form=loan_request_order_form(request.POST or None)

	exist_loans=[]
	if request.method == 'POST':

		period_id=request.POST.get("period")
		period = Commodity_Period.objects.get(id=period_id)

		batch_id=request.POST.get('batch')
		batch=Commodity_Period_Batch.objects.get(id=batch_id)

		loan_id = request.POST.get('loans')
		loan = TransactionTypes.objects.get(id=loan_id)

		exist_loans = LoanApplication.objects.filter(applicant__applicant__loan=loan,applicant__applicant__period=period,applicant__applicant__batch=batch,transaction_status='UNTREATED',submission_status='SUBMITTED',applicant__processing_status='PROCESSED',approval_status='APPROVED')

	context={
	'exist_loans':exist_loans,
	'form':form,
	'task_array':task_array,
	'task_enabler_array':task_enabler_array,
	'default_password':default_password,
	}
	return render(request,'deskofficer_templates/Loan_application_processing_period_load.html',context)


def Loan_processing_scheduling_dashboard(request):
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	task_array=[]
	for task in tasks:
		task_array.append(task.task.title)



	task_enabler=TransactionEnabler.objects.filter(status="YES")
	task_enabler_array=[]
	for item in task_enabler:
		task_enabler_array.append(item.title)

	default_password="NO"
	if Staff.objects.filter(admin=request.user,default_password='YES'):
		default_password="YES"


	context={
	'task_array':task_array,
	'task_enabler_array':task_enabler_array,
	'default_password':default_password,
	}
	return render(request,'deskofficer_templates/Loan_processing_scheduling_dashboard.html',context)


def Loan_processing_scheduling_all_unscheduled(request):
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	task_array=[]
	for task in tasks:
		task_array.append(task.task.title)



	task_enabler=TransactionEnabler.objects.filter(status="YES")
	task_enabler_array=[]
	for item in task_enabler:
		task_enabler_array.append(item.title)


	default_password="NO"
	if Staff.objects.filter(admin=request.user,default_password='YES'):
		default_password="YES"

	records=LoansRepaymentBase.objects.filter(status='ACTIVE',schedule_status='UNSCHEDULED')
	context={
	'task_array':task_array,
	'task_enabler_array':task_enabler_array,
	'default_password':default_password,
	'records':records,
	}
	return render(request,'deskofficer_templates/Loan_processing_scheduling_all_unscheduled.html',context)

def Loan_processing_scheduling_all_unscheduled_processed(request,pk):

	LoansRepaymentBase.objects.filter(id=pk).update(schedule_status='SCHEDULED')
	return HttpResponseRedirect(reverse('Loan_processing_scheduling_all_unscheduled'))


def Loan_processing_scheduling_based_on_date(request):
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	task_array=[]
	for task in tasks:
		task_array.append(task.task.title)



	task_enabler=TransactionEnabler.objects.filter(status="YES")
	task_enabler_array=[]
	for item in task_enabler:
		task_enabler_array.append(item.title)

	default_password="NO"
	if Staff.objects.filter(admin=request.user,default_password='YES'):
		default_password="YES"

	form=PersonalLedger_Transaction_Account_Load_form(request.POST or None)

	records=[]
	if request.method == 'POST':
		start_date=request.POST.get('start_date')
		stop_date=request.POST.get('stop_date')



		date_format = '%Y-%m-%d'
		tdate1 = datetime.datetime.strptime(start_date, date_format)
		tdate2 = datetime.datetime.strptime(stop_date, date_format)

		records=LoansRepaymentBase.objects.filter(start_date__range=[tdate1,tdate2],status='ACTIVE',schedule_status='UNSCHEDULED')

	form.fields['start_date'].initial=get_current_date(now)
	form.fields['stop_date'].initial=get_current_date(now)
	context={
	'task_array':task_array,
	'task_enabler_array':task_enabler_array,
	'default_password':default_password,
	'form':form,
	'records':records,
	}
	return render(request,'deskofficer_templates/Loan_processing_scheduling_based_on_date.html',context)


def Loan_processing_scheduling_based_on_date_processed(request,pk):
	LoansRepaymentBase.objects.filter(id=pk).update(schedule_status='SCHEDULED')
	return HttpResponseRedirect(reverse('Loan_processing_scheduling_based_on_date'))




def loan_application_approved_process_preview(request,pk):

	now = datetime.datetime.now()
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	task_array=[]
	for task in tasks:
		task_array.append(task.task.title)

	task_enabler=TransactionEnabler.objects.filter(status="YES")
	task_enabler_array=[]
	for item in task_enabler:
		task_enabler_array.append(item.title)


	default_password="NO"
	if Staff.objects.filter(admin=request.user,default_password='YES'):
		default_password="YES"

	form=loan_application_approved_process_preview_form(request.POST or None)
	transaction_period=TransactionPeriods.objects.get(status='ACTIVE')


	processed_by=CustomUser.objects.get(id=request.user.id)
	tdate=get_current_date(now)
	applicant=LoanApplication.objects.get(id=pk)

	nok_name = applicant.nok_name
	nok_Relationship=applicant.nok_Relationship
	nok_phone_no=applicant.nok_phone_no
	nok_address=applicant.nok_address

	guarantors = LoanApplicationGuarnators.objects.filter(applicant=applicant)

	records=LoanApplicationSettings.objects.filter(applicant=applicant)

	loan_type=applicant.applicant.applicant.loan.name

	loan_amount=applicant.approved_amount
	duration = applicant.duration
	admin_charge = applicant.admin_charge
	start_date=[]
	stop_date=[]

	interest_rate = applicant.applicant.applicant.loan.interest_rate
	interest= float(int(interest_rate)/100) * float(applicant.loan_amount)
	interest_deduction=applicant.applicant.applicant.loan.interest_deduction

	if interest_deduction== "SOURCE":
		amount_scheduled = float(loan_amount)
	else:
		amount_scheduled = float(loan_amount)+ float(interest)

	monthly_repayment=math.ceil(float(amount_scheduled)/float(duration))

	my_id=applicant.applicant.applicant.member.get_member_Id
	loan_code=applicant.applicant.applicant.loan.code

	button_show = False

	if request.method=="POST" and 'btn-fetch' in request.POST:
		# effective_date_add=request.POST.get('effective_date_add')
		# if effective_date_add:
		start_date=request.POST.get('effective_date')
		start_date=datetime.datetime.strptime(start_date, '%Y-%m-%d')
		stop_date = start_date+ relativedelta(months=int(duration))
		start_date=get_current_date(start_date)
		stop_date=get_current_date(stop_date)
		button_show=True
		# 	# form.fields['effective_date_add'].initial=True
		# else:
		# 	messages.error(request,"Please Accept the Effective Date")
		# 	return HttpResponseRedirect(reverse('loan_application_approved_process_preview',args=(pk,)))



	if request.method=="POST" and 'btn-process' in request.POST:
		loan_number = generate_number(loan_code,my_id,now)
		if loan_number==0:
			messages.error(request,'Please set the loan Code')
			return HttpResponseRedirect(reverse('loan_application_approved_process_preview',args=(pk,)))

		form_print=request.POST.get('status')
		member=applicant.applicant.applicant.member
		effective_date_add=request.POST.get('effective_date_add')

		if effective_date_add:
			start_date=request.POST.get('effective_date')
			start_date=datetime.datetime.strptime(start_date, '%Y-%m-%d')
			stop_date = start_date+ relativedelta(months=int(duration))
			start_date=get_current_date(start_date)
			stop_date=get_current_date(stop_date)
		else:
			messages.error(request,"Please Accept the Effective Date")
			return HttpResponseRedirect(reverse('loan_application_approved_process_preview',args=(pk,)))

		transaction=applicant.applicant.applicant.loan

		if not nok_name:
			messages.error(request,"No Next of Kin recorded for this Member")
			return HttpResponseRedirect(reverse('loan_application_approved_process_preview',args=(pk,)))

		particulars=transaction.name + " Loan Issuance"
		s = titlecase(particulars)
		particulars=s
		debit=abs(float(loan_amount)) #+float(interest))
		credit=0
		balance=-debit

		post_to_ledger(member,
						transaction,
						loan_number,
						particulars,
						debit,
						credit,
						balance,
						get_current_date(now),
						'ACTIVE',
						tdate)


		ledger_balance=balance

		cash_book_balance=main_cashbook_balance()

		ledger_particulars= particulars + '(' + str(loan_number) + ')'
		debit=0
		credit=abs(float(loan_amount))
		balance=float(cash_book_balance)+float(credit)
		ref_no=get_ticket()
		status='ACTIVE'
		tdate=get_current_date(now)
		source='LOAN ISSUEANCE'
		main_cashbook_posting(ledger_particulars,debit,credit,balance,ref_no,status,tdate,processed_by,source)



		particulars=  "Interest on"  + transaction.name.title()
		s = titlecase(particulars)
		particulars=s
		debit=abs(float(interest))
		credit=0
		balance=-(abs(float(ledger_balance)) + abs(float(interest)))

		post_to_ledger(member,
						transaction,
						loan_number,
						particulars,
						debit,
						credit,
						balance,
						get_current_date(now),
						'ACTIVE',
						tdate)

		ledger_balance=balance

		cash_book_balance=main_cashbook_balance()

		ledger_particulars= particulars + '(' + str(loan_number) + ')'
		credit=0
		debit=abs(float(debit))
		balance=float(cash_book_balance)-float(debit)
		ref_no=get_ticket()
		status='ACTIVE'
		tdate=get_current_date(now)
		source='LOAN ISSUEANCE'
		main_cashbook_posting(ledger_particulars,debit,credit,balance,ref_no,status,tdate,processed_by,source)




		particulars=  "Admin Charges on :  "  + transaction.name.title()
		s = titlecase(particulars)
		particulars=s
		debit=abs(float(admin_charge))
		credit=0
		balance=-(abs(float(ledger_balance)) + abs(float(admin_charge)))

		post_to_ledger(member,
						transaction,
						loan_number,
						particulars,
						debit,
						credit,
						balance,
						get_current_date(now),
						'ACTIVE',
						tdate)

		ledger_balance=balance

		cash_book_balance=main_cashbook_balance()

		ledger_particulars= particulars + '(' + str(loan_number) + ')'
		credit=abs(float(admin_charge))
		debit=0
		balance=float(cash_book_balance)+float(credit)
		ref_no=get_ticket()
		status='ACTIVE'
		tdate=get_current_date(now)
		source='LOAN ISSUEANCE'
		main_cashbook_posting(ledger_particulars,debit,credit,balance,ref_no,status,tdate,processed_by,source)


		particulars=  "Deduction of Admin Charges from Source 0n:  "  + transaction.name.title()
		s = titlecase(particulars)
		particulars=s
		debit=0
		credit=abs(float(admin_charge))
		balance=(float(ledger_balance) + abs(float(admin_charge)))

		post_to_ledger(member,
						transaction,
						loan_number,
						particulars,
						debit,
						credit,
						balance,
						get_current_date(now),
						'ACTIVE',
						tdate)

		ledger_balance=balance
		cash_book_balance=main_cashbook_balance()

		ledger_particulars= particulars + '(' + str(loan_number) + ')'
		debit=abs(float(admin_charge))
		credit=0
		balance=float(cash_book_balance)-float(debit)
		ref_no=get_ticket()
		status='ACTIVE'
		tdate=get_current_date(now)
		source='LOAN ISSUEANCE'
		main_cashbook_posting(ledger_particulars,debit,credit,balance,ref_no,status,tdate,processed_by,source)


		if interest_deduction == "SOURCE":
			particulars= "Interest Deduction at source"
			s = titlecase(particulars)
			particulars=s
			debit=0
			credit=float(interest)
			balance=-(abs(float(ledger_balance)) - float(interest))

			post_to_ledger(member,
							transaction,
							loan_number,
							particulars,
							debit,
							credit,
							balance,
							get_current_date(now),
							'ACTIVE',
							tdate)



			Loans_Repayment_Base(member,
								nok_name,
								nok_Relationship,
								nok_phone_no,
								nok_address,
								duration,
								interest_deduction,
								interest_rate,
								interest,
								admin_charge,
								transaction,
								loan_number,
								float(loan_amount),
								float(monthly_repayment),
								-float(loan_amount),
								0,
								start_date,
								stop_date,
								processed_by,
								'ACTIVE',
								tdate,
								'SCHEDULED')


			cash_book_balance=main_cashbook_balance()

			ledger_particulars= particulars + '(' + str(loan_number) + ')'
			debit=abs(float(interest))
			credit=0
			balance=float(cash_book_balance)-float(debit)
			ref_no=get_ticket()
			status='ACTIVE'
			tdate=get_current_date(now)
			source='LOAN ISSUEANCE'
			main_cashbook_posting(ledger_particulars,debit,credit,balance,ref_no,status,tdate,processed_by,source)

		else:

			Loans_Repayment_Base(member,
								duration,
								interest_deduction,
								interest_rate,
								interest,
								admin_charge,
								transaction,
								loan_number,
								float(amount_scheduled),
								float(monthly_repayment),
								-amount_scheduled,
								0,
								start_date,
								stop_date,
								processed_by,
								'ACTIVE',
								tdate,
								'SCHEDULED')


		loan = LoansRepaymentBase.objects.get(loan_number=loan_number)
		for guarantor in guarantors:
			LoanGuarantors(loan=loan,member=guarantor.guarantor).save()

		applicant.transaction_status='TREATED'
		applicant.save()

		if applicant.applicant.applicant.loan.auto_stop_savings == 'YES':
			savings=LoanBasedSavings.objects.all()
			if savings:
				record=LoanBasedSavings.objects.all().first()
				StandingOrderAccounts.objects.filter(transaction__transaction=record.savings,transaction__member=member).update(status='INACTIVE')

				queryset=StandingOrderAccounts.objects.get(transaction__transaction=record.savings,transaction__member=member)
				StandingOrderDeactivatedAccounts(transaction=queryset,status='UNTREATED',processed_by=processed_by.username,tdate=tdate).save()




		return HttpResponseRedirect(reverse('Loan_application_processing_confirmation',args=(loan_number,)))






	form.fields['effective_date'].initial=transaction_period.transaction_period


	context={
	'button_show':button_show,
	'start_date':start_date,
	'stop_date':stop_date,
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
	'admin_charge':admin_charge,
	'form':form,
	'task_array':task_array,
	'task_enabler_array':task_enabler_array,
	'default_password':default_password,
	}

	return render(request,'deskofficer_templates/loan_application_approved_process_preview.html',context)



def loan_unscheduling_request_search(request):
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	task_array=[]
	for task in tasks:
		task_array.append(task.task.title)



	task_enabler=TransactionEnabler.objects.filter(status="YES")
	task_enabler_array=[]
	for item in task_enabler:
		task_enabler_array.append(item.title)


	default_password="NO"
	if Staff.objects.filter(admin=request.user,default_password='YES'):
		default_password="YES"

	title="Search Membership Loan for Unscheduling"
	form = searchForm(request.POST or None)

	return render(request,'deskofficer_templates/loan_unscheduling_request_search.html',{'form':form,'title':title,'task_array':task_array,
	'task_enabler_array':task_enabler_array,
	'default_password':default_password,})


def loan_unscheduling_request_list_load(request):
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	task_array=[]
	for task in tasks:
		task_array.append(task.task.title)



	task_enabler=TransactionEnabler.objects.filter(status="YES")
	task_enabler_array=[]
	for item in task_enabler:
		task_enabler_array.append(item.title)


	default_password="NO"
	if Staff.objects.filter(admin=request.user,default_password='YES'):
		default_password="YES"

	title="Loan Request order"
	form = searchForm(request.POST or None)

	if request.method == "POST":
		if request.POST.get("title")=="":
			return HttpResponseRedirect(reverse('loan_unscheduling_request_search'))


		records=LoansRepaymentBase.objects.filter(schedule_status='SCHEDULED',status='ACTIVE').filter(Q(loan_number__icontains=form['title'].value()) | Q(member__admin__last_name__icontains=form['title'].value()) | Q(member__admin__first_name__icontains=form['title'].value()) | Q(member__middle_name__icontains=form['title'].value()) | Q(member__file_no__icontains=form['title'].value()) | Q(member__ippis_no__icontains=form['title'].value()))
		context={
		'records':records,
		'title':title,
		'task_array':task_array,
		'task_enabler_array':task_enabler_array,
	'default_password':default_password,

		}
		return render(request,'deskofficer_templates/loan_unscheduling_request_list_load.html',context)


def loan_unscheduling_request_transaction_load(request,pk):
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	task_array=[]
	for task in tasks:
		task_array.append(task.task.title)



	task_enabler=TransactionEnabler.objects.filter(status="YES")
	task_enabler_array=[]
	for item in task_enabler:
		task_enabler_array.append(item.title)

	default_password="NO"
	if Staff.objects.filter(admin=request.user,default_password='YES'):
		default_password="YES"

	form=MemberShipRequest_approval_comment_form(request.POST or None)
	loan=LoansRepaymentBase.objects.get(id=pk)
	tdate=get_current_date(now)
	processed_by=CustomUser.objects.get(id=request.user.id)

	record_exist=[]
	if LoanUnschedulingRequest.objects.filter(loan=loan,approval_status='PENDING',status='UNTREATED').exists():
		record_exist=LoanUnschedulingRequest.objects.filter(loan=loan,approval_status='PENDING',status='UNTREATED').first()



	if request.method == 'POST':
		comment = request.POST.get('comment')
		if LoanUnschedulingRequest.objects.filter(loan=loan,approval_status='PENDING',status='UNTREATED').exists():
			item=LoanUnschedulingRequest.objects.filter(loan=loan,approval_status='PENDING',status='UNTREATED').first()
			item.comment=comment
			item.save()
		else:
			LoanUnschedulingRequest(comment=comment,loan=loan,
									approval_status='PENDING',
									status='UNTREATED',tdate=tdate,
									processed_by=processed_by.username
									).save()


		return HttpResponseRedirect(reverse('deskofficer_home'))

	if record_exist:
		form.fields['comment'].initial=record_exist.comment
	context={
	'record_exist':record_exist,
	'record':loan,
	'form':form,
	'task_array':task_array,
	'task_enabler_array':task_enabler_array,
	'default_password':default_password,
	}
	return render(request,'deskofficer_templates/loan_unscheduling_request_transaction_load.html',context)


def loan_unscheduling_request_transaction_processing(request):
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	task_array=[]
	for task in tasks:
		task_array.append(task.task.title)

	task_enabler=TransactionEnabler.objects.filter(status="YES")
	task_enabler_array=[]
	for item in task_enabler:
		task_enabler_array.append(item.title)

	default_password="NO"
	if Staff.objects.filter(admin=request.user,default_password='YES'):
		default_password="YES"

	records=LoanUnschedulingRequest.objects.filter(approval_status='APPROVED',status='UNTREATED')
	context={
	'records':records,
	'task_array':task_array,
	'task_enabler_array':task_enabler_array,
	'default_password':default_password,
	}
	return render(request,'deskofficer_templates/loan_unscheduling_request_transaction_processing.html',context)


def loan_unscheduling_request_transaction_processing_details(request,pk):
	form=loan_unscheduling_request_transaction_processing_details_form(request.POST or None)
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	task_array=[]
	for task in tasks:
		task_array.append(task.task.title)

	task_enabler=TransactionEnabler.objects.filter(status="YES")
	task_enabler_array=[]
	for item in task_enabler:
		task_enabler_array.append(item.title)

	default_password="NO"
	if Staff.objects.filter(admin=request.user,default_password='YES'):
		default_password="YES"

	record=LoanUnschedulingRequest.objects.get(id=pk)
	item=LoansRepaymentBase.objects.get(loan_number=record.loan.loan_number)

	if request.method == 'POST':
		record.status='TREATED'
		record.save()
		item.schedule_status='UNSCHEDULED'
		item.save()
		return HttpResponseRedirect(reverse('loan_unscheduling_request_transaction_processing'))

	form.fields['approval_comment'].initial=record.approval_comment
	form.fields['comment_exist'].initial=record.comment
	form.fields['approved_date'].initial=record.approval_date

	form.fields['approval_officer'].initial=record.approval_officer
	context={
	'record':record,
	'item':item,
	'form':form,
	'task_array':task_array,
	'task_enabler_array':task_enabler_array,
	'default_password':default_password,
	}
	return render(request,'deskofficer_templates/loan_unscheduling_request_transaction_processing_details.html',context)



############################################################
############## MEMBERSHIP COMMODITY LOAN SEARCH ############
############################################################

def membership_commodity_loan_search(request):
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	task_array=[]
	for task in tasks:
		task_array.append(task.task.title)

	task_enabler=TransactionEnabler.objects.filter(status="YES")
	task_enabler_array=[]
	for item in task_enabler:
		task_enabler_array.append(item.title)


	default_password="NO"
	if Staff.objects.filter(admin=request.user,default_password='YES'):
		default_password="YES"

	title="Search Membership Request Commodity"
	form = searchForm(request.POST or None)

	return render(request,'deskofficer_templates/membership_commodity_loan_search.html',{'task_array':task_array,
	'task_enabler_array':task_enabler_array,
	'default_password':default_password,'form':form,'title':title,})


def membership_commodity_loan_list_load(request):
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	task_array=[]
	for task in tasks:
		task_array.append(task.task.title)

	task_enabler=TransactionEnabler.objects.filter(status="YES")
	task_enabler_array=[]
	for item in task_enabler:
		task_enabler_array.append(item.title)


	default_password="NO"
	if Staff.objects.filter(admin=request.user,default_password='YES'):
		default_password="YES"

	title="Commodity Loan"
	form = searchForm(request.POST)
	members=[]
	if request.method == "POST":
		if request.POST.get("title")=="":
			return HttpResponseRedirect(reverse('membership_commodity_loan_search'))

		members=searchMembers(form['title'].value(),'ACTIVE')

	context={
	'members':members,
	'title':title,
	'task_array':task_array,
	'task_enabler_array':task_enabler_array,
	'default_password':default_password,
	}
	return render(request,'deskofficer_templates/membership_commodity_loan_list_load.html',context)




def membership_commodity_loan_Company_load(request,pk,period_pk,batch_pk,transaction_pk):
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	task_array=[]
	for task in tasks:
		task_array.append(task.task.title)

	task_enabler=TransactionEnabler.objects.filter(status="YES")
	task_enabler_array=[]
	for item in task_enabler:
		task_enabler_array.append(item.title)


	default_password="NO"
	if Staff.objects.filter(admin=request.user,default_password='YES'):
		default_password="YES"

	title="Commodity Loan"
	member=Members.objects.get(id=pk)
	transaction=TransactionTypes.objects.get(id=transaction_pk)
	period=Commodity_Period.objects.get(id=period_pk)
	batch=Commodity_Period_Batch.objects.get(id=batch_pk)
	records=Company_Products.objects.filter(batch=batch,period=period,product__category__transaction=transaction).order_by('company_id').values_list('company_id','company__title').distinct()

	company_array = []
	for index, d in enumerate(records):
		company_array.append(d)

	context={
	'member':member,
	'title':title,
	'task_array':task_array,
	'task_enabler_array':task_enabler_array,
	'default_password':default_password,
	'period':period,
	'batch':batch,
	'transaction':transaction,
	'records':records,
	'combo_period': str(period.title) + " " + str(batch.title),
	'company_array':company_array,
	}
	return render(request,'deskofficer_templates/membership_commodity_loan_Company_load.html',context)





def membership_commodity_loan_Company_products(request,return_pk,period_pk,batch_pk,transaction_pk,pk):
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	task_array=[]
	for task in tasks:
		task_array.append(task.task.title)

	task_enabler=TransactionEnabler.objects.filter(status="YES")
	task_enabler_array=[]
	for item in task_enabler:
		task_enabler_array.append(item.title)


	default_password="NO"
	if Staff.objects.filter(admin=request.user,default_password='YES'):
		default_password="YES"

	form=membership_commodity_loan_Company_products_process_Form(request.POST or None)
	status='UNTREATED'
	stock_status='ACTIVE'
	member=Members.objects.get(id=return_pk)
	transaction=TransactionTypes.objects.get(id=transaction_pk)
	period=Commodity_Period.objects.get(id=period_pk)
	batch=Commodity_Period_Batch.objects.get(id=batch_pk)

	company=Companies.objects.get(id=pk)

	if not Company_Products.objects.filter(company=company,period=period,batch=batch,product__category__transaction=transaction,status=stock_status).exists():
		messages.error(request,'No Available Records')
		return HttpResponseRedirect(reverse('membership_commodity_loan_Company_load', args=(return_pk,period.pk, batch.pk, transaction.pk)))

	records=Company_Products.objects.filter(company=company,period=period,batch=batch,product__category__transaction=transaction,status=stock_status)

	queryset=Members_Commodity_Loan_Products_Selection.objects.filter(product__batch=batch,product__period=period,product__company=company, member=member,status=status).order_by("-product__product__category__duration")

	querysum=Members_Commodity_Loan_Products_Selection.objects.filter(product__batch=batch,product__period=period,product__company=company, member=member,status=status).aggregate(total_coop=Sum('coop_price'),total_comp=Sum('company_price'),total_interest=Sum('interest'),total_admin_charge=Sum('admin_charges'))

	button_enabled=False
	if queryset:
		button_enabled=True


	total_coop=querysum['total_coop']
	total_comp=querysum['total_comp']
	total_interest=querysum['total_interest']
	total_admin_charge=querysum['total_admin_charge']

	context={
	'task_array':task_array,
	'task_enabler_array':task_enabler_array,
	'default_password':default_password,
	'period':period,
	'batch':batch,
	'transaction':transaction,
	'company':company,
	'records':records,
	'return_pk':return_pk,
	'member':member,
	'queryset':queryset,
	'form':form,
	'total_coop':total_coop,
	'total_comp':total_comp,
	'total_interest':total_interest,
	'total_admin_charge':total_admin_charge,
	'button_enabled':button_enabled,
	}
	return render(request,'deskofficer_templates/membership_commodity_loan_Company_products.html',context)



def membership_commodity_loan_Company_products_details(request,comp_pk,pk, member_pk,period_pk,batch_pk,transaction_pk):
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	task_array=[]
	for task in tasks:
		task_array.append(task.task.title)

	task_enabler=TransactionEnabler.objects.filter(status="YES")
	task_enabler_array=[]
	for item in task_enabler:
		task_enabler_array.append(item.title)

	default_password="NO"
	if Staff.objects.filter(admin=request.user,default_password='YES'):
		default_password="YES"

	form=membership_commodity_loan_Company_products_details_Form(request.POST or None)
	member=Members.objects.get(id=member_pk)
	processed_by=CustomUser.objects.get(id=request.user.id)

	transaction=TransactionTypes.objects.get(id=transaction_pk)
	period=Commodity_Period.objects.get(id=period_pk)
	batch=Commodity_Period_Batch.objects.get(id=batch_pk)

	company=Companies.objects.get(id=comp_pk)
	product=Company_Products.objects.get(id=pk)

	record=Commodity_Categories.objects.get(id=product.product.category_id)

	interest=0
	coop_price=0
	admin_charges=0

	if not product.amount:
		messages.error(request,'Product Cost is Missing')
		return HttpResponseRedirect(reverse('membership_commodity_loan_Company_products',args=(member.pk,period.pk,batch.pk,transaction.pk,company.pk)))

	if record.interest_rate_required == '1':
		interest=float(product.amount) *  (float(record.interest_rate)/100)
		coop_price=float(interest) + float(product.amount)
	else:
		coop_price=float(product.coop_amount)
		interest=float(product.coop_amount) -  float(product.amount)



	if record.admin_charges_required == '1':
		if not record.admin_charges or float(record.admin_charges)<=0:
			messages.error(request,"Please Admin Charges not set, consult the Administrator")
			return HttpResponseRedirect(reverse('membership_commodity_loan_Company_products',args=(member.pk,period.pk,batch.pk,transaction.pk,company.pk)))

		if record.admin_charges_rating == 'CASH':
			admin_charges=float(record.admin_charges)  #*  (float(record.interest_rate)/100)
		else:
			admin_charges=(float(record.admin_charges)/100)*float(product.amount)


	if request.method =='POST':
		status = 'UNTREATED'
		tdate=get_current_date(now)
		quantity=request.POST.get('quantity')

		if quantity and int(quantity) > 0:
			admin_charges=float(admin_charges)*float(quantity)
			duration=record.duration
			company_price=float(product.amount) *float(quantity)
			coop_price=float(coop_price)*float(quantity)
			interest=float(interest)*float(quantity)


			Members_Commodity_Loan_Products_Selection(status=status,
					tdate=tdate,
					member=member,
					product=product,
					quantity=quantity,
					admin_charges=admin_charges,
					duration=duration,
					company_price=company_price,
					coop_price=coop_price,
					interest=interest,
					processed_by=processed_by.username).save()

			return HttpResponseRedirect(reverse('membership_commodity_loan_Company_products',args=(member.pk,period.pk,batch.pk,transaction.pk,comp_pk,)))
		else:
			messages.error(request,'Quantity Missing')
			return HttpResponseRedirect(reverse('membership_commodity_loan_Company_products_details',args=(comp_pk,pk,member_pk,period.pk,batch.pk,transaction.pk)))

	product_data={
	'loan_type':record.transaction.name,
	'title':record.title,
	'product_name':product.product.product_name,
	'product_model':product.product.product_model,
	'company_price':product.amount,
	'coop_price':product.coop_amount,
	'interest_amount':interest,
	'duration':record.duration,
	'interest_rate':record.interest_rate,
	'admin_charges_rating':record.admin_charges_rating,
	'admin_charges':admin_charges,
	'gaurantors':record.guarantors,
	}

	form.fields['quantity'].initial='1'
	context={
	'task_array':task_array,
	'task_enabler_array':task_enabler_array,
	'default_password':default_password,

	'form':form,
	'member':member,
	'company':company,
	'product':product,
	'record':record,
	'interest':interest,
	'product_data':product_data,
	}
	return render(request,'deskofficer_templates/membership_commodity_loan_Company_products_details.html',context)


def membership_commodity_loan_Company_products_delete(request,pk,mem_pk,period_pk,batch_pk,transaction_pk,comp_pk):
	record=Members_Commodity_Loan_Products_Selection.objects.get(id=pk)
	record.delete()

	return HttpResponseRedirect(reverse('membership_commodity_loan_Company_products',args=(mem_pk,period_pk,batch_pk,transaction_pk,comp_pk)))



def membership_commodity_loan_Company_products_proceed(request,mem_pk,comp_pk,period_pk,batch_pk,transaction_pk):
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	task_array=[]
	for task in tasks:
		task_array.append(task.task.title)



	task_enabler=TransactionEnabler.objects.filter(status="YES")
	task_enabler_array=[]
	for item in task_enabler:
		task_enabler_array.append(item.title)

	default_password="NO"
	if Staff.objects.filter(admin=request.user,default_password='YES'):
		default_password="YES"


	form=membership_commodity_loan_Company_products_proceed_Form(request.POST or None)
	processed_by=CustomUser.objects.get(id=request.user.id)
	status='UNTREATED'
	status1='TREATED'
	stock_status='ACTIVE'
	approval_status='PENDING'
	certification_status='PENDING'
	submission_status='PENDING'

	transaction=TransactionTypes.objects.get(id=transaction_pk)
	period=Commodity_Period.objects.get(id=period_pk)
	batch=Commodity_Period_Batch.objects.get(id=batch_pk)

	member=Members.objects.get(id=mem_pk)
	company=Companies.objects.get(id=comp_pk)


	records=Company_Products.objects.filter(company=company,period=period,batch=batch,product__category__transaction=transaction,status=stock_status)

	queryset=Members_Commodity_Loan_Products_Selection.objects.filter(product__batch=batch,product__period=period,product__company=company, member=member,status=status).order_by("-product__product__category__duration")

	querysum=Members_Commodity_Loan_Products_Selection.objects.filter(product__batch=batch,product__period=period,product__company=company, member=member,status=status).aggregate(total_coop=Sum('coop_price'),total_comp=Sum('company_price'),total_interest=Sum('interest'),total_admin_charge=Sum('admin_charges'))

	if CompulsorySavings.objects.all().exists():
		compulsory_savings_id=CompulsorySavings.objects.first()

	else:
		messages.error(request,"Compulsary Savings Not Set")
		return HttpResponseRedirect(reverse('membership_commodity_loan_Company_products',args=(member.pk,period.pk,batch.pk,transaction.pk,company.pk)))

	compulsory_saving_total=0
	compulsory_savings =StandingOrderAccounts.objects.filter(transaction__member=member,transaction__transaction=compulsory_savings_id.transaction)


	if compulsory_savings:
		compulsory_saving_sum=StandingOrderAccounts.objects.filter(transaction__member=member,transaction__transaction=compulsory_savings_id.transaction).aggregate(total_amount=Sum('amount'))
		compulsory_saving_total=compulsory_saving_sum['total_amount']
	else:
		messages.error(request,"Compulsory Savings Not Available")
		return HttpResponseRedirect(reverse('membership_commodity_loan_Company_products',args=(member.pk,period.pk,batch.pk,transaction.pk,company.pk)))


	transaction_type=transaction.name

	if LoanBasedSavings.objects.all().exists():
		loan_based_savings_id=LoanBasedSavings.objects.first()

	else:
		messages.error(request,"Loan Based Savings Not Set")
		return HttpResponseRedirect(reverse('membership_commodity_loan_Company_products',args=(member.pk,period.pk,batch.pk,transaction.pk,company.pk)))

	loan_based_saving_total=0
	loan_based_savings =StandingOrderAccounts.objects.filter(transaction__member=member,transaction__transaction=loan_based_savings_id.savings)


	if loan_based_savings:
		loan_based_saving_sum=StandingOrderAccounts.objects.filter(transaction__member=member,transaction__transaction=loan_based_savings_id.savings).aggregate(total_amount=Sum('amount'))
		loan_based_saving_total=loan_based_saving_sum['total_amount']
	else:
		messages.error(request,"No Available Savings")
		return HttpResponseRedirect(reverse('membership_commodity_loan_Company_products',args=(member.pk,period.pk,batch.pk,transaction.pk,company.pk)))


	standing_order_total=0
	standing_orders =StandingOrderAccounts.objects.filter(transaction__member=member)


	if standing_orders:
		standing_order_sum=StandingOrderAccounts.objects.filter(transaction__member=member).aggregate(total_amount=Sum('amount'))
		standing_order_total=standing_order_sum['total_amount']
	else:
		messages.error(request,"No Available Savings")
		return HttpResponseRedirect(reverse('membership_commodity_loan_Company_products',args=(member.pk,period.pk,batch.pk,transaction.pk,company.pk)))


	loan_total=0
	loans=LoansRepaymentBase.objects.filter(member=member).filter(Q(balance__lt=0))
	if loans:
		loan_sum=LoansRepaymentBase.objects.filter(member=member).filter(Q(balance__lt=0)).aggregate(total_amount=Sum('repayment'))
		loan_total=loan_sum['total_amount']


	# total_debit=float(standing_order_total) + float(loan_total)

	total_coop=querysum['total_coop']
	total_comp=querysum['total_comp']
	total_interest=querysum['total_interest']
	total_admin_charge=querysum['total_admin_charge']

	selected_Duration=queryset[0].duration
	monthly_repayment=math.ceil(float(total_coop)/float(selected_Duration))


	button_enabled=True
	if request.method == 'POST':

		tdate=get_current_date(now)
		ticket=get_ticket()

		if ticket == 'a':
			messages.error(request,"Default Ticket Id not set")
			return HttpResponseRedirect(reverse('membership_commodity_loan_Company_products_proceed',args=(mem_pk,comp_pk,period_pk,batch_pk,transaction_pk)))


		applicant=Members_Commodity_Loan_Application(ticket=ticket,member=queryset[0],
											company_price=total_comp,
											coop_price=total_coop,
											interest=total_interest,
											admin_charge=total_admin_charge,
											duration=selected_Duration,
											repayment=monthly_repayment,
											processed_by=processed_by.username,
											status=status,
											tdate=tdate,
											period=period,
											loans=loan_total,
											savings=standing_order_total,
											batch=batch,
											approval_status=approval_status,
											submission_status=submission_status,
											)
		applicant.save()

		for item in standing_orders:
			description=item.transaction.transaction.name
			value=item.amount
			Members_Commodity_Loan_Application_Settings(status=status,ticket=ticket,applicant=applicant,description=description,value=value).save()

		for item in loans:
			description=item.transaction.name
			value=item.repayment
			Members_Commodity_Loan_Application_Settings(status=status,ticket=ticket,applicant=applicant,description=description,value=value).save()


		Members_Commodity_Loan_Products_Selection.objects.filter(product__period=period,product__batch=batch,product__company=company, member=member,status=status).update(ticket=ticket,status=status1)
		return HttpResponseRedirect(reverse('membership_commodity_loan_Company_products_Criteria_Dashboard',args=(member.pk,period.pk,batch.pk,transaction.pk,)))



	context={
	'task_array':task_array,
	'task_enabler_array':task_enabler_array,
	'default_password':default_password,

	'button_enabled':button_enabled,
	'company':company,
	'records':records,
	'member':member,
	'queryset':queryset,
	'form':form,
	'total_coop':total_coop,
	'total_comp':total_comp,
	'total_interest':total_interest,
	'total_admin_charge':total_admin_charge,
	'selected_Duration':selected_Duration,
	'monthly_repayment':monthly_repayment,
	'total_admin_charge':total_admin_charge,
	# 'standing_orders':standing_orders,
	# 'loans':loans,
	'transaction_type':transaction_type,
	'period':period,
	'batch':batch,
	'transaction':transaction,
	}
	return render(request,'deskofficer_templates/membership_commodity_loan_Company_products_proceed.html',context)





def membership_commodity_loan_Company_products_Criteria_Dashboard(request,member_pk,period_pk,batch_pk,transaction_pk):
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	task_array=[]
	for task in tasks:
		task_array.append(task.task.title)



	task_enabler=TransactionEnabler.objects.filter(status="YES")
	task_enabler_array=[]
	for item in task_enabler:
		task_enabler_array.append(item.title)

	default_password="NO"
	if Staff.objects.filter(admin=request.user,default_password='YES'):
		default_password="YES"


	transaction=TransactionTypes.objects.get(id=transaction_pk)
	period=Commodity_Period.objects.get(id=period_pk)
	batch=Commodity_Period_Batch.objects.get(id=batch_pk)

	member=Members.objects.get(id=member_pk)

	record=Commodity_Categories.objects.filter(transaction=transaction).first()

	context={
	'task_array':task_array,
	'task_enabler_array':task_enabler_array,
	'default_password':default_password,
	'transaction':transaction,
	'period':period,
	'batch':batch,
	'member':member,
	'record':record,
	}
	return render(request,'deskofficer_templates/membership_commodity_loan_Company_products_Criteria_Dashboard.html',context)


def membership_commodity_loan_Company_products_net_pay_Settings(request,member_pk,period_pk,batch_pk,transaction_pk):
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	task_array=[]
	for task in tasks:
		task_array.append(task.task.title)



	task_enabler=TransactionEnabler.objects.filter(status="YES")
	task_enabler_array=[]
	for item in task_enabler:
		task_enabler_array.append(item.title)


	default_password="NO"
	if Staff.objects.filter(admin=request.user,default_password='YES'):
		default_password="YES"

	form=membership_commodity_loan_Company_products_Criteria_Settings_form(request.POST or None)
	member=Members.objects.get(id=member_pk)

	period = Commodity_Period.objects.get(id=period_pk)
	batch = Commodity_Period_Batch.objects.get(id=batch_pk)
	transaction=TransactionTypes.objects.get(id=transaction_pk)


	submission_status='PENDING'
	certification_status='PENDING'
	approval_status='PENDING'
	status='UNTREATED'


	if Members_Commodity_Loan_Application.objects.filter(member__product__product__category__transaction=transaction,batch=batch,period=period,member__member=member,status=status,approval_status=approval_status,submission_status=submission_status).exists():
		applicant=Members_Commodity_Loan_Application.objects.get(member__product__product__category__transaction=transaction,batch=batch,period=period,member__member=member,status=status,approval_status=approval_status,submission_status=submission_status)
		if applicant.net_pay and float(applicant.net_pay)>0:
			net_pay=applicant.net_pay
		else:
			net_pay=member.last_used_net_pay
	else:

		messages.info(request,'No record found')
		return HttpResponseRedirect(reverse('membership_commodity_loan_Company_products_Criteria_Dashboard',args=(member_pk,period_pk,batch_pk,transaction_pk)))


	if request.method == 'POST':
		net_pay =float(request.POST.get('net_pay'))

		period = request.POST.get('period')

		date_format = '%Y-%m-%d'
		dtObj = datetime.datetime.strptime(period, date_format)
		period=get_current_date(dtObj)

		if net_pay <= 0:
			messages.info(request,"Please Net Pay Cannot be Zero(0)")
			return HttpResponseRedirect(reverse('membership_commodity_loan_Company_products_net_pay_Settings',args=(member_pk,period_pk,batch_pk,transaction_pk)))


		image_status=request.POST.get('image_status')

		if image_status:
			if request.FILES.get('image', False):
				image = request.FILES['image']
				fs=FileSystemStorage()
				filename=fs.save(image.name,image)
				image_url=fs.url(filename)

			else:
				image_url=None

			applicant.image = image_url


		applicant.net_pay = net_pay
		applicant.net_pay_as_at = period
		applicant.save()

		member.last_used_net_pay=net_pay
		member.net_pay_as_at=period
		member.save()
		messages.success(request,'Net Pay Updated Successfully')
		return HttpResponseRedirect(reverse('membership_commodity_loan_Company_products_Criteria_Dashboard',args=(member_pk,period_pk,batch_pk,transaction_pk)))

	if net_pay and float(net_pay)>0:
		form.fields['period'].initial=member.net_pay_as_at
	else:
		form.fields['period'].initial=now
	# form.fields['gross_pay'].initial=member.gross_pay
	form.fields['net_pay'].initial=net_pay
	context={
	'task_array':task_array,
	'task_enabler_array':task_enabler_array,
	'default_password':default_password,

	# 'records':records,
	'member':member,
	'form':form,

	}
	return render(request,'deskofficer_templates/membership_commodity_loan_Company_products_net_pay_Settings.html',context)


def membership_commodity_loan_application_submit(request,member_pk,period_pk,batch_pk,transaction_pk):
	member=Members.objects.get(id=member_pk)

	period = Commodity_Period.objects.get(id=period_pk)
	batch = Commodity_Period_Batch.objects.get(id=batch_pk)
	transaction=TransactionTypes.objects.get(id=transaction_pk)

	submission_status='PENDING'
	submission_status1='SUBMITTED'
	approval_status='PENDING'
	status='UNTREATED'


	if Members_Commodity_Loan_Application.objects.filter(batch=batch,period=period,member__member=member,status=status,approval_status=approval_status,submission_status=submission_status).exists():
		transaction=Members_Commodity_Loan_Application.objects.get(batch=batch,period=period,member__member=member,status=status,approval_status=approval_status,submission_status=submission_status)
	else:
		messages.info(request,'No record found')
		return HttpResponseRedirect(reverse('membership_commodity_loan_Company_products_Criteria_Dashboard',args=(member_pk,period_pk,batch_pk,transaction_pk)))


	if not transaction.net_pay:
		messages.info(request,'Net Pay not Set')
		return HttpResponseRedirect(reverse('membership_commodity_loan_Company_products_Criteria_Dashboard',args=(member_pk,period_pk,batch_pk,transaction_pk)))



	transaction.submission_status = submission_status1
	transaction.save()
	messages.success(request,'Net Pay Updated Successfully')
	return HttpResponseRedirect(reverse('deskofficer_home'))



def membership_commodity_loan_Period__manage_transaction_load(request):
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	task_array=[]
	for task in tasks:
		task_array.append(task.task.title)



	task_enabler=TransactionEnabler.objects.filter(status="YES")
	task_enabler_array=[]
	for item in task_enabler:
		task_enabler_array.append(item.title)


	default_password="NO"
	if Staff.objects.filter(admin=request.user,default_password='YES'):
		default_password="YES"

	form=Product_Linking_Period_Load_form(request.POST or None)

	applicants=[]
	if request.method == 'POST':
		transaction_id = request.POST.get('transaction')
		transaction = TransactionTypes.objects.get(id=transaction_id)

		period_id =request.POST.get('period')
		period=Commodity_Period.objects.get(id=period_id)

		batch_id =request.POST.get('batch')
		batch= Commodity_Period_Batch.objects.get(id=batch_id)
		submission_status="SUBMITTED"
		status='UNTREATED'
		approval_status='PENDING'
		applicants=Members_Commodity_Loan_Application.objects.filter(approval_status=approval_status,period=period,batch=batch,member__product__product__category__transaction=transaction,submission_status=submission_status,status=status)

	context={
	'task_array':task_array,
	'task_enabler_array':task_enabler_array,
	'default_password':default_password,
	'applicants':applicants,
	'form':form,
	}
	return render(request,'deskofficer_templates/membership_commodity_loan_Period__manage_transaction_load.html',context)



def membership_commodity_loan_Period__manage_transaction_delete_Confirmation(request,pk):
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	task_array=[]
	for task in tasks:
		task_array.append(task.task.title)



	task_enabler=TransactionEnabler.objects.filter(status="YES")
	task_enabler_array=[]
	for item in task_enabler:
		task_enabler_array.append(item.title)


	default_password="NO"
	if Staff.objects.filter(admin=request.user,default_password='YES'):
		default_password="YES"


	title = "Are you sure you want to drop this Request"
	record=Members_Commodity_Loan_Application.objects.get(ticket=pk)
	context={
	'task_array':task_array,
	'task_enabler_array':task_enabler_array,
	'default_password':default_password,


	'record':record,
	'title':title,
	}
	return render(request,'deskofficer_templates/membership_commodity_loan_Period__manage_transaction_delete_Confirmation.html',context)

def membership_commodity_loan_Period__manage_transaction_delete(request,pk):
	Members_Commodity_Loan_Products_Selection.objects.filter(ticket=pk).delete()
	return HttpResponseRedirect(reverse('membership_commodity_loan_Period__manage_transaction_load'))


def membership_commodity_loan_Period_Transactions_load(request,pk):
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	task_array=[]
	for task in tasks:
		task_array.append(task.task.title)


	task_enabler=TransactionEnabler.objects.filter(status="YES")
	task_enabler_array=[]
	for item in task_enabler:
		task_enabler_array.append(item.title)

	default_password="NO"
	if Staff.objects.filter(admin=request.user,default_password='YES'):
		default_password="YES"

	title="Commodity Loan"
	submission_status='PENDING'
	member=Members.objects.get(id=pk)

	applicants=Members_Commodity_Loan_Application.objects.filter(member__member=member,submission_status=submission_status)


	if request.method == "POST":
		transaction_id=request.POST.get('transaction')
		transaction=TransactionTypes.objects.get(id=transaction_id)

		period_id=request.POST.get('period')
		period=Commodity_Period.objects.get(id=period_id)
		batch_id=request.POST.get('batch')
		batch=Commodity_Period_Batch.objects.get(id=batch_id)
		return HttpResponseRedirect(reverse('membership_commodity_loan_Company_load',args=(member.pk,
																						period_id,batch_id,transaction_id,
																						)))

	form=Product_Linking_Period_Load_form(request.POST or None)

	context={
	'form':form,
	'member':member,
	'title':title,
	'task_array':task_array,
	'task_enabler_array':task_enabler_array,
	'default_password':default_password,

	'applicants':applicants,
	}
	return render(request,'deskofficer_templates/membership_commodity_loan_Period_Transactions_load.html',context)



def membership_commodity_loan_Dashboard_load(request,pk,return_pk):
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	task_array=[]
	for task in tasks:
		task_array.append(task.task.title)



	task_enabler=TransactionEnabler.objects.filter(status="YES")
	task_enabler_array=[]
	for item in task_enabler:
		task_enabler_array.append(item.title)

	default_password="NO"
	if Staff.objects.filter(admin=request.user,default_password='YES'):
		default_password="YES"


	title="Commodity Loan"
	submission_status='PENDING'
	member=Members.objects.get(id=return_pk)

	applicant=Members_Commodity_Loan_Application.objects.get(id=pk)

	context={
	'member':member,
	'task_array':task_array,
	'task_enabler_array':task_enabler_array,
	'default_password':default_password,
	'applicant':applicant,
	}
	return render(request,'deskofficer_templates/membership_commodity_loan_Dashboard_load.html',context)



def membership_commodity_loan_Company_products_net_pay_SettingsB(request,pk,return_pk):
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	task_array=[]
	for task in tasks:
		task_array.append(task.task.title)



	task_enabler=TransactionEnabler.objects.filter(status="YES")
	task_enabler_array=[]
	for item in task_enabler:
		task_enabler_array.append(item.title)

	default_password="NO"
	if Staff.objects.filter(admin=request.user,default_password='YES'):
		default_password="YES"

	form=membership_commodity_loan_Company_products_Criteria_Settings_form(request.POST or None)
	member=Members.objects.get(id=return_pk)

	net_pay=0
	transaction=Members_Commodity_Loan_Application.objects.get(id=pk)
	if transaction.net_pay and float(transaction.net_pay)>0:
		net_pay=transaction.net_pay
	else:
		net_pay=member.last_used_net_pay

	if request.method == 'POST':
		net_pay=request.POST.get('net_pay')


		if not float(net_pay)>0:
			messages.info(request,'Please Enter Net Pay')
			return HttpResponseRedirect(reverse('membership_commodity_loan_Company_products_net_pay_SettingsB',args=(pk,return_pk,)))



		transaction.net_pay=net_pay
		transaction.save()
		return HttpResponseRedirect(reverse('membership_commodity_loan_Dashboard_load',args=(transaction.pk,return_pk,)))

	form.fields['period'].initial=now
	form.fields['net_pay'].initial=transaction.net_pay
	context={
	'task_array':task_array,
	'task_enabler_array':task_enabler_array,
	'default_password':default_password,


	# 'records':records,
	'member':member,
	'form':form,

	}
	return render(request,'deskofficer_templates/membership_commodity_loan_Company_products_net_pay_SettingsB.html',context)



def membership_commodity_loan_application_submitB(request,pk,return_pk):
	submission_status='SUBMITTED'
	applicant=Members_Commodity_Loan_Application.objects.get(id=pk)

	if float(applicant.net_pay) <= 0:
		messages.info(request,"Net Pay Cannot be Zero(0)")
		return HttpResponseRedirect(reverse('membership_commodity_loan_Dashboard_load',args=(pk,return_pk,)))

	applicant.submission_status=submission_status
	applicant.save()

	return HttpResponseRedirect(reverse('deskofficer_home'))



def Savings_Lockup_search(request):
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	task_array=[]
	for task in tasks:
		task_array.append(task.task.title)

	task_enabler=TransactionEnabler.objects.filter(status="YES")
	task_enabler_array=[]
	for item in task_enabler:
		task_enabler_array.append(item.title)

	default_password="NO"
	if Staff.objects.filter(admin=request.user,default_password='YES'):
		default_password="YES"

	title="Search Membership"
	form = searchForm(request.POST or None)

	return render(request,'deskofficer_templates/Savings_Lockup_Search.html',{'form':form,'title':title,'task_array':task_array,
	'task_enabler_array':task_enabler_array,
	'default_password':default_password,})


def Savings_Lockup_list_load(request):
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	task_array=[]
	for task in tasks:
		task_array.append(task.task.title)

	task_enabler=TransactionEnabler.objects.filter(status="YES")
	task_enabler_array=[]
	for item in task_enabler:
		task_enabler_array.append(item.title)


	default_password="NO"
	if Staff.objects.filter(admin=request.user,default_password='YES'):
		default_password="YES"

	title="Members Exclusiveness"
	status="ACTIVE"
	lock_status='YES'
	form = searchForm(request.POST)

	if request.method == "POST":
		if request.POST.get("title")=="":
			return HttpResponseRedirect(reverse('Savings_Lockup_search'))

		records=MembersAccountsDomain.objects.filter(Q(member__ippis_no__icontains=form['title'].value()) | Q(member__file_no__icontains=form['title'].value()) | Q(member__phone_number__icontains=form['title'].value()) | Q(member__admin__first_name__icontains=form['title'].value()) | Q(member__admin__last_name__icontains=form['title'].value()) | Q(member__middle_name__icontains=form['title'].value())).filter(status=status,loan_lock=lock_status)
		context={
		'records':records,
		'title':title,
		'task_array':task_array,
	'task_enabler_array':task_enabler_array,
	'default_password':default_password,

		}
		return render(request,'deskofficer_templates/Savings_Lockup_list_load.html',context)


def Savings_Lockup_Processing(request,pk):
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	task_array=[]
	for task in tasks:
		task_array.append(task.task.title)



	task_enabler=TransactionEnabler.objects.filter(status="YES")
	task_enabler_array=[]
	for item in task_enabler:
		task_enabler_array.append(item.title)


	default_password="NO"
	if Staff.objects.filter(admin=request.user,default_password='YES'):
		default_password="YES"

	lock_status='NO'
	record=MembersAccountsDomain.objects.filter(id=pk).update(loan_lock=lock_status)
	return HttpResponseRedirect(reverse('Savings_Lockup_List_Load'))


#########################################################
############### TRANSACTION PERIOD MANAGER  ###############
#########################################################
def TransactionPeriodManager(request):
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	task_array=[]
	for task in tasks:
		task_array.append(task.task.title)

	task_enabler=TransactionEnabler.objects.filter(status="YES")
	task_enabler_array=[]
	for item in task_enabler:
		task_enabler_array.append(item.title)

	default_password="NO"
	if Staff.objects.filter(admin=request.user,default_password='YES'):
		default_password="YES"


	status='INACTIVE'
	records=TransactionPeriods.objects.all().order_by('transaction_period')
	form=TransactionPeriod_form(request.POST or None)
	if request.method=="POST":
		transaction_period=request.POST.get('transaction_period')
		if TransactionPeriods.objects.filter(transaction_period=transaction_period).exists():
			return HttpResponseRedirect(reverse('TransactionPeriodManager'))

		record=TransactionPeriods(transaction_period=transaction_period,status=status)
		record.save()
		return HttpResponseRedirect(reverse('TransactionPeriodManager'))
	form.fields['transaction_period'].initial=now

	context={
	'form':form,
	'records':records,
	'task_array':task_array,
	'task_enabler_array':task_enabler_array,
	'default_password':default_password,
	}
	return render(request,'deskofficer_templates/TransactionPeriodManager.html',context)


def TransactionPeriodsUpdate(request,pk):
	status='ACTIVE'
	status1='INACTIVE'
	all_record_update=TransactionPeriods.objects.all().update(status=status1)
	record=TransactionPeriods.objects.get(id=pk)
	record.status=status
	record.save()
	return HttpResponseRedirect(reverse('TransactionPeriodManager'))


def TransactionPeriodsDelete(request,pk):
	TransactionPeriods.objects.get(id=pk).delete()
	return HttpResponseRedirect(reverse('TransactionPeriodManager'))


#########################################################
############### MONTHLY DEDUCTIONS SECTION  ###############
#########################################################
def Monthly_Deduction_Salary_Institution_Load(request):
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	task_array=[]
	for task in tasks:
		task_array.append(task.task.title)

	task_enabler=TransactionEnabler.objects.filter(status="YES")
	task_enabler_array=[]
	for item in task_enabler:
		task_enabler_array.append(item.title)

	default_password="NO"
	if Staff.objects.filter(admin=request.user,default_password='YES'):
		default_password="YES"


	status="ACTIVE"
	transaction_period=TransactionPeriods.objects.get(status=status)
	transaction_period= get_current_date(transaction_period.transaction_period)
	items=SalaryInstitution.objects.all()

	context={
	'items':items,
	'transaction_period':transaction_period,
	'task_array':task_array,
	'task_enabler_array':task_enabler_array,
	'default_password':default_password,
	}
	return render(request,'deskofficer_templates/Monthly_Deduction_Salary_Institution_Load.html',context)



def Monthly_Individual_Transactions_Load(request,pk):
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	task_array=[]
	for task in tasks:
		task_array.append(task.task.title)

	task_enabler=TransactionEnabler.objects.filter(status="YES")
	task_enabler_array=[]
	for item in task_enabler:
		task_enabler_array.append(item.title)

	default_password="NO"
	if Staff.objects.filter(admin=request.user,default_password='YES'):
		default_password="YES"


	source1=TransactionSources.objects.get(title='SAVINGS')
	source2=TransactionSources.objects.get(title='LOAN')
	source3=TransactionSources.objects.get(title='SHOP')

	status='ACTIVE'
	transaction_period=TransactionPeriods.objects.get(status=status)
	transaction_period= get_current_date(transaction_period.transaction_period)

	transactions1=TransactionTypes.objects.filter(source=source1)
	transactions2=TransactionTypes.objects.filter(source=source2)
	transactions3=TransactionTypes.objects.filter(source=source3)

	salary_institution=SalaryInstitution.objects.get(id=pk)

	generated_transactions=MonthlyGeneratedTransactions.objects.filter(transaction_period=transaction_period)

	savings_status=False
	loans_status=False
	if MonthlyDeductionGenerationHeading.objects.filter(transaction_period=transaction_period,heading='SAVINGS'):
		savings_status=True

	if MonthlyDeductionGenerationHeading.objects.filter(transaction_period=transaction_period,heading='LOANS'):
		loans_status=True

	context={
	'savings_status':savings_status,
	'loans_status':loans_status,
	'transactions1':transactions1,
	'transactions2':transactions2,
	'transactions3':transactions3,
	'transaction_period':transaction_period,
	'salary_institution':salary_institution,
	'generated_transactions':generated_transactions,
	'task_array':task_array,
	'task_enabler_array':task_enabler_array,
	'default_password':default_password,
	}
	return render(request,'deskofficer_templates/Monthly_Individual_Transactions_Load.html',context)



def Monthly_Savings_Contribution_preview(request,pk, salary_inst_key):
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	task_array=[]
	for task in tasks:
		task_array.append(task.task.title)

	task_enabler=TransactionEnabler.objects.filter(status="YES")
	task_enabler_array=[]
	for item in task_enabler:
		task_enabler_array.append(item.title)

	default_password="NO"
	if Staff.objects.filter(admin=request.user,default_password='YES'):
		default_password="YES"


	status='ACTIVE'


	transaction_period=TransactionPeriods.objects.get(status=status)
	transaction_period= get_current_date(transaction_period.transaction_period)

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
	'task_array':task_array,
	'task_enabler_array':task_enabler_array,
	'default_password':default_password,
	}
	return render(request,'deskofficer_templates/Monthly_Savings_Contribution_preview.html',context)


def Monthly_Savings_Contribution_Generate(request,pk,salary_inst_key):
	processed_by=CustomUser.objects.get(id=request.user.id)
	tdate=get_current_date(now)
	status='ACTIVE'
	transaction_status='UNTREATED'
	processing_status='UNPROCESSED'

	transaction_period=TransactionPeriods.objects.get(status=status)
	transaction_period= get_current_date(transaction_period.transaction_period)

	salary_institution=SalaryInstitution.objects.get(id=salary_inst_key)
	transaction=TransactionTypes.objects.get(id=pk)
	members=StandingOrderAccounts.objects.filter(transaction__transaction=transaction,status=status,transaction__member__salary_institution=salary_institution)

	if MonthlyDeductionList.objects.filter(transaction_period=transaction_period,transaction=transaction,member__salary_institution=salary_institution).exists():
		messages.error(request,"Transaction already generated")
		return HttpResponseRedirect(reverse('Monthly_Savings_Contribution_preview',args=(pk,salary_inst_key)))

	for member in members:
		MonthlyDeductionList(
							member=member.transaction.member,
							transaction_period=transaction_period,
							transaction=transaction,
							account_number=member.transaction.account_number,
							amount=member.amount,
							balance=0,
							processing_status=processing_status,
							processed_by=processed_by.username,
							salary_institution=salary_institution,
							status=transaction_status,
							tdate=tdate).save()

	if MonthlyDeductionList.objects.filter(transaction_period=transaction_period,transaction=transaction).exists():
		MonthlyGeneratedTransactions(salary_institution=salary_institution,tdate=tdate,transaction=transaction,transaction_period=transaction_period,processed_by=processed_by.username,transaction_status=transaction_status).save()

	return HttpResponseRedirect(reverse('Monthly_Individual_Transactions_Load',args=(salary_inst_key,)))



def Monthly_loan_repayement_preview(request,pk, salary_inst_key):
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	task_array=[]
	for task in tasks:
		task_array.append(task.task.title)

	status='ACTIVE'
	schedule_status='SCHEDULED'

	task_enabler=TransactionEnabler.objects.filter(status="YES")
	task_enabler_array=[]
	for item in task_enabler:
		task_enabler_array.append(item.title)

	default_password="NO"
	if Staff.objects.filter(admin=request.user,default_password='YES'):
		default_password="YES"


	# transaction_period=TransactionPeriods.objects.get(status=status)
	# transaction_period=transaction_period.transaction_period

	salary_institution=SalaryInstitution.objects.get(id=salary_inst_key)
	transaction=TransactionTypes.objects.get(id=pk)
	members=LoansRepaymentBase.objects.filter(schedule_status=schedule_status,transaction=transaction,status=status,member__salary_institution=salary_institution).filter(Q(balance__lt=0))

	if not members:
		messages.info(request,'No record found for this transaction')
		return HttpResponseRedirect(reverse('Monthly_Individual_Transactions_Load', args=(salary_inst_key)))

	context={
	'transaction':transaction,
	'members':members,
	'transaction_period':transaction_period,
	'pk':pk,
	'salary_inst_key':salary_inst_key,
	'task_array':task_array,
	'task_enabler_array':task_enabler_array,
	'default_password':default_password,
	}
	return render(request,'deskofficer_templates/Monthly_loan_repayement_preview.html',context)


def Monthly_loan_repayement_Generate(request,pk, salary_inst_key):
	processed_by=CustomUser.objects.get(id=request.user.id)
	tdate=get_current_date(now)

	status='ACTIVE'
	transaction_status="UNTREATED"
	processing_status='UNPROCESSED'

	transaction_period=TransactionPeriods.objects.get(status=status)
	transaction_period= get_current_date(transaction_period.transaction_period)

	salary_institution=SalaryInstitution.objects.get(id=salary_inst_key)
	transaction=TransactionTypes.objects.get(id=pk)
	members=LoansRepaymentBase.objects.filter(transaction=transaction,status=status,member__salary_institution=salary_institution).filter(Q(balance__lt=0))


	if MonthlyDeductionList.objects.filter(transaction_period=transaction_period,transaction=transaction).exists():
		messages.error(request,"Transaction already generated")
		return HttpResponseRedirect(reverse('Monthly_loan_repayement_preview',args=(pk, salary_inst_key)))

	n_transaction=request.POST.get('transaction')
	if not n_transaction:
		messages.error(request,'Number of Expected Transactions Missing')
		return HttpResponseRedirect(reverse('Monthly_loan_repayement_preview',args=(pk, salary_inst_key)))


	for member in members:
		expected_stop_date=member.stop_date
		expected_stop_date=get_current_date(expected_stop_date)
		new_date=get_current_date(transaction_period.transaction_period)
		penalty_rate=0

		duction_amount= float(n_transaction)*float(member.repayment)

		generated_amount=0
		repayment=0
		penalty=0
		if abs(float(member.balance)) >= float(duction_amount):

			generated_amount=member.repayment

			if new_date > expected_stop_date:
				penalty=FailedLoanPenalty.objects.all().first()
				penalty_rate=penalty.code
				penalty_amount=(float(penalty_rate)/100)*float(member.balance)

				ledger_balance=get_ledger_balance(member.loan_number)

				new_ledger_balance=float(ledger_balance)+ float(penalty_amount)
				debit=abs(penalty_amount)
				credit=0
				particulars="Penalty on loan with balance of " + str(abs(member.balance))

				penalty=debit

				post_to_ledger(member.member,
							transaction,
							member.loan_number,
							particulars,
							debit,
							credit,
							new_ledger_balance,
							transaction_period.transaction_period,
							status,
							tdate
							)

				loan_date=get_current_date(member.start_date)
				due_date=get_current_date(member.stop_date)

				FailedLoanPenaltyRecords(transaction=member,
										amount=abs(member.balance),
										penalty=abs(penalty_amount),
										rate=penalty_rate,
										transaction_period=transaction_period,

										processed_by=processed_by.username,
										status=transaction_status,
										tdate=tdate
										).save()

										# loan_date=member.start_date,
										# due_date=member.stop_date,
										# penalty_date=transaction_period,

				member.loan_amount = float(abs(member.loan_amount)) + float(abs(penalty_amount))
				member.penalty_amount=float(member.penalty_amount) + float(abs(penalty_amount))
				member.balance=-(float(abs(member.balance)) + float(abs(penalty_amount)))
				member.save()
				generated_amount=float(generated_amount)+float(abs(penalty_amount))


			record=MonthlyDeductionList(member=member.member,

										transaction_period=transaction_period,
										transaction=transaction,
										account_number=member.loan_number,
										amount=generated_amount,
										amount_deducted=0,
										balance=0,
										repayment=member.repayment,
										penalty=penalty,
										salary_institution=salary_institution,
										processed_by=processed_by.username,
										status=transaction_status,
										tdate=tdate,
										processing_status=processing_status
										)
			record.save()



	if MonthlyDeductionList.objects.filter(member__salary_institution=salary_institution,transaction_period=transaction_period,transaction=transaction).exists():


		record=MonthlyGeneratedTransactions(salary_institution=salary_institution,tdate=tdate,transaction=transaction,transaction_period=transaction_period,processed_by=processed_by.username,transaction_status=transaction_status)
		record.save()

	return HttpResponseRedirect(reverse('Monthly_Individual_Transactions_Load',args=(salary_inst_key,)))



def MonthlyDeductionGenerationHeader(request, caption,salary_inst_key):
	status='UNTREATED'
	status1='ACTIVE'

	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	task_array=[]
	for task in tasks:
		task_array.append(task.task.title)

	task_enabler=TransactionEnabler.objects.filter(status="YES")
	task_enabler_array=[]
	for item in task_enabler:
		task_enabler_array.append(item.title)

	default_password="NO"
	if Staff.objects.filter(admin=request.user,default_password='YES'):
		default_password="YES"


	transaction_period=TransactionPeriods.objects.get(status=status1)
	salary_institution=SalaryInstitution.objects.get(id=salary_inst_key)


	if MonthlyDeductionGenerationHeading.objects.filter(transaction_period=transaction_period,heading=caption,salary_institution=salary_institution).exists():
		pass
	else:
		MonthlyDeductionGenerationHeading(salary_institution=salary_institution,transaction_period=transaction_period,heading=caption,status=status).save()
	return HttpResponseRedirect(reverse('Monthly_Individual_Transactions_Load', args=(salary_inst_key)))



def Monthly_Group_transaction_Institution_Load(request):
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	task_array=[]
	for task in tasks:
		task_array.append(task.task.title)

	task_enabler=TransactionEnabler.objects.filter(status="YES")
	task_enabler_array=[]
	for item in task_enabler:
		task_enabler_array.append(item.title)

	default_password="NO"
	if Staff.objects.filter(admin=request.user,default_password='YES'):
		default_password="YES"


	status='ACTIVE'
	transaction_period=TransactionPeriods.objects.get(status=status)
	transaction_period= get_current_date(transaction_period.transaction_period)

	items=SalaryInstitution.objects.all()

	records=MonthlyGroupGeneratedTransactions.objects.filter(transaction_period=transaction_period)

	context={
	'items':items,
	'transaction_period':transaction_period,
	'records':records,
	'task_array':task_array,
	'task_enabler_array':task_enabler_array,
	'default_password':default_password,
	}
	return render(request,'deskofficer_templates/Monthly_Group_transaction_Institution_Load.html',context)




def Monthly_Group_Generated_Transaction(request,pk):
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	task_array=[]
	for task in tasks:
		task_array.append(task.task.title)

	task_enabler=TransactionEnabler.objects.filter(status="YES")
	task_enabler_array=[]
	for item in task_enabler:
		task_enabler_array.append(item.title)

	default_password="NO"
	if Staff.objects.filter(admin=request.user,default_password='YES'):
		default_password="YES"


	status="ACTIVE"
	transaction_period=TransactionPeriods.objects.get(status=status)
	transaction_period= get_current_date(transaction_period.transaction_period)

	salary_institution=SalaryInstitution.objects.get(id=pk)

	transaction_ready=False
	savings_generated=False
	loans_generated=False


	if MonthlyDeductionGenerationHeading.objects.filter(transaction_period=transaction_period,heading="SAVINGS",salary_institution=salary_institution):
		savings_generated=True
	if MonthlyDeductionGenerationHeading.objects.filter(transaction_period=transaction_period,heading="LOANS",salary_institution=salary_institution):
		loans_generated=True

	if savings_generated and loans_generated:
		transaction_ready=True

	if MonthlyGroupGeneratedTransactions.objects.filter(salary_institution=salary_institution,transaction_period=transaction_period).exists():
		messages.error(request,"Transaction already generated")
		return HttpResponseRedirect(reverse('Monthly_Group_transaction_Institution_Load'))

	records=MonthlyDeductionList.objects.filter(member__salary_institution=salary_institution,transaction_period=transaction_period).order_by('member_id').values_list('member__member_id','member__file_no','member__admin__last_name','member__admin__first_name','member__middle_name','member__ippis_no').distinct()

	if not records:
		messages.error(request,'No Record Found')
		return HttpResponseRedirect(reverse('Monthly_Group_transaction_Institution_Load'))

	members_array = []
	for record in records:
		queryset=  MonthlyDeductionList.objects.filter(member__member_id=record[0],member__salary_institution=salary_institution,transaction_period=transaction_period).aggregate(total_cash=Sum('amount'))
		total_amount=queryset['total_cash']
		members_array.append((record[0][13:],record[2] + " " + record[3]+ " " + record[4],record[1],record[5],total_amount))

	context={
	'salary_institution':salary_institution,
	'transaction_period':transaction_period,
	'task_array':task_array,
	'task_enabler_array':task_enabler_array,
	'default_password':default_password,
	'records':records,
	'members_array':members_array,
	"savings_generated":savings_generated,
	"loans_generated":loans_generated,
	"transaction_ready":transaction_ready,
	}
	return render(request,'deskofficer_templates/Monthly_Group_Generated_Transaction.html',context)


def Monthly_Group_Transaction_preview(request,pk):
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	task_array=[]
	for task in tasks:
		task_array.append(task.task.title)

	task_enabler=TransactionEnabler.objects.filter(status="YES")
	task_enabler_array=[]
	for item in task_enabler:
		task_enabler_array.append(item.title)

	default_password="NO"
	if Staff.objects.filter(admin=request.user,default_password='YES'):
		default_password="YES"


	status="ACTIVE"

	transaction_period=TransactionPeriods.objects.get(status=status)
	transaction_period= get_current_date(transaction_period.transaction_period)

	member=Members.objects.get(ippis_no=pk)

	records=MonthlyDeductionList.objects.filter(transaction_period=transaction_period,member__ippis_no=pk)
	total_deductions=0

	deduction_sum=MonthlyDeductionList.objects.filter(transaction_period=transaction_period,member__ippis_no=pk).aggregate(total_amount=Sum('amount'))
	total_deductions=deduction_sum['total_amount']

	context={
	'records':records,
	'member':member,
	'transaction_period':transaction_period,
	'total_deductions':total_deductions,
	'task_array':task_array,
	'task_enabler_array':task_enabler_array,
	'default_password':default_password,
	}
	return render(request,'deskofficer_templates/Monthly_Group_Transaction_preview.html',context)



def Monthly_Group_Transaction_generate(request,pk):
	tdate=get_current_date(now)
	processed_by=CustomUser.objects.get(id=request.user.id)

	status="ACTIVE"
	processing_status='UNPROCESSED'
	transaction_status1="UNTREATED"
	transaction_status="TREATED"

	transaction_period=TransactionPeriods.objects.get(status=status)
	transaction_period= get_current_date(transaction_period.transaction_period)

	salary_institution=SalaryInstitution.objects.get(id=pk)
	members=Members.objects.filter(status=status,salary_institution=salary_institution)

	for member in members:
		total_deductions=0

		if MonthlyDeductionList.objects.filter(transaction_period=transaction_period,member=member,status=transaction_status1).exists():
			deduction_sum=MonthlyDeductionList.objects.filter(transaction_period=transaction_period,member=member,status=transaction_status1).aggregate(total_amount=Sum('amount'))
			amount=deduction_sum['total_amount']

			record=MonthlyDeductionListGenerated(processing_status=processing_status,tdate=tdate,salary_institution=salary_institution,transaction_period=transaction_period,member=member,amount=amount,transaction_status=transaction_status1,processed_by=processed_by.username)
			record.save()

	all_record_update=MonthlyDeductionList.objects.filter(transaction_period=transaction_period).update(status=transaction_status)
	all_record_update=MonthlyGeneratedTransactions.objects.filter(transaction_period=transaction_period).update(transaction_status=transaction_status)

	record=MonthlyGroupGeneratedTransactions(transaction_status=transaction_status1,salary_institution=salary_institution,transaction_period=transaction_period,processed_by=processed_by.username,tdate=tdate)
	record.save()

	return HttpResponseRedirect(reverse('Monthly_Group_transaction_Institution_Load'))



def Monthly_Group_Transaction_View(request,pk):
	status="ACTIVE"

	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	task_array=[]
	for task in tasks:
		task_array.append(task.task.title)

	task_enabler=TransactionEnabler.objects.filter(status="YES")
	task_enabler_array=[]
	for item in task_enabler:
		task_enabler_array.append(item.title)

	default_password="NO"
	if Staff.objects.filter(admin=request.user,default_password='YES'):
		default_password="YES"


	salary_institution=SalaryInstitution.objects.get(id=pk)

	transaction_period=TransactionPeriods.objects.get(status=status)
	transaction_period= get_current_date(transaction_period.transaction_period)

	records=MonthlyDeductionListGenerated.objects.filter(salary_institution=salary_institution,transaction_period=transaction_period)

	context={
	'transaction_period':transaction_period,
	'records':records,
	'task_array':task_array,
	'task_enabler_array':task_enabler_array,
	'default_password':default_password,
	}
	return render(request,'deskofficer_templates/Monthly_Group_Transaction_View.html',context)


def Monthly_Deduction_Main_and_Shop_Merger_Institution_load(request):
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	task_array=[]
	for task in tasks:
		task_array.append(task.task.title)

	task_enabler=TransactionEnabler.objects.filter(status="YES")
	task_enabler_array=[]
	for item in task_enabler:
		task_enabler_array.append(item.title)

	default_password="NO"
	if Staff.objects.filter(admin=request.user,default_password='YES'):
		default_password="YES"


	status="ACTIVE"
	transaction_period=TransactionPeriods.objects.get(status=status)
	transaction_period= get_current_date(transaction_period.transaction_period)

	items=SalaryInstitution.objects.all()

	context={
	'items':items,
	'transaction_period':transaction_period,
	# 'records':records,
	'task_array':task_array,
	'task_enabler_array':task_enabler_array,
	'default_password':default_password,
	}
	return render(request,'deskofficer_templates/Monthly_Deduction_Main_and_Shop_Merger_Institution_load.html',context)


def Monthly_Deduction_Main_and_Shop_Merger_Load(request,pk):
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	task_array=[]
	for task in tasks:
		task_array.append(task.task.title)



	task_enabler=TransactionEnabler.objects.filter(status="YES")
	task_enabler_array=[]
	for item in task_enabler:
		task_enabler_array.append(item.title)

	default_password="NO"
	if Staff.objects.filter(admin=request.user,default_password='YES'):
		default_password="YES"

	status="ACTIVE"
	transaction_status='UNTREATED'
	transaction_period=TransactionPeriods.objects.get(status=status)
	transaction_period= get_current_date(transaction_period.transaction_period)

	salary_institution=SalaryInstitution.objects.get(id=pk)

	records=MonthlyJointDeductionGeneratedTransactions.objects.filter(transaction_period=transaction_period,salary_institution=salary_institution,transaction_status=transaction_status)

	button_show=True
	if not records:
		button_show=False
		# messages.error(request,'No Record Found')
		# return HttpResponseRedirect(reverse('Monthly_Deduction_Main_and_Shop_Merger_Institution_load'))


	context={
	'button_show':button_show,
	'transaction_period':transaction_period,
	'salary_institution':salary_institution,
	'task_array':task_array,
	'task_enabler_array':task_enabler_array,
	'default_password':default_password,
	'records':records,
	}
	return render(request,'deskofficer_templates/Monthly_Deduction_Main_and_Shop_Merger_Load.html',context)


def Monthly_Deduction_Main_and_Shop_Merger_Load_Main_Preview(request,pk):
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	task_array=[]
	for task in tasks:
		task_array.append(task.task.title)



	task_enabler=TransactionEnabler.objects.filter(status="YES")
	task_enabler_array=[]
	for item in task_enabler:
		task_enabler_array.append(item.title)

	default_password="NO"
	if Staff.objects.filter(admin=request.user,default_password='YES'):
		default_password="YES"

	transaction_status='UNTREATED'
	transaction_status1='TREATED'
	processing_status='UNPROCESSED'
	status="ACTIVE"

	transaction_period=TransactionPeriods.objects.get(status=status)
	transaction_period= get_current_date(transaction_period.transaction_period)

	salary_institution=SalaryInstitution.objects.get(id=pk)
	processed_by=CustomUser.objects.get(id=request.user.id)
	tdate=get_current_date(now)

	if MonthlyJointDeductionGeneratedTransactions.objects.filter(salary_institution=salary_institution,transaction_period=transaction_period,transaction='MAIN').exists():
		messages.error(request,'Transaction already generated')
		return HttpResponseRedirect(reverse('Monthly_Deduction_Main_and_Shop_Merger_Load',args=(pk,)))

	records=MonthlyDeductionListGenerated.objects.filter(salary_institution=salary_institution,transaction_period=transaction_period,transaction_status=transaction_status)


	if request.method == 'POST':
		for record in records:
			MonthlyJointDeductionList(member=record.member,
									transaction_period=transaction_period,
									transaction="MAIN",
									amount=record.amount,
									processed_by=processed_by.username,
									salary_institution=salary_institution,
									status=transaction_status,
									processing_status=processing_status,tdate=tdate).save()

		MonthlyDeductionListGenerated.objects.filter(salary_institution=salary_institution,transaction_period=transaction_period,transaction_status=transaction_status).update(transaction_status=transaction_status1)

		MonthlyJointDeductionGeneratedTransactions(salary_institution=salary_institution,
													transaction_period=transaction_period,
													transaction='MAIN',
													processed_by=processed_by.username,
													transaction_status=transaction_status,
													tdate=tdate
													).save()

		return HttpResponseRedirect(reverse('Monthly_Deduction_Main_and_Shop_Merger_Load',args=(salary_institution.pk,)))

	context={
	'transaction_period':transaction_period,
	'salary_institution':salary_institution,
	'task_array':task_array,
	'task_enabler_array':task_enabler_array,
	'default_password':default_password,
	'records':records,
	}
	return render(request,'deskofficer_templates/Monthly_Deduction_Main_and_Shop_Merger_Load_Main_Preview.html',context)


def Monthly_Deduction_Main_and_Shop_Merger_Load_Main_Preview_details(request,pk):
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	task_array=[]
	for task in tasks:
		task_array.append(task.task.title)

	task_enabler=TransactionEnabler.objects.filter(status="YES")
	task_enabler_array=[]
	for item in task_enabler:
		task_enabler_array.append(item.title)

	default_password="NO"
	if Staff.objects.filter(admin=request.user,default_password='YES'):
		default_password="YES"

	status="ACTIVE"

	transaction_period=TransactionPeriods.objects.get(status=status)
	transaction_period= get_current_date(transaction_period.transaction_period)

	member=Members.objects.get(ippis_no=pk)

	records=MonthlyDeductionList.objects.filter(transaction_period=transaction_period,member__ippis_no=pk)
	total_deductions=0
	deduction_sum=MonthlyDeductionList.objects.filter(transaction_period=transaction_period,member__ippis_no=pk).aggregate(total_amount=Sum('amount'))
	total_deductions=deduction_sum['total_amount']

	context={
	'records':records,
	'member':member,
	'transaction_period':transaction_period,
	'total_deductions':total_deductions,
	'task_array':task_array,
	'task_enabler_array':task_enabler_array,
	'default_password':default_password,
	}
	return render(request,'deskofficer_templates/Monthly_Group_Transaction_preview.html',context)


def Monthly_Deduction_Main_and_Shop_Merger_Load_Shop_Preview(request,pk):
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	task_array=[]
	for task in tasks:
		task_array.append(task.task.title)

	task_enabler=TransactionEnabler.objects.filter(status="YES")
	task_enabler_array=[]
	for item in task_enabler:
		task_enabler_array.append(item.title)

	default_password="NO"
	if Staff.objects.filter(admin=request.user,default_password='YES'):
		default_password="YES"

	status="ACTIVE"
	transaction_period=TransactionPeriods.objects.get(status=status)
	transaction_period= get_current_date(transaction_period.transaction_period)


	salary_institution=SalaryInstitution.objects.get(id=pk)
	transaction_status='UNTREATED'
	transaction_status1='TREATED'
	processing_status='UNPROCESSED'
	processed_by=CustomUser.objects.get(id=request.user.id)
	tdate=get_current_date(now)

	if MonthlyJointDeductionGeneratedTransactions.objects.filter(salary_institution=salary_institution,transaction_period=transaction_period,transaction='SHOP').exists():
		messages.error(request,'Transaction already generated')
		return HttpResponseRedirect(reverse('Monthly_Deduction_Main_and_Shop_Merger_Load',args=(pk,)))

	records=MonthlyShopdeductionListGenerated.objects.filter(salary_institution=salary_institution,transaction_period=transaction_period,status=transaction_status)

	if request.method == 'POST':

		for record in records:
			MonthlyJointDeductionList(member=record.member,
									transaction_period=transaction_period,
									transaction="SHOP",
									amount=record.coop_amount,
									processed_by=processed_by.username,
									salary_institution=salary_institution,
									status=transaction_status,
									processing_status=processing_status,tdate=tdate).save()

		MonthlyShopdeductionListGenerated.objects.filter(salary_institution=salary_institution,transaction_period=transaction_period,status=transaction_status).update(status=transaction_status1)

		MonthlyJointDeductionGeneratedTransactions(salary_institution=salary_institution,
													transaction_period=transaction_period,
													transaction='SHOP',
													processed_by=processed_by.username,
													transaction_status=transaction_status,
													tdate=tdate
													).save()

		return HttpResponseRedirect(reverse('Monthly_Deduction_Main_and_Shop_Merger_Load',args=(salary_institution.pk,)))
	button_enabled=True
	if not records:
		button_enabled=False
	context={
	'transaction_period':transaction_period,
	'salary_institution':salary_institution,
	'task_array':task_array,
	'task_enabler_array':task_enabler_array,
	'default_password':default_password,
	'records':records,
	'button_enabled':button_enabled,
	}
	return render(request,'deskofficer_templates/Monthly_Deduction_Main_and_Shop_Merger_Load_Shop_Preview.html',context)


def Monthly_Deduction_Main_and_Shop_Merger_Load_Shop_Preview_details(request,pk):
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	task_array=[]
	for task in tasks:
		task_array.append(task.task.title)

	task_enabler=TransactionEnabler.objects.filter(status="YES")
	task_enabler_array=[]
	for item in task_enabler:
		task_enabler_array.append(item.title)

	default_password="NO"
	if Staff.objects.filter(admin=request.user,default_password='YES'):
		default_password="YES"

	status="ACTIVE"

	transaction_period=TransactionPeriods.objects.get(status=status)
	transaction_period= get_current_date(transaction_period.transaction_period)

	member=Members.objects.get(ippis_no=pk)

	records=MonthlyShopdeductionList.objects.filter(transaction_period=transaction_period,member__ippis_no=pk)
	total_deductions=0
	deduction_sum=MonthlyShopdeductionList.objects.filter(transaction_period=transaction_period,member__ippis_no=pk).aggregate(total_amount=Sum('amount'))
	total_deductions=deduction_sum['total_amount']

	context={
	'records':records,
	'member':member,
	'transaction_period':transaction_period,
	'total_deductions':total_deductions,
	'task_array':task_array,
	'task_enabler_array':task_enabler_array,
	'default_password':default_password,
	}
	return render(request,'deskofficer_templates/Monthly_Group_Transaction_preview.html',context)


def MonthlyJointDeductionsGenerate(request,pk):
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	task_array=[]
	for task in tasks:
		task_array.append(task.task.title)

	processing_status='UNPROCESSED'
	transaction_status='UNTREATED'

	task_enabler=TransactionEnabler.objects.filter(status="YES")
	task_enabler_array=[]
	for item in task_enabler:
		task_enabler_array.append(item.title)

	default_password="NO"
	if Staff.objects.filter(admin=request.user,default_password='YES'):
		default_password="YES"

	transaction_status1='TREATED'
	status="ACTIVE"
	transaction_period=TransactionPeriods.objects.get(status=status)
	transaction_period= get_current_date(transaction_period.transaction_period)

	salary_institution=SalaryInstitution.objects.get(id=pk)

	processed_by=CustomUser.objects.get(id=request.user.id)

	tdate=get_current_date(now)

	records=MonthlyJointDeductionList.objects.filter(salary_institution=salary_institution,transaction_period=transaction_period,status=transaction_status).order_by('member__member_id').values_list('member__member_id','member__file_no','member__admin__last_name','member__admin__first_name','member__middle_name','member__ippis_no').distinct()
	if not records:
		messages.error(request,'No Record Found')
		return HttpResponseRedirect(reverse('Monthly_Deduction_Main_and_Shop_Merger_Load',args=(pk,)))

	if MonthlyJointDeductionGenerated.objects.filter(transaction_period=transaction_period,salary_institution=salary_institution).exists():
		messages.error(request,'Transaction already generated')
		return HttpResponseRedirect(reverse('Monthly_Deduction_Main_and_Shop_Merger_Load',args=(salary_institution.pk,)))

	members_array = []
	for record in records:
		queryset=  MonthlyJointDeductionList.objects.filter(member__member_id=record[0],salary_institution=salary_institution,transaction_period=transaction_period).aggregate(total_cash=Sum('amount'))
		total_amount=queryset['total_cash']

		members_array.append((record[0][13:],record[2] + " " + record[3]+ " " + record[4],record[1],record[5],total_amount,record[0]))

	if request.method == 'POST':
		for record in records:
			member = Members.objects.get(member_id=record[0])
			queryset=  MonthlyJointDeductionList.objects.filter(member__member_id=record[0],salary_institution=salary_institution,transaction_period=transaction_period).aggregate(total_cash=Sum('amount'))
			total_amount=queryset['total_cash']

			MonthlyJointDeductionGenerated(member=member,
											transaction_period=transaction_period,
											amount=total_amount,
											processed_by=processed_by.username,
											salary_institution=salary_institution,
											status=transaction_status,
											processing_status=processing_status,
											tdate=tdate
											).save()
		MonthlyJointDeductionList.objects.filter(salary_institution=salary_institution,transaction_period=transaction_period,status=transaction_status).update(status=transaction_status1)
		MonthlyJointDeductionGeneratedTransactions.objects.filter(transaction_period=transaction_period,salary_institution=salary_institution,transaction_status=transaction_status).update(transaction_status=transaction_status1)

		return HttpResponseRedirect(reverse('Monthly_Deduction_Main_and_Shop_Merger_Institution_load'))

	context={
	'members_array':members_array,
	'records':records,
	'transaction_period':transaction_period,
	'records':records,
	'task_array':task_array,
	'task_enabler_array':task_enabler_array,
	'default_password':default_password,
	'salary_institution':salary_institution,
	}
	return render(request,'deskofficer_templates/MonthlyJointDeductionsGenerate.html',context)


def MonthlyJointDeductionsGenerateDetails(request,pk,member_pk):
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	task_array=[]
	for task in tasks:
		task_array.append(task.task.title)

	task_enabler=TransactionEnabler.objects.filter(status="YES")
	task_enabler_array=[]
	for item in task_enabler:
		task_enabler_array.append(item.title)

	default_password="NO"
	if Staff.objects.filter(admin=request.user,default_password='YES'):
		default_password="YES"

	status="ACTIVE"
	transaction_period=TransactionPeriods.objects.get(status=status)
	transaction_period= get_current_date(transaction_period.transaction_period)

	salary_institution=SalaryInstitution.objects.get(id=pk)
	member=Members.objects.get(ippis_no=member_pk)

	records=MonthlyJointDeductionList.objects.filter(member=member,salary_institution=salary_institution,transaction_period=transaction_period).order_by('transaction')
	if not records:
		messages.error(request,'No Record Found')
		return HttpResponseRedirect(reverse('MonthlyJointDeductionsGenerate',args=(pk,)))


	context={
	'member':member,
	'records':records,
	'transaction_period':transaction_period,
	'task_array':task_array,
	'task_enabler_array':task_enabler_array,
	'default_password':default_password,
	'salary_institution':salary_institution,
	}
	return render(request,'deskofficer_templates/MonthlyJointDeductionsGenerateDetails.html',context)



def Monthly_Deduction_excel_Export_Institution_Load(request):
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	task_array=[]
	for task in tasks:
		task_array.append(task.task.title)

	task_enabler=TransactionEnabler.objects.filter(status="YES")
	task_enabler_array=[]
	for item in task_enabler:
		task_enabler_array.append(item.title)

	default_password="NO"
	if Staff.objects.filter(admin=request.user,default_password='YES'):
		default_password="YES"

	status="ACTIVE"
	transaction_period=TransactionPeriods.objects.get(status=status)
	transaction_period= get_current_date(transaction_period.transaction_period)

	items=SalaryInstitution.objects.all()

	context={
	'items':items,
	'transaction_period':transaction_period,
	# 'records':records,
	'task_array':task_array,
	'task_enabler_array':task_enabler_array,
	'default_password':default_password,
	}
	return render(request,'deskofficer_templates/Monthly_Deduction_excel_Export_Institution_Load.html',context)


def Monthly_Deduction_excel_Export_load(request,pk):
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	task_array=[]
	for task in tasks:
		task_array.append(task.task.title)

	task_enabler=TransactionEnabler.objects.filter(status="YES")
	task_enabler_array=[]
	for item in task_enabler:
		task_enabler_array.append(item.title)

	default_password="NO"
	if Staff.objects.filter(admin=request.user,default_password='YES'):
		default_password="YES"

	salary_institution=SalaryInstitution.objects.get(id=pk)

	status="ACTIVE"
	transaction_period=TransactionPeriods.objects.get(status=status)
	transaction_period= get_current_date(transaction_period.transaction_period)

	records=MonthlyJointDeductionGenerated.objects.filter(salary_institution=salary_institution,transaction_period=transaction_period)

	button_enabled=True
	if records.count()==0:
		button_enabled=False

	context={
	'transaction_period':transaction_period,
	'records':records,
	'pk':pk,
	'salary_institution':salary_institution,
	'task_array':task_array,
	'task_enabler_array':task_enabler_array,
	'default_password':default_password,
	'button_enabled':button_enabled,
	}
	return render(request,'deskofficer_templates/Monthly_Deduction_excel_Export_load.html',context)


def Monthly_Deduction_excel_Export_Details(request,pk,member_pk):
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	task_array=[]
	for task in tasks:
		task_array.append(task.task.title)



	task_enabler=TransactionEnabler.objects.filter(status="YES")
	task_enabler_array=[]
	for item in task_enabler:
		task_enabler_array.append(item.title)

	default_password="NO"
	if Staff.objects.filter(admin=request.user,default_password='YES'):
		default_password="YES"

	salary_institution=SalaryInstitution.objects.get(id=pk)

	status="ACTIVE"
	transaction_period=TransactionPeriods.objects.get(status=status)
	transaction_period= get_current_date(transaction_period.transaction_period)

	record=MonthlyJointDeductionGenerated.objects.get(id=member_pk)

	record_array=[]
	grand_total=0
	queryset=MonthlyDeductionList.objects.filter(member=record.member,transaction_period=transaction_period,salary_institution=salary_institution)
	for item in queryset:
		record_array.append((item.transaction.name,item.account_number,item.amount))
		grand_total=grand_total + float(item.amount)

	queryset=MonthlyShopdeductionList.objects.filter(member=record.member,transaction_period=transaction_period,salary_institution=salary_institution)

	for item in queryset:
		record_array.append((item.transaction.name,item.account_number,item.amount))
		grand_total=grand_total + float(item.amount)

	context={
	'transaction_period':transaction_period,
	'record':record,
	'record_array':record_array,
	'grand_total':grand_total,
	'pk':pk,
	'task_array':task_array,
	'task_enabler_array':task_enabler_array,
	'default_password':default_password,

	}
	return render(request,'deskofficer_templates/Monthly_Deduction_excel_Export_Details.html',context)



def export_monthly_deductions_xls(request,pk):
	salary_institution=SalaryInstitution.objects.get(id=pk)

	status="ACTIVE"
	transaction_period=TransactionPeriods.objects.get(status=status)
	transaction_period= get_current_date(transaction_period.transaction_period)

	response = HttpResponse(content_type='application/ms-excel')
	response['Content-Disposition'] = 'attachment; filename="deductions.xls"'

	wb = xlwt.Workbook(encoding='utf-8')
	ws = wb.add_sheet('Users Data') # this will make a sheet named Users Data

	row_num = 0  # Sheet header, first row

	font_style = xlwt.XFStyle()
	font_style.font.bold = True

	columns = ['Member ID', 'File No', 'IPPIS No', 'Name','Amount']

	for col_num in range(len(columns)):
		ws.write(row_num, col_num, columns[col_num], font_style) # at 0 row 0 column

	font_style = xlwt.XFStyle()  # Sheet body, remaining rows

	rows = MonthlyJointDeductionGenerated.objects.filter(salary_institution=salary_institution,transaction_period=transaction_period).values_list('member__member_id','member__file_no','member__ippis_no','member__full_name', 'amount')

	for row in rows:
		row_num += 1
		for col_num in range(len(row)):
			ws.write(row_num, col_num, row[col_num], font_style)
	wb.save(response)

	return response




def export_norminal_roll_xls(request):
	response = HttpResponse(content_type='application/ms-excel')
	response['Content-Disposition'] = 'attachment; filename="deductions.xls"'

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




def Monthly_Account_deduction_Excel_import_Institution_Load(request):
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	task_array=[]
	for task in tasks:
		task_array.append(task.task.title)

	task_enabler=TransactionEnabler.objects.filter(status="YES")
	task_enabler_array=[]
	for item in task_enabler:
		task_enabler_array.append(item.title)

	default_password="NO"
	if Staff.objects.filter(admin=request.user,default_password='YES'):
		default_password="YES"

	status="ACTIVE"
	transaction_period=TransactionPeriods.objects.get(status=status)
	transaction_period= get_current_date(transaction_period.transaction_period)

	items=SalaryInstitution.objects.all()

	context={
	'items':items,
	'transaction_period':transaction_period,
	'task_array':task_array,
	'task_enabler_array':task_enabler_array,
	'default_password':default_password,
	}
	return render(request,'deskofficer_templates/Monthly_Account_deduction_Excel_import_Institution_Load.html',context)


def upload_AccountDeductionsResource(request,pk):
	tdate=get_current_date(now)
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	task_array=[]
	for task in tasks:
		task_array.append(task.task.title)



	task_enabler=TransactionEnabler.objects.filter(status="YES")
	task_enabler_array=[]
	for item in task_enabler:
		task_enabler_array.append(item.title)

	default_password="NO"
	if Staff.objects.filter(admin=request.user,default_password='YES'):
		default_password="YES"


	status="ACTIVE"
	transaction_period=TransactionPeriods.objects.get(status=status)
	transaction_period= get_current_date(transaction_period.transaction_period)

	transaction_status='UNTREATED'
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
			value = AccountDeductions(tdate=tdate,salary_institution=salary_institution,
					transaction_period=transaction_period,
					ippis_no=data[0],
					name=data[1],
					amount=data[2],
					transaction_status=transaction_status,
				)
			value.save()

	context={
	'transaction_period':transaction_period,
	'task_array':task_array,
	'task_enabler_array':task_enabler_array,
	'default_password':default_password,
	}
	return render(request,'deskofficer_templates/upload.html',context)


def Monthly_Account_deduction_Processing_Institution_Load(request):
	form = Monthly_Account_deduction_Processing_Institution_Load_form(request.POST or None)
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	task_array=[]
	for task in tasks:
		task_array.append(task.task.title)



	task_enabler=TransactionEnabler.objects.filter(status="YES")
	task_enabler_array=[]
	for item in task_enabler:
		task_enabler_array.append(item.title)

	default_password="NO"
	if Staff.objects.filter(admin=request.user,default_password='YES'):
		default_password="YES"

	status="ACTIVE"

	items=SalaryInstitution.objects.all()

	context={

	'form':form,
	'items':items,
	'task_array':task_array,
	'task_enabler_array':task_enabler_array,
	'default_password':default_password,
	}
	return render(request,'deskofficer_templates/Monthly_Account_deduction_Processing_Institution_Load.html',context)



def Monthly_Account_deduction_Processing_Preview(request):
	transaction_period_id=request.POST.get('transaction_period')
	transaction_period=TransactionPeriods.objects.get(id=transaction_period_id)

	salary_institution_id = request.POST.get('salary_institution')
	salary_institution=SalaryInstitution.objects.get(id=salary_institution_id)

	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	task_array=[]
	for task in tasks:
		task_array.append(task.task.title)


	default_password="NO"
	if Staff.objects.filter(admin=request.user,default_password='YES'):
		default_password="YES"


	task_enabler=TransactionEnabler.objects.filter(status="YES")
	task_enabler_array=[]
	for item in task_enabler:
		task_enabler_array.append(item.title)

	transaction_status='UNTREATED'
	status="ACTIVE"

	records=AccountDeductions.objects.filter(salary_institution=salary_institution,transaction_period=transaction_period,transaction_status=transaction_status)

	if not records:
		messages.error(request,'No record found')
		return HttpResponseRedirect(reverse('Monthly_Account_deduction_Processing_Institution_Load'))

	context={
	'records':records,
	'transaction_period':transaction_period,
	'pk':salary_institution_id,
	'task_array':task_array,
	'task_enabler_array':task_enabler_array,
	'default_password':default_password,
	}
	return render(request,'deskofficer_templates/Monthly_Account_deduction_Processing_Preview.html',context)


def Monthly_Account_deduction_Process(request,pk,trans_id):
	tdate=get_current_date(now)
	transaction_status='TREATED'
	status="ACTIVE"
	transaction_status1='UNTREATED'

	transaction_period=TransactionPeriods.objects.get(id=trans_id)
	transaction_period=get_current_date(transaction_period.transaction_period)
	
	salary_institution=SalaryInstitution.objects.get(id=pk)

	records=AccountDeductions.objects.filter(salary_institution=salary_institution,transaction_period=transaction_period)

	for record in records:
		if MonthlyJointDeductionGenerated.objects.filter(member__ippis_no=record.ippis_no,salary_institution=salary_institution,transaction_period=transaction_period).exists():
			coop_amount=MonthlyJointDeductionGenerated.objects.get(member__ippis_no=record.ippis_no,salary_institution=salary_institution,transaction_period=transaction_period)
			record_update=MonthlyJointDeductionGenerated.objects.filter(member__ippis_no=record.ippis_no,salary_institution=salary_institution,transaction_period=transaction_period).update(amount_deducted=record.amount,balance=float(record.amount)-float(coop_amount.amount))
		else:
			record=NonMemberAccountDeductions(transaction_status=transaction_status1,tdate=tdate,salary_institution=salary_institution,transaction_period=transaction_period,ippis_no=record.ippis_no,name=record.name,amount=record.amount)
			record.save()

	record_update=AccountDeductions.objects.filter(salary_institution=salary_institution,transaction_period=transaction_period).update(transaction_status=transaction_status)
	return HttpResponseRedirect(reverse('Monthly_Account_deduction_Processing_Institution_Load'))



def Monthly_Account_Main_and_Shop_Deductions_Separations(request):
	tdate=get_current_date(now)

	transaction_status="UNTREATED"
	transaction_status1="TREATED"

	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	task_array=[]
	for task in tasks:
		task_array.append(task.task.title)



	task_enabler=TransactionEnabler.objects.filter(status="YES")
	task_enabler_array=[]
	for item in task_enabler:
		task_enabler_array.append(item.title)

	default_password="NO"
	if Staff.objects.filter(admin=request.user,default_password='YES'):
		default_password="YES"

	form=deduction_ledger_posting_form(request.POST or None)

	records=[]
	process_status=False

	if request.method=="POST" and 'btnprocess' in request.POST:

		transaction_period_id=request.POST.get('transaction_period')
		transaction_period=TransactionPeriods.objects.get(id=transaction_period_id)
		transaction_period=get_current_date(transaction_period.transaction_period)

		status='UNTREATED'
		status1='TREATED'
		salary_institution_id=request.POST.get('salary_institution')
		salary_institution=SalaryInstitution.objects.get(id=salary_institution_id)
		processing_status='PROCESSED'


		records = MonthlyJointDeductionGenerated.objects.filter(salary_institution=salary_institution,transaction_period=transaction_period,status=status)


		for record in records:

			total_amount_deducted=record.amount_deducted
			others_amount=record.amount_deducted

			transaction="SHOP"
			if MonthlyJointDeductionList.objects.filter(transaction=transaction,member__ippis_no=record.member.ippis_no,member__salary_institution=salary_institution,transaction_period=transaction_period).exists():


				item1=MonthlyJointDeductionList.objects.get(transaction=transaction,member__ippis_no=record.member.ippis_no,member__salary_institution=salary_institution,transaction_period=transaction_period)

				if float(item1.amount) < float(total_amount_deducted):

					others_amount=float(total_amount_deducted) -float(item1.amount)

					MonthlyJointDeductionList.objects.filter(transaction=transaction,member__ippis_no=record.member.ippis_no,member__salary_institution=salary_institution,transaction_period=transaction_period).update(amount_deducted=item1.amount)

					MonthlyShopdeductionListGenerated.objects.filter(member__ippis_no=record.member.ippis_no,salary_institution=salary_institution,transaction_period=transaction_period).update(account_amount=item1.amount)

				elif float(item1.amount) == float(total_amount_deducted):

					others_amount=float(total_amount_deducted) -float(item1.amount)

					MonthlyJointDeductionList.objects.filter(transaction=transaction,member__ippis_no=record.member.ippis_no,member__salary_institution=salary_institution,transaction_period=transaction_period).update(amount_deducted=item1.amount)

					MonthlyShopdeductionListGenerated.objects.filter(member__ippis_no=record.member.ippis_no,salary_institution=salary_institution,transaction_period=transaction_period).update(account_amount=item1.amount)

				elif float(item1.amount) > float(total_amount_deducted):
					balance=float(item1.amount)-float(total_amount_deducted)
					others_amount=0
					MonthlyJointDeductionList.objects.filter(transaction=transaction,member__ippis_no=record.member.ippis_no,member__salary_institution=salary_institution,transaction_period=transaction_period).update(amount_deducted=total_amount_deducted,balance=balance)

					MonthlyShopdeductionListGenerated.objects.filter(member__ippis_no=record.member.ippis_no,salary_institution=salary_institution,transaction_period=transaction_period).update(account_amount=total_amount_deducted,balance=balance)

			transaction="MAIN"
			if MonthlyJointDeductionList.objects.filter(transaction=transaction,member__ippis_no=record.member.ippis_no,member__salary_institution=salary_institution,transaction_period=transaction_period).exists():



				item1=MonthlyJointDeductionList.objects.get(transaction=transaction,member__ippis_no=record.member.ippis_no,member__salary_institution=salary_institution,transaction_period=transaction_period)

				if float(item1.amount) < float(others_amount):

					over_deduction_amount=float(item1.amount)-float(others_amount)

					MonthlyJointDeductionList.objects.filter(transaction=transaction,member__ippis_no=record.member.ippis_no,member__salary_institution=salary_institution,transaction_period=transaction_period).update(amount_deducted=item1.amount)

					MonthlyDeductionListGenerated.objects.filter(member__ippis_no=record.member.ippis_no,salary_institution=salary_institution,transaction_period=transaction_period).update(amount_deducted=item1.amount)

				elif float(item1.amount) == float(others_amount):

					over_deduction_amount=0

					MonthlyJointDeductionList.objects.filter(transaction=transaction,member__ippis_no=record.member.ippis_no,member__salary_institution=salary_institution,transaction_period=transaction_period).update(amount_deducted=item1.amount)

					MonthlyDeductionListGenerated.objects.filter(member__ippis_no=record.member.ippis_no,salary_institution=salary_institution,transaction_period=transaction_period).update(amount_deducted=item1.amount)

				elif float(item1.amount) > float(others_amount):
					balance=float(others_amount)-float(item1.amount)
					over_deduction_amount=0
					MonthlyJointDeductionList.objects.filter(transaction=transaction,member__ippis_no=record.member.ippis_no,member__salary_institution=salary_institution,transaction_period=transaction_period).update(amount_deducted=others_amount,balance=balance)

					MonthlyDeductionListGenerated.objects.filter(member__ippis_no=record.member.ippis_no,salary_institution=salary_institution,transaction_period=transaction_period).update(amount_deducted=others_amount,balance=balance)

		MonthlyJointDeductionGenerated.objects.filter(salary_institution=salary_institution,transaction_period=transaction_period,status=status).update(status=status1)


		return HttpResponseRedirect(reverse('Monthly_Account_Main_and_Shop_Deductions_Separations'))


	if request.method=="POST" and 'btnview' in request.POST:

		transaction_period_id=request.POST.get('transaction_period')
		transaction_period=TransactionPeriods.objects.get(id=transaction_period_id)
		transaction_period=get_current_date(transaction_period.transaction_period)


		salary_institution_id=request.POST.get('salary_institution')
		salary_institution=SalaryInstitution.objects.get(id=salary_institution_id)

		records=MonthlyJointDeductionGenerated.objects.filter(transaction_period=transaction_period,salary_institution=salary_institution,status=transaction_status)


		if records.count()>0:
			process_status=True

	context={

	'form':form,
	'records':records,
	'process_status':process_status,
	'task_array':task_array,
	'task_enabler_array':task_enabler_array,
	'default_password':default_password,
	}

	return render(request,'deskofficer_templates/Monthly_Account_Main_and_Shop_Deductions_Separations.html',context)


def Monthly_Main_Account_deductions_Separations(request):
	tdate=get_current_date(now)
	processing_status = 'UNPROCESSED'
	processing_status1 = 'PROCESSED'
	transaction_status="UNTREATED"
	transaction_status1="TREATED"

	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	task_array=[]
	for task in tasks:
		task_array.append(task.task.title)



	task_enabler=TransactionEnabler.objects.filter(status="YES")
	task_enabler_array=[]
	for item in task_enabler:
		task_enabler_array.append(item.title)


	default_password="NO"
	if Staff.objects.filter(admin=request.user,default_password='YES'):
		default_password="YES"

	form=deduction_ledger_posting_form(request.POST or None)

	records=[]
	process_status=False

	if request.method=="POST" and 'btnprocess' in request.POST:

		transaction_period_id=request.POST.get('transaction_period')
		transaction_period=TransactionPeriods.objects.get(id=transaction_period_id)
		transaction_period=get_current_date(transaction_period.transaction_period)

		salary_institution_id=request.POST.get('salary_institution')
		salary_institution=SalaryInstitution.objects.get(id=salary_institution_id)


		transactions=TransactionTypes.objects.filter(~Q(source__title="GENERAL") | ~Q(source__title="UTILITIES")).order_by('rank')

		records=MonthlyDeductionListGenerated.objects.filter(transaction_period=transaction_period,salary_institution=salary_institution,processing_status=processing_status)


		for record in records:

			total_amount_deducted=record.amount_deducted

			for item in transactions:
				if MonthlyDeductionList.objects.filter(transaction=item,member__ippis_no=record.member.ippis_no,salary_institution=salary_institution,transaction_period=transaction_period).exists():
					item1=MonthlyDeductionList.objects.get(transaction=item,member__ippis_no=record.member.ippis_no,salary_institution=salary_institution,transaction_period=transaction_period)

					if float(total_amount_deducted) <= float(item1.amount):
						item1.amount_deducted=total_amount_deducted
						item1.balance=float(item1.amount)-float(total_amount_deducted)
						item1.save()
						break
					elif float(total_amount_deducted) > float(item1.amount):
						item1.amount_deducted=item1.amount
						item1.balance=0
						total_amount_deducted=float(total_amount_deducted)-float(item1.amount)
						item1.save()



		MonthlyDeductionListGenerated.objects.filter(transaction_period=transaction_period,salary_institution=salary_institution,processing_status=processing_status).update(processing_status=processing_status1)

		return HttpResponseRedirect(reverse('Monthly_Main_Account_deductions_Separations'))


	if request.method=="POST" and 'btnview' in request.POST:
		transaction_period_id=request.POST.get('transaction_period')
		transaction_period=TransactionPeriods.objects.get(id=transaction_period_id)
		transaction_period=get_current_date(transaction_period.transaction_period)


		salary_institution_id=request.POST.get('salary_institution')
		salary_institution=SalaryInstitution.objects.get(id=salary_institution_id)

		records=MonthlyDeductionListGenerated.objects.filter(transaction_period=transaction_period,salary_institution=salary_institution,processing_status=processing_status)


		if records.count()>0:
			process_status=True


	context={

	'form':form,
	'records':records,
	'process_status':process_status,
	'task_array':task_array,
	'task_enabler_array':task_enabler_array,
	'default_password':default_password,
	}

	return render(request,'deskofficer_templates/Monthly_Main_Account_deductions_Separations.html',context)




def monthly_wrongful_deduction_transaction_period_load(request):
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	task_array=[]
	for task in tasks:
		task_array.append(task.task.title)



	task_enabler=TransactionEnabler.objects.filter(status="YES")
	task_enabler_array=[]
	for item in task_enabler:
		task_enabler_array.append(item.title)

	default_password="NO"
	if Staff.objects.filter(admin=request.user,default_password='YES'):
		default_password="YES"

	form=TransactionPeriod_view_form(request.POST or None)
	records=[]
	if request.method=="POST":
		transaction_period_id=request.POST.get('transaction_period')
		transaction_period=TransactionPeriods.objects.get(id=transaction_period_id)
		transaction_period=get_current_date(transaction_period.transaction_period)
		records=NonMemberAccountDeductions.objects.filter(transaction_period=transaction_period)
	context={

	'form':form,
	'records':records,
	'task_array':task_array,
	'task_enabler_array':task_enabler_array,
	'default_password':default_password,
	}
	return render(request,'deskofficer_templates/monthly_wrongful_deduction_transaction_period_load.html',context)


def Monthly_Unbalanced_transactions(request):
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	task_array=[]
	for task in tasks:
		task_array.append(task.task.title)



	task_enabler=TransactionEnabler.objects.filter(status="YES")
	task_enabler_array=[]
	for item in task_enabler:
		task_enabler_array.append(item.title)

	default_password="NO"
	if Staff.objects.filter(admin=request.user,default_password='YES'):
		default_password="YES"

	form=TransactionPeriod_view_form(request.POST or None)
	processing_status="UNPROCESSED"
	records=[]
	if request.method=="POST":
		transaction_period_id=request.POST.get('transaction_period')
		date_format = '%Y-%m-%d'
		dtObj = datetime.datetime.strptime(transaction_period_id, date_format)
		transaction_period=get_current_date(dtObj)


		transaction_period=TransactionPeriods.objects.get(id=transaction_period_id)
		transaction_period=get_current_date(transaction_period.transaction_period)
		
		records=MonthlyJointDeductionGenerated.objects.filter(transaction_period=transaction_period,processing_status=processing_status).filter(~Q(balance=0))



	context={

	'form':form,
	'records':records,
	'task_array':task_array,
	'task_enabler_array':task_enabler_array,
	'default_password':default_password,
	}
	return render(request,'deskofficer_templates/Monthly_Unbalanced_transactions.html',context)


def Monthly_Unbalanced_transactions_Processing(request,pk):
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	task_array=[]
	for task in tasks:
		task_array.append(task.task.title)



	task_enabler=TransactionEnabler.objects.filter(status="YES")
	task_enabler_array=[]
	for item in task_enabler:
		task_enabler_array.append(item.title)

	default_password="NO"
	if Staff.objects.filter(admin=request.user,default_password='YES'):
		default_password="YES"

	record=MonthlyJointDeductionGenerated.objects.get(id=pk)

	context={
	'task_array':task_array,
	'task_enabler_array':task_enabler_array,
	'default_password':default_password,
	'record':record,
	}
	return render(request,'deskofficer_templates/Monthly_Unbalanced_transactions_Processing.html',context)


def Monthly_Unbalanced_transactions_Processing_Savings(request,pk):
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	task_array=[]
	for task in tasks:
		task_array.append(task.task.title)



	task_enabler=TransactionEnabler.objects.filter(status="YES")
	task_enabler_array=[]
	for item in task_enabler:
		task_enabler_array.append(item.title)

	default_password="NO"
	if Staff.objects.filter(admin=request.user,default_password='YES'):
		default_password="YES"


	tdate=get_current_date(now)

	processed_by=CustomUser.objects.get(id=request.user.id)

	refund_status="PROCESSED"

	member=MonthlyJointDeductionGenerated.objects.get(id=pk)
	transaction_period=member.transaction_period
	accounts=MembersAccountsDomain.objects.filter(member=member.member,transaction__source='SAVINGS')
	status="ACTIVE"


	ledger=[]
	account_number=[]
	account_number_status=False
	if request.method == "POST" and 'btn_fetch' in request.POST:
		account_type_id = request.POST.get("account_type")
		account_type=MembersAccountsDomain.objects.get(id=account_type_id)

		account_number=account_type.account_number
		account_number_status=True

		ledger=Display_PersonalLedger_All_Records(account_number)


	if request.method == "POST" and 'btn_submit' in request.POST:
		account_type_id = request.POST.get("account_type")
		transaction=MembersAccountsDomain.objects.get(id=account_type_id)
		amount=request.POST.get('amount')

		account_number=transaction.account_number
		credit=0
		debit=0
		balance_exist = 0
		balance=0
		particulars = ""
		d =[]
		if PersonalLedger.objects.filter(account_number=account_number).exists():
			record=PersonalLedger.objects.filter(account_number=account_number).last()
			credit=amount
			debit=0
			balance_exist = record.balance
			balance= float(balance_exist) + float(credit)
			particulars = 'OVER DEDUCTIONS REFUND AS AT ' + str(member.transaction_period.transaction_period.strftime("%d %B, %Y"))

		else:
			credit=amount
			debit=0
			balance=  float(credit)
			particulars = 'OVER DEDUCTIONS REFUND AS AT ' + str(member.transaction_period.transaction_period.strftime("%d %B, %Y"))



		post_to_ledger(member.member,
						transaction.transaction,
						account_number,
						particulars,
						debit,
						credit,
						balance,
						transaction_period.transaction_period,
						status,
						tdate
						)

		ref_number=transaction.transaction.name + "(" + str(account_number) + ")"
		queryset=MonthlyOverdeductionsRefund(member=member.member,
											over_deduction=member,
											channel="SAVINGS",
											processed_by=processed_by.username,
											tdate=tdate,
											ref_number=ref_number,
											)
		queryset.save()
		member.processing_status=refund_status
		member.save()

		ledger=Display_PersonalLedger_All_Records(account_number)


	context={
	'ledger':ledger,
	'member':member,
	'accounts':accounts,
	'account_number':account_number,
	'account_number_status':account_number_status,
	'task_array':task_array,
	'task_enabler_array':task_enabler_array,
	'default_password':default_password,
	}
	return render(request,'deskofficer_templates/Monthly_Unbalanced_transactions_Processing_Savings.html',context)



def Monthly_deduction_ledger_posting_preview(request):
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	task_array=[]
	for task in tasks:
		task_array.append(task.task.title)



	task_enabler=TransactionEnabler.objects.filter(status="YES")
	task_enabler_array=[]
	for item in task_enabler:
		task_enabler_array.append(item.title)

	default_password="NO"
	if Staff.objects.filter(admin=request.user,default_password='YES'):
		default_password="YES"

	form=deduction_ledger_posting_form(request.POST or None)


	tdate=get_current_date(now)
	processing_status='UNPROCESSED'
	processing_status1='PROCESSED'
	transaction_status="UNTREATED"
	transaction_status1="TREATED"
	status='ACTIVE'
	loan_status='INACTIVE'
	processed_by=CustomUser.objects	.get(id=request.user.id)


	records=[]
	process_status=False
	if request.method=="POST" and 'btnprocess' in request.POST:

		transaction_period_id=request.POST.get('transaction_period')
		transaction_period=TransactionPeriods.objects.get(id=transaction_period_id)

		salary_institution_id=request.POST.get('salary_institution')
		salary_institution=SalaryInstitution.objects.get(id=salary_institution_id)

		records=MonthlyDeductionList.objects.filter(transaction_period=transaction_period,salary_institution=salary_institution,status=transaction_status1,processing_status=processing_status).order_by('member_id')

		for record in records:
			if record.transaction.source.title == 'LOAN':

				if PersonalLedger.objects.filter(account_number=record.account_number).exists():
					ledger=PersonalLedger.objects.filter(account_number=record.account_number).last()
					balance=ledger.balance
					new_balance=float(balance) + float(record.amount_deducted)

					post_to_ledger(
								record.member,
								record.transaction,
								record.account_number,
								"Loan Repayment for the Period of " + str(transaction_period.transaction_period),
								0,
								record.amount_deducted,
								new_balance,
								transaction_period.transaction_period,
								status,
								tdate)
				else:

					new_balance= float(record.amount_deducted)
					post_to_ledger(
								record.member,
								record.transaction,
								record.account_number,
								"Loan Repayment for the Period of " + str(transaction_period.transaction_period),
								0,
								record.amount_deducted,
								new_balance,
								transaction_period.transaction_period,
								status,
								tdate
								)

				loan_record=LoansRepaymentBase.objects.get(loan_number=record.account_number)

				record_update=LoansRepaymentBase.objects.filter(loan_number=record.account_number).update(amount_paid=F('amount_paid')+float(record.amount_deducted),balance=F('balance')+float(record.amount_deducted))



				# if loan_record.loan_merge_status==loan_merge_status:

				# 	loan_groups=LoansRepaymentBase.objects.filter(merge_account_number=loan_record.loan_number)
				# 	merge_deduction_amount=record.amount_deducted

				# 	for loan_group in loan_groups:
				# 		entity_repayment=loan_group.repayment
				# 		entity_balance=loan_group.balance

				# 		if float(merge_deduction_amount) >= abs(float(entity_balance)):
				# 			new_entity_amount_paid=float(entity_repayment)
				# 			new_entity_balance=float(loan_group.balance)+(float(entity_repayment))
				# 			merge_deduction_amount=float(merge_deduction_amount)-(float(entity_repayment))
				# 		else:
				# 			new_entity_amount_paid=float(merge_deduction_amount)
				# 			new_entity_balance=float(loan_group.balance)+(float(merge_deduction_amount))
				# 			merge_deduction_amount=0

				# 		loan_group.amount_paid=float(loan_group.amount_paid)+ float(new_entity_amount_paid)
				# 		loan_group.balance=float(new_entity_balance)
				# 		loan_group.save()


				# 		if loan_group.balance >=0:

				# 			loan_group.status=loan_status
				# 			loan_group.save()


				# 			record_cleared=LoansCleared(tdate=tdate,loan=loan_group,processed_by=processed_by.username,status=transaction_status)
				# 			record_cleared.save()

				# else:



				loan_group=LoansRepaymentBase.objects.filter(loan_number=record.account_number).update(amount_paid=F('amount_paid')+float(record.amount_deducted),balance=F('balance')+float(record.amount_deducted))

				if LoansRepaymentBase.objects.filter(loan_number=record.account_number).filter(Q(balance__gte=0)):
					record_update=LoansRepaymentBase.objects.filter(loan_number=record.account_number).update(status=loan_status)


					loan=LoansRepaymentBase.objects.get(loan_number=record.account_number)
					record_cleared=LoansCleared(tdate=tdate,loan=loan,processed_by=processed_by.username,status=transaction_status)
					record_cleared.save()

			elif record.transaction.source == 'SAVINGS':

				if PersonalLedger.objects.filter(account_number=record.account_number).exists():
					ledger=PersonalLedger.objects.filter(account_number=record.account_number).last()
					balance=ledger.balance
					new_balance=float(balance) + float(record.amount_deducted)

					post_to_ledger(
									record.member,
									record.transaction,
									record.account_number,
									"Monthly Contribution for the Period of " +  str(transaction_period.transaction_period),
									0,
									record.amount_deducted,
									new_balance,
									transaction_period.transaction_period,
									status,
									tdate)
				else:

					new_balance= float(record.amount_deducted)
					post_to_ledger(
									record.member,
									record.transaction,
									record.account_number,
									"Monthly Contribution for the Period of " + str(transaction_period.transaction_period),
									0,
									record.amount_deducted,
									new_balance,
									transaction_period.transaction_period,
									status,
									tdate
									)



		MonthlyDeductionList.objects.filter(transaction_period=transaction_period,salary_institution=salary_institution,status=transaction_status1,processing_status=processing_status).update(processing_status=processing_status1)
		return HttpResponseRedirect(reverse('Monthly_deduction_ledger_posting_preview'))



	if request.method=="POST" and 'btnview' in request.POST:
		transaction_period_id=request.POST.get('transaction_period')
		transaction_period=TransactionPeriods.objects.get(id=transaction_period_id)

		salary_institution_id=request.POST.get('salary_institution')
		salary_institution=SalaryInstitution.objects.get(id=salary_institution_id)

		records=MonthlyDeductionList.objects.filter(transaction_period=transaction_period,salary_institution=salary_institution,status=transaction_status1,processing_status=processing_status).order_by('member_id')

		if records.count()>0:
			process_status=True

	context={

	'form':form,
	'records':records,
	'process_status':process_status,
	'task_array':task_array,
	'task_enabler_array':task_enabler_array,
	'default_password':default_password,
	}
	return render(request,'deskofficer_templates/Monthly_deduction_ledger_posting_preview.html',context)




#########################################################
############### EXTERNAL FASCILITY MANAGER###############
#########################################################
def external_fascility_update_search(request):
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	task_array=[]
	for task in tasks:
		task_array.append(task.task.title)



	task_enabler=TransactionEnabler.objects.filter(status="YES")
	task_enabler_array=[]
	for item in task_enabler:
		task_enabler_array.append(item.title)

	default_password="NO"
	if Staff.objects.filter(admin=request.user,default_password='YES'):
		default_password="YES"

	title="Search Membership External Fascilities"
	form = searchForm(request.POST or None)

	return render(request,'deskofficer_templates/external_fascility_update_search.html',{'form':form,'title':title,'task_array':task_array,
	'task_enabler_array':task_enabler_array,
	'default_password':default_password,})


def external_fascility_update_list_load(request):
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	task_array=[]
	for task in tasks:
		task_array.append(task.task.title)



	task_enabler=TransactionEnabler.objects.filter(status="YES")
	task_enabler_array=[]
	for item in task_enabler:
		task_enabler_array.append(item.title)

	default_password="NO"
	if Staff.objects.filter(admin=request.user,default_password='YES'):
		default_password="YES"


	title="Members Exclusiveness"
	status="ACTIVE"
	form = searchForm(request.POST)

	if request.method == "POST":
		if request.POST.get("title")=="":
			return HttpResponseRedirect(reverse('external_fascility_update_search'))

		members=searchMembers(form['title'].value(),status)

		context={
		'members':members,
		'title':title,
		'task_array':task_array,
	'task_enabler_array':task_enabler_array,
	'default_password':default_password,

		}
		return render(request,'deskofficer_templates/external_fascility_update_list_load.html',context)






#########################################################
############### EXCLUSIVENESS #####################
#########################################################
def members_wavers_request_search(request):
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	task_array=[]
	for task in tasks:
		task_array.append(task.task.title)



	task_enabler=TransactionEnabler.objects.filter(status="YES")
	task_enabler_array=[]
	for item in task_enabler:
		task_enabler_array.append(item.title)

	default_password="NO"
	if Staff.objects.filter(admin=request.user,default_password='YES'):
		default_password="YES"

	title="Search Members Additional Loan Request"
	form = searchForm(request.POST or None)

	return render(request,'deskofficer_templates/members_wavers_request_search.html',{'form':form,'title':title,'task_array':task_array,
	'task_enabler_array':task_enabler_array,
	'default_password':default_password,})


def members_wavers_request_list_load(request):
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	task_array=[]
	for task in tasks:
		task_array.append(task.task.title)



	task_enabler=TransactionEnabler.objects.filter(status="YES")
	task_enabler_array=[]
	for item in task_enabler:
		task_enabler_array.append(item.title)

	default_password="NO"
	if Staff.objects.filter(admin=request.user,default_password='YES'):
		default_password="YES"

	title="Members Additional Loan"
	form = searchForm(request.POST)
	if request.method == "POST":
		if request.POST.get("title")=="":
			return HttpResponseRedirect(reverse('members_additional_loan_request_search'))

		members=searchMembers(form['title'].value(),'ACTIVE')

		context={
		'members':members,
		'title':title,
		'task_array':task_array,
	'task_enabler_array':task_enabler_array,
	'default_password':default_password,

		}
		return render(request,'deskofficer_templates/members_wavers_request_list_load.html',context)


def members_wavers_request_register(request,pk):
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	task_array=[]
	for task in tasks:
		task_array.append(task.task.title)



	task_enabler=TransactionEnabler.objects.filter(status="YES")
	task_enabler_array=[]
	for item in task_enabler:
		task_enabler_array.append(item.title)

	default_password="NO"
	if Staff.objects.filter(admin=request.user,default_password='YES'):
		default_password="YES"

	status='UNTREATED'
	approval_status='PENDING'
	form=members_exclusiveness_request_register_form(request.POST or None)
	member=Members.objects.get(id=pk)
	items=MembersExclusiveness.objects.filter(member=member,status=status,approval_status=approval_status)

	if request.method=="POST" and 'btn-submit' in request.POST:

		tdate=get_current_date(now)

		transaction_id=request.POST.get('transactions')
		transaction=TransactionTypes.objects.get(id=transaction_id)

		period_id=request.POST.get("period")
		period = Commodity_Period.objects.get(id=period_id)

		batch_id=request.POST.get('batch')
		batch=Commodity_Period_Batch.objects.get(id=batch_id)

		task_id=request.POST.get('exceptables')
		task=ExceptableCriterias.objects.get(id=task_id)

		purpose=request.POST.get('purpose')
		if not purpose:
			messages.error(request,'Please State the Reason')
			return HttpResponseRedirect(reverse('members_wavers_request_register',args=(pk,)))


		if MembersExclusiveness.objects.filter(task=task,period=period,batch=batch,member=member,status=status,approval_status=approval_status,transaction=transaction).exists():
			messages.error(request,'Incomplete Transactions Still Active')
			return HttpResponseRedirect(reverse('members_wavers_request_register',args=(pk,)))

		if MembersExclusiveness.objects.filter(member=member,status=status,period=period,batch=batch,transaction=transaction,task=task).exists():
			messages.error(request,'You still have Open Transaction')
			return HttpResponseRedirect(reverse('members_wavers_request_register',args=(pk,)))

		record=MembersExclusiveness(task=task,purpose=purpose,period=period,batch=batch,tdate=tdate,member=member,status=status,approval_status=approval_status,transaction=transaction)
		record.save()
		messages.success(request,'Record Added Successfully')
		return HttpResponseRedirect(reverse('members_wavers_request_register',args=(pk,)))

	context={

	'member':member,
	'form':form,
	'items':items,
	'return_pk':pk,
	'task_array':task_array,
	'task_enabler_array':task_enabler_array,
	'default_password':default_password,
	}
	return render(request,'deskofficer_templates/members_wavers_request_register.html',context)




def members_wavers_request_approved_list_load(request):
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	task_array=[]
	for task in tasks:
		task_array.append(task.task.title)



	task_enabler=TransactionEnabler.objects.filter(status="YES")
	task_enabler_array=[]
	for item in task_enabler:
		task_enabler_array.append(item.title)

	default_password="NO"
	if Staff.objects.filter(admin=request.user,default_password='YES'):
		default_password="YES"

	approval_status="PENDING"
	status='UNTREATED'

	members=MembersExclusiveness.objects.filter(status=status).exclude(approval_status=approval_status)


	context={

	'members':members,
	'task_array':task_array,
	'task_enabler_array':task_enabler_array,
	'default_password':default_password,
	}
	return render(request,'deskofficer_templates/members_wavers_request_approved_list_load.html',context)


def members_wavers_request_delete(request,pk,return_pk):
	record=MembersExclusiveness.objects.get(id=pk)
	record.delete()
	return HttpResponseRedirect(reverse('members_wavers_request_register',args=(return_pk,)))




def members_additional_loan_request_search(request):
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	task_array=[]
	for task in tasks:
		task_array.append(task.task.title)



	task_enabler=TransactionEnabler.objects.filter(status="YES")
	task_enabler_array=[]
	for item in task_enabler:
		task_enabler_array.append(item.title)

	default_password="NO"
	if Staff.objects.filter(admin=request.user,default_password='YES'):
		default_password="YES"

	title="Search Members Additional Loan Request"
	form = searchForm(request.POST or None)

	return render(request,'deskofficer_templates/members_additional_loan_request_search.html',{'form':form,'title':title,'task_array':task_array,
	'task_enabler_array':task_enabler_array,
	'default_password':default_password,})


def members_additional_loan_request_list_load(request):
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	task_array=[]
	for task in tasks:
		task_array.append(task.task.title)



	task_enabler=TransactionEnabler.objects.filter(status="YES")
	task_enabler_array=[]
	for item in task_enabler:
		task_enabler_array.append(item.title)

	default_password="NO"
	if Staff.objects.filter(admin=request.user,default_password='YES'):
		default_password="YES"

	title="Members Additional Loan"
	form = searchForm(request.POST)
	if request.method == "POST":
		if request.POST.get("title")=="":
			return HttpResponseRedirect(reverse('members_additional_loan_request_search'))

		form = searchForm(request.POST)
		members=searchMembers(form['title'].value(),'ACTIVE')



		context={

		'members':members,
		'title':title,
		'task_array':task_array,
	'task_enabler_array':task_enabler_array,
	'default_password':default_password,

		}
		return render(request,'deskofficer_templates/members_additional_loan_request_list_load.html',context)


def members_additional_loan_request_register(request,pk):
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	task_array=[]
	for task in tasks:
		task_array.append(task.task.title)



	task_enabler=TransactionEnabler.objects.filter(status="YES")
	task_enabler_array=[]
	for item in task_enabler:
		task_enabler_array.append(item.title)

	default_password="NO"
	if Staff.objects.filter(admin=request.user,default_password='YES'):
		default_password="YES"

	status='UNTREATED'
	approval_status='PENDING'
	form=members_exclusiveness_request_register_form(request.POST or None)
	member=Members.objects.get(id=pk)
	items=MembersExclusiveness.objects.filter(member=member,status=status,approval_status=approval_status)

	if request.method=="POST" and 'btn-submit' in request.POST:
		tdate=get_current_date(now)

		transaction_id=request.POST.get('transactions')
		transaction=TransactionTypes.objects.get(id=transaction_id)

		period_id=request.POST.get("period")
		period = Commodity_Period.objects.get(id=period_id)

		batch_id=request.POST.get('batch')
		batch=Commodity_Period_Batch.objects.get(id=batch_id)

		task_id=request.POST.get('exceptables')
		task=ExceptableCriterias.objects.get(id=task_id)

		purpose=request.POST.get('purpose')
		if not purpose:
			messages.error(request,'Please State the Reason')
			return HttpResponseRedirect(reverse('members_additional_loan_request_register',args=(pk,)))


		if MembersExclusiveness.objects.filter(task=task,period=period,batch=batch,member=member,status=status,approval_status=approval_status,transaction=transaction).exists():
			messages.error(request,'Incomplete Transactions Still Active')
			return HttpResponseRedirect(reverse('members_additional_loan_request_register',args=(pk,)))


		record=MembersExclusiveness(task=task,purpose=purpose,period=period,batch=batch,tdate=tdate,member=member,status=status,approval_status=approval_status,transaction=transaction)
		record.save()
		messages.success(request,'Record Added Successfully')
		return HttpResponseRedirect(reverse('members_additional_loan_request_register',args=(pk,)))

	context={

	'member':member,
	'form':form,
	'items':items,
	'return_pk':pk,
	'task_array':task_array,
	'task_enabler_array':task_enabler_array,
	'default_password':default_password,
	}
	return render(request,'deskofficer_templates/members_additional_loan_request_register.html',context)


def members_exclusiveness_request_search(request):
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	task_array=[]
	for task in tasks:
		task_array.append(task.task.title)



	task_enabler=TransactionEnabler.objects.filter(status="YES")
	task_enabler_array=[]
	for item in task_enabler:
		task_enabler_array.append(item.title)

	default_password="NO"
	if Staff.objects.filter(admin=request.user,default_password='YES'):
		default_password="YES"

	title="Search Membership Exclusive Request"
	form = searchForm(request.POST or None)

	return render(request,'deskofficer_templates/members_exclusiveness_request_search.html',{'form':form,'title':title,'task_array':task_array,
	'task_enabler_array':task_enabler_array,
	'default_password':default_password,})


def members_exclusiveness_request_list_load(request):
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	task_array=[]
	for task in tasks:
		task_array.append(task.task.title)



	task_enabler=TransactionEnabler.objects.filter(status="YES")
	task_enabler_array=[]
	for item in task_enabler:
		task_enabler_array.append(item.title)

	default_password="NO"
	if Staff.objects.filter(admin=request.user,default_password='YES'):
		default_password="YES"


	title="Members Exclusiveness"
	form = searchForm(request.POST)
	if request.method == "POST":
		if request.POST.get("title")=="":
			return HttpResponseRedirect(reverse('members_exclusiveness_request_search'))

		status="ACTIVE"
		form = searchForm(request.POST)
		members=searchMembers(form['title'].value(),status)



		context={

		'members':members,
		'title':title,
		'task_array':task_array,
	'task_enabler_array':task_enabler_array,
	'default_password':default_password,

		}
		return render(request,'deskofficer_templates/members_exclusiveness_request_list_load.html',context)


def members_exclusiveness_request_register(request,pk):
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	task_array=[]
	for task in tasks:
		task_array.append(task.task.title)



	task_enabler=TransactionEnabler.objects.filter(status="YES")
	task_enabler_array=[]
	for item in task_enabler:
		task_enabler_array.append(item.title)

	default_password="NO"
	if Staff.objects.filter(admin=request.user,default_password='YES'):
		default_password="YES"

	status='UNTREATED'
	approval_status='PENDING'
	form=members_exclusiveness_request_register_form(request.POST or None)
	member=Members.objects.get(id=pk)
	items=MembersExclusiveness.objects.filter(member=member,status=status,approval_status=approval_status)

	if request.method=="POST" and 'btn-submit' in request.POST:
		tdate=get_current_date(now)
		transaction_id=request.POST.get('transactions')
		transaction=TransactionTypes.objects.get(id=transaction_id)

		period_id=request.POST.get("period")
		period = Commodity_Period.objects.get(id=period_id)

		batch_id=request.POST.get('batch')
		batch=Commodity_Period_Batch.objects.get(id=batch_id)


		if MembersExclusiveness.objects.filter(period=period,batch=batch,member=member,status=status,approval_status=approval_status,transaction=transaction).exists():
			messages.error(request,'Incomplete Transactions Still Active')
			return HttpResponseRedirect(reverse('members_exclusiveness_request_register',args=(pk,)))


		record=MembersExclusiveness(period=period,batch=batch,tdate=tdate,member=member,status=status,approval_status=approval_status,transaction=transaction)
		record.save()
		messages.success(request,'Record Added Successfully')
		return HttpResponseRedirect(reverse('members_exclusiveness_request_register',args=(pk,)))

		return HttpResponseRedirect(reverse('members_exclusiveness_request_register',args=(pk,)))


	context={

	'form':form,
	'items':items,
	'return_pk':pk,
	'task_array':task_array,
	'task_enabler_array':task_enabler_array,
	'default_password':default_password,
	}
	return render(request,'deskofficer_templates/members_exclusiveness_request_register.html',context)




def members_exclusiveness_approved_list_load(request):
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	task_array=[]
	for task in tasks:
		task_array.append(task.task.title)



	task_enabler=TransactionEnabler.objects.filter(status="YES")
	task_enabler_array=[]
	for item in task_enabler:
		task_enabler_array.append(item.title)

	default_password="NO"
	if Staff.objects.filter(admin=request.user,default_password='YES'):
		default_password="YES"

	approval_status="PENDING"
	status='UNTREATED'

	members=MembersExclusiveness.objects.filter(status=status).exclude(approval_status=approval_status)


	context={

	'members':members,
	'task_array':task_array,
	'task_enabler_array':task_enabler_array,
	'default_password':default_password,
	}
	return render(request,'deskofficer_templates/members_exclusiveness_approved_list_load.html',context)


def members_exclusiveness_approved_processed(request,pk):
	status='TREATED'
	member=MembersExclusiveness.objects.get(id=pk)
	member.status=status
	member.save()

	return HttpResponseRedirect(reverse('members_exclusiveness_approved_list_load'))





#########################################################
############### MEMBERS BANK INFO#####################
#########################################################

def MembersBankAccounts_list_search(request):
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	task_array=[]
	for task in tasks:
		task_array.append(task.task.title)



	task_enabler=TransactionEnabler.objects.filter(status="YES")
	task_enabler_array=[]
	for item in task_enabler:
		task_enabler_array.append(item.title)

	default_password="NO"
	if Staff.objects.filter(admin=request.user,default_password='YES'):
		default_password="YES"

	title="Search Membership Account Creation"
	form = searchForm(request.POST or None)

	return render(request,'deskofficer_templates/MembersBankAccounts_list_search.html',{'form':form,'title':title,'task_array':task_array,
	'task_enabler_array':task_enabler_array,
	'default_password':default_password,})



def MembersBankAccounts_list_load(request):
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	task_array=[]
	for task in tasks:
		task_array.append(task.task.title)



	task_enabler=TransactionEnabler.objects.filter(status="YES")
	task_enabler_array=[]
	for item in task_enabler:
		task_enabler_array.append(item.title)

	default_password="NO"
	if Staff.objects.filter(admin=request.user,default_password='YES'):
		default_password="YES"


	title="Bank Accoun Creation"
	status="ACTIVE"
	form = searchForm(request.POST)
	if request.method == "POST":
		if request.POST.get("title")=="":
			return HttpResponseRedirect(reverse('MembersBankAccounts_list_search'))

		members=searchMembers(form['title'].value(),status)

		context={
		'members':members,
		'title':title,
		'task_array':task_array,
	'task_enabler_array':task_enabler_array,
	'default_password':default_password,

		}
		return render(request,'deskofficer_templates/MembersBankAccounts_list_load.html',context)




def Members_Bank_Accounts(request,pk):
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	task_array=[]
	for task in tasks:
		task_array.append(task.task.title)



	task_enabler=TransactionEnabler.objects.filter(status="YES")
	task_enabler_array=[]
	for item in task_enabler:
		task_enabler_array.append(item.title)

	default_password="NO"
	if Staff.objects.filter(admin=request.user,default_password='YES'):
		default_password="YES"

	form=MembersBankAccounts_form(request.POST or None)
	member=Members.objects.get(id=pk)
	accounts = MembersBankAccounts.objects.filter(member_id_id=pk).order_by('account_priority')
	form.fields['account_name'].initial= member.admin.last_name + " " + member.admin.first_name + " " + member.middle_name
	if request.method=="POST":
		form=MembersBankAccounts_form(request.POST)


		if form.is_valid():
			member_id = Members.objects.get(id=pk)
			bank_id=form.cleaned_data['banks']
			bank=Banks.objects.get(id=bank_id)

			account_type = form.cleaned_data['account_types']
			# return HttpResponse(account_type_id)
			# account_type=AccountTypes.objects.get(id=account_type_id)

			account_name = form.cleaned_data['account_name']
			account_number = form.cleaned_data['account_number']

			if MembersBankAccounts.objects.filter(account_number=account_number).exists():
				messages.error(request,"Failed to add Account, Alreasy in Use")
				return HttpResponseRedirect(reverse('Members_Bank_Accounts',args=(pk,)))

			lock_status='OPEN'
			status="ACTIVE"

			record=MembersBankAccounts(status=status,lock_status=lock_status,member_id=member_id,bank=bank,account_type=account_type,account_name=account_name,account_number=account_number)
			record.save()
			messages.success(request,"Account Added Successfully")
			return HttpResponseRedirect(reverse('Members_Bank_Accounts',args=(pk,)))



	context={

	'form':form,
	'member':member,
	'accounts':accounts,
	'return_pk':pk,
	'task_array':task_array,
	'task_enabler_array':task_enabler_array,
	'default_password':default_password,
	}
	return render(request,'deskofficer_templates/MembersBankAccounts.html',context)

def Members_Bank_Accounts_prioritization(request,pk):
	record=MembersBankAccounts.objects.get(id=pk)
	MembersBankAccounts.objects.filter(member_id=record.member_id).update(account_priority=1)
	return_pk=record.member_id_id
	record.account_priority=0
	record.save()
	return HttpResponseRedirect(reverse('Members_Bank_Accounts',args=(return_pk,)))


def Members_Bank_Accounts_remove(request,pk):
	record=MembersBankAccounts.objects.get(id=pk)
	return_pk=record.member_id_id
	record.delete()
	return HttpResponseRedirect(reverse('Members_Bank_Accounts',args=(return_pk,)))


def Members_Bank_Accounts_lock(request,pk):
	member=Members.objects.get(id=pk)
	lock_status='LOCKED'
	record=MembersBankAccounts.objects.filter(member_id=member).update(lock_status=lock_status)


	return HttpResponseRedirect(reverse('deskofficer_home'))


def Members_Bank_Accounts_edit_search(request):
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	task_array=[]
	for task in tasks:
		task_array.append(task.task.title)



	task_enabler=TransactionEnabler.objects.filter(status="YES")
	task_enabler_array=[]
	for item in task_enabler:
		task_enabler_array.append(item.title)

	default_password="NO"
	if Staff.objects.filter(admin=request.user,default_password='YES'):
		default_password="YES"


	title="Search Membership Account Update"
	form = searchForm(request.POST or None)

	return render(request,'deskofficer_templates/Members_Bank_Accounts_edit_search.html',{'form':form,'title':title,'task_array':task_array,
	'task_enabler_array':task_enabler_array,
	'default_password':default_password,})


def Members_Bank_Accounts_edit_list_load(request):
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	task_array=[]
	for task in tasks:
		task_array.append(task.task.title)



	task_enabler=TransactionEnabler.objects.filter(status="YES")
	task_enabler_array=[]
	for item in task_enabler:
		task_enabler_array.append(item.title)

	default_password="NO"
	if Staff.objects.filter(admin=request.user,default_password='YES'):
		default_password="YES"


	title="Bank Accoun update"
	status="ACTIVE"
	form = searchForm(request.POST)

	if request.method == "POST":
		if request.POST.get("title")=="":
			return HttpResponseRedirect(reverse('Members_Bank_Accounts_edit_search'))

		members=Members.objects.filter(Q(phone_number__icontains=form['title'].value()) | Q(admin__first_name__icontains=form['title'].value()) | Q(admin__last_name__icontains=form['title'].value()) | Q(middle_name__icontains=form['title'].value())).filter(status=status)

		context={
		'members':members,
		'title':title,
		'task_array':task_array,
	'task_enabler_array':task_enabler_array,
	'default_password':default_password,

		}
		return render(request,'deskofficer_templates/Members_Bank_Accounts_edit_list_load.html',context)



def Members_Bank_Accounts_edit_details_load(request,pk):
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	task_array=[]
	for task in tasks:
		task_array.append(task.task.title)



	task_enabler=TransactionEnabler.objects.filter(status="YES")
	task_enabler_array=[]
	for item in task_enabler:
		task_enabler_array.append(item.title)

	default_password="NO"
	if Staff.objects.filter(admin=request.user,default_password='YES'):
		default_password="YES"

	member=Members.objects.get(id=pk)
	accounts = MembersBankAccounts.objects.filter(member_id_id=pk).order_by("account_priority")


	context={

		'member':member,
		'accounts':accounts,
		'return_pk':pk,
		'task_array':task_array,
	'task_enabler_array':task_enabler_array,
	'default_password':default_password,

		}
	return render(request,'deskofficer_templates/Members_Bank_Accounts_edit_details_load.html',context)


def Members_Bank_Accounts_Edit_Prioritization(request,pk):
    record=MembersBankAccounts.objects.get(id=pk)
    MembersBankAccounts.objects.filter(member_id=record.member_id).update(account_priority=1)
    return_pk=record.member_id_id
    record.account_priority=0
    record.save()
    return HttpResponseRedirect(reverse('Members_Bank_Accounts_edit_details_load',args=(return_pk,)))


def Members_Bank_Accounts_update_form(request,pk,return_pk):
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	task_array=[]
	for task in tasks:
		task_array.append(task.task.title)



	task_enabler=TransactionEnabler.objects.filter(status="YES")
	task_enabler_array=[]
	for item in task_enabler:
		task_enabler_array.append(item.title)

	default_password="NO"
	if Staff.objects.filter(admin=request.user,default_password='YES'):
		default_password="YES"


	form=MembersBankAccounts_form(request.POST or None)
	account = MembersBankAccounts.objects.get(id=pk)

	form.fields['banks'].initial= account.bank.id
	form.fields['account_types'].initial=account.account_type
	form.fields['account_name'].initial=account.account_name
	form.fields['account_number'].initial=account.account_number

	if request.method=="POST":
		form=MembersBankAccounts_form(request.POST)
		if form.is_valid():
			bank_id = form.cleaned_data['banks']
			bank=Banks.objects.get(id=bank_id)

			account_type = form.cleaned_data['account_types']

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
		'task_array':task_array,
	'task_enabler_array':task_enabler_array,
	'default_password':default_password,
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
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	task_array=[]
	for task in tasks:
		task_array.append(task.task.title)



	task_enabler=TransactionEnabler.objects.filter(status="YES")
	task_enabler_array=[]
	for item in task_enabler:
		task_enabler_array.append(item.title)

	default_password="NO"
	if Staff.objects.filter(admin=request.user,default_password='YES'):
		default_password="YES"

	title="Search Membership for Next Of Kins"
	form = searchForm(request.POST or None)

	return render(request,'deskofficer_templates/Members_Next_Of_Kins_search.html',{'form':form,'title':title,'task_array':task_array,
	'task_enabler_array':task_enabler_array,
	'default_password':default_password,})


def Members_Next_Of_Kins_list_load(request):
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	task_array=[]
	for task in tasks:
		task_array.append(task.task.title)



	task_enabler=TransactionEnabler.objects.filter(status="YES")
	task_enabler_array=[]
	for item in task_enabler:
		task_enabler_array.append(item.title)

	default_password="NO"
	if Staff.objects.filter(admin=request.user,default_password='YES'):
		default_password="YES"


	title="Members Next Of Kins"
	status="ACTIVE"
	form = searchForm(request.POST)

	if request.method == "POST":
		if request.POST.get("title")=="":
			return HttpResponseRedirect(reverse('Members_Next_Of_Kins_search'))

		# members=Members.objects.filter(Q(phone_number__icontains=form['title'].value()) | Q(admin__first_name__icontains=form['title'].value()) | Q(admin__last_name__icontains=form['title'].value()) | Q(middle_name__icontains=form['title'].value())).filter(status=status)
		members=searchMembers(form['title'].value(),status)

		context={
		'members':members,
		'title':title,
		'task_array':task_array,
	'task_enabler_array':task_enabler_array,
	'default_password':default_password,

		}
		return render(request,'deskofficer_templates/Members_Next_Of_Kins_list_load.html',context)




def addMembersNextOfKins(request,pk):
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	task_array=[]
	for task in tasks:
		task_array.append(task.task.title)



	task_enabler=TransactionEnabler.objects.filter(status="YES")
	task_enabler_array=[]
	for item in task_enabler:
		task_enabler_array.append(item.title)


	default_password="NO"
	if Staff.objects.filter(admin=request.user,default_password='YES'):
		default_password="YES"

	member=Members.objects.get(id=pk)
	title="Add Next Of Kins"
	form=MembersNextOfKins_form(request.POST or None)
	records=MembersNextOfKins.objects.filter(member=member)

	if request.method=="POST":
		form=MembersNextOfKins_form(request.POST)
		status="ACTIVE"
		if form.is_valid():
			if not NextOfKinsMaximun.objects.all().exists():
				messages.error(request,'Next of Kin Maximum missing')
				return HttpResponseRedirect(reverse('addMembersNextOfKins',args=(pk,)))

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

			lock_status='OPEN'
			record=MembersNextOfKins(lock_status=lock_status,status=status,member=member,relationships=relationships,name=name,address=address,phone_number=phone_number)
			record.save()
			messages.success(request,"Record Added Successfully")
			return HttpResponseRedirect(reverse('addMembersNextOfKins',args=(pk,)))


	context={

	'form':form,
	'member':member,
	'title':title,
	'records':records,
	'task_array':task_array,
	'task_enabler_array':task_enabler_array,
	'default_password':default_password,
	}
	return render(request,'deskofficer_templates/addMembersNextOfKins.html',context)


def MembersNextOfKins_lock(request,pk):
	member=Members.objects.get(id=pk)
	lock_status='LOCKED'
	records=MembersNextOfKins.objects.filter(member=member).update(lock_status=lock_status)
	messages.success(request,"Record Locked Successfully")
	return HttpResponseRedirect(reverse('deskofficer_home'))


def MembersNextOfKins_remove(request,pk):
	record=MembersNextOfKins.objects.get(id=pk)
	return_pk=record.member_id
	record.delete()
	messages.success(request,"Record Deleted Successfully")
	return HttpResponseRedirect(reverse('addMembersNextOfKins',args=(return_pk,)))

def Members_Next_Of_Kins_Manage_search(request):
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	task_array=[]
	for task in tasks:
		task_array.append(task.task.title)



	task_enabler=TransactionEnabler.objects.filter(status="YES")
	task_enabler_array=[]
	for item in task_enabler:
		task_enabler_array.append(item.title)

	default_password="NO"
	if Staff.objects.filter(admin=request.user,default_password='YES'):
		default_password="YES"


	title="Search Membership for Next Of Kins"
	form = searchForm(request.POST or None)

	return render(request,'deskofficer_templates/Members_Next_Of_Kins_Manage_search.html',{'form':form,'title':title,'task_array':task_array,
	'task_enabler_array':task_enabler_array,
	'default_password':default_password,})


def Members_Next_Of_Kins_Manage_list_load(request):
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	task_array=[]
	for task in tasks:
		task_array.append(task.task.title)



	task_enabler=TransactionEnabler.objects.filter(status="YES")
	task_enabler_array=[]
	for item in task_enabler:
		task_enabler_array.append(item.title)


	default_password="NO"
	if Staff.objects.filter(admin=request.user,default_password='YES'):
		default_password="YES"

	title="Members Next Of Kins"
	status="ACTIVE"
	form = searchForm(request.POST)

	if request.method == "POST":
		if request.POST.get("title")=="":
			return HttpResponseRedirect(reverse('Members_Next_Of_Kins_Manage_search'))

		members=Members.objects.filter(Q(phone_number__icontains=form['title'].value()) | Q(admin__first_name__icontains=form['title'].value()) | Q(admin__last_name__icontains=form['title'].value()) | Q(middle_name__icontains=form['title'].value())).filter(status=status)

		context={
		'members':members,
		'title':title,
		'task_array':task_array,
	'task_enabler_array':task_enabler_array,
	'default_password':default_password,

		}
		return render(request,'deskofficer_templates/Members_Next_Of_Kins_Manage_list_load.html',context)


def Members_Next_Of_Kins_Manage_NOK_Load(request,pk):
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	task_array=[]
	for task in tasks:
		task_array.append(task.task.title)



	task_enabler=TransactionEnabler.objects.filter(status="YES")
	task_enabler_array=[]
	for item in task_enabler:
		task_enabler_array.append(item.title)


	default_password="NO"
	if Staff.objects.filter(admin=request.user,default_password='YES'):
		default_password="YES"

	member=Members.objects.get(id=pk)
	noks=MembersNextOfKins.objects.filter(member_id=pk)
	title="List of Next Of Kins"

	context={
	'member':member,
	'title':title,
	'noks':noks,
	'member_id':pk,
	'task_array':task_array,
	'task_enabler_array':task_enabler_array,
	'default_password':default_password,
	}
	return render(request,'deskofficer_templates/Members_Next_Of_Kins_Manage_NOK_Load.html',context)




def Members_Next_Of_Kins_Manage_NOK_Update(request,pk,member_id):
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	task_array=[]
	for task in tasks:
		task_array.append(task.task.title)



	task_enabler=TransactionEnabler.objects.filter(status="YES")
	task_enabler_array=[]
	for item in task_enabler:
		task_enabler_array.append(item.title)


	default_password="NO"
	if Staff.objects.filter(admin=request.user,default_password='YES'):
		default_password="YES"

	form=MembersNextOfKins_form(request.POST or None)
	member=Members.objects.get(id=member_id)
	nok=MembersNextOfKins.objects.get(id=pk)
	title="Update Next Of Kins"

	form.fields['relationships'].initial= nok.relationships.id
	form.fields['name'].initial=nok.name
	form.fields['address'].initial=nok.address
	form.fields['phone_number'].initial=nok.phone_number

	if request.method=="POST":
		status="ACTIVE"
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
	'task_array':task_array,
	'task_enabler_array':task_enabler_array,
	'default_password':default_password,
	}
	return render(request,'deskofficer_templates/Members_Next_Of_Kins_Manage_NOK_Update.html',context)



def Members_Without_Next_of_Kin_list_load(request):
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	task_array=[]
	for task in tasks:
		task_array.append(task.task.title)



	task_enabler=TransactionEnabler.objects.filter(status="YES")
	task_enabler_array=[]
	for item in task_enabler:
		task_enabler_array.append(item.title)


	default_password="NO"
	if Staff.objects.filter(admin=request.user,default_password='YES'):
		default_password="YES"

	members=Members.objects.filter(status="ACTIVE")
	k=0
	member_array = []
	for member in members:
		k=k+1
		if MembersNextOfKins.objects.filter(member=member).exists():
			pass
		else:
			member_array.append((member.get_member_Id,member.get_full_name,member.id))


	context={
		'member_array':member_array,

		'task_array':task_array,
		'task_enabler_array':task_enabler_array,
	'default_password':default_password,

		}
	return render(request,'deskofficer_templates/Members_Without_Next_of_Kin_list_load.html',context)


def Members_Without_Next_of_Kin_Update(request,pk):
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	task_array=[]
	for task in tasks:
		task_array.append(task.task.title)



	task_enabler=TransactionEnabler.objects.filter(status="YES")
	task_enabler_array=[]
	for item in task_enabler:
		task_enabler_array.append(item.title)


	default_password="NO"
	if Staff.objects.filter(admin=request.user,default_password='YES'):
		default_password="YES"

	member=Members.objects.get(id=pk)
	title="Add Next Of Kins"
	form=MembersNextOfKins_form(request.POST or None)
	records=MembersNextOfKins.objects.filter(member=member)

	if request.method=="POST":
		form=MembersNextOfKins_form(request.POST)
		status="ACTIVE"
		if form.is_valid():
			if not NextOfKinsMaximun.objects.all().exists():
				messages.error(request,'Next of Kin Maximum missing')
				return HttpResponseRedirect(reverse('Members_Without_Next_of_Kin_Update',args=(pk,)))

			nok_max=NextOfKinsMaximun.objects.first()

			relationships_id=form.cleaned_data['relationships']
			relationships=NOKRelationships.objects.get(id=relationships_id)
			name=form.cleaned_data['name']
			address=form.cleaned_data['address']
			phone_number=form.cleaned_data['phone_number']

			existing_record_count=MembersNextOfKins.objects.filter(member=member).count()

			if int(nok_max.maximun) < int(existing_record_count) + 1:
				messages.error(request,'Total number of allowed Next of Kins exceeded')
				return HttpResponseRedirect(reverse('Members_Without_Next_of_Kin_Update',args=(pk,)))

			if MembersNextOfKins.objects.filter(member=member,relationships=relationships,name=name).exists():
				record_exist=MembersNextOfKins.objects.get(member=member,relationships=relationships,name=name)
				record_exist.address=address
				record_exist.phone_number=phone_number
				record_exist.status=status
				record_exist.save()
				messages.success(request,"Record Updates Successfully")
				return HttpResponseRedirect(reverse('Members_Without_Next_of_Kin_Update',args=(pk,)))

			lock_status='OPEN'
			record=MembersNextOfKins(lock_status=lock_status,status=status,member=member,relationships=relationships,name=name,address=address,phone_number=phone_number)
			record.save()
			messages.success(request,"Record Added Successfully")
			return HttpResponseRedirect(reverse('Members_Without_Next_of_Kin_Update',args=(pk,)))


	context={

	'form':form,
	'member':member,
	'title':title,
	'records':records,
	'task_array':task_array,
	'task_enabler_array':task_enabler_array,
	'default_password':default_password,
	}
	return render(request,'deskofficer_templates/Members_Without_Next_of_Kin_Update.html',context)



def MembersNextOfKins_remove_2(request,pk):
	record=MembersNextOfKins.objects.get(id=pk)
	return_pk=record.member_id
	record.delete()
	messages.success(request,"Record Deleted Successfully")
	return HttpResponseRedirect(reverse('Members_Without_Next_of_Kin_Update',args=(return_pk,)))


###########################################################
################## SALARY UPDATE ##########################
###########################################################

def Members_Salary_Update_request_search(request):
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	task_array=[]
	for task in tasks:
		task_array.append(task.task.title)



	task_enabler=TransactionEnabler.objects.filter(status="YES")
	task_enabler_array=[]
	for item in task_enabler:
		task_enabler_array.append(item.title)


	default_password="NO"
	if Staff.objects.filter(admin=request.user,default_password='YES'):
		default_password="YES"

	title="Search Membership for Salary Update"
	form = searchForm(request.POST or None)

	return render(request,'deskofficer_templates/Members_Salary_Update_request_search.html',{'form':form,'title':title,'task_array':task_array,
	'task_enabler_array':task_enabler_array,
	'default_password':default_password,})


def Members_Salary_Update_Request_list_load(request):
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	task_array=[]
	for task in tasks:
		task_array.append(task.task.title)



	task_enabler=TransactionEnabler.objects.filter(status="YES")
	task_enabler_array=[]
	for item in task_enabler:
		task_enabler_array.append(item.title)


	default_password="NO"
	if Staff.objects.filter(admin=request.user,default_password='YES'):
		default_password="YES"

	title="Members Salary Update"
	status="ACTIVE"
	form = searchForm(request.POST)
	if request.method == "POST":
		if request.POST.get("title")=="":
			return HttpResponseRedirect(reverse('Members_Salary_Update_request_search'))

		# members=Members.objects.filter(Q(phone_number__icontains=form['title'].value()) | Q(admin__first_name__icontains=form['title'].value()) | Q(admin__last_name__icontains=form['title'].value()) | Q(middle_name__icontains=form['title'].value())).filter(status=status)
		members=searchMembers(form['title'].value(),status)

		context={
		'members':members,
		'title':title,
		'task_array':task_array,
	'task_enabler_array':task_enabler_array,
	'default_password':default_password,

		}
		return render(request,'deskofficer_templates/Members_Salary_Update_Request_list_load.html',context)


def Members_Salary_Update_Request_Load(request,pk):
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	task_array=[]
	for task in tasks:
		task_array.append(task.task.title)



	task_enabler=TransactionEnabler.objects.filter(status="YES")
	task_enabler_array=[]
	for item in task_enabler:
		task_enabler_array.append(item.title)


	default_password="NO"
	if Staff.objects.filter(admin=request.user,default_password='YES'):
		default_password="YES"

	form=Members_Salary_Update_Request_form(request.POST or None)
	member=Members.objects.get(id=pk)
	if request.method=="POST":
		status='PENDING'
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
	'task_array':task_array,
	'task_enabler_array':task_enabler_array,
	'default_password':default_password,
	}
	return render(request,'deskofficer_templates/Members_Salary_Update_Request_Load.html',context)


def Members_Salary_Update_Request_approval_Load(request):
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	task_array=[]
	for task in tasks:
		task_array.append(task.task.title)



	task_enabler=TransactionEnabler.objects.filter(status="YES")
	task_enabler_array=[]
	for item in task_enabler:
		task_enabler_array.append(item.title)

	default_password="NO"
	if Staff.objects.filter(admin=request.user,default_password='YES'):
		default_password="YES"

	status="APPROVED"
	processing_status='PROCESSED'
	members=MembersSalaryUpdateRequest.objects.filter(status=status).exclude(processing_status=processing_status)


	context={

	'members':members,
	'task_array':task_array,
	'task_enabler_array':task_enabler_array,
	'default_password':default_password,
	}
	return render(request,'deskofficer_templates/Members_Salary_Update_Request_approval_Load.html',context)


def Members_Salary_Update_Request_process(request,pk):
	processing_status='PROCESSED'
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
################ NORMIAL ROLL UPLOAD #####################
###########################################################

def upload_norminal_roll(request):
	status='UNTREATED'
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	task_array=[]
	for task in tasks:
		task_array.append(task.task.title)



	task_enabler=TransactionEnabler.objects.filter(status="YES")
	task_enabler_array=[]
	for item in task_enabler:
		task_enabler_array.append(item.title)

	default_password="NO"
	if Staff.objects.filter(admin=request.user,default_password='YES'):
		default_password="YES"


	if request.method == 'POST':

		norminal_resource = NorminalRollResource()
		dataset = Dataset()
		new_norminal_roll = request.FILES['myfile']

		if not new_norminal_roll.name.endswith('xlsx'):
			messages.error(request,'Wrong format')
			return HttpResponseRedirect(reverse('upload_norminal_roll'))

		imported_data = dataset.load(new_norminal_roll.read(),format='xlsx')
		for data in imported_data:
			name=list((data[3]).split())
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




			value = NorminalRoll(member_id=data[2],
					file_no=data[1],
					ippis_no=data[1],
					last_name=last_name,
					first_name=first_name,
					middle_name=middle_name,
					phone_no=data[6],
					month=data[4],
					year=data[5],
					date_of_first_appointment=data[7],
					dob=data[8],
					next_of_kin=data[9],
					salary_institution=data[9],
					transaction_status=status,

				)
			value.save()


	context={


	'task_array':task_array,
	'task_enabler_array':task_enabler_array,
	'default_password':default_password,
	}
	return render(request,'deskofficer_templates/upload_norminal.html',context)



def upload_distinct_norminal_roll(request):
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	task_array=[]
	for task in tasks:
		task_array.append(task.task.title)



	task_enabler=TransactionEnabler.objects.filter(status="YES")
	task_enabler_array=[]
	for item in task_enabler:
		task_enabler_array.append(item.title)


	default_password="NO"
	if Staff.objects.filter(admin=request.user,default_password='YES'):
		default_password="YES"

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


	'task_array':task_array,
	'task_enabler_array':task_enabler_array,
	'default_password':default_password,
	}
	return render(request,'deskofficer_templates/upload_norminal.html',context)


def Norminal_Roll_Preview(request):
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	task_array=[]
	for task in tasks:
		task_array.append(task.task.title)



	task_enabler=TransactionEnabler.objects.filter(status="YES")
	task_enabler_array=[]
	for item in task_enabler:
		task_enabler_array.append(item.title)

	default_password="NO"
	if Staff.objects.filter(admin=request.user,default_password='YES'):
		default_password="YES"

	transaction_status="UNTREATED"
	records=NorminalRoll.objects.filter(transaction_status=transaction_status)


	context={
	'records':records,
	'task_array':task_array,
	'task_enabler_array':task_enabler_array,
	'default_password':default_password,
	}
	return render(request,'deskofficer_templates/Norminal_Roll_Preview.html',context)


def Norminal_Roll_Process(request):
	prefix=MembersIdManager.objects.first()
	tdate=get_current_date(now)
	processed_by=CustomUser.objects.get(id=request.user.id)
	if not AutoReceipt.objects.all().exists():
		messages.error(request,'Receipt not Set')
		return HttpResponseRedirect(reverse('Norminal_Roll_Preview'))

	approval_status='APPROVED'
	submission_status="SUBMITTED"
	transaction_status="UNTREATED"
	transaction_status1="TREATED"
	cashbook_status="UNPOSTED"
	status="ACTIVE"
	savings_status='PENDING'
	loan_status='PENDING'
	shares_status='PENDING'
	welfare_status='PENDING'
	date_joined_status='UPLOADED'
	dob_status='UPLOADED'
	date_of_first_appointment_status='UPLOADED'
	approval_comment="APPROVED"


	approval_officer=CustomUser.objects.get(id=request.user.id)
	MemberShipRequest.objects.all().delete()

	records=NorminalRoll.objects.filter(transaction_status=transaction_status)

	for record in records:
		file_no = str(record.file_no).zfill(5)
		ippis_no = str(record.ippis_no).zfill(5)
		phone_number = str(record.phone_no).zfill(11)

		if Members.objects.filter(Q(file_no=file_no) | Q(ippis_no=ippis_no) | Q(phone_number=phone_number)).exists():
			messages.error(request,'Duplicate records appearing')
			return HttpResponseRedirect(reverse('Norminal_Roll_Preview'))

	for record in records:
		file_no = str(record.file_no).zfill(5)
		ippis_no = str(record.ippis_no).zfill(5)
		first_name=record.first_name
		last_name=record.last_name
		middle_name=record.middle_name
		date_of_first_appointment=record.date_of_first_appointment
		next_of_kin=record.next_of_kin
		dob=record.dob
		phone_number = str(record.phone_no).zfill(11)
		month=record.month
		year = record.year

		member_id = prefix.prefix_title + "/" +  str(year) + '/' + str(record.member_id).zfill(5)

		salary_institution = SalaryInstitution.objects.get(id=record.salary_institution)

		# month_list =['JANUARY','FEBRUARY','MARCH','APRIL','MAY','JUNE','JULY','AUGUST','SEPTEMBER','OCTOBER','NOVEMBER','DECEMBER']
		approved_date=date(int(year),int(month_list.index(month))+1,1)

		item=MemberShipRequest(submission_status=submission_status,
			transaction_status=transaction_status1,
			first_name=first_name,last_name=last_name,
			middle_name=middle_name,phone_number=phone_number,
			approval_officer=approval_officer.username,
			approval_status=approval_status,
			approval_comment=approval_comment,
			salary_institution=salary_institution,
			file_no=file_no,
			ippis_no=ippis_no,
			member_id=member_id,
			month=month,
			year=year,
			date_of_first_appointment=date_of_first_appointment,
			dob=dob,
			next_of_kin=next_of_kin,
			tdate=tdate,
			approved_date=approved_date,

			)
		item.save()

		record.transaction_status=transaction_status1
		record.save()

	applicants = MemberShipRequest.objects.filter(transaction_status=transaction_status1)
	for applicant in applicants:

		receipt_obj=AutoReceipt.objects.first()
		receipt='C-' + str(receipt_obj.receipt.zfill(5))

		record=MemberShipFormSalesRecord(date_paid=approved_date,cashbook_status=cashbook_status,tdate=tdate,applicant=applicant,receipt=receipt,processed_by=processed_by.username,status=transaction_status)
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
		date_joined = applicant.applicant.approved_date
		date_of_first_appointment = applicant.applicant.date_of_first_appointment
		dob = applicant.applicant.dob


		user = CustomUser.objects.create_user(username=username,password=password,email=email,last_name=last_name,first_name=first_name,user_type=int(user_type))
		user.members.applicant=applicant
		user.members.member_id=member_id
		user.members.middle_name=middle_name
		user.members.full_name=str(first_name) + ' ' + str(last_name) + ' ' + str(middle_name)
		user.members.phone_number=phone_number
		user.members.salary_institution=salary_institution
		user.members.file_no=file_no
		user.members.ippis_no=ippis_no
		user.members.date_joined=date_joined
		user.members.status=status
		user.members.savings_status=savings_status
		user.members.loan_status=loan_status
		user.members.shares_status=shares_status
		user.members.welfare_status=welfare_status

		user.members.date_of_first_appointment=date_of_first_appointment
		user.members.dob=dob

		user.members.date_joined_status=date_joined_status
		user.members.date_of_first_appointment_status=date_of_first_appointment_status
		user.members.dob_status=dob_status
		user.save()

		applicant.status=transaction_status1
		applicant.save()

	return HttpResponseRedirect(reverse('Norminal_Roll_Preview'))


def Individual_Capture(request):
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	task_array=[]
	for task in tasks:
		task_array.append(task.task.title)

	task_enabler=TransactionEnabler.objects.filter(status="YES")
	task_enabler_array=[]
	for item in task_enabler:
		task_enabler_array.append(item.title)

	default_password="NO"
	if Staff.objects.filter(admin=request.user,default_password='YES'):
		default_password="YES"

	prefix=MembersIdManager.objects.first()
	tdate=get_current_date(now)
	processed_by=CustomUser.objects.get(id=request.user.id)

	approval_status='APPROVED'
	submission_status="SUBMITTED"
	transaction_status="UNTREATED"
	transaction_status1="TREATED"
	cashbook_status="UNPOSTED"
	status="ACTIVE"
	savings_status='PENDING'
	loan_status='PENDING'
	shares_status='PENDING'
	welfare_status='PENDING'
	date_joined_status='UPLOADED'
	dob_status='UPLOADED'
	date_of_first_appointment_status='UPLOADED'


	approval_officer=CustomUser.objects.get(id=request.user.id)
	approval_comment="APPROVED"


	form=Individual_Capture_Form(request.POST or None)
	if request.method == "POST":
		title_id=request.POST.get('title')
		title=Titles.objects.get(id=title_id)
		dob=request.POST.get('dob')
		chk_dob=request.POST.get('chk-dob')
		date_hired=request.POST.get('date_hired')
		chk_fappt=request.POST.get('chk-fappt')
		file_no=request.POST.get('file_no')
		ippis_no=request.POST.get('ippis_no')
		coop_no=request.POST.get('coop_no')
		last_name=request.POST.get('last_name')
		first_name=request.POST.get('first_name')
		middle_name=request.POST.get('middle_name')
		phone_number=request.POST.get('phone_number')
		year=request.POST.get('year_joined')
		month=request.POST.get('month_joined')
		salary_institution_id=request.POST.get('salary_institution')
		salary_institution=SalaryInstitution.objects.get(id=salary_institution_id)

		member_id = prefix.prefix_title + "/" +  str(year) + '/' + str(coop_no).zfill(5)

		# month_list =['JANUARY','FEBRUARY','MARCH','APRIL','MAY','JUNE','JULY','AUGUST','SEPTEMBER','OCTOBER','NOVEMBER','DECEMBER']
		approved_date=date(int(year),int(month_list.index(month))+1,1)
		date_joined=date(int(year),int(month_list.index(month))+1,1)



		item=MemberShipRequest(title=title,submission_status=submission_status,
			transaction_status=transaction_status1,
			first_name=first_name,last_name=last_name,
			middle_name=middle_name,phone_number=phone_number,
			approval_officer=approval_officer.username,
			approval_status=approval_status,
			approval_comment=approval_comment,
			salary_institution=salary_institution,
			file_no=file_no,
			ippis_no=ippis_no,
			member_id=member_id,
			month=month,
			year=year,

			tdate=tdate,
			approved_date=approved_date)
		item.save()

		if chk_dob:
			item.dob=dob
			item.save()

		if chk_fappt:
			item.date_of_first_appointment=date_hired
			item.save()


		applicant = item


		receipt_obj=AutoReceipt.objects.first()
		receipt='C-' + str(receipt_obj.receipt.zfill(5))

		record=MemberShipFormSalesRecord(cashbook_status=cashbook_status,tdate=tdate,applicant=applicant,receipt=receipt,processed_by=processed_by.username,status=transaction_status1,date_paid=tdate)
		record.save()

		receipt_obj.receipt=int(receipt_obj.receipt) + 1
		receipt_obj.save()


		default_password = DefaultPassword.objects.first()
		password=default_password.title
		user_type_obj = UserType.objects.get(title='MEMBERS')
		user_type=user_type_obj.code

		username = first_name + last_name + str(file_no).zfill(5)
		email = first_name + str(file_no).zfill(5) + "@gmail.com"


		user = CustomUser.objects.create_user(username=username,password=password,email=email,last_name=last_name,first_name=first_name,user_type=int(user_type))
		user.members.applicant=record
		user.members.member_id=member_id
		user.members.title=title
		user.members.middle_name=middle_name
		user.members.full_name=str(first_name) + ' ' + str(last_name) + ' ' + str(middle_name)
		user.members.phone_number=phone_number
		user.members.salary_institution=salary_institution
		user.members.file_no=file_no
		user.members.ippis_no=ippis_no
		user.members.date_joined=date_joined

		user.members.status=status
		user.members.savings_status=savings_status
		user.members.loan_status=loan_status
		user.members.shares_status=shares_status
		user.members.welfare_status=welfare_status

		user.members.date_of_first_appointment=date_hired
		user.members.dob=dob

		user.members.date_joined_status=date_joined_status

		if chk_fappt:
			user.members.date_of_first_appointment_status=date_of_first_appointment_status

		if chk_dob:
			user.members.dob_status=dob_status

		user.save()

		transactions=TransactionTypes.objects.filter(~Q(source__title="LOAN") & ~Q(source__title='GENERAL') & ~Q(code='701'))

		count=0

		for transaction in transactions:
			account_number=str(transaction.code) + str(coop_no).zfill(5)
			if MembersAccountsDomain.objects.filter(member=user.members,transaction=transaction,account_number=account_number).exists():
				pass
			else:
				count +=1
				record=MembersAccountsDomain(status=status,member=user.members,transaction=transaction,account_number=account_number)
				record.save()

		return HttpResponseRedirect(reverse("Individual_Capture"))

	form.fields['dob'].initial = now
	form.fields['date_hired'].initial = now
	context={
	'form':form,
	# 'records':records,
	'task_array':task_array,
	'task_enabler_array':task_enabler_array,
	'default_password':default_password,
	}
	return render(request,'deskofficer_templates/Individual_Capture.html',context)


def Individual_Capture_Delete_Search(request):
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	task_array=[]
	for task in tasks:
		task_array.append(task.task.title)

	task_enabler=TransactionEnabler.objects.filter(status="YES")
	task_enabler_array=[]
	for item in task_enabler:
		task_enabler_array.append(item.title)

	default_password="NO"
	if Staff.objects.filter(admin=request.user,default_password='YES'):
		default_password="YES"

	title="Search Members for Ledger Information"
	form = searchForm(request.POST or None)

	return render(request,'deskofficer_templates/Individual_Capture_Delete_Search.html',{'form':form,'title':title,'task_array':task_array,
	'task_enabler_array':task_enabler_array,
	'default_password':default_password,
	})


def Individual_Capture_Delete_List_load(request):
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	task_array=[]
	for task in tasks:
		task_array.append(task.task.title)

	task_enabler=TransactionEnabler.objects.filter(status="YES")
	task_enabler_array=[]
	for item in task_enabler:
		task_enabler_array.append(item.title)


	default_password="NO"
	if Staff.objects.filter(admin=request.user,default_password='YES'):
		default_password="YES"

	title="LIST OF MEMBERS"
	form = searchForm(request.POST)
	status="ACTIVE"


	if request.method == "POST":
		if request.POST.get("title")=="":
			messages.info(request,"Please Enter a search data")
			return HttpResponseRedirect(reverse('Uploading_Existing_Savings_Search'))

		records=Members.objects.filter(Q(file_no__icontains=form['title'].value()) |Q(ippis_no__icontains=form['title'].value()) |Q(phone_number__icontains=form['title'].value()) | Q(admin__first_name__icontains=form['title'].value()) | Q(admin__last_name__icontains=form['title'].value()) | Q(middle_name__icontains=form['title'].value())).filter(status=status)
		if records.count() <= 0:
			messages.info(request,"No Record Found")
			return HttpResponseRedirect(reverse('Uploading_Existing_Savings_Search'))

		context={
		'records':records,
		'title':title,
		'task_array':task_array,
		'task_enabler_array':task_enabler_array,
	'default_password':default_password,
		}
		return render(request,'deskofficer_templates/Individual_Capture_Delete_List_load.html',context)


def Individual_Capture_Delete(request,pk):
	member=Members.objects.get(id=pk)
	member_id=member.admin_id
	file_no=member.file_no
	MemberShipRequest.objects.filter(file_no=file_no).delete()
	CustomUser.objects.filter(id=member_id).delete()
	return HttpResponseRedirect(reverse('Individual_Capture_Delete_Search'))



############################################################################
################# UPLOADING EXISTING SAVINGS ###############################
############################################################################
def Uploading_Existing_Savings_Search(request):
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	task_array=[]
	for task in tasks:
		task_array.append(task.task.title)

	task_enabler=TransactionEnabler.objects.filter(status="YES")
	task_enabler_array=[]
	for item in task_enabler:
		task_enabler_array.append(item.title)

	default_password="NO"
	if Staff.objects.filter(admin=request.user,default_password='YES'):
		default_password="YES"

	title="Search Members for Savings Upload"
	form = searchForm(request.POST or None)

	return render(request,'deskofficer_templates/Uploading_Existing_Savings_Search.html',{'form':form,'title':title,'task_array':task_array,
	'task_enabler_array':task_enabler_array,
	'default_password':default_password,
	})


def Uploading_Existing_Savings_List_load(request):
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	task_array=[]
	for task in tasks:
		task_array.append(task.task.title)

	task_enabler=TransactionEnabler.objects.filter(status="YES")
	task_enabler_array=[]
	for item in task_enabler:
		task_enabler_array.append(item.title)

	default_password="NO"
	if Staff.objects.filter(admin=request.user,default_password='YES'):
		default_password="YES"


	title="LIST OF MEMBERS"
	form = searchForm(request.POST)
	status="ACTIVE"
	savings_status='PENDING'

	if request.method == "POST":
		if request.POST.get("title")=="":
			messages.info(request,"Please Enter a search data")
			return HttpResponseRedirect(reverse('Uploading_Existing_Savings_Search'))

		records=Members.objects.filter(Q(member_id__icontains=form['title'].value()) | Q(admin__first_name__icontains=form['title'].value()) | Q(admin__last_name__icontains=form['title'].value()) | Q(middle_name__icontains=form['title'].value())).filter(status=status,savings_status=savings_status,member_category="OLD")
		if records.count() <= 0:
			messages.info(request,"No Record Found")
			return HttpResponseRedirect(reverse('Uploading_Existing_Savings_Search'))

		context={
		'records':records,
		'title':title,
		'task_array':task_array,
		'task_enabler_array':task_enabler_array,
	'default_password':default_password,
		}
		return render(request,'deskofficer_templates/Uploading_Existing_Savings_List_load.html',context)


def Uploading_Existing_Savings_Preview(request,pk):
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	task_array=[]
	for task in tasks:
		task_array.append(task.task.title)

	task_enabler=TransactionEnabler.objects.filter(status="YES")
	task_enabler_array=[]
	for item in task_enabler:
		task_enabler_array.append(item.title)

	default_password="NO"
	if Staff.objects.filter(admin=request.user,default_password='YES'):
		default_password="YES"

	form=Uploading_Existing_Savings_form(request.POST or None)
	member_id=Members.objects.get(id=pk)

	records=SavingsUploaded.objects.filter(transaction__member=member_id)
	transaction_status='UNTREATED'
	status="ACTIVE"

	if TransactionPeriods.objects.filter(status=status).exists():
		transaction_period=TransactionPeriods.objects.get(status=status)
		transaction_period= get_current_date(transaction_period.transaction_period)

	else:
		transaction_period=now


	if request.method=="POST":
		processed_by=CustomUser.objects.get(id=request.user.id)
		transaction_period_id=request.POST.get('transaction_period')


		date_format = '%Y-%m-%d'
		dtObj = datetime.datetime.strptime(transaction_period_id, date_format)
		transaction_period=get_current_date(dtObj)

			
		balance=request.POST.get('balance')
		schedule_amount=request.POST.get('schedule_amount')

		transaction_id=request.POST.get('transactions')
		transaction=TransactionTypes.objects.get(id=transaction_id)
		
		formatted_date = defaultfilters.date(transaction_period, "SHORT_DATE_FORMAT")
		particulars="Balance Brought Forward as at " + str(formatted_date)




		standing_order=request.POST.get('standing_order')
	
		if standing_order:		
			saving = transaction

			account_number=[]
			if MembersAccountsDomain.objects.filter(member=member_id,transaction=saving).exists():
				account_number=MembersAccountsDomain.objects.get(member=member_id,transaction=saving)
			else:
				account_number=MembersAccountsDomain(member=member_id,transaction=saving,account_number=str(saving.code) + str(member_id.get_member_Id),status='ACTIVE',loan_lock='YES',processed_by=processed_by.username)
				account_number.save()


			if account_number:
				amount=schedule_amount

				minimum_amount = saving.minimum_amount

				if float(amount)<=0:
					messages.error(request,"Amount  cannot be zero(0)")
					return HttpResponseRedirect(reverse('Uploading_Existing_Savings_Preview',args=(pk,)))


				if float(amount)<float(minimum_amount):
					messages.error(request,"Amount Specified is Less than " + str(minimum_amount) + " Minimum Amount allowed for this Transaction")
					return HttpResponseRedirect(reverse('Uploading_Existing_Savings_Preview',args=(pk,)))

				if StandingOrderAccounts.objects.filter(transaction=account_number).exists():
					member=StandingOrderAccounts.objects.get(transaction=account_number)
					if member.lock_status.title == 'OPEN':
						member.amount=amount
						processed_by=processed_by.username
						member.save()
					else:
						messages.error(request,"This Transaction is Locked, Update not Allowed from this point")
					return HttpResponseRedirect(reverse('Uploading_Existing_Savings_Preview',args=(pk,)))


				member=StandingOrderAccounts(lock_status='LOCKED',status='ACTIVE',transaction=account_number,amount=amount,processed_by=processed_by.username)
				member.save()
				messages.success(request,"Standing order Created Successfully, To view it, Kindly visit the Membr's Dashboard")
				return HttpResponseRedirect(reverse('Uploading_Existing_Savings_Preview',args=(pk,)))

			else:
				messages.error(request,"Account Number not Found")
				return HttpResponseRedirect(reverse('Uploading_Existing_Savings_Preview',args=(pk,)))

		else:
			
			
			if float(balance)<=0:
				messages.error(request,"Balance Brought Forward must be greater than zero")
				return HttpResponseRedirect(reverse('Uploading_Existing_Savings_Preview',args=(pk,)))

			if MembersAccountsDomain.objects.filter(member=member_id,transaction=transaction).exists():
				member=MembersAccountsDomain.objects.get(member=member_id,transaction=transaction)
			else:
				member=MembersAccountsDomain(member=member_id,transaction=transaction,account_number=str(transaction.code) + str(member_id.get_member_Id),status='ACTIVE',loan_lock='YES')
				member.save()
				# return HttpResponseRedirect(reverse('Uploading_Existing_Savings_Preview',args=(pk,)))


			if SavingsUploaded.objects.filter(transaction=member).exists():
				record=SavingsUploaded.objects.get(transaction=member)
				record.delete()

				record=SavingsUploaded(transaction=member,particulars=particulars,balance=balance,schedule_amount=schedule_amount,processed_by=processed_by.username,status=transaction_status,transaction_period=transaction_period)
				record.save()
				messages.success(request,"Record Updated Successfully")
			else:
				record=SavingsUploaded(transaction=member,particulars=particulars,balance=balance,schedule_amount=schedule_amount,processed_by=processed_by.username,status=transaction_status,transaction_period=transaction_period)
				record.save()
				messages.success(request,"Record Addedd Successfully")

		return HttpResponseRedirect(reverse('Uploading_Existing_Savings_Preview',args=(pk,)))

	t_period= get_current_date(transaction_period)
	form.fields['transaction_period'].initial = t_period
	context={
	'member':member_id,
	'form':form,
	'records':records,
	'return_pk':pk,
	'task_array':task_array,
	'task_enabler_array':task_enabler_array,
	'default_password':default_password,
	}
	return render(request,'deskofficer_templates/Uploading_Existing_Savings_Preview.html',context)


def Uploading_Existing_Savings_validate(request,pk):
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	task_array=[]
	for task in tasks:
		task_array.append(task.task.title)

	task_enabler=TransactionEnabler.objects.filter(status="YES")
	task_enabler_array=[]
	for item in task_enabler:
		task_enabler_array.append(item.title)

	default_password="NO"
	if Staff.objects.filter(admin=request.user,default_password='YES'):
		default_password="YES"

	lock_status='LOCKED'
	savings_status='UPLOADED'
	status='UNTREATED'

	status1='ACTIVE'
	# transaction_period=TransactionPeriods.objects.get(status=status1)

	member=Members.objects.get(id=pk)
	tdate=get_current_date(now)

	if SavingsUploaded.objects.filter(transaction__member=member,status=status).exists():


		records=SavingsUploaded.objects.filter(transaction__member=member,status=status)

		for item in records:
			transaction_id=item.transaction.transaction_id
			transaction=TransactionTypes.objects.get(id=transaction_id)

			transaction_period=item.transaction_period
			particulars=item.particulars
			debit=0
			credit=item.balance
			balance=item.balance
			schedule_amount=item.schedule_amount
			account_number=str(item.transaction.account_number)

			if MembersAccountsDomain.objects.filter(account_number=account_number).count()>1:
				member_selected=MembersAccountsDomain.objects.filter(account_number=account_number).first()
			else:
				member_selected=MembersAccountsDomain.objects.get(account_number=account_number)

			# MembersAccountsDomain.objects.exclude(id=member_selected.id).delete()

			if PersonalLedger.objects.filter(member=member,transaction=transaction,account_number=account_number).exists():
				messages.success(request,"Record Already Uploaded for this Member, Consult the Administrator")
				return HttpResponseRedirect(reverse('Uploading_Existing_Savings_Preview',args=(pk,)))
			else:
				post_to_ledger(
							member,
							transaction,
							account_number,
							particulars,
							debit,
							credit,
							balance,
							transaction_period,
							status1,
							tdate
							)

			if StandingOrderAccounts.objects.filter(transaction=member_selected).exists():
				standing_order=StandingOrderAccounts.objects.get(transaction=member_selected)
				standing_order.amount=schedule_amount
				standing_order.lock_status=lock_status
				standing_order.save()

			else:

				standing_order=StandingOrderAccounts(transaction=member_selected,amount=schedule_amount,lock_status=lock_status,status=status1)
				standing_order.save()


			transaction_status='TREATED'

			item.status=transaction_status
			item.save()

		member.savings_status=savings_status
		member.save()

		messages.success(request,"Record Validated Successfully")
	else:
		messages.error(request,"No Record Found")
	return HttpResponseRedirect(reverse('Uploading_Existing_Savings_Search'))



def Uploading_Existing_Savings_delete(request,pk,return_pk):
	record=SavingsUploaded.objects.get(id=pk)
	record.delete()
	return HttpResponseRedirect(reverse('Uploading_Existing_Savings_Preview',args=(return_pk,)))







def Uploading_Existing_Savings_All_List_load(request):
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	task_array=[]
	for task in tasks:
		task_array.append(task.task.title)

	task_enabler=TransactionEnabler.objects.filter(status="YES")
	task_enabler_array=[]
	for item in task_enabler:
		task_enabler_array.append(item.title)

	default_password="NO"
	if Staff.objects.filter(admin=request.user,default_password='YES'):
		default_password="YES"


	title="LIST OF MEMBERS"

	savings_status='PENDING'


	records=Members.objects.all()

	context={
	'records':records,
	'title':title,
	'task_array':task_array,
	'task_enabler_array':task_enabler_array,
	'default_password':default_password,
	}
	return render(request,'deskofficer_templates/Uploading_Existing_Savings_All_List_load.html',context)


def Uploading_Existing_Savings_Preview_All(request,pk):
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	task_array=[]
	for task in tasks:
		task_array.append(task.task.title)

	task_enabler=TransactionEnabler.objects.filter(status="YES")
	task_enabler_array=[]
	for item in task_enabler:
		task_enabler_array.append(item.title)

	default_password="NO"
	if Staff.objects.filter(admin=request.user,default_password='YES'):
		default_password="YES"

	form=Uploading_Existing_Savings_form(request.POST or None)
	member_id=Members.objects.get(id=pk)

	records=SavingsUploaded.objects.filter(transaction__member=member_id)
	

	transaction_status='UNTREATED'
	status="ACTIVE"



	context={
	'member':member_id,
	
	'records':records,
	'return_pk':pk,
	'task_array':task_array,
	'task_enabler_array':task_enabler_array,
	'default_password':default_password,
	}
	return render(request,'deskofficer_templates/Uploading_Existing_Savings_Preview_All.html',context)




def Uploading_Existing_Savings_delete_All(request,pk,return_pk):
	record=SavingsUploaded.objects.get(id=pk)
	record.delete()
	member=Members.objects.get(id=return_pk)
	if SavingsUploaded.objects.filter(transaction__member=member).exists():
		pass
	else:
		member.savings_status='PENDING'
		member.save()
	return HttpResponseRedirect(reverse('Uploading_Existing_Savings_Preview_All',args=(return_pk,)))


def Uploading_Existing_Savings_Discard_All(request,pk):
	member=Members.objects.get(id=pk)
	SavingsUploaded.objects.filter(transaction__member=member).delete()
	member.savings_status='PENDING'
	member.save()
	return HttpResponseRedirect(reverse('Uploading_Existing_Savings_Preview_All',args=(pk,)))



def Uploading_Existing_Savings_Done_Transaction_Date_Update(request):
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	task_array=[]
	for task in tasks:
		task_array.append(task.task.title)

	task_enabler=TransactionEnabler.objects.filter(status="YES")
	task_enabler_array=[]
	for item in task_enabler:
		task_enabler_array.append(item.title)

	default_password="NO"
	if Staff.objects.filter(admin=request.user,default_password='YES'):
		default_password="YES"

	status="ACTIVE"

	if TransactionPeriods.objects.filter(status=status).exists():
		transaction_period=TransactionPeriods.objects.get(status=status)
		transaction_period=transaction_period.transaction_period
	else:
		transaction_period=now


	form=Uploading_Existing_Savings_form(request.POST or None)

	records=SavingsUploaded.objects.all()
	if request.method == 'POST':
		tdate_status=request.POST.get('t-date')
		
		date_format = '%Y-%m-%d'
		

		transaction_period_id=request.POST.get('transaction_period')
		dtObj = datetime.datetime.strptime(transaction_period_id, date_format)
		transaction_period=get_current_date(dtObj)
		
		if tdate_status:
			tdate_id=request.POST.get('tdate')
			dtObj = datetime.datetime.strptime(tdate_id, date_format)
			tdate=get_current_date(dtObj)

			SavingsUploaded.objects.all().update(tdate=tdate,transaction_period=transaction_period)
		
			particulars = f"Balance Brought Forward as at {transaction_period}"
			for record in records:
				PersonalLedger.objects.filter(account_number=record.transaction.account_number).update(transaction_period=transaction_period,tdate=tdate,particulars=particulars)
		

		else:

			SavingsUploaded.objects.all().update(transaction_period=transaction_period)
		

			particulars = f"Balance Brought Forward as at {transaction_period}"
			for record in records:
				PersonalLedger.objects.filter(account_number=record.transaction.account_number).update(transaction_period=transaction_period,particulars=particulars)
			

		return HttpResponseRedirect(reverse('Uploading_Existing_Savings_Done_Transaction_Date_Update'))
	form.fields['transaction_period'].initial = get_current_date(transaction_period)
	form.fields['tdate'].initial = get_current_date(now)
	context={
	'records':records,
	'form':form,
	'task_array':task_array,
	'task_enabler_array':task_enabler_array,
	'default_password':default_password,
	}
	return render(request,'deskofficer_templates/Uploading_Existing_Savings_Done_Transaction_Date_Update.html',context)



def Uploading_Existing_Savings_Done_List_Select_Period(request):
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	task_array=[]
	for task in tasks:
		task_array.append(task.task.title)

	task_enabler=TransactionEnabler.objects.filter(status="YES")
	task_enabler_array=[]
	for item in task_enabler:
		task_enabler_array.append(item.title)

	default_password="NO"
	if Staff.objects.filter(admin=request.user,default_password='YES'):
		default_password="YES"

	form = Uploading_Existing_Savings_Done_List_Select_Period_Form(request.POST or None)
	if request.method == "POST":
		date_format = '%Y-%m-%d'
		
		tdate_id=request.POST.get('tdate')
		dtObj = datetime.datetime.strptime(tdate_id, date_format)
		tdate=get_current_date(dtObj)

		transaction_period=request.POST.get('transaction_range')
		
		return HttpResponseRedirect(reverse('Uploading_Existing_Savings_Done_List_load', args=(transaction_period,tdate,)))
	

	form.fields['tdate'].initial=get_current_date(now)
	context={
	'form':form,
	# 'member_array':member_array,
	# 'title':title,
	'task_array':task_array,
	'task_enabler_array':task_enabler_array,
	'default_password':default_password,
	}
	return render(request,'deskofficer_templates/Uploading_Existing_Savings_Done_List_Select_Period.html',context)




def Uploading_Existing_Savings_Done_List_load(request,transaction_period,tdate):
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	task_array=[]
	for task in tasks:
		task_array.append(task.task.title)

	task_enabler=TransactionEnabler.objects.filter(status="YES")
	task_enabler_array=[]
	for item in task_enabler:
		task_enabler_array.append(item.title)

	default_password="NO"
	if Staff.objects.filter(admin=request.user,default_password='YES'):
		default_password="YES"



	title="LIST OF MEMBERS"

	savings_status='UPLOADED'

	if transaction_period == 'ALL RECORDS':
		# queryset=SavingsUploaded.objects.filter().order_by('transaction__member__member_id').values_list('transaction__member__member_id','transaction__member__admin__last_name','transaction__member__admin__first_name','transaction__member__middle_name','transaction__member__ippis_no','processed_by','tdate').distinct()
		queryset=SavingsUploaded.objects.filter().order_by('transaction__member__member_id').values_list('transaction__member__member_id','transaction__member__admin__last_name','transaction__member__admin__first_name','transaction__member__middle_name','transaction__member__ippis_no','processed_by','tdate').distinct()
	
	elif transaction_period == 'SELECTED DATE':

		date_format = '%Y-%m-%d'
		dtObj = datetime.datetime.strptime(tdate, date_format)
		t_date=get_current_date(dtObj)

		queryset=SavingsUploaded.objects.filter(Q(tdate__year=t_date.year,tdate__month=t_date.month,tdate__day=t_date.day)).order_by('transaction__member__member_id').values_list('transaction__member__member_id','transaction__member__admin__last_name','transaction__member__admin__first_name','transaction__member__middle_name','transaction__member__ippis_no','processed_by','tdate').distinct()
		
	member_array = []
	for query in queryset:
		member_array.append((query[0][13:],query[1],query[2],query[3],query[4],query[5],get_current_date(query[6])))

	context={
	# 'records':records,
	'member_array':member_array,
	'title':title,
	'task_array':task_array,
	'task_enabler_array':task_enabler_array,
	'default_password':default_password,
	}
	return render(request,'deskofficer_templates/Uploading_Existing_Savings_Done_List_load.html',context)


def Uploading_Existing_Savings_Done_View_Details(request,pk):
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	task_array=[]
	for task in tasks:
		task_array.append(task.task.title)

	task_enabler=TransactionEnabler.objects.filter(status="YES")
	task_enabler_array=[]
	for item in task_enabler:
		task_enabler_array.append(item.title)

	default_password="NO"
	if Staff.objects.filter(admin=request.user,default_password='YES'):
		default_password="YES"




	records=SavingsUploaded.objects.filter(transaction__member__ippis_no=pk)
	print(pk)
	member=Members.objects.get(ippis_no=pk)

	context={
	'records':records,
	'member':member,
	'task_array':task_array,
	'task_enabler_array':task_enabler_array,
	'default_password':default_password,
	}
	return render(request,'deskofficer_templates/Uploading_Existing_Savings_Done_View_Details.html',context)



##################################################################
###################### Additional Savings Upload #################
###################################################################
def Uploading_Existing_Savings_Additional_search(request):
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	task_array=[]
	for task in tasks:
		task_array.append(task.task.title)



	task_enabler=TransactionEnabler.objects.filter(status="YES")
	task_enabler_array=[]
	for item in task_enabler:
		task_enabler_array.append(item.title)


	default_password="NO"
	if Staff.objects.filter(admin=request.user,default_password='YES'):
		default_password="YES"

	title="Search Members for Savings Upload"
	form = searchForm(request.POST or None)

	return render(request,'deskofficer_templates/Uploading_Existing_Savings_Additional_search.html',{'form':form,'title':title,'task_array':task_array,
	'task_enabler_array':task_enabler_array,
	'default_password':default_password,})


def Uploading_Existing_Savings_Additional_list_load(request):
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	task_array=[]
	for task in tasks:
		task_array.append(task.task.title)



	task_enabler=TransactionEnabler.objects.filter(status="YES")
	task_enabler_array=[]
	for item in task_enabler:
		task_enabler_array.append(item.title)


	default_password="NO"
	if Staff.objects.filter(admin=request.user,default_password='YES'):
		default_password="YES"

	title="LIST OF MEMBERS FOR SAVINGS UPLOAD"
	status="ACTIVE"
	savings_status='PENDING'

	form = searchForm(request.POST)
	if request.method == "POST":
		if request.POST.get("title")=="":
			return HttpResponseRedirect(reverse('Uploading_Existing_Savings_Additional_search'))

		members=Members.objects.filter(Q(file_no__icontains=form['title'].value()) |Q(ippis_no__icontains=form['title'].value()) |Q(phone_number__icontains=form['title'].value()) | Q(admin__first_name__icontains=form['title'].value()) | Q(admin__last_name__icontains=form['title'].value()) | Q(middle_name__icontains=form['title'].value())).filter(status=status).filter(~Q(savings_status=savings_status))

		context={
		'members':members,
		'title':title,
		'task_array':task_array,
	'task_enabler_array':task_enabler_array,
	'default_password':default_password,

		}
		return render(request,'deskofficer_templates/Uploading_Existing_Savings_Additional_list_load.html',context)


def Uploading_Existing_Savings_Additional_Preview(request,pk):
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	task_array=[]
	for task in tasks:
		task_array.append(task.task.title)



	task_enabler=TransactionEnabler.objects.filter(status="YES")
	task_enabler_array=[]
	for item in task_enabler:
		task_enabler_array.append(item.title)

	default_password="NO"
	if Staff.objects.filter(admin=request.user,default_password='YES'):
		default_password="YES"

	form=Uploading_Existing_Savings_form(request.POST or None)
	member=Members.objects.get(id=pk)
	records=SavingsUploaded.objects.filter(transaction__member=member)
	transaction_status='UNTREATED'
	status="ACTIVE"

	if TransactionPeriods.objects.filter(status=status).exists():
		transaction_period=TransactionPeriods.objects.get(status=status)
		transaction_period=transaction_period.transaction_period
	else:
		transaction_period=now

	if request.method=="POST":
		transaction_period_id=request.POST.get('transaction_period')
		date_format = '%Y-%m-%d'
		dtObj = datetime.datetime.strptime(transaction_period_id, date_format)
		transaction_period=get_current_date(dtObj)



		balance=request.POST.get('balance')
		schedule_amount=request.POST.get('schedule_amount')
		processed_by=CustomUser.objects.get(id=request.user.id)

		transaction_id=request.POST.get('transactions')
		transaction_selected=TransactionTypes.objects.get(id=transaction_id)
		if MembersAccountsDomain.objects.filter(member=member,transaction=transaction_selected).exists():
			transaction=MembersAccountsDomain.objects.get(member=member,transaction=transaction_selected)
		else:
			transaction= MembersAccountsDomain(member=member,transaction=transaction_selected,account_number=str(transaction_selected.code) + str(member.get_member_Id),status='ACTIVE',loan_lock='YES')
			transaction.save()


		# return HttpResponse(transaction.account_number)
		formatted_date = defaultfilters.date(transaction_period, "SHORT_DATE_FORMAT")
		particulars="Balance Brought Forward as at " + str(formatted_date)

		if float(balance)<=0:
			messages.error(request,"Balance Brought Forward must be greater than zero")
			return HttpResponseRedirect(reverse('Uploading_Existing_Savings_Additional_Preview',args=(pk,)))


		if SavingsUploaded.objects.filter(transaction__member=member,transaction=transaction,status=transaction_status).exists():

			record=SavingsUploaded.objects.get(transaction__member=member,transaction=transaction,status=transaction_status)
			record.particulars=particulars
			record.balance=float(balance)
			record.schedule_amount=float(schedule_amount)
			record.processed_by=processed_by.username
			record.status=transaction_status
			record.transaction_period=transaction_period
			record.save()
			messages.success(request,"Record Updated Successfully")

		elif SavingsUploaded.objects.filter(transaction__member=member,transaction=transaction).filter(~Q(status=transaction_status)).exists():
			messages.error(request,"Record Cannot be Altered, It is already validated")

		else:
			record=SavingsUploaded(particulars=particulars,transaction=transaction,balance=balance,schedule_amount=schedule_amount,processed_by=processed_by.username,status=transaction_status,transaction_period=transaction_period)
			record.save()
			messages.success(request,"Record Addedd Successfully")

		return HttpResponseRedirect(reverse('Uploading_Existing_Savings_Additional_Preview',args=(pk,)))

	t_period = get_current_date(transaction_period)
	form.fields['transaction_period'].initial=t_period
	context={

	'member':member,
	'form':form,
	'records':records,
	'return_pk':pk,
	'task_array':task_array,
	'task_enabler_array':task_enabler_array,
	'default_password':default_password,
	}
	return render(request,'deskofficer_templates/Uploading_Existing_Savings_Additional_Preview.html',context)



def Uploading_Existing_Savings_Additional_delete(request,pk,return_pk):
	record=SavingsUploaded.objects.get(id=pk)
	record.delete()
	return HttpResponseRedirect(reverse('Uploading_Existing_Savings_Additional_Preview',args=(return_pk,)))


def Uploading_Existing_Savings_Additional_validate(request,pk):
	tdate = get_current_date(now)
	lock_status='LOCKED'
	savings_status='UPLOADED'
	status='UNTREATED'

	status1='ACTIVE'
	# transaction_period=TransactionPeriods.objects.get(status=status1)


	member=Members.objects.get(id=pk)
	if SavingsUploaded.objects.filter(transaction__member=member,status=status).exists():
		records=SavingsUploaded.objects.filter(transaction__member=member,status=status)
		for item in records:
			transaction_id=item.transaction.transaction_id
			transaction=TransactionTypes.objects.get(id=transaction_id)

			transaction_period=item.transaction_period
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
				ledger=get_ledger_balance(account_number)

				post_to_ledger(member,
								transaction,
								account_number,
								particulars,
								debit,
								credit,
								float(balance)+float(ledger),
								transaction_period,
								status1,
								tdate)

			else:
				post_to_ledger(member,
								transaction,
								account_number,
								particulars,
								debit,
								credit,
								balance,
								transaction_period,
								status1,
								tdate)


			transaction_status='TREATED'

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
############################# UPLOADING EXISTING LOANS #################
#########################################################################
def Uploading_Existing_Loans_Search(request):
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	task_array=[]
	for task in tasks:
		task_array.append(task.task.title)

	task_enabler=TransactionEnabler.objects.filter(status="YES")
	task_enabler_array=[]
	for item in task_enabler:
		task_enabler_array.append(item.title)

	default_password="NO"
	if Staff.objects.filter(admin=request.user,default_password='YES'):
		default_password="YES"

	title="Search Members for Ledger Information"
	form = searchForm(request.POST or None)

	return render(request,'deskofficer_templates/Uploading_Existing_Loans_Search.html',{'form':form,'title':title,'task_array':task_array,
	'task_enabler_array':task_enabler_array,
	'default_password':default_password,
	})



def Uploading_Existing_Loans_List_load(request):
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	task_array=[]
	for task in tasks:
		task_array.append(task.task.title)

	task_enabler=TransactionEnabler.objects.filter(status="YES")
	task_enabler_array=[]
	for item in task_enabler:
		task_enabler_array.append(item.title)

	default_password="NO"
	if Staff.objects.filter(admin=request.user,default_password='YES'):
		default_password="YES"

	title="LIST OF MEMBERS"
	form = searchForm(request.POST)
	status="ACTIVE"
	loan_status='PENDING'
	if request.method == "POST":
		if request.POST.get("title")=="":
			messages.info(request,"Please Enter a search data")
			return HttpResponseRedirect(reverse('Uploading_Existing_Loans_Search'))


		records=Members.objects.filter(Q(file_no__icontains=form['title'].value()) |Q(ippis_no__icontains=form['title'].value()) |Q(phone_number__icontains=form['title'].value()) | Q(admin__first_name__icontains=form['title'].value()) | Q(admin__last_name__icontains=form['title'].value()) | Q(middle_name__icontains=form['title'].value())).filter(status=status,loan_status=loan_status,member_category="OLD")
		if records.count() <= 0:
			messages.info(request,"No Record Found")
			return HttpResponseRedirect(reverse('Transaction_adjustment_history_Search'))

		context={
		'records':records,
		'title':title,
		'task_array':task_array,
		'task_enabler_array':task_enabler_array,
	'default_password':default_password,
		}
		return render(request,'deskofficer_templates/Uploading_Existing_Loans_List_load.html',context)


def Uploading_Existing_Loans_Preview(request,pk):
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	task_array=[]
	for task in tasks:
		task_array.append(task.task.title)



	task_enabler=TransactionEnabler.objects.filter(status="YES")
	task_enabler_array=[]
	for item in task_enabler:
		task_enabler_array.append(item.title)

	default_password="NO"
	if Staff.objects.filter(admin=request.user,default_password='YES'):
		default_password="YES"

	form=Uploading_Existing_Loans_form(request.POST or None)
	member=Members.objects.get(id=pk)
	records=LoansUploaded.objects.filter(member=member)
	transaction_status='UNTREATED'
	status="ACTIVE"
	
	if TransactionPeriods.objects.filter(status=status).exists():
		transaction_period=TransactionPeriods.objects.get(status=status)
		transaction_period= transaction_period.transaction_period
	else:
		transaction_period= now

	if request.method=="POST":
		date_format = '%Y-%m-%d'
		transaction_period_id=request.POST.get('transaction_period')
		dtObj = datetime.datetime.strptime(transaction_period_id, date_format)
		transaction_period=get_current_date(dtObj)



		formatted_date = defaultfilters.date(transaction_period, "SHORT_DATE_FORMAT")
		particulars="Balance Brought Forward as at " + str(formatted_date)

		transaction_id=request.POST.get('transactions')
		transaction=TransactionTypes.objects.get(id=transaction_id)

		interest_deduction=request.POST.get('interest_deductions')
		# interest_deduction=InterestDeductionSource.objects.get(id=interest_deduction_id)
		# return HttpResponse(interest_deduction)

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
		if float(interest_rate)<0:
			messages.error(request,'Interest Rate cannot be less than zero')
			return HttpResponseRedirect(reverse('Uploading_Existing_Loans_Preview',args=(pk,)))

		admin_charge_rate=request.POST.get('admin_charge_rate')
		if float(admin_charge_rate)<0:
			messages.error(request,'Admin Charge Rate cannot be less than zero')
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
			record.admin_charge_rate=admin_charge_rate,
			record.duration=duration,
			record.interest_deduction=interest_deduction,
			record.start_date=start_date,
			record.stop_date=stop_date,
			record.processed_by=processed_by.username
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
				admin_charge_rate=admin_charge_rate,
				duration=duration,
				interest_deduction=interest_deduction,
				start_date=start_date,
				stop_date=stop_date,
				processed_by=processed_by.username,status=transaction_status,transaction_period=transaction_period)
			record.save()
			messages.success(request,"Record Addedd Successfully")

		return HttpResponseRedirect(reverse('Uploading_Existing_Loans_Preview',args=(pk,)))
	

	form.fields['start_date'].initial=now
	form.fields['transaction_period'].initial=get_current_date(transaction_period)


	context={

	'member':member,
	'form':form,
	'records':records,
	'return_pk':pk,
	'task_array':task_array,
	'task_enabler_array':task_enabler_array,
	'default_password':default_password,
	}
	return render(request,'deskofficer_templates/Uploading_Existing_Loans_Preview.html',context)



def Uploading_Existing_Loans_validate(request,pk):
	member=Members.objects.get(id=pk)
	processed_by=CustomUser.objects.get(id=request.user.id)
	loan_status='UPLOADED'
	status = 'UNTREATED'
	status1='ACTIVE'
	status2='INACTIVE'
	schedule_status='SCHEDULED'
	loan_lock='YES'

	# transaction_period=TransactionPeriods.objects.get(status=status1)
	


	now = datetime.datetime.now()
	tdate=get_current_date(now)

	if MembersNextOfKins.objects.filter(member=member).exists():
		NOK = MembersNextOfKins.objects.filter(member=member)
		nok_name=NOK.name
		nok_Relationship=NOK.relationships.title
		nok_phone_no=NOK.phone_number
		nok_address=NOK.address
	else:
		nok_name="UNKNOWN"
		nok_Relationship="UNKNOWN"
		nok_phone_no="UNKNOWN"
		nok_address="UNKNOWN"

	if LoansUploaded.objects.filter(member=member,status=status).exists():

		loan_records=LoansUploaded.objects.filter(member=member,status=status)

		for record in loan_records:
			transaction_period=record.transaction_period
			formatted_date = defaultfilters.date(transaction_period, "SHORT_DATE_FORMAT")

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

			interest = (float(interest_rate)/100) * float(loan_amount)
			admin_charge_rate=record.admin_charge_rate
			admin_charge = (float(admin_charge_rate/100))* float(loan_amount)

			start_date=record.start_date
			stop_date=record.stop_date
			processed_by=CustomUser.objects.get(id=request.user.id)


			loan_code=transaction.code
			if LoanNumber.objects.all().count() == 0:
				messages.error(request,"Loan Number not Set")
				return HttpResponseRedirect(reverse('Uploading_Existing_Loans_Preview',args=(pk,)))

			loan_number=generate_number(loan_code,my_id,now)

			particulars="Balance Brought Forward as at " + str(formatted_date) + " for a loan of " + str(loan_amount)

			if PersonalLedger.objects.filter(member=member,transaction=transaction).exists():
				pass
			else:
				post_to_ledger(
							member,
							transaction,
							loan_number,
							particulars,
							debit,
							credit,
							balance,
							transaction_period,
							status1,
							tdate,
							)


				if LoansRepaymentBase.objects.filter(member=member,transaction=transaction,status=status1).exists():
					pass
				else:


					Loans_Repayment_Base(
						member,
						nok_name,
	                    nok_Relationship,
	                    nok_phone_no,
	                    nok_address,
						duration,
						interest_deduction,
                    	interest_rate,
                    	interest,
                    	admin_charge,
						transaction,
						loan_number,
						loan_amount,
						repayment,
						balance,
						amount_paid,
						start_date,
						stop_date,
						processed_by,
						status1,
						tdate,
						schedule_status
						)




			transaction_status='TREATED'

			record.status=transaction_status
			record.save()

		member.loan_status=loan_status
		member.save()

		if transaction.auto_stop_savings == 'YES':
			savings=LoanBasedSavings.objects.all()
			if savings:
				record=LoanBasedSavings.objects.all().first()
				if StandingOrderAccounts.objects.filter(transaction__transaction=record.savings,transaction__member=member).exists():
					StandingOrderAccounts.objects.filter(transaction__transaction=record.savings,transaction__member=member).update(status=status2)
					queryset=StandingOrderAccounts.objects.get(transaction__transaction=record.savings,transaction__member=member)
					MembersAccountsDomain.objects.filter(account_number=queryset.transaction.account_number).update(loan_lock=loan_lock)
					StandingOrderDeactivatedAccounts(transaction=queryset,status=status,processed_by=processed_by.username,tdate=tdate).save()
		messages.success(request,"Record Validated Successfully")


	else:
		messages.error(request,"No Record Found")
	return HttpResponseRedirect(reverse('deskofficer_home'))


def Uploading_Existing_Loans_delete(request,pk,return_pk):
	record=LoansUploaded.objects.get(id=pk)
	record.delete()
	return HttpResponseRedirect(reverse('Uploading_Existing_Loans_Preview',args=(return_pk,)))



########################################################################
############################# UPLOADING EXISTING ADDITIONAL LOANS ######
#########################################################################
def Uploading_Existing_Aditional_Loans(request):
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	task_array=[]
	for task in tasks:
		task_array.append(task.task.title)



	task_enabler=TransactionEnabler.objects.filter(status="YES")
	task_enabler_array=[]
	for item in task_enabler:
		task_enabler_array.append(item.title)

	default_password="NO"
	if Staff.objects.filter(admin=request.user,default_password='YES'):
		default_password="YES"


	loan_status='PENDING'
	records=Members.objects.filter(~Q(loan_status=loan_status))

	context={

	'records':records,
	'task_array':task_array,
	'task_enabler_array':task_enabler_array,
	'default_password':default_password,
	}
	return render(request,'deskofficer_templates/Uploading_Existing_Aditional_Loans.html',context)


def Uploading_Existing_Additional_Loans_Preview(request,pk):
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	task_array=[]
	for task in tasks:
		task_array.append(task.task.title)



	task_enabler=TransactionEnabler.objects.filter(status="YES")
	task_enabler_array=[]
	for item in task_enabler:
		task_enabler_array.append(item.title)

	default_password="NO"
	if Staff.objects.filter(admin=request.user,default_password='YES'):
		default_password="YES"

	form=Uploading_Existing_Loans_form(request.POST or None)
	member=Members.objects.get(id=pk)
	processed_by=CustomUser.objects.get(id=request.user.id)

	records=LoansUploaded.objects.filter(member=member)

	transaction_status='UNTREATED'
	status="ACTIVE"

	if TransactionPeriods.objects.filter(status=status).exists():
		transaction_period=TransactionPeriods.objects.get(status=status)
		transaction_period=transaction_period.transaction_period
	else:
		transaction_period=now


	if request.method=="POST":
		transaction_period_id = request.POST.get('transaction_period')
		
		date_format = '%Y-%m-%d'
		dtObj = datetime.datetime.strptime(transaction_period_id, date_format)
		transaction_period=get_current_date(dtObj)



		formatted_date = defaultfilters.date(transaction_period_id, "SHORT_DATE_FORMAT")
		particulars="Balance Brought Forward as at " + str(formatted_date)

		transaction_id=request.POST.get('transactions')
		transaction=TransactionTypes.objects.get(id=transaction_id)

		interest_deduction=request.POST.get('interest_deductions')
		# interest_deduction=InterestDeductionSource.objects.get(id=interest_deduction_id)


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
		if float(interest_rate)<0:
			messages.error(request,'Interest Rate cannot be less than zero')
			return HttpResponseRedirect(reverse('Uploading_Existing_Additional_Loans_Preview',args=(pk,)))

		admin_charge_rate=request.POST.get('admin_charge_rate')
		if float(interest_rate)<0:
			messages.error(request,'Admin Charge Rate cannot be less than zero')
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

		if LoansUploaded.objects.filter(member=member,transaction=transaction).exists():
			record=LoansUploaded.objects.get(member=member,transaction=transaction)
			record.particulars=particulars
			record.loan_amount=loan_amount
			record.amount_paid=amount_paid
			record.balance=balance
			record.repayment=repayment,
			record.admin_charge_rate=admin_charge_rate,
			record.interest_rate=interest_rate,
			record.duration=duration,
			record.interest_deduction=interest_deduction,
			record.start_date=start_date,
			record.stop_date=stop_date,
			record.processed_by=processed_by.username
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
				admin_charge_rate=admin_charge_rate,
				duration=duration,
				interest_deduction=interest_deduction,
				start_date=start_date,
				stop_date=stop_date,
				processed_by=processed_by.username,status=transaction_status,transaction_period=transaction_period)
			record.save()
			messages.success(request,"Record Addedd Successfully")

		return HttpResponseRedirect(reverse('Uploading_Existing_Additional_Loans_Preview',args=(pk,)))
	form.fields['start_date'].initial=now
	form.fields['transaction_period'].initial=get_current_date(transaction_period)


	context={

	'member':member,
	'form':form,
	'records':records,
	'return_pk':pk,
	'task_array':task_array,
	'task_enabler_array':task_enabler_array,
	'default_password':default_password,
	}
	return render(request,'deskofficer_templates/Uploading_Existing_Additional_Loans_Preview.html',context)



def Uploading_Existing_Additional_Loans_validate(request,pk):
	member=Members.objects.get(id=pk)

	loan_status='UPLOADED'
	status = 'UNTREATED'
	status1='ACTIVE'
	schedule_status='SCHEDULED'


	
	
	now = datetime.datetime.now()
	tdate=get_current_date(now)

	if MembersNextOfKins.objects.filter(member=member).exists():
		NOK = MembersNextOfKins.objects.filter(member=member)
		nok_name=NOK.name
		nok_Relationship=NOK.relationships.title
		nok_phone_no=NOK.phone_number
		nok_address=NOK.address
	else:
		nok_name="UNKNOWN"
		nok_Relationship="UNKNOWN"
		nok_phone_no="UNKNOWN"
		nok_address="UNKNOWN"

	if LoansUploaded.objects.filter(member=member,status=status).exists():

		loan_records=LoansUploaded.objects.filter(member=member,status=status)

		for record in loan_records:
			transaction_period=record.transaction_period
			formatted_date = defaultfilters.date(transaction_period, "SHORT_DATE_FORMAT")

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
			interest= (float(interest_rate)/100)*float(loan_amount)

			admin_charge_rate=record.admin_charge_rate
			admin_charge= (float(admin_charge_rate)/100)*float(admin_charge_rate)
			start_date=record.start_date
			stop_date=record.stop_date
			processed_by=CustomUser.objects.get(id=request.user.id)

			loan_code=transaction.code
			if LoanNumber.objects.all().count() == 0:
				messages.error(request,"Loan Number not Set")
				return HttpResponseRedirect(reverse('Uploading_Existing_Loans_Preview',args=(pk,)))

			loan_number=generate_number(loan_code,my_id,now)


			particulars="Balance Brought Forward as at " + str(formatted_date) + " for a loan of " + str(loan_amount)

			if PersonalLedger.objects.filter(member=member,transaction=transaction).exists():
				pass
			else:
				post_to_ledger(member,
								transaction,
								loan_number,
								particulars,
								debit,
								credit,
								balance,
								transaction_period,
								status1,
								tdate,
								)



				if LoansRepaymentBase.objects.filter(member=member,transaction=transaction,status=status1).exists():
					pass
				else:
					Loans_Repayment_Base(
						member,
						nok_name,
	                    nok_Relationship,
	                    nok_phone_no,
	                    nok_address,
						duration,
						interest_deduction,
                    	interest_rate,
                    	interest,
                    	admin_charge,
						transaction,
						loan_number,
						loan_amount,
						repayment,
						balance,
						amount_paid,
						start_date,
						stop_date,
						processed_by,
						status1,
						tdate,
						schedule_status
						)

			record.status='TREATED'
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
############################# UPDATING SALARY GROSS PAY##################
#########################################################################
def Updating_Salary_Grosspay_list_load(request):
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	task_array=[]
	for task in tasks:
		task_array.append(task.task.title)

	task_enabler=TransactionEnabler.objects.filter(status="YES")
	task_enabler_array=[]
	for item in task_enabler:
		task_enabler_array.append(item.title)

	default_password="NO"
	if Staff.objects.filter(admin=request.user,default_password='YES'):
		default_password="YES"



	status="ACTIVE"
	salary_status='PENDING'
	# records=Members.objects.filter(status=status).filter(Q(gender__isnull=True) | Q(gender=""))
	records=Members.objects.filter(status=status).filter(Q(salary_status__isnull=True) | Q(salary_status=""))

	context={
	'records':records,
	'task_array':task_array,
	'task_enabler_array':task_enabler_array,
	'default_password':default_password,
	}
	return render(request,'deskofficer_templates/Updating_Salary_Grosspay_list_load.html',context)



########################################################################
############################# UPDATING NORMINAL ROLL#####################
#########################################################################

def Norminal_Roll_Search(request):
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	task_array=[]
	for task in tasks:
		task_array.append(task.task.title)

	task_enabler=TransactionEnabler.objects.filter(status="YES")
	task_enabler_array=[]
	for item in task_enabler:
		task_enabler_array.append(item.title)


	default_password="NO"
	if Staff.objects.filter(admin=request.user,default_password='YES'):
		default_password="YES"


	title="Search Members for Cash Deposit"
	form = searchForm(request.POST or None)

	return render(request,'deskofficer_templates/Norminal_Roll_Search.html',{'form':form,'title':title,'task_array':task_array,
	'task_enabler_array':task_enabler_array,
	'default_password':default_password,})

def Norminal_Roll_Update(request,pk):
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	task_array=[]
	for task in tasks:
		task_array.append(task.task.title)

	task_enabler=TransactionEnabler.objects.filter(status="YES")
	task_enabler_array=[]
	for item in task_enabler:
		task_enabler_array.append(item.title)

	default_password="NO"
	if Staff.objects.filter(admin=request.user,default_password='YES'):
		default_password="YES"


	form = Norminal_Roll_Update_form(request.POST or None)
	member=Members.objects.get(pk=pk)

	if request.method=='POST':
		if request.POST.get("chk_title"):
			title_id=request.POST.get('title')
			member.title=Titles.objects.get(id=title_id)

		member.middle_name=request.POST.get('middle_name')

		if request.POST.get("chk_gender"):
			gender_id=request.POST.get('gender')
			member.gender=Gender.objects.get(id=gender_id)

		member.phone_number=request.POST.get('phone_number')
		if request.POST.get("chk_department"):
			department_id=request.POST.get('department')
			member.department=Departments.objects.get(id=department_id)

		salary_institution_id=request.POST.get('salary_institution')
		salary_institution=SalaryInstitution.objects.get(id=salary_institution_id)
		residential_address=request.POST.get('residential_address')
		permanent_home_address=request.POST.get('permanent_home_address')
		file_no=request.POST.get('file_no')
		ippis_no=request.POST.get('ippis_no')
		last_used_net_pay=request.POST.get('last_used_net_pay')

		if last_used_net_pay and float(last_used_net_pay) !=0:
			net_pay_as_at=request.POST.get('net_pay_as_at')
			if net_pay_as_at:
				date_format = '%Y-%m-%d'
				dtObj = datetime.datetime.strptime(net_pay_as_at, date_format)
				net_pay_as_at=get_current_date(dtObj)

			else:
				messages.error(request,'Please Specify period in Payslip')
				return HttpResponseRedirect(reverse('Norminal_Roll_Update', args=(pk,)))

		date_joined=request.POST.get('date_joined')
		date_of_first_appointment=request.POST.get('date_of_first_appointment')
		dob=request.POST.get('dob')
		phone_number=request.POST.get('phone_number')
		last_name=request.POST.get('last_name')
		first_name=request.POST.get('first_name')
		middle_name=request.POST.get('middle_name')

		
		# exist_records=Members.objects.filter(file_no=file_no)
		# k=1
		# for item in exist_records:
		# 	print(f'{item.admin.last_name} {item.pk} row{k}')
		# 	k=k+1

		if Members.objects.filter(file_no=file_no).exclude(id=pk).exists():
			messages.error(request,'Record with this File No Already Exist')
			return HttpResponseRedirect(reverse('Norminal_Roll_Update', args=(pk,)))


		if Members.objects.filter(ippis_no=ippis_no).exclude(id=pk).exists():
			messages.error(request,'Record with this Salary Code Already Exist')
			return HttpResponseRedirect(reverse('Norminal_Roll_Update', args=(pk,)))

		if Members.objects.filter(phone_number=phone_number).exclude(id=pk).exists():
			messages.error(request,'Record with this Phone Number Already Exist')
			return HttpResponseRedirect(reverse('Norminal_Roll_Update', args=(pk,)))


		member.salary_institution=salary_institution
		member.residential_address=residential_address
		member.permanent_home_address=permanent_home_address
		member.file_no=file_no
		member.ippis_no=ippis_no
		if last_used_net_pay and float(last_used_net_pay) !=0:
			member.last_used_net_pay=last_used_net_pay
			member.net_pay_as_at=net_pay_as_at

		member.date_joined=date_joined
		if request.POST.get("chk_appointment"):
			member.date_of_first_appointment=date_of_first_appointment
		if request.POST.get("chk_dob"):
			member.dob=dob
		member.phone_number=phone_number
		if middle_name:
			member.middle_name=middle_name

		member.save()
		member.admin.last_name=last_name
		member.admin.first_name=first_name
		member.admin.save()
		return HttpResponseRedirect(reverse('deskofficer_home'))

	form.fields['title'].initial= member.title_id
	form.fields['last_name'].initial= member.admin.last_name
	form.fields['first_name'].initial= member.admin.first_name
	form.fields['middle_name'].initial= member.middle_name

	form.fields['dob'].initial= member.dob
	form.fields['gender'].initial= member.gender_id
	form.fields['phone_number'].initial= member.phone_number
	form.fields['department'].initial= member.department_id

	form.fields['salary_institution'].initial= member.salary_institution_id
	form.fields['residential_address'].initial= member.residential_address
	form.fields['permanent_home_address'].initial= member.permanent_home_address

	form.fields['file_no'].initial= member.file_no
	form.fields['ippis_no'].initial= member.ippis_no
	form.fields['net_pay_as_at'].initial= member.net_pay_as_at
	form.fields['last_used_net_pay'].initial= member.last_used_net_pay
	form.fields['net_pay_as_at'].initial= member.net_pay_as_at
	form.fields['date_joined'].initial= member.date_joined
	form.fields['date_of_first_appointment'].initial= member.date_of_first_appointment

	context={
	'form':form,
	'member':member,
	'task_array':task_array,
	'task_enabler_array':task_enabler_array,
	'default_password':default_password,
	}
	return render(request,'deskofficer_templates/Norminal_Roll_Update.html',context)



def Norminal_Roll_Update_list_load(request):
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	task_array=[]
	for task in tasks:
		task_array.append(task.task.title)

	task_enabler=TransactionEnabler.objects.filter(status="YES")
	task_enabler_array=[]
	for item in task_enabler:
		task_enabler_array.append(item.title)


	default_password="NO"
	if Staff.objects.filter(admin=request.user,default_password='YES'):
		default_password="YES"


	title="LIST OF MEMBERS"
	form = searchForm(request.POST)
	status="ACTIVE"

	if request.method == "POST":
		if request.POST.get("title")=="":
			return HttpResponseRedirect(reverse('deskofficer_home'))

		members=searchMembers(form['title'].value(),status)
		# members=Members.objects.filter(Q(file_no__icontains=form['title'].value()) |Q(ippis_no__icontains=form['title'].value()) |Q(phone_number__icontains=form['title'].value()) | Q(admin__first_name__icontains=form['title'].value()) | Q(admin__last_name__icontains=form['title'].value()) | Q(middle_name__icontains=form['title'].value())).filter(status=status)

		context={
		'members':members,
		'title':title,
		'task_array':task_array,
	'task_enabler_array':task_enabler_array,
	'default_password':default_password,
		}
		return render(request,'deskofficer_templates/Norminal_Roll.html',context)



def Member_delete(request,pk):
	member=Members.objects.get(id=pk)
	member.delete()
	return HttpResponseRedirect(reverse('Norminal_Roll'))



############################################################
##################### MEMBERS SHARE ########################
############################################################

def Members_Shares_Upload_Search(request):
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	task_array=[]
	for task in tasks:
		task_array.append(task.task.title)



	task_enabler=TransactionEnabler.objects.filter(status="YES")
	task_enabler_array=[]
	for item in task_enabler:
		task_enabler_array.append(item.title)

	default_password="NO"
	if Staff.objects.filter(admin=request.user,default_password='YES'):
		default_password="YES"



	title="Search Members for Ledger Information"
	form = searchForm(request.POST or None)

	return render(request,'deskofficer_templates/Members_Shares_Upload_Search.html',{'form':form,'title':title,'task_array':task_array,
	'task_enabler_array':task_enabler_array,
	'default_password':default_password,
	})



def Members_Shares_Upload_list_load(request):
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	task_array=[]
	for task in tasks:
		task_array.append(task.task.title)

	task_enabler=TransactionEnabler.objects.filter(status="YES")
	task_enabler_array=[]
	for item in task_enabler:
		task_enabler_array.append(item.title)

	default_password="NO"
	if Staff.objects.filter(admin=request.user,default_password='YES'):
		default_password="YES"


	title="LIST OF MEMBERS"
	form = searchForm(request.POST)
	status="ACTIVE"
	shares_status = 'PENDING'
	if request.method == "POST":
		if request.POST.get("title")=="":
			messages.info(request,"Please Enter a search data")
			return HttpResponseRedirect(reverse('Members_Shares_Upload_Search'))


		records=Members.objects.filter(Q(file_no__icontains=form['title'].value()) |Q(ippis_no__icontains=form['title'].value()) |Q(phone_number__icontains=form['title'].value()) | Q(admin__first_name__icontains=form['title'].value()) | Q(admin__last_name__icontains=form['title'].value()) | Q(middle_name__icontains=form['title'].value())).filter(status=status,shares_status=shares_status,member_category='OLD')
		if records.count() <= 0:
			messages.info(request,"No Record Found")
			return HttpResponseRedirect(reverse('Transaction_adjustment_history_Search'))


		context={
		'records':records,
		'title':title,
		'task_array':task_array,
	'task_enabler_array':task_enabler_array,
	'default_password':default_password,
		}
		return render(request,'deskofficer_templates/Members_Shares_Upload_list_load.html',context)



def Members_Shares_Upload_Preview(request,pk):
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	task_array=[]
	for task in tasks:
		task_array.append(task.task.title)



	task_enabler=TransactionEnabler.objects.filter(status="YES")
	task_enabler_array=[]
	for item in task_enabler:
		task_enabler_array.append(item.title)

	default_password="NO"
	if Staff.objects.filter(admin=request.user,default_password='YES'):
		default_password="YES"



	form=Existing_Shares_Upload_form(request.POST or None)

	processed_by=CustomUser.objects.get(id=request.user.id)
	status='UNTREATED'
	status1='ACTIVE'
	shares_status='VERIFIED'


	member1=Members.objects.get(id=pk)
	tdate=get_current_date(now)

	unit_share_cost=0
	if MembersShareConfigurations.objects.all().exists():
		unit_share_cost=MembersShareConfigurations.objects.all().first()
		unit_share_cost=unit_share_cost.unit_cost


	transaction=TransactionTypes.objects.get(code=700)

	total_shares=0
	member=[]
	if MembersAccountsDomain.objects.filter(member=member1,transaction=transaction).exists():
		member=MembersAccountsDomain.objects.get(member=member1,transaction=transaction)


	if request.method=="POST" and 'btn-upload' in request.POST:

		transaction_period=TransactionPeriods.objects.get(status='ACTIVE')
		shares_amount=request.POST.get('shares_amount')


		total_shares=float(shares_amount)/float(unit_share_cost)
		shares = "{:.2f}".format(total_shares)


		effective_date=request.POST.get('effective_date')
		date = parse_date(effective_date)


		if not member:
			messages.error(request,'Please There is no account member for this Transaction')
			return HttpResponseRedirect(reverse('Members_Shares_Upload_Preview',args=(pk,)))

		account_number=member.account_number


		if MembersShareAccounts.objects.filter(member=member).exists():
			messages.info(request,'Record Already Exist')
			return HttpResponseRedirect(reverse('Members_Shares_Upload_Preview',args=(pk,)))

		record=MembersShareAccounts(member=member,
									shares=shares,
									unit_cost=unit_share_cost,
									total_cost=shares_amount,
									effective_date=effective_date,
									year=date.year,
									status=status,
									tdate=tdate,
									processed_by=processed_by.username)
		record.save()

		debit=0
		credit=shares_amount
		balance=shares_amount

		particulars='Balance Broght Forward as at ' + str(transaction_period.transaction_period) + " with shares of " + str(shares)
		post_to_ledger(member1,
						transaction,
						account_number,
						particulars,
						debit,
						credit,
						balance,
						transaction_period.transaction_period,
						status1,
						tdate,
						)
		record.save()

		member1.shares_status=shares_status
		member1.save()

		return HttpResponseRedirect(reverse('deskofficer_home'))

	form.fields['unit_cost'].initial= unit_share_cost
	form.fields['effective_date'].initial= now
	context={
	'member':member,
	'member1':member1,
	'form':form,
	'task_array':task_array,
	'task_enabler_array':task_enabler_array,
	'default_password':default_password,
	}
	return render(request,'deskofficer_templates/Members_Shares_Upload_Preview.html',context)



def Members_Initial_Shares_update_Search(request):
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	task_array=[]
	for task in tasks:
		task_array.append(task.task.title)



	task_enabler=TransactionEnabler.objects.filter(status="YES")
	task_enabler_array=[]
	for item in task_enabler:
		task_enabler_array.append(item.title)



	default_password="NO"
	if Staff.objects.filter(admin=request.user,default_password='YES'):
		default_password="YES"



	title="Search Members for Initial Share Update"
	form = searchForm(request.POST or None)

	return render(request,'deskofficer_templates/Members_Initial_Shares_update_Search.html',{'form':form,'title':title,'task_array':task_array,
	'task_enabler_array':task_enabler_array,
	'default_password':default_password,})


def Members_Initial_Shares_update_list_load(request):
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	task_array=[]
	for task in tasks:
		task_array.append(task.task.title)



	task_enabler=TransactionEnabler.objects.filter(status="YES")
	task_enabler_array=[]
	for item in task_enabler:
		task_enabler_array.append(item.title)


	default_password="NO"
	if Staff.objects.filter(admin=request.user,default_password='YES'):
		default_password="YES"



	title="LIST OF MEMBERS"
	status="ACTIVE"
	form = searchForm(request.POST)

	if request.method == "POST":
		if request.POST.get("title")=="":
			return HttpResponseRedirect(reverse('Members_Initial_Shares_update_Search'))

		members=MembersShareAccounts.objects.filter(Q(member__member__file_no__icontains=form['title'].value())
													|Q(member__member__ippis_no__icontains=form['title'].value())
													|Q(member__member__phone_number__icontains=form['title'].value())
													|Q(member__member__admin__first_name__icontains=form['title'].value())
													|Q(member__member__admin__last_name__icontains=form['title'].value())
													|Q(member__member__middle_name__icontains=form['title'].value())).filter(Q(shares__lt=2))


		context={
		'members':members,
		'title':title,
		'task_array':task_array,
	'task_enabler_array':task_enabler_array,
	'default_password':default_password,
		}
		return render(request,'deskofficer_templates/Members_Initial_Shares_update_list_load.html',context)


def Members_Initial_Shares_update_preview(request,pk):
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	task_array=[]
	for task in tasks:
		task_array.append(task.task.title)



	task_enabler=TransactionEnabler.objects.filter(status="YES")
	task_enabler_array=[]
	for item in task_enabler:
		task_enabler_array.append(item.title)


	default_password="NO"
	if Staff.objects.filter(admin=request.user,default_password='YES'):
		default_password="YES"

	form=MembersInitialShare_update_form(request.POST or None)
	tdate=get_current_date(now)
	if MembersShareConfigurations.objects.all().count()>0:
		record=MembersShareConfigurations.objects.first()
		form.fields['unit_cost'].initial=record.unit_cost


	member=MembersShareAccounts.objects.get(id=pk)

	if request.method=='POST':
		status='UNTREATED'
		approval_status='PENDING'

		transaction_id=request.POST.get('transactions')
		transaction=SharesDeductionSavings.objects.get(id=transaction_id)

		amount=record.unit_cost
		processed_by=CustomUser.objects.get(id=request.user.id)
		if MembersShareInitialUpdateRequest.objects.filter(member=member,status=status).exists():
			messages.info(request,'There is still an open transaction for this member')
			return HttpResponseRedirect(reverse('Members_Initial_Shares_update_preview',args=(pk,)))

		record=MembersShareInitialUpdateRequest(approval_status=approval_status,tdate=tdate,member=member,transaction=transaction.savings,amount=amount,processed_by=processed_by.username,status=status)
		record.save()
		messages.success(request,'Transaction Completed Successfully')
		return HttpResponseRedirect(reverse('Members_Initial_Shares_update_Search'))
	context={
	'task_array':task_array,
	'task_enabler_array':task_enabler_array,
	'default_password':default_password,
	'form':form,
	}
	return render(request,'deskofficer_templates/Members_Initial_Shares_update_preview.html',context)


def Members_Initial_Shares_update_approved_list_load(request):
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	task_array=[]
	for task in tasks:
		task_array.append(task.task.title)



	task_enabler=TransactionEnabler.objects.filter(status="YES")
	task_enabler_array=[]
	for item in task_enabler:
		task_enabler_array.append(item.title)

	default_password="NO"
	if Staff.objects.filter(admin=request.user,default_password='YES'):
		default_password="YES"


	status='UNTREATED'
	approval_status='APPROVED'
	members=MembersShareInitialUpdateRequest.objects.filter(status=status,approval_status=approval_status)

	context={
	'task_array':task_array,
	'task_enabler_array':task_enabler_array,
	'default_password':default_password,
	'members':members,
	}
	return render(request,'deskofficer_templates/Members_Initial_Shares_update_approved_list_load.html',context)


def Members_Initial_Shares_update_approved_processed(request,pk):
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	task_array=[]
	for task in tasks:
		task_array.append(task.task.title)

	task_enabler=TransactionEnabler.objects.filter(status="YES")
	task_enabler_array=[]
	for item in task_enabler:
		task_enabler_array.append(item.title)

	default_password="NO"
	if Staff.objects.filter(admin=request.user,default_password='YES'):
		default_password="YES"

	transaction_period=TransactionPeriods.objects.get(status='ACTIVE')
	status1='ACTIVE'
	status='TREATED'
	member=MembersShareInitialUpdateRequest.objects.get(id=pk)
	account_number=member.member.member.account_number
	tdate=get_current_date(now)

	ledger_balance=PersonalLedger.objects.filter(account_number=account_number).last()
	if request.method=="POST":
		savings_id=request.POST.get('savings')
		savings=TransactionTypes.objects.get(name=savings_id)

		amount=request.POST.get('amount')
		debit=0
		credit=amount
		balance=float(ledger_balance.balance) + float(amount)

		particulars='Initial Share Balance update as at ' + str(transaction_period.transaction_period) + " with shares: " + str(1) + " Deducted from " + str(savings.name)
		post_to_ledger(
						member.member.member.member,
						member.member.member.transaction,
						ledger_balance.account_number,
						particulars,
						debit,
						credit,
						balance,
						transaction_period.transaction_period,
						status1,
						tdate)


		member.status=status
		member.save()

		return HttpResponseRedirect(reverse('Members_Initial_Shares_update_approved_list_load'))

	context={
	'task_array':task_array,
	'task_enabler_array':task_enabler_array,
	'default_password':default_password,
	'member':member,
	'ledger_balance':ledger_balance.balance,
	}
	return render(request,'deskofficer_templates/Members_Initial_Shares_update_approved_processed.html',context)


def Members_Share_Purchase_Request_Search(request):
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	task_array=[]
	for task in tasks:
		task_array.append(task.task.title)

	task_enabler=TransactionEnabler.objects.filter(status="YES")
	task_enabler_array=[]
	for item in task_enabler:
		task_enabler_array.append(item.title)

	default_password="NO"
	if Staff.objects.filter(admin=request.user,default_password='YES'):
		default_password="YES"

	title="Search Members for Share Purchase"
	form = searchForm(request.POST or None)

	return render(request,'deskofficer_templates/Members_Share_Purchase_Request_Search.html',{'form':form,'title':title,'task_array':task_array,
	'task_enabler_array':task_enabler_array,
	'default_password':default_password,
	})



def Members_Share_Purchase_Request_list_load(request):
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	task_array=[]
	for task in tasks:
		task_array.append(task.task.title)

	task_enabler=TransactionEnabler.objects.filter(status="YES")
	task_enabler_array=[]
	for item in task_enabler:
		task_enabler_array.append(item.title)


	default_password="NO"
	if Staff.objects.filter(admin=request.user,default_password='YES'):
		default_password="YES"

	title="LIST OF MEMBERS"
	status="ACTIVE"
	form = searchForm(request.POST)

	if request.method == "POST":
		if request.POST.get("title")=="":
			return HttpResponseRedirect(reverse('Members_Share_Purchase_Request_Search'))

		members=MembersShareAccounts.objects.filter(Q(member__member__file_no__icontains=form['title'].value()) |Q(member__member__ippis_no__icontains=form['title'].value()) |Q(member__member__phone_number__icontains=form['title'].value()) | Q(member__member__admin__first_name__icontains=form['title'].value()) | Q(member__member__admin__last_name__icontains=form['title'].value()) | Q(member__member__middle_name__icontains=form['title'].value())).filter(member__member__status=status)

		context={
		'members':members,
		'title':title,
		'task_array':task_array,
		'task_enabler_array':task_enabler_array,
	'default_password':default_password,

		}
		return render(request,'deskofficer_templates/Members_Share_Purchase_Request_list_load.html',context)


def Members_Share_Purchase_Request_View(request,pk):
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	task_array=[]
	for task in tasks:
		task_array.append(task.task.title)

	task_enabler=TransactionEnabler.objects.filter(status="YES")
	task_enabler_array=[]
	for item in task_enabler:
		task_enabler_array.append(item.title)

	default_password="NO"
	if Staff.objects.filter(admin=request.user,default_password='YES'):
		default_password="YES"


	form = Members_Share_Purchase_Request_form(request.POST or None)
	member1=MembersShareAccounts.objects.get(id=pk)
	account_number=member1.member.account_number
	member=MembersAccountsDomain.objects.get(account_number=account_number)

	if request.method=="POST":
		tdate=get_current_date(now)
		status="UNTREATED"
		max_unit = SharesUnits.objects.all().order_by('unit').last()

		existing_share = member1.shares
		approval_status='PENDING'

		units=request.POST.get('units')
		if not units:
			messages.info(request,'Unit is missing')
			return HttpResponseRedirect(reverse('Members_Share_Purchase_Request_View',args=(pk,)))


		if int(max_unit.unit) < (int(units) + int(existing_share)):
			messages.error(request,"You have exceed the Maximum Units")
			return HttpResponseRedirect(reverse('Members_Share_Purchase_Request_View',args=(pk,)))


		if MembersSharePurchaseRequest.objects.filter(member=member,status=status).exists():
			messages.error(request,"You Still Have an Open Transaction")
			return HttpResponseRedirect(reverse('Members_Share_Purchase_Request_View',args=(pk,)))

		record=MembersSharePurchaseRequest(tdate=tdate,member=member,approval_status=approval_status,units=units,status=status)
		record.save()
		return HttpResponseRedirect(reverse('Members_Share_Purchase_Request_Search'))

	# form.fields['units'].initial=
	context={

	"form":form,
	"member":member,
	'task_array':task_array,
	'task_enabler_array':task_enabler_array,
	'default_password':default_password,

	'account_number':account_number,
	}
	return render(request,'deskofficer_templates/Members_Share_Purchase_Request_View.html',context)



def Members_Share_Purchase_Request_Manage_Search(request):
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	task_array=[]
	for task in tasks:
		task_array.append(task.task.title)



	task_enabler=TransactionEnabler.objects.filter(status="YES")
	task_enabler_array=[]
	for item in task_enabler:
		task_enabler_array.append(item.title)

	default_password="NO"
	if Staff.objects.filter(admin=request.user,default_password='YES'):
		default_password="YES"


	title="Search Members for Share Purchase"
	form = searchForm(request.POST or None)

	return render(request,'deskofficer_templates/Members_Share_Purchase_Request_Manage_Search.html',{'form':form,'title':title,'task_array':task_array,
	'task_enabler_array':task_enabler_array,
	'default_password':default_password,
	})


def Members_Share_Purchase_Request_Manage_list_load(request):
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	task_array=[]
	for task in tasks:
		task_array.append(task.task.title)


	task_enabler=TransactionEnabler.objects.filter(status="YES")
	task_enabler_array=[]
	for item in task_enabler:
		task_enabler_array.append(item.title)

	default_password="NO"
	if Staff.objects.filter(admin=request.user,default_password='YES'):
		default_password="YES"

	title="LIST OF MEMBERS"
	status="ACTIVE"
	form = searchForm(request.POST)

	if request.method == "POST":
		if request.POST.get("title")=="":
			return HttpResponseRedirect(reverse('Members_Share_Purchase_Request_Search'))

		members=MembersSharePurchaseRequest.objects.filter(Q(member__member__file_no__icontains=form['title'].value()) |Q(member__member__ippis_no__icontains=form['title'].value()) |Q(member__member__phone_number__icontains=form['title'].value()) | Q(member__member__admin__first_name__icontains=form['title'].value()) | Q(member__member__admin__last_name__icontains=form['title'].value()) | Q(member__member__middle_name__icontains=form['title'].value())).filter(member__member__status=status)

		context={
		'members':members,
		'title':title,
		'task_array':task_array,
	'task_enabler_array':task_enabler_array,
	'default_password':default_password,
		}
		return render(request,'deskofficer_templates/Members_Share_Purchase_Request_Manage_list_load.html',context)


def Members_Share_Purchase_Request_Manage_Details(request,pk):
	form=Members_Share_Purchase_Request_form(request.POST or None)
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	task_array=[]
	for task in tasks:
		task_array.append(task.task.title)



	task_enabler=TransactionEnabler.objects.filter(status="YES")
	task_enabler_array=[]
	for item in task_enabler:
		task_enabler_array.append(item.title)

	default_password="NO"
	if Staff.objects.filter(admin=request.user,default_password='YES'):
		default_password="YES"

	member=MembersSharePurchaseRequest.objects.get(id=pk)

	member1=MembersShareAccounts.objects.get(member__account_number=member.member.account_number)
	title="LIST OF MEMBERS"

	form.fields['units'].initial=member.units

	if request.method=="POST":
		tdate=get_current_date(now)
		status="UNTREATED"
		max_unit = SharesUnits.objects.all().order_by('unit').last()

		existing_share = member1.shares


		units=request.POST.get('units')
		if not units:
			messages.info(request,'Unit is missing')
			return HttpResponseRedirect(reverse('Members_Share_Purchase_Request_Manage_Details',args=(pk,)))


		if int(max_unit.unit) < (int(units) + int(existing_share)):
			messages.error(request,"You have exceed the Maximum Units")
			return HttpResponseRedirect(reverse('Members_Share_Purchase_Request_Manage_Details',args=(pk,)))

		member.units=units
		member.save()
		return HttpResponseRedirect(reverse('Members_Share_Purchase_Request_Manage_Search'))


	context={

	'form':form,
	'member':member,
	'task_array':task_array,
	'task_enabler_array':task_enabler_array,
	'default_password':default_password,

	}
	return render(request,'deskofficer_templates/Members_Share_Purchase_Request_Manage_Details.html',context)



def Members_Share_Purchase_Request_Manage_Details_delete_Confirmation(request,pk):
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	task_array=[]
	for task in tasks:
		task_array.append(task.task.title)

	task_enabler=TransactionEnabler.objects.filter(status="YES")
	task_enabler_array=[]
	for item in task_enabler:
		task_enabler_array.append(item.title)

	default_password="NO"
	if Staff.objects.filter(admin=request.user,default_password='YES'):
		default_password="YES"

	title = "Are you sure you want to drop this Request"
	record=MembersSharePurchaseRequest.objects.get(id=pk)
	context={
	'task_array':task_array,
	'task_enabler_array':task_enabler_array,
	'default_password':default_password,


	'record':record,
	'title':title,
	}
	return render(request,'deskofficer_templates/Members_Share_Purchase_Request_Manage_Details_delete_Confirmation.html',context)


def Members_Share_Purchase_Request_Manage_Details_delete(request,pk):
	record=MembersSharePurchaseRequest.objects.get(id=pk)
	record.delete()
	return HttpResponseRedirect(reverse('Members_Share_Purchase_Request_Manage_Search'))


def Members_Share_Purchase_Request_Process(request):
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	task_array=[]
	for task in tasks:
		task_array.append(task.task.title)

	task_enabler=TransactionEnabler.objects.filter(status="YES")
	task_enabler_array=[]
	for item in task_enabler:
		task_enabler_array.append(item.title)

	default_password="NO"
	if Staff.objects.filter(admin=request.user,default_password='YES'):
		default_password="YES"

	approval_status='APPROVED'
	status='UNTREATED'
	records=MembersSharePurchaseRequest.objects.filter(approval_status=approval_status,status=status)


	context={
	'task_array':task_array,
	'task_enabler_array':task_enabler_array,
	'default_password':default_password,


	'records':records,
	}
	return render(request,'deskofficer_templates/Members_Share_Purchase_Request_Process.html',context)


def Members_Share_Purchase_Request_Process_View(request,pk):
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	task_array=[]
	for task in tasks:
		task_array.append(task.task.title)



	task_enabler=TransactionEnabler.objects.filter(status="YES")
	task_enabler_array=[]
	for item in task_enabler:
		task_enabler_array.append(item.title)

	default_password="NO"
	if Staff.objects.filter(admin=request.user,default_password='YES'):
		default_password="YES"

	processed_by=CustomUser.objects.get(id=request.user.id)

	form=Members_Share_Purchase_Request_Process_View_Form(request.POST or None)
	record=MembersSharePurchaseRequest.objects.get(id=pk)
	member=MembersAccountsDomain.objects.get(account_number=record.member.account_number)
	transaction_receipt_category=TransactionTypes.objects.get(code='700')
	status1='ACTIVE'
	status='TREATED'
	status2='UNTREATED'
	receipt_status='UNUSED'
	receipt_status1='USED'
	tdate=get_current_date(now)

	if request.method=="POST":

		receipt_id=request.POST.get('receipt_no')

		if transaction_receipt_category.receipt_type=='MANUAL':
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

		payment_date=request.POST.get('payment_date')


		if request.FILES.get('image', False):
			image = request.FILES['image']
			fs=FileSystemStorage()
			filename=fs.save(image.name,image)
			image_url=fs.url(filename)

		else:
			image_url=None


		purpose=str(units) + " share(s) at a unit cost " + str(unit_cost)
		record_add=MembersCashDeposits(member=member.member,
										bank_accounts=bank_account,
										account_number=account_number,
										transaction=transaction_receipt_category,
										amount=total_cost,
										payment_reference=payment_reference,
										payment_evidience=image_url,
										receipt=receipt,
										purpose=purpose,
										payment_date=payment_date,
										processed_by=processed_by.username,
										status=status2,
										tdate=tdate)
		record_add.save()

		if MembersShareAccounts.objects.filter(member=member).exists():
			share_record=MembersShareAccounts.objects.filter(member=member).first()
			share_record.shares = int(share_record.shares) + int(units)
			share_record.unit_cost=unit_cost
			share_record.total_cost=float(share_record.total_cost) + float(total_cost)
			share_record.save()
		else:
			share_record=MembersShareAccounts(member=member,
											shares=units,
											unit_cost=unit_cost,
											total_cost=total_cost,
											effective_date=now,
											year=now.year,
											processed_by=processed_by.username,
											status=status2,
											tdate=tdate)
			share_record.save()


		if PersonalLedger.objects.filter(account_number=account_number).exists():
			ledger=PersonalLedger.objects.filter(account_number=account_number).order_by('id').last()

			debit=0
			credit=total_cost
			balance=float(ledger.balance) + float(total_cost)
			particulars= str(units) + " Unit(s) Share Purchase, at unit cost of " + str(unit_cost) +  " as at " + str(now)


			post_to_ledger(
						member.member,
						member.transaction,
						account_number,
						particulars,
						debit,
						credit,
						balance,
						get_current_date(now),
						status1,
						tdate,
						)

		else:
			debit=0
			credit=total_cost
			balance=float(total_cost)
			particulars= str(units) + " Unit(s) Share Purchase, at unit cost of " + str(unit_cost) +  " as at " + str(now)


			post_to_ledger(member.member,
							member.transaction,
							account_number,
							particulars,
							debit,
							credit,
							balance,
							get_current_date(now),
							status1,
							tdate)


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
	'task_array':task_array,
	'task_enabler_array':task_enabler_array,
	'default_password':default_password,


	'record':record,
	'form':form,
	'transaction_receipt_category':transaction_receipt_category,
	}
	return render(request,'deskofficer_templates/Members_Share_Purchase_Request_Process_View.html',context)



############################################################
##################### MEMBERS WELFARE ######################
############################################################
def Members_Welfare_Upload_Search(request):
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	task_array=[]
	for task in tasks:
		task_array.append(task.task.title)



	task_enabler=TransactionEnabler.objects.filter(status="YES")
	task_enabler_array=[]
	for item in task_enabler:
		task_enabler_array.append(item.title)

	default_password="NO"
	if Staff.objects.filter(admin=request.user,default_password='YES'):
		default_password="YES"

	title="Search Members for Ledger Information"
	form = searchForm(request.POST or None)

	return render(request,'deskofficer_templates/Members_Welfare_Upload_Search.html',{'form':form,'title':title,'task_array':task_array,
	'task_enabler_array':task_enabler_array,
	'default_password':default_password,
	})



def Members_Welfare_Upload_list_load(request):
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	task_array=[]
	for task in tasks:
		task_array.append(task.task.title)



	task_enabler=TransactionEnabler.objects.filter(status="YES")
	task_enabler_array=[]
	for item in task_enabler:
		task_enabler_array.append(item.title)

	default_password="NO"
	if Staff.objects.filter(admin=request.user,default_password='YES'):
		default_password="YES"


	title="LIST OF MEMBERS"
	form = searchForm(request.POST)
	status="ACTIVE"
	welfare_status = 'PENDING'
	records=[]
	if request.method == "POST":
		if request.POST.get("title")=="":
			messages.info(request,"Please Enter a search data")
			return HttpResponseRedirect(reverse('Members_Welfare_Upload_Search'))



		records=Members.objects.filter(Q(file_no__icontains=form['title'].value()) |Q(ippis_no__icontains=form['title'].value()) |Q(phone_number__icontains=form['title'].value()) | Q(admin__first_name__icontains=form['title'].value()) | Q(admin__last_name__icontains=form['title'].value()) | Q(middle_name__icontains=form['title'].value())).filter(status=status,welfare_status=welfare_status,member_category='OLD')
		if records.count() <= 0:
			messages.info(request,"No Record Found")
			return HttpResponseRedirect(reverse('Transaction_adjustment_history_Search'))


	context={
	'records':records,
	'title':title,
	'task_array':task_array,
	'task_enabler_array':task_enabler_array,
	'default_password':default_password,
	}
	return render(request,'deskofficer_templates/Members_Welfare_Upload_list_load.html',context)




def Members_Welfare_Upload_Preview(request,pk):
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	task_array=[]
	for task in tasks:
		task_array.append(task.task.title)



	task_enabler=TransactionEnabler.objects.filter(status="YES")
	task_enabler_array=[]
	for item in task_enabler:
		task_enabler_array.append(item.title)

	default_password="NO"
	if Staff.objects.filter(admin=request.user,default_password='YES'):
		default_password="YES"

	form=Existing_Welfare_Upload_form(request.POST or None)
	welfare_status='VERIFIED'
	transaction=TransactionTypes.objects.get(code=800)
	processed_by=CustomUser.objects.get(id=request.user.id)
	tdate=get_current_date(now)
	year=tdate.year

	member1=Members.objects.get(id=pk)

	member=[]
	if MembersAccountsDomain.objects.filter(member_id=pk,transaction=transaction).exists():
		member=MembersAccountsDomain.objects.get(member_id=pk,transaction=transaction)

	if request.method=="POST":

		transaction_period=TransactionPeriods.objects.get(status='ACTIVE')

		status='UNTREATED'
		status1='ACTIVE'

		amount=request.POST.get('amount')

		if not member:
			messages.info(request,'Account Number not Available')
			return HttpResponseRedirect(reverse('Members_Welfare_Upload_Preview',args=(pk,)))

		account_number=member.account_number

		if MembersWelfareAccounts.objects.filter(member=member).exists():
			messages.info(request,'Record Already Upload for This Member')
			return HttpResponseRedirect(reverse('Members_Welfare_Upload_Preview',args=(pk,)))

		record=MembersWelfareAccounts(member=member,
									amount=amount,
									status=status,
									year=year,
									tdate=tdate,
									processed_by=processed_by.username)
		record.save()

		member1.welfare_status=welfare_status
		member1.save()

		return HttpResponseRedirect(reverse('Members_Welfare_Upload_Search'))


	context={

	'member':member,
	'form':form,
	'task_array':task_array,
	'task_enabler_array':task_enabler_array,
	'default_password':default_password,
	}
	return render(request,'deskofficer_templates/Members_Welfare_Upload_Preview.html',context)



############################################################
##################### CASH DEPOSIT    ######################
############################################################
def Cash_Deposit_Shares_Search(request):
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	task_array=[]
	for task in tasks:
		task_array.append(task.task.title)



	task_enabler=TransactionEnabler.objects.filter(status="YES")
	task_enabler_array=[]
	for item in task_enabler:
		task_enabler_array.append(item.title)

	default_password="NO"
	if Staff.objects.filter(admin=request.user,default_password='YES'):
		default_password="YES"

	title="Search Members for Cash Deposit for Shares"
	form = searchForm(request.POST or None)

	return render(request,'deskofficer_templates/Cash_Deposit_Shares_Search.html',{'form':form,'title':title,'task_array':task_array,
	'task_enabler_array':task_enabler_array,
	'default_password':default_password,})


def Cash_Deposit_Shares_list_load(request):
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	task_array=[]
	for task in tasks:
		task_array.append(task.task.title)



	task_enabler=TransactionEnabler.objects.filter(status="YES")
	task_enabler_array=[]
	for item in task_enabler:
		task_enabler_array.append(item.title)

	default_password="NO"
	if Staff.objects.filter(admin=request.user,default_password='YES'):
		default_password="YES"

	title="LIST OF MEMBERS"
	transaction=TransactionTypes.objects.get(code='700')
	status="ACTIVE"
	form = searchForm(request.POST)

	if request.method == "POST":
		if request.POST.get("title")=="":
			return HttpResponseRedirect(reverse('Cash_Deposit_Welfare_Search'))

		members=MembersAccountsDomain.objects.filter(Q(member__file_no__icontains=form['title'].value()) |Q(member__ippis_no__icontains=form['title'].value()) |Q(member__phone_number__icontains=form['title'].value()) | Q(member__admin__first_name__icontains=form['title'].value()) | Q(member__admin__last_name__icontains=form['title'].value()) | Q(member__middle_name__icontains=form['title'].value())).filter(transaction=transaction)

		context={
		'members':members,
		'title':title,
		'task_array':task_array,
	'task_enabler_array':task_enabler_array,
	'default_password':default_password,

		}
		return render(request,'deskofficer_templates/Cash_Deposit_Shares_list_load.html',context)


def Cash_Deposit_Shares_Preview(request,pk):
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	task_array=[]
	for task in tasks:
		task_array.append(task.task.title)



	task_enabler=TransactionEnabler.objects.filter(status="YES")
	task_enabler_array=[]
	for item in task_enabler:
		task_enabler_array.append(item.title)

	default_password="NO"
	if Staff.objects.filter(admin=request.user,default_password='YES'):
		default_password="YES"

	form=Cash_Deposit_Shares_Preview_Form(request.POST or None)
	member=MembersAccountsDomain.objects.get(id=pk)
	transaction=TransactionTypes.objects.get(code='700')
	account_number=member.account_number
	max_share_obj=SharesUnits.objects.last()
	max_share=max_share_obj.unit
	status1='ACTIVE'

	unit_cost_selected=0
	if MembersShareConfigurations.objects.all().exists():
		unit_cost_obj=MembersShareConfigurations.objects.first()
		unit_cost_selected=unit_cost_obj.unit_cost

	if request.method=="POST":
		tdate=get_current_date(now)
		status='UNTREATED'
		receipt_status='UNUSED'
		receipt_status1='USED'
		receipt_id=request.POST.get('receipt_no')

		if transaction.receipt_type == 'MANUAL':
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
		purpose = request.POST.get('narration')
		payment_date = request.POST.get('payment_date')
		payment_reference = request.POST.get('payment_reference')
		account_id = request.POST.get('account')
		bank_accounts=CooperativeBankAccounts.objects.get(id=account_id)
		processed_by=CustomUser.objects.get(id=request.user.id)

		if not units or units=='0':
			messages.info(request,'Unit is Missing')
			return HttpResponseRedirect(reverse('Cash_Deposit_Shares_Preview',args=(pk,)))

		if not unit_cost or unit_cost=='0':
			messages.info(request,'Unit cost is Missing')
			return HttpResponseRedirect(reverse('Cash_Deposit_Shares_Preview',args=(pk,)))

		if not total_amount or total_amount=='0':
			messages.info(request,'Amount Paid is Missing')
			return HttpResponseRedirect(reverse('Cash_Deposit_Shares_Preview',args=(pk,)))

		if not purpose:
			messages.info(request,'Purpose is Missing')
			return HttpResponseRedirect(reverse('Cash_Deposit_Shares_Preview',args=(pk,)))

		if not payment_reference:
			messages.info(request,'Payment Reference is Missing')
			return HttpResponseRedirect(reverse('Cash_Deposit_Shares_Preview',args=(pk,)))


		if float(total_amount) != float(unit_cost) * float(units):
			messages.info(request,'Invalid Amount Specification')
			return HttpResponseRedirect(reverse('Cash_Deposit_Shares_Preview', args=(pk,)))


		if request.FILES.get('image', False):
			image = request.FILES['image']
			fs=FileSystemStorage()
			filename=fs.save(image.name,image)
			image_url=fs.url(filename)
		else:
			image_url=None


		if MembersShareAccounts.objects.filter(member=member).exists():
			record=MembersShareAccounts.objects.filter(member=member).first()

			if (int(record.shares) + int(units)) > int(record.member.member.shares):
				messages.info(request,'You have exceeded maximum shares allowed')
				return HttpResponseRedirect(reverse('Cash_Deposit_Shares_Preview', args=(pk,)))

			record.shares=int(record.shares) + int(units)
			record.unit_cost=unit_cost
			record.total_cost=float(record.total_cost) + float(total_amount)
			record.save()

		else:
			messages.info(request,'Account Does not exist')
			return HttpResponseRedirect(reverse('Cash_Deposit_Shares_Preview', args=(pk,)))

		cash_record=MembersCashDeposits(status=status,tdate=tdate,receipt=receipt,payment_evidience=image_url,bank_accounts=bank_accounts,member=member.member,transaction=transaction,account_number=account_number,amount=total_amount,payment_reference=payment_reference,payment_date=payment_date,purpose=purpose,processed_by=processed_by.username)
		cash_record.save()

		ledger=PersonalLedger.objects.filter(account_number=account_number).order_by('id').last()


		debit=0
		credit=total_amount
		balance=float(ledger.balance) + float(total_amount)
		particulars= str(units) + " Unit(s) Share Payment, at unit cost of " + str(unit_cost) +  " as at " + str(now)


		post_to_ledger(
					member.member,
					transaction,
					account_number,
					particulars,
					debit,
					credit,
					balance,
					get_current_date(now),
					status1,
					tdate,
					)
		messages.success(request,'Record Saved Successfully')
		return HttpResponseRedirect(reverse('Cash_Deposit_Shares_Preview', args=(pk,)))

	form.fields['unit_cost'].initial=unit_cost_selected
	form.fields['payment_date'].initial=now


	context={
	'task_array':task_array,
	'task_enabler_array':task_enabler_array,
	'default_password':default_password,

	'member':member,
	'form':form,
	}
	return render(request,'deskofficer_templates/Cash_Deposit_Shares_Preview.html',context)



def Cash_Deposit_Welfare_Search(request):
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	task_array=[]
	for task in tasks:
		task_array.append(task.task.title)



	task_enabler=TransactionEnabler.objects.filter(status="YES")
	task_enabler_array=[]
	for item in task_enabler:
		task_enabler_array.append(item.title)

	default_password="NO"
	if Staff.objects.filter(admin=request.user,default_password='YES'):
		default_password="YES"


	title="Search Members for Cash Deposit for Welfare"
	form = searchForm(request.POST or None)

	return render(request,'deskofficer_templates/Cash_Deposit_Welfare_Search.html',{'form':form,'title':title,'task_array':task_array,
	'task_enabler_array':task_enabler_array,
	'default_password':default_password,})


def Cash_Deposit_Welfare_list_load(request):
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	task_array=[]
	for task in tasks:
		task_array.append(task.task.title)



	task_enabler=TransactionEnabler.objects.filter(status="YES")
	task_enabler_array=[]
	for item in task_enabler:
		task_enabler_array.append(item.title)

	default_password="NO"
	if Staff.objects.filter(admin=request.user,default_password='YES'):
		default_password="YES"


	title="LIST OF MEMBERS"
	transaction=TransactionTypes.objects.get(code='800')
	status="ACTIVE"
	form = searchForm(request.POST)

	if request.method == "POST":
		if request.POST.get("title")=="":
			return HttpResponseRedirect(reverse('Cash_Deposit_Welfare_Search'))
		members=MembersAccountsDomain.objects.filter(Q(member__file_no__icontains=form['title'].value()) |Q(member__ippis_no__icontains=form['title'].value()) |Q(member__phone_number__icontains=form['title'].value()) | Q(member__admin__first_name__icontains=form['title'].value()) | Q(member__admin__last_name__icontains=form['title'].value()) | Q(member__middle_name__icontains=form['title'].value())).filter(transaction=transaction)

		context={
		'members':members,
		'title':title,
		'task_array':task_array,
	'task_enabler_array':task_enabler_array,
	'default_password':default_password,

		}
		return render(request,'deskofficer_templates/Cash_Deposit_Welfare_list_load.html',context)


def Cash_Deposit_Welfare_Preview(request,pk):
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	task_array=[]
	for task in tasks:
		task_array.append(task.task.title)



	task_enabler=TransactionEnabler.objects.filter(status="YES")
	task_enabler_array=[]
	for item in task_enabler:
		task_enabler_array.append(item.title)

	default_password="NO"
	if Staff.objects.filter(admin=request.user,default_password='YES'):
		default_password="YES"


	form=Cash_Deposit_Welfare_Preview_Form(request.POST or None)

	transaction=TransactionTypes.objects.get(code='800')
	status = 'UNTREATED'
	receipt_status='UNUSED'
	receipt_status1='USED'
	tdate=get_current_date(now)
	processed_by=CustomUser.objects.get(id=request.user.id)


	member=MembersAccountsDomain.objects.get(id=pk)

	if request.method=="POST":
		enforce_payment=request.POST.get('enforce_payment')


		receipt_id=request.POST.get('receipt_no')

		if transaction.receipt_type=='MANUAL':
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

		amount = request.POST.get('amount')
		if not amount or amount =='0':
			messages.error(request,'Paid Amount is Missing')
			return HttpResponseRedirect(reverse('Cash_Deposit_Welfare_Preview',args=(pk,)))

		payment_reference = request.POST.get('payment_reference')
		if not payment_reference:
			messages.error(request,'Payment reference is Missing')
			return HttpResponseRedirect(reverse('Cash_Deposit_Welfare_Preview',args=(pk,)))

		purpose = request.POST.get('narration')
		if not purpose:
			messages.error(request,'Narration is Missing')
			return HttpResponseRedirect(reverse('Cash_Deposit_Welfare_Preview',args=(pk,)))

		year = request.POST.get('year')
		if not year:
			messages.error(request,'Year is Missing')
			return HttpResponseRedirect(reverse('Cash_Deposit_Welfare_Preview',args=(pk,)))

		payment_date = request.POST.get('payment_date')



		account_id = request.POST.get('account')
		bank_accounts=CooperativeBankAccounts.objects.get(id=account_id)


		if request.FILES.get('image', False):
			image = request.FILES['image']
			fs=FileSystemStorage()
			filename=fs.save(image.name,image)
			image_url=fs.url(filename)
		else:
			image_url=None

		if not enforce_payment:
			if MembersWelfareAccounts.objects.filter(member=member,year=year).exists():
				messages.info(request,'Record Already Exist for this Member for Year Entered')
				return HttpResponseRedirect(reverse('Cash_Deposit_Welfare_Preview',args=(pk,)))



		MembersCashDeposits(member=member.member,
							bank_accounts=bank_accounts,
							account_number=member.account_number,
							transaction=transaction,
							amount=amount,
							payment_reference=payment_reference,
							payment_evidience=image_url,
							receipt=receipt,
							purpose=purpose,
							payment_date=payment_date,
							processed_by=processed_by.username,
							status=status,
							tdate=tdate).save()


		if MembersWelfareAccounts.objects.filter(member=member,year=year).exists():
			record_exist=MembersWelfareAccounts.objects.filter(member=member,year=year).first()
			amount_exist=record_exist.amount

			record_exist.amount=float(amount) + float(amount_exist)
			record_exist.save()
			messages.success(request,'Record Updated Successfully')
		else:
			MembersWelfareAccounts(member=member,
									amount=amount,
									year=year,
									status=status,
									tdate=tdate,
									processed_by=processed_by.username).save()
			messages.success(request,'Record Saved Successfully')
		return HttpResponseRedirect(reverse('Cash_Deposit_Welfare_Search'))

	form.fields['payment_date'].initial=now


	context={
	'task_array':task_array,
	'task_enabler_array':task_enabler_array,
	'default_password':default_password,

	'member':member,
	'form':form,
	}
	return render(request,'deskofficer_templates/Cash_Deposit_Welfare_Preview.html',context)


def Cash_Deposit_Savings_Search(request):
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	task_array=[]
	for task in tasks:
		task_array.append(task.task.title)



	task_enabler=TransactionEnabler.objects.filter(status="YES")
	task_enabler_array=[]
	for item in task_enabler:
		task_enabler_array.append(item.title)


	default_password="NO"
	if Staff.objects.filter(admin=request.user,default_password='YES'):
		default_password="YES"

	title="Search Members for Cash Deposit"
	form = searchForm(request.POST or None)

	return render(request,'deskofficer_templates/Cash_Deposit_Savings_Search.html',{'form':form,'title':title,'task_array':task_array,
	'task_enabler_array':task_enabler_array,
	'default_password':default_password,})



def Cash_Deposit_Savings_list_load(request):
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	task_array=[]
	for task in tasks:
		task_array.append(task.task.title)



	task_enabler=TransactionEnabler.objects.filter(status="YES")
	task_enabler_array=[]
	for item in task_enabler:
		task_enabler_array.append(item.title)

	default_password="NO"
	if Staff.objects.filter(admin=request.user,default_password='YES'):
		default_password="YES"

	title="LIST OF MEMBERS"
	form = searchForm(request.POST)
	status="ACTIVE"

	if request.method == "POST":
		if request.POST.get("title")=="":
			return HttpResponseRedirect(reverse('Cash_Deposit_Savings_Search'))

		members=searchMembers(form['title'].value(),status)
		# members=Members.objects.filter(Q(file_no__icontains=form['title'].value()) |Q(ippis_no__icontains=form['title'].value()) |Q(phone_number__icontains=form['title'].value()) | Q(admin__first_name__icontains=form['title'].value()) | Q(admin__last_name__icontains=form['title'].value()) | Q(middle_name__icontains=form['title'].value())).filter(status=status)


		context={
		'members':members,
		'title':title,
		'task_array':task_array,
	'task_enabler_array':task_enabler_array,
	'default_password':default_password,
		}
		return render(request,'deskofficer_templates/Cash_Deposit_Savings_list_load.html',context)


def Cash_Deposit_Savings_Load(request,pk):
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	task_array=[]
	for task in tasks:
		task_array.append(task.task.title)



	task_enabler=TransactionEnabler.objects.filter(status="YES")
	task_enabler_array=[]
	for item in task_enabler:
		task_enabler_array.append(item.title)

	default_password="NO"
	if Staff.objects.filter(admin=request.user,default_password='YES'):
		default_password="YES"

	member=Members.objects.get(id=pk)
	records=MembersAccountsDomain.objects.filter(member=member,transaction__source__title="SAVINGS")

	context={
	'task_array':task_array,
	'task_enabler_array':task_enabler_array,
	'default_password':default_password,
	'records':records,
	'member':member,
	}
	return render(request,'deskofficer_templates/Cash_Deposit_Savings_Load.html',context)


def Cash_Deposit_Savings_Preview(request,pk):
	form=Cash_Deposit_Savings_form(request.POST or None)
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	task_array=[]
	for task in tasks:
		task_array.append(task.task.title)



	task_enabler=TransactionEnabler.objects.filter(status="YES")
	task_enabler_array=[]
	for item in task_enabler:
		task_enabler_array.append(item.title)


	default_password="NO"
	if Staff.objects.filter(admin=request.user,default_password='YES'):
		default_password="YES"

	receipt_status='UNUSED'
	receipt_status1='USED'
	status1='ACTIVE'
	processed_by=CustomUser.objects.get(id=request.user.id)
	status='UNTREATED'
	tdate=get_current_date(now)

	member=MembersAccountsDomain.objects.get(id=pk)



	if request.method=="POST":
		if member.transaction.receipt_type == 'MANUAL':
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

		if not amount  or amount=='0':
			messages.info(request,'Paid Amount is Missing')
			return HttpResponseRedirect(reverse('Cash_Deposit_Savings_Preview',args=(pk,)))

		if not purpose:
			messages.info(request,'Purpose is Missing')
			return HttpResponseRedirect(reverse('Cash_Deposit_Savings_Preview',args=(pk,)))

		if not payment_reference:
			messages.info(request,'Payment Reference is Missing')
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

			cash_record=MembersCashDeposits(tdate=tdate,status=status,receipt=receipt,payment_evidience=payment_evidience_url,bank_accounts=bank_accounts,member=member.member,transaction=transaction,account_number=account_number,amount=amount,payment_reference=payment_reference,payment_date=payment_date,purpose=purpose,processed_by=processed_by.username)
			cash_record.save()


			post_to_ledger(
						member.member,
						transaction,
						account_number,
						particulars,
						debit,
						credit,
						balance,
						transaction_period,
						status1,
						tdate,
						)

			messages.success(request,'Payment Posted Successfully')
			return HttpResponseRedirect(reverse('Cash_Deposit_Savings_Load',args=(member.member.pk,)))
		else:

			cash_record=MembersCashDeposits(tdate=tdate,status=status,receipt=receipt,payment_evidience=payment_evidience_url,bank_accounts=bank_accounts,member=member.member,transaction=transaction,account_number=account_number,amount=amount,payment_reference=payment_reference,payment_date=payment_date,purpose=purpose,processed_by=processed_by.username)
			cash_record.save()


			post_to_ledger(
						member.member,
						transaction,
						account_number,
						particulars,
						debit,
						credit,
						balance,
						transaction_period,
						status1,
						tdate,
						)


			messages.success(request,'Payment Posted Successfully')
			return HttpResponseRedirect(reverse('Cash_Deposit_Savings_Load',args=(member.member.pk,)))

	form.fields['payment_date'].initial= now


	context={

	'member':member,
	'form':form,
	'task_array':task_array,
	'task_enabler_array':task_enabler_array,
	'default_password':default_password,
	# 'transaction':transaction,
	}
	return render(request,'deskofficer_templates/Cash_Deposit_Savings_Preview.html',context)


def Cash_Deposit_Loans_Search(request):
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	task_array=[]
	for task in tasks:
		task_array.append(task.task.title)



	task_enabler=TransactionEnabler.objects.filter(status="YES")
	task_enabler_array=[]
	for item in task_enabler:
		task_enabler_array.append(item.title)

	default_password="NO"
	if Staff.objects.filter(admin=request.user,default_password='YES'):
		default_password="YES"

	title="Search Members for Cash Deposit"
	form = searchForm(request.POST or None)

	return render(request,'deskofficer_templates/Cash_Deposit_Loans_Search.html',{'form':form,'title':title,'task_array':task_array,
	'task_enabler_array':task_enabler_array,
	'default_password':default_password,})


def Cash_Deposit_Loan_list_load(request):
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	task_array=[]
	for task in tasks:
		task_array.append(task.task.title)



	task_enabler=TransactionEnabler.objects.filter(status="YES")
	task_enabler_array=[]
	for item in task_enabler:
		task_enabler_array.append(item.title)

	default_password="NO"
	if Staff.objects.filter(admin=request.user,default_password='YES'):
		default_password="YES"

	title="LIST OF MEMBERS"
	status="ACTIVE"
	form = searchForm(request.POST)

	if request.method == "POST":
		if request.POST.get("title")=="":
			return HttpResponseRedirect(reverse('Cash_Deposit_Loans_Search'))

		members=searchMembers(form['title'].value(),status)
		# members=Members.objects.filter(Q(file_no__icontains=form['title'].value()) |Q(ippis_no__icontains=form['title'].value()) |Q(phone_number__icontains=form['title'].value()) | Q(admin__first_name__icontains=form['title'].value()) | Q(admin__last_name__icontains=form['title'].value()) | Q(middle_name__icontains=form['title'].value())).filter(status=status)

		context={
		'members':members,
		'title':title,
		'task_array':task_array,
	'task_enabler_array':task_enabler_array,
	'default_password':default_password,
		}
		return render(request,'deskofficer_templates/Cash_Deposit_Loan_list_load.html',context)


def Cash_Deposit_Loans_Preview(request,pk):
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	task_array=[]
	for task in tasks:
		task_array.append(task.task.title)



	task_enabler=TransactionEnabler.objects.filter(status="YES")
	task_enabler_array=[]
	for item in task_enabler:
		task_enabler_array.append(item.title)

	default_password="NO"
	if Staff.objects.filter(admin=request.user,default_password='YES'):
		default_password="YES"

	form=Cash_Deposit_Loans_form(request.POST or None)
	status1='ACTIVE'
	status='INACTIVE'
	tdate=get_current_date(now)
	processed_by=CustomUser.objects	.get(id=request.user.id)
	transaction_status='UNTREATED'
	loan_status='INACTIVE'
	processed_by=CustomUser.objects	.get(id=request.user.id)



	member=Members.objects.get(id=pk)
	loans=[]
	loan_cleared_status=False

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
		transaction_period=get_current_date(now)
		debit=0
		credit=amount

		if PersonalLedger.objects.filter(member=member,transaction=transaction,account_number=account_number).exists():
			ledger=PersonalLedger.objects.filter(member=member,transaction=transaction,account_number=account_number).last()
			ledger_balance=ledger.balance
			balance=float(ledger_balance)+float(amount)

			cash_record=MembersCashDeposits(member=member,
											bank_accounts=bank_accounts,
											account_number=account_number,
											transaction=transaction,
											amount=amount,
											payment_reference=payment_reference,
											purpose=purpose,
											payment_evidience=payment_evidience_url,
											payment_date=payment_date,
											processed_by=processed_by.username,
											status=transaction_status,
											tdate=tdate,
											)
			cash_record.save()

			loan_record=LoansRepaymentBase.objects.get(loan_number=account_number)
			loan_record.amount_paid=float(loan_record.amount_paid)+float(amount)
			loan_record.balance=float(loan_record.balance)+float(amount)
			loan_record.save()

			# if loan_record.loan_merge_status==loan_merge_status:
			# 	loan_groups=LoansRepaymentBase.objects.filter(merge_account_number=loan_record.loan_number)
			# 	merge_paid_amount=float(amount)

			# 	for loan_group in loan_groups:
			# 		entity_balance=loan_group.balance

			# 		if float(merge_paid_amount) >= abs(float(entity_balance)):
			# 			new_entity_amount_paid= float(entity_balance)

			# 			new_entity_balance=float(entity_balance)+float(new_entity_amount_paid)

			# 			merge_paid_amount=float(merge_paid_amount)-(float(new_entity_amount_paid))
			# 		else:
			# 			new_entity_amount_paid=float(merge_paid_amount)
			# 			new_entity_balance=float(entity_balance.balance)+(float(merge_paid_amount))
			# 			merge_paid_amount=0

			# 		loan_group.amount_paid=float(loan_group.amount_paid)+ float(new_entity_amount_paid)
			# 		loan_group.balance=float(new_entity_balance)
			# 		loan_group.save()


			# 		if loan_group.balance >=0:
			# 			loan_cleared_status=True

			# 			loan_group.status=loan_status
			# 			loan_group.save()

			# 			record_cleared=LoansCleared(loan=loan_group,
			# 										processed_by=processed_by.username,
			# 										status=transaction_status,
			# 										tdate=tdate)
			# 			record_cleared.save()

			# else:

			loan_group=LoansRepaymentBase.objects.filter(loan_number=account_number).update(amount_paid=F("amount_paid")+float(amount),balance=F("balance")+float(amount))

			if LoansRepaymentBase.objects.filter(loan_number=account_number).filter(Q(balance__gte=0)):
				loan_cleared_status=True
				record_update=LoansRepaymentBase.objects.filter(loan_number=account_number).update(status=loan_status)


				loan=LoansRepaymentBase.objects.get(loan_number=account_number)
				record_cleared=LoansCleared(loan=loan,
											processed_by=processed_by.username,
											status=transaction_status,
											tdate=tdate)
				record_cleared.save()



			if LoansRepaymentBase.objects.filter(loan_number=account_number).filter(Q(balance__gte=0)).exists():

				loan_record.status=status
				loan_record.save()



			post_to_ledger(member,
							transaction,
							account_number,
							particulars,
							debit,
							credit,
							balance,
							transaction_period,
							status1,
							tdate,
							)

			if loan_cleared_status:
				PersonalLedger.objects.filter(member=member,transaction=transaction,account_number=account_number).update(status=status)

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
	'task_array':task_array,
	'task_enabler_array':task_enabler_array,
	'default_password':default_password,
	}
	return render(request,'deskofficer_templates/Cash_Deposit_Loans_Preview.html',context)



############################################################
##################### CASH WITHDRAWALN######################
############################################################
def Xmas_Savings_Shortlisting_list_Load(request):
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	task_array=[]
	for task in tasks:
		task_array.append(task.task.title)


	status='UNTREATED'
	tdate=get_current_date(now)
	processed_by=CustomUser.objects.get(id=request.user.id)


	members_array=[]
	button_enabled=False


	task_enabler=TransactionEnabler.objects.filter(status="YES")
	task_enabler_array=[]
	for item in task_enabler:
		task_enabler_array.append(item.title)

	default_password="NO"
	if Staff.objects.filter(admin=request.user,default_password='YES'):
		default_password="YES"

	form=Xmas_Savings_Shortlisting_form(request.POST or None)
	title="LIST OF MEMBERS FOR XMAS SAVINGS SHORTLISTING"
	transaction=TransactionTypes.objects.get(code='103')

	if request.method == 'POST' and 'btn-fetch' in request.POST:
		transaction_date=request.POST.get('transaction_date')
		batch=request.POST.get("batch")


		date_format = '%Y-%m-%d'
		dtObj = datetime.datetime.strptime(transaction_date, date_format)
		transaction_date=get_current_date(dtObj)



		members=MembersAccountsDomain.objects.filter(transaction=transaction)
		for member in members:
			if PersonalLedger.objects.filter(account_number=member.account_number).exists():
				record=PersonalLedger.objects.filter(account_number=member.account_number).last()
				if record.balance >0:
					members_array.append((member.member.get_member_Id,member.member.get_full_name,record.account_number,record.balance))

		if members_array:
			button_enabled=True

		if Xmas_Savings_Generated.objects.filter(batch=batch).exists():
			button_enabled=False

	if request.method == 'POST' and 'btn-submit' in request.POST:
		submission_status='PENDING'
		processing_status='UNPROCESSED'
		account_status='NO'
		transaction_date=request.POST.get('transaction_date')
		batch_id=request.POST.get("batch")
		batch=Commodity_Period_Batch.objects.get(id=batch_id)

		date_format = '%Y-%m-%d'
		dtObj = datetime.datetime.strptime(transaction_date, date_format)
		transaction_date=get_current_date(dtObj)

		year = transaction_date.year
		batch= str(year) + " " + batch.title

		if Xmas_Savings_Generated.objects.filter(batch=batch).exists():
			messages.error(request,'Data Already Generated for this Year')
			return HttpResponseRedirect(reverse('Xmas_Savings_Shortlisting_list_Load'))

		if not transaction_date:
			messages.error(request,'Please select Transaction Period')
			return HttpResponseRedirect(reverse('Xmas_Savings_Shortlisting_list_Load'))

		members=MembersAccountsDomain.objects.filter(transaction=transaction)
		for member in members:
			if PersonalLedger.objects.filter(account_number=member.account_number).exists():
				record=PersonalLedger.objects.filter(account_number=member.account_number).last()
				if record.balance >0:

					Xmas_Savings_Shortlist(transaction=member,
										amount=record.balance,
										period=transaction_date,
										payment_channel='CASH',
										status=status,
										batch=batch,
										submission_status=submission_status,
										processing_status=processing_status,
										account_status=account_status,
										processed_by=processed_by.username,
										tdate=tdate).save()
		Xmas_Savings_Generated(batch=batch,processed_by=processed_by.username,tdate=tdate).save()

		messages.success(request,'Records Submitted Successfully')
		return HttpResponseRedirect(reverse('deskofficer_home'))


	form.fields['transaction_date'].initial=now

	context={
	'form':form,
	'members_array':members_array,
	'title':title,
	'task_array':task_array,
	'task_enabler_array':task_enabler_array,
	'default_password':default_password,
	'button_enabled':button_enabled,

	}
	return render(request,'deskofficer_templates/Xmas_Savings_Shortlisting_list_Load.html',context)



def Xmas_Savings_Shortlisting_Filter_Batch_Load(request):
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	task_array=[]
	for task in tasks:
		task_array.append(task.task.title)
	transaction=TransactionTypes.objects.get(code='103')



	form=Xmas_Savings_Shortlisting_Export_form(request.POST or None)


	task_enabler=TransactionEnabler.objects.filter(status="YES")
	task_enabler_array=[]
	for item in task_enabler:
		task_enabler_array.append(item.title)

	default_password="NO"
	if Staff.objects.filter(admin=request.user,default_password='YES'):
		default_password="YES"

	if request.method == 'POST':
		batch=request.POST.get('batch')
		return HttpResponseRedirect(reverse('Xmas_Savings_Shortlisting_Filter_List_Load',args=(batch,'CASH',)))
	context={
	'task_array':task_array,
	'task_enabler_array':task_enabler_array,
	'default_password':default_password,
	'form':form,
	}
	return render(request,'deskofficer_templates/Xmas_Savings_Shortlisting_Filter_Batch_Load.html',context)


def Xmas_Savings_Shortlisting_Filter_List_Load(request,batch,payment):
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	task_array=[]
	for task in tasks:
		task_array.append(task.task.title)

	status='TREATED'


	task_enabler=TransactionEnabler.objects.filter(status="YES")
	task_enabler_array=[]
	for item in task_enabler:
		task_enabler_array.append(item.title)

	default_password="NO"
	if Staff.objects.filter(admin=request.user,default_password='YES'):
		default_password="YES"

	form=Xmas_Savings_Shortlisting_Export_form(request.POST or None)


	if request.method == 'POST' and 'btn-fetch' in request.POST:
		category=request.POST.get("category")
		records=Xmas_Savings_Shortlist.objects.filter(batch=batch,payment_channel=category).exclude(status=status)

		context={
		'task_array':task_array,
		'form':form,
		'records':records,
		'batch':batch,
		'payment':category,
		'task_enabler_array':task_enabler_array,
	'default_password':default_password,
		}
		return render(request,'deskofficer_templates/Xmas_Savings_Shortlisting_Filter_List_Load.html',context)

	if request.method == 'POST' and 'btn-process' in request.POST:
		category=request.POST.get("category")

		if Xmas_Savings_Shortlist.objects.filter(batch=batch,payment_channel=category).exclude(status=status).exists():
			Xmas_Savings_Shortlist.objects.filter(batch=batch,payment_channel=category).exclude(status=status).update(status=status)
		else:
			messages.error(request,'No Record Found')

		return HttpResponseRedirect(reverse('Xmas_Savings_Shortlisting_Filter_List_Load',args=(batch,category)))


	records=Xmas_Savings_Shortlist.objects.filter(batch=batch,payment_channel=payment).exclude(status=status)

	context={
	'task_array':task_array,
	'form':form,
	'records':records,
	'batch':batch,
	'payment':payment,
	'task_enabler_array':task_enabler_array,
	'default_password':default_password,
	}
	return render(request,'deskofficer_templates/Xmas_Savings_Shortlisting_Filter_List_Load.html',context)


def Xmas_Savings_Shortlisting_Switching(request,pk):
	item=Xmas_Savings_Shortlist.objects.get(id=pk)
	batch=item.batch
	payment=item.payment_channel

	if item.payment_channel == "CASH":
		item.payment_channel='TRANSFERRED'
	else:
		item.payment_channel='CASH'
	item.save()
	return HttpResponseRedirect(reverse('Xmas_Savings_Shortlisting_Filter_List_Load',args=(batch,payment,)))


def Xmas_Savings_Shortlisting_Account_Linkage_Batch_Load(request):
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	task_array=[]
	for task in tasks:
		task_array.append(task.task.title)


	transaction=TransactionTypes.objects.get(code='103')

	form=Xmas_Savings_Shortlisting_Export_form(request.POST or None)


	task_enabler=TransactionEnabler.objects.filter(status="YES")
	task_enabler_array=[]
	for item in task_enabler:
		task_enabler_array.append(item.title)

	default_password="NO"
	if Staff.objects.filter(admin=request.user,default_password='YES'):
		default_password="YES"

	if request.method == 'POST':
		batch=request.POST.get('batch')
		payment=request.POST.get('category')
		return HttpResponseRedirect(reverse('Xmas_Savings_Shortlisting_Account_Linkage_List_Load',args=(batch,payment,)))
	context={
	'task_array':task_array,
	'task_enabler_array':task_enabler_array,
	'default_password':default_password,
	'form':form,
	}
	return render(request,'deskofficer_templates/Xmas_Savings_Shortlisting_Account_Linkage_Batch_Load.html',context)


def Xmas_Savings_Shortlisting_Account_Linkage_List_Load(request,batch,payment):
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	task_array=[]
	for task in tasks:
		task_array.append(task.task.title)

	status='TREATED'
	processing_status='UNPROCESSED'


	task_enabler=TransactionEnabler.objects.filter(status="YES")
	task_enabler_array=[]
	for item in task_enabler:
		task_enabler_array.append(item.title)

	default_password="NO"
	if Staff.objects.filter(admin=request.user,default_password='YES'):
		default_password="YES"

	if payment == "CASH":
		account_status='NO'
		records=Xmas_Savings_Shortlist.objects.filter(batch=batch,payment_channel=payment,status=status,account_status=account_status,processing_status=processing_status)

		context={
		'task_array':task_array,
		'records':records,
		'batch':batch,
		'payment':payment,
		'task_enabler_array':task_enabler_array,
	'default_password':default_password,
		}
		return render(request,'deskofficer_templates/Xmas_Savings_Shortlisting_Account_Linkage_List_Load.html',context)

	elif payment == 'TRANSFERRED':
		code=0
		if XmasTransferDefaultSaving.objects.all().exists():
			default_account=XmasTransferDefaultSaving.objects.all().first()
			code=default_account.transaction.code

		account_status='NO'
		records=Xmas_Savings_Shortlist.objects.filter(batch=batch,payment_channel=payment,status=status,account_status=account_status,processing_status=processing_status)

		context={
		'task_array':task_array,
		'records':records,
		'batch':batch,
		'payment':payment,
		'task_enabler_array':task_enabler_array,
	'default_password':default_password,
		'code':code,
		}
		return render(request,'deskofficer_templates/Xmas_Savings_Shortlisting_Account_Transfer_List_Load.html',context)




def Xmas_Savings_Shortlisting_Account_Assignment_Load_Default(request,batch,payment):
	status='TREATED'
	processing_status='UNPROCESSED'
	account_status='NO'
	account_status1='YES'
	records=Xmas_Savings_Shortlist.objects.filter(batch=batch,payment_channel=payment,status=status,account_status=account_status,processing_status=processing_status)
	if records:
		for record in records:
			if MembersBankAccounts.objects.filter(member_id=record.transaction.member).exists():
				selected_account=MembersBankAccounts.objects.filter(member_id=record.transaction.member).order_by('account_priority').first()
				record.bank_account=selected_account
				record.account_status=account_status1
				record.save()
	else:
		messages.error(request,'No Record Found')

	return HttpResponseRedirect(reverse('Xmas_Savings_Shortlisting_Account_Linkage_List_Load',args=(batch,payment,)))


def Xmas_Savings_Shortlisting_Account_Assignment(request,pk):
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	task_array=[]
	for task in tasks:
		task_array.append(task.task.title)



	task_enabler=TransactionEnabler.objects.filter(status="YES")
	task_enabler_array=[]
	for item in task_enabler:
		task_enabler_array.append(item.title)

	default_password="NO"
	if Staff.objects.filter(admin=request.user,default_password='YES'):
		default_password="YES"

	member=Xmas_Savings_Shortlist.objects.get(id=pk)
	if request.method == 'POST':
		account_status='YES'
		account_id=request.POST.get('account')
		account=MembersBankAccounts.objects.get(id=account_id)

		member.bank_account=account
		member.account_status=account_status
		member.details="Xmas Savings payment"
		member.save()
		return HttpResponseRedirect(reverse('Xmas_Savings_Shortlisting_Account_Linkage_List_Load',args=(member.batch,member.payment_channel,)))

	accounts=MembersBankAccounts.objects.filter(member_id=member.transaction.member).order_by("account_priority")

	context={
	'task_array':task_array,
	'task_enabler_array':task_enabler_array,
	'default_password':default_password,
	'accounts':accounts,
	}
	return render(request,'deskofficer_templates/Xmas_Savings_Shortlisting_Account_Assignment.html',context)


def Xmas_Savings_Shortlisting_Account_Transfer(request,pk):
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	task_array=[]
	for task in tasks:
		task_array.append(task.task.title)



	task_enabler=TransactionEnabler.objects.filter(status="YES")
	task_enabler_array=[]
	for item in task_enabler:
		task_enabler_array.append(item.title)

	default_password="NO"
	if Staff.objects.filter(admin=request.user,default_password='YES'):
		default_password="YES"

	member=Xmas_Savings_Shortlist.objects.get(id=pk)

	if request.method == 'POST':
		tdate=get_current_date(now)
		account_status='YES'
		processing_status='PROCESSED'
		status1='ACTIVE'
		transaction_id = request.POST.get('transaction')
		transaction=MembersAccountsDomain.objects.get(id=transaction_id)

		particulars='Posting from Xmas Savings for ' + member.batch
		debit = 0
		credit =  member.amount
		balance=member.amount

		ledger=get_ledger_balance(transaction.account_number)

		post_to_ledger(member.transaction.member,
					transaction.transaction,
					transaction.account_number,
					particulars,
					debit,
					credit,
					float(ledger) + float(balance),
					get_current_date(now),
					status1,
					tdate)

		member.details="Cash transferred to " + transaction.transaction.name + '(' + str(transaction.account_number) + ')'
		member.account_status=account_status
		member.processing_status=processing_status
		member.save()
		return HttpResponseRedirect(reverse('Xmas_Savings_Shortlisting_Account_Linkage_List_Load',args=(member.batch,member.payment_channel,)))

	savings=MembersAccountsDomain.objects.filter(member_id=member.transaction.member,transaction__source="SAVINGS")

	context={
	'task_array':task_array,
	'task_enabler_array':task_enabler_array,
	'default_password':default_password,
	'savings':savings,
	'member':member,
	}
	return render(request,'deskofficer_templates/Xmas_Savings_Shortlisting_Account_Transfer.html',context)




def Xmas_Savings_Shortlisting_Export_Batch_Load(request):
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	task_array=[]
	for task in tasks:
		task_array.append(task.task.title)




	form=Xmas_Savings_Shortlisting_Export_form(request.POST or None)


	task_enabler=TransactionEnabler.objects.filter(status="YES")
	task_enabler_array=[]
	for item in task_enabler:
		task_enabler_array.append(item.title)

	default_password="NO"
	if Staff.objects.filter(admin=request.user,default_password='YES'):
		default_password="YES"

	if request.method == 'POST':
		batch=request.POST.get('batch')
		payment=request.POST.get('category')
		return HttpResponseRedirect(reverse('Xmas_Savings_Shortlisting_Export_List_Load',args=(batch,payment,)))
	context={
	'task_array':task_array,
	'task_enabler_array':task_enabler_array,
	'default_password':default_password,
	'form':form,
	}
	return render(request,'deskofficer_templates/Xmas_Savings_Shortlisting_Export_Batch_Load.html',context)



def Xmas_Savings_Shortlisting_Export_List_Load(request,batch,payment):
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	task_array=[]
	for task in tasks:
		task_array.append(task.task.title)

	status='TREATED'


	task_enabler=TransactionEnabler.objects.filter(status="YES")
	task_enabler_array=[]
	for item in task_enabler:
		task_enabler_array.append(item.title)



	default_password="NO"
	if Staff.objects.filter(admin=request.user,default_password='YES'):
		default_password="YES"

	records=Xmas_Savings_Shortlist.objects.filter(batch=batch,payment_channel=payment,status=status)

	context={
	'task_array':task_array,
	'records':records,
	'batch':batch,
	'payment':payment,
	'task_enabler_array':task_enabler_array,
	'default_password':default_password,
	}
	return render(request,'deskofficer_templates/Xmas_Savings_Shortlisting_Export_List_Load.html',context)



def export_xmas_savings_payment_xls(request,batch,payment):
	status='TREATED'
	response = HttpResponse(content_type='application/ms-excel')
	if payment == "CASH":
		response['Content-Disposition'] = 'attachment; filename="xmas_savings_paid.xls"'

		wb = xlwt.Workbook(encoding='utf-8')
		ws = wb.add_sheet('Users Data') # this will make a sheet named Users Data

		row_num = 0  # Sheet header, first row

		font_style = xlwt.XFStyle()
		font_style.font.bold = True

		columns = ['Member ID', 'Name', 'Saving Number', 'Bank', 'Account Name','Account Number','Amount']

		for col_num in range(len(columns)):
			ws.write(row_num, col_num, columns[col_num], font_style) # at 0 row 0 column

		font_style = xlwt.XFStyle()  # Sheet body, remaining rows


		rows = Xmas_Savings_Shortlist.objects.filter(batch=batch,payment_channel=payment,status=status).values_list('transaction__member__member_id','transaction__member__full_name','transaction__account_number','bank_account__bank','bank_account__account_name', 'bank_account__account_number', 'amount')

		for row in rows:
			row_num += 1
			for col_num in range(len(row)):
				ws.write(row_num, col_num, row[col_num], font_style)
		wb.save(response)

	elif payment == "TRANSFERRED":
		response['Content-Disposition'] = 'attachment; filename="xmas_savings_transferred.xls"'

		wb = xlwt.Workbook(encoding='utf-8')
		ws = wb.add_sheet('Users Data') # this will make a sheet named Users Data

		row_num = 0  # Sheet header, first row

		font_style = xlwt.XFStyle()
		font_style.font.bold = True

		columns = ['Member ID', 'Name', 'Saving Number','Amount']

		for col_num in range(len(columns)):
			ws.write(row_num, col_num, columns[col_num], font_style) # at 0 row 0 column

		font_style = xlwt.XFStyle()  # Sheet body, remaining rows


		rows = Xmas_Savings_Shortlist.objects.filter(batch=batch,payment_channel=payment,status=status).values_list('transaction__member__member_id','transaction__member__full_name','transaction__account_number', 'amount')

		for row in rows:
			row_num += 1
			for col_num in range(len(row)):
				ws.write(row_num, col_num, row[col_num], font_style)
		wb.save(response)

	return response



def Xmas_Savings_Shortlisting_Processing_Batch_Load(request):
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	task_array=[]
	for task in tasks:
		task_array.append(task.task.title)




	form=Xmas_Savings_Shortlisting_Export_form(request.POST or None)


	task_enabler=TransactionEnabler.objects.filter(status="YES")
	task_enabler_array=[]
	for item in task_enabler:
		task_enabler_array.append(item.title)

	default_password="NO"
	if Staff.objects.filter(admin=request.user,default_password='YES'):
		default_password="YES"

	if request.method == 'POST':
		batch=request.POST.get('batch')
		payment="CASH"
		return HttpResponseRedirect(reverse('Xmas_Savings_Shortlisting_Processing_List_Load',args=(batch,payment,)))
	context={
	'task_array':task_array,
	'task_enabler_array':task_enabler_array,
	'default_password':default_password,
	'form':form,
	}
	return render(request,'deskofficer_templates/Xmas_Savings_Shortlisting_Processing_Batch_Load.html',context)


def Xmas_Savings_Shortlisting_Processing_List_Load(request,batch,payment):
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	task_array=[]
	for task in tasks:
		task_array.append(task.task.title)

	status='TREATED'
	processing_status='UNPROCESSED'




	task_enabler=TransactionEnabler.objects.filter(status="YES")
	task_enabler_array=[]
	for item in task_enabler:
		task_enabler_array.append(item.title)

	default_password="NO"
	if Staff.objects.filter(admin=request.user,default_password='YES'):
		default_password="YES"

	records=Xmas_Savings_Shortlist.objects.filter(batch=batch,payment_channel=payment,status=status,processing_status=processing_status)

	context={
	'task_array':task_array,
	'records':records,
	'batch':batch,
	'payment':payment,
	'task_enabler_array':task_enabler_array,
	'default_password':default_password,
	}
	return render(request,'deskofficer_templates/Xmas_Savings_Shortlisting_Processing_List_Load.html',context)


def Xmas_Savings_Shortlisting_Processing_Preview(request,pk):
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	task_array=[]
	for task in tasks:
		task_array.append(task.task.title)

	status='TREATED'




	task_enabler=TransactionEnabler.objects.filter(status="YES")
	task_enabler_array=[]
	for item in task_enabler:
		task_enabler_array.append(item.title)


	default_password="NO"
	if Staff.objects.filter(admin=request.user,default_password='YES'):
		default_password="YES"


	form = Xmas_Savings_Shortlisting_Processing_Preview_form(request.POST or None)

	record=Xmas_Savings_Shortlist.objects.get(id=pk)

	if request.method == 'POST':
		processing_status='PROCESSED'
		amount_paid = request.POST.get('amount_paid')

		if record.account_status == 'NO':
			messages.error(request,'Please add Bank Account paid to for this Member')
			return HttpResponseRedirect(reverse('Xmas_Savings_Shortlisting_Processing_Preview',args=(pk,)))

		record.amount_paid=amount_paid
		record.balance=float(record.amount)-float(amount_paid)
		record.processing_status=processing_status
		record.save()
		return HttpResponseRedirect(reverse('Xmas_Savings_Shortlisting_Processing_List_Load',args=(record.batch,record.payment_channel,)))

	form.fields['generated_amount'].initial=record.amount
	form.fields['amount_paid'].initial=record.amount
	context={
	'task_array':task_array,
	'record':record,
	'batch':record.batch,
	'payment':record.payment_channel,
	'task_enabler_array':task_enabler_array,
	'default_password':default_password,
	'form':form,
	}
	return render(request,'deskofficer_templates/Xmas_Savings_Shortlisting_Processing_Preview.html',context)

def Xmas_Savings_Shortlisting_Processing_Update_Bank_account(request,pk):
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	task_array=[]
	for task in tasks:
		task_array.append(task.task.title)

	status='TREATED'




	task_enabler=TransactionEnabler.objects.filter(status="YES")
	task_enabler_array=[]
	for item in task_enabler:
		task_enabler_array.append(item.title)

	default_password="NO"
	if Staff.objects.filter(admin=request.user,default_password='YES'):
		default_password="YES"

	record=Xmas_Savings_Shortlist.objects.get(id=pk)

	if request.method == 'POST':
		account_status='YES'
		account_id = request.POST.get('account')
		bank_account=MembersBankAccounts.objects.get(id=account_id)


		record.bank_account=bank_account
		record.account_status=account_status
		record.save()
		return HttpResponseRedirect(reverse('Xmas_Savings_Shortlisting_Processing_List_Load',args=(record.batch,record.payment_channel,)))

	accounts=MembersBankAccounts.objects.filter(member_id=record.transaction.member)


	context={
	'task_array':task_array,
	'record':record,
	'batch':record.batch,
	'payment':record.payment_channel,
	'task_enabler_array':task_enabler_array,
	'default_password':default_password,
	'accounts':accounts,
	}
	return render(request,'deskofficer_templates/Xmas_Savings_Shortlisting_Processing_Update_Bank_account.html',context)



def Xmas_Savings_Shortlisting_Ledger_Posting_Batch_Load(request):
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	task_array=[]
	for task in tasks:
		task_array.append(task.task.title)

	form=Xmas_Savings_Shortlisting_Export_form(request.POST or None)
	task_enabler=TransactionEnabler.objects.filter(status="YES")
	task_enabler_array=[]
	for item in task_enabler:
		task_enabler_array.append(item.title)


	default_password="NO"
	if Staff.objects.filter(admin=request.user,default_password='YES'):
		default_password="YES"

	if request.method == 'POST':
		batch=request.POST.get('batch')
		payment="CASH"
		return HttpResponseRedirect(reverse('Xmas_Savings_Shortlisting_Ledger_Posting_List_Load',args=(batch,payment,)))
	context={
	'task_array':task_array,
	'task_enabler_array':task_enabler_array,
	'default_password':default_password,
	'form':form,
	}
	return render(request,'deskofficer_templates/Xmas_Savings_Shortlisting_Ledger_Posting_Batch_Load.html',context)


def Xmas_Savings_Shortlisting_Ledger_Posting_List_Load(request,batch,payment):
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	task_array=[]
	for task in tasks:
		task_array.append(task.task.title)

	status='TREATED'
	processing_status='PROCESSED'
	submission_status='PENDING'
	submission_status1='SUBMITTED'

	task_enabler=TransactionEnabler.objects.filter(status="YES")
	task_enabler_array=[]
	for item in task_enabler:
		task_enabler_array.append(item.title)

	default_password="NO"
	if Staff.objects.filter(admin=request.user,default_password='YES'):
		default_password="YES"

	total_positive_balance=0
	total_negative_balance=0
	total_amount_paid=0
	total_amount_generated=0

	records=Xmas_Savings_Shortlist.objects.filter(batch=batch,payment_channel=payment,status=status,processing_status=processing_status,submission_status=submission_status)
	queryset=Xmas_Savings_Shortlist.objects.filter(batch=batch,payment_channel=payment,status=status,processing_status=processing_status,submission_status=submission_status).aggregate(total_generated=Sum('amount'),total_paid=Sum('amount_paid'),total_balance=Sum('balance'),)
	queryset1=Xmas_Savings_Shortlist.objects.filter(batch=batch,payment_channel=payment,status=status,processing_status=processing_status,submission_status=submission_status).filter(Q(balance__lt=0)).aggregate(total_neg_balance=Sum('balance'),)
	queryset2=Xmas_Savings_Shortlist.objects.filter(batch=batch,payment_channel=payment,status=status,processing_status=processing_status,submission_status=submission_status).filter(Q(balance__gt=0)).aggregate(total_pos_balance=Sum('balance'),)

	if queryset:
		if queryset['total_generated']:
			total_amount_generated=queryset['total_generated']
		if queryset['total_paid']:
			total_amount_paid=abs(float(queryset['total_paid']))

	if queryset1:
		total_negative_balance=queryset1['total_neg_balance']

	if queryset2:
		total_positive_balance=queryset2['total_pos_balance']

	if request.method == "POST":
		tdate=get_current_date(now)
		status1='ACTIVE'
		if not records:
			messages.error(request,'No Record Found')
			return HttpResponseRedirect(reverse('Xmas_Savings_Shortlisting_Ledger_Posting_List_Load',args=(batch,payment,)))
		for record in records:
			particulars="Xmas Savings Payment for " + str(batch)
			debit=record.amount_paid
			credit=0
			balance=record.amount_paid

			ledger=get_ledger_balance(record.transaction.account_number)

			post_to_ledger(record.transaction.member,
					record.transaction.transaction,
					record.transaction.account_number,
					particulars,
					debit,
					credit,
					float(ledger) - float(balance),
					get_current_date(now),
					status1,
					tdate)
		Xmas_Savings_Shortlist.objects.filter(batch=batch,payment_channel=payment,status=status,processing_status=processing_status,submission_status=submission_status).update(submission_status=submission_status1)
		return HttpResponseRedirect(reverse('deskofficer_home'))

	context={
	'task_array':task_array,
	'records':records,
	'batch':batch,
	'payment':payment,
	'task_enabler_array':task_enabler_array,
	'default_password':default_password,
	'total_amount_generated':total_amount_generated,
	'total_amount_paid':total_amount_paid,
	'total_negative_balance':total_negative_balance,
	'total_positive_balance':total_positive_balance,
	}
	return render(request,'deskofficer_templates/Xmas_Savings_Shortlisting_Ledger_Posting_List_Load.html',context)


def Cash_Withdrawal_Search(request):
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	task_array=[]
	for task in tasks:
		task_array.append(task.task.title)

	task_enabler=TransactionEnabler.objects.filter(status="YES")
	task_enabler_array=[]
	for item in task_enabler:
		task_enabler_array.append(item.title)

	default_password="NO"
	if Staff.objects.filter(admin=request.user,default_password='YES'):
		default_password="YES"

	title="Search Members for Cash Withdrawal"
	form = searchForm(request.POST or None)

	return render(request,'deskofficer_templates/Cash_Withdrawal_Search.html',
				{'form':form,'title':title,'task_array':task_array,
				'task_enabler_array':task_enabler_array,
	'default_password':default_password,}
				)


def Cash_Withdrawal_list_load(request):
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	task_array=[]
	for task in tasks:
		task_array.append(task.task.title)



	task_enabler=TransactionEnabler.objects.filter(status="YES")
	task_enabler_array=[]
	for item in task_enabler:
		task_enabler_array.append(item.title)

	default_password="NO"
	if Staff.objects.filter(admin=request.user,default_password='YES'):
		default_password="YES"

	title="LIST OF MEMBERS FOR CASH WITHDRAWALS"
	status="ACTIVE"
	form = searchForm(request.POST)

	if request.method == "POST":
		if request.POST.get("title")=="":
			return HttpResponseRedirect(reverse('Cash_Withdrawal_Search'))

		members=searchMembers(form['title'].value(),status)
		# members=Members.objects.filter(Q(file_no__icontains=form['title'].value()) |Q(ippis_no__icontains=form['title'].value()) |Q(phone_number__icontains=form['title'].value()) | Q(admin__first_name__icontains=form['title'].value()) | Q(admin__last_name__icontains=form['title'].value()) | Q(middle_name__icontains=form['title'].value())).filter(status=status)

		context={
		'members':members,
		'title':title,
		'task_array':task_array,
		'task_enabler_array':task_enabler_array,
	'default_password':default_password,

		}
		return render(request,'deskofficer_templates/Cash_Withdrawal_list_load.html',context)


def Cash_Withdrawal_Transactions_load(request,pk):
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	task_array=[]
	for task in tasks:
		task_array.append(task.task.title)

	task_enabler=TransactionEnabler.objects.filter(status="YES")
	task_enabler_array=[]
	for item in task_enabler:
		task_enabler_array.append(item.title)

	default_password="NO"
	if Staff.objects.filter(admin=request.user,default_password='YES'):
		default_password="YES"

	form=Cash_Withdrawal_form(request.POST or None)
	member=Members.objects.get(id=pk)
	ledger_blance=0
	account_number=""
	member_selected=[]

	if request.method=="POST" and 'btn_fetch' in request.POST:
		transaction_id=request.POST.get('transactions')
		transaction=WithdrawableTransactions.objects.get(transaction_id=transaction_id)

		member_selected=MembersAccountsDomain.objects.get(member=member,transaction=transaction.transaction)

		# current_date = datetime.date.today()
		current_date = get_current_date(now)
		maturity_date=current_date + relativedelta(months=transaction.maturity)

		if StandingOrderAccounts.objects.filter(transaction=member_selected).exists():
			record = StandingOrderAccounts.objects.filter(transaction=member_selected).first()
			if PersonalLedger.objects.filter(member=member,account_number=member_selected.account_number).exists():
				ledger=PersonalLedger.objects.filter(member=member,account_number=member_selected.account_number).last()
				ledger_blance=ledger.balance
				account_number=member_selected.account_number
			else:
				messages.info(request,'You do not have any Balance in this Transaction')
				return HttpResponseRedirect(reverse('Cash_Withdrawal_Transactions_load',args=(pk,)))


	if request.method=="POST" and 'btn_submit' in request.POST:
		transaction_id=request.POST.get('transactions')
		transaction=WithdrawableTransactions.objects.get(transaction_id=transaction_id)

		member_selected=MembersAccountsDomain.objects.get(member=member,transaction=transaction.transaction)

		current_date = datetime.date.today()
		maturity_date=current_date + relativedelta(months=transaction.maturity)

		certification_status='PENDING'
		approval_status='PENDING'

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
			status='UNTREATED'
			processed_by=CustomUser.objects.get(id=request.user.id)

			if MembersCashWithdrawalsApplication.objects.filter(member=member_selected,status=status).exists():
				messages.info(request,'You still have Open Transaction')
				return HttpResponseRedirect(reverse('Cash_Withdrawal_Transactions_load',args=(pk,)))

			record=MembersCashWithdrawalsApplication(approval_status=approval_status,tdate=current_date,member=member_selected,
				amount=withdrawal_amount,
				narration=narration,
				processed_by=processed_by.username,
				ledger_balance=ledger_balance,
				certification_status=certification_status,
				maturity_date=maturity_date,
				status=status
				)
			record.save()
			# messages.success(request,'Transaction Completed Successfully')
			return HttpResponseRedirect(reverse('deskofficer_home'))


	button_enabled=False
	if member_selected:
		if member_selected.loan_lock.title == 'NO':
			button_enabled=True

	context={
	'button_enabled':button_enabled,
	'member_selected':member_selected,
	'form':form,
	'member':member,
	'ledger_blance':ledger_blance,
	'account_number':account_number,
	'task_array':task_array,
	'task_enabler_array':task_enabler_array,
	'default_password':default_password,
	}
	return render(request,'deskofficer_templates/Cash_Withdrawal_Transactions_load.html',context)



def Cash_Withdrawal_Transactions_Request_Status_list_Search(request):
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	task_array=[]
	for task in tasks:
		task_array.append(task.task.title)

	task_enabler=TransactionEnabler.objects.filter(status="YES")
	task_enabler_array=[]
	for item in task_enabler:
		task_enabler_array.append(item.title)

	default_password="NO"
	if Staff.objects.filter(admin=request.user,default_password='YES'):
		default_password="YES"

	title="Search Members for Cash Withdrawal Status"
	form = search_with_date_Form(request.POST or None)
	form.fields['start_date'].initial=now
	form.fields['stop_date'].initial=now
	return render(request,'deskofficer_templates/Cash_Withdrawal_Transactions_Request_Status_list_Search.html',{'form':form,'title':title,'task_array':task_array,
	'task_enabler_array':task_enabler_array,
	'default_password':default_password,})


def Cash_Withdrawal_Transactions_Request_Status_list_Load(request):
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	task_array=[]
	for task in tasks:
		task_array.append(task.task.title)

	task_enabler=TransactionEnabler.objects.filter(status="YES")
	task_enabler_array=[]
	for item in task_enabler:
		task_enabler_array.append(item.title)

	default_password="NO"
	if Staff.objects.filter(admin=request.user,default_password='YES'):
		default_password="YES"

	title="LIST OF MEMBERS FOR CASH WITHDRAWALS"
	status="ACTIVE"

	status1='UNTREATED'

	form = searchForm(request.POST or None)
	members=[]
	if request.method == "POST":

		if not request.POST.get("title"):
			return HttpResponseRedirect(reverse('Cash_Withdrawal_Transactions_Request_Status_list_Search'))


		members=MembersCashWithdrawalsApplication.objects.filter(status=status1).filter(Q(member__member__file_no__icontains=form['title'].value()) |Q(member__member__ippis_no__icontains=form['title'].value()) |Q(member__member__phone_number__icontains=form['title'].value()) | Q(member__member__admin__first_name__icontains=form['title'].value()) | Q(member__member__admin__last_name__icontains=form['title'].value()) | Q(member__member__middle_name__icontains=form['title'].value()))

	context={
	'members':members,
	'title':title,
	'task_array':task_array,
	'task_enabler_array':task_enabler_array,
	'default_password':default_password,
	}
	return render(request,'deskofficer_templates/Cash_Withdrawal_Transactions_Request_Status_list_Load.html',context)


def Cash_Withdrawal_Transactions_Request_Status_Drop(request,pk):
	MembersCashWithdrawalsApplication.objects.filter(id=pk).delete()
	return HttpResponseRedirect(reverse('deskofficer_home'))


def Cash_Withdrawal_Transactions_All_Uncleared_list_Load(request):
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	task_array=[]
	for task in tasks:
		task_array.append(task.task.title)



	task_enabler=TransactionEnabler.objects.filter(status="YES")
	task_enabler_array=[]
	for item in task_enabler:
		task_enabler_array.append(item.title)

	default_password="NO"
	if Staff.objects.filter(admin=request.user,default_password='YES'):
		default_password="YES"


	title="LIST OF MEMBERS FOR CASH WITHDRAWALS"
	status='UNTREATED'

	records=MembersCashWithdrawalsApplication.objects.filter(status=status)

	context={
	'records':records,
	'title':title,
	'task_array':task_array,
	'task_enabler_array':task_enabler_array,
	'default_password':default_password,

	}
	return render(request,'deskofficer_templates/Cash_Withdrawal_Transactions_All_Uncleared_list_Load.html',context)



def Cash_Withdrawal_Transactions_Approved_list_Search(request):
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	task_array=[]
	for task in tasks:
		task_array.append(task.task.title)



	task_enabler=TransactionEnabler.objects.filter(status="YES")
	task_enabler_array=[]
	for item in task_enabler:
		task_enabler_array.append(item.title)

	default_password="NO"
	if Staff.objects.filter(admin=request.user,default_password='YES'):
		default_password="YES"

	title="Search Members for Cash Withdrawal Status"
	form = searchForm(request.POST or None)

	return render(request,'deskofficer_templates/Cash_Withdrawal_Transactions_Approved_list_Search.html',{'form':form,'title':title,'task_array':task_array,
	'task_enabler_array':task_enabler_array,
	'default_password':default_password,})




def Cash_Withdrawal_Transactions_Approved_list_Load(request):
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	task_array=[]
	for task in tasks:
		task_array.append(task.task.title)



	task_enabler=TransactionEnabler.objects.filter(status="YES")
	task_enabler_array=[]
	for item in task_enabler:
		task_enabler_array.append(item.title)

	default_password="NO"
	if Staff.objects.filter(admin=request.user,default_password='YES'):
		default_password="YES"

	title="LIST OF MEMBERS FOR CASH WITHDRAWALS"
	status="ACTIVE"

	status1='UNTREATED'

	form = search_with_date_Form(request.POST or None)
	members=[]
	if request.method == "POST":

		if not request.POST.get("title"):
			return HttpResponseRedirect(reverse('Cash_Withdrawal_Transactions_Approved_list_Search'))

		start_date=request.POST.get('start_date')
		stop_date=request.POST.get('stop_date')

		date_format = '%Y-%m-%d'

		dtObj=datetime.datetime.strptime(start_date, date_format)
		start_date=get_current_date(dtObj)

		dtObj = datetime.datetime.strptime(stop_date, date_format)
		stop_date=get_current_date(dtObj)

		members=MembersCashWithdrawalsApplication.objects.filter(tdate__range=[start_date,stop_date],status=status1).filter(Q(member__member__file_no__icontains=form['title'].value()) |Q(member__member__ippis_no__icontains=form['title'].value()) |Q(member__member__phone_number__icontains=form['title'].value()) | Q(member__member__admin__first_name__icontains=form['title'].value()) | Q(member__member__admin__last_name__icontains=form['title'].value()) | Q(member__member__middle_name__icontains=form['title'].value()))

	context={
	'members':members,
	'title':title,
	'task_array':task_array,
	'task_enabler_array':task_enabler_array,
	'default_password':default_password,
	}
	return render(request,'deskofficer_templates/Cash_Withdrawal_Transactions_Approved_list_Load.html',context)





############################################################
##################### MEMBERSHIP TERMINATION ##############
############################################################

def membership_termination_search(request):
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	task_array=[]
	for task in tasks:
		task_array.append(task.task.title)



	task_enabler=TransactionEnabler.objects.filter(status="YES")
	task_enabler_array=[]
	for item in task_enabler:
		task_enabler_array.append(item.title)

	default_password="NO"
	if Staff.objects.filter(admin=request.user,default_password='YES'):
		default_password="YES"

	title="Search Membership Request Termination"
	form = searchForm(request.POST or None)

	return render(request,'deskofficer_templates/membership_termination_search.html',{'form':form,'title':title,'task_array':task_array})


def membership_termination_list_load(request):
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	task_array=[]
	for task in tasks:
		task_array.append(task.task.title)



	task_enabler=TransactionEnabler.objects.filter(status="YES")
	task_enabler_array=[]
	for item in task_enabler:
		task_enabler_array.append(item.title)

	default_password="NO"
	if Staff.objects.filter(admin=request.user,default_password='YES'):
		default_password="YES"

	title="Membership Termination Request"
	form = searchForm(request.POST)
	status="ACTIVE"
	members=[]
	if request.method == "POST":
		if not request.POST.get("title"):
			return HttpResponseRedirect(reverse('membership_termination_search'))
		members=searchMembers(form['title'].value(),status)

	context={
	'members':members,
	'title':title,
	'task_array':task_array,
	'task_enabler_array':task_enabler_array,
	'default_password':default_password,
	}
	return render(request,'deskofficer_templates/membership_termination_list_load.html',context)



def membership_termination_transactions_load(request,pk):
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	task_array=[]
	for task in tasks:
		task_array.append(task.task.title)



	task_enabler=TransactionEnabler.objects.filter(status="YES")
	task_enabler_array=[]
	for item in task_enabler:
		task_enabler_array.append(item.title)

	default_password="NO"
	if Staff.objects.filter(admin=request.user,default_password='YES'):
		default_password="YES"

	form=Termination_Sources_upload_form(request.POST or None)
	member=Members.objects.get(id=pk)
	processing_status='UNPROCESSED'
	processed_by=CustomUser.objects.get(id=request.user.id)
	status='UNTREATED'
	approval_status="PENDING"
	allowed_records=Termination_Loan_Allowed.objects.all()
	lock_status='LOCKED'


	record_array=[]
	for item in allowed_records:
		record_array.append(item.termination.title)

	total_loan=0
	loans=LoansRepaymentBase.objects.filter(Q(balance__lt=0) & Q(member=member))
	queryset=LoansRepaymentBase.objects.filter(Q(balance__lt=0) & Q(member=member)).aggregate(total=Sum('balance'))

	if queryset:
		total_loan=queryset['total']

	tdate=get_current_date(now)

	if request.method =="POST":

		loan_amount=request.POST.get('loan_amount')
		termination_id=request.POST.get('termination_types')
		termination = Termination_Types.objects.get(id=termination_id)
		comment=request.POST.get('comment')

		applied_date_id = request.POST.get('date_applied')

		date_format = '%Y-%m-%d'
		dtObj = datetime.datetime.strptime(applied_date_id, date_format)
		applied_date=get_current_date(dtObj)



		maturity_date= get_current_date(now + relativedelta(months=int(termination.duration)))


		if float(loan_amount)==0:
			MemberShipTerminationRequest(member=member,
										termination=termination,
										loan_amount=loan_amount,
										comment=comment,
										applied_date=applied_date,
										processed_by=processed_by.username,
										status=status,
										approval_status=approval_status,
										maturity_date=maturity_date,
										tdate=tdate,
										processing_status=processing_status,
										).save()
		elif float(loan_amount)>0:
			if termination.title in record_array:
				MemberShipTerminationRequest(member=member,
											termination=termination,
											loan_amount=loan_amount,
											comment=comment,
											applied_date=applied_date,
											processed_by=processed_by.username,
											status=status,
											approval_status=approval_status,
											maturity_date=maturity_date,
											tdate=tdate,
											processing_status=processing_status,
											).save()
			else:
				messages.error(request,'Termination not Allowed while on loan, see the Management')
				return HttpResponseRedirect(reverse('membership_termination_transactions_load',args=(pk,)))

		else:
			messages.error(request,'Termination not Allowed while on loan, see the Management')
			return HttpResponseRedirect(reverse('membership_termination_transactions_load',args=(pk,)))

		return HttpResponseRedirect(reverse(membership_termination_search))
	form.fields['date_applied'].initial = now
	if total_loan:
		form.fields['loan_amount'].initial = total_loan
	form.fields['comments'].initial = "Please for your Consideration"
	context={
	'task_array':task_array,
	'task_enabler_array':task_enabler_array,
	'default_password':default_password,
	'form':form,
	'loans':loans,
	'member':member,
	'total_loan':total_loan,
	}
	return render(request,'deskofficer_templates/membership_termination_transactions_load.html',context)



def membership_termination_approved_list_processing_list_load(request):
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	task_array=[]
	for task in tasks:
		task_array.append(task.task.title)



	task_enabler=TransactionEnabler.objects.filter(status="YES")
	task_enabler_array=[]
	for item in task_enabler:
		task_enabler_array.append(item.title)


	default_password="NO"
	if Staff.objects.filter(admin=request.user,default_password='YES'):
		default_password="YES"

	title="Membership Termination Request"

	status="UNTREATED"
	processing_status='UNPROCESSED'
	approval_status='APPROVED'
	members=MemberShipTerminationRequest.objects.filter(approval_status=approval_status,status=status,processing_status=processing_status)

	context={
	'members':members,
	'title':title,
	'task_array':task_array,
	'task_enabler_array':task_enabler_array,
	'default_password':default_password,
	}
	return render(request,'deskofficer_templates/membership_termination_approved_list_processing_list_load.html',context)


def membership_termination_approved_list_processing_preview(request,pk):
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	task_array=[]
	for task in tasks:
		task_array.append(task.task.title)



	task_enabler=TransactionEnabler.objects.filter(status="YES")
	task_enabler_array=[]
	for item in task_enabler:
		task_enabler_array.append(item.title)

	default_password="NO"
	if Staff.objects.filter(admin=request.user,default_password='YES'):
		default_password="YES"

	title="Membership Termination Request"
	tdate=get_current_date(now)
	status1='INACTIVE'
	status="UNTREATED"
	status2="TREATED"
	processed_by=CustomUser.objects.get(id=request.user.id)
	approval_status='PENDING'
	processing_status='UNPROCESSED'
	lock_status='LOCKED'
	member=MemberShipTerminationRequest.objects.get(id=pk)
	savings=MembersAccountsDomain.objects.filter(member=member.member)
	schedule_status='UNSCHEDULED'


	record_array=[]
	for item in savings:
		ledger=PersonalLedger.objects.filter(member=item.member,account_number=item.account_number).last()
		if ledger:
			record_array.append((ledger.transaction.name,ledger.account_number,0,ledger.balance))


	loans=LoansRepaymentBase.objects.filter(member=member.member).filter(Q(balance__lt=0))
	if loans:
		for item in loans:
			record_array.append((item.transaction.name,item.loan_number,abs(item.balance)))
	amount=0
	if request.method == 'POST':

		for item in savings:
			ledger=PersonalLedger.objects.filter(member=item.member,account_number=item.account_number).last()
			if ledger:
				amount=float(amount)+ float(ledger.balance)
				MemberShipTerminationTransactionBalances(applicant=member,
												account_number=ledger.account_number,
												transaction=ledger.transaction,
												debit=0,
												credit=ledger.balance,
												status=status,
												processed_by=processed_by.username,
												tdate=tdate).save()

				post_to_ledger(member.member,
					ledger.transaction,
					ledger.account_number,
					"Termination of Membership payoff ",
					ledger.balance,
					0,
					0,
					get_current_date(now),
					status1,
					tdate)

				PersonalLedger.objects.filter(account_number=ledger.account_number).update(status=status1)

		if loans:
			for item in loans:
				amount=float(amount)+ float(item.balance)
				MemberShipTerminationTransactionBalances(applicant=member,
												account_number=item.loan_number,
												transaction=item.transaction,
												debit=abs(item.balance),
												credit=0,
												status=status,
												processed_by=processed_by.username,
												tdate=tdate).save()

				post_to_ledger(member.member,
					item.transaction,
					item.loan_number,
					"Termination of Membership payoff ",
					0,
					abs(item.balance),
					0,
					get_current_date(now),
					status1,
					tdate)

				PersonalLedger.objects.filter(account_number=item.loan_number).update(status=status1)

				item.amount_paid=item.amount_paid + abs(item.balance)
				item.balance=item.balance + abs(item.balance)
				item.schedule_status=schedule_status
				item.save()

				LoansCleared(loan=item,processed_by=processed_by.username,status=status,tdate=tdate,comment="Termination of Membership").save()


				item=LoansRepaymentBase.objects.get(loan_number=item.loan_number)
				item.amount_paid=item.amount_paid + abs(item.balance)
				item.balance=item.balance + abs(item.balance)
				item.schedule_status=schedule_status
				item.save()

		MemberShipTermination(applicant=member,
							amount=amount,
							approval_status=approval_status,
							processing_status=processing_status,
							status=status,
							lock_status=lock_status,
							processed_by=processed_by.username,
							tdate=tdate).save()

		MembersAccountsDomain.objects.filter(member=member.member).update(status=status1)
		StandingOrderAccounts.objects.filter(transaction__member=member.member).update(status=status1)

		Members.objects.filter(id=member.member_id).update(status=status1)

		member.status=status2
		member.save()

		return HttpResponseRedirect(reverse('membership_termination_approved_list_processing_list_load'))
	context={
	'record_array':record_array,
	'member':member,
	'title':title,
	'task_array':task_array,
	'task_enabler_array':task_enabler_array,
	'default_password':default_password,
	}
	return render(request,'deskofficer_templates/membership_termination_approved_list_processing_preview.html',context)


def membership_termination_approved_transaction_details(request,pk):
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	task_array=[]
	for task in tasks:
		task_array.append(task.task.title)



	task_enabler=TransactionEnabler.objects.filter(status="YES")
	task_enabler_array=[]
	for item in task_enabler:
		task_enabler_array.append(item.title)


	default_password="NO"
	if Staff.objects.filter(admin=request.user,default_password='YES'):
		default_password="YES"

	records=Display_PersonalLedger_All_Records(pk)

	context={
	'records':records,
	'task_array':task_array,
	'task_enabler_array':task_enabler_array,
	'default_password':default_password,
	}
	return render(request,'deskofficer_templates/membership_termination_approved_transaction_details.html',context)


def membership_dashboard_transaction_details(request,pk):
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	task_array=[]
	for task in tasks:
		task_array.append(task.task.title)



	task_enabler=TransactionEnabler.objects.filter(status="YES")
	task_enabler_array=[]
	for item in task_enabler:
		task_enabler_array.append(item.title)


	default_password="NO"
	if Staff.objects.filter(admin=request.user,default_password='YES'):
		default_password="YES"

	records=Display_PersonalLedger_All_Records(pk)

	context={
	'records':records,
	'task_array':task_array,
	'task_enabler_array':task_enabler_array,
	'default_password':default_password,
	}
	return render(request,'deskofficer_templates/membership_dashboard_transaction_details.html',context)





def membership_termination_maturity_date_exception_search(request):
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	task_array=[]
	for task in tasks:
		task_array.append(task.task.title)



	task_enabler=TransactionEnabler.objects.filter(status="YES")
	task_enabler_array=[]
	for item in task_enabler:
		task_enabler_array.append(item.title)

	default_password="NO"
	if Staff.objects.filter(admin=request.user,default_password='YES'):
		default_password="YES"

	title="Membership Request Termination maturity Date Exception"
	form = searchForm(request.POST or None)

	return render(request,'deskofficer_templates/membership_termination_maturity_date_exception_search.html',{'form':form,'title':title,'task_array':task_array})


def membership_termination_maturity_date_exception_list_load(request):
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	task_array=[]
	for task in tasks:
		task_array.append(task.task.title)



	task_enabler=TransactionEnabler.objects.filter(status="YES")
	task_enabler_array=[]
	for item in task_enabler:
		task_enabler_array.append(item.title)


	default_password="NO"
	if Staff.objects.filter(admin=request.user,default_password='YES'):
		default_password="YES"


	title="Membership Termination Request"
	form = searchForm(request.POST)
	status="INACTIVE"
	status1='UNTREATED'
	processing_status='UNPROCESSED'
	approval_status='PENDING'
	members=[]
	if request.method == "POST":
		if not request.POST.get("title"):
			return HttpResponseRedirect(reverse('membership_termination_search'))
		members=MemberShipTermination.objects.filter(Q(applicant__member__phone_number__icontains=form['title'].value()) | Q(applicant__member__file_no__icontains=form['title'].value()) | Q(applicant__member__ippis_no__icontains=form['title'].value())  | Q(applicant__member__admin__first_name__icontains=form['title'].value()) | Q(applicant__member__admin__last_name__icontains=form['title'].value()) | Q(applicant__member__middle_name__icontains=form['title'].value())).filter(applicant__member__status=status,approval_status=approval_status,processing_status=processing_status,status=status1)


	context={
	'members':members,
	'title':title,
	'task_array':task_array,
	'task_enabler_array':task_enabler_array,
	'default_password':default_password,
	}
	return render(request,'deskofficer_templates/membership_termination_maturity_date_exception_list_load.html',context)


def membership_termination_maturity_date_exception_process(request,pk):
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	task_array=[]
	for task in tasks:
		task_array.append(task.task.title)



	task_enabler=TransactionEnabler.objects.filter(status="YES")
	task_enabler_array=[]
	for item in task_enabler:
		task_enabler_array.append(item.title)

	default_password="NO"
	if Staff.objects.filter(admin=request.user,default_password='YES'):
		default_password="YES"

	title="Membership Termination Request"
	form = Standing_Order_Suspension_Transaction_Releasing_Details_form(request.POST)
	status="UNTREATED"
	approval_status="PENDING"
	processed_by=CustomUser.objects.get(id=request.user.id)
	tdate=get_current_date(now)

	applicant=MemberShipTermination.objects.get(id=pk)
	if request.method == "POST":
		reasons=request.POST.get('comment')

		if reasons:
			MemberShipTerminationRequestException(applicant=applicant,
												reasons=reasons,
												approval_status=approval_status,
												status=status,
												processed_by=processed_by.username,
												tdate=tdate
												).save()
			return HttpResponseRedirect(reverse('deskofficer_home'))
	context={
	'applicant':applicant,
	'form':form,
	'title':title,
	'task_array':task_array,
	'task_enabler_array':task_enabler_array,
	'default_password':default_password,
	}
	return render(request,'deskofficer_templates/membership_termination_maturity_date_exception_process.html',context)



def membership_termination_maturity_date_exception_approved_list_load(request):
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	task_array=[]
	for task in tasks:
		task_array.append(task.task.title)



	task_enabler=TransactionEnabler.objects.filter(status="YES")
	task_enabler_array=[]
	for item in task_enabler:
		task_enabler_array.append(item.title)

	default_password="NO"
	if Staff.objects.filter(admin=request.user,default_password='YES'):
		default_password="YES"

	title="Membership Termination Request"
	status="UNTREATED"
	approval_status="APPROVED"


	members=MemberShipTerminationRequestException.objects.filter(approval_status=approval_status,status=status)

	context={
	'members':members,
	'title':title,
	'task_array':task_array,
	'task_enabler_array':task_enabler_array,
	'default_password':default_password,
	}
	return render(request,'deskofficer_templates/membership_termination_maturity_date_exception_approved_list_load.html',context)


def membership_termination_maturity_date_exception_approved_process(request,pk):
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	task_array=[]
	for task in tasks:
		task_array.append(task.task.title)



	task_enabler=TransactionEnabler.objects.filter(status="YES")
	task_enabler_array=[]
	for item in task_enabler:
		task_enabler_array.append(item.title)

	default_password="NO"
	if Staff.objects.filter(admin=request.user,default_password='YES'):
		default_password="YES"


	title="Membership Termination Request"
	lock_status="OPEN"
	status="TREATED"

	applicant=MemberShipTerminationRequestException.objects.get(id=pk)

	record=MemberShipTermination.objects.get(id=applicant.applicant_id)

	record.lock_status=lock_status
	record.save()

	applicant.status=status
	applicant.save()
	return HttpResponseRedirect(reverse('membership_termination_maturity_date_exception_approved_list_load'))



def membership_termination_Disbursement_Processing_list_Load(request):
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	task_array=[]
	for task in tasks:
		task_array.append(task.task.title)



	task_enabler=TransactionEnabler.objects.filter(status="YES")
	task_enabler_array=[]
	for item in task_enabler:
		task_enabler_array.append(item.title)


	default_password="NO"
	if Staff.objects.filter(admin=request.user,default_password='YES'):
		default_password="YES"

	form=membership_termination_Request_Approval_Process_form(request.POST or None)

	processed_by=CustomUser.objects.get(id=request.user.id)
	tdate=get_current_date(now)
	status='TREATED'
	status1='UNTREATED'
	approval_status='APPROVED'
	processing_status='UNPROCESSED'

	members=MemberShipTermination.objects.filter(approval_status=approval_status,status=status,processing_status=processing_status).filter(Q(amount__gt=0))


	context={
	'members':members,
	'task_array':task_array,
	'task_enabler_array':task_enabler_array,
	'default_password':default_password,
	}
	return render(request,'deskofficer_templates/membership_termination_Disbursement_Processing_list_Load.html',context)


def membership_termination_Disbursement_Processing_Preview(request,pk):
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	task_array=[]
	for task in tasks:
		task_array.append(task.task.title)



	task_enabler=TransactionEnabler.objects.filter(status="YES")
	task_enabler_array=[]
	for item in task_enabler:
		task_enabler_array.append(item.title)


	default_password="NO"
	if Staff.objects.filter(admin=request.user,default_password='YES'):
		default_password="YES"

	form=membership_termination_Disbursement_Processing_Preview_form(request.POST or None)

	member=MemberShipTermination.objects.get(id=pk)
	if request.method == 'POST':
		channel=request.POST.get('channels')


		if channel== 'CASH':
			return HttpResponseRedirect(reverse('membership_termination_Disbursement_Processing_Cash',args=(pk,'CASH')))
		elif channel == "CHEQUE":
			return HttpResponseRedirect(reverse('membership_termination_Disbursement_Processing_Cheque',args=(pk,'CHEQUE')))

		elif channel == "TRANSFER":
			return HttpResponseRedirect(reverse('membership_termination_Disbursement_Processing_Transfer',args=(pk,'TRANSFER')))


		return HttpResponse("Ok")


	form.fields['amount'].initial=member.amount
	context={
	'form':form,
	'member':member,
	'task_array':task_array,
	'task_enabler_array':task_enabler_array,
	'default_password':default_password,
	}
	return render(request,'deskofficer_templates/membership_termination_Disbursement_Processing_Preview.html',context)


def membership_termination_Disbursement_Processing_Cash(request,pk,payment):
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	task_array=[]
	for task in tasks:
		task_array.append(task.task.title)



	task_enabler=TransactionEnabler.objects.filter(status="YES")
	task_enabler_array=[]
	for item in task_enabler:
		task_enabler_array.append(item.title)

	default_password="NO"
	if Staff.objects.filter(admin=request.user,default_password='YES'):
		default_password="YES"

	processed_by=CustomUser.objects.get(id=request.user.id)
	tdate=get_current_date(now)
	status='UNTREATED'
	processing_status='PROCESSED'

	form=membership_termination_Disbursement_Processing_form(request.POST or None)

	member=MemberShipTermination.objects.get(id=pk)

	if request.method == 'POST':
		payment_channel='CASH'
		pv_number=request.POST.get('pv_number')
		pv_date=request.POST.get('pv_date')

		date_format = '%Y-%m-%d'
		dtObj = datetime.datetime.strptime(pv_date, date_format)
		pv_date=get_current_date(dtObj)
		if not pv_number:
			messages.error(request,'PV Number is Missing')
			return HttpResponseRedirect(reverse('membership_termination_Disbursement_Processing_Cash',args=(pk,payment)))
		MemberShipTerminationFundDisbursement(member=member,
											 payment_channel=payment_channel,
											 pv_number=pv_number,
											 pv_date=pv_date,
											 amount=member.amount,
											 status=status,
											 processed_by=processed_by.username,
											 tdate=tdate,
											 ).save()

		member.processing_status=processing_status
		member.save()

		return HttpResponseRedirect(reverse('membership_termination_Disbursement_Processing_list_Load'))

	form.fields['amount'].initial=member.amount
	form.fields['pv_date'].initial=now
	context={
	'form':form,
	'member':member,
	'task_array':task_array,
	'task_enabler_array':task_enabler_array,
	'default_password':default_password,
	}
	return render(request,'deskofficer_templates/membership_termination_Disbursement_Processing_Cash.html',context)

def membership_termination_Disbursement_Processing_Cheque(request,pk,payment):
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	task_array=[]
	for task in tasks:
		task_array.append(task.task.title)



	task_enabler=TransactionEnabler.objects.filter(status="YES")
	task_enabler_array=[]
	for item in task_enabler:
		task_enabler_array.append(item.title)

	default_password="NO"
	if Staff.objects.filter(admin=request.user,default_password='YES'):
		default_password="YES"

	processed_by=CustomUser.objects.get(id=request.user.id)
	tdate=get_current_date(now)
	status='UNTREATED'
	processing_status='PROCESSED'

	form=membership_termination_Disbursement_Processing_form(request.POST or None)

	member=MemberShipTermination.objects.get(id=pk)

	if request.method == 'POST':
		payment_channel='CHEQUE'
		pv_number=request.POST.get('pv_number')

		date_format = '%Y-%m-%d'

		pv_date=request.POST.get('pv_date')
		dtObj = datetime.datetime.strptime(pv_date, date_format)
		pv_date=get_current_date(dtObj)

		cheque_date=request.POST.get('cheque_date')
		dtObj = datetime.datetime.strptime(cheque_date, date_format)
		cheque_date=get_current_date(dtObj)

		cheque_number=request.POST.get("cheque_number")
		account_id=request.POST.get('accounts')
		account=CooperativeBankAccounts.objects.get(id=account_id)

		if not pv_number:
			messages.error(request,'PV Number is Missing')
			return HttpResponseRedirect(reverse('membership_termination_Disbursement_Processing_Cheque',args=(pk,payment)))

		if not cheque_number:
			messages.error(request,'Cheque Number is Missing')
			return HttpResponseRedirect(reverse('membership_termination_Disbursement_Processing_Cheque',args=(pk,payment)))

		MemberShipTerminationFundDisbursement(member=member,
											 payment_channel=payment_channel,
											 pv_number=pv_number,
											 pv_date=pv_date,
											 amount=member.amount,
											 cheque_number=cheque_number,
											 cheque_date=cheque_date,
											 coop_account=account,
											 status=status,
											 processed_by=processed_by.username,
											 tdate=tdate,
											 ).save()

		member.processing_status=processing_status
		member.save()

		return HttpResponseRedirect(reverse('membership_termination_Disbursement_Processing_list_Load'))

	form.fields['amount'].initial=member.amount
	form.fields['pv_date'].initial=now
	form.fields['cheque_date'].initial=now
	context={
	'form':form,
	'member':member,
	'task_array':task_array,
	'task_enabler_array':task_enabler_array,
	'default_password':default_password,
	}
	return render(request,'deskofficer_templates/membership_termination_Disbursement_Processing_Cheque.html',context)


def membership_termination_Disbursement_Processing_Transfer(request,pk,payment):
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	task_array=[]
	for task in tasks:
		task_array.append(task.task.title)



	task_enabler=TransactionEnabler.objects.filter(status="YES")
	task_enabler_array=[]
	for item in task_enabler:
		task_enabler_array.append(item.title)

	default_password="NO"
	if Staff.objects.filter(admin=request.user,default_password='YES'):
		default_password="YES"

	processed_by=CustomUser.objects.get(id=request.user.id)
	tdate=get_current_date(now)
	status='UNTREATED'
	processing_status='PROCESSED'

	form=membership_termination_Disbursement_Processing_form(request.POST or None)

	member=MemberShipTermination.objects.get(id=pk)

	member_accounts = MembersBankAccounts.objects.filter(member_id=member.applicant.member)

	if request.method == 'POST':
		payment_channel='TRANSFER'
		pv_number=request.POST.get('pv_number')

		date_format = '%Y-%m-%d'

		pv_date=request.POST.get('pv_date')
		dtObj = datetime.datetime.strptime(pv_date, date_format)
		pv_date=get_current_date(dtObj)

		transfer_date=request.POST.get('transfer_date')
		dtObj = datetime.datetime.strptime(transfer_date, date_format)
		transfer_date=get_current_date(dtObj)

		account_id=request.POST.get('accounts')
		account=CooperativeBankAccounts.objects.get(id=account_id)

		member_account_id=request.POST.get('member_account')
		member_account=MembersBankAccounts.objects.get(id=member_account_id)

		if not pv_number:
			messages.error(request,'PV Number is Missing')
			return HttpResponseRedirect(reverse('membership_termination_Disbursement_Processing_Transfer',args=(pk,payment)))


		MemberShipTerminationFundDisbursement(member=member,
											 payment_channel=payment_channel,
											 pv_number=pv_number,
											 pv_date=pv_date,
											 amount=member.amount,
											 member_account=member_account,
											 transfer_date=transfer_date,
											 coop_account=account,
											 status=status,
											 processed_by=processed_by.username,
											 tdate=tdate,
											 ).save()

		member.processing_status=processing_status
		member.save()

		return HttpResponseRedirect(reverse('membership_termination_Disbursement_Processing_list_Load'))

	form.fields['amount'].initial=member.amount
	form.fields['pv_date'].initial=now
	form.fields['transfer_date'].initial=now
	context={
	'member_accounts':member_accounts,
	'form':form,
	'member':member,
	'task_array':task_array,
	'task_enabler_array':task_enabler_array,
	'default_password':default_password,
	}
	return render(request,'deskofficer_templates/membership_termination_Disbursement_Processing_Transfer.html',context)




# ###############################################################
# ###############################################################
# ###############################################################
###### WATCH OUT #################################################
###################################################################
###################################################################
###################################################################

def membership_commodity_loan_form_sales_transaction_period_load(request):
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	task_array=[]
	for task in tasks:
		task_array.append(task.task.title)



	task_enabler=TransactionEnabler.objects.filter(status="YES")
	task_enabler_array=[]
	for item in task_enabler:
		task_enabler_array.append(item.title)

	default_password="NO"
	if Staff.objects.filter(admin=request.user,default_password='YES'):
		default_password="YES"

	form=Product_Linking_Period_Load_form(request.POST or None)

	approval_status='APPROVED'
	status='UNTREATED'
	applicants=[]

	transaction=[]
	if request.method == 'POST':
		period_id = request.POST.get('period')
		period = Commodity_Period.objects.get(id=period_id)

		batch_id = request.POST.get("batch")
		batch = Commodity_Period_Batch.objects.get(id=batch_id)

		transaction_id = request.POST.get('transaction')
		transaction = TransactionTypes.objects.get(id=transaction_id)

		applicants=Members_Commodity_Loan_Application.objects.filter(member__product__product__category__transaction=transaction,batch=batch,period=period,approval_status=approval_status,status=status)
		transaction=transaction.name


	context={
	'task_array':task_array,
	'task_enabler_array':task_enabler_array,
	'default_password':default_password,

	'form':form,

	'applicants':applicants,
	'transaction':transaction,
	}
	return render(request,'deskofficer_templates/membership_commodity_loan_form_sales_transaction_period_load.html',context)





def membership_commodity_loan_form_sales(request,pk):
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	task_array=[]
	for task in tasks:
		task_array.append(task.task.title)

	task_enabler=TransactionEnabler.objects.filter(status="YES")
	task_enabler_array=[]
	for item in task_enabler:
		task_enabler_array.append(item.title)

	default_password="NO"
	if Staff.objects.filter(admin=request.user,default_password='YES'):
		default_password="YES"


	form=membership_commodity_loan_form_sales_transaction_form(request.POST or None)
	applicant=Members_Commodity_Loan_Application.objects.get(pk=pk)

	if request.method == "POST" and 'admin-charge' in request.POST:
		form_print= request.POST.get('form_print')

		Members_Commodity_Loan_Application_Form_Sales(applicant=applicant,
									tdate=get_current_date(now),
									processed_by=CustomUser.objects.get(id=request.user.id),
									status='UNTREATED').save()
		applicant.status='TREATED'
		applicant.save()

		if form_print == 'NO':
			print("NO Printing")
			return HttpResponseRedirect(reverse('membership_commodity_loan_form_sales_transaction_period_load'))
		elif form_print == 'YES':
			print("Printing")
			return HttpResponseRedirect(reverse('membership_commodity_loan_form_sales_transaction_period_load'))





	form.fields['amount'].initial = applicant.coop_price
	# form.fields['interest'].initial = applicant.interest
	form.fields['admin_charges'].initial = applicant.admin_charge
	form.fields['duration'].initial = applicant.duration
	form.fields['repayment'].initial = applicant.repayment
	form.fields['form_print'].initial = applicant.member.product.product.category.transaction.form_print
	context={
	'task_array':task_array,
	'task_enabler_array':task_enabler_array,
	'default_password':default_password,

	'applicant':applicant,
	'form':form,
	}
	return render(request,'deskofficer_templates/membership_commodity_loan_form_sales.html',context)


def membership_commodity_loan_form_sales_process(request,pk,payment):
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	task_array=[]
	for task in tasks:
		task_array.append(task.task.title)

	task_enabler=TransactionEnabler.objects.filter(status="YES")
	task_enabler_array=[]
	for item in task_enabler:
		task_enabler_array.append(item.title)

	default_password="NO"
	if Staff.objects.filter(admin=request.user,default_password='YES'):
		default_password="YES"

	form=membership_commodity_loan_form_sales_process_Form(request.POST or None)
	applicant=Members_Commodity_Loan_Application.objects.get(pk=pk)
	recceipt_type=applicant.member.product.product.category.transaction.receipt_type

	if request.method == 'POST':
		tdate=get_current_date(now)
		processed_by=CustomUser.objects.get(id=request.user.id)
		status="UNTREATED"
		receipt_status='UNUSED'
		receipt_status1='USED'

		if applicant.admin_charge > 0:
			if payment != 'CASH':
				bank_id=request.POST.get('banks')
				source_bank=Banks.objects.get(id=bank_id)

				account_name=request.POST.get('account_name')
				other_details=request.POST.get('other_details')

				coop_account_id=request.POST.get('coop_accounts')
				coop_account=CooperativeBankAccounts.objects.get(id=coop_account_id)

				if not account_name:
					messages.error(request,'Account Name is Missing')
					return HttpResponseRedirect(reverse('membership_commodity_loan_form_sales_process', args=(pk,payment,)))

				if not other_details:
					messages.error(request,'Other Details is Missing')
					return HttpResponseRedirect(reverse('membership_commodity_loan_form_sales_process', args=(pk,payment,)))


			if recceipt_type == "MANUAL":
				receipt_id = request.POST.get('receipt_no')
				if Receipts.objects.filter(receipt=receipt_id,status=receipt_status).exists():
					receipt_obj=Receipts.objects.get(receipt=receipt_id,status=receipt_status)
					receipt=receipt_obj.receipt
					receipt_obj.status=receipt_status1
					receipt_obj.save()

				else:
					messages.error(request,'Receipt Already in Use or Not Available')
					return HttpResponseRedirect(reverse('membership_commodity_loan_form_sales_process', args=(pk,payment,)))

			elif recceipt_type == "AUTO":

				receipt_obj=AutoReceipt.objects.first()
				receipt='C-' + str(receipt_obj.receipt).zfill(5)
				receipt_obj.receipt=int(receipt_obj.receipt)+1
				receipt_obj.save()



			if payment != 'CASH':
				Members_Commodity_Loan_Application_Form_Sales(applicant=applicant,
															channel=payment,
															source_bank=source_bank,
															account_name=account_name,
															other_details=other_details,
															coop_account=coop_account,
															receipt=receipt,
															tdate=tdate,
															processed_by=processed_by.username,
															status=status).save()
			else:
				Members_Commodity_Loan_Application_Form_Sales(applicant=applicant,
													channel=payment,
													receipt=receipt,
													tdate=tdate,
													processed_by=processed_by.username,
													status=status).save()

		else:
			Members_Commodity_Loan_Application_Form_Sales(applicant=applicant,
									channel=payment,
									tdate=tdate,
									processed_by=processed_by.username,
									status=status).save()

		applicant.status='TREATED'
		applicant.save()

		form_print= request.POST.get('form_print')



		if form_print == 'NO':
			messages.success(request,"Record Added Successfully")
			return HttpResponseRedirect(reverse('membership_commodity_loan_form_sales_transaction_period_load'))
		elif form_print == "YES":
			print("Form printing")
			messages.success(request,"Record Added Successfully")
			return HttpResponseRedirect(reverse('membership_commodity_loan_form_sales_transaction_period_load'))


	form.fields['amount'].initial=applicant.admin_charge
	context={
	'task_array':task_array,
	'task_enabler_array':task_enabler_array,
	'default_password':default_password,
	'payment':payment,
	'applicant':applicant,
	'recceipt_type':recceipt_type,
	'form':form,
	}
	return render(request,'deskofficer_templates/membership_commodity_loan_form_sales_process.html',context)


def membership_commodity_loan_Final_Applications(request):
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	task_array=[]
	for task in tasks:
		task_array.append(task.task.title)



	task_enabler=TransactionEnabler.objects.filter(status="YES")
	task_enabler_array=[]
	for item in task_enabler:
		task_enabler_array.append(item.title)


	default_password="NO"
	if Staff.objects.filter(admin=request.user,default_password='YES'):
		default_password="YES"

	form=Product_Linking_Period_Load_form(request.POST or None)

	approval_status='APPROVED'
	status='UNTREATED'
	applicants=[]

	transaction=[]
	if request.method == 'POST':
		period_id = request.POST.get('period')
		period = Commodity_Period.objects.get(id=period_id)

		batch_id = request.POST.get("batch")
		batch = Commodity_Period_Batch.objects.get(id=batch_id)

		transaction_id = request.POST.get('transaction')
		transaction = TransactionTypes.objects.get(id=transaction_id)

		applicants=Members_Commodity_Loan_Application_Form_Sales.objects.filter(applicant__member__product__product__category__transaction=transaction,applicant__batch=batch,applicant__period=period,status=status)
		transaction=transaction.name


	context={
	'task_array':task_array,
	'task_enabler_array':task_enabler_array,
	'default_password':default_password,

	'form':form,

	'applicants':applicants,
	'transaction':transaction,
	}
	return render(request,'deskofficer_templates/membership_commodity_loan_Final_Applications.html',context)

def commodity_loan_trending_products(request):
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	task_array=[]
	for task in tasks:
		task_array.append(task.task.title)



	task_enabler=TransactionEnabler.objects.filter(status="YES")
	task_enabler_array=[]
	for item in task_enabler:
		task_enabler_array.append(item.title)

	default_password="NO"
	if Staff.objects.filter(admin=request.user,default_password='YES'):
		default_password="YES"

	records =TransactionTypes.objects.filter(category='NON-MONETARY')
	context={
	'task_array':task_array,
	'task_enabler_array':task_enabler_array,
	'default_password':default_password,
	'records':records,
	# 'transaction':transaction,
	}
	return render(request,'deskofficer_templates/commodity_loan_trending_products.html',context)


def commodity_loan_trending_products_load(request,pk):
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	task_array=[]
	for task in tasks:
		task_array.append(task.task.title)



	task_enabler=TransactionEnabler.objects.filter(status="YES")
	task_enabler_array=[]
	for item in task_enabler:
		task_enabler_array.append(item.title)

	default_password="NO"
	if Staff.objects.filter(admin=request.user,default_password='YES'):
		default_password="YES"

	transaction =TransactionTypes.objects.get(id=pk)
	records=Commodity_Categories.objects.filter(transaction=transaction)
	context={
	'task_array':task_array,
	'task_enabler_array':task_enabler_array,
	'default_password':default_password,
	'records':records,
	'transaction':transaction,
	# 'transaction':transaction,
	}
	return render(request,'deskofficer_templates/commodity_loan_trending_products_load.html',context)


def commodity_loan_trending_products_details(request,pk):
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	task_array=[]
	for task in tasks:
		task_array.append(task.task.title)



	task_enabler=TransactionEnabler.objects.filter(status="YES")
	task_enabler_array=[]
	for item in task_enabler:
		task_enabler_array.append(item.title)

	default_password="NO"
	if Staff.objects.filter(admin=request.user,default_password='YES'):
		default_password="YES"

	records=Commodity_Category_Sub.objects.filter(category=pk)
	context={
	'task_array':task_array,
	'task_enabler_array':task_enabler_array,
	'default_password':default_password,
	'records':records,

	}
	return render(request,'deskofficer_templates/commodity_loan_trending_products_details.html',context)


def trending_products_member_Search(request):
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	task_array=[]
	for task in tasks:
		task_array.append(task.task.title)



	task_enabler=TransactionEnabler.objects.filter(status="YES")
	task_enabler_array=[]
	for item in task_enabler:
		task_enabler_array.append(item.title)

	default_password="NO"
	if Staff.objects.filter(admin=request.user,default_password='YES'):
		default_password="YES"

	title="Search Members for Trending Product List"
	form = searchForm(request.POST or None)

	return render(request,'deskofficer_templates/trending_products_member_Search.html',{'form':form,'title':title,'task_array':task_array,
	'task_enabler_array':task_enabler_array,
	'default_password':default_password,
	})



def trending_products_member_list_load(request):
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	task_array=[]
	for task in tasks:
		task_array.append(task.task.title)


	task_enabler=TransactionEnabler.objects.filter(status="YES")
	task_enabler_array=[]
	for item in task_enabler:
		task_enabler_array.append(item.title)

	default_password="NO"
	if Staff.objects.filter(admin=request.user,default_password='YES'):
		default_password="YES"

	title="LIST OF MEMBERS"
	form = searchForm(request.POST)
	status="ACTIVE"
	if request.method == "POST":
		if request.POST.get("title")=="":
			messages.info(request,"Please Enter a search data")
			return HttpResponseRedirect(reverse('trending_products_member_Search'))

		members=searchMembers(form['title'].value(),status)

		context={
		'members':members,
		'title':title,
		'task_array':task_array,
		'task_enabler_array':task_enabler_array,
	'default_password':default_password,
		}
		return render(request,'deskofficer_templates/trending_products_member_list_load.html',context)




def membership_commodity_loan_Final_Applications_Process(request,pk):
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	task_array=[]
	for task in tasks:
		task_array.append(task.task.title)



	task_enabler=TransactionEnabler.objects.filter(status="YES")
	task_enabler_array=[]
	for item in task_enabler:
		task_enabler_array.append(item.title)

	default_password="NO"
	if Staff.objects.filter(admin=request.user,default_password='YES'):
		default_password="YES"

	form=searchForm(request.POST or None)

	applicant=Members_Commodity_Loan_Application_Form_Sales.objects.get(id=pk)
	member_id=applicant.applicant.member.member_id

	member=applicant.applicant.member.member

	period=applicant.applicant.period
	batch=applicant.applicant.batch
	records=Members_Commodity_Loan_Products_Selection.objects.filter(member_id=member.id,product__period=period,product__batch=batch)



	context={
	'task_array':task_array,
	'task_enabler_array':task_enabler_array,
	'default_password':default_password,
	'records':records,
	'applicant':applicant,
	'form':form,
	}
	return render(request,'deskofficer_templates/membership_commodity_loan_Final_Applications_Process.html',context)


def membership_commodity_loan_Final_Applications_Process1(request,pk):
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	task_array=[]
	for task in tasks:
		task_array.append(task.task.title)



	task_enabler=TransactionEnabler.objects.filter(status="YES")
	task_enabler_array=[]
	for item in task_enabler:
		task_enabler_array.append(item.title)

	default_password="NO"
	if Staff.objects.filter(admin=request.user,default_password='YES'):
		default_password="YES"

	form=searchForm(request.POST or None)

	applicant=Members_Commodity_Loan_Application_Form_Sales.objects.get(id=pk)


	transaction=applicant.applicant.member.product.product.category.transaction
	period=applicant.applicant.period
	batch=applicant.applicant.batch

	max_guarantor=applicant.applicant.member.product.product.category.guarantors

	guarnator_status=True
	if not max_guarantor or int(max_guarantor)<=0:
		guarnator_status=False

	guarantors=Members_Commodity_Loan_Application_Guarantors.objects.filter(applicant=applicant)

	button_show=True
	if int(max_guarantor)== int(guarantors.count()):
		button_show=False

	button_enabled=False
	if guarantors:
		button_enabled=True

	if request.method == "POST" and 'btn-search' in request.POST:
		title=request.POST.get('title')
		members=Members.objects.exclude(id=applicant.applicant.member.member.id).filter(member_id__icontains=title,status='ACTIVE')
		context={
		'task_array':task_array,
		'task_enabler_array':task_enabler_array,
	'default_password':default_password,
		'members':members,
		'pk':pk,
		}
		return render(request,'deskofficer_templates/membership_commodity_loan_Final_Applications_Process_Add_Guarantors.html',context)


	if request.method == "POST" and 'btn-process' in request.POST:
		return HttpResponseRedirect(reverse('membership_commodity_loan_Final_Applications_Process',args=(pk,)))

	context={
	'task_array':task_array,
	'task_enabler_array':task_enabler_array,
	'default_password':default_password,
	'guarnator_status':guarnator_status,
	'guarantors':guarantors,
	'button_enabled':button_enabled,
	'applicant':applicant,
	'form':form,
	'button_show':button_show,
	}
	return render(request,'deskofficer_templates/membership_commodity_loan_Final_Applications_Process.html',context)



def membership_commodity_loan_Final_Applications_Process_Add_Guarantors(request,member_pk,pk):
	applicant=Members_Commodity_Loan_Application_Form_Sales.objects.get(id=pk)
	max_guarantor=applicant.applicant.member.product.product.category.guarantors
	member=Members.objects.get(id=member_pk)

	if Members_Commodity_Loan_Application_Guarantors.objects.filter(applicant=applicant).count() >= int(max_guarantor):
		messages.info(request,"You have exceeded the maximum Guarantors Allowed")
		return HttpResponseRedirect(reverse('membership_commodity_loan_Final_Applications_Process',args=(pk,)))

	if Members_Commodity_Loan_Application_Guarantors.objects.filter(applicant=applicant,guarantor=member).exists():
		messages.error(request,'This Member already added as Guarantor')
		return HttpResponseRedirect(reverse('membership_commodity_loan_Final_Applications_Process',args=(pk,)))


	Members_Commodity_Loan_Application_Guarantors(applicant=applicant,guarantor=member).save()
	return HttpResponseRedirect(reverse('membership_commodity_loan_Final_Applications_Process',args=(pk,)))



def membership_commodity_loan_Final_Applications_Delete(request,pk,return_pk):
	Members_Commodity_Loan_Application_Guarantors.objects.get(id=pk).delete()
	messages.info(request,"Receod Deleted Successfully")
	return HttpResponseRedirect(reverse('membership_commodity_loan_Final_Applications_Process',args=(return_pk,)))



def membership_commodity_loan_Final_Applications_Process_Submit(request,pk):
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	task_array=[]
	for task in tasks:
		task_array.append(task.task.title)



	task_enabler=TransactionEnabler.objects.filter(status="YES")
	task_enabler_array=[]
	for item in task_enabler:
		task_enabler_array.append(item.title)

	default_password="NO"
	if Staff.objects.filter(admin=request.user,default_password='YES'):
		default_password="YES"

	applicant=Members_Commodity_Loan_Application_Form_Sales.objects.get(id=pk)
	max_guarantor=applicant.applicant.member.product.product.category.guarantors


	transaction=applicant.applicant.member.product.product.category.transaction
	period=applicant.applicant.period
	batch=applicant.applicant.batch

	date_duration = Company_Products_Duration.objects.get(product=applicant.applicant.member.product.product.category,period=period,batch=batch)
	start_date=date_duration.start_date
	stop_date=date_duration.stop_date
	tdate=get_current_date(now)


	schedule_status='UNSCHEDULED'
	status="ACTIVE"

	member=applicant.applicant.member.member
	my_id=member.get_member_Id

	loan_amount=applicant.applicant.coop_price
	duration=applicant.applicant.duration
	repayment=applicant.applicant.repayment
	amount_paid=0
	balance=-float(loan_amount)

	interest_deduction = "SPREAD"
	processed_by=CustomUser.objects.get(id=request.user.id)

	if max_guarantor:
		max_guarantor=applicant.applicant.member.product.product.category.guarantors
		if Members_Commodity_Loan_Application_Guarantors.objects.filter(applicant=applicant).count() < int(max_guarantor):
			messages.info(request,"You Do Not Have the Required Number of Guarantors Needed for this Fascilities")
			return HttpResponseRedirect(reverse('membership_commodity_loan_Final_Applications_Process',args=(pk,)))

	loan_code=transaction.code
	if LoanNumber.objects.all().count() == 0:
		messages.error(request,"Loan Number not Set")
		return HttpResponseRedirect(reverse('membership_commodity_loan_Final_Applications_Process',args=(pk,)))

	loan_number = generate_number(loan_code,my_id,now)


	Loans_Repayment_Base(member,
						transaction,
						loan_number,
						loan_amount,
						repayment,
						balance,
						amount_paid,
						start_date,
						stop_date,
						processed_by,
						status,
						tdate,
						schedule_status)

	debit=applicant.applicant.company_price
	credit=0
	balance = -float(debit)
	particulars= applicant.applicant.member.product.product.category.title + " ISSUANCE"

	post_to_ledger(member,
					transaction,
					loan_number,
					particulars,
					debit,
					credit,
					balance,
					get_current_date(now),
					status,
					tdate)

	ledger_balance=get_ledger_balance(loan_number)

	debit=applicant.applicant.interest
	credit=0
	balance = -float(debit) + float(ledger_balance)
	particulars=  "INTEREST ON " + applicant.applicant.member.product.product.category.title

	post_to_ledger(member,
					transaction,
					loan_number,
					particulars,
					debit,
					credit,
					balance,
					get_current_date(now),
					status,
					tdate)

	status1='TREATED'
	applicant.status=status1
	applicant.save()

	return HttpResponseRedirect(reverse('membership_commodity_loan_Final_Applications'))



def Company_add(request,pk):
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	task_array=[]
	for task in tasks:
		task_array.append(task.task.title)



	task_enabler=TransactionEnabler.objects.filter(status="YES")
	task_enabler_array=[]
	for item in task_enabler:
		task_enabler_array.append(item.title)

	default_password="NO"
	if Staff.objects.filter(admin=request.user,default_password='YES'):
		default_password="YES"

	if request.method =='POST':
		company=request.POST.get('company')
		if not company:
			messages.error(request,'Company Name Missing')
			return HttpResponseRedirect(reverse('Company_add'))
		Companies(title=company).save()

		return HttpResponseRedirect(reverse('ProformaInvoicedCommodityLoan_Invoice',args=(pk,)))

	context={
	'task_array':task_array,
	'task_enabler_array':task_enabler_array,
	'default_password':default_password,


	}
	return render(request,'deskofficer_templates/Company_add.html',context)






############################################################
##################### REPORTS      ########################
############################################################


############################################################
################ Monthly Deductions#########################
############################################################
def Monthly_Deductions_Report_Search(request):
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	task_array=[]
	for task in tasks:
		task_array.append(task.task.title)



	task_enabler=TransactionEnabler.objects.filter(status="YES")
	task_enabler_array=[]
	for item in task_enabler:
		task_enabler_array.append(item.title)

	default_password="NO"
	if Staff.objects.filter(admin=request.user,default_password='YES'):
		default_password="YES"


	title="Search Members for Monthly Deduction"
	form = searchForm(request.POST or None)

	return render(request,'deskofficer_templates/Monthly_Deductions_Report_Search.html',{'form':form,'title':title,'task_array':task_array,
	'task_enabler_array':task_enabler_array,
	'default_password':default_password,
	})



def Monthly_Deductions_Report_list_load(request):
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	task_array=[]
	for task in tasks:
		task_array.append(task.task.title)



	task_enabler=TransactionEnabler.objects.filter(status="YES")
	task_enabler_array=[]
	for item in task_enabler:
		task_enabler_array.append(item.title)

	default_password="NO"
	if Staff.objects.filter(admin=request.user,default_password='YES'):
		default_password="YES"

	title="LIST OF MEMBERS"
	form = searchForm(request.POST)
	status="ACTIVE"
	if request.method == "POST":
		if request.POST.get("title")=="":
			messages.info(request,"Please Enter a search data")
			return HttpResponseRedirect(reverse('Monthly_Deductions_Report_Search'))

		members=searchMembers(form['title'].value(),status)

		context={
		'members':members,
		'title':title,
		'task_array':task_array,
		'task_enabler_array':task_enabler_array,
	'default_password':default_password,
		}
		return render(request,'deskofficer_templates/Monthly_Deductions_Report_list_load.html',context)


def Monthly_Deductions_Report_Preview(request,pk):
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	task_array=[]
	for task in tasks:
		task_array.append(task.task.title)



	task_enabler=TransactionEnabler.objects.filter(status="YES")
	task_enabler_array=[]
	for item in task_enabler:
		task_enabler_array.append(item.title)

	default_password="NO"
	if Staff.objects.filter(admin=request.user,default_password='YES'):
		default_password="YES"

	periods=TransactionPeriods.objects.all().order_by('transaction_period')

	member=Members.objects.get(id=pk)

	record=[]
	if request.method == 'POST':
		transaction_period_id = request.POST.get('period')
		transaction_period=TransactionPeriods.objects.get(id=transaction_period_id)

		if MonthlyDeductionListGenerated.objects.filter(member=member,transaction_period=transaction_period).exists():
			record=MonthlyDeductionListGenerated.objects.get(member=member,transaction_period=transaction_period)

		records=MonthlyDeductionList.objects.filter(member=member,transaction_period=transaction_period)
	context={
	'record':record,
	'records':records,
	'periods':periods,
	'member':member,
	'task_array':task_array,
	'task_enabler_array':task_enabler_array,
	'default_password':default_password,

	}
	return render(request,'deskofficer_templates/Monthly_Deductions_Report_Preview.html',context)


def Monthly_Deductions_All_Records_Report_Period(request):
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	task_array=[]
	for task in tasks:
		task_array.append(task.task.title)



	task_enabler=TransactionEnabler.objects.filter(status="YES")
	task_enabler_array=[]
	for item in task_enabler:
		task_enabler_array.append(item.title)

	default_password="NO"
	if Staff.objects.filter(admin=request.user,default_password='YES'):
		default_password="YES"

	periods=TransactionPeriods.objects.all().order_by('transaction_period')


	records=[]
	if request.method == 'POST':
		transaction_period_id = request.POST.get('period')
		transaction_period=TransactionPeriods.objects.get(id=transaction_period_id)

		records=MonthlyDeductionListGenerated.objects.filter(transaction_period=transaction_period)


	context={
	'records':records,
	'periods':periods,
	'task_array':task_array,
	'task_enabler_array':task_enabler_array,
	'default_password':default_password,

	}
	return render(request,'deskofficer_templates/Monthly_Deductions_All_Records_Report_Period.html',context)


def Monthly_Deductions_All_Records_Report_Deatials(request,pk):
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	task_array=[]
	for task in tasks:
		task_array.append(task.task.title)


	task_enabler=TransactionEnabler.objects.filter(status="YES")
	task_enabler_array=[]
	for item in task_enabler:
		task_enabler_array.append(item.title)

	default_password="NO"
	if Staff.objects.filter(admin=request.user,default_password='YES'):
		default_password="YES"

	record=MonthlyDeductionListGenerated.objects.get(id=pk)

	records=MonthlyDeductionList.objects.filter(member=record.member,transaction_period=record.transaction_period)


	context={
	'records':records,
	'period':record.transaction_period,
	'task_array':task_array,
	'task_enabler_array':task_enabler_array,
	'default_password':default_password,

	}
	return render(request,'deskofficer_templates/Monthly_Deductions_All_Records_Report_Deatials.html',context)



############################################################
##################### GENERAL SEARCH #######################
############################################################
def Members_General_Search(request):
	status="ACTIVE"
	members=[]
	if request.method == 'POST':
		frm=request.POST.get("search")
		members=generalMemberSearch(frm,status)

		print(members)
	return HttpResponse("OK")

############################################################
##################### ACTIVE LOANS ########################
############################################################

def Load_Active_loans(request):
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	task_array=[]
	for task in tasks:
		task_array.append(task.task.title)



	task_enabler=TransactionEnabler.objects.filter(status="YES")
	task_enabler_array=[]
	for item in task_enabler:
		task_enabler_array.append(item.title)

	default_password="NO"
	if Staff.objects.filter(admin=request.user,default_password='YES'):
		default_password="YES"

	status="ACTIVE"
	records=LoansRepaymentBase.objects.filter(status=status)

	context={
	'task_array':task_array,
	'task_enabler_array':task_enabler_array,
	'default_password':default_password,
	'records':records,
	}
	return render(request,'deskofficer_templates/Load_Active_loans.html',context)


############################################################
##################### PERSONEL LEDGER ########################
############################################################

def Members_Dashboard_Search(request):
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	task_array=[]
	for task in tasks:
		task_array.append(task.task.title)



	task_enabler=TransactionEnabler.objects.filter(status="YES")
	task_enabler_array=[]
	for item in task_enabler:
		task_enabler_array.append(item.title)

	default_password="NO"
	if Staff.objects.filter(admin=request.user,default_password='YES'):
		default_password="YES"

	title="Search Members Dashboard"
	form = searchForm(request.POST or None)

	return render(request,'deskofficer_templates/Members_Dashboard_Search.html',{'form':form,'title':title,'task_array':task_array,
	'task_enabler_array':task_enabler_array,
	'default_password':default_password,
	})



def Members_Dashboard_Search_list_load(request):
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	task_array=[]
	for task in tasks:
		task_array.append(task.task.title)



	task_enabler=TransactionEnabler.objects.filter(status="YES")
	task_enabler_array=[]
	for item in task_enabler:
		task_enabler_array.append(item.title)

	default_password="NO"
	if Staff.objects.filter(admin=request.user,default_password='YES'):
		default_password="YES"

	title="LIST OF MEMBERS"
	form = searchForm(request.POST)
	status="ACTIVE"
	if request.method == "POST":
		if request.POST.get("title")=="":
			messages.info(request,"Please Enter a search data")
			return HttpResponseRedirect(reverse('Members_Dashboard_Search'))

		members=searchMembers(form['title'].value(),status)


		context={
		'members':members,
		'title':title,
		'task_array':task_array,
	'task_enabler_array':task_enabler_array,
	'default_password':default_password,
		}
		return render(request,'deskofficer_templates/Members_Dashboard_Search_list_load.html',context)


def Members_Dashboard_Load(request,pk):
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	task_array=[]
	for task in tasks:
		task_array.append(task.task.title)



	task_enabler=TransactionEnabler.objects.filter(status="YES")
	task_enabler_array=[]
	for item in task_enabler:
		task_enabler_array.append(item.title)


	default_password="NO"
	if Staff.objects.filter(admin=request.user,default_password='YES'):
		default_password="YES"

	status='UNTREATED'

	member=Members.objects.get(id=pk)
	savings=MembersAccountsDomain.objects.filter(member=member)

	savings_array=[]
	for saving in savings:
		if PersonalLedger.objects.filter(account_number=saving.account_number).exists():
			ledger = PersonalLedger.objects.filter(account_number=saving.account_number).last()
			savings_array.append((ledger.transaction.name,ledger.account_number,ledger.balance))

	loans=LoansRepaymentBase.objects.filter(member=member).filter(Q(balance__lt=0))

	queryset=[]
	if CooperativeShopLedger.objects.filter(member=member).exists():

		record=CooperativeShopLedger.objects.filter(member=member).last()
		if abs(record.balance)>0:
			queryset=record

	total_welfare=0
	welfare=MembersWelfareAccounts.objects.filter(member__member=member,status=status)
	query=MembersWelfareAccounts.objects.filter(member__member=member,status=status).aggregate(total=Sum('amount'))
	total_welfare=query['total']

	orders=StandingOrderAccounts.objects.filter(transaction__member=member)


	context={
	'total_welfare':total_welfare,
	'queryset':queryset,
	'savings_array':savings_array,
	'loans':loans,
	'member':member,
	'orders':orders,
	'task_array':task_array,
	'task_enabler_array':task_enabler_array,
	'default_password':default_password,
	}
	return render(request,'deskofficer_templates/Members_Dashboard_Load.html',context)




def PersonalLedger_Selected_Search(request):
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	task_array=[]
	for task in tasks:
		task_array.append(task.task.title)

	task_enabler=TransactionEnabler.objects.filter(status="YES")
	task_enabler_array=[]
	for item in task_enabler:
		task_enabler_array.append(item.title)

	default_password="NO"
	if Staff.objects.filter(admin=request.user,default_password='YES'):
		default_password="YES"

	title="Search Members for Ledger Information"
	form = searchForm(request.POST or None)

	return render(request,'deskofficer_templates/PersonalLedger_Selected_Search.html',{'form':form,'title':title,'task_array':task_array,
	'task_enabler_array':task_enabler_array,
	'default_password':default_password,
	})



def PersonalLedger_Selected_list_load(request):
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	task_array=[]
	for task in tasks:
		task_array.append(task.task.title)



	task_enabler=TransactionEnabler.objects.filter(status="YES")
	task_enabler_array=[]
	for item in task_enabler:
		task_enabler_array.append(item.title)


	default_password="NO"
	if Staff.objects.filter(admin=request.user,default_password='YES'):
		default_password="YES"


	title="LIST OF MEMBERS"
	form = searchForm(request.POST)
	status="ACTIVE"
	if request.method == "POST":
		if request.POST.get("title")=="":
			messages.info(request,"Please Enter a search data")
			return HttpResponseRedirect(reverse('PersonalLedger_Selected_Search'))

		members=searchMembers(form['title'].value(),status)

		context={
		'members':members,
		'title':title,
		'task_array':task_array,
	'task_enabler_array':task_enabler_array,
	'default_password':default_password,
		}
		return render(request,'deskofficer_templates/PersonalLedger_Selected_list_load.html',context)


def PersonalLedger_Transaction_Load(request,pk):
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	task_array=[]
	for task in tasks:
		task_array.append(task.task.title)



	task_enabler=TransactionEnabler.objects.filter(status="YES")
	task_enabler_array=[]
	for item in task_enabler:
		task_enabler_array.append(item.title)

	default_password="NO"
	if Staff.objects.filter(admin=request.user,default_password='YES'):
		default_password="YES"



	form=PersonalLedger_Transaction_Load_form(request.POST or None)
	member=Members.objects.get(id=pk)

	if request.method=="POST":
		transaction_id=request.POST.get('transactions')
		transaction=TransactionTypes.objects.get(id=transaction_id)
		return HttpResponseRedirect(reverse('PersonalLedger_Transaction_Account_Load',args=(member.pk,transaction.pk,)))


	context={
	'form':form,
	'member':member,
	'task_array':task_array,
	'task_enabler_array':task_enabler_array,
	'default_password':default_password,
	}
	return render(request,'deskofficer_templates/PersonalLedger_Transaction_Load.html',context)


def PersonalLedger_Transaction_Account_Load(request,pk,trans_id):
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	task_array=[]
	for task in tasks:
		task_array.append(task.task.title)



	task_enabler=TransactionEnabler.objects.filter(status="YES")
	task_enabler_array=[]
	for item in task_enabler:
		task_enabler_array.append(item.title)

	default_password="NO"
	if Staff.objects.filter(admin=request.user,default_password='YES'):
		default_password="YES"



	form=PersonalLedger_Transaction_Account_Load_form(request.POST or None)
	member=Members.objects.get(id=pk)
	# status=MembershipStatus.objects.all()
	transaction=TransactionTypes.objects.get(id=trans_id)


	p=[]
	records=[]
	account_number=""
	if request.method=="POST" and 'btn-fetch' in request.POST:
		transaction_status=request.POST.get('status')


		transaction=TransactionTypes.objects.get(id=trans_id)
		p=PersonalLedger.objects.filter(member=member,transaction=transaction,status=transaction_status).order_by('account_number').values_list('account_number', flat=True).distinct()


	if request.method=="POST" and 'btn-display' in request.POST:
		account_number=request.POST.get('transaction')
		start_date=request.POST.get('start_date')
		stop_date=request.POST.get('stop_date')

		date_format = '%Y-%m-%d'
		dtObj = datetime.datetime.strptime(start_date, date_format)
		start_date=get_current_date(dtObj)


		dtObj = datetime.datetime.strptime(stop_date, date_format)
		stop_date=get_current_date(dtObj)



		if start_date and stop_date:
			return HttpResponseRedirect(reverse('PersonalLedger_Display',args=(account_number,start_date,stop_date)))
		else:
			return HttpResponseRedirect(reverse('PersonalLedger_Transaction_Account_Load',args=(pk,trans_id,)))


	form.fields['start_date'].initial= now - relativedelta(months=int(3))
	form.fields['stop_date'].initial= now



	context={
	'form':form,
	'transaction_list':p,
	'records':records,
	'member':member,
	'task_array':task_array,
	'task_enabler_array':task_enabler_array,
	'default_password':default_password,
	# 'status':status,
	'transaction':transaction,
	'account_number':account_number,
	}
	return render(request,'deskofficer_templates/PersonalLedger_Transaction_Account_Load.html',context)


def PersonalLedger_Display(request,account_number,start_date,stop_date):
	items=Display_PersonalLedger(account_number,start_date,stop_date)
	title=[]
	if items:
		title=items[0].transaction.name

	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	task_array=[]
	for task in tasks:
		task_array.append(task.task.title)



	task_enabler=TransactionEnabler.objects.filter(status="YES")
	task_enabler_array=[]
	for item in task_enabler:
		task_enabler_array.append(item.title)


	default_password="NO"
	if Staff.objects.filter(admin=request.user,default_password='YES'):
		default_password="YES"



	context={
	'task_array':task_array,
	'task_enabler_array':task_enabler_array,
	'default_password':default_password,


	'records':items,
	'title':title
	}
	return render(request,'deskofficer_templates/PersonalLedger_Display.html',context)


def MemberShipFormSalesReport(request):
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	task_array=[]
	for task in tasks:
		task_array.append(task.task.title)

	task_enabler=TransactionEnabler.objects.filter(status="YES")
	task_enabler_array=[]
	for item in task_enabler:
		task_enabler_array.append(item.title)

	default_password="NO"
	if Staff.objects.filter(admin=request.user,default_password='YES'):
		default_password="YES"

	form=Purchase_Summary_form(request.POST or None)

	form.fields['stop_date'].initial=now
	form.fields['start_date'].initial=now

	records=[]
	if request.method == 'POST':
		start_date = request.POST.get('start_date')
		stop_date = request.POST.get('stop_date')

		date_format = '%Y-%m-%d'
		tdate1 = datetime.datetime.strptime(start_date, date_format)

		tdate2 = datetime.datetime.strptime(stop_date, date_format)
		records=MemberShipFormSalesRecord.objects.filter(tdate__range=[tdate1,tdate2],new_registration=True)


	context={
	'task_array':task_array,
	'task_enabler_array':task_enabler_array,
	'default_password':default_password,

	'form':form,
	'records':records,
	}
	return render(request,'deskofficer_templates/MemberShipFormSalesReport.html',context)



def MemberShipFormSales_Report_individual_Search(request):
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	task_array=[]
	for task in tasks:
		task_array.append(task.task.title)



	task_enabler=TransactionEnabler.objects.filter(status="YES")
	task_enabler_array=[]
	for item in task_enabler:
		task_enabler_array.append(item.title)

	default_password="NO"
	if Staff.objects.filter(admin=request.user,default_password='YES'):
		default_password="YES"

	title="Search Members"
	form = searchForm(request.POST or None)

	return render(request,'deskofficer_templates/MemberShipFormSales_Report_individual_Search.html',{'form':form,'title':title,'task_array':task_array,
	'task_enabler_array':task_enabler_array,
	'default_password':default_password,})


def MemberShipFormSales_Report_individual_list_Load(request):
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	task_array=[]
	for task in tasks:
		task_array.append(task.task.title)



	task_enabler=TransactionEnabler.objects.filter(status="YES")
	task_enabler_array=[]
	for item in task_enabler:
		task_enabler_array.append(item.title)

	default_password="NO"
	if Staff.objects.filter(admin=request.user,default_password='YES'):
		default_password="YES"

	title="LIST OF MEMBERS"
	form = searchForm(request.POST or None)
	if request.method == "POST":
		if request.POST.get("title")=="":
			return HttpResponseRedirect(reverse('MemberShipFormSales_Report_individual_Search'))

		transaction=TransactionTypes.objects.get(code='800')
		status="ACTIVE"
		# members=MembersAccountsDomain.objects.filter(Q(member__file_no__icontains=form['title'].value()) |Q(member__ippis_no__icontains=form['title'].value()) |Q(member__phone_number__icontains=form['title'].value()) | Q(member__admin__first_name__icontains=form['title'].value()) | Q(member__admin__last_name__icontains=form['title'].value()) | Q(member__middle_name__icontains=form['title'].value())).filter(member__status=status,transaction=transaction)
		members=searchMembersFormSales(form['title'].value())

		context={
		'members':members,
		'title':title,
		'task_array':task_array,
	'task_enabler_array':task_enabler_array,
	'default_password':default_password,

		}
		return render(request,'deskofficer_templates/MemberShipFormSales_Report_individual_list_Load.html',context)


##############################################################
################### DAY END TRANSACTIONS ####################
#############################################################

def MemberShipFormSalesSummary(request):
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	task_array=[]
	for task in tasks:
		task_array.append(task.task.title)



	task_enabler=TransactionEnabler.objects.filter(status="YES")
	task_enabler_array=[]
	for item in task_enabler:
		task_enabler_array.append(item.title)


	default_password="NO"
	if Staff.objects.filter(admin=request.user,default_password='YES'):
		default_password="YES"

	form=Purchase_Summary_form(request.POST or None)
	processed_by=CustomUser.objects.get(id=request.user.id)
	status="UNTREATED"
	status1="TREATED"

	form.fields['start_date'].initial=now

	records=[]
	button_show=False
	if request.method == 'POST' and 'btn_fetch' in request.POST:

		start_date = request.POST.get('start_date')


		date_format = '%Y-%m-%d'
		tdate1 = datetime.datetime.strptime(start_date, date_format)

		button_show=False
		records=MemberShipFormSalesRecord.objects.filter(tdate=tdate1,processed_by=processed_by.username,status=status)
		if records:
			button_show=True

	if request.method == 'POST' and 'btn_submit' in request.POST:
		start_date = request.POST.get('start_date')

		date_format = '%Y-%m-%d'
		tdate1 = datetime.datetime.strptime(start_date, date_format)

		records=MemberShipFormSalesRecord.objects.filter(tdate=tdate1,processed_by=processed_by.username,status=status)
		queryset=MemberShipFormSalesRecord.objects.filter(tdate=tdate1,processed_by=processed_by.username,status=status).aggregate(total=Sum('total_amount'))

		total_amount=queryset['total']
		record= Day_End_Desk_Office_Transactions(description="MEMBERSHIP FORM SALES",
												amount=total_amount,
												processed_by=processed_by.username,
												status=status,
												tdate=tdate1,
											)
		record.save()

		MemberShipFormSalesRecord.objects.filter(tdate=tdate1,processed_by=processed_by.username,status=status).update(status=status1)
		return HttpResponseRedirect(reverse('deskofficer_home'))




	context={
	'task_array':task_array,
	'task_enabler_array':task_enabler_array,
	'default_password':default_password,


	'form':form,
	'records':records,
	'button_show':button_show,
	}
	return render(request,'deskofficer_templates/MemberShipFormSalesSummary.html',context)

def MemberShip_Form_Sales_Summary_Details(request,pk):
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	task_array=[]
	for task in tasks:
		task_array.append(task.task.title)



	task_enabler=TransactionEnabler.objects.filter(status="YES")
	task_enabler_array=[]
	for item in task_enabler:
		task_enabler_array.append(item.title)

	default_password="NO"
	if Staff.objects.filter(admin=request.user,default_password='YES'):
		default_password="YES"


	record=MemberShipFormSalesRecord.objects.get(id=pk)


	context={
	'task_array':task_array,
	'task_enabler_array':task_enabler_array,
	'default_password':default_password,


	'record':record,
	}
	return render(request,'deskofficer_templates/MemberShip_Form_Sales_Summary_Details.html',context)



##########################################################################
######################## SEO SECTION #####################################
##########################################################################


def members_credit_purchase_approval(request):
	approval_status='PENDING'
	status="UNTREATED"
	records=members_credit_sales_summary.objects.filter(status=status,approval_status=approval_status)

	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	task_array=[]
	for task in tasks:
		task_array.append(task.task.title)



	task_enabler=TransactionEnabler.objects.filter(status="YES")
	task_enabler_array=[]
	for item in task_enabler:
		task_enabler_array.append(item.title)

	default_password="NO"
	if Staff.objects.filter(admin=request.user,default_password='YES'):
		default_password="YES"


	context={
	'records':records,
	'task_array':task_array,
	'task_enabler_array':task_enabler_array,
	'default_password':default_password,

	}
	return render(request,'deskofficer_templates/members_credit_purchase_approval.html',context)


def members_credit_purchase_approval_preview(request,ticket):
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	task_array=[]
	for task in tasks:
		task_array.append(task.task.title)



	task_enabler=TransactionEnabler.objects.filter(status="YES")
	task_enabler_array=[]
	for item in task_enabler:
		task_enabler_array.append(item.title)

	default_password="NO"
	if Staff.objects.filter(admin=request.user,default_password='YES'):
		default_password="YES"



	form=approval_form(request.POST or None)
	records=members_credit_sales_analysis.objects.filter(trans_code__ticket=ticket)
	sum_debit = members_credit_sales_analysis.objects.filter(trans_code__ticket=ticket).aggregate(total_debit=Sum('debit'))
	sum_credit = members_credit_sales_analysis.objects.filter(trans_code__ticket=ticket).aggregate(total_credit=Sum('credit'))

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
	if not selected_items:
		messages.error(request,'No record found')
		return HttpResponseRedirect(reverse('members_credit_purchase_approval'))

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
		approval_date=get_current_date(now)
		approval_officer=CustomUser.objects.get(id=request.user.id).username
		approval_comment=request.POST.get('comment')

		status_id=request.POST.get('approval_status')
		approval_status=ApprovalStatus.objects.get(id=status_id)

		record=members_credit_sales_summary.objects.get(trans_code__ticket=ticket)

		record.approval_comment=approval_comment
		record.approval_officer=approval_officer
		record.approval_date=approval_date
		record.approval_status=approval_status
		record.save()
		return HttpResponseRedirect(reverse('members_credit_purchase_approval'))
	form.fields['comment'].initial='APPROVED'


	context={
	'task_array':task_array,
	'task_enabler_array':task_enabler_array,
	'default_password':default_password,


	'records':records,
	'form':form,
	'full_name':selected_items[0].member.get_full_name,
	'selected_items':selected_items,
	'total_amount':total_amount,
	'total_item_count':total_item_count,
	'debit_amount':debit_amount,
	'credit_amount':credit_amount,
	'balance_amount':balance_amount,
	'balance1':balance1,
	'balance2':balance2,
	}
	return render(request,'deskofficer_templates/members_credit_purchase_approval_preview.html',context)




def Initial_Shares_Update_List_Load(request):
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	task_array=[]
	for task in tasks:
		task_array.append(task.task.title)



	task_enabler=TransactionEnabler.objects.filter(status="YES")
	task_enabler_array=[]
	for item in task_enabler:
		task_enabler_array.append(item.title)

	default_password="NO"
	if Staff.objects.filter(admin=request.user,default_password='YES'):
		default_password="YES"


	approval_status='PENDING'
	status='UNTREATED'
	members=MembersShareInitialUpdateRequest.objects.filter(status=status,approval_status=approval_status)


	context={
	'task_array':task_array,
	'task_enabler_array':task_enabler_array,
	'default_password':default_password,


	'members':members,
	'now':now,
	}
	return render(request,'deskofficer_templates/SEO/Initial_Shares_Update_List_Load.html',context)

def Initial_Shares_Update_preview(request,pk):
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	task_array=[]
	for task in tasks:
		task_array.append(task.task.title)



	task_enabler=TransactionEnabler.objects.filter(status="YES")
	task_enabler_array=[]
	for item in task_enabler:
		task_enabler_array.append(item.title)


	default_password="NO"
	if Staff.objects.filter(admin=request.user,default_password='YES'):
		default_password="YES"


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
	'task_array':task_array,
	'task_enabler_array':task_enabler_array,
	'default_password':default_password,
	'form':form,
	'member':member,
	}
	return render(request,'deskofficer_templates/Initial_Shares_Update_preview.html',context)


def Transaction_Adjustment_Approval_list_Load(request):
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	task_array=[]
	for task in tasks:
		task_array.append(task.task.title)



	task_enabler=TransactionEnabler.objects.filter(status="YES")
	task_enabler_array=[]
	for item in task_enabler:
		task_enabler_array.append(item.title)

	default_password="NO"
	if Staff.objects.filter(admin=request.user,default_password='YES'):
		default_password="YES"

	processed_by=CustomUser.objects.get(id=request.user.id)
	approval_status='PENDING'
	records=TransactionAjustmentRequest.objects.filter(approval_status=approval_status).exclude(processed_by=processed_by.username)

	context={
	'task_array':task_array,
	'task_enabler_array':task_enabler_array,
	'default_password':default_password,
	'records':records,
	}
	return render(request,'deskofficer_templates/Transaction_Adjustment_Approval_list_Load.html',context)


def Transaction_Adjustment_Approval_Process(request,pk):
	approval_officer=CustomUser.objects.get(id=request.user.id)
	tdate=get_current_date(now)
	approval_status='APPROVED'
	record=TransactionAjustmentRequest.objects.get(id=pk)
	record.approval_status=approval_status
	record.approval_officer=approval_officer.username
	record.approved_at=tdate
	record.save()
	return HttpResponseRedirect(reverse('Transaction_Adjustment_Approval_list_Load'))


def Transaction_Loan_Adjustment_Approval_list_Load(request):
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	task_array=[]
	for task in tasks:
		task_array.append(task.task.title)



	task_enabler=TransactionEnabler.objects.filter(status="YES")
	task_enabler_array=[]
	for item in task_enabler:
		task_enabler_array.append(item.title)

	default_password="NO"
	if Staff.objects.filter(admin=request.user,default_password='YES'):
		default_password="YES"


	approval_status='PENDING'
	records=TransactionLoanAjustmentRequest.objects.filter(approval_status=approval_status)

	context={
	'task_array':task_array,
	'task_enabler_array':task_enabler_array,
	'default_password':default_password,
	'records':records,
	}
	return render(request,'deskofficer_templates/Transaction_Loan_Adjustment_Approval_list_Load.html',context)


def Transaction_Loan_Adjustment_Approval_list_Process(request,pk):
	approval_status='APPROVED'
	approval_officer=CustomUser.objects.get(id=request.user.id)
	approved_at=get_current_date(now)

	record=TransactionLoanAjustmentRequest.objects.get(id=pk)
	record.approval_status=approval_status
	record.approved_at=approved_at
	record.approval_officer=approval_officer.username

	record.save()
	return HttpResponseRedirect(reverse('Transaction_Loan_Adjustment_Approval_list_Load'))


def Essential_Commodity_Loan_Request_Approval(request):
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	task_array=[]
	for task in tasks:
		task_array.append(task.task.title)



	task_enabler=TransactionEnabler.objects.filter(status="YES")
	task_enabler_array=[]
	for item in task_enabler:
		task_enabler_array.append(item.title)

	default_password="NO"
	if Staff.objects.filter(admin=request.user,default_password='YES'):
		default_password="YES"


	approval_status='PENDING'
	records=Essential_Commodity_Product_Selection_Summary.objects.filter(approval_status=approval_status)
	context={
	'task_array':task_array,
	'task_enabler_array':task_enabler_array,
	'default_password':default_password,

	'records':records,
	}
	return render(request,'deskofficer_templates/SEO/Essential_Commodity_Loan_Request_Approval.html',context)


def Essential_Commodity_Loan_Request_Approval_Details(request,pk):
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	task_array=[]
	for task in tasks:
		task_array.append(task.task.title)



	task_enabler=TransactionEnabler.objects.filter(status="YES")
	task_enabler_array=[]
	for item in task_enabler:
		task_enabler_array.append(item.title)


	default_password="NO"
	if Staff.objects.filter(admin=request.user,default_password='YES'):
		default_password="YES"

	form=Essential_Commodity_Loan_Request_Approval_Details_form(request.POST or None)

	record=Essential_Commodity_Product_Selection_Summary.objects.get(id=pk)
	ticket=record.ticket
	records=Essential_Commodity_Product_Select.objects.filter(ticket=ticket)

	if request.method == "POST":
		tdate=get_current_date(now)
		comment=request.POST.get("comment")
		approval_status_id = request.POST.get('approval_status')
		approval_status=ApprovalStatus.objects.get(id=approval_status_id)

		record.approval_comment=comment
		record.approval_status=approval_status
		record.approval_date=tdate

		record.save()

		return HttpResponseRedirect(reverse('Essential_Commodity_Loan_Request_Approval'))
	form.fields['comment'].initial="APPROVED"
	context={
	'task_array':task_array,
	'task_enabler_array':task_enabler_array,
	'default_password':default_password,

	'form':form,
	'record':record,
	'records':records,
	}
	return render(request,'deskofficer_templates/SEO/Essential_Commodity_Loan_Request_Approval_Details.html',context)

############################################################
##################### GENERAL REPORTS ######################
############################################################

def Cash_Deposit_Report_Date_Load(request):
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	task_array=[]
	for task in tasks:
		task_array.append(task.task.title)



	task_enabler=TransactionEnabler.objects.filter(status="YES")
	task_enabler_array=[]
	for item in task_enabler:
		task_enabler_array.append(item.title)


	default_password="NO"
	if Staff.objects.filter(admin=request.user,default_password='YES'):
		default_password="YES"

	form=Cash_Deposit_Report_Date_Load_form(request.POST or None)

	form.fields['start_date'].initial=now
	form.fields['stop_date'].initial=now
	records=[]
	if request.method=='POST' and 'btn_display' in request.POST:
		start_date=request.POST.get('start_date')
		stop_date=request.POST.get('stop_date')


		date_format = '%Y-%m-%d'
		dtObj = datetime.datetime.strptime(start_date, date_format)
		start_date=get_current_date(dtObj)


		dtObj = datetime.datetime.strptime(stop_date, date_format)
		stop_date=get_current_date(dtObj)

		records=MembersCashDeposits.objects.filter(created_at__range=[start_date,stop_date])

	context={
	'task_array':task_array,
	'task_enabler_array':task_enabler_array,
	'default_password':default_password,
	'form':form,
	'records':records,
	}
	return render(request,'deskofficer_templates/Cash_Deposit_Report_Date_Load.html',context)


def Norminal_Roll_List_Load(request):
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	task_array=[]
	for task in tasks:
		task_array.append(task.task.title)



	task_enabler=TransactionEnabler.objects.filter(status="YES")
	task_enabler_array=[]
	for item in task_enabler:
		task_enabler_array.append(item.title)


	default_password="NO"
	if Staff.objects.filter(admin=request.user,default_password='YES'):
		default_password="YES"

	records=Members.objects.all()

	context={
	'task_array':task_array,
	'task_enabler_array':task_enabler_array,
	'default_password':default_password,
	'records':records,
	}
	return render(request,'deskofficer_templates/Norminal_Roll_List_Load.html',context)


def Norminal_Roll_Personel_Detail(request,pk):
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	task_array=[]
	for task in tasks:
		task_array.append(task.task.title)



	task_enabler=TransactionEnabler.objects.filter(status="YES")
	task_enabler_array=[]
	for item in task_enabler:
		task_enabler_array.append(item.title)

	default_password="NO"
	if Staff.objects.filter(admin=request.user,default_password='YES'):
		default_password="YES"


	member=Members.objects.get(id=pk)

	context={
	'task_array':task_array,
	'task_enabler_array':task_enabler_array,
	'default_password':default_password,
	'member':member,
	}
	return render(request,'deskofficer_templates/Norminal_Roll_Personel_Detail.html',context)



def Over_Deductions_report(request):
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	task_array=[]
	for task in tasks:
		task_array.append(task.task.title)



	task_enabler=TransactionEnabler.objects.filter(status="YES")
	task_enabler_array=[]
	for item in task_enabler:
		task_enabler_array.append(item.title)


	default_password="NO"
	if Staff.objects.filter(admin=request.user,default_password='YES'):
		default_password="YES"

	periods=TransactionPeriods.objects.all().order_by('transaction_period')

	records=[]
	if request.method == 'POST':
		transaction_period_id = request.POST.get('period')
		transaction_period=TransactionPeriods.objects.get(id=transaction_period_id)

		records=MonthlyDeductionListGenerated.objects.filter(transaction_period=transaction_period).filter(Q(balance__gt=0))

	context={
	'records':records,
	'periods':periods,
	'task_array':task_array,
	'task_enabler_array':task_enabler_array,
	'default_password':default_password,
	}
	return render(request,'deskofficer_templates/Over_Deductions_report.html',context)


def Under_Deductions_report(request):
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	task_array=[]
	for task in tasks:
		task_array.append(task.task.title)



	task_enabler=TransactionEnabler.objects.filter(status="YES")
	task_enabler_array=[]
	for item in task_enabler:
		task_enabler_array.append(item.title)

	default_password="NO"
	if Staff.objects.filter(admin=request.user,default_password='YES'):
		default_password="YES"

	periods=TransactionPeriods.objects.all().order_by('transaction_period')

	records=[]
	if request.method == 'POST':
		transaction_period_id = request.POST.get('period')
		transaction_period=TransactionPeriods.objects.get(id=transaction_period_id)

		records=MonthlyDeductionListGenerated.objects.filter(transaction_period=transaction_period).filter(Q(balance__lt=0))

	context={
	'records':records,
	'periods':periods,
	'task_array':task_array,
	'task_enabler_array':task_enabler_array,
	'default_password':default_password,

	}
	return render(request,'deskofficer_templates/Under_Deductions_report.html',context)

def Non_Members_Deductions_report(request):
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	task_array=[]
	for task in tasks:
		task_array.append(task.task.title)



	task_enabler=TransactionEnabler.objects.filter(status="YES")
	task_enabler_array=[]
	for item in task_enabler:
		task_enabler_array.append(item.title)

	default_password="NO"
	if Staff.objects.filter(admin=request.user,default_password='YES'):
		default_password="YES"

	periods=TransactionPeriods.objects.all().order_by('transaction_period')

	records=[]
	if request.method == 'POST':
		transaction_period_id = request.POST.get('period')
		transaction_period=TransactionPeriods.objects.get(id=transaction_period_id)
		transaction_period=get_current_date(transaction_period.transaction_period)

		records=NonMemberAccountDeductions.objects.filter(transaction_period=transaction_period)

	context={
	'records':records,
	'periods':periods,
	'task_array':task_array,
	'task_enabler_array':task_enabler_array,
	'default_password':default_password,
	}
	return render(request,'deskofficer_templates/Non_Members_Deductions_report.html',context)


def Members_Welfare_Report_Search(request):
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	task_array=[]
	for task in tasks:
		task_array.append(task.task.title)



	task_enabler=TransactionEnabler.objects.filter(status="YES")
	task_enabler_array=[]
	for item in task_enabler:
		task_enabler_array.append(item.title)

	default_password="NO"
	if Staff.objects.filter(admin=request.user,default_password='YES'):
		default_password="YES"

	title="Search Members for Welfare Report"
	form = searchForm(request.POST or None)

	return render(request,'deskofficer_templates/Members_Welfare_Report_Search.html',{'form':form,'title':title,'task_array':task_array,
	'task_enabler_array':task_enabler_array,
	'default_password':default_password,})


def Members_Welfare_Report_list_load(request):
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	task_array=[]
	for task in tasks:
		task_array.append(task.task.title)



	task_enabler=TransactionEnabler.objects.filter(status="YES")
	task_enabler_array=[]
	for item in task_enabler:
		task_enabler_array.append(item.title)


	default_password="NO"
	if Staff.objects.filter(admin=request.user,default_password='YES'):
		default_password="YES"

	title="LIST OF MEMBERS"
	form = searchForm(request.POST or None)
	if request.method == "POST":
		if request.POST.get("title")=="":
			return HttpResponseRedirect(reverse('Members_Welfare_Report_Search'))

		transaction=TransactionTypes.objects.get(code='800')
		status="ACTIVE"
		members=MembersAccountsDomain.objects.filter(Q(member__file_no__icontains=form['title'].value()) |Q(member__ippis_no__icontains=form['title'].value()) |Q(member__phone_number__icontains=form['title'].value()) | Q(member__admin__first_name__icontains=form['title'].value()) | Q(member__admin__last_name__icontains=form['title'].value()) | Q(member__middle_name__icontains=form['title'].value())).filter(member__status=status,transaction=transaction)

		context={
		'members':members,
		'title':title,
		'task_array':task_array,
	'task_enabler_array':task_enabler_array,
	'default_password':default_password,

		}
		return render(request,'deskofficer_templates/Members_Welfare_Report_list_load.html',context)


def Members_Welfare_Report_details(request,pk):
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	task_array=[]
	for task in tasks:
		task_array.append(task.task.title)



	task_enabler=TransactionEnabler.objects.filter(status="YES")
	task_enabler_array=[]
	for item in task_enabler:
		task_enabler_array.append(item.title)


	default_password="NO"
	if Staff.objects.filter(admin=request.user,default_password='YES'):
		default_password="YES"

	member=MembersAccountsDomain.objects.get(id=pk)
	records=MembersWelfareAccounts.objects.filter(member=member)

	context={
	'task_array':task_array,
	'task_enabler_array':task_enabler_array,
	'default_password':default_password,
	'records':records,
	'member':member,
	}
	return render(request,'deskofficer_templates/Members_Welfare_Report_details.html',context)


def Members_Welfare_Report_General_Records(request):
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	task_array=[]
	for task in tasks:
		task_array.append(task.task.title)



	task_enabler=TransactionEnabler.objects.filter(status="YES")
	task_enabler_array=[]
	for item in task_enabler:
		task_enabler_array.append(item.title)


	default_password="NO"
	if Staff.objects.filter(admin=request.user,default_password='YES'):
		default_password="YES"

	form=Members_Welfare_Report_General_Records_form(request.POST or None)


	members_array = []
	if request.method == 'POST':
		start_year=request.POST.get('start_year')
		stop_year=request.POST.get('stop_year')

		records=MembersWelfareAccounts.objects.filter(year__range=[start_year,stop_year]).order_by('member__member_id').values_list('id','member__member__member_id','member__member__admin__last_name','member__member__admin__first_name','member__member__middle_name','member__account_number','member__member__ippis_no').distinct()

		for record in records:
			queryset=  MembersWelfareAccounts.objects.filter(year__range=[start_year,stop_year],member__member__member_id=record[1]).aggregate(total_cash=Sum('amount'))
			total_amount=queryset['total_cash']

			members_array.append((record[1][13:],record[2] + " " + record[3]+ " " + record[4],record[5],total_amount,record[6]))


	context={
	'task_array':task_array,
	'task_enabler_array':task_enabler_array,
	'default_password':default_password,
	'form':form,
	'members_array':members_array,
	}
	return render(request,'deskofficer_templates/Members_Welfare_Report_General_Records.html',context)


def Members_Welfare_Report_General_Record_details(request,pk,member_id):
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	task_array=[]
	for task in tasks:
		task_array.append(task.task.title)



	task_enabler=TransactionEnabler.objects.filter(status="YES")
	task_enabler_array=[]
	for item in task_enabler:
		task_enabler_array.append(item.title)

	default_password="NO"
	if Staff.objects.filter(admin=request.user,default_password='YES'):
		default_password="YES"

	records=MembersWelfareAccounts.objects.filter(member__member__ippis_no=pk)

	context={
	'task_array':task_array,
	'task_enabler_array':task_enabler_array,
	'default_password':default_password,
	'records':records,
	'member':member_id,
	}
	return render(request,'deskofficer_templates/Members_Welfare_Report_General_Record_details.html',context)




def Members_Cleared_Loans_Records(request):
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	task_array=[]
	for task in tasks:
		task_array.append(task.task.title)



	task_enabler=TransactionEnabler.objects.filter(status="YES")
	task_enabler_array=[]
	for item in task_enabler:
		task_enabler_array.append(item.title)


	default_password="NO"
	if Staff.objects.filter(admin=request.user,default_password='YES'):
		default_password="YES"

	form=search_with_date_Form(request.POST or None)


	records = []
	if request.method == 'POST':
		start_date=request.POST.get('start_date')
		stop_date=request.POST.get('stop_date')

		date_format = '%Y-%m-%d'
		dtObj = datetime.datetime.strptime(start_date, date_format)
		start_date=get_current_date(dtObj)


		dtObj = datetime.datetime.strptime(stop_date, date_format)
		stop_date=get_current_date(dtObj)


		records=LoansCleared.objects.filter(tdate__range=[start_date,stop_date])

	form.fields['start_date'].initial=now
	form.fields['stop_date'].initial=now

	context={
	'task_array':task_array,
	'task_enabler_array':task_enabler_array,
	'default_password':default_password,
	'form':form,
	'records':records,
	}
	return render(request,'deskofficer_templates/Members_Cleared_Loans_Records.html',context)



def Members_Cleared_Loans_Records_Details(request,pk):
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	task_array=[]
	for task in tasks:
		task_array.append(task.task.title)



	task_enabler=TransactionEnabler.objects.filter(status="YES")
	task_enabler_array=[]
	for item in task_enabler:
		task_enabler_array.append(item.title)


	default_password="NO"
	if Staff.objects.filter(admin=request.user,default_password='YES'):
		default_password="YES"

	form=search_with_date_Form(request.POST or None)

	records=PersonalLedger.objects.filter(account_number=pk)

	context={
	'task_array':task_array,
	'task_enabler_array':task_enabler_array,
	'default_password':default_password,
	'records':records,
	}
	return render(request,'deskofficer_templates/Members_Cleared_Loans_Records_Details.html',context)



def Transaction_adjustment_history_Search(request):
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	task_array=[]
	for task in tasks:
		task_array.append(task.task.title)



	task_enabler=TransactionEnabler.objects.filter(status="YES")
	task_enabler_array=[]
	for item in task_enabler:
		task_enabler_array.append(item.title)

	default_password="NO"
	if Staff.objects.filter(admin=request.user,default_password='YES'):
		default_password="YES"

	title="Search Members for Ledger Information"
	form = searchForm(request.POST or None)

	return render(request,'deskofficer_templates/Transaction_adjustment_history_Search.html',{'form':form,'title':title,'task_array':task_array,
	'task_enabler_array':task_enabler_array,
	'default_password':default_password,
	})



def Transaction_adjustment_history_List_load(request):
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	task_array=[]
	for task in tasks:
		task_array.append(task.task.title)



	task_enabler=TransactionEnabler.objects.filter(status="YES")
	task_enabler_array=[]
	for item in task_enabler:
		task_enabler_array.append(item.title)

	default_password="NO"
	if Staff.objects.filter(admin=request.user,default_password='YES'):
		default_password="YES"

	title="LIST OF MEMBERS"
	form = searchForm(request.POST)
	status="ACTIVE"
	if request.method == "POST":
		if request.POST.get("title")=="":
			messages.info(request,"Please Enter a search data")
			return HttpResponseRedirect(reverse('Transaction_adjustment_history_Search'))


		members=searchMembers(form['title'].value(),status)


		context={
		'members':members,
		'title':title,
		'task_array':task_array,
	'task_enabler_array':task_enabler_array,
	'default_password':default_password,
		}
		return render(request,'deskofficer_templates/Transaction_adjustment_history_List_load.html',context)



def TransactionAjustmentHistory_Transaction_Load(request,pk):
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	task_array=[]
	for task in tasks:
		task_array.append(task.task.title)



	task_enabler=TransactionEnabler.objects.filter(status="YES")
	task_enabler_array=[]
	for item in task_enabler:
		task_enabler_array.append(item.title)

	default_password="NO"
	if Staff.objects.filter(admin=request.user,default_password='YES'):
		default_password="YES"

	member=Members.objects.get(id=pk)
	records=MembersAccountsDomain.objects.filter(member=member,transaction__source="SAVINGS")
	context={
	'member':member,
	'task_array':task_array,
	'task_enabler_array':task_enabler_array,
	'default_password':default_password,
	'records':records,
	}
	return render(request,'deskofficer_templates/TransactionAjustmentHistory_Transaction_Load.html',context)

def TransactionAjustmentHistory_details(request,pk):
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	task_array=[]
	for task in tasks:
		task_array.append(task.task.title)



	task_enabler=TransactionEnabler.objects.filter(status="YES")
	task_enabler_array=[]
	for item in task_enabler:
		task_enabler_array.append(item.title)

	default_password="NO"
	if Staff.objects.filter(admin=request.user,default_password='YES'):
		default_password="YES"

	member=MembersAccountsDomain.objects.get(id=pk)

	records=TransactionAjustmentHistory.objects.filter(member=member)
	context={
	'member':member,
	'task_array':task_array,
	'task_enabler_array':task_enabler_array,
	'default_password':default_password,
	'records':records,
	}
	return render(request,'deskofficer_templates/TransactionAjustmentHistory_details.html',context)


def Members_Initial_Shares_Reports_Load(request):
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	task_array=[]
	for task in tasks:
		task_array.append(task.task.title)



	task_enabler=TransactionEnabler.objects.filter(status="YES")
	task_enabler_array=[]
	for item in task_enabler:
		task_enabler_array.append(item.title)

	default_password="NO"
	if Staff.objects.filter(admin=request.user,default_password='YES'):
		default_password="YES"

	members=Members.objects.all()

	members_array=[]
	for member in members:
		if MembersShareAccounts.objects.filter(Q(member__member=member) & Q(shares__lt=2)).exists():
			record=MembersShareAccounts.objects.get(member__member=member)
			members_array.append((member.member_id,member.admin.last_name + " " + member.admin.first_name+ " " + member.middle_name,record.shares,member.pk))
		elif  MembersShareAccounts.objects.exclude(member__member=member):
			members_array.append((member.member_id[13:],member.admin.last_name + " " + member.admin.first_name+ " " + member.middle_name,0,member.pk))


	context={

	'task_array':task_array,
	'task_enabler_array':task_enabler_array,
	'default_password':default_password,
	'members_array':members_array,
	}
	return render(request,'deskofficer_templates/Members_Initial_Shares_Reports_Load.html',context)


def Members_Individual_Shares_Report_Search(request):
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	task_array=[]
	for task in tasks:
		task_array.append(task.task.title)



	task_enabler=TransactionEnabler.objects.filter(status="YES")
	task_enabler_array=[]
	for item in task_enabler:
		task_enabler_array.append(item.title)

	default_password="NO"
	if Staff.objects.filter(admin=request.user,default_password='YES'):
		default_password="YES"


	title="Search Members for Shares Information"
	form = searchForm(request.POST or None)

	return render(request,'deskofficer_templates/Members_Individual_Shares_Report_Search.html',{'form':form,'title':title,'task_array':task_array,
	'task_enabler_array':task_enabler_array,
	'default_password':default_password,
	})



def Members_Individual_Shares_Report_List_load(request):
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	task_array=[]
	for task in tasks:
		task_array.append(task.task.title)



	task_enabler=TransactionEnabler.objects.filter(status="YES")
	task_enabler_array=[]
	for item in task_enabler:
		task_enabler_array.append(item.title)

	default_password="NO"
	if Staff.objects.filter(admin=request.user,default_password='YES'):
		default_password="YES"

	title="LIST OF MEMBERS"
	form = searchForm(request.POST)
	status="ACTIVE"
	if request.method == "POST":
		if request.POST.get("title")=="":
			messages.info(request,"Please Enter a search data")
			return HttpResponseRedirect(reverse('Transaction_adjustment_history_Search'))


		members=searchMembers(form['title'].value(),status)
		# members=Members.objects.filter(Q(file_no__icontains=form['title'].value()) |Q(ippis_no__icontains=form['title'].value()) |Q(phone_number__icontains=form['title'].value()) | Q(admin__first_name__icontains=form['title'].value()) | Q(admin__last_name__icontains=form['title'].value()) | Q(middle_name__icontains=form['title'].value())).filter(status=status)

		# if members.count() <= 0:
		# 	messages.info(request,"No Record Found")
		# 	return HttpResponseRedirect(reverse('Transaction_adjustment_history_Search'))


		context={
		'members':members,
		'title':title,
		'task_array':task_array,
	'task_enabler_array':task_enabler_array,
	'default_password':default_password,
		}
		return render(request,'deskofficer_templates/Members_Individual_Shares_Report_List_load.html',context)



def Members_Individual_Shares_Report_Details(request,pk):
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	task_array=[]
	for task in tasks:
		task_array.append(task.task.title)

	task_enabler=TransactionEnabler.objects.filter(status="YES")
	task_enabler_array=[]
	for item in task_enabler:
		task_enabler_array.append(item.title)

	default_password="NO"
	if Staff.objects.filter(admin=request.user,default_password='YES'):
		default_password="YES"

	title="LIST OF MEMBERS"
	form = searchForm(request.POST)

	member=Members.objects.get(id=pk)
	record=[]
	queryset=[]
	if MembersShareAccounts.objects.filter(member__member=member).exists():

		record=MembersShareAccounts.objects.get(member__member=member)
		queryset=PersonalLedger.objects.filter(account_number=record.member.account_number)

	context={
	'record':record,
	'queryset':queryset,
	'member':member,
	'title':title,
	'task_array':task_array,
	'task_enabler_array':task_enabler_array,
	'default_password':default_password,
	}
	return render(request,'deskofficer_templates/Members_Individual_Shares_Report_Details.html',context)


def Members_General_Shares_Report_List_Load(request):
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	task_array=[]
	for task in tasks:
		task_array.append(task.task.title)

	task_enabler=TransactionEnabler.objects.filter(status="YES")
	task_enabler_array=[]
	for item in task_enabler:
		task_enabler_array.append(item.title)

	default_password="NO"
	if Staff.objects.filter(admin=request.user,default_password='YES'):
		default_password="YES"

	title="LIST OF MEMBERS"
	status='UNTREATED'

	records=MembersShareAccounts.objects.filter(status=status)

	context={
	'records':records,
	'title':title,
	'task_array':task_array,
	'task_enabler_array':task_enabler_array,
	'default_password':default_password,
	}
	return render(request,'deskofficer_templates/Members_General_Shares_Report_List_Load.html',context)


# def Rental_Services_List_Load(request):
# 	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
# 	task_array=[]
# 	for task in tasks:
# 		task_array.append(task.task.title)

# 	task_enabler=TransactionEnabler.objects.filter(status="YES")
# 	task_enabler_array=[]
# 	for item in task_enabler:
# 		task_enabler_array.append(item.title)


# 	# contact=RentalBookingHeaders.objects.get(id=pk)

# 	records=RentalSubCategories.objects.all()

# 	context={

# 	'records':records,
# 	'task_array':task_array,
# 	'task_enabler_array':task_enabler_array,
	# 'default_password':default_password,
# 	}
# 	return render(request,'deskofficer_templates/Rental_Services_List_Load.html',context)


def Rental_Services_Category_List_Load(request):
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	task_array=[]
	for task in tasks:
		task_array.append(task.task.title)

	task_enabler=TransactionEnabler.objects.filter(status="YES")
	task_enabler_array=[]
	for item in task_enabler:
		task_enabler_array.append(item.title)

	default_password="NO"
	if Staff.objects.filter(admin=request.user,default_password='YES'):
		default_password="YES"

	# contact=RentalBookingHeaders.objects.get(id=pk)

	records=RentalMainCategories.objects.all()

	context={

	'records':records,
	'task_array':task_array,
	'task_enabler_array':task_enabler_array,
	'default_password':default_password,
	}
	return render(request,'deskofficer_templates/Rental_Services_Category_List_Load.html',context)



def Rental_Services_Contact_Person_Register(request,pk):
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	task_array=[]
	for task in tasks:
		task_array.append(task.task.title)

	task_enabler=TransactionEnabler.objects.filter(status="YES")
	task_enabler_array=[]
	for item in task_enabler:
		task_enabler_array.append(item.title)

	default_password="NO"
	if Staff.objects.filter(admin=request.user,default_password='YES'):
		default_password="YES"

	processed_by=CustomUser.objects.get(id=request.user.id)

	form= Rental_Services_Contact_Person_Register_Form(request.POST or None)

	record=RentalMainCategories.objects.get(id=pk)
	contacts=RentalBookingHeaders.objects.filter(category=record,status='UNTREATED',processed_by=processed_by.username)

	if request.method == 'POST':
		if RentalBookingHeaders.objects.filter(category=record,status='UNTREATED').exists():
			messages.error(request,'You Still Have an Open Transaction')
			return HttpResponseRedirect(reverse('Rental_Services_Contact_Person_Register',args=(pk,)))

		name=request.POST.get('name')
		address=request.POST.get('address')
		phone_no=request.POST.get('phone_no')

		if not name:
			messages.error(request,'Name is Missing')
			return HttpResponseRedirect(reverse('Rental_Services_Contact_Person_Register',args=(pk,)))
		if not address:
			messages.error(request,'Address is Missing')
			return HttpResponseRedirect(reverse('Rental_Services_Contact_Person_Register',args=(pk,)))

		if not phone_no:
			messages.error(request,'Phone Number is Missing')
			return HttpResponseRedirect(reverse('Rental_Services_Contact_Person_Register',args=(pk,)))

		if RentalBookingHeaders.objects.filter(category=record,name=name,phone_no=phone_no,status='UNTREATED').exists():
			messages.info(request,'You still have open trabsaction for this Customer')
			return HttpResponseRedirect(reverse('Rental_Services_Contact_Person_Register',args=(pk,)))

		contact=RentalBookingHeaders(category=record,name=name.upper(),address=address.upper(),phone_no=phone_no,status='UNTREATED',processed_by=processed_by.username)
		contact.save()
		pk=contact.id
		return HttpResponseRedirect(reverse('Rental_Date_Time_Selector',args=(pk,)))
	context={
	'record':record,
	'contacts':contacts,
	'form':form,
	'task_array':task_array,
	'task_enabler_array':task_enabler_array,
	'default_password':default_password,
	}
	return render(request,'deskofficer_templates/Rental_Services_Contact_Person_Register.html',context)


def Rental_Services_Contact_Person_Register_Delete(request,pk):
	record=RentalBookingHeaders.objects.get(id=pk)
	return_pk=record.category.pk
	record.delete()
	return HttpResponseRedirect(reverse('Rental_Services_Contact_Person_Register',args=(pk,)))


def Rental_Date_Time_Selector(request,pk):
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	task_array=[]
	for task in tasks:
		task_array.append(task.task.title)

	task_enabler=TransactionEnabler.objects.filter(status="YES")
	task_enabler_array=[]
	for item in task_enabler:
		task_enabler_array.append(item.title)

	default_password="NO"
	if Staff.objects.filter(admin=request.user,default_password='YES'):
		default_password="YES"

	t = time.localtime()
	current_time = time.strftime("%H:%M", t)
	processed_by=CustomUser.objects.get(id=request.user.id)
	form =Rental_Date_Time_Selector_Form(request.POST or None)

	person=RentalBookingHeaders.objects.get(id=pk)



	selections=RentalBookingSelections.objects.filter(contact=person,processed_by=processed_by.username,status='UNTREATED')
	queryset=RentalBookingSelections.objects.filter(contact=person,processed_by=processed_by.username,status='UNTREATED').aggregate(total_amount=Sum('amount'))
	total_amount=queryset['total_amount']

	button_show=False
	if selections:
		button_show=True

	if request.method == 'POST':
		b_date=request.POST.get('date')

		date_format = '%Y-%m-%d'
		dtObj = datetime.datetime.strptime(b_date, date_format)
		b_date=get_current_date(dtObj)

		start_time=request.POST.get('start_time')
		stop_time=request.POST.get('stop_time')

		return HttpResponseRedirect(reverse('Rental_Products_List_Load',args=(
																			pk,
																			b_date,
																			start_time,
																			stop_time,
																			)))



	form.fields['date'].initial=now
	form.fields['start_time'].initial=current_time
	form.fields['stop_time'].initial=current_time
	context={
	'total_amount':total_amount,
	'form':form,
	'button_show':button_show,
	'person':person,
	'selections':selections,
	'task_array':task_array,
	'task_enabler_array':task_enabler_array,
	'default_password':default_password,
	}
	return render(request,'deskofficer_templates/Rental_Date_Time_Selector.html',context)


def Rental_Products_List_Load(request,pk,b_date,start_time,stop_time):
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	task_array=[]
	for task in tasks:
		task_array.append(task.task.title)

	task_enabler=TransactionEnabler.objects.filter(status="YES")
	task_enabler_array=[]
	for item in task_enabler:
		task_enabler_array.append(item.title)

	default_password="NO"
	if Staff.objects.filter(admin=request.user,default_password='YES'):
		default_password="YES"

	processed_by=CustomUser.objects.get(id=request.user.id)
	tdate=get_current_date(now)

	person=RentalBookingHeaders.objects.get(id=pk)
	records=RentalPriceSettings.objects.filter(main_category=person.category)

	selections=RentalBookingSelections.objects.filter(contact=person,booked_date=b_date,start_time=start_time,stop_time=stop_time,processed_by=processed_by.username,status='UNTREATED')

	button_show=False
	if selections:
		button_show=True

	if request.method == 'POST':
		service_id=request.POST.get('service')
		service=RentalPriceSettings.objects.get(id=service_id)
		if RentalBookingSelections.objects.filter(contact=person,service=service,booked_date=b_date,start_time=start_time,stop_time=stop_time,status='UNTREATED').exists():
			pass
		else:
			RentalBookingSelections(contact=person,service=service,amount=service.amount,booked_date=b_date,start_time=start_time,stop_time=stop_time,tdate=tdate,processed_by=processed_by.username).save()

		RentalBookingSelectionsSummary.objects.filter(contact=person).delete()
		return HttpResponseRedirect(reverse('Rental_Products_List_Load',args=(pk,b_date,start_time,stop_time)))

	context={
	'person':person,
	'button_show':button_show,
	'selections':selections,
	'records':records,
	'b_date':b_date,
	'start_time':start_time,
	'stop_time':stop_time,
	'task_array':task_array,
	'task_enabler_array':task_enabler_array,
	'default_password':default_password,
	}
	return render(request,'deskofficer_templates/Rental_Products_List_Load.html',context)


def Rental_Services_Selection_List_Load_Delete(request,pk,b_date,start_time,stop_time):
	record=RentalBookingSelections.objects.get(id=pk)
	pk=record.contact.pk
	record.delete()
	return HttpResponseRedirect(reverse('Rental_Products_List_Load',args=(pk,b_date,start_time,stop_time)))


def Rental_Services_Group_Selection_List_Load_Delete(request,pk):
	record=RentalBookingSelections.objects.get(id=pk)

	pk=record.contact.pk
	record.delete()
	return HttpResponseRedirect(reverse('Rental_Date_Time_Selector',args=(pk,)))


def Rental_Services_Selection_Preview(request,pk):
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	task_array=[]
	for task in tasks:
		task_array.append(task.task.title)

	task_enabler=TransactionEnabler.objects.filter(status="YES")
	task_enabler_array=[]
	for item in task_enabler:
		task_enabler_array.append(item.title)

	default_password="NO"
	if Staff.objects.filter(admin=request.user,default_password='YES'):
		default_password="YES"

	form=Rental_Services_Selection_Preview_Form(request.POST or None)
	form1=Rental_Services_Selection_Preview_Final_Form(request.POST or None)

	processed_by=CustomUser.objects.get(id=request.user.id)
	tdate=get_current_date(now)

	person=RentalBookingHeaders.objects.get(id=pk)

	selections=RentalBookingSelections.objects.filter(contact=person,processed_by=processed_by.username,status='UNTREATED')
	queryset=RentalBookingSelections.objects.filter(contact=person,processed_by=processed_by.username,status='UNTREATED').aggregate(total_amount=Sum('amount'))
	total_amount=queryset['total_amount']


	transaction = TransactionTypes.objects.get(code='300')
	receipt_type=transaction.receipt_type
	button_enabled=False

	if receipt_type== 'AUTO':
		button_show=False

	elif receipt_type == "MANUAL":
		button_show=True

	amount=0
	discount=0
	balance=0

	amount_due=0
	amount_paid=0

	if RentalBookingSelectionsSummary.objects.filter(contact=person,tdate=tdate,status='UNTREATED',processed_by=processed_by.username).exists():
		record=RentalBookingSelectionsSummary.objects.get(contact=person,tdate=tdate,status='UNTREATED',processed_by=processed_by.username)
		amount_due=record.balance
		discount=record.discount
		button_enabled=True

	if request.method == 'POST' and "btn-compute" in request.POST:
		amount=total_amount
		discount=request.POST.get('discount')

		if float(discount)>=float(amount):
			messages.error(request,'Discount cannot be greater than Amount')
			return HttpResponseRedirect(reverse('Rental_Services_Selection_Preview',args=(pk,)))

		balance=float(amount) - float(discount)

		if RentalBookingSelectionsSummary.objects.filter(contact=person,tdate=tdate,status='UNTREATED',processed_by=processed_by.username).exists():
			record=RentalBookingSelectionsSummary.objects.get(contact=person,tdate=tdate,status='UNTREATED',processed_by=processed_by.username)
			record.discount=discount
			record.net_pay=balance
			record.balance=balance
			record.save()

		else:
			RentalBookingSelectionsSummary(contact=person,
										amount=amount,
										discount=discount,
										net_pay=balance,
										balance=balance,
										tdate=tdate,
										status='UNTREATED',
										processed_by=processed_by.username
										).save()

		return HttpResponseRedirect(reverse('Rental_Services_Selection_Preview',args=(pk,)))



	if request.method == 'POST' and "btn-process" in request.POST:
		amount_due=request.POST.get('amount_due')
		amount_paid=request.POST.get('amount_paid')
		if amount_paid and float(amount_paid)>0:
			if float(amount_paid) <=float(amount_due):


				if receipt_type=="AUTO":
					receipt=0
				elif receipt_type == 'MANUAL':
					receipt=request.POST.get('receipt_no')

				receipt=generate_main_receipt(receipt_type,receipt)

				if receipt == 'a':
					messages.error(request,'Receipt not found')
					return HttpResponseRedirect(reverse('Rental_Services_Selection_Preview',args=(pk,)))
				elif receipt=='b':
					messages.error(request,'Receipt Already in Use')
					return HttpResponseRedirect(reverse('Rental_Services_Selection_Preview',args=(pk,)))

				RentalBookingSelectionsPayment(contact=person,
												receipt=receipt,
												amount=amount_paid,
												tdate=tdate,status='UNTREATED',
												processed_by=processed_by.username
												).save()

				RentalBookingSelectionsSummary.objects.filter(contact=person).update(amount_paid=F('amount_paid')+float(amount_paid),balance=F('balance')-float(amount_paid))
				RentalBookingSelectionsSummary.objects.filter(contact=person).filter(Q(balance__lte=0)).update(status='TREATED')

				person.status='TREATED'
				person.save()
				return HttpResponseRedirect(reverse('Rental_Services_Category_List_Load'))
			else:
				messages.error(request,'Amount Paid Cannot be More than Amount Due')
				return HttpResponseRedirect(reverse('Rental_Services_Selection_Preview',args=(pk,)))

		messages.error(request,'No Payment Made')
		return HttpResponseRedirect(reverse('Rental_Services_Selection_Preview',args=(pk,)))

	form.fields['amount'].initial=total_amount
	form.fields['discount'].initial=discount
	form1.fields['amount_due'].initial=amount_due
	form1.fields['amount_paid'].initial=amount_paid
	context={
	'button_enabled':button_enabled,
	'button_show':button_show,
	'form':form,
	'form1':form1,
	'person':person,
	'selections':selections,
	'amount_due':amount_due,
	'amount_paid':amount_paid,
	'total_amount':total_amount,
	'task_array':task_array,
	'task_enabler_array':task_enabler_array,
	'default_password':default_password,
	}
	return render(request,'deskofficer_templates/Rental_Services_Selection_Preview.html',context)



def Rental_Services_Unpaid_Bill(request):
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	task_array=[]
	for task in tasks:
		task_array.append(task.task.title)

	task_enabler=TransactionEnabler.objects.filter(status="YES")
	task_enabler_array=[]
	for item in task_enabler:
		task_enabler_array.append(item.title)


	default_password="NO"
	if Staff.objects.filter(admin=request.user,default_password='YES'):
		default_password="YES"

	records=RentalBookingSelectionsSummary.objects.filter(Q(balance__gt=0))

	context={
	'records':records,
	'task_array':task_array,
	'task_enabler_array':task_enabler_array,
	'default_password':default_password,
	}
	return render(request,'deskofficer_templates/Rental_Services_Unpaid_Bill.html',context)



def Rental_Services_Unpaid_Bill_Preview(request,pk):
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	task_array=[]
	for task in tasks:
		task_array.append(task.task.title)

	task_enabler=TransactionEnabler.objects.filter(status="YES")
	task_enabler_array=[]
	for item in task_enabler:
		task_enabler_array.append(item.title)

	default_password="NO"
	if Staff.objects.filter(admin=request.user,default_password='YES'):
		default_password="YES"

	form=Rental_Services_Selection_Preview_Final_Form(request.POST or None)
	record=RentalBookingSelectionsSummary.objects.get(id=pk)
	person = record.contact
	tdate=get_current_date(now)
	processed_by=CustomUser.objects.get(id=request.user.id)

	transaction = TransactionTypes.objects.get(code='300')
	receipt_type=transaction.receipt_type
	button_enabled=False

	if receipt_type== 'AUTO':
		button_show=False

	elif receipt_type == "MANUAL":
		button_show=True

	if request.method == 'POST':
		amount_paid=request.POST.get('amount_paid')
		amount_due=request.POST.get('amount_due')

		if amount_paid and float(amount_paid)>0:
			if float(amount_paid) <=float(amount_due):

				if receipt_type=="AUTO":
					receipt_obj=0
				elif receipt_type == 'MANUAL':
					receipt_obj=request.POST.get('receipt_no')

					if not receipt_obj or int(receipt_obj)<=0:
						messages.error(request, "Invalid Receipt No")
						return HttpResponseRedirect(reverse('Rental_Services_Unpaid_Bill_Preview',args=(pk,)))


				receipt=generate_main_receipt(receipt_type,receipt_obj)

				if receipt == 'a':
					messages.error(request,'Receipt not found')
					return HttpResponseRedirect(reverse('Rental_Services_Unpaid_Bill_Preview',args=(pk,)))
				elif receipt=='b':
					messages.error(request,'Receipt Already in Use')
					return HttpResponseRedirect(reverse('Rental_Services_Unpaid_Bill_Preview',args=(pk,)))

				RentalBookingSelectionsPayment(contact=person,
														receipt=receipt,
														amount=amount_paid,
														tdate=tdate,status='UNTREATED',
														processed_by=processed_by.username
														).save()

				RentalBookingSelectionsSummary.objects.filter(contact=person).update(amount_paid=F('amount_paid')+float(amount_paid),balance=F('balance')-float(amount_paid))
				RentalBookingSelectionsSummary.objects.filter(contact=person).filter(Q(balance__lte=0)).update(status='TREATED')

				return HttpResponseRedirect(reverse('Rental_Services_Unpaid_Bill'))
			else:
				messages.error(request,'Amount Paid Cannot be More than Amount Due')
				return HttpResponseRedirect(reverse('Rental_Services_Unpaid_Bill_Preview',args=(pk,)))

		messages.error(request,'No Payment Made')
		return HttpResponseRedirect(reverse('Rental_Services_Unpaid_Bill_Preview',args=(pk,)))

	form.fields['amount_due'].initial=record.balance
	form.fields['amount_paid'].initial=0
	context={
	'button_show':button_show,
	'form':form,
	'person':person,
	'record':record,
	'task_array':task_array,
	'task_enabler_array':task_enabler_array,
	'default_password':default_password,
	}
	return render(request,'deskofficer_templates/Rental_Services_Unpaid_Bill_Preview.html',context)


def Rental_Services_Management(request):
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	task_array=[]
	for task in tasks:
		task_array.append(task.task.title)

	task_enabler=TransactionEnabler.objects.filter(status="YES")
	task_enabler_array=[]
	for item in task_enabler:
		task_enabler_array.append(item.title)

	default_password="NO"
	if Staff.objects.filter(admin=request.user,default_password='YES'):
		default_password="YES"

	records=RentalBookingHeaders.objects.filter(processing_status='UNPROCESSED')


	context={
	'records':records,
	'task_array':task_array,
	'task_enabler_array':task_enabler_array,
	'default_password':default_password,
	}
	return render(request,'deskofficer_templates/Rental_Services_Management.html',context)



def Rental_Services_Management_Process(request,pk):
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	task_array=[]
	for task in tasks:
		task_array.append(task.task.title)

	task_enabler=TransactionEnabler.objects.filter(status="YES")
	task_enabler_array=[]
	for item in task_enabler:
		task_enabler_array.append(item.title)

	default_password="NO"
	if Staff.objects.filter(admin=request.user,default_password='YES'):
		default_password="YES"

	record=RentalBookingHeaders.objects.get(id=pk)

	queryset=RentalBookingSelections.objects.filter(contact=record,status='UNTREATED').order_by('booked_date').values_list('booked_date','booked_date').distinct()

	booking_array = []
	for query in queryset:
		booking_array.append((query[0],query[1]))


	context={
	'queryset':queryset,
	'record':record,
	'booking_array':booking_array,
	'task_array':task_array,
	'task_enabler_array':task_enabler_array,
	'default_password':default_password,
	}
	return render(request,'deskofficer_templates/Rental_Services_Management_Process.html',context)


def Rental_Services_Management_Process_Completed(request,pk,b_date):
	record=RentalBookingHeaders.objects.get(id=pk)
	tdate=get_current_date(now)
	booked_date=b_date
	# print("Current Date: " + str(tdate))
	# print("Booked Date: " + str(booked_date))

	if str(tdate) < str(booked_date):
		messages.info(request,'Sorry Booked Date is still ahead of this Current Date')
		return HttpResponseRedirect(reverse('Rental_Services_Management_Process',args=(record.pk,)))

	RentalBookingSelections.objects.filter(contact=record,booked_date=b_date).update(status='TREATED')

	if RentalBookingSelections.objects.filter(contact=record,status='UNTREATED').exists():
		pass
	else:
		record.processing_status='PROCESSED'
		record.save()
	return HttpResponseRedirect(reverse('Rental_Services_Management_Process',args=(record.pk,)))



def Rental_Services_Management_Process_Details(request,pk,contact):
	tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
	task_array=[]
	for task in tasks:
		task_array.append(task.task.title)

	task_enabler=TransactionEnabler.objects.filter(status="YES")
	task_enabler_array=[]
	for item in task_enabler:
		task_enabler_array.append(item.title)


	default_password="NO"
	if Staff.objects.filter(admin=request.user,default_password='YES'):
		default_password="YES"

	record=RentalBookingHeaders.objects.get(id=contact)

	records=RentalBookingSelections.objects.filter(contact=record,booked_date=pk)

	context={
	'booked_date':pk,
	'record':record,
	'records':records,
	'task_array':task_array,
	'task_enabler_array':task_enabler_array,
	'default_password':default_password,
	}
	return render(request,'deskofficer_templates/Rental_Services_Management_Process_Details.html',context)
