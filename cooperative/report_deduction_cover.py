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

def path_relative_to_file(base_file_path, relative_path):
    base_dir = os.path.dirname(os.path.abspath(base_file_path))
    return os.path.normpath(os.path.join(base_dir, relative_path))




def deductionCoverDateTable(width,height,date):
	widthList = [
	width * 60 / 100,
	width * 30 / 100,
	width * 10 / 100,
	
	]
	res = Table([
		['',date,''],
		
	
		],
		widthList,
		height
		)

	res.setStyle([
		# ('GRID', (0, 0), (-1, -1), 1, 'black'),
		
		('FONTSIZE', (0,0), (-1,-1), 13),
		# ('FONTNAME', (0,1), (0,-1), 'Helvetica-Bold'),

		('ALIGN', (0,0), (-1,-1), 'RIGHT'),
		('VALIGN', (0,0), (-1,-1), 'MIDDLE'),

		# ('RIGHTPADDING', (3,0), (-1,-1), 20),


		])
	return res


def addressTable(width,height):
	heightList = [
	height * 60 / 100,
	height * 40 / 100,

	
	]
	res = Table([
		[_paragraphAddress()],
		['Sir'],
		
	
		],
		width,
		heightList
		)

	res.setStyle([
		# ('GRID', (0, 0), (-1, -1), 1, 'black'),
		
		('FONTSIZE', (0,0), (1,1), 13),
		('FONTNAME', (0,1), (1,1), 'Helvetica'),

		# ('ALIGN', (0,0), (-1,-1), 'RIGHT'),
		# ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),

		('LEFTPADDING', (0, 0), (-1, -1), 0),

		('BOTTOMPADDING', (0, 0), (1, 0), 10),
		('BOTTOMPADDING', (0,1), (1,1), 20),
		])
	return res



def _paragraphAddress():


	para1Style = ParagraphStyle('para1d')
	para1Style.fontSize = 14
	para1Style.alignment = TA_LEFT
	para1Style.spaceAfter = 3
	para1Style.fontName='Helvetica'
	para1Style.textColor = colors.HexColor('#000')

	para1=Paragraph("""Director of Finance""",para1Style)
	para2=Paragraph("Alex Ekwueme Federal University Teaching Hospital",para1Style)
	para3=Paragraph("Abakaliki",para1Style)


	paraList=[para1,para2,para3]
	
	return paraList 



def deductionOrderBodyTable(width,height,transaction_period):
	widthList=[
	width * 80 / 100,
	width * 20 / 100,
	]

	res = Table([
		[_paragraphBody(transaction_period),''],
			
		],
		widthList,
		height
		)

	res.setStyle([
		# ('GRID', (0, 0), (-1, -1), 1, 'black'),
		
		('FONTSIZE', (0,0), (1,1), 13),
		('FONTNAME', (0,1), (1,1), 'Helvetica'),

		# ('ALIGN', (0,0), (-1,-1), 'RIGHT'),
		# ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),

		('LEFTPADDING', (0, 0), (-1, -1), 0),

		('BOTTOMPADDING', (0, 0), (-1, -1), 50),
	
		])
	return res


def _paragraphBody(transaction_period):


	para1Style = ParagraphStyle('para1d')
	para1Style.fontSize = 13
	para1Style.alignment = TA_JUSTIFY
	# para1Style.spaceBefore = 4
	para1Style.spaceAfter = 7
	para1Style.fontName='Helvetica'
	para1Style.textColor = colors.HexColor('#000')


	paratTitleStyle = ParagraphStyle('paraAd')
	paratTitleStyle.fontSize = 13
	paratTitleStyle.alignment = TA_JUSTIFY
	paratTitleStyle.spaceAfter = 15
	paratTitleStyle.fontName='Helvetica-Bold'
	paratTitleStyle.textColor = colors.HexColor('#000')


	para1=Paragraph(f"""FORWARDING OF DEDUCTION SCHEDULE FOR MONTH OF {transaction_period}""",paratTitleStyle)
	para2=Paragraph("""This is to request that the amount against the names as per attached 
		schedule be""",para1Style)
	para3=Paragraph(f"""deducted from source for the month of {transaction_period}.""",para1Style)
	para4=Paragraph("in favour of <b>FETHA II Staff CTCS Ltd.</b>",para1Style)
	para5=Paragraph("Union Bank Account details as shown below:",para1Style)

	paraList=[para1,para2,para3,para4,para5]
	return paraList 


def bankTable(width,height,account):
	# record=CooperativeBankAccounts.objects.first()
	record = CooperativeBankAccounts.objects.get(id=account)
	widthList = [
	width * 25 / 100,
	width * 75 / 100,
	]


	heightList=[

	height * 12 /100,
	height * 12 /100,
	height * 12 /100,
	height * 12 /100,
	height * 40 /100,
	height * 12 /100,
	
	]

	res = Table([
		['BANK:',record.bank.title.upper()],
		['ACCOUNT NAME:',record.account_name.upper()],
		['ACCOUNT NUMBER:',record.account_number],
		['SORT CODE:',record.sort_code],
		['Thank you.',''],
		['',''],
		],
		widthList,
		heightList
		)

	res.setStyle([
		# ('GRID', (0, 0), (-1, -1), 1, 'black'),
		
		('FONTSIZE', (0,0), (-1,-1), 13),
		('FONTNAME', (0,0), (1,3), 'Helvetica-Bold'),

		# ('ALIGN', (0,0), (0,-1), 'RIGHT'),
		# ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),

		('LEFTPADDING', (0, 0), (-1, -1), 0),

		('BOTTOMPADDING', (0, 4), (-1, -1), 25),
		# ('BOTTOMPADDING', (0,1), (1,1), 20),
		])
	return res


def signatureTable(width,height,stafList):
	widthList = [
	width * 40 / 100,
	width * 50 / 100,
	width * 10 / 100,
	]


	heightList=[

	height * 20 /100,
	height * 20 /100,
	height * 20 /100,
	height * 20 /100,
	height * 20 /100,
	
	]

	res = Table([
		['','',''],
		['','',''],
		[stafList[0],stafList[1],''],
		[stafList[2],stafList[3],''],
		['','',''],
		
		],
		widthList,
		heightList
		)

	res.setStyle([
		# ('GRID', (0, 0), (-1, -1), 1, 'black'),
		
		('FONTSIZE', (0,0), (-1,-1), 13),
		('FONTNAME', (0,0), (-1,-1), 'Helvetica-Bold'),

		('ALIGN', (0,0), (-1,-1), 'CENTER'),
		('VALIGN', (0,0), (-1,-1), 'MIDDLE'),

		('LEFTPADDING', (0, 0), (-1, -1), 0),
		

		# ('BOTTOMPADDING', (0, 0), (-1, -1), 5),
		# ('BOTTOMPADDING', (0,1), (1,1), 20),
		])
	return res