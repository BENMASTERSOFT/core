from .models import *
from django.utils.dateparse import parse_date
from dateutil.relativedelta import relativedelta
from datetime import datetime
from django.db.models import Count, Sum


def coopshopledger(account_number,tdate1,tdate2):
	records = CooperativeShopLedger.objects.filter(account_number=account_number,created_at__range=[tdate1,tdate2])

	return records

def shopCashDepositFilter(tdate,processed_by,status):
	tyear=int(tdate.year)
	tmonth=int(tdate.month)
	tday=int(tdate.day)

	records=Cooperative_Shop_Cash_Deposit.objects.filter(tdate__year=tyear,tdate__month=tmonth,tdate__day=tday,processed_by=processed_by,status2=status)
	return records

def calculateTotalCashDeposit(tdate,processed_by,status):
	tyear=int(tdate.year)
	tmonth=int(tdate.month)
	tday=int(tdate.day)

	queryset=  Cooperative_Shop_Cash_Deposit.objects.filter(tdate__year=tyear,tdate__month=tmonth,tdate__day=tday,processed_by=processed_by,status2=status).aggregate(total_cash=Sum('amount_paid'))
	total_amount=queryset['total_cash']
	return total_amount

def get_cooperative_shop_balance(account_number):
	transaction_status=TransactionStatus.objects.get(title='TREATED')
	ledger_balance=0
	if CooperativeShopLedger.objects.filter(account_number=account_number).exists():
		ledger=CooperativeShopLedger.objects.filter(account_number=account_number).last()
		ledger_balance=ledger.balance
		ledger.status=transaction_status
		ledger.save()

	return ledger_balance


def cooperative_shop_ledger_posting(account_number,status,member,particulars,debit,credit,balance,tdate,processed_by):
	CooperativeShopLedger(account_number=account_number,status=status,member=member,particulars=particulars,debit=debit,credit=credit,balance=balance,tdate=tdate,processed_by=processed_by).save()
	return 0