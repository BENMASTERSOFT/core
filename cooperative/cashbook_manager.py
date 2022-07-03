
from .models import CashBook_Shop,CustomUser, CashBook_Main


def shop_cashbook_posting(particulars,debit,credit,balance,ref_no,status,tdate,processed_by,source):
   
    CashBook_Shop(particulars=particulars,debit=debit,credit=credit,balance=balance,ref_no=ref_no,status=status,tdate=tdate,processed_by=processed_by,source=source).save()
    return 0

# shop_cashbook_balance
# shop_cashbook_posting
# shop_cashbook_posting(particulars,debeit,crdit,balance,ref_no,status,tdate)
# shop_cashbook_posting(item[0],item[1],item[2],balance,item[3] + ' - ' + str(item[4]),cashbook_status,tdate)

def shop_cashbook_balance():
    balance=0
    if CashBook_Shop.objects.all().exists():
        balance_obj=CashBook_Shop.objects.all().last()
        balance=balance_obj.balance

    return balance

def main_cashbook_posting(particulars,debit,credit,balance,ref_no,status,tdate,processed_by,source):
   
    CashBook_Main(particulars=particulars,debit=debit,credit=credit,balance=balance,ref_no=ref_no,status=status,tdate=tdate,processed_by=processed_by,source=source).save()
    return 0

# shop_cashbook_balance
# shop_cashbook_posting
# shop_cashbook_posting(particulars,debeit,crdit,balance,ref_no,status,tdate)
# shop_cashbook_posting(item[0],item[1],item[2],balance,item[3] + ' - ' + str(item[4]),cashbook_status,tdate)

def main_cashbook_balance():
    balance=0
    if CashBook_Main.objects.all().exists():
        balance_obj=CashBook_Main.objects.all().last()
        balance=balance_obj.balance

    return balance



    # cash_book_balance=main_cashbook_balance()
    
    # particulars='Loan Application form sales'
    # debit=admin_charge
    # credit=0
    # balance=float(cash_book_balance)-float(debit)
    # ref_no=get_ticket()
    # status='ACTIVE'
    # tdate=get_current_date(now)
    # processed_by=CustomUser.objects.get(id=request.user.id)
    # source='FORM SALES'
    # main_cashbook_posting(particulars,debit,credit,balance,ref_no,status,tdate,processed_by,source)
    