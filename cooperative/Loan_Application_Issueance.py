from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter, A4, landscape
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.enums import TA_JUSTIFY, TA_LEFT, TA_CENTER, TA_RIGHT
from . models import *
from .current_date import get_print_date
import os.path
from django.http import HttpResponse, HttpResponseRedirect
import inflect
from num2words import num2words
from . program import  generatePDF
from reportlab.platypus import Table, Image, Paragraph
from reportlab.lib import colors




	# print(num2words(amount_converted, to = 'ordinal'))
	# print(num2words(amount_converted, to = 'ordinal_num'))
	# print(num2words(amount_converted, to = 'year'))
	# print(num2words(amount_converted, to = 'currency'))
	  
	# Language Support.
	# print(num2words(amount_converted, lang ='es'))

def path_relative_to_file(base_file_path, relative_path):
    base_dir = os.path.dirname(os.path.abspath(base_file_path))
    return os.path.normpath(os.path.join(base_dir, relative_path))


def loanApplicationIssueanceMainHeaderTitle():
	header_text=ReportHeader.objects.first()
	line1=header_text.line1
	line2=header_text.line2


	paraList =[]
	para1Style = ParagraphStyle('para1d')
	para1Style.fontSize = 18
	para1Style.alignment = TA_CENTER
	para1Style.spaceAfter = 10
	para1Style.fontName='Helvetica-Bold'
	para1Style.textColor = colors.HexColor('#000')



	para1 = Paragraph(line1,para1Style)
	para2 = Paragraph(line2,para1Style)
	paraList = [para1,para2]
	return paraList



def Loan_Application_Issueance_dateTable(width,height,receipt_id,date):

	widthList = [
	width * 25 / 100,
	width * 50 / 100,
	width * 25 / 100,
	
	]
	res = Table([
		[Loan_Application_IssueanceMemberIdTable(widthList[0],height,receipt_id),Loan_Application_IssueanceSectionAMiddleTable(widthList[1],height,receipt_id),date],
		],
		widthList,
		height
		)

	res.setStyle([
		# ('GRID', (0, 0), (-1, -1), 1, 'black'),
		
		('FONTSIZE', (0,0), (-1,-1), 12),
		# ('FONTNAME', (0,1), (0,-1), 'Helvetica-Bold'),

		('ALIGN', (0,0), (-1,-1), 'CENTER'),
		# ('ALIGN', (1,0), (1,0), 'CENTER'),
		('VALIGN', (0,0), (-1,-1), 'MIDDLE'),

		('FONTSIZE', (0,0), (-1,-1), 13),
		('FONTNAME', (0,0), (-1,-1), 'Helvetica-Bold'),


		])
	return res


def Loan_Application_IssueanceSectionAMiddleTable(width,height,receipt_id):
	record=LoanFormIssuance.objects.get(receipt=receipt_id)
	heightList = [
	height * 50 / 100,
	height * 50 / 100,
	
	]


	res = Table([
		['FETHA II COOPERATIVE THRIFT AND CREDIT SOCIETY LTD.'],
		[record.loan.name],
		
		],
		width,
		heightList
		)

	res.setStyle([
		# ('GRID', (0, 0), (-1, -1), 1, 'black'),
		
		('FONTSIZE', (0,0), (-1,-1), 11),
		('FONTNAME', (0,0), (-1,-1), 'Helvetica-Bold'),

		('ALIGN', (0,0), (-1,-1), 'CENTER'),
		('VALIGN', (0,0), (-1,-1), 'MIDDLE'),



		# ('BOTTOMPADDING', (0, 0), (1, 0), 0),
	
		])
	return res

def Loan_Application_IssueanceMemberIdTable(width,height,receipt_id):
	record=LoanFormIssuance.objects.get(receipt=receipt_id)
	heightList = [
		height * 50 / 100,
		height * 50 / 100,	
	]

	res = Table([
		[f'COOP NO: {record.member.coop_no}'],
		[f'RECEIPT NO:{record.receipt}'],
		
	
		],
		width,
		heightList
		)

	res.setStyle([
		# ('GRID', (0, 0), (-1, -1), 1, 'black'),
		
		('FONTSIZE', (0,0), (-1,-1), 12),
		('FONTNAME', (0,0), (-1,-1), 'Helvetica-Bold'),

		('ALIGN', (0,0), (-1,-1), 'LEFT'),
		('VALIGN', (0,0), (-1,-1), 'MIDDLE'),

		('LEFTPADDING', (0, 0), (-1, -1), 15),

		# ('BOTTOMPADDING', (0, 0), (1, 0), 10),
		# ('BOTTOMPADDING', (0,1), (1,1), 20),
		])
	return res



def Loan_Application_IssueanceSectionATable(width,height,receipt_id):

	heightList = [
	height * 8 / 100,
	height * 46 / 100,
	height * 46 / 100,
	]
	res = Table([
		[_Loan_Application_IssueanceParagraphSectionA()],
		[Loan_Application_IssueanceSectionABodyTable(width,heightList[1],receipt_id)],
		[Loan_Application_IssueanceDeclarationTable(width,heightList[2],receipt_id)],
		],
		width,
		heightList
		)

	res.setStyle([
		# ('GRID', (0, 0), (-1, -1), 1, 'black'),
		
		# ('FONTSIZE', (0,0), (1,1), 13),
		# ('FONTNAME', (0,1), (1,1), 'Helvetica'),

		('ALIGN', (0,0), (1,0), 'CENTER'),
		('VALIGN', (0,0), (1,0), 'MIDDLE'),



		('BOTTOMPADDING', (0, 0), (1, 0), 0),
	
		])
	return res



def _Loan_Application_IssueanceParagraphSectionA():


	para1Style = ParagraphStyle('para1')
	para1Style.fontSize = 11
	para1Style.alignment = TA_CENTER
	para1Style.spaceAfter = 3
	para1Style.fontName='Helvetica'
	para1Style.textColor = colors.HexColor('#000')

	para1=Paragraph("""<u><b>SECTION A:</b> (To be completed by the Applicant)</u>""",para1Style)

	return para1 



def Loan_Application_IssueanceSectionABodyTable(width,height,receipt_id):
	record=LoanFormIssuance.objects.get(receipt=receipt_id)
	widthList=[
	width * 20 / 100,
	width * 80 / 100,
	]

	heightList = [
	height * 10 /100,
	height * 10 /100,
	height * 10 /100,
	height * 10 /100,
	height * 10 /100,
	height * 10 /100,
	height * 10 /100,
	height * 10 /100,
	height * 10 /100,
	height * 10 /100,
	
	]

	

	if record.member.department:
		department=record.member.department.title
	else:
		department = '-----------------------------------------------------------------------------------------------------------------'
	
	if record.member.last_used_net_pay:
		salary=f'  {record.member.last_used_net_pay}'
	else:
		salary = '-----------------------------------------------------------------------------------------------------------------'
	
	if record.member.residential_address:
		r_address=f'  {record.member.residential_address}'
	else:
		r_address = '-----------------------------------------------------------------------------------------------------------------'
	


	res = Table([
		['Name of applicant:',record.member.get_full_name],
		['Department:',department],
		['Present Salary Grade:',salary],
		['Residential Address:',r_address],
		['Bank Name:','-----------------------------------------------------------------------------------------------------------------'],
		['Account No:','-----------------------------------------------------------------------------------------------------------------'],
		['Next of Kin:','-----------------------------------------------------------------------------------------------------------------'],
		['Address:','-----------------------------------------------------------------------------------------------------------------'],
		['Phone No','-----------------------------------------------------------------------------------------------------------------'],
		['Relationship','-----------------------------------------------------------------------------------------------------------------'],
			
		],
		widthList,
		heightList
		)

	res.setStyle([
		# ('GRID', (0, 0), (-1, -1), 1, 'black'),
		
		('FONTSIZE', (0,0), (-1,-1), 11),
		# ('FONTNAME', (0,1), (1,1), 'Helvetica'),

		# ('ALIGN', (0,0), (-1,-1), 'RIGHT'),
		# ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),

		# ('LEFTPADDING', (0, 0), (-1, -1), 0),

		('BOTTOMPADDING', (0, 0), (-1, -1), 0),
	
		])
	return res


def Loan_Application_IssueanceDeclarationTable(width,height,pk):
	# record=CooperativeBankAccounts.objects.first()
	# record = CooperativeBankAccounts.objects.get(id=account)


	

	res = Table([
		[Loan_Application_IssueanceParagraphAmountApplied(pk)],
		
		],
		width-50,
		height
		)

	res.setStyle([
		# ('GRID', (0, 0), (-1, -1), 1, 'black'),
		
		# ('FONTSIZE', (0,0), (-1,-1), 13),
		# ('FONTNAME', (0,0), (1,3), 'Helvetica-Bold'),

		# ('ALIGN', (0,0), (0,-1), 'RIGHT'),
		# ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),

		('LEFTPADDING', (0, 0), (-1, -1), 5),

		# ('BOTTOMPADDING', (0, 4), (-1, -1), 25),
		# ('BOTTOMPADDING', (0,1), (1,1), 20),
		])
	return res

import locale

def Loan_Application_IssueanceParagraphAmountApplied(receipt_id):
	  
	record=LoanFormIssuance.objects.get(receipt=receipt_id)
	amount=record.loan_amount
	amount_converted = str(amount)[:-3]
	p = inflect.engine()
	amount_in_words=p.number_to_words(amount_converted).title()
	amount_saved =record.amount_saved

	
	p = inflect.engine()
	amount_saved_in_words=p.number_to_words(amount_saved).title()


	# naira_sign= str('\u20a6')
	# print(naira_sign)
	para1Style = ParagraphStyle('para1d')
	para1Style.fontSize = 10
	para1Style.alignment = TA_JUSTIFY
	# para1Style.spaceBefore = 4
	para1Style.spaceAfter = 5
	para1Style.fontName='Helvetica'
	para1Style.textColor = colors.HexColor('#000')


	

	para1=Paragraph(f"""Amount of loans applied for in words and figure:    <u><b>{amount_in_words} Naira Only </b></u>""",para1Style)
	para2=Paragraph(f" <u><b>=N={amount}</b></u>_________________________________________________________________",para1Style)
	para3=Paragraph("",para1Style)

	para4=Paragraph(f"""Amount deposited in words and figure:    <u><b>{amount_saved_in_words} Naira Only </b></u>""",para1Style)
	para5=Paragraph(f" <u><b>=N={amount_saved}</b></u>_________________________________________________________________",para1Style)
	para6=Paragraph("",para1Style)

	para7=Paragraph(f"""Declaration (by Borrower) I Agree to abide by the terms of the repayment of project loan stated below,
		I am aware that the Interest and Admin Charges are to be deducted up front""",para1Style)
	para8=Paragraph("",para1Style)
	para9=Paragraph(" <b>Signature:</b> _____________________________   <b>Date:</b> __________________________",para1Style)

	paraList=[para1,para2,para3,para4,para5,para6,para7,para8,para9]
	return paraList 


def Loan_Application_IssueanceSectionBTable(width,height):
	# record=CooperativeBankAccounts.objects.first()
	# record = CooperativeBankAccounts.objects.get(id=account)
	heightList = [
	height * 15 / 100,
	height * 85 / 100,
	]

	res = Table([
		[Loan_Application_IssueanceParagraphSectionB()],
		[Loan_Application_IssueanceSectionBDetailTable(width,heightList[1])],
		
		],
		width-20,
		heightList
		)

	res.setStyle([
		# ('GRID', (0, 0), (-1, -1), 1, 'black'),
		
		# ('FONTSIZE', (0,0), (-1,-1), 13),
		# ('FONTNAME', (0,0), (1,3), 'Helvetica-Bold'),

		# ('ALIGN', (0,0), (0,-1), 'RIGHT'),
		# ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),

		('LEFTPADDING', (0, 0), (-1, -1), 5),

		# ('BOTTOMPADDING', (0, 4), (-1, -1), 25),
		# ('BOTTOMPADDING', (0,1), (1,1), 20),
		])
	return res

def Loan_Application_IssueanceParagraphSectionB():


	para1Style = ParagraphStyle('para2')
	para1Style.fontSize = 10
	para1Style.alignment = TA_CENTER
	para1Style.spaceAfter = 5
	para1Style.fontName='Helvetica'
	para1Style.textColor = colors.HexColor('#000')

	para1=Paragraph("""<u><b>SECTION B:</b> (For Office Use Only)</u>""",para1Style)

	return para1

def Loan_Application_IssueanceSectionBDetailTable(width,height):
	res = Table([
		[__Loan_Application_IssueanceParagraphSectionBDetails()],
		
		],
		width-15,
		height,
		)

	res.setStyle([
		# ('GRID', (0, 0), (-1, -1), 1, 'black'),
		
		# ('FONTSIZE', (0,0), (-1,-1), 13),
		# ('FONTNAME', (0,0), (-1,-1), 'Helvetica-Bold'),

		# ('ALIGN', (0,0), (-1,-1), 'CENTER'),
		# ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),

		('LEFTPADDING', (0, 0), (-1, -1), 0),
		

		# ('BOTTOMPADDING', (0, 0), (-1, -1), 5),
		# ('BOTTOMPADDING', (0,1), (1,1), 20),
		])
	return res

def __Loan_Application_IssueanceParagraphSectionBDetails():

	para1Style = ParagraphStyle('para1d')
	para1Style.fontSize = 10
	para1Style.alignment = TA_JUSTIFY
	# para1Style.spaceBefore = 4
	para1Style.spaceAfter = 5
	para1Style.fontName='Helvetica'
	para1Style.textColor = colors.HexColor('#000')


	
	para1=Paragraph(f"""Amount deposited in words and figure:______________________________________________________________________""",para1Style)
	para2=Paragraph(f"""Amount of loans applied for in words and figure:_______________________________________________________________""",para1Style)
	para3=Paragraph(f"Amount Approved:______________________________________________________________________________________",para1Style)
	para4=Paragraph(f"Interest on Loan:_______________________________________________________________________________________",para1Style)
	para5=Paragraph(f"Admin Charge:_________________________________________________________________________________________",para1Style)
	para6=Paragraph(f"Approved/Not Approved:_________________________________________________________________________________",para1Style)
	para7=Paragraph(f"Payback Period:__________________________________<u>(No of Installation)</u>______________________________________",para1Style)
	para8=Paragraph(f"Repayment Starts:______________________________________Finish___________________________________________",para1Style)



	paraList=[para1,para2,para3,para4,para5,para6,para7,para8]
	return paraList 


def Loan_Application_IssueanceSectionCTable(width,height,pk):
	heightList=[
	height * 7 /100,
	height * 23 /100,
	height * 71 /100,
	]

	res = Table([
		[__Loan_Application_IssueanceParagraphSectionCTitle()],
		[__Loan_Application_IssueanceParagraphSectionCDeclaration(pk)],
		[Loan_Application_IssueanceSectionCDetailTable(width,heightList[2])],
		],
		width-25,
		heightList,
		)

	res.setStyle([
		# ('GRID', (0, 0), (-1, -1), 1, 'black'),

		('LEFTPADDING', (0, 0), (-1, -1), 0),
	
		])
	return res

def __Loan_Application_IssueanceParagraphSectionCTitle():

	paraCStyle = ParagraphStyle('paraCd')
	paraCStyle.fontSize = 10
	paraCStyle.alignment = TA_CENTER
	# paraCStyle.spaceBefore = 4
	paraCStyle.spaceAfter = 5
	paraCStyle.fontName='Helvetica-Bold'
	paraCStyle.textColor = colors.HexColor('#000')

	paraC=Paragraph(f"""<u>SECTION C:</u>""",paraCStyle)
	
	return paraC 


def __Loan_Application_IssueanceParagraphSectionCDeclaration(receipt_id):
	record=LoanFormIssuance.objects.get(receipt=receipt_id)
	guarantor_id= record.loan.guarantors

	guarantor=num2words(guarantor_id, to = 'year').title()
	transaction_type =(record.loan.name).lower()
	para1Style = ParagraphStyle('para1d')
	para1Style.fontSize = 10
	para1Style.alignment = TA_JUSTIFY
	# para1Style.spaceBefore = 4
	para1Style.spaceAfter = 5
	para1Style.fontName='Helvetica'
	para1Style.textColor = colors.HexColor('#000')


	
	para1=Paragraph(f"""{guarantor} Guarantor(s) who must be members of Transaction Institutions anchored by the Cooperative.""",para1Style)
	para2=Paragraph(f"""I am aware that ________________________________ is applying for the above mentioned {transaction_type} and 
		hereby guarantee him/her""",para1Style)
	


	paraList=[para1,para2]
	return paraList 



def Loan_Application_IssueanceSectionCDetailTable(width,height):
	heightList=[
		height * 50 /100,
		height * 50 /100,
		
	]
	
	widthList=[
		width * 5 /100,
		width * 90 /100,
	
	]

	res = Table([
		['1.',__Loan_Application_IssueanceRow1sectionCDetailTable()],
		['2.',__Loan_Application_IssueanceRow1sectionCDetailTable()],
		
	
		],
		widthList,
		heightList,
		)

	res.setStyle([
		# ('GRID', (0, 0), (-1, -1), 1, 'black'),

		('LEFTPADDING', (0, 0), (-1, -1), 0),
		('ALIGN', (0,0), (0,-1), 'LEFT'),
		('VALIGN', (0,0), (0,-1), 'TOP'),
	
		])
	return res

def __Loan_Application_IssueanceRow1sectionCDetailTable():

	para1Style = ParagraphStyle('para1d')
	para1Style.fontSize = 9
	para1Style.alignment = TA_JUSTIFY
	# para1Style.spaceBefore = 4
	para1Style.spaceAfter = 2
	para1Style.fontName='Helvetica'
	para1Style.textColor = colors.HexColor('#000')


	
	para1=Paragraph(f"""Name of Guarantor:_________________________________________________________________________________________""",para1Style)
	para2=Paragraph(f"""Signature:_________________________________________________________________________________________________""",para1Style)
	para3=Paragraph(f"""Department:_______________________________________________________________________________________________""",para1Style)
	para4=Paragraph(f"""Residential Address:_________________________________________________________________________________________""",para1Style)
	para5=Paragraph(f"""CTCS NO:_________________________________________________________________________________________________""",para1Style)
	
	


	paraList=[para1,para2,para3,para4,para5]
	return paraList 






def Loan_Application_IssueanceSectionApprovalTable(width,height):
	
	res = Table([
		[__Loan_Application_IssueanceParagraphSectionCApproval()],
		],
		width,
		height,
		)

	res.setStyle([
		# ('GRID', (0, 0), (-1, -1), 1, 'black'),

		('LEFTPADDING', (0, 0), (-1, -1), 0),
		# ('ALIGN', (0,0), (0,-1), 'LEFT'),
		# ('VALIGN', (0,0), (0,-1), 'MIDDLE'),
	
		])
	return res


def __Loan_Application_IssueanceParagraphSectionCApproval():

	para1Style = ParagraphStyle('para1d')
	para1Style.fontSize = 10
	para1Style.alignment = TA_JUSTIFY
	# para1Style.spaceBefore = 4
	para1Style.spaceAfter = 5
	para1Style.fontName='Helvetica'
	para1Style.textColor = colors.HexColor('#000')


	
	para1=Paragraph(f"""<b>Approval Officer</b> (President):______________________________<b>Signature Date:</b>______________________________""",para1Style)
	
	


	paraList=[para1,]
	return paraList 
