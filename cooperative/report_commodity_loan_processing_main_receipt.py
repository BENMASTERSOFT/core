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
import inflect

month_list =['JANUARY','FEBRUARY','MARCH','APRIL','MAY','JUNE','JULY','AUGUST','SEPTEMBER','OCTOBER','NOVEMBER','DECEMBER']


now = datetime.datetime.now()
inflector = inflect.engine()


def path_relative_to_file(base_file_path, relative_path):
    base_dir = os.path.dirname(os.path.abspath(base_file_path))
    return os.path.normpath(os.path.join(base_dir, relative_path))




def _commodity_main_invoice_original(width,height,receipt):
	record=Members_Commodity_Loan_Application.objects.get(receipt=receipt)
	heightList=[
	height*8 / 100,
	height*10 / 100,
	height*3 / 100,
	height*10 / 100,
	height*62 / 100,
	height*7 / 100,
	]
	width=width-5

	# line1 = f"This is to certify that the above named, has undertaken to pay the <u><b><i>Aformentioned Sum</i></b></u> being the cost of the above <u><b><i>items</i></b></u> in <u><b><i> {record.duration} months </i></b></u> as contained above."
	# paraList =[]
	# para1Style = ParagraphStyle('para1d')
	# para1Style.fontSize = 12
	# para1Style.alignment = TA_LEFT
	# para1Style.spaceAfter = 10
	# para1Style.fontName='Helvetica'
	# para1Style.textColor = colors.HexColor('#000')



	# para1 = Paragraph(line1,para1Style)
	# # para2 = Paragraph(line2,para1Style)
	# paraList = [para1]

	res = Table([
		[_invoiceHeader()],
		[_commodityMainReceiptLogoTable(width,heightList[1])],
		[_commodityMainReceiptCaption(width,heightList[2],record.receipt)],
		[_commodityCustomerSection(width,heightList[3],record.receipt)],
		[_commodity_main_invoice_details(width,heightList[4],record.receipt)],
		[_commodity_main_invoiceSignatureTable(width,heightList[5])],
		],
		width,
		heightList
		)

	res.setStyle([
		('GRID', (0, 0), (-1, -1), 1, 'red'),

		('LEFTPADDING', (0, 0), (-1, -1), 0),
		# ('LEFTPADDING', (0, 0), (0, 0), 5),
		# ('LEFTPADDING', (0, 4), (0, 4), 25),
		# ('RIGHTPADDING', (0, 4), (0, 4), 25),
		('BOTTOMPADDING', (0, 0), (-1, -1), 0),

		('BOTTOMPADDING', (0, 0), (0, 0), 10),
		# ('LEFTPADDING', (-1, -1), (-1, -1), 0),
		

		('ALIGN',(0, 2), (0, 2), 'CENTER' ),
		# ('VLIGN',(0, 2), (0, 2), 'MIDDLE' ),
		])

	return res


def _invoiceHeader():
	line1="FETHA II STAFF CO-OPERATIVE THRIFT AND CREDIT SOCIETY LTD."



	paraList =[]
	para1Style = ParagraphStyle('para1d')
	para1Style.fontSize = 11
	para1Style.alignment = TA_CENTER
	# para1Style.spaceAfter = 10
	para1Style.fontName='Helvetica-Bold'
	para1Style.textColor = colors.HexColor('#000')


	para2Style = ParagraphStyle('para2d')
	para2Style.fontSize = 9
	para2Style.alignment = TA_CENTER
	# para2Style.spaceAfter = 20
	para2Style.fontName='Helvetica'
	para2Style.textColor = colors.HexColor('#000')


	para1 = Paragraph(line1,para1Style)
	para2 = Paragraph(f'<u><b>Motto:</b></u> United we Stand',para2Style)
	paraList = [para1,para2]
	return paraList


def _commodityMainReceiptLogoTable(width, height):
	widthList = [
		width * 30 / 100,
		width * 40 / 100,
		width * 30 / 100,
	]
	tdate=get_print_date(now)

	para1Style = ParagraphStyle('para1d')
	para1Style.fontSize = 12
	para1Style.alignment = TA_LEFT
	para1Style.spaceAfter = 3
	para1Style.fontName='Helvetica-Bold'
	para1Style.textColor = colors.HexColor('#000')

	line1 =Paragraph(f'<u>HEAD OFFICE</u>',para1Style)
	
	para2Style = ParagraphStyle('para2d')
	para2Style.fontSize = 10
	para2Style.alignment = TA_LEFT

	para2Style.fontName='Helvetica'
	para2Style.textColor = colors.HexColor('#000')
	
	line2 =Paragraph('FETHA II',para2Style)

	para3Style = ParagraphStyle('para3d')
	para3Style.fontSize = 10
	para3Style.alignment = TA_LEFT

	para3Style.fontName='Helvetica'
	para3Style.textColor = colors.HexColor('#000')
	
	line3 =Paragraph('Abakaliki,',para3Style)

	para4Style = ParagraphStyle('para4d')
	para4Style.fontSize = 10
	para4Style.alignment = TA_LEFT

	para4Style.fontName='Helvetica'
	para4Style.textColor = colors.HexColor('#000')
	
	line4 =Paragraph('Ebonyi State.',para4Style)

	paraList = [line1,line2,line3,line4]

	img1='COOPLOGO.png'
	leftImagePath=path_relative_to_file(__file__, f'../static/logo/{img1}')
	leftImageWidth = widthList[0]
	leftImg = Image(leftImagePath, leftImageWidth, height-15, kind = 'proportional')

	res = Table([
		[paraList,leftImg,'Phone Numbers']
		],
		widthList,
		height
		)

	res.setStyle([
		# ('GRID', (1, 0), (1, 0), 1, 'red'),

		('LEFTPADDING', (0, 0), (0, 0), 10),
		# ('LEFTPADDING', (0, 1), (1, 0), 15),
		# ('BOTTOMPADDING', (0, 0), (0, 0), 5),

		('BOTTOMPADDING', (1, 0), (-1, -1), 12),
		# ('LEFTPADDING', (-1, -1), (-1, -1), 0),
		

		('ALIGN',(1, 0), (1, 0), 'CENTER' ),
		# ('VLIGN',(1, 0), (1, 0), 'MIDDLE' ),
		])

	return res




def _commodityMainReceiptCaption(width,height,receipt):
	widthList=[
	width*30 / 100,
	width*40 / 100,
	width*30 / 100,
	]

	res = Table([
		['','Cash/Credit Sales Invoice',f'NO: {receipt}'],
		],
		widthList,
		height
		)
	
	res.setStyle([
		('GRID', (1, 0), (1, 0), 1, 'red'),

		# ('LEFTPADDING', (0, 0), (-1, -1), 0),
		# ('LEFTPADDING', (0, 0), (0, 0), 5),
		# ('BOTTOMPADDING', (0, 0), (0, 0), 5),

		# ('BOTTOMPADDING', (-1, -1), (-1, -1), 25),
		('RIGHTPADDING', (-1, 0), (-1, 0), 30),
		
		('FONTSIZE', (0, 0), (-1, -1), 10),
		('FONTNAME', (0, 0), (-1, -1), 'Helvetica'),

		# ('ALIGN',(1, 0), (1, 0), 'CENTER' ),
		# ('ALIGN',(-1, 0), (-1, 0), 'RIGHT' ),
		# ('VLIGN',(1, 0), (1, 0), 'MIDDLE' ),
		])

	return res


def _commodityCustomerSection(width,height,receipt):

	widthList=[
	width*60 / 100,
	width*40 / 100,
	]

	res = Table([
		[_commodityCustomerSectionDetailsContainer(widthList[0],height,receipt),_commodityCustomerSectionDateContainer(widthList[1],height,receipt)],
		],
		widthList,
		height
		)
	
	res.setStyle([
		# ('GRID', (0, 0), (-1, -1), 1, 'red'),

		# ('LEFTPADDING', (0, 0), (-1, -1), 0),
		('LEFTPADDING', (0, 0), (-1, -1), 0),
		# ('BOTTOMPADDING', (0, 0), (0, 0), 5),

		# ('BOTTOMPADDING', (-1, -1), (-1, -1), 25),
		('RIGHTPADDING', (-1, 0), (-1, 0), 30),
		
		('FONTSIZE', (0, 0), (-1, -1), 10),
		('FONTNAME', (0, 0), (-1, -1), 'Helvetica'),

		# ('ALIGN',(1, 0), (1, 0), 'CENTER' ),
		# ('ALIGN',(-1, 0), (-1, 0), 'RIGHT' ),
		# ('VLIGN',(1, 0), (1, 0), 'MIDDLE' ),
		])

	return res


def _commodityCustomerSectionDetailsContainer(width,height,receipt):
	
	width=width-10

	height=height-10

	res = Table([
		[_commodityCustomerSectionDetails(width,height,receipt)],
		],
		width,
		height
		)
	
	res.setStyle([
		# ('GRID', (0, 0), (-1, -1), 1, 'red'),

		# ('LEFTPADDING', (0, 0), (-1, -1), 0),
		('LEFTPADDING', (0, 0), (0, -1), 5),
		# ('BOTTOMPADDING', (0, 0), (0, 0), 5),

		# ('BOTTOMPADDING', (-1, -1), (-1, -1), 25),
		('RIGHTPADDING', (0, 0), (-1, -1), 0),
		
		('FONTSIZE', (0, 0), (-1, -1), 10),
		('FONTNAME', (0, 0), (-1, -1), 'Helvetica'),
		('FONTNAME', (0, 0), (0, -1), 'Helvetica-Bold'),

		# ('ALIGN',(1, 0), (1, 0), 'CENTER' ),
		# ('ALIGN',(-1, 0), (-1, 0), 'RIGHT' ),
		# ('VLIGN',(1, 0), (1, 0), 'MIDDLE' ),
		])

	return res

def _commodityCustomerSectionDetails(width,height,receipt):
	record=Members_Commodity_Loan_Application.objects.get(receipt=receipt)
	name=record.member.member.get_full_name

	phone_number=record.member.member.phone_number

	residential_address=[]
	if record.member.member.residential_address:
		residential_address=record.member.member.residential_address
	

	widthList=[
	width*24 / 100,
	width*76 / 100,
	]

	heightList=[
	height*33/100,
	height*33/100,
	height*33/100,
	]

	res = Table([
		['Name:',name],
		['Address:',residential_address],
		['Phone No:',phone_number],
		],
		widthList,
		heightList
		)
	
	res.setStyle([
		('GRID', (0, 0), (-1, -1), 1, 'red'),

		# ('LEFTPADDING', (0, 0), (-1, -1), 0),
		('LEFTPADDING', (0, 0), (0, -1), 5),
		# ('BOTTOMPADDING', (0, 0), (0, 0), 5),

		# ('BOTTOMPADDING', (-1, -1), (-1, -1), 25),
		('RIGHTPADDING', (0, 0), (-1, -1), 0),
		
		('FONTSIZE', (0, 0), (-1, -1), 10),
		('FONTNAME', (0, 0), (-1, -1), 'Helvetica'),
		('FONTNAME', (0, 0), (0, -1), 'Helvetica-Bold'),

		# ('ALIGN',(1, 0), (1, 0), 'CENTER' ),
		# ('ALIGN',(-1, 0), (-1, 0), 'RIGHT' ),
		# ('VLIGN',(1, 0), (1, 0), 'MIDDLE' ),
		])

	return res



def _commodityCustomerSectionDateContainer(width,height,receipt):

	width=width-10

	height=height-10

	res = Table([
		[_commodityCustomerSectionDate(width,height,receipt)],
		],
		width,
		height
		)
	
	res.setStyle([
		# ('GRID', (0, 0), (-1, -1), 1, 'red'),

		# ('LEFTPADDING', (0, 0), (-1, -1), 0),
		('LEFTPADDING', (0, 0), (0, -1), 5),
		# ('BOTTOMPADDING', (0, 0), (0, 0), 5),

		# ('BOTTOMPADDING', (-1, -1), (-1, -1), 25),
		('RIGHTPADDING', (0, 0), (-1, -1), 0),
		
		('FONTSIZE', (0, 0), (-1, -1), 10),
		('FONTNAME', (0, 0), (-1, -1), 'Helvetica'),
		('FONTNAME', (0, 0), (0, -1), 'Helvetica-Bold'),

		# ('ALIGN',(1, 0), (1, 0), 'CENTER' ),
		# ('ALIGN',(-1, 0), (-1, 0), 'RIGHT' ),
		# ('VLIGN',(1, 0), (1, 0), 'MIDDLE' ),
		])

	return res

def _commodityCustomerSectionDate(width,height,receipt):
	record=Members_Commodity_Loan_Application.objects.get(receipt=receipt)
	tdate=get_current_date(record.tdate)

	widthList=[
		width*33 / 100,
		width*33 / 100,
		width*34 / 100,
	]

	heightList=[
		height*50/100,
		height*50/100,
	
	]

	res = Table([
		['Day','Month','Year'],
		[str(tdate.day).zfill(2),str(tdate.month).zfill(2),tdate.year],
		],
		widthList,
		heightList
		)
	
	res.setStyle([
		('GRID', (0, 0), (-1, -1), 1, 'red'),

		# ('LEFTPADDING', (0, 0), (-1, -1), 0),
		('LEFTPADDING', (0, 0), (0, -1), 5),
		# ('BOTTOMPADDING', (0, 0), (0, 0), 5),

		# ('BOTTOMPADDING', (-1, -1), (-1, -1), 25),
		('RIGHTPADDING', (0, 0), (-1, -1), 0),
		
		('FONTSIZE', (0, 0), (-1, -1), 10),
		('FONTNAME', (0, 0), (-1, -1), 'Helvetica'),
		('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),

		# ('ALIGN',(1, 0), (1, 0), 'CENTER' ),
		# ('ALIGN',(-1, 0), (-1, 0), 'RIGHT' ),
		# ('VLIGN',(1, 0), (1, 0), 'MIDDLE' ),
		])

	return res


def _commodity_main_invoice_details(width,height,receipt):
	record=Members_Commodity_Loan_Application.objects.get(receipt=receipt)
	heightList=[
	height*70 / 100,
	height*15 / 100,
	height*15 / 100,

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
		[_commodity_main_invoice_details_analysis(width,heightList[0],receipt)],
		[_commodity_main_invoice_details_legend(width,heightList[1],receipt)],
		[_commodity_main_invoice_numbertoWords(width,heightList[2],receipt)],
		
		],
		width,
		heightList
		)

	res.setStyle([
		('GRID', (0, 0), (-1, -1), 1, 'red'),

		('LEFTPADDING', (0, 0), (-1, -1), 0),
		('BOTTOMPADDING', (0, 0), (-1, -1), 0),

		
	
		# ('ALIGN',(0, 2), (0, 2), 'CENTER' ),
		# ('VLIGN',(0, 2), (0, 2), 'MIDDLE' ),
		])

	return res




def _commodity_main_invoice_details_analysis(width,height,receipt):
	record=Members_Commodity_Loan_Application.objects.get(receipt=receipt)
	widthList=[
	width*7 / 100,
	width*63 / 100,
	width*10 / 100,
	width*20 / 100,
	]

	heightList=[
	height*10/100,
	height*10/100,
	height*10/100,
	height*10/100,
	height*10/100,
	height*10/100,
	height*10/100,
	height*10/100,
	height*10/100,
	height*10/100,
	]

	res = Table([
		['QTY','DESCRIPTION','RATE','AMOUNT(=N=)'],
		[record.member.quantity,record.member.product.product.product_name,'',record.member.coop_price],
		['',f'Model: {record.member.product.product.product_model}','',''],
		['',f'Size: {record.member.product.product.details}','',''],
		['','','',''],
		['',f'Serial No:: {record.serial_no}','',''],
		['','','',''],
		['','','',''],
		['','','',''],
		['','','',''],
		],
		widthList,
		heightList
		)
	
	res.setStyle([
		('GRID', (0, 0), (-1, -1), 1, 'red'),

		# ('LEFTPADDING', (0, 0), (-1, -1), 0),
		# ('LEFTPADDING', (0, 0), (0, 0), 5),
		# ('BOTTOMPADDING', (0, 0), (0, 0), 5),

		# ('BOTTOMPADDING', (-1, -1), (-1, -1), 25),
		# ('RIGHTPADDING', (-1, 0), (-1, 0), 30),
		
		('FONTSIZE', (0, 0), (-1, -1), 10),
		('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),

		# ('ALIGN',(1, 0), (1, 0), 'CENTER' ),
		('ALIGN',(-1, 0), (-1, -1), 'RIGHT' ),
		# ('VLIGN',(1, 0), (1, 0), 'MIDDLE' ),
		])

	return res


def _commodity_main_invoice_details_legend(width, height,receipt):
	height=height-5
	width=width-10
	widthList = [
		width * 61 / 100,
		width * 39 / 100,
		
	]
	paraList = []
	para1Style = ParagraphStyle('para1d')
	para1Style.fontSize = 10
	para1Style.alignment = TA_LEFT

	para1Style.fontName='Helvetica'
	para1Style.textColor = colors.HexColor('#000')


	
	line1 =Paragraph(f'<i>Received the above goods in in good condition</i>',para1Style)
	line2 =Paragraph(f'<i>No refund of money after payment</i>',para1Style)

	paraList = [line1,line2]

	res = Table([
		[paraList,_commodity_main_invoice_details_legendTable(widthList[1],height,receipt)]
		],
		widthList,
		height
		)

	res.setStyle([
		# ('GRID', (0, 0), (-1, -1), 1, 'red'),

		# ('LEFTPADDING', (0, 0), (0, 0), 20),
		# ('LEFTPADDING', (0, 1), (1, 0), 15),
		# ('BOTTOMPADDING', (0, 0), (0, 0), 5),

		('BOTTOMPADDING', (0, 0), (0, 0), 15),
		# ('LEFTPADDING', (-1, -1), (-1, -1), 0),
		

		('ALIGN',(0, 0), (0, 0), 'CENTER' ),
		# ('VLIGN',(0, 0), (0, 0), 'MIDDLE' ),
		])

	return res


def _commodity_main_invoice_details_legendTable(width,height,receipt):
	record=Members_Commodity_Loan_Application.objects.get(receipt=receipt)
	heightList = [
	height * 34 / 100,
	height * 33 / 100,
	height * 33 / 100,
	]

	widthList=[
	width * 50 /100,
	width * 50 /100,
	]
	
	res = Table([
		
		['TOTAL',record.coop_price],
		['DEPOSIT',record.coop_price],
		['BALANCE',0.00],
			
		],
		widthList,
		heightList
		)

	res.setStyle([
		# ('GRID', (0, 0), (0, -1), 1, 'red'),
		('GRID', (0, 0), (-1, -1), .9, 'grey'),
		('FONTSIZE', (0,0), (-1,-1), 10),
		('FONTNAME', (0, 0), (0, -1), 'Helvetica-Bold'),

		('ALIGN', (0,0), (-1,-1), 'RIGHT'),
		# ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),

		# ('LINEABOVE', (0,0), (-1,0), 1, 'red'),
		# ('LINEBELOW', (0,0), (-1,0), 1, 'red'),
		# ('RIGHTPADDING', (3,0), (-1,-1), 20),


		])


	return res


def _commodity_main_invoice_numbertoWords(width, height,receipt):
	record=Members_Commodity_Loan_Application.objects.get(receipt=receipt)
	height=height-5
	width=width-10


	widthList = [
		width * 61 / 100,
		width * 39 / 100,
		
	]
	paraList = []
	para1Style = ParagraphStyle('para1d')
	para1Style.fontSize = 10
	para1Style.alignment = TA_LEFT

	para1Style.fontName='Helvetica'
	para1Style.textColor = colors.HexColor('#000')


	words=str(record.coop_price)[:-3]
	word1=str(record.coop_price)[-2:]

	words = str(inflector.number_to_words(int(words))).title()
	word1 = str(inflector.number_to_words(int(word1))).title()
	# amount_in_word=(f'{words} Naira {word1} kobo')
	


	
	line1 =Paragraph(f'<b>Amount in Words:</b> <u>{words}</u> Naira <u>{word1}</u> kobo',para1Style)
	

	paraList = [line1]

	res = Table([
		[paraList]
		],
		width,
		height
		)

	res.setStyle([
		# ('GRID', (0, 0), (-1, -1), 1, 'red'),

		# ('LEFTPADDING', (0, 0), (0, 0), 20),
		# ('LEFTPADDING', (0, 1), (1, 0), 15),
		# ('BOTTOMPADDING', (0, 0), (0, 0), 5),

		('BOTTOMPADDING', (0, 0), (0, 0), 15),
		# ('LEFTPADDING', (-1, -1), (-1, -1), 0),
		

		('ALIGN',(0, 0), (0, 0), 'LEFT' ),
		# ('VLIGN',(0, 0), (0, 0), 'MIDDLE' ),
		])

	return res



def _commodity_main_invoiceSignatureTable(width,height):
	# width=width-31
	# height=height-50

	style = ParagraphStyle('titlesign')
	style.fontName = 'Helvetica-Bold'
	style.fontSize = 8
	style.spaceAfter = 0
	style.alignment = TA_LEFT


	style1 = ParagraphStyle('titlesign1')
	style1.fontName = 'Helvetica'
	style1.fontSize = 8
	# style1.spaceAfter = 3
	style1.alignment = TA_LEFT



	signPara1 = Paragraph(f'_______________________________',style1)
	signPara2 = Paragraph(f"Customer's Sign",style)
	signPara3 = Paragraph(f'<i>For FETHA II CTCS</i>',style)

	paraList = [signPara1,signPara2]
	paraList1 = [signPara1,signPara3]

	widthList=[
	width*50/100,
	width*50/100,
	]

	
	res =Table([
		[paraList,paraList1],
		
		],
	widthList,
	height)


	res.setStyle([
	# ('GRID', (0, 0), (-1, -1), 10, 'red'),

	('TOPPADDING', (0, 0), (-1, -1), 100),

	('BOTTOMPADDING', (0, 0), (-1, -1), 3),

	# ('LINEABOVE', (0,0), (0,0), 3, 'red'),
	# ('BACKGROUND', (0, 0), (-1, -1), color),

	# ('TEXTCOLOR', (0, 0), (-1, -1), 'white'),

	('ALIGN', (0, 0), (-1, -1), 'CENTER'),
	# ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
	])
	return res




