
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4


def generatePDF():
	pdf = canvas('report.pdf', pagesize = A4)


	pdf.save()

	return 0