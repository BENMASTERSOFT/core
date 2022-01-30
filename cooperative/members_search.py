from .models import *
from django.db.models import Q


def searchMembers(frm,status):
	records=Members.objects.filter(Q(phone_number__icontains=frm) | Q(file_no__icontains=frm) | Q(admin__first_name__icontains=frm) | Q(admin__last_name__icontains=frm) | Q(middle_name__icontains=frm)).filter(status=status)
	return records


def searchShopMembers(frm,status):
	records=CooperativeShopLedger.objects.filter(Q(member__member__phone_number__icontains=frm) | Q(member__member__admin__first_name__icontains=frm) | Q(member__member__admin__last_name__icontains=frm) | Q(member__member__middle_name__icontains=frm)).filter(Q(balance__lt=0) & Q(status=status))
	return records