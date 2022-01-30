from .models import *
from django.utils.dateparse import parse_date
from dateutil.relativedelta import relativedelta
from datetime import datetime
from django.db.models import Count, Sum


def coopshopledger(member,tdate1,tdate2):
	records = CooperativeShopLedger.objects.filter(member__member=member).filter(created_at__range=[tdate1,tdate2])

	return records

def shopCashDepositFilter(tdate,processed_by,status):
	tyear=int(tdate.year)
	tmonth=int(tdate.month)
	tday=int(tdate.day)

	records=Cooperative_Shop_Cash_Deposit.objects.filter(tdate__year=tyear,tdate__month=tmonth,tdate__day=tday,processed_by=processed_by,status=status)
	return records

def calculateTotalCashDeposit(tdate,processed_by,status):
	tyear=int(tdate.year)
	tmonth=int(tdate.month)
	tday=int(tdate.day)

	queryset=  Cooperative_Shop_Cash_Deposit.objects.filter(tdate__year=tyear,tdate__month=tmonth,tdate__day=tday,processed_by=processed_by,status=status).aggregate(total_cash=Sum('amount'))
	total_amount=queryset['total_cash']
	return total_amount