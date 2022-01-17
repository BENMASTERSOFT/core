from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, HttpResponseRedirect
from cooperative.models import *
from django.contrib import messages
from django.urls import reverse
from cooperative.forms import *
from django.db.models import Q
import datetime
from django.db.models import Count, Sum
from datetime import datetime
from datetime import date

from django.contrib import messages
# Create your views here.

  
def auditor_home(request):
		
	title="AUDITOR"
	context={
	'title':title,
	
	}
	return render(request, "auditor_templates/dashboard.html",context)


def basic_form(request):
	return render(request, 'auditor_templates/basics/basic_form1.html')


def basic_table(request):
	return render(request, 'auditor_templates/basics/basic_tables.html')

def datatable_table(request):
	return render(request, 'auditor_templates/basics/datatable.html')

