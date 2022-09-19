from .models import StandingOrderAccounts
from django.db.models import Count, Sum
import re

def get_standing_orders(applicant):
    savings=StandingOrderAccounts.objects.filter(transaction__member_id=applicant)
    return savings


def get_standing_orders_sum(applicant):
    savings_sum=StandingOrderAccounts.objects.filter(transaction__member_id=applicant).exclude(transaction__transaction__code='102').aggregate(total_amount=Sum('amount'))
    total_savings=savings_sum['total_amount']
    return total_savings


def get_compulsory_savings(compulsory_savings,applicant):
    savings_sum=StandingOrderAccounts.objects.filter(transaction__transaction=compulsory_savings,transaction__member_id=applicant).aggregate(total_amount=Sum('amount'))
    total_savings=savings_sum['total_amount']
    return total_savings



def get_loan_based_savings(compulsory_savings,applicant):
    savings_sum=StandingOrderAccounts.objects.filter(transaction__transaction=compulsory_savings,transaction__member_id=applicant).aggregate(total_amount=Sum('amount'))
    total_savings=savings_sum['total_amount']
    return total_savings



def titlecase(s):
    return re.sub(
        r"[A-Za-z]+('[A-Za-z]+)?",
        lambda word: word.group(0).capitalize(),
        s)
