from .models import PersonalLedger


def post_to_ledger(member,transaction,account_number,particulars,debit,credit,balance,transaction_period,status,tdate,processed_by):
    record=PersonalLedger(member=member,
                        transaction=transaction,
                        account_number=account_number,
                        particulars=particulars,
                        debit=debit,
                        credit=credit,
                        balance=balance,
                        transaction_period=transaction_period,
                        status=status,
                        tdate=tdate,
                        processed_by=processed_by
                        )
    record.save()
    return 0


# def get_ledger_balance(member,transaction,account_number):
def get_ledger_balance(account_number):
    # ledger=PersonalLedger.objects.filter(member=member,transaction=transaction,account_number=account_number).order_by('id').last()
    if PersonalLedger.objects.filter(account_number=account_number).exists():

        ledger=PersonalLedger.objects.filter(account_number=account_number).order_by('id').last()
        return ledger.balance
    else:
        return 0


def get_ledger_last_transaction_period(account_number):
    # ledger=PersonalLedger.objects.filter(member=member,transaction=transaction,account_number=account_number).order_by('id').last()
    if PersonalLedger.objects.filter(account_number=account_number).exists():

        ledger=PersonalLedger.objects.filter(account_number=account_number).order_by('id').last()
        return ledger.transaction_period
    else:
        return 0

