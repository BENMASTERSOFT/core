from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, HttpResponseRedirect
from cooperative.models import *
from django.contrib import messages
from django.urls import reverse
from cooperative.forms import *
from django.db.models import Q
import csv, io
from tablib import Dataset
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import permission_required
from django.db.models import Value
from django.db.models.functions import Concat
from cooperative.resources import StockListResource
from .current_date import get_current_date
from datetime import datetime
from datetime import date
import datetime
from django.utils.dateparse import parse_date
from dateutil.relativedelta import relativedelta
now = datetime.datetime.now()
####################################################################
###################### HOME PAGE ###################################
####################################################################


def admin_home(request):
    # print(request.user__executives_tasks_model.membership_approval)
   
    current_user=[]
    if not request.user.user_type == '1':
        current_user=Executives_Tasks_Model.objects.get(user=request.user.id)
   
    members=[]
    transactions = TransactionTypes.objects.all().count()
    if MembershipStatus.objects.all().exists():
        members = Members.objects.filter(status=MembershipStatus.objects.get(title="ACTIVE")).count()
  
    record=DataCaptureManager.objects.first()
    title="System Admin"
    # staff=Staff.objects.get(admin=request.user)
 
    context={
    'current_user':current_user,
    "members":members,
    "transactions":transactions,
    'title':title,
    'record':record,
    }
    return render(request, "master_templates/dashboard.html",context)


def system_reset(request):
    status=ReceiptStatus.objects.get(title='UNUSED')
    Receipts.objects.all().update(status=status)
    

    record=CustomUser.objects.filter(user_type=5)
    record.delete()
    record=MemberShipRequest.objects.all()
    record.delete()

    record=NorminalRoll.objects.all()
    record.delete()
   
    MembersIdManager.objects.filter().update(member_id=1)
    AutoReceipt.objects.filter().update(receipt=1)

    return HttpResponseRedirect(reverse('admin_home'))



def User_Task_Manager_Update_Membership(request,pk):
    record=Staff.objects.get(id=pk)
    if record.membership:
        record.membership=False
    else:
        record.membership=True
    record.save()
    return HttpResponseRedirect(reverse('User_Task_Manager_Update',args=(pk,)))


def User_Task_Manager_Update_loan(request,pk):
    record=Staff.objects.get(id=pk)
    if record.loan:
        record.loan=False
    else:
        record.loan=True
    record.save()
    return HttpResponseRedirect(reverse('User_Task_Manager_Update',args=(pk,)))

def User_Task_Manager_Update_transaction_adjustment(request,pk):
    record=Staff.objects.get(id=pk)
    if record.transaction_adjustment:
        record.transaction_adjustment=False
    else:
        record.transaction_adjustment=True
    record.save()
    return HttpResponseRedirect(reverse('User_Task_Manager_Update',args=(pk,)))


def User_Task_Manager_Update_cash_withdrawal(request,pk):
    record=Staff.objects.get(id=pk)
    if record.cash_withdrawal:
        record.cash_withdrawal=False
    else:
        record.cash_withdrawal=True
    record.save()
    return HttpResponseRedirect(reverse('User_Task_Manager_Update',args=(pk,)))

def User_Task_Manager_Update_termination(request,pk):
    record=Staff.objects.get(id=pk)
    if record.termination:
        record.termination=False
    else:
        record.termination=True
    record.save()
    return HttpResponseRedirect(reverse('User_Task_Manager_Update',args=(pk,)))


def User_Task_Manager_Update_shares(request,pk):
    record=Staff.objects.get(id=pk)
    if record.shares:
        record.shares=False
    else:
        record.shares=True
    record.save()
    return HttpResponseRedirect(reverse('User_Task_Manager_Update',args=(pk,)))

def User_Task_Manager_Update_credit_sales(request,pk):
    record=Staff.objects.get(id=pk)
    if record.credit_sales:
        record.credit_sales=False
    else:
        record.credit_sales=True
    record.save()
    return HttpResponseRedirect(reverse('User_Task_Manager_Update',args=(pk,)))

def User_Task_Manager_Update_stock_update(request,pk):
    record=Staff.objects.get(id=pk)
    if record.stock_update:
        record.stock_update=False
    else:
        record.stock_update=True
    record.save()
    return HttpResponseRedirect(reverse('User_Task_Manager_Update',args=(pk,)))


def User_Task_Manager_Update_exclusiveness(request,pk):
    record=Staff.objects.get(id=pk)
    if record.exclusiveness:
        record.exclusiveness=False
    else:
        record.exclusiveness=True
    record.save()
    return HttpResponseRedirect(reverse('User_Task_Manager_Update',args=(pk,)))


def User_Task_Manager_Update_system_admin(request,pk):
    record=Staff.objects.get(id=pk)
    if record.system_admin:
        record.system_admin=False
    else:
        record.system_admin=True
    record.save()
    return HttpResponseRedirect(reverse('User_Task_Manager_Update',args=(pk,)))


def User_Task_Manager_Update_desk_office(request,pk):
    record=Staff.objects.get(id=pk)
    if record.desk_office:
        record.desk_office=False
    else:
        record.desk_office=True
    record.save()
    return HttpResponseRedirect(reverse('User_Task_Manager_Update',args=(pk,)))


def General_Tasks_Manager(request):
  
    current_user=[]
    if not request.user.user_type == '1':
        current_user=Executives_Tasks_Model.objects.get(user=request.user.id)

    context={
    'current_user':current_user,

    }
    return render(request,'master_templates/General_Tasks_Manager.html',context)


def Executive_Users(request):
    current_user=[]
    if not request.user.user_type == '1':
        current_user=Executives_Tasks_Model.objects.get(user=request.user.id)

    records=CustomUser.objects.filter(user_type='2')
 
    context={
    'current_user':current_user,
    'records':records,
    }
    return render(request,'master_templates/Executive_Users.html',context)


def Executive_Tasks(request,pk):
    current_user=[]
    if not request.user.user_type == '1':
        current_user=Executives_Tasks_Model.objects.get(user=request.user.id)

    form=Executive_Tasks_Model_form(request.POST or None)

    record=[]
    if Executives_Tasks_Model.objects.filter(user_id=pk).exists():
        record=Executives_Tasks_Model.objects.get(user_id=pk)
  
    if request.method == 'POST':
        user_manager=request.POST.get('user_manager')
        commodity_loan_products=request.POST.get('commodity_loan_products')
        loan_criteria_settings=request.POST.get('loan_criteria_settings')
        service_charges=request.POST.get('service_charges')
        utilities=request.POST.get('utilities')
        invoice_management=request.POST.get('invoice_management')
        components=request.POST.get('components')   
        data_imports=request.POST.get('data_imports')        
        membership_approval=request.POST.get('membership_approval')
        loan_request_approval=request.POST.get('loan_request_approval')
        loan_application_certification=request.POST.get('loan_application_certification')
        loan_application_approval=request.POST.get('loan_application_approval')
        membership_exclusiveness_approval=request.POST.get('membership_exclusiveness_approval')
        commodity_loan_approval=request.POST.get('commodity_loan_approval')
        share_purchase_approval=request.POST.get('share_purchase_approval')
        commodity_loan_certification=request.POST.get('commodity_loan_certification')
        cash_withdrawal_certification=request.POST.get('cash_withdrawal_certification')
        cash_withdrawal_approval=request.POST.get('cash_withdrawal_approval')
        system_admin=request.POST.get('system_admin')
        
       
        if record:
            record.user_manager=user_manager
            record.commodity_loan_products=commodity_loan_products
            record.loan_criteria_settings=loan_criteria_settings
            record.service_charges=service_charges
            record.utilities=utilities
            record.invoice_management=invoice_management
            record.components=components
            record.data_imports=data_imports
            record.membership_approval=membership_approval
            record.loan_request_approval=loan_request_approval
            record.loan_application_certification=loan_application_certification
            record.loan_application_approval=loan_application_approval
            record.membership_exclusiveness_approval=membership_exclusiveness_approval
            record.commodity_loan_approval=commodity_loan_approval
            record.share_purchase_approval=share_purchase_approval
            record.commodity_loan_certification=commodity_loan_certification
            record.cash_withdrawal_certification=cash_withdrawal_certification
            record.cash_withdrawal_approval=cash_withdrawal_approval
            record.system_admin=system_admin
           
            record.save()
        else:
            user=CustomUser.objects.get(id=pk)
            record=Executives_Tasks_Model(user=user,
                            user_manager=0,
                            commodity_loan_products=0,
                            loan_criteria_settings=0,
                            service_charges=0,
                            utilities=0,
                            invoice_management=0,
                            components=0,
                            data_imports=0,
                            membership_approval=0,
                            loan_request_approval=0,
                            loan_application_certification=0,
                            loan_application_approval=0,
                            membership_exclusiveness_approval=0,
                            commodity_loan_approval=0,
                            share_purchase_approval=0,
                            commodity_loan_certification=0,
                            cash_withdrawal_certification=0,
                            cash_withdrawal_approval=0,
                            system_admin=0,
                            
                            )
            record.save()
     
            if user_manager:
                record.user_manager=user_manager
            else:
                record.user_manager=0
            

            if commodity_loan_products:
                record.commodity_loan_products=commodity_loan_products
            else:
                record.commodity_loan_products=0
            
            if loan_criteria_settings:
                record.loan_criteria_settings=loan_criteria_settings
            else:
                record.loan_criteria_settings=0

            if service_charges:
                record.service_charges=service_charges
            else:
                record.service_charges=0
            

            if utilities:
                record.utilities=utilities
            else:
                record.utilities=0

            if invoice_management:
                record.invoice_management=invoice_management
            else:
                record.invoice_management=0
            
            if components:
                record.components=components
            else:
                record.components=0


            if data_imports:
                record.data_imports=data_imports
            else:
                record.data_imports=0


            if membership_approval:
                record.membership_approval=membership_approval
            else:
                record.membership_approval=0
            

            if loan_request_approval:
                record.loan_request_approval=loan_request_approval
            else:
                record.loan_request_approval=0

            if loan_application_certification:
                record.loan_application_certification=loan_application_certification
            else:
                record.loan_application_certification=0
            

            if loan_application_approval:
                record.loan_application_approval=loan_application_approval
            else:
                record.loan_application_approval=0

            if membership_exclusiveness_approval:
                record.membership_exclusiveness_approval=membership_exclusiveness_approval
            else:
                record.membership_exclusiveness_approval=0
            

            if commodity_loan_approval:
                record.commodity_loan_approval=commodity_loan_approval
            else:
                record.commodity_loan_approval=0            
            

            if share_purchase_approval:
                record.share_purchase_approval=share_purchase_approval
            else:
                record.share_purchase_approval=0

            if commodity_loan_certification:
                record.commodity_loan_certification=commodity_loan_certification
            else:
                record.commodity_loan_certification=0

            
            if cash_withdrawal_certification:
                record.cash_withdrawal_certification=cash_withdrawal_certification
            else:
                record.cash_withdrawal_certification=0
            
            if cash_withdrawal_approval:
                record.cash_withdrawal_approval=cash_withdrawal_approval
            else:
                record.cash_withdrawal_approval=0

            if system_admin:
                record.system_admin=system_admin
            else:
                record.system_admin=0


            record.save()
        return HttpResponseRedirect(reverse('Executive_Tasks',args=(pk,)))
    if record:

        form.fields['user_manager'].initial=record.user_manager
        form.fields['commodity_loan_products'].initial=record.commodity_loan_products
        form.fields['loan_criteria_settings'].initial=record.loan_criteria_settings
        form.fields['service_charges'].initial=record.service_charges
        form.fields['utilities'].initial=record.utilities
        form.fields['invoice_management'].initial=record.invoice_management
        form.fields['components'].initial=record.components
        form.fields['data_imports'].initial=record.data_imports
        form.fields['membership_approval'].initial=record.membership_approval
        form.fields['loan_request_approval'].initial=record.loan_request_approval
        form.fields['loan_application_certification'].initial=record.loan_application_certification
        form.fields['loan_application_approval'].initial=record.loan_application_approval
        form.fields['membership_exclusiveness_approval'].initial=record.membership_exclusiveness_approval
        form.fields['commodity_loan_approval'].initial=record.commodity_loan_approval
        form.fields['share_purchase_approval'].initial=record.share_purchase_approval
        form.fields['commodity_loan_certification'].initial=record.commodity_loan_certification
        form.fields['cash_withdrawal_certification'].initial=record.cash_withdrawal_certification
        form.fields['cash_withdrawal_approval'].initial=record.cash_withdrawal_approval
        form.fields['system_admin'].initial=record.system_admin
      
    context={
    'current_user':current_user,
    'form':form,
    'record':record,
    }
    return render(request,'master_templates/Executive_Tasks.html',context)


def Desk_Office_Users(request):
    current_user=[]
    if not request.user.user_type == '1':
        current_user=Executives_Tasks_Model.objects.get(user=request.user.id)

    records=CustomUser.objects.filter(user_type='3')
 
    context={
    'current_user':current_user,
    'records':records,
    }
    return render(request,'master_templates/Desk_Office_Users.html',context)


def Desk_Office_Tasks(request,pk):
    current_user=[]
    if not request.user.user_type == '1':
        current_user=Executives_Tasks_Model.objects.get(user=request.user.id)

    form=Desk_Office_Tasks_form(request.POST or None)

    record=[]
    if Desk_Office_Tasks_Model.objects.filter(user_id=pk).exists():
        record=Desk_Office_Tasks_Model.objects.get(user_id=pk)
    # else:
    #     messages.error(request,'Invalid Transaction, Consult the Administrator')
    #     return HttpResponseRedirect(reverse('Desk_Office_Tasks',args=(pk,)))

    if request.method == 'POST':
        general_report=request.POST.get('general_report')
        day_end_transaction=request.POST.get('day_end_transaction')
        bank_accounts=request.POST.get('bank_accounts')
        monthly_deductions=request.POST.get('monthly_deductions')
        external_fascilities=request.POST.get('external_fascilities')
        loan_management=request.POST.get('loan_management')
        exclusiveness_request=request.POST.get('exclusiveness_request')
        salary_update=request.POST.get('salary_update')
        next_of_kin=request.POST.get('next_of_kin')
        share_management=request.POST.get('share_management')
        cash_withdrawal=request.POST.get('cash_withdrawal')
        cash_deposit=request.POST.get('cash_deposit')
        transaction_adjustment=request.POST.get('transaction_adjustment')
        standing_order_placement=request.POST.get('standing_order_placement')
        membership_registration=request.POST.get('membership_registration')
        data_capture=request.POST.get('data_capture')
        personnel_info=request.POST.get('personnel_info')
        termination=request.POST.get('termination')
        shop_credit_sales=request.POST.get('shop_credit_sales')
        salary_update_approval=request.POST.get('salary_update_approval')
        external_fascilities_approval=request.POST.get('external_fascilities_approval')
        exclusiveness_approval=request.POST.get('exclusiveness_approval')
        essential_commodity=request.POST.get('essential_commodity')
        share_update_approval=request.POST.get('share_update_approval')
        transaction_adjustment_approval=request.POST.get('transaction_adjustment_approval')
       
        if record:
            record.general_report=general_report
            record.day_end_transaction=day_end_transaction
            record.bank_accounts=bank_accounts
            record.monthly_deductions=monthly_deductions
            record.external_fascilities=external_fascilities
            record.loan_management=loan_management
            record.exclusiveness_request=exclusiveness_request
            record.salary_update=salary_update
            record.next_of_kin=next_of_kin
            record.share_management=share_management
            record.cash_withdrawal=cash_withdrawal
            record.cash_deposit=cash_deposit
            record.transaction_adjustment=transaction_adjustment
            record.standing_order_placement=standing_order_placement
            record.membership_registration=membership_registration
            record.data_capture=data_capture
            record.personnel_info=personnel_info
            record.termination=termination
            record.shop_credit_sales=shop_credit_sales
            record.salary_update_approval=salary_update_approval
            record.external_fascilities_approval=external_fascilities_approval
            record.exclusiveness_approval=exclusiveness_approval
            record.essential_commodity=essential_commodity
            record.share_update_approval=share_update_approval
            record.transaction_adjustment_approval=transaction_adjustment_approval
            record.save()
        else:
            user=CustomUser.objects.get(id=pk)
            record=Desk_Office_Tasks_Model(user=user,
                            general_report=0,
                            day_end_transaction=0,
                            bank_accounts=0,
                            monthly_deductions=0,
                            external_fascilities=0,
                            loan_management=0,
                            exclusiveness_request=0,
                            salary_update=0,
                            next_of_kin=0,
                            share_management=0,
                            cash_withdrawal=0,
                            cash_deposit=0,
                            transaction_adjustment=0,
                            standing_order_placement=0,
                            membership_registration=0,
                            personnel_info=0,
                            data_capture=0,
                            termination=0,
                            shop_credit_sales=0,
                            salary_update_approval=0,
                            external_fascilities_approval=0,
                            exclusiveness_approval=0,
                            essential_commodity=0,
                            share_update_approval=0,
                            transaction_adjustment_approval=0,
                            )
            record.save()
     
            if general_report:
                record.general_report=general_report
            else:
                record.general_report=0

            if day_end_transaction:
                record.day_end_transaction=day_end_transaction
            else:
                record.day_end_transaction=0

            if bank_accounts:
                record.bank_accounts=bank_accounts
            else:
                record.bank_accounts=0

            if monthly_deductions:
                record.monthly_deductions=monthly_deductions
            else:
                record.monthly_deductions=0

            if external_fascilities:
                record.external_fascilities=external_fascilities
            else:
                record.external_fascilities=0

            if loan_management:
                record.loan_management=loan_management
            else:
                record.loan_management=0

            if exclusiveness_request:
                record.exclusiveness_request=exclusiveness_request
            else:
                record.exclusiveness_request=0

            if salary_update:
                record.salary_update=salary_update
            else:
                record.salary_update=0

            if next_of_kin:
                record.next_of_kin=next_of_kin
            else:
                record.next_of_kin=0

            if share_management:
                record.share_management=share_management
            else:
                record.share_management=0            


            if cash_withdrawal:
                record.cash_withdrawal=cash_withdrawal
            else:
                record.cash_withdrawal=0


            if cash_deposit:
                record.cash_deposit=cash_deposit
            else:
                record.cash_deposit=0


            if transaction_adjustment:
                record.transaction_adjustment=transaction_adjustment
            else:
                record.transaction_adjustment=0


            if standing_order_placement:
                record.standing_order_placement=standing_order_placement
            else:
                record.standing_order_placement=0


            if membership_registration:
                record.membership_registration=membership_registration
            else:
                record.membership_registration=0


            if personnel_info:
                record.personnel_info=personnel_info
            else:
                record.personnel_info=0


            if data_capture:
                record.data_capture=data_capture
            else:
                record.data_capture=0

            if termination:
                record.termination=termination
            else:
                record.termination=0


            if shop_credit_sales:
                record.shop_credit_sales=shop_credit_sales
            else:
                record.shop_credit_sales=0

            if salary_update_approval:
                record.salary_update_approval=salary_update_approval
            else:
                record.salary_update_approval=0

            if external_fascilities_approval:
                record.external_fascilities_approval=external_fascilities_approval
            else:
                record.external_fascilities_approval=0

            if exclusiveness_approval:
                record.exclusiveness_approval=exclusiveness_approval
            else:
                record.exclusiveness_approval=0
            
            if essential_commodity:
                record.essential_commodity=essential_commodity
            else:
                record.essential_commodity=0
 
            if share_update_approval:
                record.share_update_approval=share_update_approval
            else:
                record.share_update_approval=0

            if transaction_adjustment_approval:
                record.transaction_adjustment_approval=transaction_adjustment_approval
            else:
                record.transaction_adjustment_approval=0



            record.save()
        return HttpResponseRedirect(reverse('Desk_Office_Tasks',args=(pk,)))
    if record:

        form.fields['general_report'].initial=record.general_report
        form.fields['day_end_transaction'].initial=record.day_end_transaction
        form.fields['bank_accounts'].initial=record.bank_accounts
        form.fields['monthly_deductions'].initial=record.monthly_deductions
        form.fields['external_fascilities'].initial=record.external_fascilities
        form.fields['loan_management'].initial=record.loan_management
        form.fields['exclusiveness_request'].initial=record.exclusiveness_request
        form.fields['salary_update'].initial=record.salary_update
        form.fields['next_of_kin'].initial=record.next_of_kin
        form.fields['share_management'].initial=record.share_management
        form.fields['cash_withdrawal'].initial=record.cash_withdrawal
        form.fields['cash_deposit'].initial=record.cash_deposit
        form.fields['standing_order_placement'].initial=record.standing_order_placement
        form.fields['transaction_adjustment'].initial=record.transaction_adjustment
        form.fields['membership_registration'].initial=record.membership_registration
        form.fields['personnel_info'].initial=record.personnel_info
        form.fields['data_capture'].initial=record.data_capture
        form.fields['termination'].initial=record.termination
        form.fields['shop_credit_sales'].initial=record.shop_credit_sales
        form.fields['salary_update_approval'].initial=record.salary_update_approval
        form.fields['external_fascilities_approval'].initial=record.external_fascilities_approval
        form.fields['exclusiveness_approval'].initial=record.exclusiveness_approval
        form.fields['essential_commodity'].initial=record.essential_commodity
        form.fields['share_update_approval'].initial=record.share_update_approval
        form.fields['transaction_adjustment_approval'].initial=record.transaction_adjustment_approval
    context={
    'current_user':current_user,
    'form':form,
    'record':record,
    }
    return render(request,'master_templates/Desk_Office_Tasks.html',context)


def Shop_Users(request):
    current_user=[]
    if not request.user.user_type == '1':
        current_user=Executives_Tasks_Model.objects.get(user=request.user.id)

    records=CustomUser.objects.filter(user_type='4')
 
    context={
    'current_user':current_user,
    'records':records,
    }
    return render(request,'master_templates/Shop_Users.html',context)





def Shop_Tasks(request,pk):
    current_user=[]
    if not request.user.user_type == '1':
        current_user=Executives_Tasks_Model.objects.get(user=request.user.id)

    form=Shop_Tasks_form(request.POST or None)

    record=[]
    if Shop_Tasks_Models.objects.filter(user_id=pk).exists():
        record=Shop_Tasks_Models.objects.filter(user_id=pk).first()

    if request.method == 'POST':
        form = Shop_Tasks_form(request.POST)
        
        sales=request.POST.get('sales')
        debt_recovery=request.POST.get('debt_recovery')
        purchases=request.POST.get('purchases')
        item_write_off=request.POST.get('item_write_off')
        item_write_off=request.POST.get('item_write_off')
        personal_ledger=request.POST.get('personal_ledger')
        general_report=request.POST.get('general_report')
        day_end_transaction=request.POST.get('day_end_transaction')
        monthly_deduction=request.POST.get('monthly_deduction')
        product_manager=request.POST.get('product_manager')
        suppliers_manager=request.POST.get('suppliers_manager')
     
        # return HttpResponseRedirect(reverse('Shop_Tasks',args=(pk,)))
        if record:
            # return HttpResponse("Ok")
            record.sales=sales
            record.debt_recovery=debt_recovery
            record.purchases=purchases
            record.item_write_off=item_write_off
            record.personal_ledger=personal_ledger
            record.general_report=general_report
            record.day_end_transaction=day_end_transaction
            record.monthly_deduction=monthly_deduction
            record.product_manager=product_manager
            record.suppliers_manager=suppliers_manager
            record.save()
        else:
            user=CustomUser.objects.get(id=pk)
            record=Shop_Tasks_Models(user=user,
                            sales=0,
                            debt_recovery=0,
                            purchases=0,
                            item_write_off=0,
                            personal_ledger=0,
                            general_report=0,
                            day_end_transaction=0,
                            monthly_deduction=0,
                            product_manager=0,
                            suppliers_manager=0,)
            record.save()
     
            if sales:
                record.sales=sales
            else:
                record.sales=0

            if debt_recovery:
                record.debt_recovery=debt_recovery
            else:
                record.debt_recovery=0
            if purchases:
                record.purchases=purchases
            else:
                record.purchases=0
            if item_write_off:
                record.item_write_off=item_write_off
            else:
                record.item_write_off=0
            if personal_ledger:
                record.personal_ledger=personal_ledger
            else:
                record.personal_ledger=0
            if general_report:
                record.general_report=general_report
            else:
                record.general_report=0
            if day_end_transaction:
                record.day_end_transaction=day_end_transaction
            else:
                record.day_end_transaction=0
            if monthly_deduction:
                record.monthly_deduction=monthly_deduction
            else:
                record.monthly_deduction=0
            if product_manager:
                record.product_manager=product_manager
            else:
                record.product_manager=0
            if suppliers_manager:
                record.suppliers_manager=suppliers_manager
            else:
                record.suppliers_manager=0
            record.save()
        return HttpResponseRedirect(reverse('Shop_Tasks',args=(pk,)))
    if record:

        form.fields['sales'].initial=record.sales
        form.fields['debt_recovery'].initial=record.debt_recovery
        form.fields['purchases'].initial=record.purchases
        form.fields['item_write_off'].initial=record.item_write_off
        form.fields['personal_ledger'].initial=record.personal_ledger
        form.fields['general_report'].initial=record.general_report
        form.fields['day_end_transaction'].initial=record.day_end_transaction
        form.fields['monthly_deduction'].initial=record.monthly_deduction
        form.fields['product_manager'].initial=record.product_manager
        form.fields['suppliers_manager'].initial=record.suppliers_manager
    context={
    'current_user':current_user,
    'form':form,
    'record':record,
    }
    return render(request,'master_templates/Shop_Tasks.html',context)





####################################################################
###################### VALIDATION ###################################
####################################################################


@csrf_exempt
def check_email_exist(request):
    email=request.POST.get("email")
    user_obj=CustomUser.objects.filter(email=email).exists()
    if user_obj:
        return HttpResponse(True)
    else:
        return  HttpResponse(False)


@csrf_exempt
def check_username_exist(request):
    username=request.POST.get("username")
    user_obj=CustomUser.objects.filter(username=username).exists()
    if user_obj:
        return HttpResponse(True)
    else:
        return  HttpResponse(False)


@csrf_exempt
def check_phone_no_exist(request):
    phone_no=request.POST.get("phone_no")
    user_obj=Members.objects.filter(phone_number=phone_no).exists()
    if user_obj:
        return HttpResponse(True)
    else:
        return  HttpResponse(False)



####################################################################
######################BASIC  PAGE ###################################
####################################################################
def basic_form(request):
	return render(request, 'master_templates/basics/basic_form1.html')


def basic_table(request):
	return render(request, 'master_templates/basics/basic_tables.html')

def datatable_table(request):
	return render(request, 'master_templates/basics/datatable.html')



####################################################################
###################### IMPORTS SECTION##############################
####################################################################
@permission_required('admin.can_add_log_entry')
def Termination_Sources_upload(request):
    current_user=[]
    if not request.user.user_type == '1':
        current_user=Executives_Tasks_Model.objects.get(user=request.user.id)

    template = "master_templates/file_upload.html"
    
    
    prompt = {
        'order': "Upload Termination Types, Order of the CSV should be Code, Title"
    }
    
    if request.method == "GET":
        return render(request, template, prompt)
    
    csv_file = request.FILES['file']
    
    if not csv_file.name.endswith('.csv'):
        messages.error(request, "This id not a csv file")
        
    data_set = csv_file.read().decode('UTF-8')
    io_string = io.StringIO(data_set)
    next(io_string)
    
    for column in csv.reader(io_string, delimiter=',',  quotechar='|', quoting =csv.QUOTE_NONE):
        _, created = Termination_Types.objects.update_or_create(
            title=column[1],    
        )
        
    context = {'current_user':current_user,}
    return render(request, template, context)



@permission_required('admin.can_add_log_entry')
def MonthlyDeductionGenerationHeaders_upload(request):
    current_user=[]
    if not request.user.user_type == '1':
        current_user=Executives_Tasks_Model.objects.get(user=request.user.id)

    template = "master_templates/file_upload.html"
    
    
    prompt = {
        'order': "Upload Monthly Deduction Generation Headers Status, Order of the CSV should be Code, Title"
    }
    
    if request.method == "GET":
        return render(request, template, prompt)
    
    csv_file = request.FILES['file']
    
    if not csv_file.name.endswith('.csv'):
        messages.error(request, "This id not a csv file")
        
    data_set = csv_file.read().decode('UTF-8')
    io_string = io.StringIO(data_set)
    next(io_string)
    
    for column in csv.reader(io_string, delimiter=',',  quotechar='|', quoting =csv.QUOTE_NONE):
        _, created = MonthlyDeductionGenerationHeaders.objects.update_or_create(
            title=column[1],    
        )
        
    context = {'current_user':current_user,}
    return render(request, template, context)


@permission_required('admin.can_add_log_entry')
def YesNo_upload(request):
    current_user=[]
    if not request.user.user_type == '1':
        current_user=Executives_Tasks_Model.objects.get(user=request.user.id)

    template = "master_templates/file_upload.html"
    
    
    prompt = {
        'order': "Upload Yes/No Status, Order of the CSV should be Code, Title"
    }
    
    if request.method == "GET":
        return render(request, template, prompt)
    
    csv_file = request.FILES['file']
    
    if not csv_file.name.endswith('.csv'):
        messages.error(request, "This id not a csv file")
        
    data_set = csv_file.read().decode('UTF-8')
    io_string = io.StringIO(data_set)
    next(io_string)
    
    for column in csv.reader(io_string, delimiter=',',  quotechar='|', quoting =csv.QUOTE_NONE):
        _, created = YesNo.objects.update_or_create(
            title=column[1],    
        )
        
    context = {'current_user':current_user,}
    return render(request, template, context)


@permission_required('admin.can_add_log_entry')
def LoanMergeStatus_upload(request):
    current_user=[]
    if not request.user.user_type == '1':
        current_user=Executives_Tasks_Model.objects.get(user=request.user.id)

    template = "master_templates/file_upload.html"
    
    
    prompt = {
        'order': "Upload Loan Merge Status, Order of the CSV should be Code, Title"
    }
    
    if request.method == "GET":
        return render(request, template, prompt)
    
    csv_file = request.FILES['file']
    
    if not csv_file.name.endswith('.csv'):
        messages.error(request, "This id not a csv file")
        
    data_set = csv_file.read().decode('UTF-8')
    io_string = io.StringIO(data_set)
    next(io_string)
    
    for column in csv.reader(io_string, delimiter=',',  quotechar='|', quoting =csv.QUOTE_NONE):
        _, created = LoanMergeStatus.objects.update_or_create(
            title=column[1],    
        )
        
    context = {'current_user':current_user,}
    return render(request, template, context)



@permission_required('admin.can_add_log_entry')
def MultipleLoanStatus_upload(request):
    current_user=[]
    if not request.user.user_type == '1':
        current_user=Executives_Tasks_Model.objects.get(user=request.user.id)

    template = "master_templates/file_upload.html"
    
    
    prompt = {
        'order': "Upload Multiple Loan Status, Order of the CSV should be Code, Title"
    }
    
    if request.method == "GET":
        return render(request, template, prompt)
    
    csv_file = request.FILES['file']
    
    if not csv_file.name.endswith('.csv'):
        messages.error(request, "This id not a csv file")
        
    data_set = csv_file.read().decode('UTF-8')
    io_string = io.StringIO(data_set)
    next(io_string)
    
    for column in csv.reader(io_string, delimiter=',',  quotechar='|', quoting =csv.QUOTE_NONE):
        _, created = MultipleLoanStatus.objects.update_or_create(
            title=column[1],    
        )
        
    context = {'current_user':current_user,}
    return render(request, template, context)


@permission_required('admin.can_add_log_entry')
def WithdrawalStatus_upload(request):
    current_user=[]
    if not request.user.user_type == '1':
        current_user=Executives_Tasks_Model.objects.get(user=request.user.id)

    template = "master_templates/file_upload.html"
    
    
    prompt = {
        'order': "Upload Withdrawal Status, Order of the CSV should be Code, Title"
    }
    
    if request.method == "GET":
        return render(request, template, prompt)
    
    csv_file = request.FILES['file']
    
    if not csv_file.name.endswith('.csv'):
        messages.error(request, "This id not a csv file")
        
    data_set = csv_file.read().decode('UTF-8')
    io_string = io.StringIO(data_set)
    next(io_string)
    
    for column in csv.reader(io_string, delimiter=',',  quotechar='|', quoting =csv.QUOTE_NONE):
        _, created = WithdrawalStatus.objects.update_or_create(
            title=column[1],    
        )
        
    context = {'current_user':current_user,}
    return render(request, template, context)



@permission_required('admin.can_add_log_entry')
def Date_of_birth_status_upload(request):
    current_user=[]
    if not request.user.user_type == '1':
        current_user=Executives_Tasks_Model.objects.get(user=request.user.id)

    template = "master_templates/file_upload.html"
    
    
    prompt = {
        'order': "Upload Date of Birth Upload Status, Order of the CSV should be Code, Title"
    }
    
    if request.method == "GET":
        return render(request, template, prompt)
    
    csv_file = request.FILES['file']
    
    if not csv_file.name.endswith('.csv'):
        messages.error(request, "This id not a csv file")
        
    data_set = csv_file.read().decode('UTF-8')
    io_string = io.StringIO(data_set)
    next(io_string)
    
    for column in csv.reader(io_string, delimiter=',',  quotechar='|', quoting =csv.QUOTE_NONE):
        _, created = Date_of_birth_status.objects.update_or_create(
            title=column[1],    
        )
        
    context = {'current_user':current_user,}
    return render(request, template, context)


@permission_required('admin.can_add_log_entry')
def DateJoinedUploadStatus_upload(request):
    current_user=[]
    if not request.user.user_type == '1':
        current_user=Executives_Tasks_Model.objects.get(user=request.user.id)

    template = "master_templates/file_upload.html"
    
    
    prompt = {
        'order': "Upload Date Joined Upload Status, Order of the CSV should be Code, Title"
    }
    
    if request.method == "GET":
        return render(request, template, prompt)
    
    csv_file = request.FILES['file']
    
    if not csv_file.name.endswith('.csv'):
        messages.error(request, "This id not a csv file")
        
    data_set = csv_file.read().decode('UTF-8')
    io_string = io.StringIO(data_set)
    next(io_string)
    
    for column in csv.reader(io_string, delimiter=',',  quotechar='|', quoting =csv.QUOTE_NONE):
        _, created = DateJoinedUploadStatus.objects.update_or_create(
            title=column[1],    
        )
        
    context = {'current_user':current_user,}
    return render(request, template, context)



@permission_required('admin.can_add_log_entry')
def DateOfFirstAppointment_Status_upload(request):
    current_user=[]
    if not request.user.user_type == '1':
        current_user=Executives_Tasks_Model.objects.get(user=request.user.id)

    template = "master_templates/file_upload.html"
    
    
    prompt = {
        'order': "Upload Date of First Appoint Status, Order of the CSV should be Code, Title"
    }
    
    if request.method == "GET":
        return render(request, template, prompt)
    
    csv_file = request.FILES['file']
    
    if not csv_file.name.endswith('.csv'):
        messages.error(request, "This id not a csv file")
        
    data_set = csv_file.read().decode('UTF-8')
    io_string = io.StringIO(data_set)
    next(io_string)
    
    for column in csv.reader(io_string, delimiter=',',  quotechar='|', quoting =csv.QUOTE_NONE):
        _, created = DateOfFirstAppointment_Status.objects.update_or_create(
            title=column[1],    
        )
        
    context = {'current_user':current_user,}
    return render(request, template, context)


@permission_required('admin.can_add_log_entry')
def WelfareUploadStatus_upload(request):
    current_user=[]
    if not request.user.user_type == '1':
        current_user=Executives_Tasks_Model.objects.get(user=request.user.id)

    template = "master_templates/file_upload.html"
    
    
    prompt = {
        'order': "Upload Welfare Upload Status, Order of the CSV should be Code, Title"
    }
    
    if request.method == "GET":
        return render(request, template, prompt)
    
    csv_file = request.FILES['file']
    
    if not csv_file.name.endswith('.csv'):
        messages.error(request, "This id not a csv file")
        
    data_set = csv_file.read().decode('UTF-8')
    io_string = io.StringIO(data_set)
    next(io_string)
    
    for column in csv.reader(io_string, delimiter=',',  quotechar='|', quoting =csv.QUOTE_NONE):
        _, created = WelfareUploadStatus.objects.update_or_create(
            title=column[1],    
        )
        
    context = {'current_user':current_user,}
    return render(request, template, context)


@permission_required('admin.can_add_log_entry')
def SharesUploadStatus_upload(request):
    current_user=[]
    if not request.user.user_type == '1':
        current_user=Executives_Tasks_Model.objects.get(user=request.user.id)

    template = "master_templates/file_upload.html"
    
    
    prompt = {
        'order': "Upload Share Status, Order of the CSV should be Code, Title"
    }
    
    if request.method == "GET":
        return render(request, template, prompt)
    
    csv_file = request.FILES['file']
    
    if not csv_file.name.endswith('.csv'):
        messages.error(request, "This id not a csv file")
        
    data_set = csv_file.read().decode('UTF-8')
    io_string = io.StringIO(data_set)
    next(io_string)
    
    for column in csv.reader(io_string, delimiter=',',  quotechar='|', quoting =csv.QUOTE_NONE):
        _, created = SharesUploadStatus.objects.update_or_create(
            title=column[1],    
        )
        
    context = {'current_user':current_user,}
    return render(request, template, context)


@permission_required('admin.can_add_log_entry')
def UsersLevel_upload(request):
    current_user=[]
    if not request.user.user_type == '1':
        current_user=Executives_Tasks_Model.objects.get(user=request.user.id)

    template = "master_templates/file_upload.html"
    
    
    prompt = {
        'order': "Upload Users Level, Order of the CSV should be Code, Title"
    }
    
    if request.method == "GET":
        return render(request, template, prompt)
    
    csv_file = request.FILES['file']
    
    if not csv_file.name.endswith('.csv'):
        messages.error(request, "This id not a csv file")
        
    data_set = csv_file.read().decode('UTF-8')
    io_string = io.StringIO(data_set)
    next(io_string)
    
    for column in csv.reader(io_string, delimiter=',',  quotechar='|', quoting =csv.QUOTE_NONE):
        _, created = UsersLevel.objects.update_or_create(
            title=column[0],    
        )
        
    context = {'current_user':current_user,}
    return render(request, template, context)


@permission_required('admin.can_add_log_entry')
def SharesUnits_upload(request):
    current_user=[]
    if not request.user.user_type == '1':
        current_user=Executives_Tasks_Model.objects.get(user=request.user.id)

    template = "master_templates/file_upload.html"
    
    
    prompt = {
        'order': "Upload Shares Units, Order of the CSV should be Code, Title"
    }
    
    if request.method == "GET":
        return render(request, template, prompt)
    
    csv_file = request.FILES['file']
    
    if not csv_file.name.endswith('.csv'):
        messages.error(request, "This id not a csv file")
        
    data_set = csv_file.read().decode('UTF-8')
    io_string = io.StringIO(data_set)
    next(io_string)
    
    for column in csv.reader(io_string, delimiter=',',  quotechar='|', quoting =csv.QUOTE_NONE):
        _, created = SharesUnits.objects.update_or_create(
            unit=column[0],    
        )
        
    context = {'current_user':current_user,}
    return render(request, template, context)


@permission_required('admin.can_add_log_entry')
def LoansUploadStatus_upload(request):
    current_user=[]
    if not request.user.user_type == '1':
        current_user=Executives_Tasks_Model.objects.get(user=request.user.id)

    template = "master_templates/file_upload.html"
    
    
    prompt = {
        'order': "Upload Loan Status, Order of the CSV should be Code, Title"
    }
    
    if request.method == "GET":
        return render(request, template, prompt)
    
    csv_file = request.FILES['file']
    
    if not csv_file.name.endswith('.csv'):
        messages.error(request, "This id not a csv file")
        
    data_set = csv_file.read().decode('UTF-8')
    io_string = io.StringIO(data_set)
    next(io_string)
    
    for column in csv.reader(io_string, delimiter=',',  quotechar='|', quoting =csv.QUOTE_NONE):
        _, created = LoansUploadStatus.objects.update_or_create(
            title=column[1],    
        )
        
    context = {'current_user':current_user,}
    return render(request, template, context)


@permission_required('admin.can_add_log_entry')
def LoanCategory_upload(request):
    current_user=[]
    if not request.user.user_type == '1':
        current_user=Executives_Tasks_Model.objects.get(user=request.user.id)

    template = "master_templates/file_upload.html"
    
    
    prompt = {
        'order': "Upload Loan Category, Order of the CSV should be Code, Title"
    }
    
    if request.method == "GET":
        return render(request, template, prompt)
    
    csv_file = request.FILES['file']
    
    if not csv_file.name.endswith('.csv'):
        messages.error(request, "This id not a csv file")
        
    data_set = csv_file.read().decode('UTF-8')
    io_string = io.StringIO(data_set)
    next(io_string)
    
    for column in csv.reader(io_string, delimiter=',',  quotechar='|', quoting =csv.QUOTE_NONE):
        _, created = LoanCategory.objects.update_or_create(
            title=column[1],    
        )
        
    context = {'current_user':current_user,}
    return render(request, template, context)


@permission_required('admin.can_add_log_entry')
def SavingsUploadStatus_upload(request):
    current_user=[]
    if not request.user.user_type == '1':
        current_user=Executives_Tasks_Model.objects.get(user=request.user.id)

    template = "master_templates/file_upload.html"
    
    
    prompt = {
        'order': "Upload Savings Status, Order of the CSV should be Code, Title"
    }
    
    if request.method == "GET":
        return render(request, template, prompt)
    
    csv_file = request.FILES['file']
    
    if not csv_file.name.endswith('.csv'):
        messages.error(request, "This id not a csv file")
        
    data_set = csv_file.read().decode('UTF-8')
    io_string = io.StringIO(data_set)
    next(io_string)
    
    for column in csv.reader(io_string, delimiter=',',  quotechar='|', quoting =csv.QUOTE_NONE):
        _, created = SavingsUploadStatus.objects.update_or_create(
            title=column[1],    
        )
        
    context = {'current_user':current_user,}
    return render(request, template, context)


@permission_required('admin.can_add_log_entry')
def LoanScheduleStatus_upload(request):
    current_user=[]
    if not request.user.user_type == '1':
        current_user=Executives_Tasks_Model.objects.get(user=request.user.id)

    template = "master_templates/file_upload.html"
    
    
    prompt = {
        'order': "Order of the CSV should be Code, Title"
    }
    
    if request.method == "GET":
        return render(request, template, prompt)
    
    csv_file = request.FILES['file']
    
    if not csv_file.name.endswith('.csv'):
        messages.error(request, "This id not a csv file")
        
    data_set = csv_file.read().decode('UTF-8')
    io_string = io.StringIO(data_set)
    next(io_string)
    
    for column in csv.reader(io_string, delimiter=',',  quotechar='|', quoting =csv.QUOTE_NONE):
        _, created = LoanScheduleStatus.objects.update_or_create(
            title=column[1],    
        )
        
    context = {'current_user':current_user,}
    return render(request, template, context)

    

@permission_required('admin.can_add_log_entry')
def ExlusiveStatus_upload(request):
    current_user=[]
    if not request.user.user_type == '1':
        current_user=Executives_Tasks_Model.objects.get(user=request.user.id)

    template = "master_templates/file_upload.html"
    
    
    prompt = {
        'order': "Order of the CSV should be Code, Title"
    }
    
    if request.method == "GET":
        return render(request, template, prompt)
    
    csv_file = request.FILES['file']
    
    if not csv_file.name.endswith('.csv'):
        messages.error(request, "This id not a csv file")
        
    data_set = csv_file.read().decode('UTF-8')
    io_string = io.StringIO(data_set)
    next(io_string)
    
    for column in csv.reader(io_string, delimiter=',',  quotechar='|', quoting =csv.QUOTE_NONE):
        _, created = ExclusiveStatus.objects.update_or_create(
            title=column[1],    
        )
        
    context = {'current_user':current_user,}
    return render(request, template, context)



@permission_required('admin.can_add_log_entry')
def LockedStatus_upload(request):
    current_user=[]
    if not request.user.user_type == '1':
        current_user=Executives_Tasks_Model.objects.get(user=request.user.id)

    template = "master_templates/file_upload.html"
    
    
    prompt = {
        'order': "Order of the CSV should be Code, Title"
    }
    
    if request.method == "GET":
        return render(request, template, prompt)
    
    csv_file = request.FILES['file']
    
    if not csv_file.name.endswith('.csv'):
        messages.error(request, "This id not a csv file")
        
    data_set = csv_file.read().decode('UTF-8')
    io_string = io.StringIO(data_set)
    next(io_string)
    
    for column in csv.reader(io_string, delimiter=',',  quotechar='|', quoting =csv.QUOTE_NONE):
        _, created = LockedStatus.objects.update_or_create(
            title=column[1],    
        )
        
    context = {'current_user':current_user,}
    return render(request, template, context)



@permission_required('admin.can_add_log_entry')
def ReceiptTypes_upload(request):
    current_user=[]
    if not request.user.user_type == '1':
        current_user=Executives_Tasks_Model.objects.get(user=request.user.id)

    template = "master_templates/file_upload.html"
    
    
    prompt = {
        'order': "Order of the CSV should be Code, Title"
    }
    
    if request.method == "GET":
        return render(request, template, prompt)
    
    csv_file = request.FILES['file']
    
    if not csv_file.name.endswith('.csv'):
        messages.error(request, "This id not a csv file")
        
    data_set = csv_file.read().decode('UTF-8')
    io_string = io.StringIO(data_set)
    next(io_string)
    
    for column in csv.reader(io_string, delimiter=',',  quotechar='|', quoting =csv.QUOTE_NONE):
        _, created = ReceiptTypes.objects.update_or_create(
            title=column[1],    
        )
        
    context = {'current_user':current_user,}
    return render(request, template, context)


    
@permission_required('admin.can_add_log_entry')
def PaymentChannels_upload(request):
    current_user=[]
    if not request.user.user_type == '1':
        current_user=Executives_Tasks_Model.objects.get(user=request.user.id)

    template = "master_templates/file_upload.html"
    
    
    prompt = {
        'order': "Order of the CSV should be Code, Title"
    }
    
    if request.method == "GET":
        return render(request, template, prompt)
    
    csv_file = request.FILES['file']
    
    if not csv_file.name.endswith('.csv'):
        messages.error(request, "This id not a csv file")
        
    data_set = csv_file.read().decode('UTF-8')
    io_string = io.StringIO(data_set)
    next(io_string)
    
    for column in csv.reader(io_string, delimiter=',',  quotechar='|', quoting =csv.QUOTE_NONE):
        _, created = PaymentChannels.objects.update_or_create(
            title=column[1],    
        )
        
    context = {'current_user':current_user,}
    return render(request, template, context)


    
@permission_required('admin.can_add_log_entry')
def TicketStatus_upload(request):
    current_user=[]
    if not request.user.user_type == '1':
        current_user=Executives_Tasks_Model.objects.get(user=request.user.id)

    template = "master_templates/file_upload.html"
    
    
    prompt = {
        'order': "Order of the CSV should be Code, Title"
    }
    
    if request.method == "GET":
        return render(request, template, prompt)
    
    csv_file = request.FILES['file']
    
    if not csv_file.name.endswith('.csv'):
        messages.error(request, "This id not a csv file")
        
    data_set = csv_file.read().decode('UTF-8')
    io_string = io.StringIO(data_set)
    next(io_string)
    
    for column in csv.reader(io_string, delimiter=',',  quotechar='|', quoting =csv.QUOTE_NONE):
        _, created = TicketStatus.objects.update_or_create(
            title=column[1],    
        )
        
    context = {'current_user':current_user,}
    return render(request, template, context)





@permission_required('admin.can_add_log_entry')
def SalesCategory_upload(request):
    current_user=[]
    if not request.user.user_type == '1':
        current_user=Executives_Tasks_Model.objects.get(user=request.user.id)

    template = "master_templates/file_upload.html"
    
    
    prompt = {
		'order': "Order of the CSV should be Code, Title"
	}
    
    if request.method == "GET":
        return render(request, template, prompt)
    
    csv_file = request.FILES['file']
    
    if not csv_file.name.endswith('.csv'):
        messages.error(request, "This id not a csv file")
        
    data_set = csv_file.read().decode('UTF-8')
    io_string = io.StringIO(data_set)
    next(io_string)
	
    for column in csv.reader(io_string, delimiter=',',  quotechar='|', quoting =csv.QUOTE_NONE):
        _, created = SalesCategory.objects.update_or_create(
			title=column[1],	
		)
        
    context = {'current_user':current_user,}
    return render(request, template, context)



@permission_required('admin.can_add_log_entry')
def ProductCategory_upload(request):
    current_user=[]
    if not request.user.user_type == '1':
        current_user=Executives_Tasks_Model.objects.get(user=request.user.id)

    template = "master_templates/file_upload.html"
    
    
    prompt = {
        'order': "Order of the CSV should be Code, Title"
    }
    
    if request.method == "GET":
        return render(request, template, prompt)
    
    csv_file = request.FILES['file']
    
    if not csv_file.name.endswith('.csv'):
        messages.error(request, "This id not a csv file")
        
    data_set = csv_file.read().decode('UTF-8')
    io_string = io.StringIO(data_set)
    next(io_string)
    
    for column in csv.reader(io_string, delimiter=',',  quotechar='|', quoting =csv.QUOTE_NONE):
        _, created = ProductCategory.objects.update_or_create(
            code=column[0],    
            title=column[1],    
        )
        
    context = {'current_user':current_user,}
    return render(request, template, context)

  
@permission_required('admin.can_add_log_entry')
def Product_Write_off_Reasons_upload(request):
    current_user=[]
    if not request.user.user_type == '1':
        current_user=Executives_Tasks_Model.objects.get(user=request.user.id)

    template = "master_templates/file_upload.html"
    
    
    prompt = {
        'order': "Order of the CSV should be  Title"
    }
    
    if request.method == "GET":
        return render(request, template, prompt)
    
    csv_file = request.FILES['file']
    
    if not csv_file.name.endswith('.csv'):
        messages.error(request, "This id not a csv file")
        
    data_set = csv_file.read().decode('UTF-8')
    io_string = io.StringIO(data_set)
    next(io_string)
    
    for column in csv.reader(io_string, delimiter=',',  quotechar='|', quoting =csv.QUOTE_NONE):
        _, created = ItemWriteOffReasons.objects.update_or_create(    
            title=column[1],    
        )
        
    context = {'current_user':current_user,}
    return render(request, template, context)

  
@permission_required('admin.can_add_log_entry')
def Stock_upload(request):
    current_user=[]
    if not request.user.user_type == '1':
        current_user=Executives_Tasks_Model.objects.get(user=request.user.id)

    template = "master_templates/file_upload.html"
    
    
    prompt = {
        'order': "Order of the CSV should be Code, Title"
    }
    
    if request.method == "GET":
        return render(request, template, prompt)
    
    csv_file = request.FILES['file']
    
    if not csv_file.name.endswith('.csv'):
        messages.error(request, "This id not a csv file")
        
    data_set = csv_file.read().decode('UTF-8')
    io_string = io.StringIO(data_set)
    next(io_string)
    
    for column in csv.reader(io_string, delimiter=',',  quotechar='|', quoting =csv.QUOTE_NONE):
           _, created = Stock.objects.update_or_create(
            code=str(column[0]).zfill(5),    
            item_name=column[1],    
            category=ProductCategory.objects.get(code=column[2]),    
            quantity=0,    
            no_in_pack=column[4],    
            re_order_level=column[5],    
            unit_selling_price=column[6],   
        )
        
    context = {'current_user':current_user,}
    return render(request, template, context)



def upload_stock_roll(request):  
    current_user=[]
    if not request.user.user_type == '1':
        current_user=Executives_Tasks_Model.objects.get(user=request.user.id)

    DataCapture=DataCaptureManager.objects.first() 
    if request.method == 'POST':
    
        stock_resource = StockListResource()
        dataset = Dataset()
        new_stock_list = request.FILES['myfile']

        if not new_stock_list.name.endswith('xlsx'):
            messages.error(request,'Wrong format')
            return HttpResponseRedirect(reverse('upload_stock_roll',args=(pk,))) 

        imported_data = dataset.load(new_stock_list.read(),format='xlsx')
        for data in imported_data: 

            category=ProductCategory.objects.get(code=data[2])
            value = Stock(code=str(data[0]).zfill(5),
                    item_name=data[1],            
                    category=category,           
                    details=data[3],            
                    quantity=0,            
                    no_in_pack=data[4],          
                    re_order_level=data[5],            
                    unit_selling_price=data[6],   
             
                )
            value.save()
    context={
    'current_user':current_user,
    
    'DataCapture':DataCapture,
    }
    return render(request,'master_templates/upload_stock.html',context) 


  
  
@permission_required('admin.can_add_log_entry')
def AdminCharges_upload(request):
    current_user=[]
    if not request.user.user_type == '1':
        current_user=Executives_Tasks_Model.objects.get(user=request.user.id)

    template = "master_templates/file_upload.html"
    
    
    prompt = {
        'order': "Order of the CSV should be Code, Title"
    }
    
    if request.method == "GET":
        return render(request, template, prompt)
    
    csv_file = request.FILES['file']
    
    if not csv_file.name.endswith('.csv'):
        messages.error(request, "This id not a csv file")
        
    data_set = csv_file.read().decode('UTF-8')
    io_string = io.StringIO(data_set)
    next(io_string)
    
    for column in csv.reader(io_string, delimiter=',',  quotechar='|', quoting =csv.QUOTE_NONE):
        _, created = AdminCharges.objects.update_or_create(
            title=column[1],    
        )
        
    context = {'current_user':current_user,}
    return render(request, template, context)

    

@permission_required('admin.can_add_log_entry')
def title_upload(request):
    current_user=[]
    if not request.user.user_type == '1':
        current_user=Executives_Tasks_Model.objects.get(user=request.user.id)

    template = "master_templates/file_upload.html"
    
    
    prompt = {
        'order': "Order of the CSV should be Code, Title"
    }
    
    if request.method == "GET":
        return render(request, template, prompt)
    
    csv_file = request.FILES['file']
    
    if not csv_file.name.endswith('.csv'):
        messages.error(request, "This id not a csv file")
        
    data_set = csv_file.read().decode('UTF-8')
    io_string = io.StringIO(data_set)
    next(io_string)
    
    for column in csv.reader(io_string, delimiter=',',  quotechar='|', quoting =csv.QUOTE_NONE):
        _, created = Titles.objects.update_or_create(
            title=column[1],    
        )
        
    context = {'current_user':current_user,}
    return render(request, template, context)


@permission_required('admin.can_add_log_entry')
def states_upload(request):
    current_user=[]
    if not request.user.user_type == '1':
        current_user=Executives_Tasks_Model.objects.get(user=request.user.id)

    template = "master_templates/file_upload.html"
    
    
    prompt = {
        'order': "Order of the CSV should be Title"
    }
    
    if request.method == "GET":
        return render(request, template, prompt)
    
    csv_file = request.FILES['file']
    
    if not csv_file.name.endswith('.csv'):
        messages.error(request, "This id not a csv file")
        
    data_set = csv_file.read().decode('UTF-8')
    io_string = io.StringIO(data_set)
    next(io_string)
    
    for column in csv.reader(io_string, delimiter=',',  quotechar='|', quoting =csv.QUOTE_NONE):
        _, created = States.objects.update_or_create(
            title=column[1],    
        )
        
    context = {'current_user':current_user,}
    return render(request, template, context)



@permission_required('admin.can_add_log_entry')
def NOKRelationships_upload(request):
    current_user=[]
    if not request.user.user_type == '1':
        current_user=Executives_Tasks_Model.objects.get(user=request.user.id)

    template = "master_templates/file_upload.html"
    
    
    prompt = {
        'order': "Order of the CSV should be Title"
    }
    
    if request.method == "GET":
        return render(request, template, prompt)
    
    csv_file = request.FILES['file']
    
    if not csv_file.name.endswith('.csv'):
        messages.error(request, "This id not a csv file")
        
    data_set = csv_file.read().decode('UTF-8')
    io_string = io.StringIO(data_set)
    next(io_string)
    
    for column in csv.reader(io_string, delimiter=',',  quotechar='|', quoting =csv.QUOTE_NONE):
        _, created = NOKRelationships.objects.update_or_create(
            title=column[1],    
        )
        
    context = {'current_user':current_user,}
    return render(request, template, context)


@permission_required('admin.can_add_log_entry')
def lga_upload(request):
    current_user=[]
    if not request.user.user_type == '1':
        current_user=Executives_Tasks_Model.objects.get(user=request.user.id)

    template = "master_templates/file_upload.html"
    
    
    prompt = {
        'order': "Order of the CSV should be Title"
    }
    
    if request.method == "GET":
        return render(request, template, prompt)
    
    csv_file = request.FILES['file']
    
    if not csv_file.name.endswith('.csv'):
        messages.error(request, "This id not a csv file")
        
    data_set = csv_file.read().decode('UTF-8')
    io_string = io.StringIO(data_set)
    next(io_string)
    
    for column in csv.reader(io_string, delimiter=',',  quotechar='|', quoting =csv.QUOTE_NONE):
        _, created = Lga.objects.update_or_create(
            title=column[0], 
            state=States.objects.get(id=column[1])   
        )
        
    context = {'current_user':current_user,}
    return render(request, template, context)



@permission_required('admin.can_add_log_entry')
def SubmissionStatus_upload(request):
    current_user=[]
    if not request.user.user_type == '1':
        current_user=Executives_Tasks_Model.objects.get(user=request.user.id)

    template = "master_templates/file_upload.html"
    
    
    prompt = {
        'order': "Order of the CSV should be Title"
    }
    
    if request.method == "GET":
        return render(request, template, prompt)
    
    csv_file = request.FILES['file']
    
    if not csv_file.name.endswith('.csv'):
        messages.error(request, "This id not a csv file")
        
    data_set = csv_file.read().decode('UTF-8')
    io_string = io.StringIO(data_set)
    next(io_string)
    
    for column in csv.reader(io_string, delimiter=',',  quotechar='|', quoting =csv.QUOTE_NONE):
        _, created = SubmissionStatus.objects.update_or_create(
            title=column[1],    
        )
        
    context = {'current_user':current_user,}
    return render(request, template, context)


@permission_required('admin.can_add_log_entry')
def MembershipStatus_upload(request):
    current_user=[]
    if not request.user.user_type == '1':
        current_user=Executives_Tasks_Model.objects.get(user=request.user.id)

    template = "master_templates/file_upload.html"
    
    
    prompt = {
        'order': "Order of the CSV should be Title"
    }
    
    if request.method == "GET":
        return render(request, template, prompt)
    
    csv_file = request.FILES['file']
    
    if not csv_file.name.endswith('.csv'):
        messages.error(request, "This id not a csv file")
        
    data_set = csv_file.read().decode('UTF-8')
    io_string = io.StringIO(data_set)
    next(io_string)
    
    for column in csv.reader(io_string, delimiter=',',  quotechar='|', quoting =csv.QUOTE_NONE):
        _, created = MembershipStatus.objects.update_or_create(
            title=column[1],    
        )
        
    context = {'current_user':current_user,}
    return render(request, template, context)


@permission_required('admin.can_add_log_entry')
def ProcessingStatus_upload(request):
    current_user=[]
    if not request.user.user_type == '1':
        current_user=Executives_Tasks_Model.objects.get(user=request.user.id)

    template = "master_templates/file_upload.html"
    
    
    prompt = {
        'order': "Order of the CSV should be Title"
    }
    
    if request.method == "GET":
        return render(request, template, prompt)
    
    csv_file = request.FILES['file']
    
    if not csv_file.name.endswith('.csv'):
        messages.error(request, "This id not a csv file")
        
    data_set = csv_file.read().decode('UTF-8')
    io_string = io.StringIO(data_set)
    next(io_string)
    
    for column in csv.reader(io_string, delimiter=',',  quotechar='|', quoting =csv.QUOTE_NONE):
        _, created = ProcessingStatus.objects.update_or_create(
            title=column[1],    
        )
        
    context = {'current_user':current_user,}
    return render(request, template, context)


@permission_required('admin.can_add_log_entry')
def CertificationStatus_upload(request):
    current_user=[]
    if not request.user.user_type == '1':
        current_user=Executives_Tasks_Model.objects.get(user=request.user.id)

    template = "master_templates/file_upload.html"
    
    
    prompt = {
        'order': "Order of the CSV should be Title"
    }
    
    if request.method == "GET":
        return render(request, template, prompt)
    
    csv_file = request.FILES['file']
    
    if not csv_file.name.endswith('.csv'):
        messages.error(request, "This id not a csv file")
        
    data_set = csv_file.read().decode('UTF-8')
    io_string = io.StringIO(data_set)
    next(io_string)
    
    for column in csv.reader(io_string, delimiter=',',  quotechar='|', quoting =csv.QUOTE_NONE):
        _, created = CertificationStatus.objects.update_or_create(
            title=column[1],    
        )
        
    context = {'current_user':current_user,}
    return render(request, template, context)


@permission_required('admin.can_add_log_entry')
def ApprovalStatus_upload(request):
    current_user=[]
    if not request.user.user_type == '1':
        current_user=Executives_Tasks_Model.objects.get(user=request.user.id)

    template = "master_templates/file_upload.html"
    
    
    prompt = {
        'order': "Order of the CSV should be Title"
    }
    
    if request.method == "GET":
        return render(request, template, prompt)
    
    csv_file = request.FILES['file']
    
    if not csv_file.name.endswith('.csv'):
        messages.error(request, "This id not a csv file")
        
    data_set = csv_file.read().decode('UTF-8')
    io_string = io.StringIO(data_set)
    next(io_string)
    
    for column in csv.reader(io_string, delimiter=',',  quotechar='|', quoting =csv.QUOTE_NONE):
        _, created = ApprovalStatus.objects.update_or_create(
            title=column[1],    
        )
        
    context = {'current_user':current_user,}
    return render(request, template, context)



@permission_required('admin.can_add_log_entry')
def TransactionStatus_upload(request):
    current_user=[]
    if not request.user.user_type == '1':
        current_user=Executives_Tasks_Model.objects.get(user=request.user.id)

    template = "master_templates/file_upload.html"
    
    
    prompt = {
        'order': "Order of the CSV should be Title"
    }
    
    if request.method == "GET":
        return render(request, template, prompt)
    
    csv_file = request.FILES['file']
    
    if not csv_file.name.endswith('.csv'):
        messages.error(request, "This id not a csv file")
        
    data_set = csv_file.read().decode('UTF-8')
    io_string = io.StringIO(data_set)
    next(io_string)
    
    for column in csv.reader(io_string, delimiter=',',  quotechar='|', quoting =csv.QUOTE_NONE):
        _, created = TransactionStatus.objects.update_or_create(
            title=column[1],    
        )
        
    context = {'current_user':current_user,}
    return render(request, template, context)


    
@permission_required('admin.can_add_log_entry')
def ReceiptStatus_upload(request):
    current_user=[]
    if not request.user.user_type == '1':
        current_user=Executives_Tasks_Model.objects.get(user=request.user.id)

    template = "master_templates/file_upload.html"
    
    
    prompt = {
        'order': "Order of the CSV should be Title"
    }
    
    if request.method == "GET":
        return render(request, template, prompt)
    
    csv_file = request.FILES['file']
    
    if not csv_file.name.endswith('.csv'):
        messages.error(request, "This id not a csv file")
        
    data_set = csv_file.read().decode('UTF-8')
    io_string = io.StringIO(data_set)
    next(io_string)
    
    for column in csv.reader(io_string, delimiter=',',  quotechar='|', quoting =csv.QUOTE_NONE):
        _, created = ReceiptStatus.objects.update_or_create(
            title=column[1],    
        )
        
    context = {'current_user':current_user,}
    return render(request, template, context)    


    
@permission_required('admin.can_add_log_entry')
def Gender_upload(request):
    current_user=[]
    if not request.user.user_type == '1':
        current_user=Executives_Tasks_Model.objects.get(user=request.user.id)

    template = "master_templates/file_upload.html"
    
    
    prompt = {
        'order': "Order of the CSV should be Title"
    }
    
    if request.method == "GET":
        return render(request, template, prompt)
    
    csv_file = request.FILES['file']
    
    if not csv_file.name.endswith('.csv'):
        messages.error(request, "This id not a csv file")
        
    data_set = csv_file.read().decode('UTF-8')
    io_string = io.StringIO(data_set)
    next(io_string)
    
    for column in csv.reader(io_string, delimiter=',',  quotechar='|', quoting =csv.QUOTE_NONE):
        _, created = Gender.objects.update_or_create(
            title=column[1],    
        )
        
    context = {'current_user':current_user,}
    return render(request, template, context)    


@permission_required('admin.can_add_log_entry')
def Banks_upload(request):
    current_user=[]
    if not request.user.user_type == '1':
        current_user=Executives_Tasks_Model.objects.get(user=request.user.id)

    template = "master_templates/file_upload.html"
    
    
    prompt = {
        'order': "Order of the CSV should be Title"
    }
    
    if request.method == "GET":
        return render(request, template, prompt)
    
    csv_file = request.FILES['file']
    
    if not csv_file.name.endswith('.csv'):
        messages.error(request, "This id not a csv file")
        
    data_set = csv_file.read().decode('UTF-8')
    io_string = io.StringIO(data_set)
    next(io_string)
    
    for column in csv.reader(io_string, delimiter=',',  quotechar='|', quoting =csv.QUOTE_NONE):
        _, created = Banks.objects.update_or_create(
            title=column[1],    
        )
        
    context = {'current_user':current_user,}
    return render(request, template, context)    





    
@permission_required('admin.can_add_log_entry')
def Locations_upload(request):
    current_user=[]
    if not request.user.user_type == '1':
        current_user=Executives_Tasks_Model.objects.get(user=request.user.id)

    template = "master_templates/file_upload.html"
    
    
    prompt = {
        'order': "Order of the CSV should be Title"
    }
    
    if request.method == "GET":
        return render(request, template, prompt)
    
    csv_file = request.FILES['file']
    
    if not csv_file.name.endswith('.csv'):
        messages.error(request, "This id not a csv file")
        
    data_set = csv_file.read().decode('UTF-8')
    io_string = io.StringIO(data_set)
    next(io_string)
    
    for column in csv.reader(io_string, delimiter=',',  quotechar='|', quoting =csv.QUOTE_NONE):
        _, created = Locations.objects.update_or_create(
            title=column[1],    
        )
        
    context = {'current_user':current_user,}
    return render(request, template, context)    



@permission_required('admin.can_add_log_entry')
def AccountTypes_upload(request):
    current_user=[]
    if not request.user.user_type == '1':
        current_user=Executives_Tasks_Model.objects.get(user=request.user.id)

    template = "master_templates/file_upload.html"
    
    
    prompt = {
        'order': "Order of the CSV should be Title"
    }
    
    if request.method == "GET":
        return render(request, template, prompt)
    
    csv_file = request.FILES['file']
    
    if not csv_file.name.endswith('.csv'):
        messages.error(request, "This id not a csv file")
        
    data_set = csv_file.read().decode('UTF-8')
    io_string = io.StringIO(data_set)
    next(io_string)
    
    for column in csv.reader(io_string, delimiter=',',  quotechar='|', quoting =csv.QUOTE_NONE):
        _, created = AccountTypes.objects.update_or_create(
            title=column[1],    
        )
        
    context = {'current_user':current_user,}
    return render(request, template, context)

    
@permission_required('admin.can_add_log_entry')
def Departments_upload(request):
    current_user=[]
    if not request.user.user_type == '1':
        current_user=Executives_Tasks_Model.objects.get(user=request.user.id)

    template = "master_templates/file_upload.html"
    
    
    prompt = {
        'order': "Order of the CSV should be Title"
    }
    
    if request.method == "GET":
        return render(request, template, prompt)
    
    csv_file = request.FILES['file']
    
    if not csv_file.name.endswith('.csv'):
        messages.error(request, "This id not a csv file")
        
    data_set = csv_file.read().decode('UTF-8')
    io_string = io.StringIO(data_set)
    next(io_string)
    
    for column in csv.reader(io_string, delimiter=',',  quotechar='|', quoting =csv.QUOTE_NONE):
        _, created = Departments.objects.update_or_create(
            title=column[1],    
        )
        
    context = {'current_user':current_user,}
    return render(request, template, context)

    
@permission_required('admin.can_add_log_entry')
def SalaryInstitution_upload(request):
    current_user=[]
    if not request.user.user_type == '1':
        current_user=Executives_Tasks_Model.objects.get(user=request.user.id)

    template = "master_templates/file_upload.html"
    
    
    prompt = {
        'order': "Order of the CSV should be Title"
    }
    
    if request.method == "GET":
        return render(request, template, prompt)
    
    csv_file = request.FILES['file']
    
    if not csv_file.name.endswith('.csv'):
        messages.error(request, "This id not a csv file")
        
    data_set = csv_file.read().decode('UTF-8')
    io_string = io.StringIO(data_set)
    next(io_string)
    
    for column in csv.reader(io_string, delimiter=',',  quotechar='|', quoting =csv.QUOTE_NONE):
        _, created = SalaryInstitution.objects.update_or_create(
            title=column[1],    
        )
        
    context = {'current_user':current_user,}
    return render(request, template, context)   

    
@permission_required('admin.can_add_log_entry')
def InterestDeductionSource_upload(request):
    current_user=[]
    if not request.user.user_type == '1':
        current_user=Executives_Tasks_Model.objects.get(user=request.user.id)

    template = "master_templates/file_upload.html"
    
    
    prompt = {
        'order': "Order of the CSV should be Title"
    }
    
    if request.method == "GET":
        return render(request, template, prompt)
    
    csv_file = request.FILES['file']
    
    if not csv_file.name.endswith('.csv'):
        messages.error(request, "This id not a csv file")
        
    data_set = csv_file.read().decode('UTF-8')
    io_string = io.StringIO(data_set)
    next(io_string)
    
    for column in csv.reader(io_string, delimiter=',',  quotechar='|', quoting =csv.QUOTE_NONE):
        _, created = InterestDeductionSource.objects.update_or_create(
            title=column[1],    
        )
        
    context = {'current_user':current_user,}
    return render(request, template, context)   

    
    
@permission_required('admin.can_add_log_entry')
def TransactionSources_upload(request):
    current_user=[]
    if not request.user.user_type == '1':
        current_user=Executives_Tasks_Model.objects.get(user=request.user.id)

    template = "master_templates/file_upload.html"
    
    
    prompt = {
        'order': "Order of the CSV should be Title"
    }
    
    if request.method == "GET":
        return render(request, template, prompt)
    
    csv_file = request.FILES['file']
    
    if not csv_file.name.endswith('.csv'):
        messages.error(request, "This id not a csv file")
        
    data_set = csv_file.read().decode('UTF-8')
    io_string = io.StringIO(data_set)
    next(io_string)
    
    for column in csv.reader(io_string, delimiter=',',  quotechar='|', quoting =csv.QUOTE_NONE):
        _, created = TransactionSources.objects.update_or_create(
            title=column[1],    
        )
        
    context = {'current_user':current_user,}
    return render(request, template, context)


@permission_required('admin.can_add_log_entry')
def UserType_upload(request):
    current_user=[]
    if not request.user.user_type == '1':
        current_user=Executives_Tasks_Model.objects.get(user=request.user.id)

    template = "master_templates/file_upload.html"
    
    
    prompt = {
        'order': "Order of the CSV should be Title"
    }
    
    if request.method == "GET":
        return render(request, template, prompt)
    
    csv_file = request.FILES['file']
    
    if not csv_file.name.endswith('.csv'):
        messages.error(request, "This id not a csv file")
        
    data_set = csv_file.read().decode('UTF-8')
    io_string = io.StringIO(data_set)
    next(io_string)
    
    for column in csv.reader(io_string, delimiter=',',  quotechar='|', quoting =csv.QUOTE_NONE):
        _, created = UserType.objects.update_or_create(
            code=column[1],    
            title=column[2],    
        )
        
    context = {'current_user':current_user,}
    return render(request, template, context)



@permission_required('admin.can_add_log_entry')
def loan_criteria_base_upload(request):
    current_user=[]
    if not request.user.user_type == '1':
        current_user=Executives_Tasks_Model.objects.get(user=request.user.id)

    template = "master_templates/file_upload.html"
    
    
    prompt = {
        'order': "Order of the CSV should be Sources,Description"
    }
    
    if request.method == "GET":
        return render(request, template, prompt)
    
    csv_file = request.FILES['file']
    
    if not csv_file.name.endswith('.csv'):
        messages.error(request, "This id not a csv file")
        
    data_set = csv_file.read().decode('UTF-8')
    io_string = io.StringIO(data_set)
    next(io_string)
    
    for column in csv.reader(io_string, delimiter=',',  quotechar='|', quoting =csv.QUOTE_NONE):
        _, created = LoanCriteriaBase.objects.update_or_create(
            source=column[1],    
            description=column[2],    
        )
        
    context = {'current_user':current_user,}
    return render(request, template, context)


####################################################################
###################### COMMODITY MANAGER ######################
####################################################################
def Commodity_Products_Add_Transactions_Load(request):
    current_user=[]
    if not request.user.user_type == '1':
        current_user=Executives_Tasks_Model.objects.get(user=request.user.id)

    records =TransactionTypes.objects.filter(category__title='NON-MONETARY')
    context={
    'current_user':current_user,
    'records':records,
    }
    return render(request,'master_templates/Commodity_Products_Add_Transactions_Load.html',context)



def Commodity_Products_Add_Transactions_Categories_Load(request,pk):
    current_user=[]
    if not request.user.user_type == '1':
        current_user=Executives_Tasks_Model.objects.get(user=request.user.id)

    records =Commodity_Categories.objects.filter(transaction_id=pk)
    context={
    'current_user':current_user,
    'records':records,
    }
    return render(request,'master_templates/Commodity_Products_Add_Transactions_Categories_Load.html',context)

def Commodity_Products_add(request,pk):
    current_user=[]
    if not request.user.user_type == '1':
        current_user=Executives_Tasks_Model.objects.get(user=request.user.id)

    form = Commodity_Products_add_Form(request.POST or None)
    record =Commodity_Categories.objects.get(id=pk)
    status=MembershipStatus.objects.get(title='ACTIVE')
    records=Commodity_Product_List.objects.filter(category=record)
    
    if request.method=="POST":
        product_name = request.POST.get('product_name')
        product_model = request.POST.get('product_model')
        details = request.POST.get('details')
        queryset=Commodity_Product_List(category=record,product_name=product_name,product_model=product_model,details=details,status=status)
        queryset.save()
        messages.success(request,'Record Submitted Successfully')
        return HttpResponseRedirect(reverse('Commodity_Products_add',args=(pk,)))
    context={
    'current_user':current_user,
    'form':form,
    'record':record,
    'records':records,
    }
    return render(request,'master_templates/Commodity_Products_add.html',context)




def Commodity_Products_Manage_Transactions_Load(request):
    current_user=[]
    if not request.user.user_type == '1':
        current_user=Executives_Tasks_Model.objects.get(user=request.user.id)

    records =TransactionTypes.objects.filter(category__title='NON-MONETARY')
    context={
    'current_user':current_user,
    'records':records,
    }
    return render(request,'master_templates/Commodity_Products_Manage_Transactions_Load.html',context)



def Commodity_Products_Manage_Load(request,pk):
    current_user=[]
    if not request.user.user_type == '1':
        current_user=Executives_Tasks_Model.objects.get(user=request.user.id)

    transaction =TransactionTypes.objects.get(id=pk)
    records=Commodity_Product_List.objects.filter(category__transaction=transaction)

    context={
    'current_user':current_user,
    'records':records,
    }
    return render(request,'master_templates/Commodity_Products_Manage_Load.html',context)


def Commodity_Products_Manage_Update(request,pk):
    current_user=[]
    if not request.user.user_type == '1':
        current_user=Executives_Tasks_Model.objects.get(user=request.user.id)

    form = Commodity_Products_Update_Form(request.POST or None)
    record=Commodity_Product_List.objects.get(id=pk)
    
    form.fields['product_name'].initial = record.product_name
    form.fields['product_model'].initial = record.product_model
    form.fields['details'].initial = record.details
    form.fields['status'].initial = record.status.id

    if request.method == 'POST':
        product_name=request.POST.get('product_name')
        product_model=request.POST.get('product_model')
        details=request.POST.get('details')
        status_id = request.POST.get('status')
        status=MembershipStatus.objects.get(id=status_id)
        
        record.product_name=product_name
        record.product_model=product_model
        record.details=details
        record.status=status
        record.save()
        messages.success(request,'Record Updated Successfully')
        return HttpResponseRedirect(reverse('Commodity_Products_Manage_Load',args=(record.category.transaction_id,)))
    context={
    'current_user':current_user,
    'form':form,
    'record':record,
    }
    return render(request,'master_templates/Commodity_Products_Manage_Update.html',context)


def Commodity_Products_Manage_Remove(request,pk):
    record=Commodity_Product_List.objects.get(id=pk)
   
    if Members_Commodity_Loan_Products_Selection.objects.filter(product__product=record).exists():
        messages.error(request,'Record Already in Use')
        return HttpResponseRedirect(reverse('Commodity_Products_Manage_Load',args=(record.category.transaction_id,)))
    record.delete()
    messages.success(request,'Record Deleted Successfully')
    return HttpResponseRedirect(reverse('Commodity_Products_Manage_Load',args=(record.category.transaction_id,)))



def addCompanies(request):
    current_user=[]
    if not request.user.user_type == '1':
        current_user=Executives_Tasks_Model.objects.get(user=request.user.id)

    items= Companies.objects.all()
    title="Add Companies"
    form = addCompaniesForm(request.POST or None)
    if request.method ==  "POST":
        form = addCompaniesForm(request.POST)
        if form.is_valid():
            title=form.cleaned_data["title"]
            record = Companies(title=title)
            record.save()
            messages.success(request,"Record Added Successfully")
            return  HttpResponseRedirect(reverse('addCompanies'))
    context={
    'current_user':current_user,
    'form':form,
    'items':items,
    'url':'addCompanies',
    'button_text':"Add Companies",
    'title':title,
    }
    return render(request,'master_templates/add_single_item.html', context)

def Manage_Companies(request):
    current_user=[]
    if not request.user.user_type == '1':
        current_user=Executives_Tasks_Model.objects.get(user=request.user.id)

    companies=Companies.objects.all()
    context={
    'current_user':current_user,
    'companies':companies,
    }
    return render(request,'master_templates/manage_companies.html', context)

def Manage_Companies_update(request,pk):
    current_user=[]
    if not request.user.user_type == '1':
        current_user=Executives_Tasks_Model.objects.get(user=request.user.id)

    form = addCompaniesForm(request.POST or None)
    company=Companies.objects.get(id=pk)

    form.fields['title'].initial=company.title

    if request.method == "POST":
        title=request.POST.get('title')
        company.title=title
        company.save()
        return HttpResponseRedirect(reverse('Manage_Companies'))
    context={
    'current_user':current_user,
    'form':form,
    'company':company,
    }
    return render(request,'master_templates/Manage_Companies_update.html', context)


def Delete_Companies(request,pk):
    record=Companies.objects.get(id=pk)
    record.delete()
    return HttpResponseRedirect(reverse('Manage_Companies'))



def Product_Linking_Period_Load(request):
    current_user=[]
    if not request.user.user_type == '1':
        current_user=Executives_Tasks_Model.objects.get(user=request.user.id)


    if request.method == "POST":
        period_obj=request.POST.get('period')
        period=Commodity_Period.objects.get(id=period_obj)

        batch_obj=request.POST.get('batch')
        batch=Commodity_Period_Batch.objects.get(id=batch_obj)

        transaction_obj=request.POST.get('transaction')
        transaction=TransactionTypes.objects.get(id=transaction_obj)

        return HttpResponseRedirect(reverse('Product_Linking_Company_Load',args=(period_obj, batch_obj,transaction_obj)))
    form=Product_Linking_Period_Load_form(request.POST or None)
    context={
    'current_user':current_user,
    'form':form,
    # 'period':period,
    # 'batch':batch,
    }
    return render(request,'master_templates/Product_Linking_Period_Load.html',context)


def Product_Linking_Company_Load(request,period_obj,batch_obj,transaction_obj):
    current_user=[]
    if not request.user.user_type == '1':
        current_user=Executives_Tasks_Model.objects.get(user=request.user.id)

    companies=Companies.objects.all()

    period=Commodity_Period.objects.get(id=period_obj)        
    batch=Commodity_Period_Batch.objects.get(id=batch_obj)
    transaction=TransactionTypes.objects.get(id=transaction_obj)

    context={
    'current_user':current_user,
    'companies':companies,
    'period':period,
    'batch':batch,
    'transaction':transaction,
    }
    return render(request,'master_templates/Product_Linking_Company_Load.html',context)



def Product_Linking_Details(request,pk,period_pk,batch_pk,transaction_pk):
    current_user=[]
    if not request.user.user_type == '1':
        current_user=Executives_Tasks_Model.objects.get(user=request.user.id)


    period=Commodity_Period.objects.get(id=period_pk)        
    batch=Commodity_Period_Batch.objects.get(id=batch_pk)
    transaction=TransactionTypes.objects.get(id=transaction_pk)

    company=Companies.objects.get(id=pk)
    status=MembershipStatus.objects.get(title='ACTIVE')
    
    records=Commodity_Product_List.objects.filter(category__transaction=transaction,status=status)
    linked_records = Company_Products.objects.filter(company=company,period=period,batch=batch,product__category__transaction=transaction)

    context={
    'current_user':current_user,
    'company':company,
    'records':records,
    'linked_records':linked_records,
    'period':period,
    'batch':batch,
    'transaction':transaction,
    }
    return render(request,'master_templates/Product_Linking_Details.html',context)


def Product_Linking_Details_Preview(request,comp_pk,pk,period_pk,batch_pk,transaction_pk):
    current_user=[]
    if not request.user.user_type == '1':
        current_user=Executives_Tasks_Model.objects.get(user=request.user.id)

    form=Product_Linking_Details_Preview_form(request.POST or None)
    company=Companies.objects.get(id=comp_pk)
    product=Commodity_Product_List.objects.get(id=pk)


    if request.method == "POST":
        period=Commodity_Period.objects.get(id=period_pk)        
        batch=Commodity_Period_Batch.objects.get(id=batch_pk)

        status=MembershipStatus.objects.get(title='ACTIVE')
        amount=request.POST.get('amount')
        
        if Company_Products.objects.filter(company=company,product=product,period=period,batch=batch).exists():
            Company_Products.objects.filter(company=company,product=product,period=period,batch=batch).update(amount=amount)
        else:
            Company_Products(company=company,product=product,period=period,batch=batch,amount=amount,status=status).save()
        return HttpResponseRedirect(reverse('Product_Linking_Details',args=(comp_pk,period_pk,batch_pk,transaction_pk)))
    
    form.fields['product_name'].initial=product.product_name
    form.fields['product_model'].initial=product.product_model
    form.fields['details'].initial=product.details
    context={
    'current_user':current_user,
    'company':company,
    'form':form,
    'product':product,
    }
    return render(request,'master_templates/Product_Linking_Details_Preview.html',context)



def Product_UnLinking_Process(request,comp_pk,pk,period_pk, batch_pk, transaction_pk):
    current_user=[]
    if not request.user.user_type == '1':
        current_user=Executives_Tasks_Model.objects.get(user=request.user.id)

    product=Company_Products.objects.get(id=pk)
    product.delete()

    messages.success(request,"Record Deleted Successfully")
    return  HttpResponseRedirect(reverse('Product_Linking_Details',args=(comp_pk,period_pk,batch_pk,transaction_pk,)))
    context={
    'current_user':current_user,
    'company':company,
    'records':records,
    }
    return render(request,'master_templates/Product_Linking_Details.html',context)



def Product_Settings_Period_Load(request):
    current_user=[]
    if not request.user.user_type == '1':
        current_user=Executives_Tasks_Model.objects.get(user=request.user.id)


    if request.method == "POST":
        period_obj=request.POST.get('period')
        period=Commodity_Period.objects.get(id=period_obj)

        batch_obj=request.POST.get('batch')
        batch=Commodity_Period_Batch.objects.get(id=batch_obj)

        transaction_obj=request.POST.get('transaction')
        transaction=TransactionTypes.objects.get(id=transaction_obj)

        return HttpResponseRedirect(reverse('Product_Price_Settings_Company_Load',args=(period_obj, batch_obj,transaction_obj)))
    form=Product_Linking_Period_Load_form(request.POST or None)
    context={
    'current_user':current_user,
    'form':form,
    # 'period':period,
    # 'batch':batch,
    }
    return render(request,'master_templates/Product_Settings_Period_Load.html',context)



def Product_Price_Settings_Company_Load(request,period_obj,batch_obj,transaction_obj):
    current_user=[]
    if not request.user.user_type == '1':
        current_user=Executives_Tasks_Model.objects.get(user=request.user.id)

    companies=Companies.objects.all()
    period=Commodity_Period.objects.get(id=period_obj)
    batch=Commodity_Period_Batch.objects.get(id=batch_obj)
    transaction=TransactionTypes.objects.get(id=transaction_obj)

    context={
    'current_user':current_user,
    'companies':companies,
    'period':period,
    'batch':batch,
    'transaction':transaction,
    }
    return render(request,'master_templates/Product_Price_Settings_Company_Load.html',context)


def Product_Price_Settings_details(request,pk,period_obj,batch_obj,transaction_obj):
    current_user=[]
    if not request.user.user_type == '1':
        current_user=Executives_Tasks_Model.objects.get(user=request.user.id)

    company=Companies.objects.get(id=pk)
    period=Commodity_Period.objects.get(id=period_obj)
    batch=Commodity_Period_Batch.objects.get(id=batch_obj)
    transaction=TransactionTypes.objects.get(id=transaction_obj)


    # records=Company_Products.objects.filter(company=company)
    records=Company_Products.objects.filter(company=company,period=period,batch=batch,product__category__transaction=transaction)

    context={
    'current_user':current_user,
    'records':records,
    'company':company,
    'period':period,
    'batch':batch,
    'transaction':transaction,
    }
    return render(request,'master_templates/Product_Price_Settings_details.html',context)


def Product_Price_Settings_Update(request,comp_pk,pk):
    current_user=[]
    if not request.user.user_type == '1':
        current_user=Executives_Tasks_Model.objects.get(user=request.user.id)

    form=Commodity_Products_Price_Update_Form(request.POST or None)
    company=Companies.objects.get(id=comp_pk)
    record=Company_Products.objects.get(id=pk)


    form.fields['product_name'].initial=record.product.product_name
    form.fields['product_model'].initial=record.product.product_model
    form.fields['details'].initial=record.product.details
    form.fields['unit_cost_price'].initial=record.amount
    form.fields['status'].initial=record.status_id


    if request.method == 'POST':
        unit_cost_price=request.POST.get('unit_cost_price')
        status_id=request.POST.get('status')
        status=MembershipStatus.objects.get(id=status_id)
        record.amount=unit_cost_price
        record.status=status
        record.save()
        return HttpResponseRedirect(reverse('Product_Price_Settings_details',args=(comp_pk,record.period_id,record.batch_id,record.product.category.transaction_id)))
     
    context={
    'current_user':current_user,
    'record':record,
    'company':company,
    'form':form,
    }
    return render(request,'master_templates/Product_Price_Settings_Update.html',context)


####################################################################
###################### USER ACCOUNT MANAGERS ######################
####################################################################


def Invoice_Title(request):
    current_user=[]
    if not request.user.user_type == '1':
        current_user=Executives_Tasks_Model.objects.get(user=request.user.id)

    form=Invoice_Title_form(request.POST or None)
   
    if InvoiceHeader.objects.all().count()>0:
        record=InvoiceHeader.objects.first()
      
        form.fields['title'].initial = record.title
        form.fields['address1'].initial = record.address1
        form.fields['address2'].initial = record.address2
        form.fields['phone_no'].initial = record.phone_no


    if request.method == "POST":
        title=request.POST.get("title")
        address1=request.POST.get("address1")
        address2=request.POST.get("address2")
        phone_no=request.POST.get("phone_no")

        if InvoiceHeader.objects.all().count()>0:
            record=InvoiceHeader.objects.first()
      
            record.title=title
            record.address1=address1
            record.address2=address2
            record.phone_no=phone_no
            record.save()
            messages.success(request,'Record Updated Successfully')
        else:
            record=InvoiceHeader(title=title,address1=address1,address2=address2,phone_no=phone_no)
            record.save()
            messages.success(request,'Record Added Successfully')
        return HttpResponseRedirect(reverse('Invoice_Title'))
    
 

    context={
    'current_user':current_user,
    'form':form,
    }
    return render(request,'master_templates/Invoice_Title.html',context)

def DataCapture_Manager(request):
    current_user=[]
    if not request.user.user_type == '1':
        current_user=Executives_Tasks_Model.objects.get(user=request.user.id)

    form=DataCapture_Manager_form(request.POST or None)
    item=[]
    if DataCaptureManager.objects.all().exists():
        item=DataCaptureManager.objects.first()

    item=DataCaptureManager.objects.first()
    if request.method=='POST':
        status_id=request.POST.get('status')
        status=MembershipStatus.objects.get(id=status_id)

        if DataCaptureManager.objects.all().exists():
            record=DataCaptureManager.objects.first()
            record.status=status
        else:
            record=DataCaptureManager(status=status)
        record.save()
        return HttpResponseRedirect(reverse('DataCapture_Manager'))
    if item:
        form.fields['status'].initial=item.status.id
    context={
    'current_user':current_user,
    'form':form,

    }
    return render(request,'master_templates/DataCapture_Manager.html',context)



def add_staff(request):
    current_user=[]
    if not request.user.user_type == '1':
        current_user=Executives_Tasks_Model.objects.get(user=request.user.id)

    title="Add Staff"
    form = addUsersForm(request.POST or None)
    items=UserType.objects.all()
    users = CustomUser.objects.exclude(Q(user_type__iexact='1') | Q(user_type__iexact='5'))
    
    if request.method == "POST":
        title_id=request.POST.get("title")
        title=Titles.objects.get(id=title_id)

    

        username=request.POST.get("username")
        first_name=request.POST.get("first_name")
        last_name=request.POST.get("last_name")
        middle_name=request.POST.get("middle_name")
        password=request.POST.get("password")
        email=request.POST.get("email")
        phone_number=request.POST.get("phone_no")
        address=request.POST.get("address")
        gender_id=request.POST.get("gender")
        gender= Gender.objects.get(id=gender_id)
        user_type_obj=request.POST.get("user_type")
        user_type = UserType.objects.get(id=user_type_obj)

        password=[]
        if DefaultPassword.objects.all().exists():
            password_obj=DefaultPassword.objects.first()
            password=password_obj.title
        else:
            messages.error(request,'Default Password not Set')
            return HttpResponseRedirect(reverse("add_staff")) 
        try:
            if user_type.code == '2':
                user = CustomUser.objects.create_user(username=username,password=password,email=email,last_name=last_name,first_name=first_name,user_type=2)
                record=Executives_Tasks_Model(user=user).save()
            if user_type.code == '3':
                user = CustomUser.objects.create_user(username=username,password=password,email=email,last_name=last_name,first_name=first_name,user_type=3)
                record=Desk_Office_Tasks_Model(user=user).save()
            if user_type.code == '4':
                user = CustomUser.objects.create_user(username=username,password=password,email=email,last_name=last_name,first_name=first_name,user_type=4)
                record=Shop_Tasks_Models(user=user).save()

            user.staff.middle_name=middle_name
            user.staff.address=address
            user.staff.phone_number=phone_number
            user.staff.gender=gender
            user.staff.title=title
            user.save()
            messages.success(request,"User Added Successfully")
            return HttpResponseRedirect(reverse("add_staff"))
        except:
            messages.error(request,"Failed to add System User")
            return HttpResponseRedirect(reverse("add_staff")) 

    context={
    'current_user':current_user,
    'title':title,
    'form':form,
    'users':users,
    'url':'add_staff',
    'items':items,
    'button_text':"Add",
    }
    return render(request, "master_templates/add_staff.html",context)



def add_staff_manage(request):
    current_user=[]
    if not request.user.user_type == '1':
        current_user=Executives_Tasks_Model.objects.get(user=request.user.id)

    users = CustomUser.objects.exclude(Q(user_type__iexact='1') | Q(user_type__iexact='5'))
    context={
    'current_user':current_user,
    'users':users,
    }
    return render(request,'master_templates/addStaff_manage.html',context)

def add_staff_manage_view(request,pk):
    current_user=[]
    if not request.user.user_type == '1':
        current_user=Executives_Tasks_Model.objects.get(user=request.user.id)

    form=add_staff_manage_form(request.POST or None)
    user=Staff.objects.get(admin_id=pk)
    user_type=UserType.objects.get(code=user.admin.user_type)
    form.fields['title'].initial=user.title.id
    form.fields['last_name'].initial=user.admin.last_name
    form.fields['first_name'].initial=user.admin.first_name
    form.fields['middle_name'].initial=user.middle_name
    form.fields['address'].initial=user.address
    form.fields['phone_no'].initial=user.phone_number
    form.fields['gender'].initial=user.gender.id
 
    form.fields['username'].initial=user.admin.username
    form.fields['user_type'].initial=user_type.id
    form.fields['email'].initial=user.admin.email
    
    if request.method == "POST":
        title_id=request.POST.get("title")
        title=Titles.objects.get(id=title_id)
 
        username=request.POST.get("username")
        first_name=request.POST.get("first_name")
        last_name=request.POST.get("last_name")
        middle_name=request.POST.get("middle_name")
        password1=request.POST.get("password1")
        password2=request.POST.get("password2")
        email=request.POST.get("email")
        phone_number=request.POST.get("phone_no")
        address=request.POST.get("address")
        gender_id=request.POST.get("gender")
        gender= Gender.objects.get(id=gender_id)
        user_type_obj=request.POST.get("user_type")
        user_type = UserType.objects.get(id=user_type_obj)

        changepassword=request.POST.get("changepassword")
        if changepassword:
            if password1 != password2:
                messages.info(request,"Password Mismatch")
                return HttpResponseRedirect(reverse('add_staff_manage_view',args=(pk,)))
            password=password1        
            user.admin.set_password(password)  # replace with your real password
        user.admin.username=username
        user.admin.first_name=first_name
        user.admin.last_name=last_name
        user.admin.email=email
        user.admin.user_type=user_type.code
        user.middle_name=middle_name
        user.phone_number=phone_number
        user.address=address
        user.gender=gender
    
        user.title=title

        user.save()
        user.admin.save()
        return HttpResponseRedirect(reverse('add_staff_manage'))
    context={
    'current_user':current_user,
    'form':form,
    }
    return render(request,'master_templates/add_staff_manage_view.html',context)



def super_user_add(request):
    form=super_user_manage_form(request.POST or None)
    current_user=[]
    if not request.user.user_type == '1':
        current_user=Executives_Tasks_Model.objects.get(user=request.user.id)

    if request.method == 'POST':
        username=request.POST.get("username")
        first_name=request.POST.get("first_name")
        last_name=request.POST.get("last_name")
        password1=request.POST.get("password1")
        password2=request.POST.get("password2")
        email=request.POST.get("email")
        user = CustomUser.objects.create_user(username=username,password=password1,email=email,last_name=last_name,first_name=first_name,user_type=1)
        return HttpResponseRedirect(reverse('super_user_add'))
    context={
    'form':form,
    'current_user':current_user,
    }
    return render(request,'master_templates/super_user_add.html',context)




def super_user_manage(request):
    current_user=[]
    if not request.user.user_type == '1':
        current_user=Executives_Tasks_Model.objects.get(user=request.user.id)

    users = CustomUser.objects.filter(Q(user_type__iexact='1'))
    context={
    'current_user':current_user,
    'users':users,
    }
    return render(request,'master_templates/super_user_manage.html',context)


def super_user_manage_view(request,pk):
    current_user=[]
    if not request.user.user_type == '1':
        current_user=Executives_Tasks_Model.objects.get(user=request.user.id)

    form=super_user_manage_form(request.POST or None)
    user=CustomUser.objects.get(id=pk) 
    form.fields['last_name'].initial=user.last_name
    form.fields['first_name'].initial=user.first_name
    form.fields['username'].initial=user.username
    form.fields['email'].initial=user.email
    
    if request.method == "POST": 
        username=request.POST.get("username")
        first_name=request.POST.get("first_name")
        last_name=request.POST.get("last_name")
        password1=request.POST.get("password1")
        password2=request.POST.get("password2")
        email=request.POST.get("email")
        
        if CustomUser.objects.filter(email=email).exclude(id=pk).exists():
            messages.info(request,'Email already in Use')
            return HttpResponseRedirect(reverse('super_user_manage_view',args=(pk,)))
       
        changepassword=request.POST.get("changepassword")
        if changepassword:
            if password1 != password2:
                messages.info(request,"Password Mismatch")
                return HttpResponseRedirect(reverse('super_user_manage_view',args=(pk,)))
            password=password1        
            user.admin.set_password(password)  # replace with your real password
        user.username=username
        user.first_name=first_name
        user.last_name=last_name
        user.email=email
    
        user.save()
    
    context={
    'current_user':current_user,
    'form':form,
    }
    return render(request,'master_templates/super_user_manage_view.html',context)

####################################################################
###################### MEMBERS SHARES AND WELFARE ##################
####################################################################
def Shares_Deduction_savings(request):
    current_user=[]
    if not request.user.user_type == '1':
        current_user=Executives_Tasks_Model.objects.get(user=request.user.id)

    form=Shares_Deductions_savings_form(request.POST or None)
    records=SharesDeductionSavings.objects.all()

    if request.method == 'POST':
       
        savings_id=request.POST.get('transactions')
        savings=TransactionTypes.objects.get(id=savings_id)

        if SharesDeductionSavings.objects.filter(savings=savings).exists(): 
            messages.info(request,'Record Already already Exist')
           
        else:
            record=SharesDeductionSavings(savings=savings)    
            record.save()
            messages.success(request,'Record Saved Successfully')
        return HttpResponseRedirect(reverse('Shares_Deduction_savings'))
    context={
    'current_user':current_user,
    'form':form,
    'records':records,
    }
    return render(request,'master_templates/Shares_Deduction_savings.html',context)


def Shares_Deduction_savings_remove(request,pk):
    record=SharesDeductionSavings.objects.get(id=pk)
    record.delete()
    return HttpResponseRedirect(reverse('Shares_Deduction_savings'))


def AddShares_Configurations(request):
    current_user=[]
    if not request.user.user_type == '1':
        current_user=Executives_Tasks_Model.objects.get(user=request.user.id)

    form=MembersShareConfigurations_form(request.POST or None)
    form_update=MembersInitialShare_update_form(request.POST or None)

    record=[]
    if MembersShareConfigurations.objects.all().exists():
        record=MembersShareConfigurations.objects.first()
        form.fields['unit_cost'].initial=record.unit_cost

    if request.method == 'POST':
       
        unit_cost=request.POST.get('unit_cost')

        if MembersShareConfigurations.objects.all().exists(): 
            record=MembersShareConfigurations.objects.first()           
           
            record.unit_cost=unit_cost
        else:
            record=MembersShareConfigurations(unit_cost=unit_cost)    

        record.save()
        return HttpResponseRedirect(reverse('AddShares_Configurations'))
    context={
    'current_user':current_user,
    'form':form,
    'record':record,
    }
    return render(request,'master_templates/AddShares_Configurations.html',context)


def addWelfare_Configurations(request):
    current_user=[]
    if not request.user.user_type == '1':
        current_user=Executives_Tasks_Model.objects.get(user=request.user.id)

    form=MembersWelfare_form(request.POST or None)
    record=[]
    if MembersWelfare.objects.all().exists():
        record=MembersWelfare.objects.first()
        form.fields['amount'].initial=record.amount

    if request.method == 'POST':
        amount=request.POST.get('amount')

        if MembersWelfare.objects.all().exists(): 
            record=MembersShareConfigurations.objects.first()           
            record.amount=amount
        else:
            record=MembersWelfare(amount=amount)    

        record.save()
        return HttpResponseRedirect(reverse('addWelfare_Configurations'))
    context={
    'current_user':current_user,
    'form':form,
    'record':record,
    }
    return render(request,'master_templates/addWelfare_Configurations.html',context)


####################################################################
###################### COMPONENNTS PAGE ############################
####################################################################
def MembersCompulsorySavings(request):
    current_user=[]
    if not request.user.user_type == '1':
        current_user=Executives_Tasks_Model.objects.get(user=request.user.id)

    form = CompulsorySavings_form(request.POST or None)
    records = CompulsorySavings.objects.all()
    if request.method == "POST":
        transaction_id = request.POST.get('transactions')
        transaction=TransactionTypes.objects.get(id=transaction_id)

        if CompulsorySavings.objects.filter(transaction=transaction).exists():
            pass
        else:
            record=CompulsorySavings(transaction=transaction)
            record.save()

        return HttpResponseRedirect(reverse('MembersCompulsorySavings'))
    context={
    'current_user':current_user,
        'form':form,
        'records':records,
    }
    return render(request,'master_templates/MembersCompulsorySavings.html', context)


def MembersCompulsorySavings_delete(request,pk):
    record = CompulsorySavings.objects.get(id=pk)
    record.delete()
    return HttpResponseRedirect(reverse('MembersCompulsorySavings'))


def addState(request):
    current_user=[]
    if not request.user.user_type == '1':
        current_user=Executives_Tasks_Model.objects.get(user=request.user.id)

    items= States.objects.all()
    title="Add State"
    form = addStateForm(request.POST or None)
    if request.method ==  "POST":
        form = addStateForm(request.POST)
        if form.is_valid():
            title=form.cleaned_data["title"]
            record = States(title=title)
            record.save()
            messages.success(request,"Record Added Successfully")
        return	HttpResponseRedirect(reverse('addState'))
    context={
    'current_user':current_user,
    'form':form,
    'items':items,
    'url':'addState',
    'button_text':"Add State",
    'title':title,
    }
    return render(request,'master_templates/add_single_item.html', context)



def Manage_state(request):
    current_user=[]
    if not request.user.user_type == '1':
        current_user=Executives_Tasks_Model.objects.get(user=request.user.id)

    states=States.objects.all()
    context={
    'current_user':current_user,
    'states':states,
    }
    return render(request,'master_templates/manage_state.html', context)


def delete_state(request,pk):
	state=States.objects.get(id=pk)
	state.delete()
	messages.success(request,"Record Deleted Successfully")
	return HttpResponseRedirect(reverse('addState'))


def addNOKRelationships(request):
    current_user=[]
    if not request.user.user_type == '1':
        current_user=Executives_Tasks_Model.objects.get(user=request.user.id)

    items= States.objects.all()
    title="Add State"
    form = addNOKRelationshipsForm(request.POST or None)
    if request.method ==  "POST":
        form = addNOKRelationshipsForm(request.POST)
        if form.is_valid():
            title=form.cleaned_data["title"]
            record = NOKRelationships(title=title)
            record.save()
            messages.success(request,"Record Added Successfully")
            return  HttpResponseRedirect(reverse('addNOKRelationships'))
    context={
    'current_user':current_user,
    'form':form,
    'items':items,
    'url':'NOKRelationships',
    'button_text':"Add Record",
    'title':title,
    }
    return render(request,'master_templates/add_single_item.html', context)



def Manage_NOKRelationships(request):
    current_user=[]
    if not request.user.user_type == '1':
        current_user=Executives_Tasks_Model.objects.get(user=request.user.id)

    Relationships=NOKRelationships.objects.all()
    context={
    'current_user':current_user,
    'Relationships':Relationships,
    }
    return render(request,'master_templates/manage_NOKRelationships.html', context)


def Manage_NOKRelationships_Remove(request,pk):
    relationship=NOKRelationships.objects.get(id=pk)
    relationship.delete()
    return HttpResponseRedirect(reverse('Manage_NOKRelationships'))


def Manage_NOKRelationships_Max_No(request):
    current_user=[]
    if not request.user.user_type == '1':
        current_user=Executives_Tasks_Model.objects.get(user=request.user.id)

    record=[]
    if NextOfKinsMaximun.objects.all().exists:
        record = NextOfKinsMaximun.objects.first()
    
    if request.method ==  'POST':
        max_no = request.POST.get('max_no')
        if record:
            record.maximun=max_no
            record.save()
        else:
            item=NextOfKinsMaximun(maximun=max_no)
            item.save()
        return HttpResponseRedirect(reverse('admin_home'))
    
    context={
    'current_user':current_user,
    'record':record,
    }
    return render(request,'master_templates/Manage_NOKRelationships_Max_No.html',context)


def Commodity_Transaction_Period(request):
    form=Commodity_Transaction_Period_form(request.POST or None)
    records=Commodity_Period.objects.all()
    if request.method == 'POST':
        title=request.POST.get('period')
        Commodity_Period(title=title).save()
        messages.success(request,'Record Added Successfully')
        return HttpResponseRedirect(reverse('Commodity_Transaction_Period'))
    context={
    'form':form,
    'records':records,
    }
    return render(request,'master_templates/Commodity_Transaction_Period.html',context)


def Commodity_Transaction_Period_Delete(request,pk):
    record=Commodity_Period.objects.get(id=pk)
    if Company_Products.objects.filter(period=record).exists():
        messages.error(request,'This Period is already in Use')
        return HttpResponseRedirect(reverse('Commodity_Transaction_Period'))

    record.delete()
    messages.success(request,'Record Deleted Successfully')
    return HttpResponseRedirect(reverse('Commodity_Transaction_Period'))


def Commodity_Transaction_Period_Batch(request):
    form=Commodity_Transaction_Period_Batch_form(request.POST or None)
    records=Commodity_Period_Batch.objects.all()
    if request.method == 'POST':
        title=request.POST.get('batch')
        Commodity_Period_Batch(title=title).save()
        messages.success(request,'Record Added Successfully')
        return HttpResponseRedirect(reverse('Commodity_Transaction_Period_Batch'))
    context={
    'form':form,
    'records':records,
    }
    return render(request,'master_templates/Commodity_Transaction_Period_Batch.html',context)



def Commodity_Transaction_Period_Batch_Delete(request,pk):
    record=Commodity_Period_Batch.objects.get(id=pk)
    if Company_Products.objects.filter(batch=record).exists():
        messages.error(request,'This Batch is already in Use')
        return HttpResponseRedirect(reverse('Commodity_Transaction_Period_Batch'))
    record.delete()
    messages.success(request,'Record Deleted Successfully')
    return HttpResponseRedirect(reverse('Commodity_Transaction_Period_Batch'))


def addCommodityCategory(request):
    current_user=[]
    if not request.user.user_type == '1':
        current_user=Executives_Tasks_Model.objects.get(user=request.user.id)

    title="Add Commodity Category"
    items= Commodity_Categories.objects.all()
    form = addCommodityCategoryForm(request.POST or None)
    receipt_type=ReceiptTypes.objects.get(title='NONE')
    status=MembershipStatus.objects.get(title='ACTIVE')
    multiple_loan_status=MultipleLoanStatus.objects.get(title='NOT ALLOWED')
    form_print=YesNo.objects.get(title='NO')
    if request.method ==  "POST":
        
        title=request.POST.get("title")
        price_status=request.POST.get("price_status")
        transaction_id=request.POST.get('transactions')
        transaction=TransactionTypes.objects.get(id=transaction_id)
        if Commodity_Categories.objects.filter(title=title).exists():
            messages.error(request,'Record with this name already exist')
            return  HttpResponseRedirect(reverse('addCommodityCategory'))
        record = Commodity_Categories(price_status=price_status,transaction=transaction,title=title,receipt_type=receipt_type,status=status,multiple_loan_status=multiple_loan_status,form_print=form_print)
        record.save()
        messages.success(request,"Record Added Successfully")
        return  HttpResponseRedirect(reverse('addCommodityCategory'))
    
    records=Commodity_Categories.objects.all()
    context={
    'current_user':current_user,
    'form':form,
    'records':records,
    'items':items,
    'url':'addCommodityCategory',
    'button_text':"Add Record",
    'title':title,
    }
    return render(request,'master_templates/addCommodityCategory.html', context)

def Manage_Commodity_Categories_Delete(request,pk):
    record=Commodity_Categories.objects.get(id=pk)
    record.delete()
    messages.success(request,'Record Deleted Successfully')
    return  HttpResponseRedirect(reverse('addCommodityCategory'))



def Manage_Commodity_Categories_Core_properties_Transactions_Load(request):
    current_user=[]
    if not request.user.user_type == '1':
        current_user=Executives_Tasks_Model.objects.get(user=request.user.id)

    records =TransactionTypes.objects.filter(category__title='NON-MONETARY')
    context={
    'current_user':current_user,
    'records':records,
    }
    return render(request,'master_templates/Manage_Commodity_Categories_Core_properties_Transactions_Load.html',context)



def Manage_Commodity_Categories_Core_Values(request,pk):
    current_user=[]
    if not request.user.user_type == '1':
        current_user=Executives_Tasks_Model.objects.get(user=request.user.id)
    transaction =TransactionTypes.objects.get(id=pk)
    records=Commodity_Categories.objects.filter(transaction=transaction)
    
    context={
    'current_user':current_user,
    'records':records,
    }
    return render(request,'master_templates/Manage_Commodity_Categories_Core_Values.html', context)






def Manage_Commodity_Categories_Core_properties(request,pk):
    current_user=[]
    if not request.user.user_type == '1':
        current_user=Executives_Tasks_Model.objects.get(user=request.user.id)

    form = Manage_Commodity_Categories_Optional_properties_Form(request.POST or None)
    record=Commodity_Categories.objects.get(id=pk)
    if request.method == 'POST':
        interest_rate_required = request.POST.get('interest_rate_required')
        admin_charges_required = request.POST.get('admin_charges_required')
        guarantor_required = request.POST.get('guarantor_required')
        
        record.interest_rate_required=interest_rate_required
        record.admin_charges_required=admin_charges_required
        record.guarantor_required=guarantor_required

        record.save()
        return HttpResponseRedirect(reverse('Manage_Commodity_Categories_Core_Values',args=(record.transaction_id,)))
    form.fields['interest_rate_required'].initial=record.interest_rate_required
    form.fields['admin_charges_required'].initial=record.admin_charges_required
    form.fields['guarantor_required'].initial=record.guarantor_required
    context={
    'current_user':current_user,
    'form':form,
    'record':record,
    }
    return render(request,'master_templates/Manage_Commodity_Categories_Optional_properties.html', context)


def Manage_Commodity_Categories_Peripherals_Transactions_Load(request):
    current_user=[]
    if not request.user.user_type == '1':
        current_user=Executives_Tasks_Model.objects.get(user=request.user.id)

    records =TransactionTypes.objects.filter(category__title='NON-MONETARY')
    context={
    'current_user':current_user,
    'records':records,
    }
    return render(request,'master_templates/Manage_Commodity_Categories_Peripherals_Transactions_Load.html',context)


def Manage_Commodity_Categories_Peripherals(request,pk):
    current_user=[]
    if not request.user.user_type == '1':
        current_user=Executives_Tasks_Model.objects.get(user=request.user.id)
    transaction =TransactionTypes.objects.get(id=pk)
    records=Commodity_Categories.objects.filter(transaction=transaction)
    
    
    context={
    'current_user':current_user,
    'records':records,
    }
    return render(request,'master_templates/Manage_Commodity_Categories_Peripherals.html', context)



def Manage_Commodity_Categories_Update(request,pk):
    current_user=[]
    if not request.user.user_type == '1':
        current_user=Executives_Tasks_Model.objects.get(user=request.user.id)

    form = addCommodityCategoryForm(request.POST or None)
    record=Commodity_Categories.objects.get(id=pk)
    if request.method == 'POST':
        if record.interest_rate_required == '1':
            interest_deduction_id = request.POST.get('interest_deductions')
           
            interest_rate = request.POST.get('interest_rate')
            
            if interest_rate <= "0":
                messages.error(request,'Interest Rate is Missing')
                return HttpResponseRedirect(reverse('Manage_Commodity_Categories_Update',args=(pk,)))
        
        if record.admin_charges_required == '1':
            admin_charges_rating_id = request.POST.get('admin_charges_rating')
            admin_charges_rating=AdminCharges.objects.get(id=admin_charges_rating_id)

            admin_charges = request.POST.get('admin_charges')
            if admin_charges <= "0":
                messages.error(request,'Admin Charge is Missing')
                return HttpResponseRedirect(reverse('Manage_Commodity_Categories_Update',args=(pk,)))

         

          

        if record.guarantor_required == '1':
            guarantors = request.POST.get('guarantors')
            
            if guarantors <= "0":
                messages.error(request,'Guarantor is Missing')
                return HttpResponseRedirect(reverse('Manage_Commodity_Categories_Update',args=(pk,)))

        loan_age = request.POST.get('loan_age')
        if loan_age <= "0":
            messages.error(request,'Loan Age is Missing')
            return HttpResponseRedirect(reverse('Manage_Commodity_Categories_Update',args=(pk,)))


        duration = request.POST.get('duration')
        if duration <= "0":
            messages.error(request,'Duration is Missing')
            return HttpResponseRedirect(reverse('Manage_Commodity_Categories_Update',args=(pk,)))



        receipt_type_id = request.POST.get('receipt_type')
        receipt_type=ReceiptTypes.objects.get(id=receipt_type_id)
        
        price_status = request.POST.get('price_status')

        if record.interest_rate_required == '1':
            record.interest_rate=interest_rate
        
        if record.admin_charges_required == '1':
            record.admin_charges_rating=admin_charges_rating
            record.admin_charges=admin_charges
         
        
        if record.guarantor_required == '1':
            record.guarantors=guarantors
        
        record.duration=duration
        record.loan_age=loan_age
        record.receipt_type=receipt_type

        record.price_status=price_status

        record.save()
        return HttpResponseRedirect(reverse('Manage_Commodity_Categories_Peripherals',args=(record.transaction_id,)))
    form.fields['title'].initial=record.title
    form.fields['price_status'].initial=record.price_status
    form.fields['interest_rate'].initial=record.interest_rate
    form.fields['duration'].initial=record.duration
    form.fields['loan_age'].initial=record.loan_age
    form.fields['guarantors'].initial=record.guarantors
    form.fields['receipt_type'].initial=record.receipt_type_id
    form.fields['admin_charges_rating'].initial=record.admin_charges_rating_id
    form.fields['admin_charges'].initial=record.admin_charges
    
    context={
    'current_user':current_user,
    'form':form,
    'record':record,
    }
    return render(request,'master_templates/Manage_Commodity_Categories_Update.html', context)


def addGender(request):
    current_user=[]
    if not request.user.user_type == '1':
        current_user=Executives_Tasks_Model.objects.get(user=request.user.id)

    title="Add Gender"
    items= Gender.objects.all()
    form = addGenderForm(request.POST or None)
    if request.method ==  "POST":
        form = addGenderForm(request.POST)
        if form.is_valid():
            title=form.cleaned_data["title"]
            record = Gender(title=title)
            record.save()
            messages.success(request,"Record Added Successfully")
        return	HttpResponseRedirect(reverse('addGender'))
    context={
    'current_user':current_user,
    'form':form,
    'items':items,
    'url':'addGender',
    'button_text':"Add Record",
    'title':title,
    }
    return render(request,'master_templates/add_single_item.html', context)



def addSalaryInstitution(request):
    current_user=[]
    if not request.user.user_type == '1':
        current_user=Executives_Tasks_Model.objects.get(user=request.user.id)

    title="Add Salary Institution"
    items= SalaryInstitution.objects.all()
    form = addSalaryInstitutionForm(request.POST or None)
    if request.method ==  "POST":
        form = addSalaryInstitutionForm(request.POST)
        if form.is_valid():
            title=form.cleaned_data["title"]
            record = SalaryInstitution(title=title)
            record.save()
            messages.success(request,"Record Added Successfully")
        return	HttpResponseRedirect(reverse('addSalaryInstitution'))
    context={
    'current_user':current_user,
    'form':form,
    'items':items,
    'url':'addSalaryInstitution',
    'button_text':"Add Record",
    'title':title,
    }
    return render(request,'master_templates/add_single_item.html', context)


def addTitles(request):
    current_user=[]
    if not request.user.user_type == '1':
        current_user=Executives_Tasks_Model.objects.get(user=request.user.id)

    title="Add Titles"
    items= Titles.objects.all()
    form = addTitlesForm(request.POST or None)
    if request.method ==  "POST":
        form = addTitlesForm(request.POST)
        if form.is_valid():
            title=form.cleaned_data["title"]
            record = Titles(title=title)
            record.save()
            messages.success(request,"Record Added Successfully")
        return	HttpResponseRedirect(reverse('addTitles'))
    context={
    'current_user':current_user,
    'form':form,
    'items':items,
    'url':'addTitles',
    'button_text':"Add Record",
    'title':title,
    }
    return render(request,'master_templates/add_single_item.html', context)


def addDepartments(request):
    current_user=[]
    if not request.user.user_type == '1':
        current_user=Executives_Tasks_Model.objects.get(user=request.user.id)

    title="Add Departments"
    items= Departments.objects.all()
    form = addDepartmentsForm(request.POST or None)
    if request.method ==  "POST":
        form = addDepartmentsForm(request.POST)
        if form.is_valid():
            title=form.cleaned_data["title"]
            record = Departments(title=title)
            record.save()
            messages.success(request,"Record Added Successfully")
        return	HttpResponseRedirect(reverse('addDepartments'))
    context={
    'current_user':current_user,
    'form':form,
    'items':items,
    'url':'addDepartments',
    'button_text':"Add Record",
    'title':title,
    }
    return render(request,'master_templates/add_single_item.html', context)

def addBanks(request):
    current_user=[]
    if not request.user.user_type == '1':
        current_user=Executives_Tasks_Model.objects.get(user=request.user.id)

    title="Add Banks"
    items= Banks.objects.all()
    form = addBanksForm(request.POST or None)
    if request.method ==  "POST":
        form = addBanksForm(request.POST)
        if form.is_valid():
            title=form.cleaned_data["title"]
            record = Banks(title=title)
            record.save()
            messages.success(request,"Record Added Successfully")
        return	HttpResponseRedirect(reverse('addBanks'))
    context={
    'current_user':current_user,
    'form':form,
    'items':items,
    'url':'addBanks',
    'button_text':"Add Record",
    'title':title,
    }
    return render(request,'master_templates/add_single_item.html', context)

	
def addLocations(request):
    current_user=[]
    if not request.user.user_type == '1':
        current_user=Executives_Tasks_Model.objects.get(user=request.user.id)

    title="Add Locations"
    items= Locations.objects.all()
    form = addLocationsForm(request.POST or None)
    if request.method ==  "POST":
        form = addLocationsForm(request.POST)
        if form.is_valid():
            title=form.cleaned_data["title"]
            record = Locations(title=title)
            record.save()
            messages.success(request,"Record Added Successfully")
        return	HttpResponseRedirect(reverse('addLocations'))
    context={
    'current_user':current_user,
    'form':form,
    'items':items,
    'url':'addLocations',
    'button_text':"Add Record",
    'title':title,
    }
    return render(request,'master_templates/add_single_item.html', context)



def addDefaultPassword(request):
    current_user=[]
    if not request.user.user_type == '1':
        current_user=Executives_Tasks_Model.objects.get(user=request.user.id)

    title="Add Membership Status"
    item=[]
    if DefaultPassword.objects.all().exists():
        item= DefaultPassword.objects.all().first()

    form = addDefaultPasswordForm(request.POST or None)
    if request.method ==  "POST":
        form = addDefaultPasswordForm(request.POST)
        if form.is_valid():
            title=form.cleaned_data["title"]
            if DefaultPassword.objects.all().exists():
                record = DefaultPassword.objects.first()
                record.title=title
                record.save()
                messages.success(request,"Record Updated Successfully")
                return	HttpResponseRedirect(reverse('addDefaultPassword'))


            record = DefaultPassword(title=title)
            record.save()
            messages.success(request,"Record Added Successfully")
            return	HttpResponseRedirect(reverse('addDefaultPassword'))
    if item:
        form.fields['title'].initial=item.title
    context={
    'current_user':current_user,
    'form':form,
    'item':item,
    'url':'addDefaultPassword',
    'button_text':"Add Record",
    'title':title,
    }
    return render(request,'master_templates/add_single_item.html', context)



def addTransactionTypes(request):
    current_user=[]
    if not request.user.user_type == '1':
        current_user=Executives_Tasks_Model.objects.get(user=request.user.id)

    transaction_types = TransactionTypes.objects.all().order_by("code")
    form=addTransactionTypesForm(request.POST or None)
    
    if request.method=="POST":
        form = addTransactionTypesForm(request.POST)

        source_id=request.POST.get("source")
        source = TransactionSources.objects.get(id=source_id)

        share_unit_min=request.POST.get("share_unit_min")
        share_unit_max=request.POST.get("share_unit_max")
        

        code=request.POST.get("code")
        name=request.POST.get("name")
        maximum_amount=request.POST.get("maximum_amount")
        minimum_amount=request.POST.get("minimum_amount")

        receipts_obj=request.POST.get("receipts")
        receipts=ReceiptTypes.objects.get(id=receipts_obj)

        rank=request.POST.get("rank")
        form_print=YesNo.objects.get(title='NO')
        status=MembershipStatus.objects.get(title='ACTIVE')
        multiple_loan_status=MultipleLoanStatus.objects.get(title='NOT ALLOWED')
        if TransactionTypes.objects.filter(code=code).exists():
            messages.error(request,"Record with this code already exist")
            return HttpResponseRedirect(reverse('addTransactionTypes'))

        record = TransactionTypes(multiple_loan_status=multiple_loan_status,status=status,receipt_type=receipts,form_print=form_print,source=source,code=code,name=name,maximum_amount=maximum_amount,minimum_amount=minimum_amount,rank=rank,share_unit_min=share_unit_min,share_unit_max=share_unit_max)
        record.save()
        return HttpResponseRedirect(reverse('addTransactionTypes'))
    context={
    'current_user':current_user,
    'form':form,
    'transaction_types':transaction_types,
    }
    return render(request, 'master_templates/addTransactionTypes.html',context)


def TransactionTypes_Manage_Load(request):
    current_user=[]
    if not request.user.user_type == '1':
        current_user=Executives_Tasks_Model.objects.get(user=request.user.id)

    transaction_types = TransactionTypes.objects.all().order_by("code")
    
    context={
    'current_user':current_user,
 
    'transaction_types':transaction_types,
    }
    return render(request,'master_templates/TransactionTypes_Manage_Load.html',context)


def TransactionTypes_Update(request,pk):
    current_user=[]
    if not request.user.user_type == '1':
        current_user=Executives_Tasks_Model.objects.get(user=request.user.id)

    form=addTransactionTypes_update_Form(request.POST or None)
    transaction = TransactionTypes.objects.get(id=pk)
    form.fields['code'].initial=transaction.code
    form.fields['name'].initial=transaction.name
    form.fields['rank'].initial=transaction.rank
    form.fields['receipts'].initial=transaction.receipt_type.id
    form.fields['maximum_amount'].initial=transaction.maximum_amount
    form.fields['minimum_amount'].initial=transaction.minimum_amount
    form.fields['share_unit_min'].initial=transaction.share_unit_min
    form.fields['share_unit_max'].initial=transaction.share_unit_max

    if request.method == "POST":
        receipts_obj=request.POST.get('receipts')
        receipts=ReceiptTypes.objects.get(id=receipts_obj)
        code=request.POST.get('code')
        name=request.POST.get('name')
        rank=request.POST.get('rank')
        maximum_amount=request.POST.get('maximum_amount')
        minimum_amount=request.POST.get('minimum_amount')
        share_unit_min=request.POST.get('share_unit_min')
        share_unit_max=request.POST.get('share_unit_max')
        
        transaction.code=code
        transaction.name=name
        transaction.receipt_type=receipts
        transaction.rank=rank
        transaction.maximum_amount=maximum_amount
        transaction.minimum_amount=minimum_amount
        transaction.share_unit_min=share_unit_min
        transaction.share_unit_max=share_unit_max

        transaction.save()
        return HttpResponseRedirect(reverse('TransactionTypes_Manage_Load'))

    context={
    'current_user':current_user,
    'form':form,
    'transaction':transaction,
    }
    return render(request,'master_templates/TransactionTypes_Update.html',context)

def FormAutoPrint_Settings(request):
    current_user=[]
    if not request.user.user_type == '1':
        current_user=Executives_Tasks_Model.objects.get(user=request.user.id)

    form = FormAutoPrint_Settings_Form(request.POST or None)
    items = FormAutoPrints.objects.all()
    if request.method == 'POST':
        form== FormAutoPrint_Settings_Form(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('FormAutoPrint_Settings'))
    context={
    'current_user':current_user,
    'form':form,
    'items':items,
    }
    return render(request,'master_templates/FormAutoPrint_Settings.html',context)



def FormAutoPrint_SettingsUpdate(request,pk):
    current_user=[]
    if not request.user.user_type == '1':
        current_user=Executives_Tasks_Model.objects.get(user=request.user.id)

    form = FormAutoPrint_Settings_Update_Form(request.POST or None)
    item = FormAutoPrints.objects.get(id=pk)
 
    if request.method == 'POST':
        title=request.POST.get('title')
        status_id=request.POST.get('status')
        status=YesNo.objects.get(title=status_id)
      
       
        item.title=title
        item.status=status
        item.save()
        return HttpResponseRedirect(reverse('FormAutoPrint_Settings'))
    form.fields['title'].initial=item.title
    form.fields['status'].initial=item.status
    context={
    'current_user':current_user,
    'form':form,
    'items':item,
    }
    return render(request,'master_templates/FormAutoPrint_SettingsUpdate.html',context)






####################################################################
###################### LOAN RELATED MATTERS ########################
####################################################################

def loan_based_savings_update(request):
    current_user=[]
    if not request.user.user_type == '1':
        current_user=Executives_Tasks_Model.objects.get(user=request.user.id)

    saving=LoanBasedSavings.objects.first()
    form =LoanBasedSavingsForm(request.POST or None)
    if request.method=="POST":
        saving = request.POST.get('saving')
        savings=TransactionTypes.objects.get(id=saving)
        if LoanBasedSavings.objects.all().exists():
            record = LoanBasedSavings.objects.first()
            record.savings=savings
            record.save()
        else:

            record = LoanBasedSavings(savings=savings)
            record.save()
        return HttpResponseRedirect(reverse('loan_based_savings_update'))
    context={
    'current_user':current_user,
    'form':form,
    'saving':saving,
    }
    return render(request, 'master_templates/loan_based_savings.html',context)

def loan_category_settings(request):
    current_user=[]
    if not request.user.user_type == '1':
        current_user=Executives_Tasks_Model.objects.get(user=request.user.id)

    form=loan_category_settings_form(request.POST or None)
    records = TransactionTypes.objects.filter(source__title="LOAN")

    if request.method == 'POST':
        loan_id=request.POST.get('loan')
        loan=TransactionTypes.objects.get(id=loan_id)

        category_id=request.POST.get('category')
        category=LoanCategory.objects.get(id=category_id)

        loan.category=category
        loan.save()
        return HttpResponseRedirect(reverse('loan_category_settings'))
    context={
    'current_user':current_user,
    'records':records,
    'form':form,
    }
    return render(request, 'master_templates/loan_category_settings.html',context)


def loan_settings_load(request):
    current_user=[]
    if not request.user.user_type == '1':
        current_user=Executives_Tasks_Model.objects.get(user=request.user.id)

    records = TransactionTypes.objects.filter(source__title="LOAN",category__title='MONETARY')
    context={
    'current_user':current_user,
    'records':records,
    }
    return render(request, 'master_templates/loan_settings_load.html',context)


def loan_settings_details_load(request,pk):
    current_user=[]
    if not request.user.user_type == '1':
        current_user=Executives_Tasks_Model.objects.get(user=request.user.id)

    record = TransactionTypes.objects.get(id=pk)
    saving= LoanBasedSavings.objects.first()
    context={
    'current_user':current_user,
    'record':record,
    'saving':saving,
    'pk':pk,
    }
    return render(request, 'master_templates/loan_settings_details_load.html',context)




def loan_guarantors_update(request,pk):
    current_user=[]
    if not request.user.user_type == '1':
        current_user=Executives_Tasks_Model.objects.get(user=request.user.id)

    item= TransactionTypes.objects.get(id=pk)
    title="Update Loan Guarantors for " +  item.name
    instructions='''
    This page enable you to set the total number of Gaurantors 
    needed to access this loan. 
    '''
    form = loan_guarantors_update_form(request.POST or None)

    if request.method ==  "POST":
        form = loan_guarantors_update_form(request.POST)
        if form.is_valid():
            guarantors=form.cleaned_data["guarantors"]
            record = TransactionTypes.objects.get(id=pk)
            record.guarantors=guarantors
            record.save()
            messages.success(request,"Record Updated Successfully")
            return	HttpResponseRedirect(reverse('loan_settings_details_load',args=(pk,)))

    form.fields['guarantors'].initial=item.guarantors
    context={
    'current_user':current_user,
    'form':form,
    'instructions':instructions,
    'url':'loan_guarantors_update',
    'button_text':"Update Record",
    'title':title,
    }
    return render(request,'master_templates/loan_criteria_update.html', context)


def default_admin_charges_update(request,pk):
    current_user=[]
    if not request.user.user_type == '1':
        current_user=Executives_Tasks_Model.objects.get(user=request.user.id)

    item= TransactionTypes.objects.get(id=pk)
    title="Update Default Admin Charges for " +  item.name
    instructions='''
    This page enable you to set the default admin Charge, this will apply if the the laon amount
    is not greater to Minimum Loan Admin Charge for this loan. 
    '''
    form = default_admin_charges_update_form(request.POST or None)

    if request.method ==  "POST":
        form = default_admin_charges_update_form(request.POST)
        if form.is_valid():
            admin_charges=form.cleaned_data["default_admin_charges"]
            record = TransactionTypes.objects.get(id=pk)
            record.default_admin_charges=admin_charges
            record.save()
            messages.success(request,"Record Updated Successfully")
            return  HttpResponseRedirect(reverse('loan_settings_details_load',args=(pk,)))

    form.fields['default_admin_charges'].initial=item.default_admin_charges
    context={
    'current_user':current_user,
    'form':form,
    'instructions':instructions,
    'url':'default_admin_charges_update',
    'button_text':"Update Record",
    'title':title,
    }
    return render(request,'master_templates/loan_criteria_update.html', context)

    
def MultipleLoanStatus_update(request,pk):
    current_user=[]
    if not request.user.user_type == '1':
        current_user=Executives_Tasks_Model.objects.get(user=request.user.id)

    item= TransactionTypes.objects.get(id=pk)
    title="Update Default Admin Charges for " +  item.name
    instructions='''
    This page enable you to set if members are allowed to access multiple 
    fascilities for for this loan. 
    '''
    form = MultipleLoanStatus_update_form(request.POST or None)

    if request.method ==  "POST":
        form = MultipleLoanStatus_update_form(request.POST)
        if form.is_valid():
            multiple_loan_status_id=form.cleaned_data["multiple_loan_status"]
            multiple_loan_status=MultipleLoanStatus.objects.get(id=multiple_loan_status_id)
            record = TransactionTypes.objects.get(id=pk)
            record.multiple_loan_status=multiple_loan_status
            record.save()
            messages.success(request,"Record Updated Successfully")
            return  HttpResponseRedirect(reverse('loan_settings_details_load',args=(pk,)))

    form.fields['multiple_loan_status'].initial=item.multiple_loan_status
    context={
    'current_user':current_user,
    'form':form,
    'instructions':instructions,
    'url':'MultipleLoanStatus_update',
    'button_text':"Update Record",
    'title':title,
    }
    return render(request,'master_templates/loan_criteria_update.html', context)


def loan_savings_based_update(request,pk):
    current_user=[]
    if not request.user.user_type == '1':
        current_user=Executives_Tasks_Model.objects.get(user=request.user.id)

    item= TransactionTypes.objects.get(id=pk)
    title="Update Loan Savings Based for " +  item.name
    instructions='''
    This page enable you to set the percentage amout to be saved in 
    order to access a given loan.
    '''
    form = loan_savings_based_update_form(request.POST or None)

    if request.method ==  "POST":
        form = loan_savings_based_update_form(request.POST)
        if form.is_valid():
            savings_rate=form.cleaned_data["loan_savings_based"]
            record = TransactionTypes.objects.get(id=pk)
            record.savings_rate=savings_rate
            record.save()
            messages.success(request,"Record Updated Successfully")
            return  HttpResponseRedirect(reverse('loan_settings_details_load',args=(pk,)))

    form.fields['loan_savings_based'].initial=item.savings_rate
    context={
    'current_user':current_user,
    'form':form,
    'instructions':instructions,
    'url':'loan_savings_based_update',
    'button_text':"Update Record",
    'title':title,
    }
    return render(request,'master_templates/loan_criteria_update.html', context)



def loan_category_update(request,pk):
    current_user=[]
    if not request.user.user_type == '1':
        current_user=Executives_Tasks_Model.objects.get(user=request.user.id)

    item= TransactionTypes.objects.get(id=pk)
    title="Update Loan Category for " +  item.name
    instructions='''
    This page enable you to set whether a loan is monetary or Not.
    '''
    form = loan_category_update_form(request.POST or None)

    if request.method ==  "POST":
        form = loan_category_update_form(request.POST)
        if form.is_valid():
            category_id=form.cleaned_data["category"]
            category=LoanCategory.objects.get(id=category_id)
            record = TransactionTypes.objects.get(id=pk)
            record.category=category
            record.save()
            messages.success(request,"Record Updated Successfully")
            return  HttpResponseRedirect(reverse('loan_settings_details_load',args=(pk,)))

    form.fields['category'].initial=item.category
    context={
    'current_user':current_user,
    'form':form,
    'instructions':instructions,
    'url':'loan_category_update',
    'button_text':"Update Record",
    'title':title,
    }
    return render(request,'master_templates/loan_criteria_update.html', context)


def loan_duration_update(request,pk):
    current_user=[]
    if not request.user.user_type == '1':
        current_user=Executives_Tasks_Model.objects.get(user=request.user.id)

    item= TransactionTypes.objects.get(id=pk)
    title="Update Loan Duration for " +  item.name
    instructions='''
    This page enable you to set the duration of Loans.
    '''
    form = loan_duration_update_form(request.POST or None)

    if request.method ==  "POST":
        form = loan_duration_update_form(request.POST)
        if form.is_valid():
            duration=form.cleaned_data["duration"]
            record = TransactionTypes.objects.get(id=pk)
            record.duration=duration
            record.save()
            messages.success(request,"Record Updated Successfully")
            return  HttpResponseRedirect(reverse('loan_settings_details_load',args=(pk,)))

    form.fields['duration'].initial=item.duration
    context={
    'current_user':current_user,
    'form':form,
    'instructions':instructions,
    'url':'loan_duration_update',
    'button_text':"Update Record",
    'title':title,
    }
    return render(request,'master_templates/loan_criteria_update.html', context)


def loan_name_update(request,pk):
    current_user=[]
    if not request.user.user_type == '1':
        current_user=Executives_Tasks_Model.objects.get(user=request.user.id)

    item= TransactionTypes.objects.get(id=pk)
    title="Update Loan Description for " +  item.name
    instructions='''
    This page enable you to modify the Title of Loans.
    '''
    form = loan_name_update_form(request.POST or None)

    if request.method ==  "POST":
        form = loan_name_update_form(request.POST)
        if form.is_valid():
            name=form.cleaned_data["name"]
            record = TransactionTypes.objects.get(id=pk)
            record.name=name
            record.save()
            messages.success(request,"Record Updated Successfully")
            return	HttpResponseRedirect(reverse('loan_settings_details_load',args=(pk,)))

    form.fields['name'].initial=item.name
    context={
    'current_user':current_user,
    'form':form,
    'instructions':instructions,
    'url':'loan_name_update',
    'button_text':"Update Record",
    'title':title,
    }
    return render(request,'master_templates/loan_criteria_update.html', context)


def loan_interest_rate_update(request,pk):
    current_user=[]
    if not request.user.user_type == '1':
        current_user=Executives_Tasks_Model.objects.get(user=request.user.id)

    item= TransactionTypes.objects.get(id=pk)
    title="Update Loan Interest Rate  for " +  item.name
    instructions='''
    This page enable you to set the interest rate of Loans.
    '''

    form = loan_interest_rate_update_form(request.POST or None)

    if request.method ==  "POST":
        form = loan_interest_rate_update_form(request.POST)
        if form.is_valid():
            interest_rate=form.cleaned_data["interest_rate"]
            record = TransactionTypes.objects.get(id=pk)
            record.interest_rate=interest_rate
            record.save()
            messages.success(request,"Record Updated Successfully")
            return	HttpResponseRedirect(reverse('loan_settings_details_load',args=(pk,)))
    form.fields['interest_rate'].initial=item.interest_rate
    context={
    'current_user':current_user,
    'form':form,
    'instructions':instructions,
    'url':'loan_interest_rate_update',
    'button_text':"Update Record",
    'title':title,
    }
    return render(request,'master_templates/loan_criteria_update.html', context)


def loan_interest_deduction_soucrces_update(request,pk):
    current_user=[]
    if not request.user.user_type == '1':
        current_user=Executives_Tasks_Model.objects.get(user=request.user.id)

    item= TransactionTypes.objects.get(id=pk)
    title="Update Loan Interest Deduction Sources  for " +  item.name
    instructions='''
    This page enable you to set whether the interest will be deducted at source or 
    be spread out with the monthly deduction of the Loans.
    '''
    form = loan_interest_deduction_soucrces_Form(request.POST or None)

    if request.method ==  "POST":
        form = loan_interest_deduction_soucrces_Form(request.POST)
        if form.is_valid():
            source=form.cleaned_data["source"]
            interest_deduction=InterestDeductionSource.objects.get(id=source)

            record = TransactionTypes.objects.get(id=pk)
            record.interest_deduction=interest_deduction
            record.save()
            messages.success(request,"Record Updated Successfully")
            return	HttpResponseRedirect(reverse('loan_settings_details_load',args=(pk,)))

    form.fields['source'].initial=item.interest_deduction
    context={
    'current_user':current_user,
    'form':form,
    'instructions':instructions,
    'url':'loan_interest_deduction_soucrces_update',
    'button_text':"Update Record",
    'title':title,
    }
    return render(request,'master_templates/loan_criteria_update.html', context)


def loan_maximum_amount_update(request,pk):
    current_user=[]
    if not request.user.user_type == '1':
        current_user=Executives_Tasks_Model.objects.get(user=request.user.id)

    item= TransactionTypes.objects.get(id=pk)
    title="Update Loan Maximum Amount  for " +  item.name
    instructions='''
    This page enable you to set maximum amount of Loans.
    '''
    form = loan_maximum_amount_update_form(request.POST or None)

    if request.method ==  "POST":
        form = loan_maximum_amount_update_form(request.POST)
        if form.is_valid():
            maximum_amount=form.cleaned_data["maximum_amount"]
            record = TransactionTypes.objects.get(id=pk)
            record.maximum_amount=maximum_amount
            record.save()
            messages.success(request,"Record Updated Successfully")
            return	HttpResponseRedirect(reverse('loan_settings_details_load',args=(pk,)))

    form.fields['maximum_amount'].initial=item.maximum_amount
    context={
    'current_user':current_user,
    'form':form,
    'instructions':instructions,
    'url':'loan_maximum_amount_update',
    'button_text':"Update Record",
    'title':title,
    }
    return render(request,'master_templates/loan_criteria_update.html', context)


def loan_rank_update_update(request,pk):
    current_user=[]
    if not request.user.user_type == '1':
        current_user=Executives_Tasks_Model.objects.get(user=request.user.id)

    item= TransactionTypes.objects.get(id=pk)
    title="Update Loan Rank  for " +  item.name
    instructions='''
    This page enable you to set the order in which 
    monthly deduction shall flow fro the bulk deduction.
    '''

    form = loan_rank_update_form(request.POST or None)

    if request.method ==  "POST":
        form = loan_rank_update_form(request.POST)
        if form.is_valid():
            rank=form.cleaned_data["rank"]
            record = TransactionTypes.objects.get(id=pk)
            record.rank=rank
            record.save()
            messages.success(request,"Record Updated Successfully")
            return	HttpResponseRedirect(reverse('loan_settings_details_load',args=(pk,)))

    form.fields['rank'].initial=item.rank
    context={
    'current_user':current_user,
    'form':form,
    'instructions':instructions,
    'url':'loan_rank_update_update',
    'button_text':"Update Record",
    'title':title,
    }
    return render(request,'master_templates/loan_criteria_update.html', context)


def loan_admin_charges_rate_update(request,pk):
    current_user=[]
    if not request.user.user_type == '1':
        current_user=Executives_Tasks_Model.objects.get(user=request.user.id)

    item= TransactionTypes.objects.get(id=pk)
    title="Update Loan Rank  for " +  item.name
    instructions='''
    This page enable you to set whether admin charge is Cash or a 
    percentage of amount requested for loan.
    '''
    form = loan_admin_charges_rate_update_form(request.POST or None)

    if request.method ==  "POST":
        form = loan_admin_charges_rate_update_form(request.POST)
        if form.is_valid():
            admin_charge_id=form.cleaned_data["admin_charges_rating"]
            admin_charges_rating=AdminCharges.objects.get(id=admin_charge_id)
            record = TransactionTypes.objects.get(id=pk)
            record.admin_charges_rating=admin_charges_rating
            record.save()
            messages.success(request,"Record Updated Successfully")
            return	HttpResponseRedirect(reverse('loan_settings_details_load',args=(pk,)))

    form.fields['admin_charges_rating'].initial=item.admin_charges_rating
    context={
    'current_user':current_user,
    'form':form,
    'instructions':instructions,
    'url':'loan_admin_charges_rate_update',
    'button_text':"Update Record",
    'title':title,
    }
    return render(request,'master_templates/loan_criteria_update.html', context)


def loan_admin_charges_update(request,pk):
    current_user=[]
    if not request.user.user_type == '1':
        current_user=Executives_Tasks_Model.objects.get(user=request.user.id)

    item= TransactionTypes.objects.get(id=pk)
    title="Update Loan Admin Charges  for " +  item.name
    instructions='''
    This page enable you to set the percentage rating of 
    the Admin charge if it percentage based.
    '''
    form = loan_admin_charges_update_form(request.POST or None)

    if request.method ==  "POST":
        form = loan_admin_charges_update_form(request.POST)
        if form.is_valid():
            admin_charges=form.cleaned_data["admin_charges"]
            record = TransactionTypes.objects.get(id=pk)
            record.admin_charges=admin_charges
            record.save()
            messages.success(request,"Record Updated Successfully")
            return	HttpResponseRedirect(reverse('loan_settings_details_load',args=(pk,)))

    form.fields['admin_charges'].initial=item.admin_charges
    context={
    'current_user':current_user,
    'form':form,
    'instructions':instructions,
    'url':'loan_admin_charges_update',
    'button_text':"Update Record",
    'title':title,
    }
    return render(request,'master_templates/loan_criteria_update.html', context)

	

def loan_admin_charges_minimum_update(request,pk):
    current_user=[]
    if not request.user.user_type == '1':
        current_user=Executives_Tasks_Model.objects.get(user=request.user.id)

    item= TransactionTypes.objects.get(id=pk)
    title="Update Loan Admin Charges Minimum  for " +  item.name
    instructions='''
    This page enable you to set the minimum loan amount 
    upon which there would be flat rate in cash of Admin Charges. 
    '''
    form = loan_admin_charges_minimum_update_form(request.POST or None)

    if request.method ==  "POST":
        form = loan_admin_charges_minimum_update_form(request.POST)
        if form.is_valid():
            admin_charges_minimum=form.cleaned_data["admin_charges_minimum"]
            record = TransactionTypes.objects.get(id=pk)
            record.admin_charges_minimum=admin_charges_minimum
            record.save()
            messages.success(request,"Record Updated Successfully")
            return	HttpResponseRedirect(reverse('loan_settings_details_load',args=(pk,)))

    form.fields['admin_charges_minimum'].initial=item.admin_charges_minimum
    context={
    'current_user':current_user,
    'form':form,
    'instructions':instructions,
    'url':'loan_admin_charges_minimum_update',
    'button_text':"Update Record",
    'title':title,
    }
    return render(request,'master_templates/loan_criteria_update.html', context)

	
def loan_salary_relationship_update(request,pk):
    current_user=[]
    if not request.user.user_type == '1':
        current_user=Executives_Tasks_Model.objects.get(user=request.user.id)

    item= TransactionTypes.objects.get(id=pk)
    title="Update Loan Salary Loan Relationship  for " +  item.name

    instructions='''
    This page enable you to set the percentage which loans is allowed to be 
    given from the members Net Salary. 
    '''
    form = loan_salary_relationship_update_form(request.POST or None)

    if request.method ==  "POST":
        form = loan_salary_relationship_update_form(request.POST)
        if form.is_valid():
            salary_loan_relationship=form.cleaned_data["salary_loan_relationship"]
            record = TransactionTypes.objects.get(id=pk)
            record.salary_loan_relationship=salary_loan_relationship
            record.save()
            messages.success(request,"Record Updated Successfully")
            return	HttpResponseRedirect(reverse('loan_settings_details_load',args=(pk,)))

    form.fields['salary_loan_relationship'].initial=item.salary_loan_relationship
    context={
    'current_user':current_user,
    'form':form,
    'instructions':instructions,
    'url':'loan_salary_relationship_update',
    'button_text':"Update Record",
    'title':title,
    }
    return render(request,'master_templates/loan_criteria_update.html', context)


def loan_loan_age_update(request,pk):
    current_user=[]
    if not request.user.user_type == '1':
        current_user=Executives_Tasks_Model.objects.get(user=request.user.id)

    item= TransactionTypes.objects.get(id=pk)
    title="Update Loan Age  for " +  item.name
    instructions='''
    This page enable you to set the number of months one has to a member before 
    Such person can access this loan. 
    '''
    form = loan_loan_age_update_form(request.POST or None)

    if request.method ==  "POST":
        form = loan_loan_age_update_form(request.POST)
        if form.is_valid():
            loan_age=form.cleaned_data["loan_age"]
            record = TransactionTypes.objects.get(id=pk)
            record.loan_age=loan_age
            record.save()
            messages.success(request,"Record Updated Successfully")
            return	HttpResponseRedirect(reverse('loan_settings_details_load',args=(pk,)))

    form.fields['loan_age'].initial=item.loan_age
    context={
    'current_user':current_user,
    'form':form,
    'instructions':instructions,
    'url':'loan_loan_age_update',
    'button_text':"Update Record",
    'title':title,
    }
    return render(request,'master_templates/loan_criteria_update.html', context)




####################################################################
###################### NON-MONETARY LOAN SETTINGS ###################
####################################################################
def loan_settings_non_monetary_list_load(request):
    current_user=[]
    if not request.user.user_type == '1':
        current_user=Executives_Tasks_Model.objects.get(user=request.user.id)

    records = TransactionTypes.objects.filter(category__title='NON-MONETARY')
    context={
    'current_user':current_user,
    'records':records,
    }
    return render(request, 'master_templates/loan_settings_non_monetary_list_load.html',context)



def loan_settings_non_monetary_Categories_load(request,pk):
    current_user=[]
    if not request.user.user_type == '1':
        current_user=Executives_Tasks_Model.objects.get(user=request.user.id)

    records = Commodity_Categories.objects.filter(transaction_id=pk)
    context={
    'current_user':current_user,
    'records':records,
    }
    return render(request, 'master_templates/loan_settings_non_monetary_Categories_load.html',context)




def loan_settings_non_monetary_settings(request,pk):
    record = Commodity_Categories.objects.get(id=pk)
    current_user=[]
    if not request.user.user_type == '1':
        current_user=Executives_Tasks_Model.objects.get(user=request.user.id)

    context={
    'current_user':current_user,
  
    'record':record,
    }
    return render(request,'master_templates/loan_settings_non_monetary_settings.html',context)




def non_monetary_oan_guarantors_update(request,pk):
    current_user=[]
    if not request.user.user_type == '1':
        current_user=Executives_Tasks_Model.objects.get(user=request.user.id)

    item=  Commodity_Categories.objects.get(id=pk)
    title="Update Loan Guarnators for " +  item.title
    instructions='''
    This page enable you to set the total number of Gaurantors 
    needed to access this loan. 
    '''
    form = loan_guarantors_update_form(request.POST or None)

    if request.method ==  "POST":
        form = loan_guarantors_update_form(request.POST)
        if form.is_valid():
            guarantors=form.cleaned_data["guarantors"]
            record = Commodity_Categories.objects.get(id=pk)
            record.guarantors=guarantors
            record.save()
            messages.success(request,"Record Updated Successfully")
            return  HttpResponseRedirect(reverse('loan_settings_non_monetary_settings',args=(pk,)))

    form.fields['guarantors'].initial=item.guarantors
    context={
    'current_user':current_user,
    'form':form,
    'instructions':instructions,
    'url':'non_monetary_oan_guarantors_update',
    'button_text':"Update Record",
    'title':title,
    }
    return render(request,'master_templates/loan_criteria_update.html', context)


    
def Non_Monetary_MultipleLoanStatus_update(request,pk):
    current_user=[]
    if not request.user.user_type == '1':
        current_user=Executives_Tasks_Model.objects.get(user=request.user.id)

    item= Commodity_Categories.objects.get(id=pk)
    title="Update Default Admin Charges for " +  item.title
    instructions='''
    This page enable you to set if members are allowed to access multiple 
    fascilities for for this loan. 
    '''
    form = MultipleLoanStatus_update_form(request.POST or None)

    if request.method ==  "POST":
        form = MultipleLoanStatus_update_form(request.POST)
        if form.is_valid():
            multiple_loan_status_id=form.cleaned_data["multiple_loan_status"]
            multiple_loan_status=MultipleLoanStatus.objects.get(id=multiple_loan_status_id)
            record = Commodity_Categories.objects.get(id=pk)
            record.multiple_loan_status=multiple_loan_status
            record.save()
            messages.success(request,"Record Updated Successfully")
            return  HttpResponseRedirect(reverse('loan_settings_non_monetary_settings',args=(pk,)))

    form.fields['multiple_loan_status'].initial=item.multiple_loan_status
    context={
    'current_user':current_user,
    'form':form,
    'instructions':instructions,
    'url':'Non_Monetary_MultipleLoanStatus_update',
    'button_text':"Update Record",
    'title':title,
    }
    return render(request,'master_templates/loan_criteria_update.html', context)



def non_monetary_loan_duration_update(request,pk):
    current_user=[]
    if not request.user.user_type == '1':
        current_user=Executives_Tasks_Model.objects.get(user=request.user.id)

    item= Commodity_Categories.objects.get(id=pk)
    title="Update Loan Duration for " +  item.title
    instructions='''
    This page enable you to set the duration of Loans.
    '''
    form = loan_duration_update_form(request.POST or None)

    if request.method ==  "POST":
        form = loan_duration_update_form(request.POST)
        if form.is_valid():
            duration=form.cleaned_data["duration"]
            record = Commodity_Categories.objects.get(id=pk)
            record.duration=duration
            record.save()
            messages.success(request,"Record Updated Successfully")
            return  HttpResponseRedirect(reverse('loan_settings_non_monetary_settings',args=(pk,)))

    form.fields['duration'].initial=item.duration
    context={
    'current_user':current_user,
    'form':form,
    'instructions':instructions,
    'url':'non_monetary_loan_duration_update',
    'button_text':"Update Record",
    'title':title,
    }
    return render(request,'master_templates/loan_criteria_update.html', context)


def non_monetary_loan_name_update(request,pk):
    current_user=[]
    if not request.user.user_type == '1':
        current_user=Executives_Tasks_Model.objects.get(user=request.user.id)

    item= Commodity_Categories.objects.get(id=pk)
    title="Update Loan Description for " +  item.title
    instructions='''
    This page enable you to modify the Title of Loans.
    '''
    form = loan_name_update_form(request.POST or None)

    if request.method ==  "POST":
        form = loan_name_update_form(request.POST)
        if form.is_valid():
            name=form.cleaned_data["name"]
            record = Commodity_Categories.objects.get(id=pk)
            record.title=name
            record.save()
            messages.success(request,"Record Updated Successfully")
            return  HttpResponseRedirect(reverse('loan_settings_non_monetary_settings',args=(pk,)))

    form.fields['name'].initial=item.title
    context={
    'current_user':current_user,
    'form':form,
    'instructions':instructions,
    'url':'non_monetary_loan_name_update',
    'button_text':"Update Record",
    'title':title,
    }
    return render(request,'master_templates/loan_criteria_update.html', context)


def non_monetary_loan_interest_rate_update(request,pk):
    current_user=[]
    if not request.user.user_type == '1':
        current_user=Executives_Tasks_Model.objects.get(user=request.user.id)

    item= Commodity_Categories.objects.get(id=pk)
    title="Update Loan Interest Rate  for " +  item.title
    instructions='''
    This page enable you to set the interest rate of Loans.
    '''

    form = loan_interest_rate_update_form(request.POST or None)

    if request.method ==  "POST":
        form = loan_interest_rate_update_form(request.POST)
        if form.is_valid():
            interest_rate=form.cleaned_data["interest_rate"]
            record = Commodity_Categories.objects.get(id=pk)
            record.interest_rate=interest_rate
            record.save()
            messages.success(request,"Record Updated Successfully")
            return  HttpResponseRedirect(reverse('loan_settings_non_monetary_settings',args=(pk,)))
    form.fields['interest_rate'].initial=item.interest_rate
    context={
    'current_user':current_user,
    'form':form,
    'instructions':instructions,
    'url':'non_monetary_loan_interest_rate_update',
    'button_text':"Update Record",
    'title':title,
    }
    return render(request,'master_templates/loan_criteria_update.html', context)




def non_monetary_loan_admin_charges_rate_update(request,pk):
    current_user=[]
    if not request.user.user_type == '1':
        current_user=Executives_Tasks_Model.objects.get(user=request.user.id)

    item= Commodity_Categories.objects.get(id=pk)
    title="Update Loan AdminCharge Rate for " +  item.title
    instructions='''
    This page enable you to set whether admin charge is Cash or a 
    percentage of amount requested for loan.
    '''
    form = loan_admin_charges_rate_update_form(request.POST or None)

    if request.method ==  "POST":
        form = loan_admin_charges_rate_update_form(request.POST)
        if form.is_valid():
            admin_charge_id=form.cleaned_data["admin_charges_rating"]
            admin_charges_rating=AdminCharges.objects.get(id=admin_charge_id)
            record = Commodity_Categories.objects.get(id=pk)
            record.admin_charges_rating=admin_charges_rating
            record.save()
            messages.success(request,"Record Updated Successfully")
            return  HttpResponseRedirect(reverse('loan_settings_non_monetary_settings',args=(pk,)))
    if item.admin_charges_rating:
        form.fields['admin_charges_rating'].initial=item.admin_charges_rating.id
    
    context={
    'current_user':current_user,
    'form':form,
    'instructions':instructions,
    'url':'non_monetary_loan_admin_charges_rate_update',
    'button_text':"Update Record",
    'title':title,
    }
    return render(request,'master_templates/loan_criteria_update.html', context)




def non_monetary_loan_admin_charges_update(request,pk):
    current_user=[]
    if not request.user.user_type == '1':
        current_user=Executives_Tasks_Model.objects.get(user=request.user.id)

    item= Commodity_Categories.objects.get(id=pk)
    title="Update Loan Admin Charges  for " +  item.title
    instructions='''
    This page enable you to set the percentage rating of 
    the Admin charge if it percentage based.
    '''
    form = loan_admin_charges_update_form(request.POST or None)

    if request.method ==  "POST":
        form = loan_admin_charges_update_form(request.POST)
        if form.is_valid():
            admin_charges=form.cleaned_data["admin_charges"]
            record = Commodity_Categories.objects.get(id=pk)
            record.admin_charges=admin_charges
            record.save()
            messages.success(request,"Record Updated Successfully")
            return  HttpResponseRedirect(reverse('loan_settings_non_monetary_settings',args=(pk,)))

    form.fields['admin_charges'].initial=item.admin_charges
    context={
    'current_user':current_user,
    'form':form,
    'instructions':instructions,
    'url':'non_monetary_loan_admin_charges_update',
    'button_text':"Update Record",
    'title':title,
    }
    return render(request,'master_templates/loan_criteria_update.html', context)

    

def non_monetary_loan_form_print_update(request,pk):
    current_user=[]
    if not request.user.user_type == '1':
        current_user=Executives_Tasks_Model.objects.get(user=request.user.id)

    item= Commodity_Categories.objects.get(id=pk)
    title="Update Loan Form Print  for " +  item.title
    instructions='''
    This page enable you to set the minimum loan amount 
    upon which there would be flat rate in cash of Admin Charges. 
    '''
    form = loan_form_print_form(request.POST or None)

    if request.method ==  "POST":
        form = loan_form_print_form(request.POST)
        if form.is_valid():
            form_print_id=form.cleaned_data["form_print"]
            form_print=YesNo.objects.get(id=form_print_id)
            record = Commodity_Categories.objects.get(id=pk)
            record.form_print=form_print
            record.save()
            messages.success(request,"Record Updated Successfully")
            return  HttpResponseRedirect(reverse('loan_settings_non_monetary_settings',args=(pk,)))

    form.fields['form_print'].initial=item.form_print.id
    context={
    'current_user':current_user,
    'form':form,
    'instructions':instructions,
    'url':'non_monetary_loan_form_print_update',
    'button_text':"Update Record",
    'title':title,
    }
    return render(request,'master_templates/loan_criteria_update.html', context)

    
def non_monetary_loan_receipt_type_update(request,pk):
    current_user=[]
    if not request.user.user_type == '1':
        current_user=Executives_Tasks_Model.objects.get(user=request.user.id)

    item= Commodity_Categories.objects.get(id=pk)
    title="Update Loan Salary Loan Relationship  for " +  item.title

    instructions='''
    This page enable you to set the Receipt Type for Issuance. 
    '''
    form = loan_Receipt_type_update_form(request.POST or None)

    if request.method ==  "POST":
        form = loan_Receipt_type_update_form(request.POST)
        if form.is_valid():
            receipt_type_id=form.cleaned_data["receipt_type"]
            receipt_type=ReceiptTypes.objects.get(id=receipt_type_id)
            record = Commodity_Categories.objects.get(id=pk)
            record.receipt_type=receipt_type
            record.save()
            messages.success(request,"Record Updated Successfully")
            return  HttpResponseRedirect(reverse('loan_settings_non_monetary_settings',args=(pk,)))

    form.fields['receipt_type'].initial=item.receipt_type.id
    context={
    'current_user':current_user,
    'form':form,
    'instructions':instructions,
    'url':'non_monetary_loan_receipt_type_update',
    'button_text':"Update Record",
    'title':title,
    }
    return render(request,'master_templates/loan_criteria_update.html', context)


def non_monetary_loan_loan_age_update(request,pk):
    current_user=[]
    if not request.user.user_type == '1':
        current_user=Executives_Tasks_Model.objects.get(user=request.user.id)

    item= Commodity_Categories.objects.get(id=pk)
    title="Update Loan Age  for " +  item.title
    instructions='''
    This page enable you to set the number of months one has to a member before 
    Such person can access this loan. 
    '''
    form = loan_loan_age_update_form(request.POST or None)

    if request.method ==  "POST":
        form = loan_loan_age_update_form(request.POST)
        if form.is_valid():
            loan_age=form.cleaned_data["loan_age"]
            record = Commodity_Categories.objects.get(id=pk)
            record.loan_age=loan_age
            record.save()
            messages.success(request,"Record Updated Successfully")
            return  HttpResponseRedirect(reverse('loan_settings_non_monetary_settings',args=(pk,)))

    form.fields['loan_age'].initial=item.loan_age
    context={
    'current_user':current_user,
    'form':form,
    'instructions':instructions,
    'url':'non_monetary_loan_loan_age_update',
    'button_text':"Update Record",
    'title':title,
    }
    return render(request,'master_templates/loan_criteria_update.html', context)


####################################################################
###################### CUSTOMIZED COMMODITY LOAN SETTINGS ##########
####################################################################
def Customized_Commodity_Loan_Settings(request):
    current_user=[]
    if not request.user.user_type == '1':
        current_user=Executives_Tasks_Model.objects.get(user=request.user.id)

    transaction=TransactionTypes.objects.get(code='206')
    context={
    'current_user':current_user,
    'transaction':transaction,
    }
    return render(request,'master_templates/Customized_Commodity_Loan_Settings.html',context)


def Customized_loan_guarantors_update(request,pk):
    current_user=[]
    if not request.user.user_type == '1':
        current_user=Executives_Tasks_Model.objects.get(user=request.user.id)

    item= TransactionTypes.objects.get(id=pk)
    title="Update Loan Guarnators for " +  item.name
    instructions='''
    This page enable you to set the total number of Gaurantors 
    needed to access this loan. 
    '''
    form = loan_guarantors_update_form(request.POST or None)

    if request.method ==  "POST":
        form = loan_guarantors_update_form(request.POST)
        if form.is_valid():
            guarantors=form.cleaned_data["guarantors"]
            record = TransactionTypes.objects.get(id=pk)
            record.guarantors=guarantors
            record.save()
            messages.success(request,"Record Updated Successfully")
            return  HttpResponseRedirect(reverse('Customized_Commodity_Loan_Settings'))

    form.fields['guarantors'].initial=item.guarantors
    context={
    'current_user':current_user,
    'form':form,
    'instructions':instructions,
    'url':'loan_guarantors_update',
    'button_text':"Update Record",
    'title':title,
    }
    return render(request,'master_templates/loan_criteria_update.html', context)


def Customized_loan_form_print_update(request,pk):
    current_user=[]
    if not request.user.user_type == '1':
        current_user=Executives_Tasks_Model.objects.get(user=request.user.id)

    item= TransactionTypes.objects.get(id=pk)
    title="Update Loan Form Print  for " +  item.name
    instructions='''
    This page enable you to set if Form should be Printed out Automatically. 
    '''
    form = loan_form_print_form(request.POST or None)

    if request.method ==  "POST":
        form = loan_form_print_form(request.POST)
        if form.is_valid():
            form_print_id=form.cleaned_data["form_print"]
            form_print=YesNo.objects.get(id=form_print_id)
            record = TransactionTypes.objects.get(id=pk)
            record.form_print=form_print
            record.save()
            messages.success(request,"Record Updated Successfully")
            return  HttpResponseRedirect(reverse('Customized_Commodity_Loan_Settings'))

    form.fields['form_print'].initial=item.form_print.id
    context={
    'current_user':current_user,
    'form':form,
    'instructions':instructions,
    'url':'Customized__loan_form_print_update',
    'button_text':"Update Record",
    'title':title,
    }
    return render(request,'master_templates/loan_criteria_update.html', context)

def Customized_receipt_type_update(request,pk):
    current_user=[]
    if not request.user.user_type == '1':
        current_user=Executives_Tasks_Model.objects.get(user=request.user.id)

    item= TransactionTypes.objects.get(id=pk)
    title="Update Receipt Type for " +  item.name
    instructions='''
    This page enable you to set the Receipt Type. 
    '''
    form = loan_Receipt_type_update_form(request.POST or None)

    if request.method ==  "POST":
        form = loan_Receipt_type_update_form(request.POST)
        if form.is_valid():
            receipt_type_id=form.cleaned_data["receipt_type"]
            receipt_type=ReceiptTypes.objects.get(id=receipt_type_id)
            record = TransactionTypes.objects.get(id=pk)
            record.receipt_type=receipt_type
            record.save()
            messages.success(request,"Record Updated Successfully")
            return  HttpResponseRedirect(reverse('Customized_Commodity_Loan_Settings'))

    form.fields['receipt_type'].initial=item.receipt_type
    context={
    'current_user':current_user,
    'form':form,
    'instructions':instructions,
    'url':'Customized_receipt_type_update',
    'button_text':"Update Record",
    'title':title,
    }
    return render(request,'master_templates/loan_criteria_update.html', context)

  


def Customized_loan_category_update(request,pk):
    current_user=[]
    if not request.user.user_type == '1':
        current_user=Executives_Tasks_Model.objects.get(user=request.user.id)

    item= TransactionTypes.objects.get(id=pk)
    title="Update Loan Category for " +  item.name
    instructions='''
    This page enable you to set whether a loan is monetary or Not.
    '''
    form = loan_category_update_form(request.POST or None)

    if request.method ==  "POST":
        form = loan_category_update_form(request.POST)
        if form.is_valid():
            category_id=form.cleaned_data["category"]
            category=LoanCategory.objects.get(id=category_id)
            record = TransactionTypes.objects.get(id=pk)
            record.category=category
            record.save()
            messages.success(request,"Record Updated Successfully")
            return  HttpResponseRedirect(reverse('Customized_Commodity_Loan_Settings'))

    form.fields['category'].initial=item.category
    context={
    'current_user':current_user,
    'form':form,
    'instructions':instructions,
    'url':'loan_category_update',
    'button_text':"Update Record",
    'title':title,
    }
    return render(request,'master_templates/loan_criteria_update.html', context)


def Customized_loan_duration_update(request,pk):
    current_user=[]
    if not request.user.user_type == '1':
        current_user=Executives_Tasks_Model.objects.get(user=request.user.id)

    item= TransactionTypes.objects.get(id=pk)
    title="Update Loan Duration for " +  item.name
    instructions='''
    This page enable you to set the duration of Loans.
    '''
    form = loan_duration_update_form(request.POST or None)

    if request.method ==  "POST":
        form = loan_duration_update_form(request.POST)
        if form.is_valid():
            duration=form.cleaned_data["duration"]
            record = TransactionTypes.objects.get(id=pk)
            record.duration=duration
            record.save()
            messages.success(request,"Record Updated Successfully")
            return  HttpResponseRedirect(reverse('Customized_Commodity_Loan_Settings'))

    form.fields['duration'].initial=item.duration
    context={
    'current_user':current_user,
    'form':form,
    'instructions':instructions,
    'url':'loan_duration_update',
    'button_text':"Update Record",
    'title':title,
    }
    return render(request,'master_templates/loan_criteria_update.html', context)


def Customized_loan_name_update(request,pk):
    current_user=[]
    if not request.user.user_type == '1':
        current_user=Executives_Tasks_Model.objects.get(user=request.user.id)

    item= TransactionTypes.objects.get(id=pk)
    title="Update Loan Description for " +  item.name
    instructions='''
    This page enable you to modify the Title of Loans.
    '''
    form = loan_name_update_form(request.POST or None)

    if request.method ==  "POST":
        form = loan_name_update_form(request.POST)
        if form.is_valid():
            name=form.cleaned_data["name"]
            record = TransactionTypes.objects.get(id=pk)
            record.name=name
            record.save()
            messages.success(request,"Record Updated Successfully")
            return  HttpResponseRedirect(reverse('Customized_Commodity_Loan_Settings'))

    form.fields['name'].initial=item.name
    context={
    'current_user':current_user,
    'form':form,
    'instructions':instructions,
    'url':'loan_name_update',
    'button_text':"Update Record",
    'title':title,
    }
    return render(request,'master_templates/loan_criteria_update.html', context)


def Customized_loan_interest_rate_update(request,pk):
    current_user=[]
    if not request.user.user_type == '1':
        current_user=Executives_Tasks_Model.objects.get(user=request.user.id)

    item= TransactionTypes.objects.get(id=pk)
    title="Update Loan Interest Rate  for " +  item.name
    instructions='''
    This page enable you to set the interest rate of Loans.
    '''

    form = loan_interest_rate_update_form(request.POST or None)

    if request.method ==  "POST":
        form = loan_interest_rate_update_form(request.POST)
        if form.is_valid():
            interest_rate=form.cleaned_data["interest_rate"]
            record = TransactionTypes.objects.get(id=pk)
            record.interest_rate=interest_rate
            record.save()
            messages.success(request,"Record Updated Successfully")
            return  HttpResponseRedirect(reverse('Customized_Commodity_Loan_Settings'))
    form.fields['interest_rate'].initial=item.interest_rate
    context={
    'current_user':current_user,
    'form':form,
    'instructions':instructions,
    'url':'loan_interest_rate_update',
    'button_text':"Update Record",
    'title':title,
    }
    return render(request,'master_templates/loan_criteria_update.html', context)



def Customized_loan_rank_update_update(request,pk):
    current_user=[]
    if not request.user.user_type == '1':
        current_user=Executives_Tasks_Model.objects.get(user=request.user.id)

    item= TransactionTypes.objects.get(id=pk)
    title="Update Loan Rank  for " +  item.name
    instructions='''
    This page enable you to set the order in which 
    monthly deduction shall flow fro the bulk deduction.
    '''

    form = loan_rank_update_form(request.POST or None)

    if request.method ==  "POST":
        form = loan_rank_update_form(request.POST)
        if form.is_valid():
            rank=form.cleaned_data["rank"]
            record = TransactionTypes.objects.get(id=pk)
            record.rank=rank
            record.save()
            messages.success(request,"Record Updated Successfully")
            return  HttpResponseRedirect(reverse('Customized_Commodity_Loan_Settings'))

    form.fields['rank'].initial=item.rank
    context={
    'current_user':current_user,
    'form':form,
    'instructions':instructions,
    'url':'loan_rank_update_update',
    'button_text':"Update Record",
    'title':title,
    }
    return render(request,'master_templates/loan_criteria_update.html', context)


def Customized_loan_admin_charges_rate_update(request,pk):
    current_user=[]
    if not request.user.user_type == '1':
        current_user=Executives_Tasks_Model.objects.get(user=request.user.id)

    item= TransactionTypes.objects.get(id=pk)
    title="Update Loan Rank  for " +  item.name
    instructions='''
    This page enable you to set whether admin charge is Cash or a 
    percentage of amount requested for loan.
    '''
    form = loan_admin_charges_rate_update_form(request.POST or None)

    if request.method ==  "POST":
        form = loan_admin_charges_rate_update_form(request.POST)
        if form.is_valid():
            admin_charge_id=form.cleaned_data["admin_charges_rating"]
            admin_charges_rating=AdminCharges.objects.get(id=admin_charge_id)
            record = TransactionTypes.objects.get(id=pk)
            record.admin_charges_rating=admin_charges_rating
            record.save()
            messages.success(request,"Record Updated Successfully")
            return  HttpResponseRedirect(reverse('Customized_Commodity_Loan_Settings'))

    form.fields['admin_charges_rating'].initial=item.admin_charges_rating
    context={
    'current_user':current_user,
    'form':form,
    'instructions':instructions,
    'url':'loan_admin_charges_rate_update',
    'button_text':"Update Record",
    'title':title,
    }
    return render(request,'master_templates/loan_criteria_update.html', context)


def Customized_loan_admin_charges_update(request,pk):
    current_user=[]
    if not request.user.user_type == '1':
        current_user=Executives_Tasks_Model.objects.get(user=request.user.id)

    item= TransactionTypes.objects.get(id=pk)
    title="Update Loan Admin Charges  for " +  item.name
    instructions='''
    This page enable you to set the percentage rating of 
    the Admin charge if it percentage based.
    '''
    form = loan_admin_charges_update_form(request.POST or None)

    if request.method ==  "POST":
        form = loan_admin_charges_update_form(request.POST)
        if form.is_valid():
            admin_charges=form.cleaned_data["admin_charges"]
            record = TransactionTypes.objects.get(id=pk)
            record.admin_charges=admin_charges
            record.save()
            messages.success(request,"Record Updated Successfully")
            return  HttpResponseRedirect(reverse('Customized_Commodity_Loan_Settings'))

    form.fields['admin_charges'].initial=item.admin_charges
    context={
    'current_user':current_user,
    'form':form,
    'instructions':instructions,
    'url':'loan_admin_charges_update',
    'button_text':"Update Record",
    'title':title,
    }
    return render(request,'master_templates/loan_criteria_update.html', context)

    
def Customized_loan_loan_age_update(request,pk):
    current_user=[]
    if not request.user.user_type == '1':
        current_user=Executives_Tasks_Model.objects.get(user=request.user.id)

    item= TransactionTypes.objects.get(id=pk)
    title="Update Loan Age  for " +  item.name
    instructions='''
    This page enable you to set the number of months one has to a member before 
    Such person can access this loan. 
    '''
    form = loan_loan_age_update_form(request.POST or None)

    if request.method ==  "POST":
        form = loan_loan_age_update_form(request.POST)
        if form.is_valid():
            loan_age=form.cleaned_data["loan_age"]
            record = TransactionTypes.objects.get(id=pk)
            record.loan_age=loan_age
            record.save()
            messages.success(request,"Record Updated Successfully")
            return  HttpResponseRedirect(reverse('Customized_Commodity_Loan_Settings'))

    form.fields['loan_age'].initial=item.loan_age
    context={
    'current_user':current_user,
    'form':form,
    'instructions':instructions,
    'url':'loan_loan_age_update',
    'button_text':"Update Record",
    'title':title,
    }
    return render(request,'master_templates/loan_criteria_update.html', context)


####################################################################
###################### APPROVABLE TRANSACTION ######################
####################################################################


	
def membership_price_settings_load(request):
    current_user=[]
    if not request.user.user_type == '1':
        current_user=Executives_Tasks_Model.objects.get(user=request.user.id)

    transaction=TransactionTypes.objects.get(code='100')
    title="Membership Registration"
    title1="Membership Registration Charges"

    form=membership_price_settings_form(request.POST or None)
    form.fields['admin_charges'].initial=transaction.admin_charges
    if request.method ==  "POST":

        form = membership_price_settings_form(request.POST)
        if form.is_valid():
            admin_charges=form.cleaned_data['admin_charges']
            transaction.admin_charges=admin_charges
            transaction.save()
            messages.success(request,"Record Updated Successfully")
        return	HttpResponseRedirect(reverse('membership_price_settings_load'))

    context={
    'current_user':current_user,
    'form':form,
    # 'pk':pk,
    'transaction':transaction,
    'url':'membership_price_settings_update',
    'button_text':"Add Record",
    'title':title,
    'title1':title1,
    }
    return render(request,'master_templates/membership_price_settings_update.html', context)


####################################################################
###################### RECEIPT AND ID MANAGER ######################
####################################################################

def AutoReceipt_Setup(request):
    current_user=[]
    if not request.user.user_type == '1':
        current_user=Executives_Tasks_Model.objects.get(user=request.user.id)

    record=[]
    if AutoReceipt.objects.all().exists():
        record=AutoReceipt.objects.first()

    if request.method=="POST":
        receipt=request.POST.get("receipt")
        if AutoReceipt.objects.all().exists():
            record=AutoReceipt.objects.first()
            record.receipt=receipt
            record.save()
        else:
            record=AutoReceipt(receipt=receipt)
            record.save()
        return HttpResponseRedirect(reverse('AutoReceipt_Setup'))
    context={
    'current_user':current_user,
    'record':record,
    }
    return render(request,'master_templates/AutoReceipt_Setup.html',context)



def receipt_manager(request):
    current_user=[]
    if not request.user.user_type == '1':
        current_user=Executives_Tasks_Model.objects.get(user=request.user.id)

    form = receipt_manager_form(request.POST or None)
    receipts=Receipts.objects.all()
    if request.method=="POST":
        status=ReceiptStatus.objects.get(title='UNUSED')
        start_point = request.POST.get('start_point')
        stop_point = request.POST.get('stop_point')

        for i in  range(int(start_point),int(stop_point)+1): 
            record=Receipts(status=status,receipt=str(i).zfill(5))
            record.save()
        return HttpResponseRedirect(reverse('receipt_manager'))
    context={
    'current_user':current_user,
    'form':form,
    'receipts':receipts,
    }
    return render(request,'master_templates/receipt_manager.html',context)


def receipt_manager_shop(request):
    current_user=[]
    if not request.user.user_type == '1':
        current_user=Executives_Tasks_Model.objects.get(user=request.user.id)

    form = receipt_manager_form(request.POST or None)
    receipts=Receipts_Shop.objects.all()
    if request.method=="POST":
        status=ReceiptStatus.objects.get(title='UNUSED')
        start_point = request.POST.get('start_point')
        stop_point = request.POST.get('stop_point')
        
        for i in  range(int(start_point),int(stop_point)+1): 
            record=Receipts_Shop(status=status,receipt=str(i).zfill(5))
            record.save()
        return HttpResponseRedirect(reverse('receipt_manager_shop'))
    context={
    'current_user':current_user,
    'form':form,
    'receipts':receipts,
    }
    return render(request,'master_templates/receipt_manager_shop.html',context)


def Members_IdManager(request):
    current_user=[]
    if not request.user.user_type == '1':
        current_user=Executives_Tasks_Model.objects.get(user=request.user.id)

    form=MembersIdManager_form(request.POST or None)
    if MembersIdManager.objects.all().exists():
        record_exist = MembersIdManager.objects.first()
        form.fields['prefix_title'].initial=record_exist.prefix_title
        form.fields['prefix_year'].initial=record_exist.prefix_year
        form.fields['member_id'].initial=record_exist.member_id

    if request.method=="POST":
        prefix_title= request.POST.get('prefix_title')
        prefix_year= request.POST.get('prefix_year')
        member_id= request.POST.get('member_id')

        if MembersIdManager.objects.all().exists():
            record=MembersIdManager.objects.first()
            record.prefix_title=prefix_title
            record.prefix_year=prefix_year
            record.member_id=member_id.zfill(5)
            record.save()
            messages.success(request,"Record Updated Successfully")
            return HttpResponseRedirect(reverse('Members_IdManager'))

        record=MembersIdManager(prefix_title=prefix_title,prefix_year=prefix_year,member_id=member_id.zfill(5))
        record.save()
        messages.success(request,"Record Updated Successfully")
        return HttpResponseRedirect(reverse('Members_IdManager'))

    context={
    'current_user':current_user,
    'form':form,
    }
    return render(request,'master_templates/MembersIdManager.html',context)


def SharesUnits_add(request):
    current_user=[]
    if not request.user.user_type == '1':
        current_user=Executives_Tasks_Model.objects.get(user=request.user.id)

    items=SharesUnits.objects.all()
    if request.method=="POST":

        unit = request.POST.get('unit')
        if SharesUnits.objects.filter(unit=unit).exists():
            messages.error(request,"Record Already Exist")
        else:
            record=SharesUnits(unit=unit)
            record.save()
            messages.success(request,"Record Added Successfully")
        return HttpResponseRedirect(reverse('SharesUnits_add'))
    context={
    'current_user':current_user,
    'items':items,
    }
    return render(request,'master_templates/SharesUnits_add.html',context)


def Loan_Number_Manager(request):
    current_user=[]
    if not request.user.user_type == '1':
        current_user=Executives_Tasks_Model.objects.get(user=request.user.id)

    form=Loan_Number_Manager_form(request.POST or None)
    if LoanNumber.objects.all().count()>0:
        item=LoanNumber.objects.first()
        form.fields['code'].initial=item.code


    if request.method=="POST":
        code=request.POST.get('code')

        if LoanNumber.objects.all().count()>0:
            record=LoanNumber.objects.first()
            record.code=code
            record.save()

        else:
            record=LoanNumber(code=code)
            record.save()
        return HttpResponseRedirect(reverse('Loan_Number_Manager'))

    context={
    'current_user':current_user,
    'form':form,
    }
    return render(request,'master_templates/Loan_Number_Manager.html',context)

#######################################################################
################## COOPERATIVE ACCOUNTS ################################
#######################################################################
def CooperativeBankAccounts_add(request):
    current_user=[]
    if not request.user.user_type == '1':
        current_user=Executives_Tasks_Model.objects.get(user=request.user.id)

    form=CooperativeBankAccounts_form(request.POST or None)
    banks=CooperativeBankAccounts.objects.all()
    if request.method == 'POST':
        bank_id=request.POST.get('bank')
        bank=Banks.objects.get(id=bank_id)

        account_type_id=request.POST.get('account_type')
        account_type=AccountTypes.objects.get(id=account_type_id)

        account_name=request.POST.get('account_name')
        account_number=request.POST.get('account_number')

        if CooperativeBankAccounts.objects.filter(bank=bank,account_number=account_number).exists():
            messages.error(request,'This account Number is already in Use')
            return HttpResponseRedirect(reverse('CooperativeBankAccounts_add'))

        record=CooperativeBankAccounts(bank=bank,account_type=account_type,account_name=account_name,account_number=account_number)
        record.save()

        messages.success(request,"Record Added Successfully")
        return HttpResponseRedirect(reverse('CooperativeBankAccounts_add'))

    context={
    'current_user':current_user,
    'form':form,
    'banks':banks,
    }
    return render(request,'master_templates/CooperativeBankAccounts_add.html',context)


def CooperativeBankAccounts_Remove(request,pk):
    record=CooperativeBankAccounts.objects.get(id=pk)
    record.delete()
    return HttpResponseRedirect(reverse('CooperativeBankAccounts_add'))


def CooperativeBankAccounts_Update(request,pk):
    current_user=[]
    if not request.user.user_type == '1':
        current_user=Executives_Tasks_Model.objects.get(user=request.user.id)

    form=CooperativeBankAccounts_form(request.POST or None)
    record=CooperativeBankAccounts.objects.get(id=pk)

    form.fields['account_name'].initial=record.account_name
    form.fields['account_number'].initial=record.account_number
    form.fields['bank'].initial=record.bank.id
    form.fields['account_type'].initial=record.account_type.id
    if request.method=="POST":
        bank_id=request.POST.get('bank')
        bank=Banks.objects.get(id=bank_id)

        account_type_id = request.POST.get('account_type')
        account_type=AccountTypes.objects.get(id=account_type_id)

        account_name=request.POST.get('account_name')
        account_number=request.POST.get('account_number')

        record.bank=bank
        record.account_type=account_type
        record.account_name=account_name
        record.account_number=account_number
        record.save()
        return HttpResponseRedirect(reverse('CooperativeBankAccounts_add'))
    context={
    'current_user':current_user,
    'form':form,
    }
    return render(request,'master_templates/CooperativeBankAccounts_Update.html',context)

#######################################################################
################## WITHDRAWAL CONTROLLER ##############################
#######################################################################



def WithdrawalController_add(request):
    current_user=[]
    if not request.user.user_type == '1':
        current_user=Executives_Tasks_Model.objects.get(user=request.user.id)

    form=WithdrawalController_form(request.POST or None)
    if request.method=="POST":
        status=WithdrawalStatus.objects.get(title='LOCKED')
        transaction_id=request.POST.get('transactions')
        transaction=TransactionTypes.objects.get(id=transaction_id)

        maturity=request.POST.get('maturity')
        record=WithdrawableTransactions(status=status,transaction=transaction,maturity=maturity)
        record.save()
        messages.success(request,'Tranaction Successfully Completed')
        return HttpResponseRedirect(reverse('WithdrawalController_add'))
    context={
    'current_user':current_user,
    'form':form,
    }
    return render(request,'master_templates/WithdrawalController_add.html',context)


def WithdrawalController(request):
    current_user=[]
    if not request.user.user_type == '1':
        current_user=Executives_Tasks_Model.objects.get(user=request.user.id)

    transactions=WithdrawableTransactions.objects.all()
    context={
    'current_user':current_user,
    'transactions':transactions,
    }
    return render(request,'master_templates/WithdrawalController.html',context)


def WithdrawalController_View(request,pk):
    current_user=[]
    if not request.user.user_type == '1':
        current_user=Executives_Tasks_Model.objects.get(user=request.user.id)

    form=WithdrawalController_update_form(request.POST or None)
    transaction=WithdrawableTransactions.objects.get(id=pk)

    if request.method=="POST":
        status_id=request.POST.get('status')
        status=WithdrawalStatus.objects.get(id=status_id)
        maturity=request.POST.get('maturity')

        transaction.maturity=maturity
        transaction.status=status
        transaction.save()
        return HttpResponseRedirect(reverse('WithdrawalController'))

    form.fields['maturity'].initial=transaction.maturity
    form.fields['status'].initial=transaction.status.id
    context={
    'current_user':current_user,
    'transaction':transaction,
    'form':form,
    }
    return render(request,'master_templates/WithdrawalController_View.html',context)






def WithdrawalController_Process(request,pk):
    status1=WithdrawalStatus.objects.get(title='LOCKED')
    status2=WithdrawalStatus.objects.get(title='UNLOCKED')
    transaction=TransactionTypes.objects.get(id=pk)
    if transaction.withdrawal_status.title =='LOCKED':
        transaction.withdrawal_status=status2
    else:
        transaction.withdrawal_status=status1
    transaction.save()
    return HttpResponseRedirect(reverse('WithdrawalController'))

#######################################################################
############################ SHOP #####################################
#######################################################################
def CustomerID_Manager(request):
    current_user=[]
    if not request.user.user_type == '1':
        current_user=Executives_Tasks_Model.objects.get(user=request.user.id)

    form=CustomerID_Manager_form(request.POST or None)
    item=[]
    if CustomerID.objects.all().exists():
        item=CustomerID.objects.first()
        form.fields['code'].initial=item.title
        
    if request.method=="POST":
        code=request.POST.get('code')
        if CustomerID.objects.all().exists():
            record=CustomerID.objects.first()
            record.title=code
           
        else:
            record=CustomerID(title=code)
        record.save()
        return HttpResponseRedirect(reverse('CustomerID_Manager'))
    context={
    'current_user':current_user,
    'form':form,
    }
    return render(request,'master_templates/CustomerID_Manager.html',context)



#######################################################################
################## PRESIDENT VIEWS  ##################################
#######################################################################
def membership_request_approvals_list_load(request):
    current_user=[]
    if not request.user.user_type == '1':
        current_user=Executives_Tasks_Model.objects.get(user=request.user.id)

    submission_status=SubmissionStatus.objects.get(title='SUBMITTED')
    approval_status=ApprovalStatus.objects.get(title='PENDING')
    applicants=MemberShipRequest.objects.filter(submission_status=submission_status,approval_status=approval_status)
    context={
    'current_user':current_user,
    'applicants':applicants,
    }
    return render(request,'master_templates/membership_request_approvals_list_load.html',context)


def membership_request_approval_info(request,pk):
    current_user=[]
    if not request.user.user_type == '1':
        current_user=Executives_Tasks_Model.objects.get(user=request.user.id)

    form_comment=MemberShipRequest_approval_comment_form(request.POST or None)
    form_attachment=MemberShipRequest_approval_attachment_form(request.POST or None)
    applicant=MemberShipRequest.objects.get(id=pk)
    officer=CustomUser.objects.get(id=request.user.id)

    existing_infos = MemberShipRequestAdditionalInfo.objects.filter(applicant_id=pk).exclude(officer=officer)
    existing_attachments = MemberShipRequestAdditionalAttachment.objects.filter(applicant_id=pk).exclude(officer=officer)
    approval_comments = MemberShipRequestAdditionalInfo.objects.filter(applicant_id=pk,officer=officer)
    approval_attachments = MemberShipRequestAdditionalAttachment.objects.filter(applicant_id=pk,officer=officer)

    
    context={
    'applicant':applicant,
    'current_user':current_user,
    'form_comment':form_comment,
    'form_attachment':form_attachment,
    'pk':pk,
    'existing_infos':existing_infos,
    'existing_attachments':existing_attachments,
    'approval_comments':approval_comments,
    'approval_attachments':approval_attachments,
    }
    return render(request,'master_templates/membership_request_approval_info.html',context)


def membership_request_approval_info_delete(request,pk):
    record= MemberShipRequestAdditionalInfo.objects.get(id=pk)
    return_pk=record.applicant_id
    record.delete()
    return HttpResponseRedirect(reverse('membership_request_approval_info',args=(return_pk,)))


def membership_request_approval_comment_save(request,pk):
    applicant=MemberShipRequest.objects.get(id=pk)
    officer=CustomUser.objects.get(id=request.user.id)
    if request.method=="POST" and 'btn_info' in request.POST:
        comment=request.POST.get('comment')
    
        record=MemberShipRequestAdditionalInfo(applicant=applicant,comment=comment,officer=officer)
        record.save()
        return HttpResponseRedirect(reverse('membership_request_approval_info',args=(pk,)))



def membership_request_approval_attachment_save(request,pk):
    applicant=MemberShipRequest.objects.get(id=pk)
    officer=CustomUser.objects.get(id=request.user.id)

    if request.method=="POST" and 'btn_attachment' in request.POST:
        attachment_form=MemberShipRequest_approval_attachment_form(request.POST)
        caption=request.POST.get('caption')
        
        
        if request.FILES.get('image', False):
            image = request.FILES['image']
            fs=FileSystemStorage()
            filename=fs.save(image.name,image)
            image_url=fs.url(filename)
    
        else:
            image_url=None

        record=MemberShipRequestAdditionalAttachment(image=image_url,applicant=applicant,caption=caption,officer=officer)
        record.save()
        return HttpResponseRedirect(reverse('membership_request_approval_info',args=(pk,)))


def membership_request_approval_attachment_delete(request,pk):
    record= MemberShipRequestAdditionalAttachment.objects.get(id=pk)
    return_pk=record.applicant_id
    record.delete()
    return HttpResponseRedirect(reverse('membership_request_approval_info',args=(return_pk,)))



def MemberShipRequest_approval_submit(request,pk):
    current_user=[]
    if not request.user.user_type == '1':
        current_user=Executives_Tasks_Model.objects.get(user=request.user.id)

    form=MemberShipRequest_approval_submit_form(request.POST or None)
    
    if request.method=="POST":
        approval_status_id=request.POST.get('approval_status')
        approval_status=ApprovalStatus.objects.get(id=approval_status_id)

        record = MemberShipRequest.objects.get(id=pk)
        
        record.approval_status=approval_status
        record.approved_date=datetime.date.today()
        record.save()
        return HttpResponseRedirect(reverse('membership_request_approvals_list_load'))
    context={
    'current_user':current_user,
    'form':form,
    }
    return render(request,'master_templates/MemberShipRequest_approval_submit.html',context)


def loan_request_approval_list_load(request):
    current_user=[]
    if not request.user.user_type == '1':
        current_user=Executives_Tasks_Model.objects.get(user=request.user.id)
    # return HttpResponse(current_user.cash_withdrawal_approval)
    
    approval_status=ApprovalStatus.objects.get(title='PENDING')
    transaction_status=TransactionStatus.objects.get(title='UNTREATED')
    
    applicants=LoanRequest.objects.filter(approval_status=approval_status,transaction_status=transaction_status)

    context={
    'current_user':current_user,
    'applicants':applicants,
    }
    return render(request,'master_templates/loan_request_approval_list_load.html',context)


def Loan_request_approval_details(request,pk):
    current_user=[]
    if not request.user.user_type == '1':
        current_user=Executives_Tasks_Model.objects.get(user=request.user.id)

    loan_comment=LoanRequest.objects.get(id=pk)
    loan_analysis=LoanRequestSettings.objects.filter(applicant_id=pk,category='ANALYSIS')
    loan_summary=LoanRequestSettings.objects.filter(applicant_id=pk,category='SUMMARY')
    

    approval_status=ApprovalStatus.objects.all()
    


    if request.method=='POST':
        approval_officer=CustomUser.objects.get(id=request.user.id)
        comment=request.POST.get('comment')
        approved_amount=request.POST.get('amount')

        if float(approved_amount)<=0:
            messages.info(request,"Amount approved cannot be less than or equal to Zero(0)")
            return HttpResponseRedirect(reverse('Loan_request_approval_details', args=(pk,)))
        
        if float(loan_comment.loan_amount) < float(approved_amount):
            messages.info(request,"Amount approved cannot be more than applied Amount")
            return HttpResponseRedirect(reverse('Loan_request_approval_details', args=(pk,)))

        status_id=request.POST.get('status')
        status=ApprovalStatus.objects.get(id=status_id)

        approved_date= get_current_date(now)


        loan_comment.approval_status=status
        loan_comment.approval_comment=comment
        loan_comment.approval_date=approved_date
        loan_comment.approval_officer=approval_officer
        loan_comment.approved_amount=approved_amount
        loan_comment.save()
    
        return HttpResponseRedirect(reverse('loan_request_approval_list_load'))
        
    form=MemberShipRequestAdditionalInfo_form(request.POST or None)
    context={
    'current_user':current_user,
    'loan_analysis':loan_analysis,
    'loan_summary':loan_summary,
    'pk':pk,
    'form':form,
    'loan_comment':loan_comment,
    'approval_status':approval_status,
    }
    return render(request,'master_templates/Loan_request_approval_details.html',context)


def loan_application_approval_list_load(request):
    current_user=[]
    if not request.user.user_type == '1':
        current_user=Executives_Tasks_Model.objects.get(user=request.user.id)

    certification_status=CertificationStatus.objects.get(title='CERTIFIED')
    approval_status=ApprovalStatus.objects.get(title='PENDING')
    
    applicants=LoanApplication.objects.filter(approval_status=approval_status,certification_status=certification_status,approval_officer__officer_id=current_user)

    context={
    'current_user':current_user,
    'applicants':applicants,
    }
    return render(request,'master_templates/loan_application_approval_list_load.html',context)


def Loan_application_approval_details(request,pk):
    current_user=[]
    if not request.user.user_type == '1':
        current_user=Executives_Tasks_Model.objects.get(user=request.user.id)

    loan_comment=LoanApplication.objects.get(id=pk)
    loan_analysis=LoanApplicationSettings.objects.filter(applicant_id=pk,category='ANALYSIS')
    loan_summary=LoanApplicationSettings.objects.filter(applicant_id=pk,category='SUMMARY')
    approval_status=ApprovalStatus.objects.all()
    


    if request.method=='POST':

        comment=request.POST.get('comment')
        approved_amount=request.POST.get('amount')
        if float(loan_comment.loan_amount) < float(approved_amount):
            messages.success(request,"Amount approved cannot be more than applied Amount")
            return HttpResponseRedirect(reverse('Loan_request_approval_details', args=(pk,)))

        status_id=request.POST.get('status')
        status=ApprovalStatus.objects.get(id=status_id)

        approved_date= datetime.datetime.now()


        loan_comment.approval_status=status
        loan_comment.approval_comment=comment
        loan_comment.approval_date=approved_date
        loan_comment.approved_amount=approved_amount
        loan_comment.save()
    
        return HttpResponseRedirect(reverse('loan_application_approval_list_load'))

    context={
    'current_user':current_user,
    'loan_analysis':loan_analysis,
    'loan_summary':loan_summary,
    'pk':pk,
    'loan_comment':loan_comment,
    'approval_status':approval_status,
    }
    return render(request,'master_templates/Loan_application_approval_details.html',context)


def savings_cash_withdrawal_Certitication_list_load(request):
    current_user=[]
    if not request.user.user_type == '1':
        current_user=Executives_Tasks_Model.objects.get(user=request.user.id)

 
    status=TransactionStatus.objects.get(title='UNTREATED')
    approval_status=ApprovalStatus.objects.get(title='PENDING')
  
    applicants=MembersCashWithdrawalsApplication.objects.filter(approval_status=approval_status,status=status)

    context={
    'current_user':current_user,
    'applicants':applicants,
    }
    return render(request,'master_templates/savings_cash_withdrawal_Certitication_list_load.html',context)


def savings_cash_withdrawal_list_load(request):
    current_user=[]
    if not request.user.user_type == '1':
        current_user=Executives_Tasks_Model.objects.get(user=request.user.id)


    status=TransactionStatus.objects.get(title='UNTREATED')
    approval_status=ApprovalStatus.objects.get(title='PENDING')
    
    applicants=MembersCashWithdrawalsApplication.objects.filter(approval_status=approval_status,status=status)

    context={
    'current_user':current_user,
    'applicants':applicants,
    }
    return render(request,'master_templates/savings_cash_withdrawal_list_load.html',context)


def savings_cash_withdrawal_preview(request,pk):
    current_user=[]
    if not request.user.user_type == '1':
        current_user=Executives_Tasks_Model.objects.get(user=request.user.id)

    form=savings_cash_withdrawal_preview_form(request.POST or None)
    applicant=MembersCashWithdrawalsApplication.objects.get(id=pk)
    applied_date =applicant.created_at
    
    maturity_date=applicant.maturity_date
    exclusive_status=ExclusiveStatus.objects.get(title="EXCLUSIVE")
    
    if applicant.member.member.exclusive_status==exclusive_status:
        submission_status=True
    else:
        submission_status=False
        if maturity_date <= current_date:
            submission_status=True
    approval_status=ApprovalStatus.objects.get(title='APPROVED')
    form.fields['ledger_balance'].initial= applicant.ledger_balance
    form.fields['amount_applied'].initial= applicant.amount
    form.fields['amount_approved'].initial= applicant.amount
    form.fields['status'].initial= applicant.status.id
    form.fields['comment'].initial= "Please Process"
    form.fields['status'].initial= approval_status.id

    if request.method=="POST":
        status_id=request.POST.get('status')
        status=ApprovalStatus.objects.get(id=status_id)
        amount_approved=request.POST.get('amount_approved')
        amount_applied=request.POST.get('amount_applied')
        comment=request.POST.get('comment')
        certification_officer_id=request.POST.get('certification_officers')
    
        certification_officer=CertificationOfficers.objects.get(id=certification_officer_id)
        
        if status.title == 'APPROVED':          
            if float(amount_approved) > float(amount_applied):
                messages.error(request,'Amount Approved Cannot be More than Applied Amount')
                return HttpResponseRedirect(reverse('savings_cash_withdrawal_preview',args=(pk,)))
            applicant.approval_status=status
            applicant.approved_amount=amount_approved
            applicant.approval_comment=comment
            applicant.approval_status=status
            applicant.certification_officer=certification_officer
            applicant.save()
            return HttpResponseRedirect(reverse('savings_cash_withdrawal_list_load'))
        else:
            pass
    context={
    'current_user':current_user,
    'applicant':applicant,
    'form':form,
    'submission_status':submission_status,
    }
    return render(request,'master_templates/savings_cash_withdrawal_preview.html',context)



def members_exclusiveness_list_load(request):
    current_user=[]
    if not request.user.user_type == '1':
        current_user=Executives_Tasks_Model.objects.get(user=request.user.id)
        # return HttpResponse(current_user)
    status=TransactionStatus.objects.get(title='UNTREATED')
    approval_status=ApprovalStatus.objects.get(title='PENDING')
    
    applicants=MembersExclusiveness.objects.filter(approval_status=approval_status,status=status)
    
    context={
    'current_user':current_user,
    'applicants':applicants,
    }
    return render(request,'master_templates/members_exclusiveness_list_load.html',context)


def members_exclusiveness_process(request,pk):
    current_user=[]
    if not request.user.user_type == '1':
        current_user=Executives_Tasks_Model.objects.get(user=request.user.id)

    form=members_exclusiveness_request_approval_process_form(request.POST or None)
    applicant=MembersExclusiveness.objects.get(id=pk)
    if request.method=="POST":
        processing_status=ProcessingStatus.objects.get(title='UNPROCESSED')
        approval_officer=CustomUser.objects.get(id=request.user.id)
        comment=request.POST.get('comment')
        status_id=request.POST.get('approval_status')
        status=ApprovalStatus.objects.get(id=status_id)
        applicant.approval_status=status
        applicant.approval_comment=comment
        applicant.approval_officer=approval_officer
        applicant.processing_status=processing_status
        applicant.approved_at=now
        applicant.save()
        return HttpResponseRedirect(reverse('members_exclusiveness_list_load'))

    context={
    'current_user':current_user,
    'form':form,
    'applicant':applicant,
    }
    return render(request,'master_templates/members_exclusiveness_process.html',context)


def Shares_Purchase_Request_Approval_List_Load(request):
    current_user=[]
    if not request.user.user_type == '1':
        current_user=Executives_Tasks_Model.objects.get(user=request.user.id)

    status=TransactionStatus.objects.get(title='UNTREATED')
    approval_status=ApprovalStatus.objects.get(title='PENDING')
    records=MembersSharePurchaseRequest.objects.filter(approval_status=approval_status,status=status)
    
    context={
    'current_user':current_user,
    'records':records,
    }
    return render(request,'master_templates/Shares_Purchase_Request_Approval_List_Load.html',context)


def Shares_Purchase_Request_Approval_Processed(request,pk):
    current_user=[]
    if not request.user.user_type == '1':
        current_user=Executives_Tasks_Model.objects.get(user=request.user.id)

    form=Shares_Purchase_Request_Approval_Processed_form(request.POST or None)
    record=MembersSharePurchaseRequest.objects.get(id=pk)

    if request.method=="POST":
        units = request.POST.get("units")
        comment=request.POST.get('comment')

        approval_status_id=request.POST.get('approval_status')
        approval_status=ApprovalStatus.objects.get(id=approval_status_id)

        record.units=units
        record.approval_status=approval_status
        record.approval_date=now
        record.approval_comment=comment
        record.save()
        return HttpResponseRedirect(reverse('Shares_Purchase_Request_Approval_List_Load'))
    form.fields['units'].initial=record.units
    context={
    'current_user':current_user,
    'form':form,
    'record':record,
    }
    return render(request,'master_templates/Shares_Purchase_Request_Approval_Processed.html', context)


def Cash_Withdrawal_Request_Approval_List_Load(request):
    current_user=[]
    if not request.user.user_type == '1':
        current_user=Executives_Tasks_Model.objects.get(user=request.user.id)

    context={
     'current_user':current_user,
    }
    return render(request,'master_templates/Cash_Withdrawal_Request_Approval_List_Load.html',context)
#######################################################################
################## SECRETARY SECTION #####################################
#######################################################################

def Loan_request_certification_list_load(request):
    current_user=[]
    if not request.user.user_type == '1':
        current_user=Executives_Tasks_Model.objects.get(user=request.user.id)

    
    submission_status=SubmissionStatus.objects.get(title="SUBMITTED")
    certification_status=CertificationStatus.objects.get(title="PENDING")
    applicants=LoanRequest.objects.filter(certification_officer__officer_id=current_user,submission_status=submission_status,certification_status=certification_status)
    
    context={
    'current_user':current_user,
    'applicants':applicants

    }
    return render(request,'master_templates/SECRETARY/Loan_request_certification_list_load.html',context)


def Loan_request_certification_details(request,pk):
    current_user=[]
    if not request.user.user_type == '1':
        current_user=Executives_Tasks_Model.objects.get(user=request.user.id)

    loan_comment=LoanRequest.objects.get(id=pk)
    loan_analysis=LoanRequestSettings.objects.filter(applicant_id=pk,category='ANALYSIS')
    loan_summary=LoanRequestSettings.objects.filter(applicant_id=pk,category='SUMMARY')
    

    certification_status=CertificationStatus.objects.all()
    approval_officers=ApprovalOfficers.objects.filter(transaction__transaction_id=loan_comment.loan.id)


    if request.method=='POST':

        comment=request.POST.get('comment')
        officer_id=request.POST.get('officer')
        officer=ApprovalOfficers.objects.get(id=officer_id)

        status_id=request.POST.get('status')
        status=CertificationStatus.objects.get(id=status_id)

        certified_date= datetime.datetime.now()


        loan_comment.certification_status=status
        loan_comment.certification_comment=comment
        loan_comment.certification_date=certified_date
        loan_comment.approval_officer=officer
        loan_comment.save()
    
        return HttpResponseRedirect(reverse('Loan_request_certification_list_load'))

    context={
    'current_user':current_user,
    'loan_analysis':loan_analysis,
    'loan_summary':loan_summary,
    'pk':pk,
    'loan_comment':loan_comment,
    'approval_officers':approval_officers,
    'certification_status':certification_status,
    }
    return render(request,'master_templates/SECRETARY/Loan_request_certification_details.html',context)



def Loan_application_certification_list_load(request):
    current_user=[]
    if not request.user.user_type == '1':
        current_user=Executives_Tasks_Model.objects.get(user=request.user.id)

    
    submission_status=SubmissionStatus.objects.get(title="SUBMITTED")
    certification_status=CertificationStatus.objects.get(title="PENDING")
    applicants=LoanApplication.objects.filter(certification_officer__officer_id=current_user,submission_status=submission_status,certification_status=certification_status)
    
    context={
    'current_user':current_user,
    'applicants':applicants

    }
    return render(request,'master_templates/SECRETARY/Loan_application_certification_list_load.html',context)


def Loan_application_certification_details(request,pk):
    current_user=[]
    if not request.user.user_type == '1':
        current_user=Executives_Tasks_Model.objects.get(user=request.user.id)

    loan_comment=LoanApplication.objects.get(id=pk)
    loan_analysis=LoanApplicationSettings.objects.filter(applicant_id=pk,category='ANALYSIS')
    loan_summary=LoanApplicationSettings.objects.filter(applicant_id=pk,category='SUMMARY')
    

    certification_status=CertificationStatus.objects.all()
    approval_officers=ApprovalOfficers.objects.filter(transaction__transaction_id=loan_comment.applicant.applicant.loan.id)


    if request.method=='POST':

        comment=request.POST.get('comment')
        officer_id=request.POST.get('officer')
        officer=ApprovalOfficers.objects.get(id=officer_id)

        status_id=request.POST.get('status')
        status=CertificationStatus.objects.get(id=status_id)

        certified_date= datetime.datetime.now()


        loan_comment.certification_status=status
        loan_comment.certification_comment=comment
        loan_comment.certification_date=certified_date
        loan_comment.approval_officer=officer
        loan_comment.save()
    
        return HttpResponseRedirect(reverse('Loan_application_certification_list_load'))

    context={
    'current_user':current_user,
    'loan_analysis':loan_analysis,
    'loan_summary':loan_summary,
    'pk':pk,
    'loan_comment':loan_comment,
    'approval_officers':approval_officers,
    'certification_status':certification_status,
    }
    return render(request,'master_templates/SECRETARY/Loan_application_certification_details.html',context)


def Non_Monetary_Loan_Request_certification_Load(request):
    current_user=[]
    if not request.user.user_type == '1':
        current_user=Executives_Tasks_Model.objects.get(user=request.user.id)

    status=TransactionStatus.objects.get(title='UNTREATED')
    transaction=TransactionTypes.objects.get(code='204')
   
    user=CustomUser.objects.get(id=request.user.id)
   
    certification_officer=CertificationOfficers.objects.get(officer=user,transaction__transaction=transaction)
  
    certification_status=CertificationStatus.objects.get(title='PENDING')

    records=Members_Commodity_Loan_Application.objects.filter(status=status,certification_officer=certification_officer,certification_status=certification_status)
    
   
    context={
    'current_user':current_user,
    'records':records,
    
    }
    return render(request,'master_templates/SECRETARY/Non_Monetary_Loan_Request_certification_Load.html',context)

def Non_Monetary_Loan_Request_certification_Load_details(request,pk):
    current_user=[]
    if not request.user.user_type == '1':
        current_user=Executives_Tasks_Model.objects.get(user=request.user.id)

    form=Non_Monetary_Loan_Request_certification_Load_details_form(request.POST or None)
    record=Members_Commodity_Loan_Application.objects.get(id=pk)
    ticket=record.ticket
    queryset=Members_Commodity_Loan_Products_Selection.objects.filter(ticket=ticket)

    if request.method == 'POST':
        certification_status=CertificationStatus.objects.get(title="CERTIFIED")
        certification_comment=request.POST.get('comment')
        approval_officer_id=request.POST.get('approval_officers')
        approval_officer=ApprovalOfficers.objects.get(id=approval_officer_id)
        certification_date=get_current_date(now)
        
        record.certification_date=certification_date
        record.certification_comment=certification_comment
        record.approval_officer=approval_officer
        record.certification_status=certification_status
        record.save()
        return HttpResponseRedirect(reverse('Non_Monetary_Loan_Request_certification_Load'))

    form.fields['comment'].initial="For your Consideration"
    context={
    'current_user':current_user,
    'queryset':queryset,
    'ticket':ticket,
    'record':record,
    'form':form,
    }
    return render(request,'master_templates/SECRETARY/Non_Monetary_Loan_Request_certification_Load_details.html',context)



#######################################################################
################## TREASURER     ################################
#######################################################################

def withdrawal_confirmation_list_load(request):
    current_user=[]
    if not request.user.user_type == '1':
        current_user=Executives_Tasks_Model.objects.get(user=request.user.id)

    status=TransactionStatus.objects.get(title='UNTREATED')
    disbursement_status=ApprovalStatus.objects.get(title='PENDING')
    records=MembersCashWithdrawalsMain.objects.filter(status=status,disbursement_status=disbursement_status)
    
    context={
    'current_user':current_user,
    'records':records,
    }
    return render(request,'master_templates/TREASURER/withdrawal_confirmation_list_load.html',context)


def withdrawal_confirmation_details(request,pk):
    status1=MembershipStatus.objects.get(title='ACTIVE')

    
    disbursement_officer=DisbursementOfficers.objects.get(officer_id=request.user.id)
    disbursement_status=ApprovalStatus.objects.get(title='APPROVED')

    record=MembersCashWithdrawalsMain.objects.get(id=pk)
    
    account_number=record.member.member.account_number
    ledger=PersonalLedger.objects.filter(account_number=account_number).last()
    
    debit=record.member.approved_amount
    credit=0
    balance= float(ledger.balance) - float(debit)


    transaction_period=now

    if record.channel.title == 'CHEQUE':
        particulars="Withdrawal through CHEQUE, with No "  + str(record.cheque_number) + ', ' + str(record.coop_account.account_name) + '(' + record.coop_account.bank.title + ')'      
    elif record.channel.title == 'CASH':
        particulars="Withdrawal through CASH" 
    elif record.channel.title == 'TRANSFER':
        particulars="Withdrawal through TRANSFER from " + str(record.coop_account.account_name) + '(' + record.coop_account.bank.title + ') into ' + record.member_account.account_name + '(' + str(record.member_account.account_number)  + ')'
        # particulars="Withdrawal through TRANSFER from " + str(record.coop_account.account_name) + '(' + record.coop_account.bank.title + ') into ' + str(record.member_account.account_number) 

    transaction=record.member.member.transaction
    member=record.member.member.member

    ledger_record=PersonalLedger(member=member,transaction=transaction,account_number=account_number,particulars=particulars,debit=debit,credit=credit,balance=balance,transaction_period=transaction_period,status=status1)
    ledger_record.save()


    
    record.disbursement_status=disbursement_status
    record.disbursement_officer=disbursement_officer
    record.disbursement_date=now
    record.save()

    return HttpResponseRedirect(reverse('withdrawal_confirmation_list_load'))

####################################################################
###################### RECEIPT AND ID MANAGER ######################
####################################################################

def tre_AutoReceipt_Setup(request):
    current_user=[]
    if not request.user.user_type == '1':
        current_user=Executives_Tasks_Model.objects.get(user=request.user.id)

    record=[]
    if AutoReceipt.objects.all().exists():
        record=AutoReceipt.objects.first()

    if request.method=="POST":
        receipt=request.POST.get("receipt")
        if AutoReceipt.objects.all().exists():
            record=AutoReceipt.objects.first()
            record.receipt=receipt
            record.save()
        else:
            record=AutoReceipt(receipt=receipt)
            record.save()
        return HttpResponseRedirect(reverse('tre_AutoReceipt_Setup'))
    context={
    'current_user':current_user,
    'record':record,
    }
    return render(request,'master_templates/TREASURER/AutoReceipt_Setup.html',context)



def tre_receipt_manager(request):
    current_user=[]
    if not request.user.user_type == '1':
        current_user=Executives_Tasks_Model.objects.get(user=request.user.id)

    form = receipt_manager_form(request.POST or None)
    receipts=Receipts.objects.all()
    if request.method=="POST":
        start_point = request.POST.get('start_point')
        stop_point = request.POST.get('stop_point')
        
        for i in  range(int(start_point),int(stop_point)+1): 
            record=Receipts(receipt=str(i).zfill(5))
            record.save()
        return HttpResponseRedirect(reverse('tre_receipt_manager'))
    context={
    'current_user':current_user,
    'form':form,
    'receipts':receipts,
    }
    return render(request,'master_templates/TREASURER/receipt_manager.html',context)


#######################################################################
################## COOPERATIVE ACCOUNTS ################################
#######################################################################

def tre_CooperativeBankAccounts_add(request):
    current_user=[]
    if not request.user.user_type == '1':
        current_user=Executives_Tasks_Model.objects.get(user=request.user.id)

    form=CooperativeBankAccounts_form(request.POST or None)
    banks=CooperativeBankAccounts.objects.all()
    if request.method == 'POST':
        bank_id=request.POST.get('bank')
        bank=Banks.objects.get(id=bank_id)

        account_type_id=request.POST.get('account_type')
        account_type=AccountTypes.objects.get(id=account_type_id)

        account_name=request.POST.get('account_name')
        account_number=request.POST.get('account_number')

        if CooperativeBankAccounts.objects.filter(bank=bank,account_number=account_number).exists():
            messages.error(request,'This account Number is already in Use')
            return HttpResponseRedirect(reverse('tre_CooperativeBankAccounts_add'))

        record=CooperativeBankAccounts(bank=bank,account_type=account_type,account_name=account_name,account_number=account_number)
        record.save()

        messages.success(request,"Record Added Successfully")
        return HttpResponseRedirect(reverse('tre_CooperativeBankAccounts_add'))

    context={
    'current_user':current_user,
    'form':form,
    'banks':banks,
    }
    return render(request,'master_templates/TREASURER/CooperativeBankAccounts_add.html',context)


def tre_CooperativeBankAccounts_Remove(request,pk):
    record=CooperativeBankAccounts.objects.get(id=pk)
    record.delete()
    return HttpResponseRedirect(reverse('tre_CooperativeBankAccounts_add'))


def tre_CooperativeBankAccounts_Update(request,pk):
    current_user=[]
    if not request.user.user_type == '1':
        current_user=Executives_Tasks_Model.objects.get(user=request.user.id)

    form=CooperativeBankAccounts_form(request.POST or None)
    record=CooperativeBankAccounts.objects.get(id=pk)

    form.fields['account_name'].initial=record.account_name
    form.fields['account_number'].initial=record.account_number
    form.fields['bank'].initial=record.bank.id
    form.fields['account_type'].initial=record.account_type.id
    if request.method=="POST":
        bank_id=request.POST.get('bank')
        bank=Banks.objects.get(id=bank_id)

        account_type_id = request.POST.get('account_type')
        account_type=AccountTypes.objects.get(id=account_type_id)

        account_name=request.POST.get('account_name')
        account_number=request.POST.get('account_number')

        record.bank=bank
        record.account_type=account_type
        record.account_name=account_name
        record.account_number=account_number
        record.save()
        return HttpResponseRedirect(reverse('tre_CooperativeBankAccounts_add'))
        
    context={
    'current_user':current_user,
    'form':form,
    }
    return render(request,'master_templates/TREASURER/CooperativeBankAccounts_Update.html',context)



####################################################################
###################### FIN. SECRETARY ######################
####################################################################

def Cash_Withdrawal_Approved_list_load(request):
    current_user=[]
    if not request.user.user_type == '1':
        current_user=Executives_Tasks_Model.objects.get(user=request.user.id)

    status=TransactionStatus.objects.get(title="UNTREATED")
    approval_status=ApprovalStatus.objects.get(title='APPROVED')
    applicants=MembersCashWithdrawalsApplication.objects.filter(status=status,approval_status=approval_status)
    
    context={
    'current_user':current_user,
    'applicants':applicants,
    }
    return render(request,'master_templates/FINSEC/Cash_Withdrawal_Approved_list_load.html',context)


def Cash_Withdrawal_Approved_Details(request,pk):
    current_user=[]
    if not request.user.user_type == '1':
        current_user=Executives_Tasks_Model.objects.get(user=request.user.id)

    form=Cash_Withdrawal_Approved_Details_form(request.POST or None)
    applicant=MembersCashWithdrawalsApplication.objects.get(id=pk)
    member_accounts=MembersBankAccounts.objects.filter(member_id=applicant.member.member)

    form.fields['amount'].initial=applicant.approved_amount
    form.fields['payment_date'].initial=now

    cheque=False
    cash=False
    transfer=False
    if request.method=="POST" and 'btn_fetch' in request.POST:
        
        channel_id=request.POST.get('channels')
        channel = PaymentChannels.objects.get(id=channel_id)

        cheque=False
        if channel.title=="CHEQUE":
            cheque=True
        elif channel.title=="CASH":
            cash=True
        elif channel.title=="TRANSFER":
            transfer=True
        
    if request.method=="POST" and 'btn_submit' in request.POST:
        status=TransactionStatus.objects.get(title="UNTREATED")
        processed_by=CustomUser.objects.get(id=request.user.id)

        channel_id=request.POST.get('channels')
        channel = PaymentChannels.objects.get(id=channel_id)
        
        amount =request.POST.get('amount')
        payment_date =request.POST.get('payment_date')
        
        officer_id =request.POST.get('officers')
        disbursement_officer=DisbursementOfficers.objects.get(id=officer_id)
        
        channels_id =request.POST.get('channels')
        channels=PaymentChannels.objects.get(id=channels_id)

        if channel.title=="CHEQUE":
            coop_account_id =request.POST.get('account')
            coop_account=CooperativeBankAccounts.objects.get(id=coop_account_id)
            cheque_number=request.POST.get('cheque_number')
            
            if cheque_number=="":
                messages.error(request,'Cheque Number Missing')
                return HttpResponseRedirect(reverse('Cash_Withdrawal_Approved_Details',args=(pk,)))
            
            record=MembersCashWithdrawalsMain(member=applicant,
                channel=channel,
                payment_date=payment_date,
                coop_account=coop_account,
                cheque_number=cheque_number,
                processed_by=processed_by,
                disbursement_officer=disbursement_officer,
                status=status,
                )
            record.save()
        elif channel.title=="CASH":
            
            record=MembersCashWithdrawalsMain(member=applicant,
                channel=channel,
                payment_date=payment_date,
                processed_by=processed_by,
                disbursement_officer=disbursement_officer,
                status=status,
                )
            record.save()
        elif channel.title=="TRANSFER":
            coop_account_id =request.POST.get('account')
            coop_account=CooperativeBankAccounts.objects.get(id=coop_account_id)

            member_account_id=request.POST.get('member_account')
            member_account=MembersBankAccounts.objects.get(id=member_account_id)
            record=MembersCashWithdrawalsMain(member=applicant,
                channel=channel,
                payment_date=payment_date,
                coop_account=coop_account,
                member_account=member_account,
                processed_by=processed_by,
                disbursement_officer=disbursement_officer,
                status=status,
                )
            record.save()
            
        certification_date=now      
        status=TransactionStatus.objects.get(title="TREATED")
        certification_status=CertificationStatus.objects.get(title='CERTIFIED')
        
        applicant.status=status
        applicant.certification_status=certification_status
        applicant.certification_date=certification_date
        applicant.save()
        return HttpResponseRedirect(reverse('Cash_Withdrawal_Approved_list_load'))
            
    context={
    'current_user':current_user,
    'member_accounts':member_accounts,
    'applicant':applicant,
    'form':form,
    'cheque':cheque,
    'cash':cash,
    'transfer':transfer,
    }
    return render(request,'master_templates/FINSEC/Cash_Withdrawal_Approved_Details.html',context)






#######################################################################
################## GENERAL REPORT #####################################
#######################################################################

def transaction_views_ranked(request):
    current_user=[]
    if not request.user.user_type == '1':
        current_user=Executives_Tasks_Model.objects.get(user=request.user.id)

    transactions=TransactionTypes.objects.filter(~Q(source__title='GENERAl')).order_by('rank')
    context={
    'current_user':current_user,
    'transactions':transactions,

    }
    return render(request,'master_templates/reports/transaction_views_ranked.html',context)


def List_of_Users(request):
    current_user=[]
    if not request.user.user_type == '1':
        current_user=Executives_Tasks_Model.objects.get(user=request.user.id)

    users=Staff.objects.all()
    records=UserType.objects.all().order_by('code')
    # users=Staff.objects.annotate(full_name=Concat("admin__first_name", Value(" "), "admin__last_name")).all().values_lst("full_name")

    context={
    'current_user':current_user,
    'users':users,
    'records':records,
    }
    return render(request,'master_templates/List_of_Users.html',context)