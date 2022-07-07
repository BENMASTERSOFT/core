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
import xlwt
####################################################################
###################### HOME PAGE ###################################
####################################################################

TRANSACTION_STATUS=(
    ('UNTREATED','UNTREATED'),
    ("TREATED","TREATED")
    )

PROCESSING_STATUS=(
    ("UNPROCESSED",'UNPROCESSED'),
    ("PROCESSED","PROCESSED")
    )

CHANNELS=(
        ("CASH","CASH"),
        ("POS","POS"),
        ("TRANSFER","TRANSFER"),
        )

SUBMISSION_STATUS=(
        ('SUBMITTED','SUBMITTED'),
        ('NOT SUBMITTED','NOT SUBMITTED')
        )

MEMBERSHIP_STATUS=(
        ("ACTIVE","ACTIVE"),
        ("INACTIVE","INACTIVE")
        )
SALES_CATEGORIES=(
        ("CASH","CASH"),
        ("CREDIT","CREDIT"),
        ("ITEMS RETURN","ITEMS RETURN"),
        )
CASHBOOK_STATUS=(
        ("UNPOSTED","UNPOSTED"),
        ("POSTED","POSTED")
        )
CERTIFICATION_STATUS=(
        ("PENDING",'PENDING'),
        ("CERTIFIED",'CERTIFIED'),
        ("NOT CERTIFIED",'NOT CERTIFIED'),
        )
LOAN_SCHEDULE_STATUS=(
        ("UNSCHEDULED","UNSCHEDULED"),
        ("SCHEDULED","SCHEDULED")
        )
APPROVAL_STATUS=(
        ('PENDING',"PENDING"),
        ('APPROVED',"APPROVED")
        )


TICKET_STATUS=(
        ("OPEN","OPEN"),
        ("CLOSED","CLOSED")
        )
RECEIPT_TYPES=(
        ('AUTO','AUTO'),
        ('MANUAL','MANUAL')
        )
RECEIPT_STATUS=(
        ('UNUSED','UNUSED'),
        ('USED','USED')
        )
LOCK_STATUS=(
            ("OPEN",'OPEN'),
            ("LOCKED",'LOCKED'),
            )
UPLOAD_STATUS=(
            ("PENDING","PENDING"),
            ("UPLOADED","UPLOADED"),
            ("VERIFIED","VERIFIED")
            )
MULTIPLE_LOAN_STATUS=(
            ("NOT ALLOWED",'NOT ALLOWED'),
            ("ALLOWED",'ALLOWED'),
            )
YESNO=(
    ("NO","NO"),
    ("YES","YES")
    )
ADMIN_CHARGES=(
    ("CASH","CASH"),
    ("PERCENTAGE","PERCENTAGE")
    )

INTEREST_DEDUCTION=(
                    ("SOURCE","SOURCE"),
                    ("SPREAD","SPREAD")
                    )

ACCOUNT_TYPES=(
            ("SAVINGS","SAVINGS"),
            ("CURRENT","CURRENT")
            )

PAYMENT_CHANNEL=(
                ("CASH","CASH"),
                ("CHEQUE","CHEQUE"),
                ("TRANSFEWR","TRANSFEWR")
                )

WITHDRAWAL_STATUS=(
        ("LOCKED","LOCKED"),
        ("UNLOCKED","UNLOCKED")
        )
LOAN_CATEGORY=(
            ("MONETARY","MONETARY"),
            ("NON-MONETARY","NON-MONETARY")
            )
def admin_home(request):
    task_array=[]

    if not request.user.user_type == '1':


        tasks=System_Users_Tasks_Model.objects.filter(user_id=request.user.id)

        for task in tasks:
            # print(task.task.title)
            task_array.append(task.task.title)

    members=[]
    transactions = TransactionTypes.objects.all().count()

    members = Members.objects.filter(status="ACTIVE").count()
    title="System Admin"

    context={
    'task_array':task_array,
    "members":members,
    "transactions":transactions,
    'title':title,
    # 'record':record,
    }
    return render(request, "master_templates/dashboard.html",context)


def User_Profile(request):

    user_id=CustomUser.objects.get(id=request.user.id)
    task_array=[]
    if not request.user.user_type == '1':
        tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
        for task in tasks:
            task_array.append(task.task.title)


    form=add_staff_manage_form(request.POST or None)

    user=Staff.objects.get(admin_id=user_id)
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
                return HttpResponseRedirect(reverse('User_Profile'))
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
        return HttpResponseRedirect(reverse('admin_home'))
    context={
    'task_array':task_array,
    'form':form,
    }
    return render(request, "master_templates/User_Profile.html",context)


# def system_reset(request):
#     Receipts.objects.all().update(status='UNUSED')


#     record=CustomUser.objects.filter(user_type=5)
#     record.delete()
#     record=MemberShipRequest.objects.all()
#     record.delete()

#     record=NorminalRoll.objects.all()
#     record.delete()

#     MembersIdManager.objects.filter().update(member_id=1)
#     AutoReceipt.objects.filter().update(receipt=1)
#     LoanNumber.objects.filter().update(code=1)


#     Members_Credit_Sales_Selected.objects.all().delete()
#     CooperativeShopLedger.objects.all().delete()
#     Daily_Sales.objects.all().delete()
#     Daily_Sales_Cash_Flow_Summary.objects.all().delete()
#     Cooperative_Shop_Cash_Deposit.objects.all().delete()
#     General_Cash_Sales_Selected.objects.all().delete()
#     Day_End_Sales_Transactions.objects.all().delete()
#     Daily_Cash_Deposit_Summary.objects.all().delete()
#     members_shop_credit_loans.objects.all().delete()

#     MonthlyShopdeductionListGenerated.objects.all().delete()
#     MonthlyShopdeductionList.objects.all().delete()
#     MonthlyShopGroupGeneratedTransactions.objects.all().delete()
#     MonthlyJointDeductionList.objects.all().delete()
#     MonthlyJointDeductionGeneratedTransactions.objects.all().delete()
#     MonthlyJointDeductionGenerated.objects.all().delete()
#     MonthlyDeductionList.objects.all().delete()
#     MonthlyGeneratedTransactions.objects.all().delete()
#     MonthlyDeductionListGenerated.objects.all().delete()
#     MonthlyGroupGeneratedTransactions.objects.all().delete()
#     MonthlyDeductionGenerationHeading.objects.all().delete()
#     AccountDeductions.objects.all().delete()
#     NonMemberAccountDeductions.objects.all().delete()
#     MonthlyOverdeductionsRefund.objects.all().delete()


#     return HttpResponseRedirect(reverse('admin_home'))



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
    task_array=[]
    if not request.user.user_type == '1':
        tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
        for task in tasks:
            task_array.append(task.task.title)
    context={
    'task_array':task_array,

    }
    return render(request,'master_templates/General_Tasks_Manager.html',context)


def Executive_Users(request):
    task_array=[]
    if not request.user.user_type == '1':
        tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
        for task in tasks:
            task_array.append(task.task.title)


    records=CustomUser.objects.filter(user_type='2')

    context={
    'task_array':task_array,
    'records':records,
    }
    return render(request,'master_templates/Executive_Users.html',context)


def Executive_Users_Tasks_Preview(request,pk):
    task_array=[]

    if not request.user.user_type == '1':

        tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
        for task in tasks:
            task_array.append(task.task.title)

    tasks=System_Users_Tasks.objects.filter(usertype__code='2')
    user=CustomUser.objects.get(id=pk)
    records=System_Users_Tasks_Model.objects.filter(user=user).order_by('task__rank')



    if request.method =="POST" and 'btn-all' in request.POST:
        for task in tasks:
            if System_Users_Tasks_Model.objects.filter(task=task,user=user).exists():
                pass
            else:
                System_Users_Tasks_Model(task=task,user=user).save()

        return HttpResponseRedirect(reverse('Executive_Users_Tasks_Preview',args=(pk,)))

    if request.method =="POST" and 'btn-selected' in request.POST:
        task_id=request.POST.get('task')
        task=System_Users_Tasks.objects.get(id=task_id)

        if System_Users_Tasks_Model.objects.filter(task=task,user=user).exists():
            messages.info(request,'Record already Exist')
            return HttpResponseRedirect(reverse('Executive_Users_Tasks_Preview',args=(pk,)))

        System_Users_Tasks_Model(task=task,user=user).save()
        return HttpResponseRedirect(reverse('Executive_Users_Tasks_Preview',args=(pk,)))


    context={
    'tasks':tasks,
    'task_array':task_array,
    'records':records,
    'user':user,
    }
    return render(request,'master_templates/Executive_Users_Tasks_Preview.html',context)


def Executive_Users_Tasks_Remove(request,pk):
    record=System_Users_Tasks_Model.objects.get(id=pk)
    return_pk=record.user_id
    record.delete()
    return HttpResponseRedirect(reverse('Executive_Users_Tasks_Preview',args=(return_pk,)))


def Desk_Office_Users(request):
    task_array=[]
    if not request.user.user_type == '1':
        tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
        for task in tasks:
            task_array.append(task.task.title)

    records=CustomUser.objects.filter(user_type='3')

    context={
    'task_array':task_array,
    'records':records,
    }
    return render(request,'master_templates/Desk_Office_Users.html',context)


def Desk_Office_Tasks_Preview(request,pk):
    task_array=[]
    if not request.user.user_type == '1':
        tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
        for task in tasks:
            task_array.append(task.task.title)

    tasks=System_Users_Tasks.objects.filter(usertype__code='3')
    user=CustomUser.objects.get(id=pk)
    records=System_Users_Tasks_Model.objects.filter(user=user).order_by('task__rank')

    if request.method =="POST" and 'btn-all' in request.POST:

        for task in tasks:
            if System_Users_Tasks_Model.objects.filter(task=task,user=user).exists():
                pass
            else:
                System_Users_Tasks_Model(task=task,user=user).save()

        return HttpResponseRedirect(reverse('Desk_Office_Tasks_Preview',args=(pk,)))

    if request.method =="POST" and 'btn-selected' in request.POST:

        task_id=request.POST.get('task')
        task=System_Users_Tasks.objects.get(id=task_id)

        if System_Users_Tasks_Model.objects.filter(task=task,user=user).exists():
            messages.info(request,'Record already Exist')
            return HttpResponseRedirect(reverse('Desk_Office_Tasks_Preview',args=(pk,)))

        System_Users_Tasks_Model(task=task,user=user).save()
        return HttpResponseRedirect(reverse('Desk_Office_Tasks_Preview',args=(pk,)))



    context={
    'tasks':tasks,
    'task_array':task_array,
    'records':records,
    'user':user,
    }
    return render(request,'master_templates/Desk_Office_Tasks_Preview.html',context)


def Desk_Office_Tasks_Remove(request,pk):
    record=System_Users_Tasks_Model.objects.get(id=pk)
    return_pk=record.user_id
    record.delete()
    return HttpResponseRedirect(reverse('Desk_Office_Tasks_Preview',args=(return_pk,)))


def Shop_Users(request):
    task_array=[]
    if not request.user.user_type == '1':
        tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
        for task in tasks:
            task_array.append(task.task.title)

    records=CustomUser.objects.filter(user_type='4')

    context={
    'task_array':task_array,
    'records':records,
    }
    return render(request,'master_templates/Shop_Users.html',context)


def Shop_Users_Tasks_Preview(request,pk):
    task_array=[]
    if not request.user.user_type == '1':
        tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
        for task in tasks:
            task_array.append(task.task.title)

    tasks=System_Users_Tasks.objects.filter(usertype__code='4')

    user=CustomUser.objects.get(id=pk)
    records=System_Users_Tasks_Model.objects.filter(user=user).order_by('task__rank')



    if request.method =="POST" and 'btn-all' in request.POST:
        for task in tasks:
            if System_Users_Tasks_Model.objects.filter(task=task,user=user).exists():
                pass
            else:
                System_Users_Tasks_Model(task=task,user=user).save()
        return HttpResponseRedirect(reverse('Shop_Users_Tasks_Preview',args=(pk,)))


    if request.method =="POST" and 'btn-selected' in request.POST:
        task_id=request.POST.get('task')
        task=System_Users_Tasks.objects.get(id=task_id)

        if System_Users_Tasks_Model.objects.filter(task=task,user=user).exists():
            messages.info(request,'Record already Exist')
            return HttpResponseRedirect(reverse('Shop_Users_Tasks_Preview',args=(pk,)))

        System_Users_Tasks_Model(task=task,user=user).save()
        return HttpResponseRedirect(reverse('Shop_Users_Tasks_Preview',args=(pk,)))


    context={
    'tasks':tasks,
    'task_array':task_array,
    'records':records,
    'user':user,
    }
    return render(request,'master_templates/Shop_Users_Tasks_Preview.html',context)


def Shop_Users_Tasks_Remove(request,pk):
    record=System_Users_Tasks_Model.objects.get(id=pk)
    return_pk=record.user_id
    record.delete()
    return HttpResponseRedirect(reverse('Shop_Users_Tasks_Preview',args=(return_pk,)))



def Shop_Tasks(request,pk):
    task_array=[]
    if not request.user.user_type == '1':
        tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
        for task in tasks:
            task_array.append(task.task.title)
    form=Shop_Tasks_form(request.POST or None)

    record=[]
    if Shop_Tasks_Models.objects.filter(user_id=pk).exists():
        record=Shop_Tasks_Models.objects.filter(user_id=pk).first()

    if request.method == 'POST':
        form = Shop_Tasks_form(request.POST)

        sales=request.POST.get('sales')
        debt_recovery=request.POST.get('debt_recovery')
        purchases=request.POST.get('purchases')
        purchases_tracking=request.POST.get('purchases_tracking')
        item_write_off=request.POST.get('item_write_off')
        item_write_off_approval=request.POST.get('item_write_off_approval')
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
            record.purchases_tracking=purchases_tracking
            record.purchases=purchases
            record.item_write_off_approval=item_write_off_approval
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
                            purchases_tracking=0,
                            purchases=0,
                            item_write_off_approval=0,
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

            if purchases_tracking:
                record.purchases_tracking=purchases_tracking
            else:
                record.purchases_tracking=0

            if purchases:
                record.purchases=purchases
            else:
                record.purchases=0

            if item_write_off:
                record.item_write_off=item_write_off
            else:
                record.item_write_off=0

            if item_write_off_approval:
                record.item_write_off_approval=item_write_off_approval
            else:
                record.item_write_off_approval=0


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
        form.fields['purchases_tracking'].initial=record.purchases_tracking
        form.fields['purchases'].initial=record.purchases
        form.fields['item_write_off_approval'].initial=record.item_write_off_approval
        form.fields['item_write_off'].initial=record.item_write_off
        form.fields['personal_ledger'].initial=record.personal_ledger
        form.fields['general_report'].initial=record.general_report
        form.fields['day_end_transaction'].initial=record.day_end_transaction
        form.fields['monthly_deduction'].initial=record.monthly_deduction
        form.fields['product_manager'].initial=record.product_manager
        form.fields['suppliers_manager'].initial=record.suppliers_manager
    context={
    'task_array':task_array,
    'form':form,
    'record':record,
    }
    return render(request,'master_templates/Shop_Tasks.html',context)


def Termination_Loan_Allowed_load(request):
    task_array=[]
    if not request.user.user_type == '1':
        tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
        for task in tasks:
            task_array.append(task.task.title)

    processed_by=CustomUser.objects.get(id=request.user.id)
    tdate=get_current_date(now)
    title="Termination Control"
    form = Termination_Loan_Allowed_load_Form(request.POST or None)

    records=Termination_Loan_Allowed.objects.all()
    if request.method == "POST":
        termination_type_id=request.POST.get('termination_type')
        termination_type=Termination_Types.objects.get(id=termination_type_id)
        Termination_Loan_Allowed(termination=termination_type,processed_by=processed_by,tdate=tdate).save()

        return HttpResponseRedirect(reverse('Termination_Loan_Allowed_load'))
    context={
    'records':records,
    'form':form,
    'title':title,
    'task_array':task_array,
    }
    return render(request,'master_templates/Termination_Loan_Allowed_load.html',context)


def Termination_Loan_Allowed_Remove(request,pk):
    Termination_Loan_Allowed.objects.filter(id=pk).delete()
    return HttpResponseRedirect(reverse('Termination_Loan_Allowed_load'))



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
def ExceptableCriterias_upload(request):
    task_array=[]
    if not request.user.user_type == '1':
        tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
        for task in tasks:
            task_array.append(task.task.title)

    template = "master_templates/file_upload.html"


    prompt = {
        'order': "Upload Members Waver Types, Order of the CSV should be Code, Title"
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
        _, created = ExceptableCriterias.objects.update_or_create(
            title=column[1],
        )

    context = {'task_array':task_array,}
    return render(request, template, context)


@permission_required('admin.can_add_log_entry')
def Termination_Sources_upload(request):
    task_array=[]
    if not request.user.user_type == '1':
        tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
        for task in tasks:
            task_array.append(task.task.title)

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

    context = {'task_array':task_array,}
    return render(request, template, context)



@permission_required('admin.can_add_log_entry')
def MonthlyDeductionGenerationHeaders_upload(request):
    task_array=[]
    if not request.user.user_type == '1':
        tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
        for task in tasks:
            task_array.append(task.task.title)
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

    context = {'task_array':task_array,}
    return render(request, template, context)


@permission_required('admin.can_add_log_entry')
def SharesUnits_upload(request):
    task_array=[]
    if not request.user.user_type == '1':
        tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
        for task in tasks:
            task_array.append(task.task.title)

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

    context = {'task_array':task_array,}
    return render(request, template, context)


@permission_required('admin.can_add_log_entry')
def ProductCategory_upload(request):
    task_array=[]
    if not request.user.user_type == '1':
        tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
        for task in tasks:
            task_array.append(task.task.title)


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

    context = {'task_array':task_array,}
    return render(request, template, context)


@permission_required('admin.can_add_log_entry')
def Product_Write_off_Reasons_upload(request):
    task_array=[]
    if not request.user.user_type == '1':
        tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
        for task in tasks:
            task_array.append(task.task.title)

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

    context = {'task_array':task_array,}
    return render(request, template, context)


@permission_required('admin.can_add_log_entry')
def Stock_upload(request):
    task_array=[]
    if not request.user.user_type == '1':
        tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
        for task in tasks:
            task_array.append(task.task.title)

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

    lock_status = LockedStatus.objects.get(title='LOCKED')
    for column in csv.reader(io_string, delimiter=',',  quotechar='|', quoting =csv.QUOTE_NONE):
           _, created = Stock.objects.update_or_create(
            code=str(column[0]).zfill(5),
            item_name=column[1],
            category=ProductCategory.objects.get(code=column[2]),
            quantity=0,
            no_in_pack=column[4],
            re_order_level=column[5],
            unit_selling_price=column[6],
            lock_status=lock_status,
        )

    context = {'task_array':task_array,}
    return render(request, template, context)



def upload_stock_roll(request):
    task_array=[]
    if not request.user.user_type == '1':
        tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
        for task in tasks:
            task_array.append(task.task.title)


    if request.method == 'POST':
        lock_status='LOCKED'
        stock_resource = StockListResource()
        dataset = Dataset()
        new_stock_list = request.FILES['myfile']

        if not new_stock_list.name.endswith('xlsx'):
            messages.error(request,'Wrong format')
            return HttpResponseRedirect(reverse('upload_stock_roll'))

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
                    lock_status=lock_status,
                )
            value.save()
    context={
    'task_array':task_array,

    }
    return render(request,'master_templates/upload_stock.html',context)


@permission_required('admin.can_add_log_entry')
def title_upload(request):
    task_array=[]
    if not request.user.user_type == '1':
        tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
        for task in tasks:
            task_array.append(task.task.title)
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

    context = {'task_array':task_array,}
    return render(request, template, context)


@permission_required('admin.can_add_log_entry')
def states_upload(request):
    task_array=[]
    if not request.user.user_type == '1':
        tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
        for task in tasks:
            task_array.append(task.task.title)

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

    context = {'task_array':task_array,}
    return render(request, template, context)



@permission_required('admin.can_add_log_entry')
def NOKRelationships_upload(request):
    task_array=[]
    if not request.user.user_type == '1':
        tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
        for task in tasks:
            task_array.append(task.task.title)
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

    context = {'task_array':task_array,}
    return render(request, template, context)


@permission_required('admin.can_add_log_entry')
def lga_upload(request):
    task_array=[]
    if not request.user.user_type == '1':
        tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
        for task in tasks:
            task_array.append(task.task.title)
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

    context = {'task_array':task_array,}
    return render(request, template, context)


@permission_required('admin.can_add_log_entry')
def Gender_upload(request):
    task_array=[]
    if not request.user.user_type == '1':
        tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
        for task in tasks:
            task_array.append(task.task.title)
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

    context = {'task_array':task_array,}
    return render(request, template, context)


@permission_required('admin.can_add_log_entry')
def Banks_upload(request):
    task_array=[]
    if not request.user.user_type == '1':
        tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
        for task in tasks:
            task_array.append(task.task.title)
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

    context = {'task_array':task_array,}
    return render(request, template, context)






@permission_required('admin.can_add_log_entry')
def Locations_upload(request):
    task_array=[]
    if not request.user.user_type == '1':
        tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
        for task in tasks:
            task_array.append(task.task.title)
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

    context = {'task_array':task_array,}
    return render(request, template, context)


@permission_required('admin.can_add_log_entry')
def Departments_upload(request):
    task_array=[]
    if not request.user.user_type == '1':
        tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
        for task in tasks:
            task_array.append(task.task.title)
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

    context = {'task_array':task_array,}
    return render(request, template, context)


@permission_required('admin.can_add_log_entry')
def SalaryInstitution_upload(request):
    task_array=[]
    if not request.user.user_type == '1':
        tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
        for task in tasks:
            task_array.append(task.task.title)
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

    context = {'task_array':task_array,}
    return render(request, template, context)


@permission_required('admin.can_add_log_entry')
def TransactionSources_upload(request):
    task_array=[]
    if not request.user.user_type == '1':
        tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
        for task in tasks:
            task_array.append(task.task.title)
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

    context = {'task_array':task_array,}
    return render(request, template, context)


@permission_required('admin.can_add_log_entry')
def UserTypes_upload(request):
    task_array=[]
    if not request.user.user_type == '1':
        tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
        for task in tasks:
            task_array.append(task.task.title)
    template = "master_templates/file_upload.html"


    prompt = {
        'order': "User Types Order of the CSV should be Code Title"
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

    context = {'task_array':task_array,}
    return render(request, template, context)


@permission_required('admin.can_add_log_entry')
def System_Users_Tasks_upload(request):
    task_array=[]
    if not request.user.user_type == '1':
        tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
        for task in tasks:
            task_array.append(task.task.title)
    template = "master_templates/file_upload.html"


    prompt = {
        'order': "User Task Order of the CSV should be UserType, Title"
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
       _, created = System_Users_Tasks.objects.update_or_create(
            usertype=UserType.objects.get(code=column[0]),
            title=column[1],
            rank=column[2],
        )

    context = {'task_array':task_array,}
    return render(request, template, context)


@permission_required('admin.can_add_log_entry')
def Transaction_Types_upload(request):
    task_array=[]
    if not request.user.user_type == '1':
        tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
        for task in tasks:
            task_array.append(task.task.title)
    template = "master_templates/file_upload.html"


    prompt = {
        'order': "UsTransaction Types Order of the CSV should be Code,Name, Source"
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
       _, created = TransactionTypes.objects.update_or_create(
            source=TransactionSources.objects.get(id=column[2]),
            code=column[0],
            name=column[1],
        )

    context = {'task_array':task_array,}
    return render(request, template, context)



####################################################################
###################### COMMODITY MANAGER ######################
####################################################################
def Commodity_Products_Add_Transactions_Load(request):
    task_array=[]
    if not request.user.user_type == '1':
        tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
        for task in tasks:
            task_array.append(task.task.title)
    records =TransactionTypes.objects.filter(category='NON-MONETARY')
    context={
    'task_array':task_array,
    'records':records,
    }
    return render(request,'master_templates/Commodity_Products_Add_Transactions_Load.html',context)



def Commodity_Products_Add_Transactions_Categories_Load(request,pk):
    task_array=[]
    if not request.user.user_type == '1':
        tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
        for task in tasks:
            task_array.append(task.task.title)
    records =Commodity_Categories.objects.filter(transaction_id=pk)
    context={
    'task_array':task_array,
    'records':records,
    }
    return render(request,'master_templates/Commodity_Products_Add_Transactions_Categories_Load.html',context)



def Commodity_Products_add(request,pk):
    task_array=[]
    if not request.user.user_type == '1':
        tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
        for task in tasks:
            task_array.append(task.task.title)
    form = Commodity_Products_add_Form(request.POST or None)
    record =Commodity_Categories.objects.get(id=pk)
    records=Commodity_Product_List.objects.filter(category=record)

    if request.method=="POST":
        product_name = request.POST.get('product_name')
        product_model = request.POST.get('product_model')
        details = request.POST.get('details')
        queryset=Commodity_Product_List(category=record,product_name=product_name.upper(),product_model=product_model.upper(),details=details.title(),status="ACTIVE")
        queryset.save()
        messages.success(request,'Record Submitted Successfully')
        return HttpResponseRedirect(reverse('Commodity_Products_add',args=(pk,)))
    context={
    'task_array':task_array,
    'form':form,
    'record':record,
    'records':records,
    }
    return render(request,'master_templates/Commodity_Products_add.html',context)




def Commodity_Products_Manage_Transactions_Load(request):
    task_array=[]
    if not request.user.user_type == '1':
        tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
        for task in tasks:
            task_array.append(task.task.title)
    records =TransactionTypes.objects.filter(category='NON-MONETARY')
    context={
    'task_array':task_array,
    'records':records,
    }
    return render(request,'master_templates/Commodity_Products_Manage_Transactions_Load.html',context)



def Commodity_Products_Manage_Load(request,pk):
    task_array=[]
    if not request.user.user_type == '1':
        tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
        for task in tasks:
            task_array.append(task.task.title)
    transaction =TransactionTypes.objects.get(id=pk)
    records=Commodity_Product_List.objects.filter(category__transaction=transaction)

    context={
    'task_array':task_array,
    'records':records,
    }
    return render(request,'master_templates/Commodity_Products_Manage_Load.html',context)


def Commodity_Products_Manage_Update(request,pk):
    task_array=[]
    if not request.user.user_type == '1':
        tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
        for task in tasks:
            task_array.append(task.task.title)
    form = Commodity_Products_Update_Form(request.POST or None)
    record=Commodity_Product_List.objects.get(id=pk)


    if request.method == 'POST':
        product_name=request.POST.get('product_name')
        product_model=request.POST.get('product_model')
        details=request.POST.get('details')
        status = request.POST.get('status')


        record.product_name=product_name.upper()
        record.product_model=product_model.upper()
        record.details=details.title()
        record.status=status
        record.save()
        messages.success(request,'Record Updated Successfully')
        return HttpResponseRedirect(reverse('Commodity_Products_Manage_Load',args=(record.category.transaction_id,)))

    form.fields['product_name'].initial = record.product_name
    form.fields['product_model'].initial = record.product_model
    form.fields['details'].initial = record.details
    form.fields['status'].initial = record.status

    context={
    'task_array':task_array,
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
    task_array=[]
    if not request.user.user_type == '1':
        tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
        for task in tasks:
            task_array.append(task.task.title)
    items= Companies.objects.all()
    title="Add Companies"
    form = addCompaniesForm(request.POST or None)
    if request.method ==  "POST":
        form = addCompaniesForm(request.POST)
        if form.is_valid():
            title=form.cleaned_data["title"]
            record = Companies(title=title.upper())
            record.save()
            messages.success(request,"Record Added Successfully")
            return  HttpResponseRedirect(reverse('addCompanies'))
    context={
    'task_array':task_array,
    'form':form,
    'items':items,
    'url':'addCompanies',
    'button_text':"Add Company",
    'title':title,
    }
    return render(request,'master_templates/add_single_item.html', context)

def Manage_Companies(request):
    task_array=[]
    if not request.user.user_type == '1':
        tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
        for task in tasks:
            task_array.append(task.task.title)
    companies=Companies.objects.all()
    context={
    'task_array':task_array,
    'companies':companies,
    }
    return render(request,'master_templates/manage_companies.html', context)

def Manage_Companies_update(request,pk):
    task_array=[]
    if not request.user.user_type == '1':
        tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
        for task in tasks:
            task_array.append(task.task.title)
    form = addCompaniesForm(request.POST or None)
    company=Companies.objects.get(id=pk)

    form.fields['title'].initial=company.title

    if request.method == "POST":
        title=request.POST.get('title')
        company.title=title.upper()
        company.save()
        return HttpResponseRedirect(reverse('Manage_Companies'))
    context={
    'task_array':task_array,
    'form':form,
    'company':company,
    }
    return render(request,'master_templates/Manage_Companies_update.html', context)


def Delete_Companies(request,pk):
    record=Companies.objects.get(id=pk)
    record.delete()
    return HttpResponseRedirect(reverse('Manage_Companies'))



def Product_Linking_Period_Load(request):
    task_array=[]
    if not request.user.user_type == '1':
        tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
        for task in tasks:
            task_array.append(task.task.title)

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
    'task_array':task_array,
    'form':form,
    # 'period':period,
    # 'batch':batch,
    }
    return render(request,'master_templates/Product_Linking_Period_Load.html',context)


def Product_Linking_Company_Load(request,period_obj,batch_obj,transaction_obj):
    task_array=[]
    if not request.user.user_type == '1':
        tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
        for task in tasks:
            task_array.append(task.task.title)
    companies=Companies.objects.all()

    period=Commodity_Period.objects.get(id=period_obj)
    batch=Commodity_Period_Batch.objects.get(id=batch_obj)
    transaction=TransactionTypes.objects.get(id=transaction_obj)

    context={
    'task_array':task_array,
    'companies':companies,
    'period':period,
    'batch':batch,
    'transaction':transaction,
    }
    return render(request,'master_templates/Product_Linking_Company_Load.html',context)



def Product_Linking_Details(request,pk,period_pk,batch_pk,transaction_pk):
    task_array=[]
    if not request.user.user_type == '1':
        tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
        for task in tasks:
            task_array.append(task.task.title)

    period=Commodity_Period.objects.get(id=period_pk)
    batch=Commodity_Period_Batch.objects.get(id=batch_pk)
    transaction=TransactionTypes.objects.get(id=transaction_pk)
    # return HttpResponse(transaction.name)
    company=Companies.objects.get(id=pk)

    records=Commodity_Product_List.objects.filter(category__transaction=transaction,status='ACTIVE')
    linked_records = Company_Products.objects.filter(company=company,period=period,batch=batch,product__category__transaction=transaction)

    context={
    'task_array':task_array,
    'company':company,
    'records':records,
    'linked_records':linked_records,
    'period':period,
    'batch':batch,
    'transaction':transaction,
    }
    return render(request,'master_templates/Product_Linking_Details.html',context)


def Product_Linking_Details_Preview(request,comp_pk,pk,period_pk,batch_pk,transaction_pk):
    task_array=[]
    if not request.user.user_type == '1':
        tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
        for task in tasks:
            task_array.append(task.task.title)
    form=Product_Linking_Details_Preview_form(request.POST or None)
    company=Companies.objects.get(id=comp_pk)
    product=Commodity_Product_List.objects.get(id=pk)

    coop_price_enabled=False
    if product.category.interest_rate_required != '1':
        coop_price_enabled=True

    if request.method == "POST":
        period=Commodity_Period.objects.get(id=period_pk)
        batch=Commodity_Period_Batch.objects.get(id=batch_pk)

        amount=request.POST.get('amount')

        coop_amount=0
        if product.category.interest_rate_required != '1':
            coop_amount=request.POST.get('coop_amount')

            if not coop_amount:
                messages.error(request,'Company Price Missing')
                return HttpResponseRedirect(reverse('Product_Linking_Details',args=(comp_pk,period_pk,batch_pk,transaction_pk)))


        if not amount:
            messages.error(request,'Company Price Missing')
            return HttpResponseRedirect(reverse('Product_Linking_Details',args=(comp_pk,period_pk,batch_pk,transaction_pk)))

        if Company_Products.objects.filter(company=company,product=product,period=period,batch=batch).exists():
            Company_Products.objects.filter(company=company,product=product,period=period,batch=batch).update(amount=amount,coop_amount=coop_amount)
        else:
            Company_Products(company=company,product=product,period=period,batch=batch,amount=amount,coop_amount=coop_amount,status='ACTIVE').save()

        return HttpResponseRedirect(reverse('Product_Linking_Details',args=(comp_pk,period_pk,batch_pk,transaction_pk)))

    form.fields['product_name'].initial=product.product_name
    form.fields['product_model'].initial=product.product_model
    form.fields['details'].initial=product.details
    context={
    'task_array':task_array,
    'company':company,
    'form':form,
    'product':product,
    'coop_price_enabled':coop_price_enabled,
    }
    return render(request,'master_templates/Product_Linking_Details_Preview.html',context)



def Product_UnLinking_Process(request,comp_pk,pk,period_pk, batch_pk, transaction_pk):
    task_array=[]
    if not request.user.user_type == '1':
        tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
        for task in tasks:
            task_array.append(task.task.title)
    product=Company_Products.objects.get(id=pk)
    product.delete()

    messages.success(request,"Record Deleted Successfully")
    return  HttpResponseRedirect(reverse('Product_Linking_Details',args=(comp_pk,period_pk,batch_pk,transaction_pk,)))
    context={
    'task_array':task_array,
    'company':company,
    'records':records,
    }
    return render(request,'master_templates/Product_Linking_Details.html',context)



def Product_Duration_Settings_Period_Load(request):
    task_array=[]
    if not request.user.user_type == '1':
        tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
        for task in tasks:
            task_array.append(task.task.title)

    if request.method == "POST":
        period_obj=request.POST.get('period')
        period=Commodity_Period.objects.get(id=period_obj)

        batch_obj=request.POST.get('batch')
        batch=Commodity_Period_Batch.objects.get(id=batch_obj)

        transaction_obj=request.POST.get('transaction')
        transaction=TransactionTypes.objects.get(id=transaction_obj)

        return HttpResponseRedirect(reverse('Product_Duration_Settings_Service_Load',args=(period_obj, batch_obj,transaction_obj)))
    form=Product_Linking_Period_Load_form(request.POST or None)
    context={
    'task_array':task_array,
    'form':form,
    # 'period':period,
    # 'batch':batch,
    }
    return render(request,'master_templates/Product_Duration_Settings_Period_Load.html',context)


def Product_Duration_Settings_Service_Load(request,period_obj,batch_obj,transaction_obj):
    task_array=[]
    if not request.user.user_type == '1':
        tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
        for task in tasks:
            task_array.append(task.task.title)

    period=Commodity_Period.objects.get(id=period_obj)
    batch=Commodity_Period_Batch.objects.get(id=batch_obj)
    transaction=TransactionTypes.objects.get(id=transaction_obj)

    if request.method == 'POST':
        trans_package_id=request.POST.get('transaction')

        trans_package=Commodity_Categories.objects.get(id=trans_package_id)
        duration=trans_package.duration

        start_date_id=request.POST.get("start_date")
        date_format = '%Y-%m-%d'
        dtObj = datetime.datetime.strptime(start_date_id, date_format)
        start_date=get_current_date(dtObj)


        stop_date = start_date+ relativedelta(months=int(duration))


        if  Company_Products_Duration.objects.filter(product=trans_package,period=period,batch=batch).exists():
            messages.error(request,'Record Already Exist')
            return HttpResponseRedirect(reverse('Product_Duration_Settings_Service_Load',args=(period_obj,batch_obj,transaction_obj)))


        Company_Products_Duration(product=trans_package,period=period,batch=batch,start_date=start_date,stop_date=stop_date).save()
        messages.success(request,'Record Added Successfully')
        return HttpResponseRedirect(reverse('Product_Duration_Settings_Service_Load',args=(period_obj,batch_obj,transaction_obj)))


    form=Cash_Deposit_Report_Date_Load_form(request.POST or None)
    records=Commodity_Categories.objects.filter(transaction=transaction).order_by('id').values_list('id','title').distinct()

    durations=Company_Products_Duration.objects.filter(period=period,batch=batch)

    form.fields['start_date'].initial=now
    form.fields['stop_date'].initial=now
    context={
    'task_array':task_array,
    'durations':durations,
    'period':period,
    'batch':batch,
    'transaction':transaction,
    'form':form,
    'records':records,
    }
    return render(request,'master_templates/Product_Duration_Settings_Service_Load.html',context)


def Product_Duration_Settings_Service_Delete(request,pk,period_obj,batch_obj,transaction_obj):
    Company_Products_Duration.objects.get(id=pk).delete()
    messages.success(request,'Record Deleted Successfully')
    return HttpResponseRedirect(reverse('Product_Duration_Settings_Service_Load',args=(period_obj,batch_obj,transaction_obj)))




def Product_Settings_Period_Load(request):
    task_array=[]
    if not request.user.user_type == '1':
        tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
        for task in tasks:
            task_array.append(task.task.title)

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
    'task_array':task_array,
    'form':form,
    # 'period':period,
    # 'batch':batch,
    }
    return render(request,'master_templates/Product_Settings_Period_Load.html',context)



def Product_Price_Settings_Company_Load(request,period_obj,batch_obj,transaction_obj):
    task_array=[]
    if not request.user.user_type == '1':
        tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
        for task in tasks:
            task_array.append(task.task.title)
    companies=Companies.objects.all()
    period=Commodity_Period.objects.get(id=period_obj)
    batch=Commodity_Period_Batch.objects.get(id=batch_obj)
    transaction=TransactionTypes.objects.get(id=transaction_obj)

    context={
    'task_array':task_array,
    'companies':companies,
    'period':period,
    'batch':batch,
    'transaction':transaction,
    }
    return render(request,'master_templates/Product_Price_Settings_Company_Load.html',context)


def Product_Price_Settings_details(request,pk,period_obj,batch_obj,transaction_obj):
    task_array=[]
    if not request.user.user_type == '1':
        tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
        for task in tasks:
            task_array.append(task.task.title)
    company=Companies.objects.get(id=pk)
    period=Commodity_Period.objects.get(id=period_obj)
    batch=Commodity_Period_Batch.objects.get(id=batch_obj)
    transaction=TransactionTypes.objects.get(id=transaction_obj)


    # records=Company_Products.objects.filter(company=company)
    records=Company_Products.objects.filter(company=company,period=period,batch=batch,product__category__transaction=transaction)

    context={
    'task_array':task_array,
    'records':records,
    'company':company,
    'period':period,
    'batch':batch,
    'transaction':transaction,
    }
    return render(request,'master_templates/Product_Price_Settings_details.html',context)


def Product_Price_Settings_Update(request,comp_pk,pk):
    task_array=[]
    if not request.user.user_type == '1':
        tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
        for task in tasks:
            task_array.append(task.task.title)
    form=Commodity_Products_Price_Update_Form(request.POST or None)
    company=Companies.objects.get(id=comp_pk)
    record=Company_Products.objects.get(id=pk)

    coop_price_enabled=False
    if record.product.category.interest_rate_required != '1':
        coop_price_enabled=True



    if request.method == 'POST':
        unit_cost_price=request.POST.get('unit_cost_price')
        coop_price=0
        if coop_price_enabled:
            coop_price=request.POST.get('coop_price')
        else:
            coop_price=float(unit_cost_price) + (float(record.product.category.interest_rate)/100)*float(unit_cost_price)

        status=request.POST.get('status')
        record.amount=unit_cost_price
        record.coop_amount=coop_price
        record.status=status
        record.save()
        return HttpResponseRedirect(reverse('Product_Price_Settings_details',args=(comp_pk,record.period_id,record.batch_id,record.product.category.transaction_id)))


    form.fields['product_name'].initial=record.product.product_name
    form.fields['product_model'].initial=record.product.product_model
    form.fields['details'].initial=record.product.details
    form.fields['unit_cost_price'].initial=record.amount
    form.fields['coop_price'].initial=record.coop_amount
    form.fields['status'].initial=record.status

    context={
    'task_array':task_array,
    'record':record,
    'company':company,
    'form':form,
    'coop_price_enabled':coop_price_enabled,
    }
    return render(request,'master_templates/Product_Price_Settings_Update.html',context)


####################################################################
###################### USER ACCOUNT MANAGERS ######################
####################################################################

def Users_Task_Add_Category_load(request):
    task_array=[]
    if not request.user.user_type == '1':
        tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
        for task in tasks:
            task_array.append(task.task.title)
    records=UserType.objects.all()

    context={
    'task_array':task_array,

    'records':records,
    }
    return render(request,'master_templates/Users_Task_Add_Category_load.html',context)


def export_User_Task_xls(request):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="user_tasks.xls"'

    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Users Data') # this will make a sheet named Users Data

    row_num = 0  # Sheet header, first row

    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    columns = ['Title', 'Rank','User' ]

    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style) # at 0 row 0 column

    font_style = xlwt.XFStyle()  # Sheet body, remaining rows

    rows = System_Users_Tasks.objects.all().values_list('title','rank','usertype__title')

    for row in rows:
        row_num += 1
        for col_num in range(len(row)):
            ws.write(row_num, col_num, row[col_num], font_style)
    wb.save(response)

    return response




def Users_Task_Add(request,pk):
    task_array=[]
    if not request.user.user_type == '1':
        tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
        for task in tasks:
            task_array.append(task.task.title)
    form=Users_Task_Add_form(request.POST or None)
    usertype = UserType.objects.get(id=pk)
    records = System_Users_Tasks.objects.filter(usertype=usertype).order_by('rank')

    if request.method == "POST" and 'btn-process' in request.POST:
        title=request.POST.get("title")
        rank=request.POST.get("rank")

        if System_Users_Tasks.objects.filter(title=title,usertype=usertype).exists():
            messages.info(request,'This record already exist')
            return HttpResponseRedirect(reverse('Users_Task_Add',args=(pk,)))

        System_Users_Tasks(title=title.upper(),usertype=usertype,rank=rank).save()

        messages.success(request,'Record Added Successfully')
        return HttpResponseRedirect(reverse('Users_Task_Add',args=(pk,)))
    context={
    'task_array':task_array,
    'form':form,
    'records':records,
    'usertype':usertype,
    }
    return render(request,'master_templates/Users_Task_Add.html',context)

def Users_Task_Edit(request,pk):
    task_array=[]
    if not request.user.user_type == '1':
        tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
        for task in tasks:
            task_array.append(task.task.title)

    form=Users_Task_Add_form(request.POST or None)
    record = System_Users_Tasks.objects.get(id=pk)
    usertype=record.usertype

    if request.method == "POST" and 'btn-process' in request.POST:
        title=request.POST.get("title")
        rank=request.POST.get("rank")
        edit_title=request.POST.get("edit-title")

        if edit_title:
            if System_Users_Tasks.objects.filter(title=title,usertype=usertype).exists():
                messages.info(request,'This record already exist')
                return HttpResponseRedirect(reverse('Users_Task_Add',args=(usertype.pk,)))

            record.title=title.upper()

        record.rank=rank
        record.save()

        messages.success(request,'Record Updated Successfully')
        return HttpResponseRedirect(reverse('Users_Task_Add',args=(usertype.pk,)))
    form.fields['title'].initial=record.title
    form.fields['rank'].initial=record.rank
    context={
    'task_array':task_array,
    'form':form,

    'usertype':usertype,
    }
    return render(request,'master_templates/Users_Task_Edit.html',context)



def Users_Task_Delete(request,pk):
    record=System_Users_Tasks.objects.get(id=pk)
    usertype=UserType.objects.get(id=record.usertype_id)
    record.delete()
    return HttpResponseRedirect(reverse('Users_Task_Add',args=(usertype.pk,)))

def Invoice_Title(request):
    users = CustomUser.objects.exclude(Q(user_type__iexact='1') | Q(user_type__iexact='5'))
    task_array=[]
    if not request.user.user_type == '1':
        tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
        for task in tasks:
            task_array.append(task.task.title)
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
    'users':users,
    'task_array':task_array,
    'form':form,
    }
    return render(request,'master_templates/Invoice_Title.html',context)

def Executive_Positions_add(request):
    users = CustomUser.objects.exclude(Q(user_type__iexact='1') | Q(user_type__iexact='5'))
    task_array=[]
    if not request.user.user_type == '1':
        tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
        for task in tasks:
            task_array.append(task.task.title)
    title="Add Staff"
    form = Executive_Positions_Form(request.POST or None)

    records = ExecutivePositions.objects.all()
    if request.method == 'POST':
        title=request.POST.get('title')
        if title:
            ExecutivePositions(title=title).save()
            messages.success(request,'Record added Successfully')
            return HttpResponseRedirect(reverse('Executive_Positions_add'))

        else:
            messages.error(request,'Description missing')
            return HttpResponseRedirect(reverse('Executive_Positions_add'))

    context={
    'records':records,
    'users':users,
    'task_array':task_array,
    'form':form,
    }
    return render(request,'master_templates/Executive_Positions_add.html',context)


def Executive_Positions_Delete(request,pk):
    ExecutivePositions.objects.filter(id=pk).delete()
    messages.success(request,'Record Deleted Successfully')
    return HttpResponseRedirect(reverse('Executive_Positions_add'))



def Executive_add(request):
    users = CustomUser.objects.exclude(Q(user_type__iexact='1') | Q(user_type__iexact='5'))
    task_array=[]
    if not request.user.user_type == '1':
        tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
        for task in tasks:
            task_array.append(task.task.title)
    title="Select member to add as Executive"

    records = Members.objects.filter(status='ACTIVE')

    context={
    'users':users,
    'task_array':task_array,
    'records':records,
    'title':title,
    }
    return render(request,'master_templates/Executive_add.html',context)


def Executive_Member_Select(request,pk):
    users = CustomUser.objects.exclude(Q(user_type__iexact='1') | Q(user_type__iexact='5'))
    task_array=[]
    if not request.user.user_type == '1':
        tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
        for task in tasks:
            task_array.append(task.task.title)


    form = Executive_Member_Select_Form(request.POST or None)
    record = Members.objects.get(id=pk)

    if request.method == 'POST':
        name = request.POST.get("elias")
        position_id = request.POST.get("position")
        position = ExecutivePositions.objects.get(id=position_id)
        start_date_id = request.POST.get("start_date")

        date_format = '%Y-%m-%d'
        dtObj = datetime.datetime.strptime(start_date_id, date_format)
        start_date=get_current_date(dtObj)


        if Executives.objects.filter(position=position,status='ACTIVE').exists():
            messages.error(request,'There is still an active member for this Position')
            return HttpResponseRedirect(reverse('Executive_Member_Select', args=(pk,)))

        Executives(member=record,name=name,position=position,start_date=start_date,status='ACTIVE').save()
        return HttpResponseRedirect(reverse('Executive_add'))



    records=Executives.objects.filter(status='ACTIVE')
    if record.title:
        form.fields['name'].initial = "{} {}".format(record.title.title,record.get_full_name)
        form.fields['elias'].initial = "{} {}".format(record.title.title,record.get_full_name)
    else:
        form.fields['name'].initial = "{}".format(record.get_full_name)
        form.fields['elias'].initial = "{}".format(record.get_full_name)

    form.fields['start_date'].initial = now
    context={
    'users':users,
    'task_array':task_array,
    'record':record,
    'records':records,
    'form':form,

    }
    return render(request,'master_templates/Executive_Member_Select.html',context)



def Executive_Member_Remove(request,pk):
    item=Executives.objects.get(id=pk)
    return_pk = item.member.pk
    item.delete()
    return HttpResponseRedirect(reverse('Executive_Member_Select', args=(return_pk,)))


def Executive_add_Existing(request):
    users = CustomUser.objects.exclude(Q(user_type__iexact='1') | Q(user_type__iexact='5'))
    task_array=[]
    if not request.user.user_type == '1':
        tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
        for task in tasks:
            task_array.append(task.task.title)
    title="Select member to add as Executive"

    records = Executives.objects.filter(status='INACTIVE')

    context={
    'users':users,
    'task_array':task_array,
    'records':records,
    'title':title,
    }
    return render(request,'master_templates/Executive_add_Existing.html',context)


def Executive_add_Existing_Update(request,pk):
    users = CustomUser.objects.exclude(Q(user_type__iexact='1') | Q(user_type__iexact='5'))
    task_array=[]
    if not request.user.user_type == '1':
        tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
        for task in tasks:
            task_array.append(task.task.title)

    form = Executive_Member_Select_Form(request.POST or None)
    record = Executives.objects.get(id=pk)
    if request.method == 'POST':
        name = request.POST.get("elias")

        position_id = request.POST.get("position")
        position = ExecutivePositions.objects.get(id=position_id)
        start_date_id = request.POST.get("start_date")

        date_format = '%Y-%m-%d'
        dtObj = datetime.datetime.strptime(start_date_id, date_format)
        start_date=get_current_date(dtObj)


        if Executives.objects.filter(position=position,status='ACTIVE').exists():
            messages.error(request,'There is still an active member for this Position')
            return HttpResponseRedirect(reverse('Executive_add_Existing_Update', args=(pk,)))



        Executives(member=record.member,name=name,position=position,start_date=start_date,status='ACTIVE').save()
        return HttpResponseRedirect(reverse('Executive_add_Existing'))

    records=Executives.objects.filter(status='ACTIVE')
    form.fields['elias'].initial = record.name
    form.fields['position'].initial = record.position.id
    form.fields['start_date'].initial = now
    context={
    'users':users,
    'task_array':task_array,
    'record':record,
    'records':records,
    'form':form,
    }
    return render(request,'master_templates/Executive_add_Existing_Update.html',context)



def Executive_Member_Manage(request):
    users = CustomUser.objects.exclude(Q(user_type__iexact='1') | Q(user_type__iexact='5'))
    task_array=[]
    if not request.user.user_type == '1':
        tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
        for task in tasks:
            task_array.append(task.task.title)

    records=Executives.objects.filter(status='ACTIVE')


    context={
    'users':users,
    'task_array':task_array,
    'records':records,
    }
    return render(request,'master_templates/Executive_Member_Manage.html',context)



def Executive_Member_Manage_Update(request,pk):
    users = CustomUser.objects.exclude(Q(user_type__iexact='1') | Q(user_type__iexact='5'))
    task_array=[]
    if not request.user.user_type == '1':
        tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
        for task in tasks:
            task_array.append(task.task.title)
    form = Executive_Member_Select_Form(request.POST or None)
    record=Executives.objects.get(id=pk)


    if request.method == 'POST' and 'btn-update' in request.POST:
        name = request.POST.get('elias')
        position_id = request.POST.get("position")
        position = ExecutivePositions.objects.get(id=position_id)
        start_date_id = request.POST.get("start_date")

        date_format = '%Y-%m-%d'
        dtObj = datetime.datetime.strptime(start_date_id, date_format)
        start_date=get_current_date(dtObj)

        if Executives.objects.filter(position=position,status='ACTIVE').filter(~Q(id=pk)).exists():
            messages.error(request,'There is still an active Member in this Postion')
            return HttpResponseRedirect(reverse('Executive_Member_Manage_Update', args=(pk,)))

        record.position=position
        record.name=name
        record.start_date=start_date
        record.save()

        return HttpResponseRedirect(reverse('Executive_Member_Manage'))


    if request.method == 'POST' and 'btn-terminate' in request.POST:
        stop_date_id = request.POST.get("stop_date")

        date_format = '%Y-%m-%d'
        dtObj = datetime.datetime.strptime(stop_date_id, date_format)
        stop_date=get_current_date(dtObj)


        record.status='INACTIVE'
        record.stop_date=stop_date
        record.save()

        return HttpResponseRedirect(reverse('Executive_Member_Manage'))



    form.fields['elias'].initial = record.name
    form.fields['position'].initial = record.position.id
    form.fields['start_date'].initial = record.start_date
    form.fields['stop_date'].initial = now
    context={
    'users':users,
    'task_array':task_array,
    'record':record,
    'form':form,
    }
    return render(request,'master_templates/Executive_Member_Manage_Update.html',context)


def add_staff(request):
    task_array=[]
    if not request.user.user_type == '1':
        tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
        for task in tasks:
            task_array.append(task.task.title)
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
        # try:
        if user_type.code == '2':
            usertype_code = '2'
            user = CustomUser.objects.create_user(username=username,password=password,email=email,last_name=last_name,first_name=first_name,user_type=2)

        if user_type.code == '3':
            usertype_code = '3'
            user = CustomUser.objects.create_user(username=username,password=password,email=email,last_name=last_name,first_name=first_name,user_type=3)

        if user_type.code == '4':
            usertype_code = '4'
            user = CustomUser.objects.create_user(username=username,password=password,email=email,last_name=last_name,first_name=first_name,user_type=4)


        user.staff.middle_name=middle_name
        user.staff.address=address
        user.staff.phone_number=phone_number
        user.staff.gender=gender
        user.staff.title=title
        user.save()

        # tasks=System_Users_Tasks.objects.filter(usertype=usertype_code)
        # for task in tasks:
        #     System_Users_Tasks_Model(task=task,user=user).save()

        messages.success(request,"User Added Successfully")
        return HttpResponseRedirect(reverse("add_staff"))
        # except:
        #     messages.error(request,"Failed to add System User")
        #     return HttpResponseRedirect(reverse("add_staff"))

    context={
    'task_array':task_array,
    'title':title,
    'form':form,
    'users':users,
    'url':'add_staff',
    'items':items,
    'button_text':"Add",
    }
    return render(request, "master_templates/add_staff.html",context)

def add_staff_delete(request,pk):
    CustomUser.objects.filter(id=pk).delete()
    return HttpResponseRedirect(reverse("add_staff"))

def add_staff_manage(request):
    task_array=[]
    if not request.user.user_type == '1':
        tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
        for task in tasks:
            task_array.append(task.task.title)
    users = CustomUser.objects.exclude(Q(user_type__iexact='1') | Q(user_type__iexact='5'))
    context={
    'task_array':task_array,
    'users':users,
    }
    return render(request,'master_templates/addStaff_manage.html',context)

def add_staff_delete_1(request,pk):
    CustomUser.objects.filter(id=pk).delete()
    return HttpResponseRedirect(reverse("add_staff_manage"))


def add_staff_manage_view(request,pk):
    task_array=[]
    if not request.user.user_type == '1':
        tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
        for task in tasks:
            task_array.append(task.task.title)
    form=add_staff_manage_form(request.POST or None)
    user=Staff.objects.get(admin_id=pk)

    existing_user_type=UserType.objects.get(code=user.admin.user_type)

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


        if existing_user_type ==  user_type:
            pass
        else:
            System_Users_Tasks_Model.objects.filter(user=user.admin).delete()
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
    'task_array':task_array,
    'form':form,
    }
    return render(request,'master_templates/add_staff_manage_view.html',context)



def super_user_add(request):
    form=super_user_manage_form(request.POST or None)
    task_array=[]
    if not request.user.user_type == '1':
        tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
        for task in tasks:
            task_array.append(task.task.title)
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
    'task_array':task_array,
    }
    return render(request,'master_templates/super_user_add.html',context)




def super_user_manage(request):
    task_array=[]
    if not request.user.user_type == '1':
        tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
        for task in tasks:
            task_array.append(task.task.title)
    users = CustomUser.objects.filter(Q(user_type__iexact='1'))
    context={
    'task_array':task_array,
    'users':users,
    }
    return render(request,'master_templates/super_user_manage.html',context)


def super_user_manage_view(request,pk):
    task_array=[]
    if not request.user.user_type == '1':
        tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
        for task in tasks:
            task_array.append(task.task.title)
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
    'task_array':task_array,
    'form':form,
    }
    return render(request,'master_templates/super_user_manage_view.html',context)

####################################################################
###################### MEMBERS SHARES AND WELFARE ##################
####################################################################
def Shares_Deduction_savings(request):
    task_array=[]
    if not request.user.user_type == '1':
        tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
        for task in tasks:
            task_array.append(task.task.title)
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
    'task_array':task_array,
    'form':form,
    'records':records,
    }
    return render(request,'master_templates/Shares_Deduction_savings.html',context)


def Shares_Deduction_savings_remove(request,pk):
    record=SharesDeductionSavings.objects.get(id=pk)
    record.delete()
    return HttpResponseRedirect(reverse('Shares_Deduction_savings'))


def AddShares_Configurations(request):
    task_array=[]
    if not request.user.user_type == '1':
        tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
        for task in tasks:
            task_array.append(task.task.title)
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
    'task_array':task_array,
    'form':form,
    'record':record,
    }
    return render(request,'master_templates/AddShares_Configurations.html',context)


def addWelfare_Configurations(request):
    task_array=[]
    if not request.user.user_type == '1':
        tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
        for task in tasks:
            task_array.append(task.task.title)
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
    'task_array':task_array,
    'form':form,
    'record':record,
    }
    return render(request,'master_templates/addWelfare_Configurations.html',context)


####################################################################
###################### COMPONENNTS PAGE ############################
####################################################################
def MembersCompulsorySavings(request):
    task_array=[]
    if not request.user.user_type == '1':
        tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
        for task in tasks:
            task_array.append(task.task.title)
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
    'task_array':task_array,
        'form':form,
        'records':records,
    }
    return render(request,'master_templates/MembersCompulsorySavings.html', context)


def MembersCompulsorySavings_delete(request,pk):
    record = CompulsorySavings.objects.get(id=pk)
    record.delete()
    return HttpResponseRedirect(reverse('MembersCompulsorySavings'))


def addState(request):
    task_array=[]
    if not request.user.user_type == '1':
        tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
        for task in tasks:
            task_array.append(task.task.title)
    items= States.objects.all()
    title="Add State"
    form = addStateForm(request.POST or None)
    if request.method ==  "POST":
        form = addStateForm(request.POST)
        if form.is_valid():
            title=form.cleaned_data["title"]
            record = States(title=title.upper())
            record.save()
            messages.success(request,"Record Added Successfully")
        return	HttpResponseRedirect(reverse('addState'))
    context={
    'task_array':task_array,
    'form':form,
    'items':items,
    'url':'addState',
    'button_text':"Add State",
    'title':title,
    }
    return render(request,'master_templates/add_single_item.html', context)




def addExpiringDateInterval(request):

    task_array=[]
    if not request.user.user_type == '1':
        tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
        for task in tasks:
            task_array.append(task.task.title)
    item=[]
    if ExpiringDateInterval.objects.all().exists():
        item= ExpiringDateInterval.objects.first()

    title="Add Expiring Date Interval"
    form = addExpiringDateIntervalForm(request.POST or None)
    if request.method ==  "POST":

        if form.is_valid():
            title=form.cleaned_data["title"]
            if ExpiringDateInterval.objects.all().exists():
                ExpiringDateInterval.objects.all().update(title=title)
            else:
                record = ExpiringDateInterval(title=title)
                record.save()
            messages.success(request,"Record Added Successfully")
        return  HttpResponseRedirect(reverse('addExpiringDateInterval'))
    if item:
        form.fields['title'].initial=item.title
    context={
    'task_array':task_array,
    'form':form,
    'item':item,

    'title':title,
    }
    return render(request,'master_templates/addExpiringDateInterval.html', context)




def BankAccounts_Designation_List_Load(request):
    task_array=[]
    if not request.user.user_type == '1':
        tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
        for task in tasks:
            task_array.append(task.task.title)
    banks=CooperativeBankAccounts.objects.all()

    context={
    'task_array':task_array,
    'banks':banks,
    }
    return render(request,'master_templates/BankAccounts_Designation_List_Load.html',context)


def BankAccounts_Designation_Process(request,pk):
    task_array=[]
    if not request.user.user_type == '1':
        tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
        for task in tasks:
            task_array.append(task.task.title)

    form=BankAccounts_Designation_Process_form(request.POST or None)
    bank=CooperativeBankAccounts.objects.get(id=pk)


    records=CooperativeBankAccountsOperationalDesignations.objects.filter(account=bank)
    if request.method == "POST":
        transaction_id=request.POST.get('transactions')
        transaction=TransactionTypes.objects.get(id=transaction_id)

        CooperativeBankAccountsOperationalDesignations(account=bank,transaction=transaction,status='ACTIVE').save()
        return HttpResponseRedirect(reverse('BankAccounts_Designation_Process',args=(pk,)))

    context={
    'task_array':task_array,
    'bank':bank,
    'form':form,
    'records':records,
    }
    return render(request,'master_templates/BankAccounts_Designation_Process.html',context)




def Manage_state(request):
    task_array=[]
    if not request.user.user_type == '1':
        tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
        for task in tasks:
            task_array.append(task.task.title)
    states=States.objects.all()
    context={
    'task_array':task_array,
    'states':states,
    }
    return render(request,'master_templates/manage_state.html', context)


def delete_state(request,pk):
	state=States.objects.get(id=pk)
	state.delete()
	messages.success(request,"Record Deleted Successfully")
	return HttpResponseRedirect(reverse('addState'))


def addNOKRelationships(request):
    task_array=[]
    if not request.user.user_type == '1':
        tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
        for task in tasks:
            task_array.append(task.task.title)
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
    'task_array':task_array,
    'form':form,
    'items':items,
    'url':'NOKRelationships',
    'button_text':"Add Record",
    'title':title,
    }
    return render(request,'master_templates/add_single_item.html', context)



def Manage_NOKRelationships(request):
    task_array=[]
    if not request.user.user_type == '1':
        tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
        for task in tasks:
            task_array.append(task.task.title)
    Relationships=NOKRelationships.objects.all()
    context={
    'task_array':task_array,
    'Relationships':Relationships,
    }
    return render(request,'master_templates/manage_NOKRelationships.html', context)


def Manage_NOKRelationships_Remove(request,pk):
    relationship=NOKRelationships.objects.get(id=pk)
    relationship.delete()
    return HttpResponseRedirect(reverse('Manage_NOKRelationships'))


def Manage_NOKRelationships_Max_No(request):
    task_array=[]
    if not request.user.user_type == '1':
        tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
        for task in tasks:
            task_array.append(task.task.title)
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
    'task_array':task_array,
    'record':record,
    }
    return render(request,'master_templates/Manage_NOKRelationships_Max_No.html',context)


def Manage_Product_Code(request):
    task_array=[]
    if not request.user.user_type == '1':
        tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
        for task in tasks:
            task_array.append(task.task.title)
    form=Manage_Product_CodeForm(request.POST or None)

    record=[]
    if Product_Code.objects.all().exists():
        record=Product_Code.objects.first()

    if request.method == 'POST':
        code = request.POST.get('code')
        if code:
            if record:
                record.code=code
                record.save()
                return HttpResponseRedirect(reverse('admin_home'))
            Product_Code(code=code).save()
            return HttpResponseRedirect(reverse('admin_home'))

        messages.error(request,'Please Enter Code')
        return HttpResponseRedirect(reverse('Manage_Product_Code'))

    if record:
        form.fields['code'].initial=record.code
    context={
    'task_array':task_array,
    'record':record,
    'form':form,
    }
    return render(request,'master_templates/Manage_Product_Code.html',context)

def Xmas_Savings_Transaction_Period(request):
    task_array=[]
    if not request.user.user_type == '1':
        tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
        for task in tasks:
            task_array.append(task.task.title)

    form=Xmas_Savings_Transaction_Period_form(request.POST or None)
    records=XmasSavingsTransactionPeriod.objects.all()

    if request.method ==  'POST':
        batch = request.POST.get('batch')

        if XmasSavingsTransactionPeriod.objects.filter(batch=batch).exists():
            messages.error(request, "Record Already Exists")
            return HttpResponseRedirect(reverse('Xmas_Savings_Transaction_Period'))

        else:
            XmasSavingsTransactionPeriod(batch=batch,status='INACTIVE').save()
        return HttpResponseRedirect(reverse('Xmas_Savings_Transaction_Period'))
    context={
    'task_array':task_array,
    'records':records,
    'form':form,
    }
    return render(request,'master_templates/Xmas_Savings_Transaction_Period.html',context)

def Xmas_Savings_Transaction_Period_Delete(request,pk):
    XmasSavingsTransactionPeriod.objects.filter(id=pk).delete()
    return HttpResponseRedirect(reverse('Xmas_Savings_Transaction_Period'))


def Xmas_Savings_Default_Transfer_Account(request):
    task_array=[]
    if not request.user.user_type == '1':
        tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
        for task in tasks:
            task_array.append(task.task.title)

    form=Xmas_Savings_Default_Transfer_Account_form(request.POST or None)
    record=[]
    if XmasTransferDefaultSaving.objects.all().exists:
        record = XmasTransferDefaultSaving.objects.first()

    if request.method ==  'POST':
        transaction_id = request.POST.get('transaction')
        transaction=TransactionTypes.objects.get(id=transaction_id)

        if XmasTransferDefaultSaving.objects.all().exists():
            XmasTransferDefaultSaving.objects.all().update(transaction=transaction)

        else:
            XmasTransferDefaultSaving(transaction=transaction).save()

        return HttpResponseRedirect(reverse('Xmas_Savings_Default_Transfer_Account'))
    if record:
        form.fields['transaction'].initial=record.transaction.id
    context={
    'task_array':task_array,
    'record':record,
    'form':form,
    }
    return render(request,'master_templates/Xmas_Savings_Default_Transfer_Account.html',context)


def Commodity_Transaction_Period(request):
    task_array=[]
    if not request.user.user_type == '1':
        tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
        for task in tasks:
            task_array.append(task.task.title)
    form=Commodity_Transaction_Period_form(request.POST or None)
    records=Commodity_Period.objects.all()
    if request.method == 'POST':
        title=request.POST.get('period')
        if Commodity_Period.objects.filter(title=title).exists():
            return HttpResponseRedirect(reverse('Commodity_Transaction_Period'))

        Commodity_Period(title=title).save()
        messages.success(request,'Record Added Successfully')
        return HttpResponseRedirect(reverse('Commodity_Transaction_Period'))
    context={
    'form':form,
    'task_array':task_array,
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
    task_array=[]
    if not request.user.user_type == '1':
        tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
        for task in tasks:
            task_array.append(task.task.title)
    form=Commodity_Transaction_Period_Batch_form(request.POST or None)
    records=Commodity_Period_Batch.objects.all()
    if request.method == 'POST':
        title=request.POST.get('batch')
        if Commodity_Period_Batch.objects.filter(title=title).exists():
            return HttpResponseRedirect(reverse('Commodity_Transaction_Period_Batch'))

        Commodity_Period_Batch(title=title).save()
        messages.success(request,'Record Added Successfully')
        return HttpResponseRedirect(reverse('Commodity_Transaction_Period_Batch'))
    context={
    'form':form,
    'records':records,
    'task_array':task_array,
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
    task_array=[]
    if not request.user.user_type == '1':
        tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
        for task in tasks:
            task_array.append(task.task.title)
    title="Add Commodity Category"
    items= Commodity_Categories.objects.all()
    form = addCommodityCategoryForm(request.POST or None)

    if request.method ==  "POST":

        title=request.POST.get("title")
        transaction_id=request.POST.get('transactions')
        transaction=TransactionTypes.objects.get(id=transaction_id)
        if Commodity_Categories.objects.filter(title=title).exists():
            messages.error(request,'Record with this name already exist')
            return  HttpResponseRedirect(reverse('addCommodityCategory'))
        record = Commodity_Categories(transaction=transaction,title=title,receipt_type="NONE",status="ACTIVE",multiple_loan_status='NOT ALLOWED',form_print="NO")
        record.save()
        messages.success(request,"Record Added Successfully")
        return  HttpResponseRedirect(reverse('addCommodityCategory'))

    records=Commodity_Categories.objects.all()
    context={
    'task_array':task_array,
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


def addCommodityCategorySub(request,pk):
    task_array=[]
    if not request.user.user_type == '1':
        tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
        for task in tasks:
            task_array.append(task.task.title)
    title="Add Commodity Sub Categories"
    category= Commodity_Categories.objects.get(id=pk)
    records= Commodity_Category_Sub.objects.filter(category=category)
    form = addCommodityCategoryForm(request.POST or None)

    if request.method ==  "POST":

        title=request.POST.get("title")

        if Commodity_Category_Sub.objects.filter(title=title).exists():
            messages.error(request,'Record with this name already exist')
            return  HttpResponseRedirect(reverse('addCommodityCategorySub',args=(pk,)))
        record = Commodity_Category_Sub(category=category,title=title.upper())
        record.save()
        messages.success(request,"Record Added Successfully")
        return  HttpResponseRedirect(reverse('addCommodityCategorySub',args=(pk,)))


    context={
    'task_array':task_array,
    'form':form,
    'records':records,
    'category':category,
    'url':'addCommodityCategorySub',
    'button_text':"Add Record",
    'title':title,
    }
    return render(request,'master_templates/addCommodityCategorySub.html', context)



def Manage_Commodity_Sub_Categories_Delete(request,pk):
    record=Commodity_Category_Sub.objects.get(id=pk)
    return_pk = record.category.pk
    record.delete()
    messages.success(request,'Record Deleted Successfully')
    return  HttpResponseRedirect(reverse('addCommodityCategorySub',args=(return_pk,)))

def Manage_Commodity_Categories_Title_Update(request,pk):
    task_array=[]
    if not request.user.user_type == '1':
        tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
        for task in tasks:
            task_array.append(task.task.title)
    record=Commodity_Categories.objects.get(id=pk)
    form = Manage_Commodity_Categories_Title_Update_form(request.POST or None)

    if request.method == 'POST':
        title = request.POST.get('title')
        record.title=title
        record.save()
        return HttpResponseRedirect(reverse('addCommodityCategory'))
    form.fields['title'].initial= record.title
    context={
    'task_array':task_array,
    'record':record,
    'form':form,
    }
    return render(request,'master_templates/Manage_Commodity_Categories_Title_Update.html',context)




def Manage_Commodity_Categories_Core_properties_Transactions_Load(request):
    task_array=[]
    if not request.user.user_type == '1':
        tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
        for task in tasks:
            task_array.append(task.task.title)
    records =TransactionTypes.objects.filter(category='NON-MONETARY')
    context={
    'task_array':task_array,
    'records':records,
    }
    return render(request,'master_templates/Manage_Commodity_Categories_Core_properties_Transactions_Load.html',context)



def Manage_Commodity_Categories_Core_Values(request,pk):
    task_array=[]
    if not request.user.user_type == '1':
        tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
        for task in tasks:
            task_array.append(task.task.title)

    transaction =TransactionTypes.objects.get(id=pk)
    records=Commodity_Categories.objects.filter(transaction=transaction)

    context={
    'task_array':task_array,
    'records':records,
    }
    return render(request,'master_templates/Manage_Commodity_Categories_Core_Values.html', context)






def Manage_Commodity_Categories_Core_properties(request,pk):
    task_array=[]
    if not request.user.user_type == '1':
        tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
        for task in tasks:
            task_array.append(task.task.title)


    interest_rate_form = Manage_Commodity_Categories_Optional_properties_Form(request.POST or None)
    admin_charges_form = Manage_Commodity_Categories_Optional_properties_Form(request.POST or None)
    guarantor_form = Manage_Commodity_Categories_Optional_properties_Form(request.POST or None)

    record=Commodity_Categories.objects.get(id=pk)
    if request.method == 'POST' and 'btn-interest' in request.POST:
        interest_rate_required = request.POST.get('interest_rate_required')
        record.interest_rate_required=interest_rate_required
        record.interest_rate=0
        record.save()
        return HttpResponseRedirect(reverse('Manage_Commodity_Categories_Core_properties',args=(pk,)))

    if request.method == 'POST' and 'btn-admin' in request.POST:
        admin_charges_required = request.POST.get('admin_charges_required')
        record.admin_charges_required=admin_charges_required
        record.admin_charges=0
        record.save()
        return HttpResponseRedirect(reverse('Manage_Commodity_Categories_Core_properties',args=(pk,)))

    if request.method == 'POST' and 'btn-guarantor' in request.POST:
        guarantor_required = request.POST.get('guarantor_required')
        record.guarantor_required=guarantor_required
        record.guarantors=0
        record.save()

        return HttpResponseRedirect(reverse('Manage_Commodity_Categories_Core_properties',args=(pk,)))

    interest_rate_form.fields['interest_rate_required'].initial=record.interest_rate_required
    admin_charges_form.fields['admin_charges_required'].initial=record.admin_charges_required
    guarantor_form.fields['guarantor_required'].initial=record.guarantor_required
    context={
    'task_array':task_array,
    'interest_rate_form':interest_rate_form,
    'admin_charges_form':admin_charges_form,
    'guarantor_form':guarantor_form,
    'record':record,
    }
    return render(request,'master_templates/Manage_Commodity_Categories_Optional_properties.html', context)


def Manage_Commodity_Categories_Peripherals_Transactions_Load(request):
    task_array=[]
    if not request.user.user_type == '1':
        tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
        for task in tasks:
            task_array.append(task.task.title)
    records =TransactionTypes.objects.filter(category='NON-MONETARY')
    context={
    'task_array':task_array,
    'records':records,
    }
    return render(request,'master_templates/Manage_Commodity_Categories_Peripherals_Transactions_Load.html',context)


def Manage_Commodity_Categories_Peripherals(request,pk):
    task_array=[]
    if not request.user.user_type == '1':
        tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
        for task in tasks:
            task_array.append(task.task.title)

    transaction =TransactionTypes.objects.get(id=pk)
    records=Commodity_Categories.objects.filter(transaction=transaction)


    context={
    'task_array':task_array,
    'records':records,
    }
    return render(request,'master_templates/Manage_Commodity_Categories_Peripherals.html', context)



def Manage_Commodity_Categories_Update(request,pk):
    task_array=[]
    if not request.user.user_type == '1':
        tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
        for task in tasks:
            task_array.append(task.task.title)
    form = addCommodityCategoryForm(request.POST or None)
    record=Commodity_Categories.objects.get(id=pk)

    if request.method == 'POST':

        title = request.POST.get('title')
        if record.interest_rate_required == '1':
            interest_deduction_id = request.POST.get('interest_deductions')

            interest_rate = request.POST.get('interest_rate')

            if interest_rate <= "0":
                messages.error(request,'Interest Rate is Missing')
                return HttpResponseRedirect(reverse('Manage_Commodity_Categories_Update',args=(pk,)))

        if record.admin_charges_required == '1':
            admin_charges_rating = request.POST.get('admin_charges_rating')


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



        receipt_type = request.POST.get('receipt_type')


        if record.interest_rate_required == '1':
            record.interest_rate=interest_rate

        if record.admin_charges_required == '1':
            record.admin_charges_rating=admin_charges_rating
            record.admin_charges=admin_charges


        if record.guarantor_required == '1':
            record.guarantors=guarantors

        record.title=title
        record.duration=duration
        record.loan_age=loan_age
        record.receipt_type=receipt_type
        record.save()


        return HttpResponseRedirect(reverse('Manage_Commodity_Categories_Peripherals',args=(record.transaction_id,)))
    form.fields['title'].initial=record.title

    form.fields['interest_rate'].initial=record.interest_rate
    form.fields['duration'].initial=record.duration
    form.fields['loan_age'].initial=record.loan_age
    form.fields['guarantors'].initial=record.guarantors
    form.fields['receipt_type'].initial=record.receipt_type
    form.fields['admin_charges_rating'].initial=record.admin_charges_rating
    form.fields['admin_charges'].initial=record.admin_charges

    context={
    'task_array':task_array,
    'form':form,
    'record':record,
    }
    return render(request,'master_templates/Manage_Commodity_Categories_Update.html', context)


def addGender(request):
    task_array=[]
    if not request.user.user_type == '1':
        tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
        for task in tasks:
            task_array.append(task.task.title)
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
    'task_array':task_array,
    'form':form,
    'items':items,
    'url':'addGender',
    'button_text':"Add Record",
    'title':title,
    }
    return render(request,'master_templates/add_single_item.html', context)

def Manage_Gender(request):
    task_array=[]
    if not request.user.user_type == '1':
        tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
        for task in tasks:
            task_array.append(task.task.title)
    title="Manage Gender"
    items= Gender.objects.all()


    context={
    'task_array':task_array,
    'items':items,
    'title':title,
    }
    return render(request,'master_templates/Manage_Gender.html', context)


def Manage_Gender_Processing(request,pk):
    task_array=[]
    if not request.user.user_type == '1':
        tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
        for task in tasks:
            task_array.append(task.task.title)

    form=Manage_Departments_Processing_form(request.POST or None)
    title="Manage Departments"
    item= Gender.objects.get(id=pk)

    if request.method == 'POST':
        title=request.POST.get('title')

        item.title=title
        item.save()
        return HttpResponseRedirect(reverse('Manage_Gender'))
    form.fields['title'].initial=item.title
    context={
    'form':form,
    'task_array':task_array,
    'item':item,
    'title':title,
    }
    return render(request,'master_templates/Manage_Gender_Processing.html', context)



def addSalaryInstitution(request):
    task_array=[]
    if not request.user.user_type == '1':
        tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
        for task in tasks:
            task_array.append(task.task.title)
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
    'task_array':task_array,
    'form':form,
    'items':items,
    'url':'addSalaryInstitution',
    'button_text':"Add Record",
    'title':title,
    }
    return render(request,'master_templates/add_single_item.html', context)



def Manage_Salary_Institution(request):
    task_array=[]
    if not request.user.user_type == '1':
        tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
        for task in tasks:
            task_array.append(task.task.title)
    title="Manage Departments"
    items= SalaryInstitution.objects.all()


    context={
    'task_array':task_array,
    'items':items,
    'title':title,
    }
    return render(request,'master_templates/Manage_Salary_Institution.html', context)


def Manage_Salary_Institution_Processing(request,pk):
    task_array=[]
    if not request.user.user_type == '1':
        tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
        for task in tasks:
            task_array.append(task.task.title)

    form=Manage_Departments_Processing_form(request.POST or None)
    title="Manage Departments"
    item= SalaryInstitution.objects.get(id=pk)

    if request.method == 'POST':
        title=request.POST.get('title')

        item.title=title
        item.save()
        return HttpResponseRedirect(reverse('Manage_Salary_Institution'))
    form.fields['title'].initial=item.title
    context={
    'form':form,
    'task_array':task_array,
    'item':item,
    'title':title,
    }
    return render(request,'master_templates/Manage_Salary_Institution_Processing.html', context)


def addTitles(request):
    task_array=[]
    if not request.user.user_type == '1':
        tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
        for task in tasks:
            task_array.append(task.task.title)
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
    'task_array':task_array,
    'form':form,
    'items':items,
    'url':'addTitles',
    'button_text':"Add Record",
    'title':title,
    }
    return render(request,'master_templates/add_single_item.html', context)


def Manage_Titles(request):
    task_array=[]
    if not request.user.user_type == '1':
        tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
        for task in tasks:
            task_array.append(task.task.title)
    title="Manage Titles"
    items= Titles.objects.all()


    context={
    'task_array':task_array,
    'items':items,
    'title':title,
    }
    return render(request,'master_templates/Manage_Titles.html', context)


def Manage_Titles_Processing(request,pk):
    task_array=[]
    if not request.user.user_type == '1':
        tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
        for task in tasks:
            task_array.append(task.task.title)

    form=Manage_Departments_Processing_form(request.POST or None)
    title="Manage Titles"
    item= Titles.objects.get(id=pk)

    if request.method == 'POST':
        title=request.POST.get('title')

        item.title=title
        item.save()
        return HttpResponseRedirect(reverse('Manage_Titles'))
    form.fields['title'].initial=item.title
    context={
    'form':form,
    'task_array':task_array,
    'item':item,
    'title':title,
    }
    return render(request,'master_templates/Manage_Titles_Processing.html', context)



def addDepartments(request):
    task_array=[]
    if not request.user.user_type == '1':
        tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
        for task in tasks:
            task_array.append(task.task.title)
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
    'task_array':task_array,
    'form':form,
    'items':items,
    'url':'addDepartments',
    'button_text':"Add Record",
    'title':title,
    }
    return render(request,'master_templates/add_single_item.html', context)




def Manage_Departments(request):
    task_array=[]
    if not request.user.user_type == '1':
        tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
        for task in tasks:
            task_array.append(task.task.title)
    title="Manage Departments"
    items= Departments.objects.all()


    context={
    'task_array':task_array,
    'items':items,
    'title':title,
    }
    return render(request,'master_templates/Manage_Departments.html', context)


def Manage_Departments_Processing(request,pk):
    task_array=[]
    if not request.user.user_type == '1':
        tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
        for task in tasks:
            task_array.append(task.task.title)

    form=Manage_Departments_Processing_form(request.POST or None)
    title="Manage Departments"
    item= Departments.objects.get(id=pk)

    if request.method == 'POST':
        title=request.POST.get('title')

        item.title=title
        item.save()
        return HttpResponseRedirect(reverse('Manage_Departments'))
    form.fields['title'].initial=item.title
    context={
    'form':form,
    'task_array':task_array,
    'item':item,
    'title':title,
    }
    return render(request,'master_templates/Manage_Departments_Processing.html', context)


def addBanks(request):
    task_array=[]
    if not request.user.user_type == '1':
        tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
        for task in tasks:
            task_array.append(task.task.title)
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
        return  HttpResponseRedirect(reverse('addBanks'))
    context={
    'task_array':task_array,
    'form':form,
    'items':items,
    'url':'addBanks',
    'button_text':"Add Record",
    'title':title,
    }
    return render(request,'master_templates/add_single_item.html', context)



def Manage_Banks(request):
    task_array=[]
    if not request.user.user_type == '1':
        tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
        for task in tasks:
            task_array.append(task.task.title)
    title="Manage Departments"
    items= Banks.objects.all()


    context={
    'task_array':task_array,
    'items':items,
    'title':title,
    }
    return render(request,'master_templates/Manage_Banks.html', context)


def Manage_Banks_Processing(request,pk):
    task_array=[]
    if not request.user.user_type == '1':
        tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
        for task in tasks:
            task_array.append(task.task.title)

    form=Manage_Departments_Processing_form(request.POST or None)
    title="Manage Departments"
    item= Banks.objects.get(id=pk)

    if request.method == 'POST':
        title=request.POST.get('title')

        item.title=title
        item.save()
        return HttpResponseRedirect(reverse('Manage_Banks'))
    form.fields['title'].initial=item.title
    context={
    'form':form,
    'task_array':task_array,
    'item':item,
    'title':title,
    }
    return render(request,'master_templates/Manage_Banks_Processing.html', context)




def addLocations(request):
    task_array=[]
    if not request.user.user_type == '1':
        tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
        for task in tasks:
            task_array.append(task.task.title)
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
    'task_array':task_array,
    'form':form,
    'items':items,
    'url':'addLocations',
    'button_text':"Add Record",
    'title':title,
    }
    return render(request,'master_templates/add_single_item.html', context)

def Manage_Locations(request):
    task_array=[]
    if not request.user.user_type == '1':
        tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
        for task in tasks:
            task_array.append(task.task.title)
    title="Manage Departments"
    items= Locations.objects.all()


    context={
    'task_array':task_array,
    'items':items,
    'title':title,
    }
    return render(request,'master_templates/Manage_Locations.html', context)


def Manage_Locations_Processing(request,pk):
    task_array=[]
    if not request.user.user_type == '1':
        tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
        for task in tasks:
            task_array.append(task.task.title)

    form=Manage_Departments_Processing_form(request.POST or None)
    title="Manage Departments"
    item= Locations.objects.get(id=pk)

    if request.method == 'POST':
        title=request.POST.get('title')

        item.title=title
        item.save()
        return HttpResponseRedirect(reverse('Manage_Locations'))
    form.fields['title'].initial=item.title
    context={
    'form':form,
    'task_array':task_array,
    'item':item,
    'title':title,
    }
    return render(request,'master_templates/Manage_Locations_Processing.html', context)


def addDefaultPassword(request):
    task_array=[]
    if not request.user.user_type == '1':
        tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
        for task in tasks:
            task_array.append(task.task.title)
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
    'task_array':task_array,
    'form':form,
    'item':item,
    'url':'addDefaultPassword',
    'button_text':"Add Record",
    'title':title,
    }
    return render(request,'master_templates/add_single_item.html', context)


def TransactionTypes_Sources_Manage(request):
    task_array=[]
    if not request.user.user_type == '1':
        tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
        for task in tasks:
            task_array.append(task.task.title)
    records = TransactionSources.objects.all()

    context={
    'task_array':task_array,
    'records':records,
    }
    return render(request,'master_templates/TransactionTypes_Sources_Manage.html',context)

def TransactionTypes_Sources_Manage_Process(request,pk):
    task_array=[]
    if not request.user.user_type == '1':
        tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
        for task in tasks:
            task_array.append(task.task.title)

    form=TransactionTypes_Sources_Manage_Process_form(request.POST or None)
    record = TransactionSources.objects.get(id=pk)

    if request.method == 'POST':
        maximum_amount=request.POST.get('maximum_amount')
        salary_rate=request.POST.get('salary_rate')
        loan_based_saving=request.POST.get('loan_based_saving')

        if not maximum_amount:
            maximum_amount=0

        if not salary_rate:
            salary_rate=0

        if not loan_based_saving:
            loan_based_saving=0


        record.maximum_amount=maximum_amount
        record.salary_loan_relationship=salary_rate
        record.loan_based_saving=loan_based_saving
        record.save()
        return HttpResponseRedirect(reverse('TransactionTypes_Sources_Manage_Process',args=(pk,)))

    form.fields['maximum_amount'].initial=record.maximum_amount
    form.fields['salary_rate'].initial=record.salary_loan_relationship
    form.fields['loan_based_saving'].initial=record.loan_based_saving
    context={
    'task_array':task_array,
    'record':record,
    'form':form,
    }
    return render(request,'master_templates/TransactionTypes_Sources_Manage_Process.html',context)


def addTransactionTypes(request):
    task_array=[]
    if not request.user.user_type == '1':
        tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
        for task in tasks:
            task_array.append(task.task.title)
    transaction_types = TransactionTypes.objects.all().order_by("code")
    form=addTransactionTypesForm(request.POST or None)

    if request.method=="POST":
        form = addTransactionTypesForm(request.POST)

        source_id=request.POST.get("source")
        source = TransactionSources.objects.get(id=source_id)
        code=request.POST.get("code")
        name=request.POST.get("name")

        # share_unit_min=request.POST.get("share_unit_min")
        # share_unit_max=request.POST.get("share_unit_max")
        # maximum_amount=request.POST.get("maximum_amount")
        # minimum_amount=request.POST.get("minimum_amount")
        # receipts=request.POST.get("receipts")
        # rank=request.POST.get("rank")





        form_print='NO'
        multiple_loan_status='NOT ALLOWED'
        if TransactionTypes.objects.filter(code=code).exists():
            messages.error(request,"Record with this code already exist")
            return HttpResponseRedirect(reverse('addTransactionTypes'))

        # record = TransactionTypes(multiple_loan_status=multiple_loan_status,status='ACTIVE',receipt_type=receipts,form_print=form_print,source=source,code=code,name=name,maximum_amount=maximum_amount,minimum_amount=minimum_amount,rank=rank,share_unit_min=share_unit_min,share_unit_max=share_unit_max)
        record = TransactionTypes(multiple_loan_status=multiple_loan_status,status='ACTIVE',form_print=form_print,source=source,code=code,name=name)
        record.save()
        return HttpResponseRedirect(reverse('addTransactionTypes'))
    context={
    'task_array':task_array,
    'form':form,
    'transaction_types':transaction_types,
    }
    return render(request, 'master_templates/addTransactionTypes.html',context)

def addTransactionTypes_Remove(request,pk):
    TransactionTypes.objects.filter(id=pk).delete()
    return HttpResponseRedirect(reverse('addTransactionTypes'))

def TransactionTypes_Manage_Load(request):
    task_array=[]
    if not request.user.user_type == '1':
        tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
        for task in tasks:
            task_array.append(task.task.title)
    transaction_types = TransactionTypes.objects.all().order_by("code")

    context={
    'task_array':task_array,

    'transaction_types':transaction_types,
    }
    return render(request,'master_templates/TransactionTypes_Manage_Load.html',context)



def TransactionTypes_Ranking_Load(request):
    task_array=[]
    if not request.user.user_type == '1':
        tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
        for task in tasks:
            task_array.append(task.task.title)
    records = TransactionTypes.objects.filter(Q(source__title='SAVINGS') | Q(source__title='LOAN')).order_by("rank")

    context={
    'task_array':task_array,

    'records':records,
    }
    return render(request,'master_templates/TransactionTypes_Ranking_Load.html',context)


def TransactionTypes_Ranking_Update(request,pk):
    task_array=[]
    if not request.user.user_type == '1':
        tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
        for task in tasks:
            task_array.append(task.task.title)
    record = TransactionTypes.objects.get(id=pk)
    form = loan_rank_update_form(request.POST or None)

    if request.method == 'POST':
        rank = request.POST.get('rank')

        record.rank = rank
        record.save()
        return HttpResponseRedirect(reverse('TransactionTypes_Ranking_Load'))
    form.fields['rank'].initial= record.rank
    context={
    'task_array':task_array,
    'record':record,
    'form':form,
    }
    return render(request,'master_templates/TransactionTypes_Ranking_Update.html',context)




def TransactionTypes_Update(request,pk):
    task_array=[]
    if not request.user.user_type == '1':
        tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
        for task in tasks:
            task_array.append(task.task.title)
    form=addTransactionTypes_update_Form(request.POST or None)
    transaction = TransactionTypes.objects.get(id=pk)
    form.fields['code'].initial=transaction.code
    form.fields['name'].initial=transaction.name
    form.fields['source'].initial=transaction.source.id

    # form.fields['rank'].initial=transaction.rank
    # form.fields['receipts'].initial=transaction.receipt_type
    # if transaction.maximum_amount:
    #     form.fields['maximum_amount'].initial=transaction.maximum_amount
    # else:
    #     form.fields['maximum_amount'].initial=0

    # if transaction.minimum_amount:
    #     form.fields['minimum_amount'].initial=transaction.minimum_amount
    # else:
    #     form.fields['minimum_amount'].initial=0
    # form.fields['share_unit_min'].initial=transaction.share_unit_min
    # form.fields['share_unit_max'].initial=transaction.share_unit_max
    # form.fields['form_print'].initial=transaction.form_print

    if request.method == "POST":
        receipts=request.POST.get('receipts')
        source_id = request.POST.get('source')
        source = TransactionSources.objects.get(id=source_id)

        # form_print = request.POST.get('form_print')

        code=request.POST.get('code')
        name=request.POST.get('name')
        # rank=request.POST.get('rank')
        # maximum_amount=request.POST.get('maximum_amount')
        # minimum_amount=request.POST.get('minimum_amount')
        # share_unit_min=request.POST.get('share_unit_min')
        # share_unit_max=request.POST.get('share_unit_max')

        transaction.code=code
        transaction.name=name
        transaction.source=source
        # transaction.receipt_type=receipts
        # transaction.rank=rank
        # transaction.maximum_amount=maximum_amount
        # transaction.minimum_amount=minimum_amount
        # transaction.share_unit_min=share_unit_min
        # transaction.share_unit_max=share_unit_max
        # transaction.form_print=form_print

        transaction.save()
        return HttpResponseRedirect(reverse('TransactionTypes_Manage_Load'))

    context={
    'task_array':task_array,
    'form':form,
    'transaction':transaction,
    }
    return render(request,'master_templates/TransactionTypes_Update.html',context)


def FormAutoPrint_Settings(request):
    task_array=[]
    if not request.user.user_type == '1':
        tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
        for task in tasks:
            task_array.append(task.task.title)
    form = FormAutoPrint_Settings_Form(request.POST or None)
    items = FormAutoPrints.objects.all()
    if request.method == 'POST':
        title=request.POST.get("title")
        status = request.POST.get("status")


        FormAutoPrints(title=title,status=status).save()
        return HttpResponseRedirect(reverse('FormAutoPrint_Settings'))
    context={
    'task_array':task_array,
    'form':form,
    'items':items,
    }
    return render(request,'master_templates/FormAutoPrint_Settings.html',context)



def FormAutoPrint_SettingsUpdate(request,pk):
    task_array=[]
    if not request.user.user_type == '1':
        tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
        for task in tasks:
            task_array.append(task.task.title)
    form = FormAutoPrint_Settings_Update_Form(request.POST or None)
    item = FormAutoPrints.objects.get(id=pk)

    if request.method == 'POST':
        title=request.POST.get('title')
        status=request.POST.get('status')



        item.title=title
        item.status=status
        item.save()
        return HttpResponseRedirect(reverse('FormAutoPrint_Settings'))
    form.fields['title'].initial=item.title
    form.fields['status'].initial=item.status
    context={
    'task_array':task_array,
    'form':form,
    'items':item,
    }
    return render(request,'master_templates/FormAutoPrint_SettingsUpdate.html',context)






####################################################################
###################### LOAN RELATED MATTERS ########################
####################################################################

def loan_based_savings_update(request):
    task_array=[]
    if not request.user.user_type == '1':
        tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
        for task in tasks:
            task_array.append(task.task.title)
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
    'task_array':task_array,
    'form':form,
    'saving':saving,
    }
    return render(request, 'master_templates/loan_based_savings.html',context)

def loan_category_settings(request):
    task_array=[]
    if not request.user.user_type == '1':
        tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
        for task in tasks:
            task_array.append(task.task.title)
    form=loan_category_settings_form(request.POST or None)
    records = TransactionTypes.objects.filter(source__title="LOAN")

    if request.method == 'POST':
        loan_id=request.POST.get('loan')
        loan=TransactionTypes.objects.get(id=loan_id)

        category=request.POST.get('category')


        loan.category=category
        loan.save()
        return HttpResponseRedirect(reverse('loan_category_settings'))
    context={
    'task_array':task_array,
    'records':records,
    'form':form,
    }
    return render(request, 'master_templates/loan_category_settings.html',context)


def loan_settings_load(request):
    task_array=[]
    if not request.user.user_type == '1':
        tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
        for task in tasks:
            task_array.append(task.task.title)
    records = TransactionTypes.objects.filter(source__title="LOAN",category='MONETARY')
    context={
    'task_array':task_array,
    'records':records,
    }
    return render(request, 'master_templates/loan_settings_load.html',context)

def Savings_Manager_load(request):
    task_array=[]
    if not request.user.user_type == '1':
        tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
        for task in tasks:
            task_array.append(task.task.title)
    records = TransactionTypes.objects.filter(source__title="SAVINGS")

    context={
    'task_array':task_array,
    'records':records,

    }
    return render(request, 'master_templates/Savings_Manager_load.html',context)


def Savings_Manager_Update(request,pk):
    task_array=[]
    if not request.user.user_type == '1':
        tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
        for task in tasks:
            task_array.append(task.task.title)
    record = TransactionTypes.objects.get(id=pk)
    form = Savings_Manager_Update_form(request.POST or None)


    if request.method == 'POST':
        amount = request.POST.get('amount')
        record.minimum_amount=amount
        record.save()
        return HttpResponseRedirect(reverse('Savings_Manager_load'))

    form.fields['amount'].initial = record.minimum_amount
    context={
    'task_array':task_array,
    'record':record,
    'form':form,
    }
    return render(request, 'master_templates/Savings_Manager_Update.html',context)


def loan_settings_details_load(request,pk):
    task_array=[]
    if not request.user.user_type == '1':
        tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
        for task in tasks:
            task_array.append(task.task.title)
    record = TransactionTypes.objects.get(id=pk)
    saving= LoanBasedSavings.objects.first()
    context={
    'task_array':task_array,
    'record':record,
    'saving':saving,
    'pk':pk,
    }
    return render(request, 'master_templates/loan_settings_details_load.html',context)


def loan_guarantors_gross_pay_update(request,pk):
    task_array=[]
    if not request.user.user_type == '1':
        tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
        for task in tasks:
            task_array.append(task.task.title)
    item= TransactionTypes.objects.get(id=pk)
    title="Update Loan Guarantors Gross Pay Rate for " +  item.name
    instructions='''
    This page enable you to set the Gaurantors Gross Pay Rating
    needed to access this loan.
    '''
    form = loan_guarantors_gross_pay_update_form(request.POST or None)

    if request.method ==  "POST":
        form = loan_guarantors_gross_pay_update_form(request.POST)
        if form.is_valid():
            guarantors_gross_pay_rating=form.cleaned_data["guarantors_gross_pay_rating"]

            item.guarantors_gross_pay_rating=guarantors_gross_pay_rating
            item.save()
            messages.success(request,"Record Updated Successfully")
            return  HttpResponseRedirect(reverse('loan_settings_details_load',args=(pk,)))

    form.fields['guarantors_gross_pay_rating'].initial=item.guarantors_gross_pay_rating
    context={
    'task_array':task_array,
    'form':form,
    'instructions':instructions,
    'url':'loan_guarantors_update',
    'button_text':"Update Record",
    'title':title,
    }
    return render(request,'master_templates/loan_criteria_update.html', context)




def loan_guarantors_update(request,pk):
    task_array=[]
    if not request.user.user_type == '1':
        tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
        for task in tasks:
            task_array.append(task.task.title)
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
    'task_array':task_array,
    'form':form,
    'instructions':instructions,
    'url':'loan_guarantors_update',
    'button_text':"Update Record",
    'title':title,
    }
    return render(request,'master_templates/loan_criteria_update.html', context)


def default_admin_charges_update(request,pk):
    task_array=[]
    if not request.user.user_type == '1':
        tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
        for task in tasks:
            task_array.append(task.task.title)
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
    'task_array':task_array,
    'form':form,
    'instructions':instructions,
    'url':'default_admin_charges_update',
    'button_text':"Update Record",
    'title':title,
    }
    return render(request,'master_templates/loan_criteria_update.html', context)


def MultipleLoanStatus_update(request,pk):
    task_array=[]
    if not request.user.user_type == '1':
        tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
        for task in tasks:
            task_array.append(task.task.title)
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
            multiple_loan_status=form.cleaned_data["multiple_loan_status"]
            record = TransactionTypes.objects.get(id=pk)
            record.multiple_loan_status=multiple_loan_status
            record.save()
            messages.success(request,"Record Updated Successfully")
            return  HttpResponseRedirect(reverse('loan_settings_details_load',args=(pk,)))

    form.fields['multiple_loan_status'].initial=item.multiple_loan_status
    context={
    'task_array':task_array,
    'form':form,
    'instructions':instructions,
    'url':'MultipleLoanStatus_update',
    'button_text':"Update Record",
    'title':title,
    }
    return render(request,'master_templates/loan_criteria_update.html', context)


def auto_stop_savings_update(request,pk):
    task_array=[]
    if not request.user.user_type == '1':
        tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
        for task in tasks:
            task_array.append(task.task.title)
    item= TransactionTypes.objects.get(id=pk)
    title="Update Auto Stop Savings for " +  item.name
    instructions='''
    This page enable you to Manage Auto Stop Saving Anchored for for this loan.
    '''
    form = auto_stop_savings_update_form(request.POST or None)

    if request.method ==  "POST":
        if form.is_valid():
            auto_stop_savings=form.cleaned_data["auto_stop_savings"]

            item.auto_stop_savings=auto_stop_savings
            item.save()
            messages.success(request,"Record Updated Successfully")
            return  HttpResponseRedirect(reverse('loan_settings_details_load',args=(pk,)))

    form.fields['auto_stop_savings'].initial=item.auto_stop_savings
    context={
    'task_array':task_array,
    'form':form,
    'instructions':instructions,
    'url':'auto_stop_savings_update',
    'button_text':"Update Record",
    'title':title,
    }
    return render(request,'master_templates/loan_criteria_update.html', context)



def receipt_types_settings(request,pk):
    task_array=[]
    if not request.user.user_type == '1':
        tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
        for task in tasks:
            task_array.append(task.task.title)
    item= TransactionTypes.objects.get(id=pk)
    title="Update Receipt Type for " +  item.name
    instructions='''
    This page enable you to Manage Receipt Type for for this loan.
    '''
    form = receipt_types_settings_form(request.POST or None)

    if request.method ==  "POST":
        if form.is_valid():
            receipt_type=form.cleaned_data["receipt_type"]

            item.receipt_type=receipt_type
            item.save()
            messages.success(request,"Record Updated Successfully")
            return  HttpResponseRedirect(reverse('loan_settings_details_load',args=(pk,)))

    form.fields['receipt_type'].initial=item.receipt_type
    context={
    'task_array':task_array,
    'form':form,
    'instructions':instructions,
    'url':'receipt_types_settings',
    'button_text':"Update Record",
    'title':title,
    }
    return render(request,'master_templates/loan_criteria_update.html', context)


def loan_savings_based_update(request,pk):
    task_array=[]
    if not request.user.user_type == '1':
        tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
        for task in tasks:
            task_array.append(task.task.title)
    item= TransactionTypes.objects.get(id=pk)
    title="Update Loan Savings Based for " +  item.name
    instructions='''
    This page enable you to set whether this transaction is based on a certain savings.
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
    'task_array':task_array,
    'form':form,
    'instructions':instructions,
    'url':'loan_savings_based_update',
    'button_text':"Update Record",
    'title':title,
    }
    return render(request,'master_templates/loan_criteria_update.html', context)


def loan_savings_based_Rate_update(request,pk):
    task_array=[]
    if not request.user.user_type == '1':
        tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
        for task in tasks:
            task_array.append(task.task.title)
    item= TransactionTypes.objects.get(id=pk)
    title="Update Loan Savings Based Rate for " +  item.name
    instructions='''
    This page enable you to set the percentage amout to be saved in
    order to access a given loan.
    '''
    form = loan_savings_based_Rate_update_form(request.POST or None)

    if request.method ==  "POST":

        if form.is_valid():
            saving_rating=form.cleaned_data["loan_savings_based_rate"]
            record = TransactionTypes.objects.get(id=pk)
            record.saving_rating=saving_rating
            record.save()
            messages.success(request,"Record Updated Successfully")
            return  HttpResponseRedirect(reverse('loan_settings_details_load',args=(pk,)))

    form.fields['loan_savings_based_rate'].initial=item.saving_rating
    context={
    'task_array':task_array,
    'form':form,
    'instructions':instructions,
    'url':'loan_savings_based_Rate_update',
    'button_text':"Update Record",
    'title':title,
    }
    return render(request,'master_templates/loan_criteria_update.html', context)



def loan_category_update(request,pk):
    task_array=[]
    if not request.user.user_type == '1':
        tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
        for task in tasks:
            task_array.append(task.task.title)
    item= TransactionTypes.objects.get(id=pk)
    title="Update Loan Category for " +  item.name
    instructions='''
    This page enable you to set whether a loan is monetary or Not.
    '''
    form = loan_category_update_form(request.POST or None)

    if request.method ==  "POST":
        form = loan_category_update_form(request.POST)
        if form.is_valid():
            category=form.cleaned_data["category"]

            record = TransactionTypes.objects.get(id=pk)
            record.category=category
            record.save()
            messages.success(request,"Record Updated Successfully")
            return  HttpResponseRedirect(reverse('loan_settings_details_load',args=(pk,)))

    form.fields['category'].initial=item.category
    context={
    'task_array':task_array,
    'form':form,
    'instructions':instructions,
    'url':'loan_category_update',
    'button_text':"Update Record",
    'title':title,
    }
    return render(request,'master_templates/loan_criteria_update.html', context)


def loan_duration_update(request,pk):
    task_array=[]
    if not request.user.user_type == '1':
        tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
        for task in tasks:
            task_array.append(task.task.title)
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
    'task_array':task_array,
    'form':form,
    'instructions':instructions,
    'url':'loan_duration_update',
    'button_text':"Update Record",
    'title':title,
    }
    return render(request,'master_templates/loan_criteria_update.html', context)


def loan_name_update(request,pk):
    task_array=[]
    if not request.user.user_type == '1':
        tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
        for task in tasks:
            task_array.append(task.task.title)
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
    'task_array':task_array,
    'form':form,
    'instructions':instructions,
    'url':'loan_name_update',
    'button_text':"Update Record",
    'title':title,
    }
    return render(request,'master_templates/loan_criteria_update.html', context)


def loan_interest_rate_update(request,pk):
    task_array=[]
    if not request.user.user_type == '1':
        tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
        for task in tasks:
            task_array.append(task.task.title)
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
    'task_array':task_array,
    'form':form,
    'instructions':instructions,
    'url':'loan_interest_rate_update',
    'button_text':"Update Record",
    'title':title,
    }
    return render(request,'master_templates/loan_criteria_update.html', context)


def loan_interest_deduction_soucrces_update(request,pk):
    task_array=[]
    if not request.user.user_type == '1':
        tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
        for task in tasks:
            task_array.append(task.task.title)
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
            interest_deduction=form.cleaned_data["source"]
            record = TransactionTypes.objects.get(id=pk)
            record.interest_deduction=interest_deduction
            record.save()
            messages.success(request,"Record Updated Successfully")
            return	HttpResponseRedirect(reverse('loan_settings_details_load',args=(pk,)))

    form.fields['source'].initial=item.interest_deduction
    context={
    'task_array':task_array,
    'form':form,
    'instructions':instructions,
    'url':'loan_interest_deduction_soucrces_update',
    'button_text':"Update Record",
    'title':title,
    }
    return render(request,'master_templates/loan_criteria_update.html', context)


def loan_maximum_amount_update(request,pk):
    task_array=[]
    if not request.user.user_type == '1':
        tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
        for task in tasks:
            task_array.append(task.task.title)
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
    'task_array':task_array,
    'form':form,
    'instructions':instructions,
    'url':'loan_maximum_amount_update',
    'button_text':"Update Record",
    'title':title,
    }
    return render(request,'master_templates/loan_criteria_update.html', context)


# def loan_rank_update_update(request,pk):
#     task_array=[]
#     if not request.user.user_type == '1':
#         tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
#         for task in tasks:
#             task_array.append(task.task.title)
#     item= TransactionTypes.objects.get(id=pk)
#     title="Update Loan Rank  for " +  item.name
#     instructions='''
#     This page enable you to set the order in which
#     monthly deduction shall flow fro the bulk deduction.
#     '''

#     form = loan_rank_update_form(request.POST or None)

#     if request.method ==  "POST":
#         form = loan_rank_update_form(request.POST)
#         if form.is_valid():
#             rank=form.cleaned_data["rank"]
#             record = TransactionTypes.objects.get(id=pk)
#             record.rank=rank
#             record.save()
#             messages.success(request,"Record Updated Successfully")
#             return	HttpResponseRedirect(reverse('loan_settings_details_load',args=(pk,)))

#     form.fields['rank'].initial=item.rank
#     context={
#     'task_array':task_array,
#     'form':form,
#     'instructions':instructions,
#     'url':'loan_rank_update_update',
#     'button_text':"Update Record",
#     'title':title,
#     }
#     return render(request,'master_templates/loan_criteria_update.html', context)


def loan_admin_charges_rate_update(request,pk):
    task_array=[]
    if not request.user.user_type == '1':
        tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
        for task in tasks:
            task_array.append(task.task.title)
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
            admin_charges_rating=form.cleaned_data["admin_charges_rating"]

            record = TransactionTypes.objects.get(id=pk)
            record.admin_charges_rating=admin_charges_rating
            record.save()
            messages.success(request,"Record Updated Successfully")
            return	HttpResponseRedirect(reverse('loan_settings_details_load',args=(pk,)))

    form.fields['admin_charges_rating'].initial=item.admin_charges_rating
    context={
    'task_array':task_array,
    'form':form,
    'instructions':instructions,
    'url':'loan_admin_charges_rate_update',
    'button_text':"Update Record",
    'title':title,
    }
    return render(request,'master_templates/loan_criteria_update.html', context)


def loan_admin_charges_update(request,pk):
    task_array=[]
    if not request.user.user_type == '1':
        tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
        for task in tasks:
            task_array.append(task.task.title)
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
    'task_array':task_array,
    'form':form,
    'instructions':instructions,
    'url':'loan_admin_charges_update',
    'button_text':"Update Record",
    'title':title,
    }
    return render(request,'master_templates/loan_criteria_update.html', context)



def loan_admin_charges_minimum_update(request,pk):
    task_array=[]
    if not request.user.user_type == '1':
        tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
        for task in tasks:
            task_array.append(task.task.title)
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
    'task_array':task_array,
    'form':form,
    'instructions':instructions,
    'url':'loan_admin_charges_minimum_update',
    'button_text':"Update Record",
    'title':title,
    }
    return render(request,'master_templates/loan_criteria_update.html', context)


def loan_salary_relationship_update(request,pk):
    task_array=[]
    if not request.user.user_type == '1':
        tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
        for task in tasks:
            task_array.append(task.task.title)
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
    'task_array':task_array,
    'form':form,
    'instructions':instructions,
    'url':'loan_salary_relationship_update',
    'button_text':"Update Record",
    'title':title,
    }
    return render(request,'master_templates/loan_criteria_update.html', context)


def loan_loan_age_update(request,pk):
    task_array=[]
    if not request.user.user_type == '1':
        tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
        for task in tasks:
            task_array.append(task.task.title)
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
    'task_array':task_array,
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
def trending_commodity_signatories(request):
    task_array=[]
    if not request.user.user_type == '1':
        tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
        for task in tasks:
            task_array.append(task.task.title)
    records = Treanding_Commodity_Signatory.objects.all()
    form = trending_commodity_signatories_form(request.POST or None )
    if request.method == 'POST':
        name = request.POST.get('name')
        designation = request.POST.get('designation')
        phone_no = request.POST.get('phone_no')

        if not name:
            messages.error(request, "Name is missing")
            return HttpResponseRedirect(reverse('trending_commodity_signatories'))
        if not designation:
            messages.error(request, "Designation is missing")
            return HttpResponseRedirect(reverse('trending_commodity_signatories'))
        if not phone_no:
            messages.error(request, "Phone Number is missing")
            return HttpResponseRedirect(reverse('trending_commodity_signatories'))


        Treanding_Commodity_Signatory(name=name.upper(),designation=designation.upper(),phone_no=phone_no).save()
        return HttpResponseRedirect(reverse('trending_commodity_signatories'))

    context={
    'task_array':task_array,
    'form':form,
    'records':records,
    }
    return render(request, 'master_templates/trending_commodity_signatories.html',context)


def trending_commodity_signatories_delete(request,pk):
    Treanding_Commodity_Signatory.objects.filter(id=pk).delete()
    return HttpResponseRedirect(reverse('trending_commodity_signatories'))



def Commodity_SubCategeory_list_load(request):
    task_array=[]
    if not request.user.user_type == '1':
        tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
        for task in tasks:
            task_array.append(task.task.title)
    records = TransactionTypes.objects.filter(category='NON-MONETARY')
    context={
    'task_array':task_array,
    'records':records,
    }
    return render(request, 'master_templates/Commodity_SubCategeory_list_load.html',context)


def loan_settings_non_monetary_Sub_Categories_load(request,pk):
    task_array=[]
    if not request.user.user_type == '1':
        tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
        for task in tasks:
            task_array.append(task.task.title)
    records = Commodity_Categories.objects.filter(transaction_id=pk)
    context={
    'task_array':task_array,
    'records':records,
    }
    return render(request, 'master_templates/loan_settings_non_monetary_Sub_Categories_load.html',context)



def loan_settings_non_monetary_Sub_Categories_Preview(request,pk):
    task_array=[]
    if not request.user.user_type == '1':
        tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
        for task in tasks:
            task_array.append(task.task.title)
    records = Commodity_Category_Sub.objects.filter(category_id=pk)
    category = Commodity_Categories.objects.get(id=pk)
    context={
    'task_array':task_array,
    'category':category,
    'records':records,
    }
    return render(request, 'master_templates/loan_settings_non_monetary_Sub_Categories_Preview.html',context)


def loan_settings_non_monetary_Sub_Categories_Update(request,pk):

    record = Commodity_Category_Sub.objects.get(id=pk)
    return_pk=record.category.pk
    if record.status == 'ACTIVE':
        record.status = 'INACTIVE'
    elif record.status == 'INACTIVE':
        record.status = 'ACTIVE'
    record.save()
    return HttpResponseRedirect(reverse('loan_settings_non_monetary_Sub_Categories_Preview',args=(return_pk,)))

def loan_settings_non_monetary_list_load(request):
    task_array=[]
    if not request.user.user_type == '1':
        tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
        for task in tasks:
            task_array.append(task.task.title)
    records = TransactionTypes.objects.filter(category='NON-MONETARY')
    context={
    'task_array':task_array,
    'records':records,
    }
    return render(request, 'master_templates/loan_settings_non_monetary_list_load.html',context)



def loan_settings_non_monetary_Categories_load(request,pk):
    task_array=[]
    if not request.user.user_type == '1':
        tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
        for task in tasks:
            task_array.append(task.task.title)
    records = Commodity_Categories.objects.filter(transaction_id=pk)
    context={
    'task_array':task_array,
    'records':records,
    }
    return render(request, 'master_templates/loan_settings_non_monetary_Categories_load.html',context)




def loan_settings_non_monetary_settings(request,pk):
    record = Commodity_Categories.objects.get(id=pk)
    task_array=[]
    if not request.user.user_type == '1':
        tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
        for task in tasks:
            task_array.append(task.task.title)
    context={
    'task_array':task_array,

    'record':record,
    }
    return render(request,'master_templates/loan_settings_non_monetary_settings.html',context)





def non_monetary_oan_guarantors_update(request,pk):
    task_array=[]
    if not request.user.user_type == '1':
        tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
        for task in tasks:
            task_array.append(task.task.title)
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
    'task_array':task_array,
    'form':form,
    'instructions':instructions,
    'url':'non_monetary_oan_guarantors_update',
    'button_text':"Update Record",
    'title':title,
     'item':item,
    }
    return render(request,'master_templates/loan_criteria_update.html', context)


def non_monetary_oan_guarantors_gross_pay_rating_update(request,pk):
    task_array=[]
    if not request.user.user_type == '1':
        tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
        for task in tasks:
            task_array.append(task.task.title)
    item=  Commodity_Categories.objects.get(id=pk)
    title="Update Loan Guarnators for " +  item.title
    instructions='''
    This page enable you to set Gaurantors
    Gross Pay Ratinf
    needed to access this loan.
    '''
    form = loan_guarantors_gross_pay_update_form(request.POST or None)

    if request.method ==  "POST":
        form = loan_guarantors_gross_pay_update_form(request.POST)
        if form.is_valid():
            guarantors_gross_pay_rating=form.cleaned_data["guarantors_gross_pay_rating"]

            item.guarantors_gross_pay_rating=guarantors_gross_pay_rating
            item.save()
            messages.success(request,"Record Updated Successfully")
            return  HttpResponseRedirect(reverse('loan_settings_non_monetary_settings',args=(pk,)))

    form.fields['guarantors_gross_pay_rating'].initial=item.guarantors_gross_pay_rating
    context={
    'task_array':task_array,
    'form':form,
    'instructions':instructions,
    'url':'non_monetary_oan_guarantors_update',
    'button_text':"Update Record",
    'title':title,
    'item':item,
    }
    return render(request,'master_templates/loan_criteria_update.html', context)



def Non_Monetary_MultipleLoanStatus_update(request,pk):
    task_array=[]
    if not request.user.user_type == '1':
        tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
        for task in tasks:
            task_array.append(task.task.title)
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
            multiple_loan_status=form.cleaned_data["multiple_loan_status"]

            record = Commodity_Categories.objects.get(id=pk)
            record.multiple_loan_status=multiple_loan_status
            record.save()
            messages.success(request,"Record Updated Successfully")
            return  HttpResponseRedirect(reverse('loan_settings_non_monetary_settings',args=(pk,)))

    form.fields['multiple_loan_status'].initial=item.multiple_loan_status
    context={
    'task_array':task_array,
    'form':form,
    'instructions':instructions,
    'url':'Non_Monetary_MultipleLoanStatus_update',
    'button_text':"Update Record",
    'title':title,
     'item':item,
    }
    return render(request,'master_templates/loan_criteria_update.html', context)



def non_monetary_loan_duration_update(request,pk):
    task_array=[]
    if not request.user.user_type == '1':
        tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
        for task in tasks:
            task_array.append(task.task.title)
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
    'task_array':task_array,
    'form':form,
    'instructions':instructions,
    'url':'non_monetary_loan_duration_update',
    'button_text':"Update Record",
    'title':title,
     'item':item,
    }
    return render(request,'master_templates/loan_criteria_update.html', context)


def non_monetary_loan_name_update(request,pk):
    task_array=[]
    if not request.user.user_type == '1':
        tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
        for task in tasks:
            task_array.append(task.task.title)
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
    'task_array':task_array,
    'form':form,
    'instructions':instructions,
    'url':'non_monetary_loan_name_update',
    'button_text':"Update Record",
    'title':title,
     'item':item,
    }
    return render(request,'master_templates/loan_criteria_update.html', context)


def non_monetary_loan_interest_rate_update(request,pk):
    task_array=[]
    if not request.user.user_type == '1':
        tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
        for task in tasks:
            task_array.append(task.task.title)
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
    'task_array':task_array,
    'form':form,
    'instructions':instructions,
    'url':'non_monetary_loan_interest_rate_update',
    'button_text':"Update Record",
    'title':title,
     'item':item,
    }
    return render(request,'master_templates/loan_criteria_update.html', context)




def non_monetary_loan_admin_charges_rate_update(request,pk):
    task_array=[]
    if not request.user.user_type == '1':
        tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
        for task in tasks:
            task_array.append(task.task.title)
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
            admin_charges_rating=form.cleaned_data["admin_charges_rating"]

            record = Commodity_Categories.objects.get(id=pk)
            record.admin_charges_rating=admin_charges_rating
            record.save()
            messages.success(request,"Record Updated Successfully")
            return  HttpResponseRedirect(reverse('loan_settings_non_monetary_settings',args=(pk,)))
    if item.admin_charges_rating:
        form.fields['admin_charges_rating'].initial=item.admin_charges_rating

    context={
    'task_array':task_array,
    'form':form,
    'instructions':instructions,
    'url':'non_monetary_loan_admin_charges_rate_update',
    'button_text':"Update Record",
    'title':title,
     'item':item,
    }
    return render(request,'master_templates/loan_criteria_update.html', context)




def non_monetary_loan_admin_charges_update(request,pk):
    task_array=[]
    if not request.user.user_type == '1':
        tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
        for task in tasks:
            task_array.append(task.task.title)
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
    'task_array':task_array,
    'form':form,
    'instructions':instructions,
    'url':'non_monetary_loan_admin_charges_update',
    'button_text':"Update Record",
    'title':title,
     'item':item,
    }
    return render(request,'master_templates/loan_criteria_update.html', context)



# def non_monetary_loan_form_print_update(request,pk):
#     task_array=[]
#     if not request.user.user_type == '1':
#         tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
#         for task in tasks:
#             task_array.append(task.task.title)
#     item= Commodity_Categories.objects.get(id=pk)
#     title="Update Loan Form Print  for " +  item.title
#     instructions='''
#     This page enable you to set the minimum loan amount
#     upon which there would be flat rate in cash of Admin Charges.
#     '''
#     form = loan_form_print_form(request.POST or None)

#     if request.method ==  "POST":
#         form = loan_form_print_form(request.POST)
#         if form.is_valid():
#             form_print=form.cleaned_data["form_print"]

#             record = Commodity_Categories.objects.get(id=pk)
#             record.form_print=form_print
#             record.save()
#             messages.success(request,"Record Updated Successfully")
#             return  HttpResponseRedirect(reverse('loan_settings_non_monetary_settings',args=(pk,)))

#     form.fields['form_print'].initial=item.form_print
#     context={
#     'task_array':task_array,
#     'form':form,
#     'instructions':instructions,
#     'url':'non_monetary_loan_form_print_update',
#     'button_text':"Update Record",
#     'title':title,
#      'item':item,
#     }
#     return render(request,'master_templates/loan_criteria_update.html', context)


def non_monetary_loan_receipt_type_update(request,pk):
    task_array=[]
    if not request.user.user_type == '1':
        tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
        for task in tasks:
            task_array.append(task.task.title)
    item= Commodity_Categories.objects.get(id=pk)
    title="Update Loan Salary Loan Relationship  for " +  item.title

    instructions='''
    This page enable you to set the Receipt Type for Issuance.
    '''
    form = loan_Receipt_type_update_form(request.POST or None)

    if request.method ==  "POST":
        form = loan_Receipt_type_update_form(request.POST)
        if form.is_valid():
            receipt_type=form.cleaned_data["receipt_type"]

            record = Commodity_Categories.objects.get(id=pk)
            record.receipt_type=receipt_type
            record.save()
            messages.success(request,"Record Updated Successfully")
            return  HttpResponseRedirect(reverse('loan_settings_non_monetary_settings',args=(pk,)))

    form.fields['receipt_type'].initial=item.receipt_type
    context={
    'task_array':task_array,
    'form':form,
    'instructions':instructions,
    'url':'non_monetary_loan_receipt_type_update',
    'button_text':"Update Record",
    'title':title,
     'item':item,
    }
    return render(request,'master_templates/loan_criteria_update.html', context)


def non_monetary_loan_loan_age_update(request,pk):
    task_array=[]
    if not request.user.user_type == '1':
        tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
        for task in tasks:
            task_array.append(task.task.title)
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
    'task_array':task_array,
    'form':form,
    'instructions':instructions,
    'url':'non_monetary_loan_loan_age_update',
    'button_text':"Update Record",
    'title':title,
     'item':item,
    }
    return render(request,'master_templates/loan_criteria_update.html', context)


####################################################################
###################### CUSTOMIZED COMMODITY LOAN SETTINGS ##########
####################################################################
# def Customized_Commodity_Loan_Settings(request):
#     task_array=[]
#     if not request.user.user_type == '1':
#         tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
#         for task in tasks:
#             task_array.append(task.task.title)
#     transaction=TransactionTypes.objects.get(code='206')
#     context={
#     'task_array':task_array,
#     'transaction':transaction,
#     }
#     return render(request,'master_templates/Customized_Commodity_Loan_Settings.html',context)


# def Customized_loan_guarantors_update(request,pk):
#     task_array=[]
#     if not request.user.user_type == '1':
#         tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
#         for task in tasks:
#             task_array.append(task.task.title)
#     item= TransactionTypes.objects.get(id=pk)
#     title="Update Loan Guarnators for " +  item.name
#     instructions='''
#     This page enable you to set the total number of Gaurantors
#     needed to access this loan.
#     '''
#     form = loan_guarantors_update_form(request.POST or None)

#     if request.method ==  "POST":
#         form = loan_guarantors_update_form(request.POST)
#         if form.is_valid():
#             guarantors=form.cleaned_data["guarantors"]
#             record = TransactionTypes.objects.get(id=pk)
#             record.guarantors=guarantors
#             record.save()
#             messages.success(request,"Record Updated Successfully")
#             return  HttpResponseRedirect(reverse('Customized_Commodity_Loan_Settings'))

#     form.fields['guarantors'].initial=item.guarantors
#     context={
#     'task_array':task_array,
#     'form':form,
#     'instructions':instructions,
#     'url':'loan_guarantors_update',
#     'button_text':"Update Record",
#     'title':title,
#      'item':item,
#     }
#     return render(request,'master_templates/loan_criteria_update.html', context)


# def Customized_loan_form_print_update(request,pk):
#     task_array=[]
#     if not request.user.user_type == '1':
#         tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
#         for task in tasks:
#             task_array.append(task.task.title)
#     item= TransactionTypes.objects.get(id=pk)
#     title="Update Loan Form Print  for " +  item.name
#     instructions='''
#     This page enable you to set if Form should be Printed out Automatically.
#     '''
#     form = loan_form_print_form(request.POST or None)

#     if request.method ==  "POST":
#         form = loan_form_print_form(request.POST)
#         if form.is_valid():
#             form_print=form.cleaned_data["form_print"]

#             record = TransactionTypes.objects.get(id=pk)
#             record.form_print=form_print
#             record.save()
#             messages.success(request,"Record Updated Successfully")
#             return  HttpResponseRedirect(reverse('Customized_Commodity_Loan_Settings'))

#     form.fields['form_print'].initial=item.form_print.id
#     context={
#     'task_array':task_array,
#     'form':form,
#     'instructions':instructions,
#     'url':'Customized__loan_form_print_update',
#     'button_text':"Update Record",
#     'title':title,
#      'item':item,
#     }
#     return render(request,'master_templates/loan_criteria_update.html', context)

# def Customized_receipt_type_update(request,pk):
#     task_array=[]
#     if not request.user.user_type == '1':
#         tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
#         for task in tasks:
#             task_array.append(task.task.title)
#     item= TransactionTypes.objects.get(id=pk)
#     title="Update Receipt Type for " +  item.name
#     instructions='''
#     This page enable you to set the Receipt Type.
#     '''
#     form = loan_Receipt_type_update_form(request.POST or None)

#     if request.method ==  "POST":
#         form = loan_Receipt_type_update_form(request.POST)
#         if form.is_valid():
#             receipt_type_id=form.cleaned_data["receipt_type"]
#             receipt_type=ReceiptTypes.objects.get(id=receipt_type_id)
#             record = TransactionTypes.objects.get(id=pk)
#             record.receipt_type=receipt_type
#             record.save()
#             messages.success(request,"Record Updated Successfully")
#             return  HttpResponseRedirect(reverse('Customized_Commodity_Loan_Settings'))

#     form.fields['receipt_type'].initial=item.receipt_type
#     context={
#     'task_array':task_array,
#     'form':form,
#     'instructions':instructions,
#     'url':'Customized_receipt_type_update',
#     'button_text':"Update Record",
#     'title':title,
#      'item':item,
#     }
#     return render(request,'master_templates/loan_criteria_update.html', context)




# def Customized_loan_category_update(request,pk):
#     task_array=[]
#     if not request.user.user_type == '1':
#         tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
#         for task in tasks:
#             task_array.append(task.task.title)
#     item= TransactionTypes.objects.get(id=pk)
#     title="Update Loan Category for " +  item.name
#     instructions='''
#     This page enable you to set whether a loan is monetary or Not.
#     '''
#     form = loan_category_update_form(request.POST or None)

#     if request.method ==  "POST":
#         form = loan_category_update_form(request.POST)
#         if form.is_valid():
#             category_id=form.cleaned_data["category"]
#             category=LoanCategory.objects.get(id=category_id)
#             record = TransactionTypes.objects.get(id=pk)
#             record.category=category
#             record.save()
#             messages.success(request,"Record Updated Successfully")
#             return  HttpResponseRedirect(reverse('Customized_Commodity_Loan_Settings'))

#     form.fields['category'].initial=item.category
#     context={
#     'task_array':task_array,
#     'form':form,
#     'instructions':instructions,
#     'url':'loan_category_update',
#     'button_text':"Update Record",
#     'title':title,
#      'item':item,
#     }
#     return render(request,'master_templates/loan_criteria_update.html', context)


# def Customized_loan_duration_update(request,pk):
#     task_array=[]
#     if not request.user.user_type == '1':
#         tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
#         for task in tasks:
#             task_array.append(task.task.title)
#     item= TransactionTypes.objects.get(id=pk)
#     title="Update Loan Duration for " +  item.name
#     instructions='''
#     This page enable you to set the duration of Loans.
#     '''
#     form = loan_duration_update_form(request.POST or None)

#     if request.method ==  "POST":
#         form = loan_duration_update_form(request.POST)
#         if form.is_valid():
#             duration=form.cleaned_data["duration"]
#             record = TransactionTypes.objects.get(id=pk)
#             record.duration=duration
#             record.save()
#             messages.success(request,"Record Updated Successfully")
#             return  HttpResponseRedirect(reverse('Customized_Commodity_Loan_Settings'))

#     form.fields['duration'].initial=item.duration
#     context={
#     'task_array':task_array,
#     'form':form,
#     'instructions':instructions,
#     'url':'loan_duration_update',
#     'button_text':"Update Record",
#     'title':title,
#      'item':item,
#     }
#     return render(request,'master_templates/loan_criteria_update.html', context)


# def Customized_loan_name_update(request,pk):
#     task_array=[]
#     if not request.user.user_type == '1':
#         tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
#         for task in tasks:
#             task_array.append(task.task.title)
#     item= TransactionTypes.objects.get(id=pk)
#     title="Update Loan Description for " +  item.name
#     instructions='''
#     This page enable you to modify the Title of Loans.
#     '''
#     form = loan_name_update_form(request.POST or None)

#     if request.method ==  "POST":
#         form = loan_name_update_form(request.POST)
#         if form.is_valid():
#             name=form.cleaned_data["name"]
#             record = TransactionTypes.objects.get(id=pk)
#             record.name=name
#             record.save()
#             messages.success(request,"Record Updated Successfully")
#             return  HttpResponseRedirect(reverse('Customized_Commodity_Loan_Settings'))

#     form.fields['name'].initial=item.name
#     context={
#     'task_array':task_array,
#     'form':form,
#     'instructions':instructions,
#     'url':'loan_name_update',
#     'button_text':"Update Record",
#     'title':title,
#     'item':item,
#     }
#     return render(request,'master_templates/loan_criteria_update.html', context)


# def Customized_loan_interest_rate_update(request,pk):
#     task_array=[]
#     if not request.user.user_type == '1':
#         tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
#         for task in tasks:
#             task_array.append(task.task.title)
#     item= TransactionTypes.objects.get(id=pk)
#     title="Update Loan Interest Rate  for " +  item.name
#     instructions='''
#     This page enable you to set the interest rate of Loans.
#     '''

#     form = loan_interest_rate_update_form(request.POST or None)

#     if request.method ==  "POST":
#         form = loan_interest_rate_update_form(request.POST)
#         if form.is_valid():
#             interest_rate=form.cleaned_data["interest_rate"]
#             record = TransactionTypes.objects.get(id=pk)
#             record.interest_rate=interest_rate
#             record.save()
#             messages.success(request,"Record Updated Successfully")
#             return  HttpResponseRedirect(reverse('Customized_Commodity_Loan_Settings'))
#     form.fields['interest_rate'].initial=item.interest_rate
#     context={
#     'task_array':task_array,
#     'form':form,
#     'instructions':instructions,
#     'url':'loan_interest_rate_update',
#     'button_text':"Update Record",
#     'title':title,
#     'item':item,
#     }
#     return render(request,'master_templates/loan_criteria_update.html', context)



# def Customized_loan_rank_update_update(request,pk):
#     task_array=[]
#     if not request.user.user_type == '1':
#         tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
#         for task in tasks:
#             task_array.append(task.task.title)
#     item= TransactionTypes.objects.get(id=pk)
#     title="Update Loan Rank  for " +  item.name
#     instructions='''
#     This page enable you to set the order in which
#     monthly deduction shall flow fro the bulk deduction.
#     '''

#     form = loan_rank_update_form(request.POST or None)

#     if request.method ==  "POST":
#         form = loan_rank_update_form(request.POST)
#         if form.is_valid():
#             rank=form.cleaned_data["rank"]
#             record = TransactionTypes.objects.get(id=pk)
#             record.rank=rank
#             record.save()
#             messages.success(request,"Record Updated Successfully")
#             return  HttpResponseRedirect(reverse('Customized_Commodity_Loan_Settings'))

#     form.fields['rank'].initial=item.rank
#     context={
#     'task_array':task_array,
#     'form':form,
#     'instructions':instructions,
#     'url':'loan_rank_update_update',
#     'button_text':"Update Record",
#     'title':title,
#     'item':item,
#     }
#     return render(request,'master_templates/loan_criteria_update.html', context)


# def Customized_loan_admin_charges_rate_update(request,pk):
#     task_array=[]
#     if not request.user.user_type == '1':
#         tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
#         for task in tasks:
#             task_array.append(task.task.title)
#     item= TransactionTypes.objects.get(id=pk)
#     title="Update Loan Rank  for " +  item.name
#     instructions='''
#     This page enable you to set whether admin charge is Cash or a
#     percentage of amount requested for loan.
#     '''
#     form = loan_admin_charges_rate_update_form(request.POST or None)

#     if request.method ==  "POST":
#         form = loan_admin_charges_rate_update_form(request.POST)
#         if form.is_valid():
#             admin_charge_id=form.cleaned_data["admin_charges_rating"]
#             admin_charges_rating=AdminCharges.objects.get(id=admin_charge_id)
#             record = TransactionTypes.objects.get(id=pk)
#             record.admin_charges_rating=admin_charges_rating
#             record.save()
#             messages.success(request,"Record Updated Successfully")
#             return  HttpResponseRedirect(reverse('Customized_Commodity_Loan_Settings'))

#     form.fields['admin_charges_rating'].initial=item.admin_charges_rating
#     context={
#     'task_array':task_array,
#     'form':form,
#     'instructions':instructions,
#     'url':'loan_admin_charges_rate_update',
#     'button_text':"Update Record",
#     'title':title,
#     'item':item,
#     }
#     return render(request,'master_templates/loan_criteria_update.html', context)


# def Customized_loan_admin_charges_update(request,pk):
#     task_array=[]
#     if not request.user.user_type == '1':
#         tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
#         for task in tasks:
#             task_array.append(task.task.title)
#     item= TransactionTypes.objects.get(id=pk)
#     title="Update Loan Admin Charges  for " +  item.name
#     instructions='''
#     This page enable you to set the percentage rating of
#     the Admin charge if it percentage based.
#     '''
#     form = loan_admin_charges_update_form(request.POST or None)

#     if request.method ==  "POST":
#         form = loan_admin_charges_update_form(request.POST)
#         if form.is_valid():
#             admin_charges=form.cleaned_data["admin_charges"]
#             record = TransactionTypes.objects.get(id=pk)
#             record.admin_charges=admin_charges
#             record.save()
#             messages.success(request,"Record Updated Successfully")
#             return  HttpResponseRedirect(reverse('Customized_Commodity_Loan_Settings'))

#     form.fields['admin_charges'].initial=item.admin_charges
#     context={
#     'task_array':task_array,
#     'form':form,
#     'instructions':instructions,
#     'url':'loan_admin_charges_update',
#     'button_text':"Update Record",
#     'title':title,
#      'item':item,
#     }
#     return render(request,'master_templates/loan_criteria_update.html', context)


# def Customized_loan_loan_age_update(request,pk):
#     task_array=[]
#     if not request.user.user_type == '1':
#         tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
#         for task in tasks:
#             task_array.append(task.task.title)
#     item= TransactionTypes.objects.get(id=pk)
#     title="Update Loan Age  for " +  item.name
#     instructions='''
#     This page enable you to set the number of months one has to a member before
#     Such person can access this loan.
#     '''
#     form = loan_loan_age_update_form(request.POST or None)

#     if request.method ==  "POST":
#         form = loan_loan_age_update_form(request.POST)
#         if form.is_valid():
#             loan_age=form.cleaned_data["loan_age"]
#             record = TransactionTypes.objects.get(id=pk)
#             record.loan_age=loan_age
#             record.save()
#             messages.success(request,"Record Updated Successfully")
#             return  HttpResponseRedirect(reverse('Customized_Commodity_Loan_Settings'))

#     form.fields['loan_age'].initial=item.loan_age
#     context={
#     'task_array':task_array,
#     'form':form,
#     'instructions':instructions,
#     'url':'loan_loan_age_update',
#     'button_text':"Update Record",
#     'title':title,
#      'item':item,
#     }
#     return render(request,'master_templates/loan_criteria_update.html', context)


####################################################################
###################### APPROVABLE TRANSACTION ######################
####################################################################



def membership_price_settings_load(request):
    task_array=[]
    if not request.user.user_type == '1':
        tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
        for task in tasks:
            task_array.append(task.task.title)
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
    'task_array':task_array,
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
    task_array=[]
    if not request.user.user_type == '1':
        tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
        for task in tasks:
            task_array.append(task.task.title)
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
    'task_array':task_array,
    'record':record,
    }
    return render(request,'master_templates/AutoReceipt_Setup.html',context)



def receipt_manager(request):
    task_array=[]
    if not request.user.user_type == '1':
        tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
        for task in tasks:
            task_array.append(task.task.title)
    form = receipt_manager_form(request.POST or None)
    receipts=Receipts.objects.all()
    if request.method=="POST":
        start_point = request.POST.get('start_point')
        stop_point = request.POST.get('stop_point')

        for i in  range(int(start_point),int(stop_point)+1):
            record=Receipts(status='UNUSED',receipt=str(i).zfill(5))
            record.save()
        return HttpResponseRedirect(reverse('receipt_manager'))
    context={
    'task_array':task_array,
    'form':form,
    'receipts':receipts,
    }
    return render(request,'master_templates/receipt_manager.html',context)


def receipt_manager_shop(request):
    task_array=[]
    if not request.user.user_type == '1':
        tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
        for task in tasks:
            task_array.append(task.task.title)
    form = receipt_manager_form(request.POST or None)
    receipts=Receipts_Shop.objects.all()
    if request.method=="POST":
        start_point = request.POST.get('start_point')
        stop_point = request.POST.get('stop_point')

        for i in  range(int(start_point),int(stop_point)+1):
            record=Receipts_Shop(status='UNUSED',receipt=str(i).zfill(5))
            record.save()
        return HttpResponseRedirect(reverse('receipt_manager_shop'))
    context={
    'task_array':task_array,
    'form':form,
    'receipts':receipts,
    }
    return render(request,'master_templates/receipt_manager_shop.html',context)

def TransactionEnabler_Add(request):
    task_array=[]
    if not request.user.user_type == '1':
        tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
        for task in tasks:
            task_array.append(task.task.title)
    form=TransactionEnabler_Form(request.POST or None)
    records = TransactionEnabler.objects.all()

    if request.method=="POST":
        status='NO'
        title=request.POST.get('title')
        if TransactionEnabler.objects.filter(title=title).exists():
            messages.info(request,'Record already Exist')

        else:
            TransactionEnabler(title=title.upper(),status=status).save()
            messages.success(request,"Record Updated Successfully")
        return HttpResponseRedirect(reverse('TransactionEnabler_Add'))

    context={
    'task_array':task_array,
    'form':form,
    'records':records,
    }
    return render(request,'master_templates/TransactionEnabler_Add.html',context)

def TransactionEnabler_Manage(request):
    task_array=[]
    if not request.user.user_type == '1':
        tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
        for task in tasks:
            task_array.append(task.task.title)
    records = TransactionEnabler.objects.all()


    context={
    'task_array':task_array,
    'records':records,
    }
    return render(request,'master_templates/TransactionEnabler_Manage.html',context)


def TransactionEnabler_enabler(request,pk):
    record=TransactionEnabler.objects.get(id=pk)
    if record.status == "YES":
        record.status="NO"
    else:
        record.status="YES"
    record.save()

    messages.success(request,"Record Updated Successfully")
    return HttpResponseRedirect(reverse('TransactionEnabler_Manage'))


def TransactionEnabler_delete(request,pk):
    TransactionEnabler.objects.filter(id=pk).delete()
    messages.info(request,"Record Deleted Successfully")
    return HttpResponseRedirect(reverse('TransactionEnabler_Add'))


def Members_IdManager(request):
    task_array=[]
    if not request.user.user_type == '1':
        tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
        for task in tasks:
            task_array.append(task.task.title)
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
    'task_array':task_array,
    'form':form,
    }
    return render(request,'master_templates/MembersIdManager.html',context)


def SharesUnits_add(request):
    task_array=[]
    if not request.user.user_type == '1':
        tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
        for task in tasks:
            task_array.append(task.task.title)
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
    'task_array':task_array,
    'items':items,
    }
    return render(request,'master_templates/SharesUnits_add.html',context)

def SharesUnits_Max_Min_Values(request):
    task_array=[]
    if not request.user.user_type == '1':
        tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
        for task in tasks:
            task_array.append(task.task.title)

    form = SharesUnits_Max_Min_Values_form(request.POST or None)

    item=TransactionTypes.objects.get(code='700')
    if request.method=="POST":

        share_unit_max = request.POST.get('share_unit_max')
        share_unit_min = request.POST.get('share_unit_min')

        if float(share_unit_min) > float(share_unit_max):
            messages.error(request,"Invalid Input")
            return HttpResponseRedirect(reverse('SharesUnits_Max_Min_Values'))

        item.share_unit_max=share_unit_max
        item.share_unit_min=share_unit_min
        item.save()
        messages.success(request,"Record Updated Successfully")
        return HttpResponseRedirect(reverse('SharesUnits_Max_Min_Values'))

    form.fields['share_unit_max'].initial=item.share_unit_max
    form.fields['share_unit_min'].initial=item.share_unit_min
    context={
    'task_array':task_array,
    'item':item,
    'form':form,
    }
    return render(request,'master_templates/SharesUnits_Max_Min_Values.html',context)


def Loan_Number_Manager(request):
    task_array=[]
    if not request.user.user_type == '1':
        tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
        for task in tasks:
            task_array.append(task.task.title)
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
    'task_array':task_array,
    'form':form,
    }
    return render(request,'master_templates/Loan_Number_Manager.html',context)


def FailedLoanPenalty_Manager(request):
    task_array=[]
    if not request.user.user_type == '1':
        tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
        for task in tasks:
            task_array.append(task.task.title)
    form=FailedLoanPenalty_Manager_form(request.POST or None)
    if FailedLoanPenalty.objects.all().count()>0:
        item=FailedLoanPenalty.objects.first()
        form.fields['code'].initial=item.code


    if request.method=="POST":
        code=request.POST.get('code')

        if FailedLoanPenalty.objects.all().count()>0:
            record=FailedLoanPenalty.objects.first()
            record.code=code
            record.save()

        else:
            record=FailedLoanPenalty(code=code)
            record.save()
        return HttpResponseRedirect(reverse('FailedLoanPenalty_Manager'))

    context={
    'task_array':task_array,
    'form':form,
    }
    return render(request,'master_templates/FailedLoanPenalty_Manager.html',context)


def FailedLoanPenalty_Duration_Manager(request):
    task_array=[]
    if not request.user.user_type == '1':
        tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
        for task in tasks:
            task_array.append(task.task.title)
    
    form=FailedLoanPenalty_Duration_Manager_form(request.POST or None)

    if FailedLoanPenaltyDuration.objects.all().count()>0:
        item=FailedLoanPenaltyDuration.objects.first()
        form.fields['duration'].initial=item.duration


    if request.method=="POST":
        duration=request.POST.get('duration')

        if FailedLoanPenaltyDuration.objects.all().count()>0:
            record=FailedLoanPenaltyDuration.objects.first()
            record.duration=duration
            record.save()

        else:
            record=FailedLoanPenaltyDuration(duration=duration)
            record.save()
        return HttpResponseRedirect(reverse('FailedLoanPenalty_Duration_Manager'))

    context={
    'task_array':task_array,
    'form':form,
    }
    return render(request,'master_templates/FailedLoanPenalty_Duration_Manager.html',context)

#######################################################################
################## COOPERATIVE ACCOUNTS ################################
#######################################################################

def CooperativeBankAccounts_Operational_Designation(request):
    task_array=[]
    if not request.user.user_type == '1':
        tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
        for task in tasks:
            task_array.append(task.task.title)
    form=CooperativeBankAccounts_form(request.POST or None)
    banks=CooperativeBankAccounts.objects.all()

    if request.method == 'POST':
        bank_id=request.POST.get('bank')
        bank=Banks.objects.get(id=bank_id)

        account_type=request.POST.get('account_type')


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
    'task_array':task_array,
    'form':form,
    'banks':banks,
    }
    return render(request,'master_templates/CooperativeBankAccounts_add.html',context)

def CooperativeBankAccounts_add(request):
    task_array=[]
    if not request.user.user_type == '1':
        tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
        for task in tasks:
            task_array.append(task.task.title)
    form=CooperativeBankAccounts_form(request.POST or None)
    banks=CooperativeBankAccounts.objects.all()
    if request.method == 'POST':
        bank_id=request.POST.get('bank')
        bank=Banks.objects.get(id=bank_id)

        account_type=request.POST.get('account_type')

        account_name=request.POST.get('account_name')
        account_number=request.POST.get('account_number')
        sort_code=request.POST.get('sort_code')

        if CooperativeBankAccounts.objects.filter(bank=bank,account_number=account_number).exists():
            messages.error(request,'This account Number is already in Use')
            return HttpResponseRedirect(reverse('CooperativeBankAccounts_add'))

        record=CooperativeBankAccounts(bank=bank,account_type=account_type,account_name=account_name,account_number=account_number,sort_code=sort_code)
        record.save()

        messages.success(request,"Record Added Successfully")
        return HttpResponseRedirect(reverse('CooperativeBankAccounts_add'))

    context={
    'task_array':task_array,
    'form':form,
    'banks':banks,
    }
    return render(request,'master_templates/CooperativeBankAccounts_add.html',context)


def CooperativeBankAccounts_Remove(request,pk):
    record=CooperativeBankAccounts.objects.get(id=pk)
    record.delete()
    return HttpResponseRedirect(reverse('CooperativeBankAccounts_add'))


def CooperativeBankAccounts_Update(request,pk):
    task_array=[]
    if not request.user.user_type == '1':
        tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
        for task in tasks:
            task_array.append(task.task.title)
    form=CooperativeBankAccounts_form(request.POST or None)
    record=CooperativeBankAccounts.objects.get(id=pk)

    form.fields['account_name'].initial=record.account_name
    form.fields['account_number'].initial=record.account_number
    form.fields['bank'].initial=record.bank.id
    form.fields['account_type'].initial=record.account_type
    form.fields['sort_code'].initial=record.sort_code
    if request.method=="POST":
        bank_id=request.POST.get('bank')
        bank=Banks.objects.get(id=bank_id)

        account_type= request.POST.get('account_type')


        account_name=request.POST.get('account_name')
        account_number=request.POST.get('account_number')
        sort_code=request.POST.get('sort_code')

        record.bank=bank
        record.account_type=account_type
        record.account_name=account_name
        record.account_number=account_number
        record.sort_code=sort_code
        record.save()
        return HttpResponseRedirect(reverse('CooperativeBankAccounts_add'))
    context={
    'task_array':task_array,
    'form':form,
    }
    return render(request,'master_templates/CooperativeBankAccounts_Update.html',context)

#######################################################################
################## WITHDRAWAL CONTROLLER ##############################
#######################################################################



def WithdrawalController_add(request):
    task_array=[]
    if not request.user.user_type == '1':
        tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
        for task in tasks:
            task_array.append(task.task.title)
    form=WithdrawalController_form(request.POST or None)
    if request.method=="POST":
        transaction_id=request.POST.get('transactions')
        transaction=TransactionTypes.objects.get(id=transaction_id)

        maturity=request.POST.get('maturity')
        record=WithdrawableTransactions(status='LOCKED',transaction=transaction,maturity=maturity)
        record.save()
        messages.success(request,'Tranaction Successfully Completed')
        return HttpResponseRedirect(reverse('WithdrawalController_add'))
    context={
    'task_array':task_array,
    'form':form,
    }
    return render(request,'master_templates/WithdrawalController_add.html',context)


def WithdrawalController(request):
    task_array=[]
    if not request.user.user_type == '1':
        tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
        for task in tasks:
            task_array.append(task.task.title)
    transactions=WithdrawableTransactions.objects.all()
    context={
    'task_array':task_array,
    'transactions':transactions,
    }
    return render(request,'master_templates/WithdrawalController.html',context)


def WithdrawalController_View(request,pk):
    task_array=[]
    if not request.user.user_type == '1':
        tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
        for task in tasks:
            task_array.append(task.task.title)
    form=WithdrawalController_update_form(request.POST or None)
    transaction=WithdrawableTransactions.objects.get(id=pk)

    if request.method=="POST":
        status=request.POST.get('status')
        maturity=request.POST.get('maturity')

        transaction.maturity=maturity
        transaction.status=status
        transaction.save()
        return HttpResponseRedirect(reverse('WithdrawalController'))

    form.fields['maturity'].initial=transaction.maturity
    form.fields['status'].initial=transaction.status
    context={
    'task_array':task_array,
    'transaction':transaction,
    'form':form,
    }
    return render(request,'master_templates/WithdrawalController_View.html',context)






def WithdrawalController_Process(request,pk):
    transaction=TransactionTypes.objects.get(id=pk)
    if transaction.withdrawal_status =='LOCKED':
        transaction.withdrawal_status='UNLOCKED'
    else:
        transaction.withdrawal_status='LOCKED'
    transaction.save()
    return HttpResponseRedirect(reverse('WithdrawalController'))

#######################################################################
############################ SHOP #####################################
#######################################################################
def CustomerID_Manager(request):
    task_array=[]
    if not request.user.user_type == '1':
        tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
        for task in tasks:
            task_array.append(task.task.title)
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
    'task_array':task_array,
    'form':form,
    }
    return render(request,'master_templates/CustomerID_Manager.html',context)



#######################################################################
################## PRESIDENT VIEWS  ##################################
#######################################################################
def membership_request_approvals_list_load(request):
    task_array=[]
    if not request.user.user_type == '1':
        tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
        for task in tasks:
            task_array.append(task.task.title)

    applicants=MemberShipRequest.objects.filter(submission_status='SUBMITTED',approval_status='PENDING')
    context={
    'task_array':task_array,
    'applicants':applicants,
    }
    return render(request,'master_templates/membership_request_approvals_list_load.html',context)


def membership_request_approval_info(request,pk):
    task_array=[]
    if not request.user.user_type == '1':
        tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
        for task in tasks:
            task_array.append(task.task.title)
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
    'task_array':task_array,
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
    task_array=[]
    if not request.user.user_type == '1':
        tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
        for task in tasks:
            task_array.append(task.task.title)
    form=MemberShipRequest_approval_submit_form(request.POST or None)

    if request.method=="POST":
        approval_status=request.POST.get('approval_status')


        record = MemberShipRequest.objects.get(id=pk)

        record.approval_status=approval_status
        record.approved_date=datetime.date.today()
        record.save()
        return HttpResponseRedirect(reverse('membership_request_approvals_list_load'))
    context={
    'task_array':task_array,
    'form':form,
    }
    return render(request,'master_templates/MemberShipRequest_approval_submit.html',context)






def loan_request_approval_period_load(request):
    task_array=[]
    if not request.user.user_type == '1':
        tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
        for task in tasks:
            task_array.append(task.task.title)    # return HttpResponse(current_user.cash_withdrawal_approval)



    form=loan_request_order_form(request.POST or None)

    applicants=[]
    if request.method == 'POST':
        period_id=request.POST.get("period")
        period = Commodity_Period.objects.get(id=period_id)

        batch_id=request.POST.get('batch')
        batch=Commodity_Period_Batch.objects.get(id=batch_id)

        loan_id = request.POST.get('loans')
        loan = TransactionTypes.objects.get(id=loan_id)

        applicants = LoanRequest.objects.filter(loan=loan,period=period,batch=batch,approval_status='PENDING',transaction_status='UNTREATED').filter(~Q(submission_status='PENDING'))

    context={
    'task_array':task_array,
    'applicants':applicants,
    'form':form,
    }
    return render(request,'master_templates/loan_request_approval_period_load.html',context)



def Loan_request_approval_details(request,pk):

    task_array=[]
    if not request.user.user_type == '1':
        tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
        for task in tasks:
            task_array.append(task.task.title)

    loan_comment=LoanRequest.objects.get(id=pk)
    loan_analysis=LoanRequestSettings.objects.filter(applicant_id=pk,category='ANALYSIS')
    loan_summary=LoanRequestSettings.objects.filter(applicant_id=pk,category='SUMMARY')



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

        status=request.POST.get('approval_status')


        approved_date= get_current_date(now)


        loan_comment.approval_status=status
        loan_comment.approval_comment=comment
        loan_comment.approval_date=approved_date
        loan_comment.approval_officer=approval_officer.username
        loan_comment.approved_amount=approved_amount
        loan_comment.save()

        return HttpResponseRedirect(reverse('loan_request_approval_period_load'))

    form=MemberShipRequestAdditionalInfo_form(request.POST or None)
    form.fields['comment'].initial="Approved"
    context={
    'task_array':task_array,
    'loan_analysis':loan_analysis,
    'loan_summary':loan_summary,
    'pk':pk,
    'form':form,
    'loan_comment':loan_comment,
    }
    return render(request,'master_templates/Loan_request_approval_details.html',context)


def Loan_application_approval_period_load(request):
    task_array=[]
    if not request.user.user_type == '1':
        tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
        for task in tasks:
            task_array.append(task.task.title)


    form=loan_request_order_form(request.POST or None)
    exist_loans=[]
    if request.method == 'POST':
        period_id=request.POST.get("period")
        period = Commodity_Period.objects.get(id=period_id)

        batch_id=request.POST.get('batch')
        batch=Commodity_Period_Batch.objects.get(id=batch_id)

        loan_id = request.POST.get('loans')
        loan = TransactionTypes.objects.get(id=loan_id)

        exist_loans = LoanApplication.objects.filter(applicant__applicant__loan=loan,applicant__applicant__period=period,applicant__applicant__batch=batch,transaction_status='UNTREATED',submission_status='SUBMITTED',applicant__processing_status='PROCESSED',approval_status='PENDING')

    context={
    'exist_loans':exist_loans,
    'form':form,
    'task_array':task_array,

    }
    return render(request,'master_templates/Loan_application_approval_period_load.html',context)




def Loan_application_approval_details(request,pk):
    form = Loan_application_approval_form(request.POST or None)
    task_array=[]
    if not request.user.user_type == '1':
        tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
        for task in tasks:
            task_array.append(task.task.title)
    loan_comment=LoanApplication.objects.get(id=pk)
    loan_analysis=LoanApplicationSettings.objects.filter(applicant_id=pk,category='ANALYSIS')
    loan_summary=LoanApplicationSettings.objects.filter(applicant_id=pk,category='SUMMARY')


    if request.method=='POST':
        approval_officer=CustomUser.objects.get(id=request.user.id).username
        comment=request.POST.get('comment')
        approved_amount=request.POST.get('amount')

        if float(loan_comment.loan_amount) < float(approved_amount):
            messages.success(request,"Amount approved cannot be more than applied Amount")
            return HttpResponseRedirect(reverse('Loan_request_approval_details', args=(pk,)))

        status=request.POST.get('approval_status')


        approved_date= get_current_date(now)

        loan_comment.approval_status=status
        loan_comment.approval_comment=comment
        loan_comment.approval_date=approved_date
        loan_comment.approved_amount=approved_amount
        loan_comment.approval_officer=approval_officer
        loan_comment.save()

        return HttpResponseRedirect(reverse('Loan_application_approval_period_load'))

    form.fields['amount'].initial=loan_comment.loan_amount
    form.fields['comment'].initial="Please Process"
    context={
    'task_array':task_array,
    'loan_analysis':loan_analysis,
    'loan_summary':loan_summary,
    'pk':pk,
    'loan_comment':loan_comment,
    'form':form,
    'approval_status':APPROVAL_STATUS,
    }
    return render(request,'master_templates/Loan_application_approval_details.html',context)


def Loan_unscheduling_approval_load(request):
    task_array=[]
    if not request.user.user_type == '1':
        tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
        for task in tasks:
            task_array.append(task.task.title)


    records = LoanUnschedulingRequest.objects.filter(status='UNTREATED',approval_status='PENDING')

    context={
    'task_array':task_array,
    'records':records,
    }
    return render(request,'master_templates/Loan_unscheduling_approval_load.html',context)



def Loan_unscheduling_approval_preview(request,pk):
    form=Loan_unscheduling_approval_preview_form(request.POST or None)
    task_array=[]
    if not request.user.user_type == '1':
        tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
        for task in tasks:
            task_array.append(task.task.title)

    record=LoanUnschedulingRequest.objects.get(id=pk)

    if request.method == "POST":
        approval_date=get_current_date(now)
        approval_officer=CustomUser.objects.get(id=request.user.id).username
        approval_status = request.POST.get('approval_status')


        comment=request.POST.get('comment')
        record.approval_comment=comment
        record.approval_status=approval_status
        record.approval_officer=approval_officer
        record.approval_date=approval_date
        record.save()
        return HttpResponseRedirect(reverse('Loan_unscheduling_approval_load'))

    form.fields['comment_exist'].initial=record.comment
    context={
    'form':form,
    'task_array':task_array,
    'record':record,
    }
    return render(request,'master_templates/Loan_unscheduling_approval_preview.html',context)





def membership_commodity_loan_Period_approval_transaction_load(request):
    task_array=[]
    if not request.user.user_type == '1':
        tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
        for task in tasks:
            task_array.append(task.task.title)
    submission_status='SUBMITTED'
    approval_status='PENDING'

    form=Product_Linking_Period_Load_form(request.POST or None)

    applicants=[]
    if request.method == 'POST':
        transaction_id = request.POST.get('transaction')
        transaction = TransactionTypes.objects.get(id=transaction_id)

        period_id =request.POST.get('period')
        period=Commodity_Period.objects.get(id=period_id)

        batch_id =request.POST.get('batch')
        batch= Commodity_Period_Batch.objects.get(id=batch_id)

        applicants=Members_Commodity_Loan_Application.objects.filter(approval_status="PENDING",period=period,batch=batch,member__product__product__category__transaction=transaction,submission_status='SUBMITTED',status='UNTREATED')

    context={
    'task_array':task_array,
    'applicants':applicants,
    'form':form,
    }
    return render(request,'master_templates/membership_commodity_loan_Period_approval_transaction_load.html',context)





def membership_commodity_loan_Period_approval_transaction_details(request,pk):
    form =membership_commodity_loan_Period_approval_transaction_details_form(request.POST or None)
    task_array=[]
    if not request.user.user_type == '1':
        tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
        for task in tasks:
            task_array.append(task.task.title)
    applicant=Members_Commodity_Loan_Application.objects.get(id=pk)
    processed_by=CustomUser.objects.get(id=request.user.id)

    if request.method == 'POST':
        approval_date=get_current_date(now)
        approval_comment=request.POST.get("comment")
        approval_status=request.POST.get("approval_status")



        applicant.approval_officer=processed_by.username
        applicant.approval_status=approval_status
        applicant.approval_date=approval_date
        applicant.approval_comment=approval_comment
        applicant.save()
        return HttpResponseRedirect(reverse('membership_commodity_loan_Period_approval_transaction_load'))

    form.fields['comment'].initial = "Approved"
    context={
    'task_array':task_array,

    'applicant':applicant,
    'form':form,
    }
    return render(request,'master_templates/membership_commodity_loan_Period_approval_transaction_details.html',context)




def savings_cash_withdrawal_Certitication_list_load(request):
    task_array=[]
    if not request.user.user_type == '1':
        tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
        for task in tasks:
            task_array.append(task.task.title)



    applicants=MembersCashWithdrawalsApplication.objects.filter(approval_status="PENDING",status='UNTREATED')

    context={
    'task_array':task_array,
    'applicants':applicants,
    }
    return render(request,'master_templates/savings_cash_withdrawal_Certitication_list_load.html',context)


def savings_cash_withdrawal_list_load(request):
    task_array=[]
    if not request.user.user_type == '1':
        tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
        for task in tasks:
            task_array.append(task.task.title)


    applicants=MembersCashWithdrawalsApplication.objects.filter(approval_status='PENDING',status='UNTREATED')

    context={
    'task_array':task_array,
    'applicants':applicants,
    }
    return render(request,'master_templates/savings_cash_withdrawal_list_load.html',context)


def savings_cash_withdrawal_preview(request,pk):
    task_array=[]
    if not request.user.user_type == '1':
        tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
        for task in tasks:
            task_array.append(task.task.title)
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
    approval_status='APPROVED'
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
    'task_array':task_array,
    'applicant':applicant,
    'form':form,
    'submission_status':submission_status,
    }
    return render(request,'master_templates/savings_cash_withdrawal_preview.html',context)



def members_exclusiveness_list_load(request):
    task_array=[]
    if not request.user.user_type == '1':
        tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
        for task in tasks:
            task_array.append(task.task.title)        # return HttpResponse(current_user)


    applicants=MembersExclusiveness.objects.filter(approval_status='PENDING',status='UNTREATED')

    context={
    'task_array':task_array,
    'applicants':applicants,
    }
    return render(request,'master_templates/members_exclusiveness_list_load.html',context)


def members_exclusiveness_process(request,pk):
    task_array=[]
    if not request.user.user_type == '1':
        tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
        for task in tasks:
            task_array.append(task.task.title)
    form=members_exclusiveness_request_approval_process_form(request.POST or None)
    applicant=MembersExclusiveness.objects.get(id=pk)
    if request.method=="POST":
        approval_officer=CustomUser.objects.get(id=request.user.id).username
        comment=request.POST.get('comment')
        status=request.POST.get('approval_status')

        applicant.approval_status=status
        applicant.approval_comment=comment
        applicant.approval_officer=approval_officer
        applicant.processing_status='UNPROCESSED'
        applicant.approved_at=now
        applicant.save()
        return HttpResponseRedirect(reverse('members_exclusiveness_list_load'))

    context={
    'task_array':task_array,
    'form':form,
    'applicant':applicant,
    }
    return render(request,'master_templates/members_exclusiveness_process.html',context)


def Shares_Purchase_Request_Approval_List_Load(request):
    task_array=[]
    if not request.user.user_type == '1':
        tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
        for task in tasks:
            task_array.append(task.task.title)

    records=MembersSharePurchaseRequest.objects.filter(approval_status='PENDING',status='UNTREATED')

    context={
    'task_array':task_array,
    'records':records,
    }
    return render(request,'master_templates/Shares_Purchase_Request_Approval_List_Load.html',context)


def Shares_Purchase_Request_Approval_Processed(request,pk):
    task_array=[]
    if not request.user.user_type == '1':
        tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
        for task in tasks:
            task_array.append(task.task.title)
    form=Shares_Purchase_Request_Approval_Processed_form(request.POST or None)
    record=MembersSharePurchaseRequest.objects.get(id=pk)

    if request.method=="POST":
        units = request.POST.get("units")
        comment=request.POST.get('comment')

        approval_status=request.POST.get('approval_status')


        record.units=units
        record.approval_status=approval_status
        record.approval_date=now
        record.approval_comment=comment
        record.save()
        return HttpResponseRedirect(reverse('Shares_Purchase_Request_Approval_List_Load'))
    form.fields['units'].initial=record.units
    context={
    'task_array':task_array,
    'form':form,
    'record':record,
    }
    return render(request,'master_templates/Shares_Purchase_Request_Approval_Processed.html', context)


def Cash_Withdrawal_Request_Approval_List_Load(request):
    task_array=[]
    if not request.user.user_type == '1':
        tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
        for task in tasks:
            task_array.append(task.task.title)



    records=MembersCashWithdrawalsApplication.objects.filter(approval_status='PENDING',status='UNTREATED')

    context={
     'records':records,
     'task_array':task_array,
    }
    return render(request,'master_templates/Cash_Withdrawal_Request_Approval_List_Load.html',context)

def Cash_Withdrawal_Request_Approval_Processing(request,pk):
    task_array=[]
    if not request.user.user_type == '1':
        tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
        for task in tasks:
            task_array.append(task.task.title)


    record=MembersCashWithdrawalsApplication.objects.get(id=pk)

    context={
     'record':record,
     'task_array':task_array,
    }
    return render(request,'master_templates/Cash_Withdrawal_Request_Approval_Processing.html',context)


def membership_termination_Duration_Manager_Transaction_Load(request):

    task_array=[]
    if not request.user.user_type == '1':
        tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
        for task in tasks:
            task_array.append(task.task.title)
    transactions=Termination_Types.objects.all()

    context={
     'transactions':transactions,
     'task_array':task_array,
    }
    return render(request,'master_templates/membership_termination_Duration_Manager_Transaction_Load.html',context)


def membership_termination_Duration_Manager(request,pk):
    form=membership_termination_Duration_form(request.POST or None)
    task_array=[]
    if not request.user.user_type == '1':
        tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
        for task in tasks:
            task_array.append(task.task.title)
    transaction=Termination_Types.objects.get(id=pk)

    if request.method == 'POST':
        duration=request.POST.get('duration')

        transaction.duration=duration
        transaction.save()

        return HttpResponseRedirect(reverse('membership_termination_Duration_Manager_Transaction_Load'))

    form.fields['duration'].initial=transaction.duration
    context={
     'form':form,
     'transaction':transaction,
     'task_array':task_array,
    }
    return render(request,'master_templates/membership_termination_Duration_Manager.html',context)


def membership_termination_Request_Approval_List_Load(request):
    task_array=[]
    if not request.user.user_type == '1':
        tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
        for task in tasks:
            task_array.append(task.task.title)


    members=MemberShipTerminationRequest.objects.filter(approval_status='PENDING',status='UNTREATED')

    context={
     'members':members,
     'task_array':task_array,
    }
    return render(request,'master_templates/membership_termination_Request_Approval_List_Load.html',context)



def membership_termination_Request_Approval_Process(request,pk):
    task_array=[]
    if not request.user.user_type == '1':
        tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
        for task in tasks:
            task_array.append(task.task.title)
    form=membership_termination_Request_Approval_Process_form(request.POST or None)
    current_date=get_current_date(now)

    member=MemberShipTerminationRequest.objects.get(id=pk)
    maturity_date=member.maturity_date

    approved_date = get_current_date(now)
    approval_officer=CustomUser.objects.get(id=request.user.id).username

    if request.method == 'POST':

        comment = request.POST.get("comment")
        approval_status = request.POST.get("approval_status")


        member.approval_status=approval_status
        member.approval_comment=comment
        member.approved_at=approved_date
        member.approval_officer=approval_officer
        member.save()
        return HttpResponseRedirect(reverse('membership_termination_Request_Approval_List_Load'))


    context={
    'form':form,
     # 'button_enabled':button_enabled,
     'member':member,
     'task_array':task_array,
    }
    return render(request,'master_templates/membership_termination_Request_Approval_Process.html',context)


def membership_termination_maturity_date_exception_Approval_List_Load(request):
    task_array=[]
    if not request.user.user_type == '1':
        tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
        for task in tasks:
            task_array.append(task.task.title)


    members=MemberShipTerminationRequestException.objects.filter(approval_status='PENDING',status='UNTREATED')

    context={
     'members':members,
     'task_array':task_array,
    }
    return render(request,'master_templates/membership_termination_maturity_date_exception_Approval_List_Load.html',context)


def membership_termination_maturity_date_exception_Approval_Preview(request,pk):
    task_array=[]
    if not request.user.user_type == '1':
        tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
        for task in tasks:
            task_array.append(task.task.title)
    form=Standing_Order_Suspension_Transaction_Approvals_Load_Details_form(request.POST or None)

    member=MemberShipTerminationRequestException.objects.get(id=pk)
    approval_officer=CustomUser.objects.get(id=request.user.id)

    approved_date = get_current_date (now)
    if request.method == "POST":
        # return HttpResponse("OKKKKKk")
        comment=request.POST.get('comment')


        approval_status=request.POST.get('approval_status')


        member.approved_at=approved_date
        member.approval_status=approval_status
        member.approval_comment=comment
        member.approval_officer=approval_officer.username
        member.save()

        return HttpResponseRedirect(reverse('membership_termination_maturity_date_exception_Approval_List_Load'))

    form.fields ['purpose'].initial =member.reasons
    context={
     'member':member,
     'form':form,
     'task_array':task_array,
    }
    return render(request,'master_templates/membership_termination_maturity_date_exception_Approval_Preview.html',context)



def membership_termination_maturity_date_exception_Approval_Process1(request,pk):
    task_array=[]
    if not request.user.user_type == '1':
        tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
        for task in tasks:
            task_array.append(task.task.title)
    form=Standing_Order_Suspension_Transaction_Approvals_Load_Details_form(request.POST or None)

    member=MemberShipTerminationRequestException.objects.get(id=pk)
    approval_officer=CustomUser.objects.get(id=request.user.id)

    approved_date = get_current_date (now)
    if request.method == "POST":
        # return HttpResponse("OKKKKKk")
        comment=request.POST.get('comment')


        approval_status=request.POST.get('approval_status')


        member.approved_at=approved_date
        member.approval_status=approval_status
        member.approval_comment=comment
        member.approval_officer=approval_officer.username
        member.save()

        return HttpResponseRedirect(reverse('membership_termination_maturity_date_exception_Approval_List_Load'))

    form.fields ['purpose'].initial =member.reasons
    context={
     'member':member,
     'form':form,
     'task_array':task_array,
    }
    return render(request,'master_templates/membership_termination_maturity_date_exception_Approval_Process.html',context)


def membership_termination_Disbursement_Approval_List_Load(request):
    task_array=[]
    if not request.user.user_type == '1':
        tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
        for task in tasks:
            task_array.append(task.task.title)

    members=MemberShipTermination.objects.filter(approval_status='PENDING',processing_status='UNPROCESSED',status='UNTREATED')

    context={
     'members':members,
     'task_array':task_array,
    }
    return render(request,'master_templates/membership_termination_Disbursement_Approval_List_Load.html',context)


def membership_termination_Disbursement_Approval_Preview(request,pk):
    task_array=[]
    if not request.user.user_type == '1':
        tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
        for task in tasks:
            task_array.append(task.task.title)

    form=membership_termination_Request_Approval_Process_form(request.POST or None)

    approval_officer=CustomUser.objects.get(id=request.user.id)
    approved_date=get_current_date(now)


    member=MemberShipTermination.objects.get(id=pk)

    current_date=member.applicant.applied_date
    maturity_date=member.applicant.maturity_date

    if request.method == 'POST':

        approval_status=request.POST.get("approval_status")


        comment=request.POST.get('comment')

        member.approval_officer=approval_officer.username
        member.approval_comment=comment
        member.approval_status=approval_status
        member.approved_at=approved_date
        member.status='TREATED'
        member.save()
        return HttpResponseRedirect(reverse("membership_termination_Disbursement_Approval_List_Load"))

    button_enabled=False
    if maturity_date <= current_date:
        button_enabled=True
    else:
        if member.lock_status == 'OPEN':
            button_enabled=True


    context={
     'button_enabled':button_enabled,
     'form':form,
     'member':member,
     'task_array':task_array,
    }
    return render(request,'master_templates/membership_termination_Disbursement_Approval_Preview.html',context)




####################################################################
###################### RENTALS        ######################
####################################################################
def RentalMainCategories_add(request):
    task_array=[]
    if not request.user.user_type == '1':
        tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
        for task in tasks:
            task_array.append(task.task.title)
    form=RentalProducts_add_Form(request.POST or None)

    records=RentalMainCategories.objects.all()
    if request.method == "POST":
        processed_by=CustomUser.objects.get(id=request.user.id)
        description=request.POST.get("description")

        if not description:
            messages.error(request,'Description is Missing')
            return HttpResponseRedirect(reverse('RentalMainCategories_add'))

        if RentalMainCategories.objects.filter(description=description).exists():
            messages.info(request,'Record already Exist')
            return HttpResponseRedirect(reverse('RentalMainCategories_add'))

        RentalMainCategories(description=description.upper(),processed_by=processed_by).save()
        return HttpResponseRedirect(reverse('RentalMainCategories_add'))

    context={

     'form':form,
     'records':records,
     'task_array':task_array,
    }
    return render(request,'master_templates/RentalMainCategories_add.html',context)


def RentalMainCategories_delete(request,pk):
    RentalMainCategories.objects.filter(id=pk).delete()
    messages.info(request,'Record Deleted')
    return HttpResponseRedirect(reverse('RentalMainCategories_add'))



def RentalProducts_add(request):
    task_array=[]
    if not request.user.user_type == '1':
        tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
        for task in tasks:
            task_array.append(task.task.title)


    form=RentalProducts_add_Form(request.POST or None)

    records=RentalProducts.objects.all()

    if request.method == "POST":
        processed_by=CustomUser.objects.get(id=request.user.id)

        description=request.POST.get("description")

        if not description:
            messages.error(request,'Description is Missing')
            return HttpResponseRedirect(reverse('RentalProducts_add'))

        if RentalProducts.objects.filter(description=description).exists():
            messages.info(request,'Record already Exist')
            return HttpResponseRedirect(reverse('RentalProducts_add'))

        RentalProducts(description=description.upper(),processed_by=processed_by).save()
        return HttpResponseRedirect(reverse('RentalProducts_add'))
    context={

     'form':form,
     'records':records,
     'task_array':task_array,
    }
    return render(request,'master_templates/RentalProducts_add.html',context)


def RentalProducts_delete(request,pk):
    RentalProducts.objects.filter(id=pk).delete()
    messages.info(request,'Record Deleted')
    return HttpResponseRedirect(reverse('RentalProducts_add'))



def Rental_Price_Settings(request):
    task_array=[]
    if not request.user.user_type == '1':
        tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
        for task in tasks:
            task_array.append(task.task.title)
    form=Rental_Price_Settings_Form(request.POST or None)

    records=RentalPriceSettings.objects.all()

    if request.method == 'POST':
        processed_by=CustomUser.objects.get(id=request.user.id)
        amount = request.POST.get('amount')

        if not amount or float(amount) < 0:
            messages.error(request,'Amount cannot be less zero')
            return HttpResponseRedirect(reverse('Rental_Price_Settings'))

        main_category_id=request.POST.get('category')
        main_category=RentalMainCategories.objects.get(id=main_category_id)

        product_id=request.POST.get('product')
        product=RentalProducts.objects.get(id=product_id)

        if  RentalPriceSettings.objects.filter(main_category=main_category,products=product).exists():
            record=RentalPriceSettings.objects.get(main_category=main_category,products=product)
            record.amount=amount
            record.status='ACTIVE'
            record.save()
            messages.success(request,'Record Updated Successfully')
            return HttpResponseRedirect(reverse('Rental_Price_Settings'))

        RentalPriceSettings(main_category=main_category,products=product,amount=amount,status='ACTIVE',processed_by=processed_by).save()
        messages.success(request,'Record Added Successfully')
        return HttpResponseRedirect(reverse('Rental_Price_Settings'))

    context={
     'form':form,
     'records':records,
     'task_array':task_array,
    }
    return render(request,'master_templates/Rental_Price_Settings.html',context)


def Rental_Price_Settings_delete(request,pk):
    RentalPriceSettings.objects.filter(id=pk).delete()
    messages.info(request,'Record Deleted')
    return HttpResponseRedirect(reverse('Rental_Price_Settings'))

####################################################################
###################### FIN. SECRETARY ######################
####################################################################

def Cash_Withdrawal_Approved_list_load(request):
    task_array=[]
    if not request.user.user_type == '1':
        tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
        for task in tasks:
            task_array.append(task.task.title)

    applicants=MembersCashWithdrawalsApplication.objects.filter(status='UNTREATED',approval_status='APPROVED')

    context={
    'task_array':task_array,
    'applicants':applicants,
    }
    return render(request,'master_templates/FINSEC/Cash_Withdrawal_Approved_list_load.html',context)




#######################################################################
################## GENERAL REPORT #####################################
#######################################################################

def transaction_views_ranked(request):
    task_array=[]
    if not request.user.user_type == '1':
        tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
        for task in tasks:
            task_array.append(task.task.title)
    transactions=TransactionTypes.objects.filter(~Q(source__title='GENERAl')).order_by('rank')
    context={
    'task_array':task_array,
    'transactions':transactions,

    }
    return render(request,'master_templates/reports/transaction_views_ranked.html',context)


def List_of_Users(request):
    task_array=[]
    if not request.user.user_type == '1':
        tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
        for task in tasks:
            task_array.append(task.task.title)
    users=Staff.objects.all()
    records=UserType.objects.all().order_by('code')
    # users=Staff.objects.annotate(full_name=Concat("admin__first_name", Value(" "), "admin__last_name")).all().values_lst("full_name")

    context={
    'task_array':task_array,
    'users':users,
    'records':records,
    }
    return render(request,'master_templates/List_of_Users.html',context)
