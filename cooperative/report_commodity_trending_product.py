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

now = datetime.datetime.now()

def path_relative_to_file(base_file_path, relative_path):
    base_dir = os.path.dirname(os.path.abspath(base_file_path))
    return os.path.normpath(os.path.join(base_dir, relative_path))



def _trendingProductHeader():
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


def _trendingProductGetLogoTable(width, height):
	widthList = [
		width * 20 / 100,
		width * 56 / 100,
		width * 19 / 100,
	]
	tdate=get_print_date(now)
	para1Style = ParagraphStyle('para1d')
	para1Style.fontSize = 14
	para1Style.alignment = TA_CENTER

	para1Style.fontName='Helvetica-Bold'
	para1Style.textColor = colors.HexColor('#000')


	cur_date =Paragraph(f'<u>{tdate}</u>',para1Style)

	img1='COOPLOGO.png'
	leftImagePath=path_relative_to_file(__file__, f'../static/logo/{img1}')
	leftImageWidth = widthList[0]
	leftImg = Image(leftImagePath, leftImageWidth, height, kind = 'proportional')

	res = Table([
		[leftImg,_trendingProductTitleTable(widthList[1],height),cur_date]
		],
		widthList,
		height
		)

	res.setStyle([
		# ('GRID', (0, 0), (-1, -1), 1, 'red'),

		('LEFTPADDING', (0, 0), (-1, -1), 0),
		('LEFTPADDING', (0, 0), (0, 0), 5),
		('BOTTOMPADDING', (0, 0), (0, 0), 5),

		('BOTTOMPADDING', (-1, -1), (-1, -1), 25),
		('LEFTPADDING', (-1, -1), (-1, -1), 0),
		

		('ALIGN',(0, 2), (0, 2), 'CENTER' ),
		# ('VLIGN',(0, 2), (0, 2), 'MIDDLE' ),
		])

	return res


def _trendingProductTitleTable(width,height):
	heightList = [
	height * 60 / 100,
	height * 30 / 100,
	height * 10 / 100,
	
	]
	res = Table([
		[_trendingProductPara()],
		
		['LIST OF PRODUCTS'],
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



def _trendingProductPara():
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



def _trendingProductBodyTable(width,height):
	heightList = [
	height * 7 / 100,
	height * 7 / 100,
	height * 7 / 100,
	height * 7 / 100,
	height * 7 / 100,
	height * 7 / 100,
	height * 7 / 100,
	height * 7 / 100,
	height * 7 / 100,
	height * 7 / 100,
	height * 7 / 100,
	height * 7 / 100,
	height * 7 / 100,
	height * 7 / 100,
	height * 2 / 100,
	
	]

	widthList=[
	width * 5 /100,
	width * 20 /100,
	width * 50 /100,
	width * 20 /100,
	width * 5 /100,
	]
	
	res = Table([
		
		[''],
		[''],
		[''],
		[''],
		[''],
		[''],
		[''],
		[''],
		[''],
		[''],
		[''],
		[''],
		[''],
		[''],
		[''],
	
		],
		width,
		heightList
		)

	res.setStyle([
		('GRID', (0, 0), (-1, -1), 1, 'black'),
		
		('FONTSIZE', (0,1), (0,-1), 14),
		('FONTNAME', (0,1), (0,-1), 'Helvetica-Bold'),

		('ALIGN', (0,0), (-1,-1), 'CENTER'),
		('VALIGN', (0,0), (-1,-1), 'MIDDLE'),

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

def _loanApplicationCerticateGenNextOfKinTable(width, height,pk):

	style = ParagraphStyle('titlenok')
	style.fontName = 'Helvetica'
	style.fontSize = 12
	style.alignment = TA_CENTER

	titlePara = Paragraph(f'<u><b>SECTION C</b><i>(Next of Kin)</i></u>',style)

	heightList = [
		height * 20 /100,
		height * 75 /100,
	]

	res = Table([
		[titlePara],
		[_loanApplicationCerticateNextOfKinBodyTable(width,heightList[1],pk)],
		],

		width-27,
		heightList)

	res.setStyle([
		('GRID', (0, 0), (-1, -1), .6, 'grey'),

		('BOTTOMPADDING', (0,0), (0,0), 10),
		('LEFTPADDING', (0,0), (-1,-1), 0),
		# ('RIGHTPADDING', (0,0), (-1,-1), -20),
		# ('BOTTOMPADDING', (0,0), (-1,-1), 0),

		])
	return res


def _loanApplicationCerticateNextOfKinBodyTable(width, height,pk):
	applicant=LoansRepaymentBase.objects.get(loan_number=pk)
	# NOK=MembersNextOfKins.objects.get(id=applicant.nok_id)
	widthList = [
		width * 5 / 100,
		width * 15 / 100,
		width * 75 / 100,
	]

	heightList=[
		height * 25 /100,
		height * 25 /100,
		height * 25 /100,
		height * 25 /100,
	]
	res = Table([
		['','NAME:',applicant.nok_name],
		['','PHONE NO:',applicant.nok_phone_no],
		['','RELATIONSHIP:',applicant.nok_Relationship],
		['','ADDRESS:',applicant.nok_address],

		],
		widthList,
		heightList
		)
	
	res.setStyle([
	# ('GRID', (0, 0), (-1, -1), 1, 'red'),
	('FONTNAME', (1,0), (1,-1), 'Helvetica-Bold'),
	('LINEBELOW', (0,0), (-1,-1), .8, 'grey'),
	('BOTTOMPADDING', (0,0), (0,0), 10),
	])
	return res



def _loanApplicationCerticateGenGurantorTable(width, height,pk):

	style = ParagraphStyle('titlenok')
	style.fontName = 'Helvetica'
	style.fontSize = 12

	style.spaceAfter = 20
	style.alignment = TA_CENTER

	titlePara = Paragraph(f'<u><b>SECTION D</b><i>(Guarantors)</i></u>',style)

	heightList = [
		height * 20 /100,
		height * 80 /100,
	]

	res = Table([
		[titlePara],
		[_loanApplicationCerticateGuarantorBodyTable(width,heightList[1],pk)],
		],

		width-27,
		heightList)

	res.setStyle([
		# ('GRID', (0, 0), (-1, -1), .6, 'grey'),

	# ('INNERGRID', (0, 0), (-1, -1), .5, 'grey'),
		('LEFTPADDING', (0,0), (-1,-1), 0),
		# ('RIGHTPADDING', (0,0), (-1,-1), -20),
		('BOTTOMPADDING', (0,0), (0,0), 10),

		])
	return res


def _loanApplicationCerticateGuarantorBodyTable(width, height,pk):
	# applicant=LoansRepaymentBase.objects.get(loan_number=pk)
	
	widthList = [
		width * 5 / 100,
		width * 5 / 100,
		width * 85 / 100,
	
	]

	heightList=[
		height * 50 /100,
		height * 50 /100,
		
	]
	res = Table([
		['','1',_loanApplicationCerticateGuarantor1BodyDetailsTable(widthList[2],heightList[0],pk)],
		['','2',_loanApplicationCerticateGuarantor2BodyDetailsTable(widthList[2],heightList[1],pk)],
	
		

		],
		widthList,
		heightList
		)
	
	res.setStyle([
	('GRID', (0, 0), (-1, -1), .7, 'grey'),
	# ('FONTNAME', (1,0), (1,-1), 'Helvetica-Bold'),
	# ('LINEBELOW', (0,0), (-1,-1), .8, 'grey'),
	('BOTTOMPADDING', (0,0), (0,0), 15),
	])
	return res



def _loanApplicationCerticateGuarantor1BodyDetailsTable(width, height,pk):
	applicant=LoansRepaymentBase.objects.get(loan_number=pk)
	guarantor1=LoanGuarantors.objects.filter(loan=applicant).first()
	
	widthList = [
		
		width * 15 / 100,
		width * 83.5 / 100,
	]

	heightList=[
		height * 50 /100,
		height * 50 /100,
	
	]
	res = Table([
		['NAME:',guarantor1.member.get_full_name],
		['COOP NO:',guarantor1.member.get_member_Id],
	
		],
		widthList,
		heightList
		)
	
	res.setStyle([
	# ('GRID', (0, 0), (-1, -1), 1, 'red'),
	('FONTNAME', (0,0), (0,-1), 'Helvetica-Bold'),
	('LINEBELOW', (0,0), (-1,-1), .8, 'grey'),
	('LEFTPADDING', (0,0), (0,-1), 0),
	])
	return res


def _loanApplicationCerticateGuarantor2BodyDetailsTable(width, height,pk):
	applicant=LoansRepaymentBase.objects.get(loan_number=pk)
	guarantors=LoanGuarantors.objects.filter(loan=applicant)
	

	widthList = [
		
		width * 15 / 100,
		width * 83.5 / 100,
	]

	heightList=[
		height * 50 /100,
		height * 50 /100,
	
	]

	res = []
	if guarantors.count()>1:
		guarantor2=LoanGuarantors.objects.filter(loan=applicant).last()

		res = Table([
			['NAME:',guarantor2.member.get_full_name],
			['COOP NO:',guarantor2.member.get_member_Id],
		
			],
			widthList,
			heightList
			)
	else:
		res = Table([
			['NAME:',""],
			['COOP NO:',''],
		
			],
			widthList,
			heightList
			)

	res.setStyle([
	# ('GRID', (0, 0), (-1, -1), 1, 'red'),
	('FONTNAME', (0,0), (0,-1), 'Helvetica-Bold'),
	('LINEBELOW', (0,0), (-1,-1), .8, 'grey'),
	('LEFTPADDING', (0,0), (0,-1), 0),
	])
	return res



def _loanApplicationCerticateGenSignatureTable(width,height):
	width=width-31
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
	signPara2 = Paragraph(f'PROF. IYARE',style)
	signPara3 = Paragraph(f'<i>PRESIDENT</i>',style1)

	paraList = [signPara1,signPara2,signPara3]

	res =Table([
		[paraList],
	
		],
	width,
	height)


	res.setStyle([
	# ('GRID', (0, 0), (-1, -1), 1, 'red'),

	('TOPPADDING', (0, 0), (-1, -1), 55),

	('BOTTOMPADDING', (0, 0), (-1, -1), 7),

	# ('LINEABOVE', (0,0), (0,0), 3, 'red'),
	# ('BACKGROUND', (0, 0), (-1, -1), color),

	# ('TEXTCOLOR', (0, 0), (-1, -1), 'white'),

	('ALIGN', (0, 0), (-1, -1), 'CENTER'),
	# ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
	])
	return res




def _loanApplicationCerticateMembershipGenFooterTable(width, height,operator):
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
		height * 55 / 100,
		height * 45 / 100,
	]

	widthList=[
	width * 5 /100,
	width * 90 /100,
	width * 5 /100,
	]

	res = Table([
			['',text1,''],
			['',text2,''],
			], 
			widthList, heightList)


	color = colors.HexColor('#003363')

	res.setStyle([
	# ('GRID', (0, 0), (-1, -1), 1, 'red'),

	('TOPPADDING', (1, 1), (1, 1), 10),

	('BOTTOMPADDING', (1, 0), (1, 0), 5),

	('BACKGROUND', (0, 0), (1, 0), color),
	('FONTSIZE', (1,0), (1,0), 9),
	('TEXTCOLOR', (1, 0), (1, 0), 'white'),

	('ALIGN', (1, 1), (1, 1), 'CENTER'),
	('VALIGN', (1, 1), (1, 1), 'BOTTOM'),


	# ('VALIGN', (-1, 0), (-1, -1), 'TOP'),
	# ('FONTSIZE', (-1, 0), (-1, -1), 8),
	])
	return res

