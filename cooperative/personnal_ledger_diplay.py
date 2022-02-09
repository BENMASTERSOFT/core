from . models import PersonalLedger
from django.db.models import Q


def Display_PersonalLedger(account_number,start_date,stop_date):
	records=PersonalLedger.objects.filter(account_number=account_number).filter(Q(transaction_period__gte=start_date) & Q(transaction_period__lte=stop_date))

	return records