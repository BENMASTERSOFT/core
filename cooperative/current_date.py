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

def get_print_date(now):
    tday=now.day
    tmonth=now.month
    tyear=now.year
    
    tdate=date(tyear,tmonth,tday)

    d = tdate.strftime("%d %b, %Y")
    return d

def numOfDays(date1, date2):
    return (date2-date1).days
     


        # date_format = '%Y-%m-%d'
        # dtObj = datetime.strptime(current_date, date_format)

        # year=int(dtObj.year)
        # month=int(dtObj.month)
        # day=int(dtObj.day)