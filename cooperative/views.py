from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from cooperative.EmailBackEnd import EmailBackEnd
from django.contrib import messages
from django.urls import reverse



def home(request):
	return render(request,'cooperative/dashboard.html')

def ShowLoginPage(request):
	return render(request,'cooperative/users/sign_in.html')


def doLogin(request):
	if request.method!="POST":
		return HttpResponse("<h2>Method Not Allowed</h2>")
	else:
		user=EmailBackEnd.authenticate(request,username=request.POST.get("username"),password=request.POST.get("password"))
		if user!=None:
			
			login(request,user)
			if user.user_type=="1":
				return HttpResponseRedirect(reverse('admin_home'))
			elif user.user_type=="2":
			
				return HttpResponseRedirect(reverse('president_home'))
			elif user.user_type=="3":
				return HttpResponseRedirect(reverse('secretary_home'))

			elif user.user_type=="4":
				return HttpResponseRedirect(reverse('treasurer_home'))

			elif user.user_type=="5":
				return HttpResponseRedirect(reverse('FINSEC_home'))
			
			elif user.user_type=="6":
				return HttpResponseRedirect(reverse('deskofficer_home'))
			

			elif user.user_type=="7":
				return HttpResponseRedirect(reverse('SEO_home'))
			

			elif user.user_type=="8":
				return HttpResponseRedirect(reverse('shop_home'))

			elif user.user_type=="9":
				return HttpResponseRedirect(reverse('auditor_home'))
			

			else:

				return HttpResponse("Not Seen")
			
		else:
			messages.error(request,"Invalid Login Details")
			return HttpResponseRedirect("/")


def GetUserDetails(request):
	if request.user!=None:
		return HttpResponse("User :"+request.user.email+" Usertype :"+request.user.user_type)
	else:
		return HttpResponse("Please Login First")


def logout_user(request):
	logout(request)
	return HttpResponseRedirect("/")
