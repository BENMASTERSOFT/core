from django.contrib import admin
from cooperative.models import CustomUser

from django.contrib.auth.admin import UserAdmin


class UserModel(UserAdmin):
	pass


admin.site.register(CustomUser,UserModel)
