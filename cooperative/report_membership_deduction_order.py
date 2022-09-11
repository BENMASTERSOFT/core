from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter, A4, landscape
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.enums import TA_JUSTIFY, TA_LEFT, TA_CENTER, TA_RIGHT
from . models import *
from .current_date import get_print_date
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

now = datetime.datetime.now()

def path_relative_to_file(base_file_path, relative_path):
    base_dir = os.path.dirname(os.path.abspath(base_file_path))
    return os.path.normpath(os.path.join(base_dir, relative_path))



def _membershipDeductionOrderHeader():
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


def _membershipDeductionOrderGetLogoTable(width, height):
	widthList = [
		width * 20 / 100,
		width * 60 / 100,
		width * 20 / 100,
	]


	img1='COOPLOGO.png'
	leftImagePath=path_relative_to_file(__file__, f'../static/logo/{img1}')
	leftImageWidth = widthList[0]
	leftImg = Image(leftImagePath, leftImageWidth, height, kind = 'proportional')

	res = Table([
		[leftImg,_membershipDeductionOrderTitleTable(widthList[1],height),'']
		],
		widthList,
		height
		)

	res.setStyle([
		# ('GRID', (0, 0), (-1, -1), 1, 'red'),

		('LEFTPADDING', (0, 0), (-1, -1), 0),
		# ('LEFTPADDING', (0, 0), (0, 0), 10),

		('BOTTOMPADDING', (0, 0), (-1, -1), 0),
		

		('ALIGN',(0, 0), (0, 0), 'CENTER' ),
		('VLIGN',(0, 0), (0, 0), 'MIDDLE' ),

	
		])

	return res


def _membershipDeductionOrderTitleTable(width,height):
	heightList = [
	height * 60 / 100,
	height * 30 / 100,
	height * 10 / 100,
	
	]
	res = Table([
		[__membershipDeductionOrderTitlePara()],
		
		['DEDUCTION FORM'],
		[''],
		],
		width,
		heightList
		)

	res.setStyle([
		# ('GRID', (0, 0), (-1, -1), 1, 'black'),
		
		('FONTSIZE', (0,1), (0,-1), 14),
		('FONTNAME', (0,1), (0,-1), 'Helvetica-Bold'),

		('ALIGN', (0,0), (-1,-1), 'CENTER'),
		('VALIGN', (0,0), (-1,-1), 'MIDDLE'),

		# ('RIGHTPADDING', (3,0), (-1,-1), 20),


		])


	return res

def __membershipDeductionOrderTitlePara():
	header_text=ReportHeader.objects.first()
	line3=header_text.line3
	line4=header_text.line4

	para1Style = ParagraphStyle('para1d')
	para1Style.fontSize = 14
	para1Style.alignment = TA_CENTER
	para1Style.spaceAfter = 3
	para1Style.fontName='Helvetica-Bold'
	para1Style.textColor = colors.HexColor('#000')

	para1=Paragraph(f"""<b>{line3}</b>""",para1Style)
	para2=Paragraph(f"<b>{line4}</b>",para1Style)

	paraList=[para1,para2]
	
	return paraList 



def _membershipDeductionOrderReceiptSection(width,height,pk):
	record=MemberShipFormSalesRecord.objects.get(receipt=pk)
	widthList=[
		width * 30 / 100,
		width * 40 / 100,
		width * 30 / 100,
	]
	receipt=record.receipt

	tdate = get_print_date(record.tdate)

	paraReceipt = Paragraph(f"<b>Receipt No:</b> {receipt}")
	paraId = Paragraph(f'<b>CTCS NO:</b>')
	paraDate = Paragraph(f'<b>Date:</b> {tdate}')
	res = Table([
		[paraReceipt,paraId,paraDate]
		],
		widthList,
		height,
		)
	res.setStyle([
		# ('GRID', (0, 0), (-1, -1), 1, 'black'),
		('LEFTPADDING', (0, 0), (-1, -1), 10),
		('INNERGRID', (0, 0), (-1, -1), .5, 'grey'),

		('LINEABOVE', (0,0), (-1,0), 1, 'red'),
		('LINEBELOW', (0,0), (-1,0), 1, 'red'),
		# ('LINEBELOW', (1,3), (1,3), 1, color),
		
		])
	return res


def _membershipDeductionOrderDeductionGenBodyTable(width, height,pk):
	heightList = [
		height * 20 / 100,
		height * 50 / 100,
		height * 30 / 100,
	]

	# [_genPriceListTable(width,heightList[1])],
	widthList=[
	width*90/100,
	width*0/100,
	]
	res = Table([
		[_membershipDeductionOrderDeductionPersonalDataParagraph(pk),''],
		[_membershipDeductionOrderGenPriceListTable(width,heightList[1]),''],
		[_membershipDeductionOrderGenSignatureTable(width,heightList[2]),''],

		],
		widthList,
		heightList
		)
	
	res.setStyle([
	# ('GRID', (0, 0), (-1, -1), 1, 'red'),

	# ('RIGHTPADDING', (0, 0), (-1, -1), 20),
	('LEFTPADDING', (0, 0), (-1, -1), 0),
	('LEFTPADDING', (0, 0), (0, 0), 15),
	# ('LEFTPADDING', (0, 1), (1, 1), 15),

	('BOTTOMPADDING', (0, 0), (-1, -1), 0),
	('BOTTOMPADDING', (0, 0), (0, 0), 1),
	('BOTTOMPADDING', (0, -1), (-1, -1), 60),

	# ('BACKGROUND', (0, 0), (-1, -1), color),

	# ('TEXTCOLOR', (0, 0), (-1, -1), 'white'),

	# ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
	# ('VALIGN', (0, 0), (0, -1), 'BOTTOM'),
	# ('VALIGN', (-1, 0), (-1, -1), 'TOP'),
	])
	return res

def _membershipDeductionOrderDeductionPersonalDataParagraph(pk):
	record=MemberShipFormSalesRecord.objects.get(receipt=pk)
	paraStyle = ParagraphStyle('para1cc')
	paraStyle.fontSize = 12
	paraStyle.alignment = TA_JUSTIFY
	# paraStyle.spaceBefore = 2
	paraStyle.spaceAfter = 3
	paraStyle.fontName='Helvetica'
	paraStyle.wordWrap='LTR'
	paraStyle.spaceShrinkage=.02
	paraStyle.leading=20
	paraStyle.textColor = colors.HexColor('#000')

	paraStyle.leftIndent=0
	paraStyle.rightIndent=0
	
	try:		
		department=record.applicant.department.title
	except:
		department='________________'


	para1=Paragraph(f"I,<u> <b> {record.applicant.last_name} {record.applicant.first_name} {record.applicant.middle_name}</b> </u> of the Department of <u><b>{department}</b></u>, <b>Alex  Ekwueme Federal university Hospital, Abakaliki</b> hereby give my consent to be saving",paraStyle)
	para2=Paragraph("the sum of ____________________________________________________________________",paraStyle)
	para3=Paragraph("(__________________) with effect from _________________________________________",paraStyle)

	paraList = [para1,para2,para3]

	return paraList


def _membershipDeductionOrderGenPriceListTable(width, height):

	# style = ParagraphStyle('titleprices')
	# style.fontSize = 20
	# style.fontName = 'Helvetica-Bold'
	# style.spaceAfter = 15

	# titlePara = Paragraph('Details',style)

	pricesTable = _membershipDeductionOrderGenPricesTable(width * 97 / 100, height * 90 / 100)
	
	elementsList = [pricesTable]


	res = Table([
		[elementsList]
		],

		width,
		height)

	res.setStyle([
		# ('GRID', (0, 0), (-1, -1), 1, 'red'),


		('LEFTPADDING', (0,0), (-1,-1), 10),
		# ('RIGHTPADDING', (0,0), (-1,-1), -20),
		('BOTTOMPADDING', (0,0), (-1,-1), 0),

		])
	return res


def _membershipDeductionOrderGenPricesTable(width, height):
	records=TransactionTypes.objects.filter(source__title='SAVINGS')

	matrix = [['TYPES OF SAVINGS','AMOUNT']]


	# fileName='priceTable.csv'
	# filePath=path_relative_to_file(__file__, f'../resources/{fileName}')
	# with open(filePath, 'r') as file:
		# matrix = list(csv.reader(file))
	for record in records:
		data = [record.name,'']

		matrix.append(data)
	
	matrix.append(("TOTAL",''))
	
	

	widthList = [
		width * 40 / 100,
		width * 50 / 100,
		width * 10 / 100,
		

	]
	rowCount = len(matrix)
	res = Table(matrix, widthList, height / rowCount,'')


	color = colors.toColor('rgba(0, 115, 153, 0.9)')

	res.setStyle([
	
		('GRID', (0, 0), (-1, -1), .5, 'grey'),

		# ('BACKGROUND', (0,0), (-1,0), color),
		# ('TEXTCOLOR', (0,0), (-1,0), 'white'),
		('FONTSIZE', (0,0), (-1,0), 12),
		('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),

		('ALIGN', (1,0), (-1,0), 'CENTER'),
		('VALIGN', (0,0), (-1,-1), 'MIDDLE'),

		('ALIGN', (1,1), (2,-1), 'CENTER'),
		('ALIGN', (5,1), (5,-1), 'RIGHT'),

		# ("ROWBACKGROUNDS", (0,1), (-1,-1), [
		# 	'antiquewhite', 'beige' #, colors.grey
		# 	])
		])

	return res

def _membershipDeductionOrderGenSignatureTable(width,height):

	widthList=[
		width * 25 /100,
		width * 55 /100,
		width * 20 /100,
	]

	res =Table([
		['TOTAL SHARE:','_______________________________________',''],
		['SIGN:','_______________________________________',''],
		['DATE:','_______________________________________',''],
		['PHONE:','_______________________________________',''],
	],
	widthList,
	height * 10 /100)


	res.setStyle([
	# ('GRID', (0, 0), (-1, -1), 1, 'red'),

	('LEFTPADDING', (0, 0), (-1, -1), 5),

	('BOTTOMPADDING', (0, 0), (-1, -1), 0),

	# ('BACKGROUND', (0, 0), (-1, -1), color),

	# ('TEXTCOLOR', (0, 0), (-1, -1), 'white'),

	# ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
	# ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
	])
	return res

def _membershipDeductionOrderGenFooterTable(width, height,operator):
	
	tdate = get_print_date(now)
	
	text2=f"Printed By:{operator}      Date Printed: {tdate}"


	res = Table([
			[text2],
			], 
			width, height)


	color = colors.HexColor('#003363')

	res.setStyle([
	# ('GRID', (0, 0), (-1, -1), 1, 'red'),

	('LEFTPADDING', (0, 0), (-1, -1), 0),

	('BOTTOMPADDING', (0, 0), (-1, -1), 10),

	('BACKGROUND', (0, 0), (0, 0), color),
	('FONTSIZE', (0,0), (0,0), 9),
	('TEXTCOLOR', (0, 0), (0, 0), 'white'),

	('ALIGN', (0, 0), (-1, -1), 'CENTER'),
	('VALIGN', (0, 0), (0, -1), 'BOTTOM'),


	('VALIGN', (-1, 0), (-1, -1), 'TOP'),
	('FONTSIZE', (-1, 0), (-1, -1), 8),
	])
	return res