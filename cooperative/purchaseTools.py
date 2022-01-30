from .models import *
from django.db.models import Count, Sum

def purchaseTempTotal(purchase):
	queryset=Purchases_Temp.objects.filter(purchase=purchase).aggregate(total_cost=Sum('total_cost'),total_item=Sum('quantity'))
	# print(queryset['total_cost'])
	# print("============================")
	return (queryset['total_cost'],queryset['total_item'])
	

