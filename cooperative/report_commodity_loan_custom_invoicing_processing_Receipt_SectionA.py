from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter, A4, landscape
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.enums import TA_JUSTIFY, TA_LEFT, TA_CENTER, TA_RIGHT
from . models import *

from .current_date import get_current_date,get_print_date
import os.path
from django.http import HttpResponse, HttpResponseRedirect
from . program import  generatePDF
from reportlab.platypus import Table, Image, Paragraph
from reportlab.lib import colors
from datetime import datetime
from datetime import date
import datetime
from django.utils.dateparse import parse_date
from dateutil.relativedelta import relativedelta

month_list =['JANUARY','FEBRUARY','MARCH','APRIL','MAY','JUNE','JULY','AUGUST','SEPTEMBER','OCTOBER','NOVEMBER','DECEMBER']


now = datetime.datetime.now()


def path_relative_to_file(base_file_path, relative_path):
    base_dir = os.path.dirname(os.path.abspath(base_file_path))
    return os.path.normpath(os.path.join(base_dir, relative_path))




def _commodity_temporary_invoice_original(width,height,receipt):
	record=Members_Commodity_Loan_Application.objects.get(receipt=receipt)
	heightList=[
	height*10 / 100,
	height*10 / 100,
	height*5 / 100,
	height*50 / 100,
	height*7 / 100,
	height*18 / 100,
	]
	
	line1 = f"This is to certify that the above named, has undertaken to pay the <u><b><i>Aformentioned Sum</i></b></u> being the cost of the above <u><b><i>items</i></b></u> in <u><b><i> {record.duration} months </i></b></u> as contained above."
	paraList =[]
	para1Style = ParagraphStyle('para1d')
	para1Style.fontSize = 12
	para1Style.alignment = TA_LEFT
	para1Style.spaceAfter = 10
	para1Style.fontName='Helvetica'
	para1Style.textColor = colors.HexColor('#000')



	para1 = Paragraph(line1,para1Style)
	# para2 = Paragraph(line2,para1Style)
	paraList = [para1]

	res = Table([
		[_invoiceHeader()],
		[_commodityReceiptTitleTable(width,heightList[1])],
		[_commodity_original_copy(width,heightList[2],receipt)],
		[_commodityReceiptBodyTable(width,heightList[3],receipt)],
		[paraList],
		[_commodityCerticateGenSignatureTable(width,heightList[5])],
		],
		width,
		heightList
		)

	res.setStyle([
		# ('GRID', (0, 0), (-1, -1), 1, 'red'),

		('LEFTPADDING', (0, 0), (-1, -1), 0),
		('LEFTPADDING', (0, 0), (0, 0), 5),
		('LEFTPADDING', (0, 4), (0, 4), 25),
		('RIGHTPADDING', (0, 4), (0, 4), 25),
		('BOTTOMPADDING', (0, 0), (0, 0), 5),

		('BOTTOMPADDING', (-1, -1), (-1, -1), 25),
		('LEFTPADDING', (-1, -1), (-1, -1), 0),
		

		('ALIGN',(0, 2), (0, 2), 'CENTER' ),
		# ('VLIGN',(0, 2), (0, 2), 'MIDDLE' ),
		])

	return res


def _commodity_original_copy(width,height,receipt):
	widthList=[
	width*30 / 100,
	width*40 / 100,
	width*30 / 100,
	]

	res = Table([
		['','ORIGINAL',f'RECEIPT NO: {receipt}'],
		],
		widthList,
		height
		)
	
	res.setStyle([
		# ('GRID', (1, 0), (1, 0), 1, 'red'),

		# ('LEFTPADDING', (0, 0), (-1, -1), 0),
		# ('LEFTPADDING', (0, 0), (0, 0), 5),
		# ('BOTTOMPADDING', (0, 0), (0, 0), 5),

		# ('BOTTOMPADDING', (-1, -1), (-1, -1), 25),
		('RIGHTPADDING', (-1, 0), (-1, 0), 30),
		
		('FONTSIZE', (1, 0), (1, 0), 12),
		('FONTNAME', (1, 0), (1, 0), 'Helvetica'),

		('ALIGN',(1, 0), (1, 0), 'CENTER' ),
		('ALIGN',(-1, 0), (-1, 0), 'RIGHT' ),
		# ('VLIGN',(1, 0), (1, 0), 'MIDDLE' ),
		])

	return res



def _commodity_temporary_invoice_duplicate(width,height,receipt):
	record=Members_Commodity_Loan_Application.objects.get(receipt=receipt)
	heightList=[
	height*10 / 100,
	height*10 / 100,
	height*5 / 100,
	height*50 / 100,
	height*7 / 100,
	height*18 / 100,
	]
	
	line1 = f"This is to certify that the above named, has undertaken to pay the <u><b><i>Aformentioned Sum</i></b></u> being the cost of the above <u><b><i>items</i></b></u> in <u><b><i> {record.duration} months </i></b></u> as contained above."
	paraList =[]
	para1Style = ParagraphStyle('para1d')
	para1Style.fontSize = 12
	para1Style.alignment = TA_LEFT
	para1Style.spaceAfter = 10
	para1Style.fontName='Helvetica'
	para1Style.textColor = colors.HexColor('#000')



	para1 = Paragraph(line1,para1Style)
	# para2 = Paragraph(line2,para1Style)
	paraList = [para1]

	res = Table([
		[_invoiceHeader()],
		[_commodityReceiptTitleTable(width,heightList[1])],
		[_commodity_duplicate_copy(width,heightList[2],receipt)],
		[_commodityReceiptBodyTable(width,heightList[3],receipt)],
		[paraList],
		[_commodityCerticateGenSignatureTable(width,heightList[5])],
		],
		width,
		heightList
		)

	res.setStyle([
		# ('GRID', (0, 4), (0, 4), 10, 'red'),

		('LEFTPADDING', (0, 0), (-1, -1), 0),
		('LEFTPADDING', (0, 0), (0, 0), 5),
		('LEFTPADDING', (0, 4), (0, 4), 25),
		('RIGHTPADDING', (0, 4), (0, 4), 25),
		('BOTTOMPADDING', (0, 0), (0, 0), 5),

		('BOTTOMPADDING', (-1, -1), (-1, -1), 25),
		('LEFTPADDING', (-1, -1), (-1, -1), 0),
		

		('ALIGN',(0, 2), (0, 2), 'CENTER' ),
		# ('VLIGN',(0, 2), (0, 2), 'MIDDLE' ),
		])

	return res




def _commodity_duplicate_copy(width,height,receipt):
	widthList=[
	width*30 / 100,
	width*40 / 100,
	width*30 / 100,
	]

	res = Table([
		['','DUPLICATE',f'RECEIPT NO: {receipt}'],
		],
		widthList,
		height
		)
	
	res.setStyle([
		# ('GRID', (1, 0), (1, 0), 1, 'red'),

		# ('LEFTPADDING', (0, 0), (-1, -1), 0),
		# ('LEFTPADDING', (0, 0), (0, 0), 5),
		# ('BOTTOMPADDING', (0, 0), (0, 0), 5),

		# ('BOTTOMPADDING', (-1, -1), (-1, -1), 25),
		('RIGHTPADDING', (-1, 0), (-1, 0), 30),
		
		('FONTSIZE', (1, 0), (1, 0), 12),
		('FONTNAME', (1, 0), (1, 0), 'Helvetica'),

		('ALIGN',(1, 0), (1, 0), 'CENTER' ),
		('ALIGN',(-1, 0), (-1, 0), 'RIGHT' ),
		# ('VLIGN',(1, 0), (1, 0), 'MIDDLE' ),
		])

	return res



def _invoiceHeader():
	line1="FETHA II STAFF CO-OPERATIVE THRIFT AND CREDIT SOCIETY"
	line2="LTD"


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




def _commodityReceiptTitleTable(width, height):
	widthList = [
		width * 30 / 100,
		width * 40 / 100,
		width * 30 / 100,
	]
	tdate=get_print_date(now)
	para1Style = ParagraphStyle('para1d')
	para1Style.fontSize = 14
	para1Style.alignment = TA_CENTER

	para1Style.fontName='Helvetica-Bold'
	para1Style.textColor = colors.HexColor('#000')


	cur_date =Paragraph(f'<u>{tdate}</u>',para1Style)
	receipt_tag =Paragraph(f'<u>TEMPORAL RECEIPT</u>',para1Style)


	img1='COOPLOGO.png'
	leftImagePath=path_relative_to_file(__file__, f'../static/logo/{img1}')
	leftImageWidth = widthList[0]
	leftImg = Image(leftImagePath, leftImageWidth, height, kind = 'proportional')

	res = Table([
		[leftImg,receipt_tag,cur_date]
		],
		widthList,
		height
		)

	res.setStyle([
		# ('GRID', (1, 0), (1, 0), 1, 'red'),

		('LEFTPADDING', (0, 0), (0, 0), 20),
		# ('LEFTPADDING', (0, 1), (1, 0), 15),
		# ('BOTTOMPADDING', (0, 0), (0, 0), 5),

		('BOTTOMPADDING', (1, 0), (-1, -1), 12),
		# ('LEFTPADDING', (-1, -1), (-1, -1), 0),
		

		('ALIGN',(1, 0), (1, 0), 'CENTER' ),
		# ('VLIGN',(1, 0), (1, 0), 'MIDDLE' ),
		])

	return res





def _commodityReceiptBodyTable(width,height,receipt):
	record=Members_Commodity_Loan_Application.objects.get(receipt=receipt)
	heightList = [
	height * 11 / 100,
	height * 11 / 100,
	height * 11 / 100,
	height * 11 / 100,
	height * 11 / 100,
	height * 11 / 100,
	height * 11 / 100,
	height * 11 / 100,
	height * 11 / 100,
	height * 1 / 100,
	
	
	
	]

	widthList=[
	width * 3 /100,
	width * 22 /100,
	width * 70 /100,
	width * 5 /100,
	]


	month = month_list[record.effective_date.month-1]
	effective_date = '{} {}'.format(month,record.effective_date.year)


	department=[]
	if record.member.member.department:
		department=record.member.member.department.title

	res = Table([
		
		['','NAME:',record.member.member.get_full_name,''],
		['','DEPT:',department,''],
		['','CTCS NO:',record.member.member.coop_no,''],
		['','PURCHASE:',record.member.product.product.product_name,''],
		['','SIZE:',record.member.product.product.details,''],
		['','QUANTITY:',record.member.quantity,''],
		['','AMOUNT:',record.coop_price,''],
		['','MONTHLY PAYMENT:',record.repayment,''],
		['','EFFECTIVE DATE:',effective_date,''],
		['','','',''],
	
		
		],
		widthList,
		heightList
		)

	res.setStyle([
		# ('GRID', (1, 1), (1, -1), 1, 'red'),
		('INNERGRID', (0, 0), (-1, -1), .9, 'grey'),
		('FONTSIZE', (0,0), (-1,-1), 11),
		('FONTNAME', (1, 0), (1, -1), 'Helvetica-Bold'),

		('ALIGN', (0,0), (-1,-1), 'LEFT'),
		('VALIGN', (0,0), (-1,-1), 'MIDDLE'),

		('LINEABOVE', (0,0), (-1,0), 1, 'red'),
		('LINEBELOW', (0,0), (-1,0), 1, 'red'),
		# ('RIGHTPADDING', (3,0), (-1,-1), 20),


		])


	return res


def _loanApplicationCerticatePersonnelSection(width,height,pk):
	applicant=LoansRepaymentBase.objects.get(loan_number=pk)
	heightList=[
		height * 30 / 100,
		height * 70 / 100,
		
	]
	para1Style = ParagraphStyle('para1d')
	para1Style.fontSize = 12
	para1Style.alignment = TA_CENTER
	
	para1Style.fontName='Helvetica'
	para1Style.textColor = colors.HexColor('#000')

	para1=Paragraph(f"""<u><b>SECTION A</b>(Personnal Data)</u>""",para1Style)
	

	res = Table([
		[para1],
		[_loanApplicationCerticatePersonnelBodyTable(width,heightList[1],pk)],
		],
		width-27,
		heightList,
		)
	res.setStyle([
		('GRID', (0, 0), (-1, -1), .8, 'grey'),
		('LEFTPADDING', (0, 0), (-1, -1), 0),
		('BOTTOMPADDING', (0, 0), (-1, -1), 0),
		('BOTTOMPADDING', (0, 0), (0, 0), 5),

		# ('INNERGRID', (0, 0), (-1, -1), .5, 'grey'),

		# ('LINEABOVE', (0,0), (-1,0), 1, 'red'),
		# ('LINEBELOW', (0,0), (-1,0), 1, 'red'),
		# ('LINEBELOW', (1,3), (1,3), 1, color),
		
		])
	return res


def _loanApplicationCerticatePersonnelBodyTable(width, height,pk):
	applicant=LoansRepaymentBase.objects.get(loan_number=pk)
	widthList = [
		width * 5 / 100,
		width * 10 / 100,
		width * 80 / 100,
	]

	heightList=[
	height * 50 /100,
	height * 50 /100,
	]
	res = Table([
		['','NAME:',applicant.member.get_full_name],
		['','COOP. NO:',applicant.member.member_id],

		],
		widthList,
		heightList
		)
	
	res.setStyle([
	# ('GRID', (0, 0), (-1, -1), 1, 'red'),
	('FONTNAME', (1,0), (1,-1), 'Helvetica-Bold'),
	('LINEBELOW', (0,0), (-1,-1), .8, 'grey'),
	
	])
	return res



def _loanApplicationCerticateGenBodyTable(width, height,pk):
	applicant=LoansRepaymentBase.objects.get(loan_number=pk)
	widthList = [
		width * 5 / 100,
		width * 25 / 100,
		width * 65 / 100,
	]

	heightList=[
	height * 10 /100,
	height * 9 /100,
	height * 9 /100,
	height * 9 /100,
	height * 9 /100,
	height * 9 /100,
	height * 9 /100,
	height * 9 /100,
	height * 9 /100,
	height * 9 /100,
	height * 9 /100,
	
	]
	# [_genPriceListTable(width,heightList[1])],

	res = Table([
		['','LOAN NUMBER',applicant.loan_number],
		['','LOAN TYPE',applicant.transaction.name],
		['','DURATION',f'{applicant.duration} Month(s)'],
		['','START DATE',get_print_date(applicant.start_date)],
		['','STOP DATE',get_print_date(applicant.stop_date)],
		['','LOAN AMOUNT',f'=N={applicant.loan_amount}'],
		['','MONTHLY REPAYMENT',f'=N={applicant.repayment}'],
		['','IINTEREST DEDUCTION',applicant.interest_deduction],
		['','INTEREST AMOUNT',f'=N={applicant.interest}'],
		['','IINTEREST RATE',f'{applicant.interest_rate}%'],
		['','ADMIN CHARGES',f'=N={applicant.admin_charge}'],
		],
		widthList,
		heightList
		)
	
	res.setStyle([
	('GRID', (0, 0), (-1, -1), .6, 'grey'),
	# ('INNERGRID', (0, 0), (-1, -1), .5, 'grey'),
	('LINEBELOW', (0,-1), (-1,-1), 1, 'grey'),
	# ('RIGHTPADDING', (0, 0), (-1, -1), 20),
	# ('LEFTPADDING', (0, 0), (-1, -1), 0),
	# ('LEFTPADDING', (0, 0), (0, 0), 15),
	# ('LEFTPADDING', (0, 1), (1, 1), 15),

	# ('BOTTOMPADDING', (0, 0), (-1, -1), 0),
	# ('BOTTOMPADDING', (0, 0), (0, 0), 1),
	# ('BOTTOMPADDING', (0, -1), (-1, -1), 60),

	# ('BACKGROUND', (0, 0), (-1, -1), color),


	('FONTNAME', (1,0), (1,-1), 'Helvetica-Bold'),

	# ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
	# ('VALIGN', (0, 0), (0, -1), 'BOTTOM'),
	# ('VALIGN', (-1, 0), (-1, -1), 'TOP'),
	("ROWBACKGROUNDS", (0,1), (-1,-1), [
			'antiquewhite', 'beige' #, colors.grey
			])
	])
	return res




def _commodityCerticateGenSignatureTable(width,height):
	width=width-31
	height=height-50
	style = ParagraphStyle('titlesign')
	style.fontName = 'Helvetica-Bold'
	style.fontSize = 12
	style.spaceAfter = 3
	style.alignment = TA_CENTER


	style1 = ParagraphStyle('titlesign1')
	style1.fontName = 'Helvetica'
	style1.fontSize = 8
	style1.spaceAfter = 3
	style1.alignment = TA_CENTER



	signPara1 = Paragraph(f'_______________________________',style1)
	signPara2 = Paragraph(f'Name and Signature',style)
	signPara3 = Paragraph(f'<i>FOR PRESIDENT</i>',style1)

	paraList = [signPara1,signPara2,signPara3]

	res =Table([
		[paraList],
	
		],
	width,
	height)


	res.setStyle([
	# ('GRID', (0, 0), (-1, -1), 10, 'red'),

	('TOPPADDING', (0, 0), (-1, -1), 100),

	('BOTTOMPADDING', (0, 0), (-1, -1), 0),

	# ('LINEABOVE', (0,0), (0,0), 3, 'red'),
	# ('BACKGROUND', (0, 0), (-1, -1), color),

	# ('TEXTCOLOR', (0, 0), (-1, -1), 'white'),

	('ALIGN', (0, 0), (-1, -1), 'CENTER'),
	# ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
	])
	return res




