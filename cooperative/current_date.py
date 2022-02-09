from datetime import datetime
from datetime import date
import datetime
from django.utils.dateparse import parse_date
from dateutil.relativedelta import relativedelta
from .personnal_ledger_diplay import Display_PersonalLedger


def get_current_date(now):
    tday=now.day
    tmonth=now.month
    tyear=now.year
    
    tdate=date(tyear,tmonth,tday)

    return tdate