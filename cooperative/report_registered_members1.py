from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter, A4, landscape
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.enums import TA_JUSTIFY, TA_LEFT, TA_CENTER, TA_RIGHT

from . models import *

from . report_header import _titlePara

from .current_date import get_print_date
import os.path
from django.http import HttpResponse, HttpResponseRedirect



from . program import  generatePDF
from reportlab.platypus import Table, Image, Paragraph
from reportlab.lib import colors




def path_relative_to_file(base_file_path, relative_path):
    base_dir = os.path.dirname(os.path.abspath(base_file_path))
    return os.path.normpath(os.path.join(base_dir, relative_path))


def _registeredMembersMainHeaderTitle():
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





# def _registeredMembersGetLogoTable(width, height):
# 	widthList = [
# 		width * 20 / 100,
# 		width * 55 / 100,
# 		width * 10 / 100,
# 	]


# 	img1='COOPLOGO.png'
# 	leftImagePath=path_relative_to_file(__file__, f'../static/logo/{img1}')
# 	leftImageWidth = widthList[0]
# 	leftImg = Image(leftImagePath, leftImageWidth, height, kind = 'proportional')

# 	res = Table([
# 		[leftImg,registeredMembersTitleTable(widthList[1],height),'']
# 		],
# 		widthList,
# 		height
# 		)

# 	res.setStyle([
# 		('GRID', (0, 0), (-1, -1), 2, 'red'),

# 		# ('LEFTPADDING', (0, 0), (-1, -1), 0),
		

# 		# ('BOTTOMPADDING', (0, 0), (-1, -1), 0),
		

# 		# ('ALIGN',(0, 0), (0, 0), 'CENTER' ),
# 		# ('VLIGN',(0, 0), (0, 0), 'MIDDLE' ),

	
# 		])

# 	return res


def registeredMembersTitleTable(width,height):
	heightList = [
	height * 60 / 100,
	height * 30 / 100,
	height * 10 / 100,
	
	]
	res = Table([
		[_titlePara()],
		
		['REGISTERED MEMBER FORM'],
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


def registeredMemberReceiptSection(width,height,pk):
	record=Members.objects.get(ippis_no=pk)
	widthList=[
		width * 30 / 100,
		width * 40 / 100,
		width * 30 / 100,
	]
	receipt=record.applicant.receipt
	member_id=record.member_id

	tdate = get_print_date(record.tdate)

	paraReceipt = Paragraph(f"<b>Receipt No:</b> {receipt}")
	paraId = Paragraph(f'<b>CTCS NO:</b> {member_id}')
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



def registeredMemberBody(width,height,pk):
	record=Members.objects.get(ippis_no=pk)

	return "BODY"