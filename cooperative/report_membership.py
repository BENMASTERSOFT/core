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


def _membershipMainHeaderTitle():
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

def _membershipGenHeaderTable(width, height):
	widthList = [
		width * 2 / 100,
		width * 20 / 100,
		width * 56 / 100,
		width * 20 / 100,		
		width * 2 / 100,		
				
	]


	img1='COOPLOGO.png'
	leftImagePath=path_relative_to_file(__file__, f'../static/logo/{img1}')
	leftImageWidth = widthList[1]
	leftImg = Image(leftImagePath, leftImageWidth, height, kind = 'proportional')
	
	
	res = Table([
		['',leftImg, _membershipTitleTable(widthList[2],height), _membershipPassportTable(leftImageWidth,height),'']
		],
		widthList,
		height)

	res.setStyle([
		# ('GRID', (0, 0), (-1, -1), 1, 'red'),

		('LEFTPADDING', (0, 0), (-1, -1), 0),
		('LEFTPADDING', (0, 0), (0, 0), 10),

		('BOTTOMPADDING', (0, 0), (-1, -1), 5),

		('ALIGN',(0, 0), (0, 0), 'CENTER' ),
		('VLIGN',(0, 0), (0, 0), 'MIDDLE' ),

		# ('FONTSIZE', (2, 0), (2,0), 20),
		# ('LEFTPADDING', (2, 0), (2,0), -widthList[1] + 98),
		# ('BOTTOMPADDING', (2, 0), (2,0), 40),
		])
	
	return res

def _membershipPassportTable(width, height):
	img2='dummy.png'
	rightImagePath=path_relative_to_file(__file__, f'../static/logo/{img2}')
	rightImageWidth = width
	rightImg = Image(rightImagePath, rightImageWidth, height, kind = 'proportional')


	widthList = [
		width * 95 / 100,
		width * 5 / 100,		
	]

	res = Table([
		[rightImg,''],
		],
		widthList,height)

	res.setStyle([
		('GRID', (0, 0), (0, -1), 1, 'black'),


		('ALIGN', (3,0), (-1,-1), 'CENTER'),
		# ('RIGHTPADDING', (3,0), (-1,-1), 25),


		('VALIGN', (3,0), (-1,-1), 'MIDDLE'),
		])
	return res


def _membershipTitleTable(width,height):
	heightList = [
	height * 60 / 100,
	height * 30 / 100,
	height * 10 / 100,
	
	]
	res = Table([
		[_membershipTitlePara()],
		
		['MEMBERSHIP FORM'],
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


def _membershipTitlePara():
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

def _membershipReceiptSection(width,height,pk):
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


def _membershipGenBodyTable(width, height,pk):
	heightList = [
		height * 20 / 100,
		height * 80 / 100,
	]
	res = Table([
		[_membershipPersonalDataParagraph(pk)],
		[_membershipDetailsDataTable(width,heightList[1],pk)],

		],
		width-20,
		heightList
		)
	
	res.setStyle([
	# ('GRID', (0, 0), (-1, -1), 1, 'red'),

	('LEFTPADDING', (0, 0), (1, 0), 15),
	('RIGHTPADDING', (0, 0), (-1, -1), 20),
	# ('LEFTPADDING', (0, 0), (-1, -1), 0),

	('BOTTOMPADDING', (0, 0), (-1, -1), 0),
	('BOTTOMPADDING', (0, 0), (1, 0), 15),

	# ('BACKGROUND', (0, 0), (-1, -1), color),

	# ('TEXTCOLOR', (0, 0), (-1, -1), 'white'),

	# ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
	# ('VALIGN', (0, 0), (0, -1), 'BOTTOM'),
	# ('VALIGN', (-1, 0), (-1, -1), 'TOP'),
	])
	return res

def _membershipDetailsDataTable(width, height,pk):
	record=MemberShipFormSalesRecord.objects.get(receipt=pk)
	widthList = [
		width * 1 / 100,
		width * 33 / 100,
		width * 46 / 100,
		width * 20 / 100,
	]

	heightList = [
		height * 5 / 100,
		height * 5 / 100,
		height * 5 / 100,
		height * 5 / 100,
		height * 5 / 100,
		height * 5 / 100,
		height * 5 / 100,
		height * 5 / 100,
		height * 5 / 100,
		height * 5 / 100,
		height * 5 / 100,
		height * 5 / 100,
		height * 5 / 100,
		height * 5 / 100,
		height * 5 / 100,
		height * 5 / 100,
		height * 5 / 100,
		height * 5 / 100,
		height * 5 / 100,
		
		height * 5 / 100,
		

	]
	paraPhoneStyle = ParagraphStyle('paraphone')
	# paraPhoneStyle.fontSize = 13
	# paraPhoneStyle.alignment = TA_JUSTIFY
	# paraPhoneStyle.spaceBefore = 5
	# paraPhoneStyle.spaceAfter = 10
	# paraPhoneStyle.fontName='Helvetica'
	# paraPhoneStyle.wordWrap='LTR'
	# paraPhoneStyle.spaceShrinkage=.02
	# paraPhoneStyle.leading=20
	paraPhoneStyle.textColor = colors.HexColor('#000')

	# paraPhoneStyle.leftIndent=0
	# paraPhoneStyle.rightIndent=0

	paraPhone = Paragraph(f'<u>{record.applicant.phone_number}</u>_____________________________________',paraPhoneStyle)

	res = Table([
		['','My Next of Kin is:', '_______________________________________________________________'],
		['','Relationship:', '_______________________________________________________________'],
		['','Address:', '_______________________________________________________________'],
		['','Phone Number:', '_______________________________________________________________'],
		['','Residential Addr.(optional):', '______________________________________________________________'],
		['','', '_______________________________________________________________'],
		['','Perm. Home Addr.(optional):', '________________________________________________________________'],
		['','', '________________________________________________________________'],
		['','File Number:', '________________________________________________________________'],
		['','IPPIS Number:', '________________________________________________________________'],
		['','Date of First Appt(optional):', '________________________________________________________________'],
		
		['','Phone Number:', paraPhone],
		['','Salary Grade & Step:', '________________________________________________________________'],
		['','Email Address:', '________________________________________________________________'],
		
		['','', ''],
		['','Bank Name:', '________________________________________________________________'],
		['','Account Number:', '________________________________________________________________'],
		['','', ''],
	
		['','', ''],
		['','', 'Sign: ____________________  Date: __________________________________'],
		
		],
		widthList,
		heightList,
		)
	
	res.setStyle([
	# ('GRID', (0, 0), (-1, -1), 1, 'red'),

	('LEFTPADDING', (0, 0), (-1, -1), 0),

	('BOTTOMPADDING', (0, 0), (-1, -1), 10),
	# ('LINEBELOW', (1, 0), (-1, -1), 5, 'red'),
	('FONTSIZE', (1,0), (1,-1), 14),
	('FONTNAME', (1,0), (1,-1), 'Helvetica'),

	])
	return res

def _membershipPersonalDataParagraph(pk):
	record=MemberShipFormSalesRecord.objects.get(receipt=pk)
	para1Style = ParagraphStyle('para1c')
	para1Style.fontSize = 14
	para1Style.alignment = TA_JUSTIFY
	para1Style.spaceBefore = 5
	para1Style.spaceAfter = 10
	para1Style.fontName='Helvetica'
	para1Style.wordWrap='LTR'
	para1Style.spaceShrinkage=.02
	para1Style.leading=20
	para1Style.textColor = colors.HexColor('#000')

	para1Style.leftIndent=0
	para1Style.rightIndent=0
	try:		
		department=record.applicant.department.title
	except:
		department='________________'

	para1=Paragraph(f"I,<u> <b> {record.applicant.last_name} {record.applicant.first_name} {record.applicant.middle_name}</b> </u> of the Department of <u><b>{department}</b></u>, <b>Alex  Ekwueme Federal university Hospital, Abakaliki</b> hereby give my consent to register and belong to the above named cooperative society",para1Style)
	para2=Paragraph("I have also accepted to abide by the regulations that guide the society",para1Style)

	paraList = [para1,para2]

	return paraList


def _membershipGenFooterTable(width, height,operator):
	line1=''
	line2=''
	if ReportFooter.objects.filter(code='001').exists():
		footer_text=ReportFooter.objects.get(code='001')
		note=footer_text.note
		

	# date_format = '%Y-%m-%d'
            
 #    current_date = datetime.strptime(now, date_format)

	tdate = get_print_date(now)
	text1 = str(note)
	text2=f"Printed By:{operator}      Date Printed: {tdate}"

	heightList = [
		height * 60 / 100,
		height * 30 / 100,
	]
	res = Table([
			[text1],
			[text2],
			], 
			width, heightList)


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

