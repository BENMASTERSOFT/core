from django.utils.deprecation import MiddlewareMixin
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect


class LoginCheckMiddleWare(MiddlewareMixin):

	def process_view(self, request,view_func, view_args,view_kwargs):
		modulename=view_func.__module__
		user=request.user
	
		if user.is_authenticated:

			if user.user_type == "1":
				if modulename == "cooperative.master_views":
					pass
				elif modulename == "cooperative.views" or modulename == "django.views.static":
					pass
				else:
					return HttpResponseRedirect(reverse('admin_home'))

			elif user.user_type == "2":
				if modulename == "cooperative.master_views":
					pass
				elif modulename == "cooperative.views"  or modulename == "django.views.static":
					pass
				else:
					return HttpResponseRedirect(reverse("admin_home"))
			
	
			elif user.user_type == "3":
				if modulename == "cooperative.deskofficer_views":
					pass
				elif modulename == "cooperative.views"  or modulename == "django.views.static":
					pass
				else:
					return HttpResponseRedirect(reverse('deskofficer_home'))
			
		

			elif user.user_type == "4":
				if modulename == "cooperative.shop_views":
					pass
				elif modulename == "cooperative.views"  or modulename == "django.views.static":
					pass
				else:
					return HttpResponseRedirect(reverse('shop_home'))
			


			elif user.user_type == "10":
				pass




			else:
				return HttpResponseRedirect(reverse('ShowLoginPage'))

			
		else:
			if request.path == reverse("ShowLoginPage") or request.path == reverse("doLogin") or modulename == "django.contrib.auth.views":
				pass
			else:
				return HttpResponseRedirect(reverse("ShowLoginPage"))

