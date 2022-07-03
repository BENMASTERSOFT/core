from .models import LoanNumber,  LoansRepaymentBase, LoanRequestSettings,LoanApplicationSettings


def generate_number(loan_code,my_id,now):
    if LoanNumber.objects.all().count()==0:
        return 0
    loan_number_selector_id=LoanNumber.objects.first()
    loan_number_selector=loan_number_selector_id.code
    
    current_time= str(now.year) + str(now.month).zfill(2)   
    loan_number=str(loan_code) + str(my_id) + str(current_time) + str(loan_number_selector).zfill(5)

    loan_number_selector_id.code=int(loan_number_selector)+1
    loan_number_selector_id.save()

    return loan_number


def duration_calculator():
    pass

def Loans_Repayment_Base(member,nok_name,
                    nok_Relationship,
                    nok_phone_no,
                    nok_address,duration,
                    interest_deduction,
                    interest_rate,
                    interest,
                    admin_charge,transaction,loan_number,loan_amount,repayment,balance,amount_paid,start_date,stop_date,processed_by,status,tdate,schedule_status):
   
    LoansRepaymentBase(member=member,
                        nok_name=nok_name,
                        nok_Relationship=nok_Relationship,
                        nok_phone_no=nok_phone_no,
                        nok_address=nok_address,
                        duration=duration,
                        interest_deduction=interest_deduction,
                        interest_rate=interest_rate,
                        interest=interest,
                        admin_charge=admin_charge,
                        transaction=transaction,
                        loan_number=loan_number,
                        loan_amount=loan_amount,
                        repayment=repayment,
                        balance=balance,
                        amount_paid=amount_paid,
                        start_date=start_date,
                        stop_date=stop_date,
                        processed_by=processed_by,
                        status=status,
                        tdate=tdate,
                        schedule_status=schedule_status).save()
    return 0



def Loans_Repayment_Base_Existing(member,
                    interest_deduction,
                    interest_rate,
                    interest,
                    admin_charge,transaction,loan_number,loan_amount,repayment,balance,amount_paid,start_date,stop_date,processed_by,status,tdate,schedule_status):
   
    LoansRepaymentBase(member=member,
                        duration=duration,
                        interest_deduction=interest_deduction,
                        interest_rate=interest_rate,
                        interest=interest,
                        admin_charge=admin_charge,
                        transaction=transaction,
                        loan_number=loan_number,
                        loan_amount=loan_amount,
                        repayment=repayment,
                        balance=balance,
                        amount_paid=amount_paid,
                        start_date=start_date,
                        stop_date=stop_date,
                        processed_by=processed_by,
                        status=status,
                        tdate=tdate,
                        schedule_status=schedule_status).save()
    return 0
# def Loan_Disbursed_Posting(member,transaction,loan_number,amount_scheduled,repayment,amount_paid,balance,duration,interest_rate,interest_deduction,start_date,stop_date,processed_by,loan_merge_status,status,schedule_status,tdate):

#     LoansDisbursed(
#                 member=member,       
#                 transaction=transaction,
#                 loan_number=loan_number,
#                 loan_amount=amount_scheduled,
#                 repayment=repayment,
#                 amount_paid=amount_paid,
#                 balance=balance,
#                 duration=duration,
#                 interest_rate=interest_rate,
#                 interest_deduction=interest_deduction,
#                 start_date=start_date,
#                 stop_date=stop_date,
#                 processed_by=processed_by,
#                 loan_merge_status=loan_merge_status,
#                 status=status,
#                 schedule_status=schedule_status,
#                 tdate=tdate).save()
#     return 0


def Loan_Request_Posting(applicant,description,value,category,status,waver):
    loan_setting=LoanRequestSettings(applicant=applicant,description=description,value=value,category=category,status=status,waver=waver)
    loan_setting.save()
    return 0


def Loan_Application_Posting(applicant,description,value,category,status,tag,waver):
    loan_setting=LoanApplicationSettings(applicant=applicant,description=description,value=value,category=category,status=status,tag=tag,waver=waver)
    loan_setting.save()
    return 0