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
####################################################################
###################### HOME PAGE ###################################
####################################################################


def admin_home(request):
    record=DataCaptureManager.objects.first()
    title="System Admin"
  
    context={
    'title':title,
    'record':record,
    }
    return render(request, "master_templates/dashboard.html",context)


def system_reset(request):
   
    # record=MembersNextOfKins.objects.all()
    # record.delete()
    record=CustomUser.objects.filter(user_type=10)
    record.delete()
    record=MemberShipRequest.objects.all()
    record.delete()
    record=MemberShipRequestAdditionalInfo.objects.all()
    record.delete()
    record=MemberShipRequestAdditionalAttachment.objects.all()
    record.delete()
    record=MemberShipFormSalesRecord.objects.all()
    record.delete()
    record=Members.objects.all()
    record.delete()

    record=AccountDeductions.objects.all()
    record.delete()
    record=CooperativeBankAccounts.objects.all()
    record.delete()    

    # record=ApprovableTransactions.objects.all()
    # record.delete()
    # record=ApprovalOfficers.objects.all()
    # record.delete()
    # record=TransactionPeriods.objects.all()
    # record.delete()
    # record=Receipts.objects.all()
    # record.delete()
    # record=CooperativeBankAccounts.objects.all()
    # record.delete()
    # record=CertifiableTransactions.objects.all()
    # record.delete()
    # record=CertificationOfficers.objects.all()
    # record.delete()


    record=SavingsUploaded.objects.all()
    record.delete()
    record=LoansUploaded.objects.all()
    record.delete()
    record=MembersExclusiveness.objects.all()
    record.delete()

    record=StandingOrderAccounts.objects.all()
    record.delete()
    record=LoanRequest.objects.all()
    record.delete()
    record=LoanGuarantors.objects.all()
    record.delete()
    record=ExternalFascilitiesTemp.objects.all()
    record.delete()
    record=ExternalFascilitiesMain.objects.all()
    record.delete()
    record=LoanRequestAttachments.objects.all()
    record.delete()
    record=LoanRequestSettings.objects.all()
    record.delete()
    record=LoanFormIssuance.objects.all()
    record.delete()
    record=LoanApplication.objects.all()
    record.delete()
    record=LoanApplicationGuarnators.objects.all()
    record.delete()
    record=LoanApplicationSettings.objects.all()
    record.delete()
    record=LoansDisbursed.objects.all()
    record.delete()
    record=LoansCleared.objects.all()
    record.delete()
    record=MonthlyDeductionList.objects.all()
    record.delete()
    record=MonthlyGeneratedTransactions.objects.all()
    record.delete()
    record=MonthlyDeductionListGenerated.objects.all()
    record.delete()
    record=MonthlyGroupGeneratedTransactions.objects.all()
    record.delete()
    record=AccountDeductions.objects.all()
    record.delete()
    record=NonMemberAccountDeductions.objects.all()
    record.delete()
    record=MembersSalaryUpdateRequest.objects.all()
    record.delete()
    record=PersonalLedger.objects.all()
    record.delete()
    record=CashBook.objects.all()
    record.delete()
    record=NorminalRoll.objects.all()
    record.delete()
    record=Stock.objects.all()
    record.delete()
    record=Members_Credit_Sales_Selected.objects.all()
    record.delete()
    record=Members_Credit_Sales_external_fascilities.objects.all()
    record.delete()
    record=members_credit_purchase_summary.objects.all()
    record.delete()
    record=members_credit_purchase_analysis.objects.all()
    record.delete()
    record=CustomerID.objects.all()
    record.delete()
    record=Customers.objects.all()
    record.delete()
    record=General_Cash_Sales_Selected.objects.all()
    record.delete()
    record=Daily_Sales.objects.all()
    record.delete()
    record=Daily_Sales_Summary.objects.all()
    record.delete()
    record=Cheque_Table.objects.all()
    record.delete()
    record=CooperativeShopLedger.objects.all()
    record.delete()

    return HttpResponseRedirect(reverse('admin_home'))



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
def LoanMergeStatus_upload(request):
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
        
    context = {}
    return render(request, template, context)



@permission_required('admin.can_add_log_entry')
def MultipleLoanStatus_upload(request):
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
        
    context = {}
    return render(request, template, context)


@permission_required('admin.can_add_log_entry')
def WithdrawalStatus_upload(request):
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
        
    context = {}
    return render(request, template, context)



@permission_required('admin.can_add_log_entry')
def DateJoinedUploadStatus_upload(request):
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
        
    context = {}
    return render(request, template, context)


@permission_required('admin.can_add_log_entry')
def WelfareUploadStatus_upload(request):
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
        
    context = {}
    return render(request, template, context)


@permission_required('admin.can_add_log_entry')
def SharesUploadStatus_upload(request):
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
        
    context = {}
    return render(request, template, context)


@permission_required('admin.can_add_log_entry')
def UsersLevel_upload(request):
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
        
    context = {}
    return render(request, template, context)


@permission_required('admin.can_add_log_entry')
def SharesUnits_upload(request):
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
        
    context = {}
    return render(request, template, context)


@permission_required('admin.can_add_log_entry')
def LoansUploadStatus_upload(request):
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
        
    context = {}
    return render(request, template, context)


@permission_required('admin.can_add_log_entry')
def LoanCategory_upload(request):
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
        
    context = {}
    return render(request, template, context)


@permission_required('admin.can_add_log_entry')
def SavingsUploadStatus_upload(request):
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
        
    context = {}
    return render(request, template, context)


@permission_required('admin.can_add_log_entry')
def LoanScheduleStatus_upload(request):
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
        
    context = {}
    return render(request, template, context)

    

@permission_required('admin.can_add_log_entry')
def ExlusiveStatus_upload(request):
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
        
    context = {}
    return render(request, template, context)



@permission_required('admin.can_add_log_entry')
def LockedStatus_upload(request):
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
        
    context = {}
    return render(request, template, context)



@permission_required('admin.can_add_log_entry')
def ReceiptTypes_upload(request):
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
        
    context = {}
    return render(request, template, context)


    
@permission_required('admin.can_add_log_entry')
def PaymentChannels_upload(request):
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
        
    context = {}
    return render(request, template, context)


    
@permission_required('admin.can_add_log_entry')
def TicketStatus_upload(request):
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
        
    context = {}
    return render(request, template, context)





@permission_required('admin.can_add_log_entry')
def SalesCategory_upload(request):
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
        
    context = {}
    return render(request, template, context)



@permission_required('admin.can_add_log_entry')
def ProductCategory_upload(request):
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
        
    context = {}
    return render(request, template, context)

  
@permission_required('admin.can_add_log_entry')
def Product_Write_off_Reasons_upload(request):
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
        
    context = {}
    return render(request, template, context)

  
@permission_required('admin.can_add_log_entry')
def Stock_upload(request):
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
        
    context = {}
    return render(request, template, context)



def upload_stock_roll(request):   
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
    
    'DataCapture':DataCapture,
    }
    return render(request,'master_templates/upload_stock.html',context) 


  
  
@permission_required('admin.can_add_log_entry')
def AdminCharges_upload(request):
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
        
    context = {}
    return render(request, template, context)

    

@permission_required('admin.can_add_log_entry')
def title_upload(request):
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
        
    context = {}
    return render(request, template, context)


@permission_required('admin.can_add_log_entry')
def states_upload(request):
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
        
    context = {}
    return render(request, template, context)



@permission_required('admin.can_add_log_entry')
def NOKRelationships_upload(request):
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
        
    context = {}
    return render(request, template, context)


@permission_required('admin.can_add_log_entry')
def lga_upload(request):
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
        
    context = {}
    return render(request, template, context)



@permission_required('admin.can_add_log_entry')
def SubmissionStatus_upload(request):
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
        
    context = {}
    return render(request, template, context)


@permission_required('admin.can_add_log_entry')
def MembershipStatus_upload(request):
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
        
    context = {}
    return render(request, template, context)


@permission_required('admin.can_add_log_entry')
def ProcessingStatus_upload(request):
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
        
    context = {}
    return render(request, template, context)


@permission_required('admin.can_add_log_entry')
def CertificationStatus_upload(request):
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
        
    context = {}
    return render(request, template, context)


@permission_required('admin.can_add_log_entry')
def ApprovalStatus_upload(request):
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
        
    context = {}
    return render(request, template, context)



@permission_required('admin.can_add_log_entry')
def TransactionStatus_upload(request):
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
        
    context = {}
    return render(request, template, context)


    
@permission_required('admin.can_add_log_entry')
def ReceiptStatus_upload(request):
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
        
    context = {}
    return render(request, template, context)    


    
@permission_required('admin.can_add_log_entry')
def Gender_upload(request):
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
        
    context = {}
    return render(request, template, context)    


@permission_required('admin.can_add_log_entry')
def Banks_upload(request):
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
        
    context = {}
    return render(request, template, context)    





    
@permission_required('admin.can_add_log_entry')
def Locations_upload(request):
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
        
    context = {}
    return render(request, template, context)    



@permission_required('admin.can_add_log_entry')
def AccountTypes_upload(request):
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
        
    context = {}
    return render(request, template, context)

    
@permission_required('admin.can_add_log_entry')
def Departments_upload(request):
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
        
    context = {}
    return render(request, template, context)

    
@permission_required('admin.can_add_log_entry')
def SalaryInstitution_upload(request):
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
        
    context = {}
    return render(request, template, context)   

    
@permission_required('admin.can_add_log_entry')
def InterestDeductionSource_upload(request):
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
        
    context = {}
    return render(request, template, context)   

    
    
@permission_required('admin.can_add_log_entry')
def TransactionSources_upload(request):
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
        
    context = {}
    return render(request, template, context)


@permission_required('admin.can_add_log_entry')
def UserType_upload(request):
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
        
    context = {}
    return render(request, template, context)



@permission_required('admin.can_add_log_entry')
def loan_criteria_base_upload(request):
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
        
    context = {}
    return render(request, template, context)




####################################################################
###################### USER ACCOUNT MANAGERS ######################
####################################################################
def DataCapture_Manager(request):
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
    'form':form,

    }
    return render(request,'master_templates/DataCapture_Manager.html',context)


def addUserType(request):
	items = UserType.objects.all()
	form=addUserTypesForm(request.POST or None)
	if request.method == "POST":
		form = addUserTypesForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(reverse('addUserType'))
	context={
	'form':form,
	'items':items

	}
	return render(request,'master_templates/add_user_types.html', context)


def UserType_delete(request, pk):
	user_type = UserType.objects.get(id=pk)
	user_type.delete()
	return HttpResponseRedirect(reverse('addUserType'))


def add_staff(request):
    title="Add Staff"
    form = addUsersForm(request.POST or None)
    items=UserType.objects.all()
    users = CustomUser.objects.exclude(Q(user_type__iexact='1') | Q(user_type__iexact='10'))
    if request.method == "POST":
        title_id=request.POST.get("title")
        title=Titles.objects.get(id=title_id)

        userlevel_id=request.POST.get('userlevel')
        userlevel=UsersLevel.objects.get(id=userlevel_id)
        
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
        password="Password123"

        try:
            if user_type.code == '2':
                user = CustomUser.objects.create_user(username=username,password=password,email=email,last_name=last_name,first_name=first_name,user_type=2)
            if user_type.code == '3':
                user = CustomUser.objects.create_user(username=username,password=password,email=email,last_name=last_name,first_name=first_name,user_type=3)
            if user_type.code == '4':
                user = CustomUser.objects.create_user(username=username,password=password,email=email,last_name=last_name,first_name=first_name,user_type=4)
            if user_type.code == '5':
                user = CustomUser.objects.create_user(username=username,password=password,email=email,last_name=last_name,first_name=first_name,user_type=5)
            if user_type.code == '6':
                user = CustomUser.objects.create_user(username=username,password=password,email=email,last_name=last_name,first_name=first_name,user_type=6)
            if user_type.code == '7':
                user = CustomUser.objects.create_user(username=username,password=password,email=email,last_name=last_name,first_name=first_name,user_type=7)
            if user_type.code == '8':
                user = CustomUser.objects.create_user(username=username,password=password,email=email,last_name=last_name,first_name=first_name,user_type=8)
            if user_type.code == '9':
                user = CustomUser.objects.create_user(username=username,password=password,email=email,last_name=last_name,first_name=first_name,user_type=9)


            user.staff.middle_name=middle_name
            user.staff.address=address
            user.staff.phone_number=phone_number
            user.staff.gender=gender
            user.staff.title=title
            user.staff.userlevel=userlevel
            user.save()
            messages.success(request,"User Added Successfully")
            return HttpResponseRedirect(reverse("add_staff"))
        except:
            messages.error(request,"Failed to add System User")
            return HttpResponseRedirect(reverse("add_staff")) 

    context={
    'title':title,
    'form':form,
    'users':users,
    'url':'add_staff',
    'items':items,
    'button_text':"Add",
    }
    return render(request, "master_templates/add_staff.html",context)



def add_staff_manage(request):
    users = CustomUser.objects.exclude(Q(user_type__iexact='1') | Q(user_type__iexact='10'))
    context={
    'users':users,
    }
    return render(request,'master_templates/addStaff_manage.html',context)

def add_staff_manage_view(request,pk):
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
    form.fields['userlevel'].initial=user.userlevel.id
    form.fields['username'].initial=user.admin.username
    form.fields['user_type'].initial=user_type.id
    form.fields['email'].initial=user.admin.email
    
    if request.method == "POST":
        title_id=request.POST.get("title")
        title=Titles.objects.get(id=title_id)

        userlevel_id=request.POST.get('userlevel')
        userlevel=UsersLevel.objects.get(id=userlevel_id)
        
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
        user.userlevel=userlevel
        user.title=title

        user.save()
        user.admin.save()
        return HttpResponseRedirect(reverse('add_staff_manage'))
    context={
    'form':form,
    }
    return render(request,'master_templates/add_staff_manage_view.html',context)


def super_user_manage(request):
    users = CustomUser.objects.filter(Q(user_type__iexact='1'))
    context={
    'users':users,
    }
    return render(request,'master_templates/super_user_manage.html',context)


def super_user_manage_view(request,pk):
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
    'form':form,
    }
    return render(request,'master_templates/super_user_manage_view.html',context)

####################################################################
###################### MEMBERS SHARES AND WELFARE ##################
####################################################################
def Shares_Deduction_savings(request):
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
    'form':form,
    'records':records,
    }
    return render(request,'master_templates/Shares_Deduction_savings.html',context)


def Shares_Deduction_savings_remove(request,pk):
    record=SharesDeductionSavings.objects.get(id=pk)
    record.delete()
    return HttpResponseRedirect(reverse('Shares_Deduction_savings'))


def AddShares_Configurations(request):
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
    'form':form,
    'record':record,
    }
    return render(request,'master_templates/AddShares_Configurations.html',context)


def addWelfare_Configurations(request):
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
    'form':form,
    'record':record,
    }
    return render(request,'master_templates/addWelfare_Configurations.html',context)


####################################################################
###################### COMPONENNTS PAGE ############################
####################################################################
def MembersCompulsorySavings(request):
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
        'form':form,
        'records':records,
    }
    return render(request,'master_templates/MembersCompulsorySavings.html', context)


def MembersCompulsorySavings_delete(request,pk):
    record = CompulsorySavings.objects.get(id=pk)
    record.delete()
    return HttpResponseRedirect(reverse('MembersCompulsorySavings'))


def addState(request):
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
	'form':form,
	'items':items,
	'url':'addState',
	'button_text':"Add State",
	'title':title,
	}
	return render(request,'master_templates/add_single_item.html', context)



def Manage_state(request):
	states=States.objects.all()
	context={
	'states':states,
	}
	return render(request,'master_templates/manage_state.html', context)


def delete_state(request,pk):
	state=States.objects.get(id=pk)
	state.delete()
	messages.success(request,"Record Deleted Successfully")
	return HttpResponseRedirect(reverse('addState'))


def addNOKRelationships(request):
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
    'form':form,
    'items':items,
    'url':'NOKRelationships',
    'button_text':"Add Record",
    'title':title,
    }
    return render(request,'master_templates/add_single_item.html', context)


def Manage_NOKRelationships(request):
    Relationships=NOKRelationships.objects.all()
    context={
    'Relationships':Relationships,
    }
    return render(request,'master_templates/manage_NOKRelationships.html', context)


def Manage_NOKRelationships_Remove(request,pk):
    relationship=NOKRelationships.objects.get(id=pk)
    relationship.delete()
    return HttpResponseRedirect(reverse('Manage_NOKRelationships'))


def addTransactionStatus(request):
	title="Add Transaction Status"
	items= TransactionStatus.objects.all()
	form = addTransactionStatusForm(request.POST or None)
	if request.method ==  "POST":
		form = addTransactionStatusForm(request.POST)
		if form.is_valid():
			title=form.cleaned_data["title"]
			record = TransactionStatus(title=title)
			record.save()
			messages.success(request,"Record Added Successfully")
			return	HttpResponseRedirect(reverse('addTransactionStatus'))
	context={
	'form':form,
	'items':items,
	'url':'addTransactionStatus',
	'button_text':"Add Record",
	'title':title,
	}
	return render(request,'master_templates/add_single_item.html', context)


def addReceiptStatus(request):
	title="Add Receipt Status"
	items= ReceiptStatus.objects.all()
	form = addReceiptStatusForm(request.POST or None)
	if request.method ==  "POST":
		form = addReceiptStatusForm(request.POST)
		if form.is_valid():
			title=form.cleaned_data["title"]
			record = ReceiptStatus(title=title)
			record.save()
			messages.success(request,"Record Added Successfully")
			return	HttpResponseRedirect(reverse('addReceiptStatus'))
	context={
	'form':form,
	'items':items,
	'url':'addReceiptStatus',
	'button_text':"Add Record",
	'title':title,
	}
	return render(request,'master_templates/add_single_item.html', context)


def addProcessingStatus(request):
	title="Add Processing Status"
	items= ProcessingStatus.objects.all()
	form = addProcessingStatusForm(request.POST or None)
	if request.method ==  "POST":
		form = addProcessingStatusForm(request.POST)
		if form.is_valid():
			title=form.cleaned_data["title"]
			record = ProcessingStatus(title=title)
			record.save()
			messages.success(request,"Record Added Successfully")
			return	HttpResponseRedirect(reverse('addProcessingStatus'))
	context={
	'form':form,
	'items':items,
	'url':'addProcessingStatus',
	'button_text':"Add Record",
	'title':title,
	}
	return render(request,'master_templates/add_single_item.html', context)


# def addUserLevels(request):
# 	title="Add User Levels"
# 	items= UserLevels.objects.all()
# 	form = addUserLevelsForm(request.POST or None)
# 	if request.method ==  "POST":
# 		form = addUserLevelsForm(request.POST)
# 		if form.is_valid():
# 			title=form.cleaned_data["title"]
# 			record = UserLevels(title=title)
# 			record.save()
# 			messages.success(request,"Record Added Successfully")
# 			return	HttpResponseRedirect(reverse('addUserLevels'))
# 	context={
# 	'form':form,
# 	'items':items,
# 	'url':'addUserLevels',
# 	'button_text':"Add Record",
# 	'title':title,
# 	}
# 	return render(request,'master_templates/add_single_item.html', context)


def addTransactionSources(request):
	title="Add Transaction Sources"
	items= TransactionSources.objects.all()
	form = addTransactionSourcesForm(request.POST or None)
	if request.method ==  "POST":
		form = addTransactionSourcesForm(request.POST)
		if form.is_valid():
			title=form.cleaned_data["title"]
			record = TransactionSources(title=title)
			record.save()
			messages.success(request,"Record Added Successfully")
			return	HttpResponseRedirect(reverse('addTransactionSources'))
	context={
	'form':form,
	'items':items,
	'url':'addTransactionSources',
	'button_text':"Add Record",
	'title':title,
	}
	return render(request,'master_templates/add_single_item.html', context)


def addGender(request):
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
	'form':form,
	'items':items,
	'url':'addGender',
	'button_text':"Add Record",
	'title':title,
	}
	return render(request,'master_templates/add_single_item.html', context)


def addInterestDeductionSource(request):
	title="Add Interest Deduction Source"
	items= InterestDeductionSource.objects.all()
	form = addInterestDeductionSourceForm(request.POST or None)
	if request.method ==  "POST":
		form = addInterestDeductionSourceForm(request.POST)
		if form.is_valid():
			title=form.cleaned_data["title"]
			record = InterestDeductionSource(title=title)
			record.save()
			messages.success(request,"Record Added Successfully")
			return	HttpResponseRedirect(reverse('addInterestDeductionSource'))
	context={
	'form':form,
	'items':items,
	'url':'addInterestDeductionSource',
	'button_text':"Add Record",
	'title':title,
	}
	return render(request,'master_templates/add_single_item.html', context)


def addSalaryInstitution(request):
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
	'form':form,
	'items':items,
	'url':'addSalaryInstitution',
	'button_text':"Add Record",
	'title':title,
	}
	return render(request,'master_templates/add_single_item.html', context)


def addTitles(request):
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
	'form':form,
	'items':items,
	'url':'addTitles',
	'button_text':"Add Record",
	'title':title,
	}
	return render(request,'master_templates/add_single_item.html', context)


def addDepartments(request):
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
	'form':form,
	'items':items,
	'url':'addDepartments',
	'button_text':"Add Record",
	'title':title,
	}
	return render(request,'master_templates/add_single_item.html', context)

def addBanks(request):
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
	'form':form,
	'items':items,
	'url':'addBanks',
	'button_text':"Add Record",
	'title':title,
	}
	return render(request,'master_templates/add_single_item.html', context)

	
def addLocations(request):
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
	'form':form,
	'items':items,
	'url':'addLocations',
	'button_text':"Add Record",
	'title':title,
	}
	return render(request,'master_templates/add_single_item.html', context)


def addMembershipStatus(request):
	title="Add Membership Status"
	items= MembershipStatus.objects.all()
	form = addMembershipStatusForm(request.POST or None)
	if request.method ==  "POST":
		form = addMembershipStatusForm(request.POST)
		if form.is_valid():
			title=form.cleaned_data["title"]
			record = MembershipStatus(title=title)
			record.save()
			messages.success(request,"Record Added Successfully")
			return	HttpResponseRedirect(reverse('addMembershipStatus'))
	context={
	'form':form,
	'items':items,
	'url':'addMembershipStatus',
	'button_text':"Add Record",
	'title':title,
	}
	return render(request,'master_templates/add_single_item.html', context)


def addDefaultPassword(request):
	title="Add Membership Status"
	item= DefaultPassword.objects.filter()

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

	form.fields['title'].initial=items[0].title
	context={
	'form':form,
	'items':items,
	'url':'addDefaultPassword',
	'button_text':"Add Record",
	'title':title,
	}
	return render(request,'master_templates/add_single_item.html', context)



def addTransactionTypes(request):
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
        if TransactionTypes.objects.filter(code=code).exists():
            messages.error(request,"Record with this code already exist")
            return HttpResponseRedirect(reverse('addTransactionTypes'))

        record = TransactionTypes(receipt_type=receipts,source=source,code=code,name=name,maximum_amount=maximum_amount,minimum_amount=minimum_amount,rank=rank,share_unit_min=share_unit_min,share_unit_max=share_unit_max)
        record.save()
        return HttpResponseRedirect(reverse('addTransactionTypes'))
    context={
    'form':form,
    'transaction_types':transaction_types,
    }
    return render(request, 'master_templates/addTransactionTypes.html',context)


def TransactionTypes_Manage_Load(request):
    
    transaction_types = TransactionTypes.objects.all().order_by("code")
    
    context={
 
    'transaction_types':transaction_types,
    }
    return render(request,'master_templates/TransactionTypes_Manage_Load.html',context)


def TransactionTypes_Update(request,pk):
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
    'form':form,
    'transaction':transaction,
    }
    return render(request,'master_templates/TransactionTypes_Update.html',context)


####################################################################
###################### LOAN RELATED MATTERS ########################
####################################################################

def loan_based_savings_update(request):
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
	'form':form,
	'saving':saving,
	}
	return render(request, 'master_templates/loan_based_savings.html',context)



def loan_settings_load(request):
	records = TransactionTypes.objects.filter(source__title="LOAN")
	context={
	'records':records,
	}
	return render(request, 'master_templates/loan_settings_load.html',context)


def loan_settings_details_load(request,pk):
	record = TransactionTypes.objects.get(id=pk)
	saving= LoanBasedSavings.objects.first()
	context={
	'record':record,
	'saving':saving,
	'pk':pk,
	}
	return render(request, 'master_templates/loan_settings_details_load.html',context)


def loan_guarantors_update(request,pk):
    item= TransactionTypes.objects.get(id=pk)
    title="Update Loan Guarnators for " +  item.name
    
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
    'form':form,
    'url':'loan_guarantors_update',
    'button_text':"Update Record",
    'title':title,
    }
    return render(request,'master_templates/loan_criteria_update.html', context)


def default_admin_charges_update(request,pk):
    item= TransactionTypes.objects.get(id=pk)
    title="Update Default Admin Charges for " +  item.name
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
    'form':form,
    # 'items':items,
    'url':'default_admin_charges_update',
    'button_text':"Update Record",
    'title':title,
    }
    return render(request,'master_templates/loan_criteria_update.html', context)

    
def MultipleLoanStatus_update(request,pk):
    item= TransactionTypes.objects.get(id=pk)
    title="Update Default Admin Charges for " +  item.name
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
    'form':form,
    # 'items':items,
    'url':'MultipleLoanStatus_update',
    'button_text':"Update Record",
    'title':title,
    }
    return render(request,'master_templates/loan_criteria_update.html', context)


def loan_savings_based_update(request,pk):
    item= TransactionTypes.objects.get(id=pk)
    title="Update Loan Savings Based for " +  item.name
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
    'form':form,
    # 'items':items,
    'url':'loan_savings_based_update',
    'button_text':"Update Record",
    'title':title,
    }
    return render(request,'master_templates/loan_criteria_update.html', context)



def loan_category_update(request,pk):
    item= TransactionTypes.objects.get(id=pk)
    title="Update Loan Category for " +  item.name
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
    'form':form,
    # 'items':items,
    'url':'loan_category_update',
    'button_text':"Update Record",
    'title':title,
    }
    return render(request,'master_templates/loan_criteria_update.html', context)


def loan_duration_update(request,pk):
    item= TransactionTypes.objects.get(id=pk)
    title="Update Loan Duration for " +  item.name
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
    'form':form,
    # 'items':items,
    'url':'loan_duration_update',
    'button_text':"Update Record",
    'title':title,
    }
    return render(request,'master_templates/loan_criteria_update.html', context)


def loan_name_update(request,pk):
	item= TransactionTypes.objects.get(id=pk)
	title="Update Loan Description for " +  item.name
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
	'form':form,
	# 'items':items,
	'url':'loan_name_update',
	'button_text':"Update Record",
	'title':title,
	}
	return render(request,'master_templates/loan_criteria_update.html', context)


def loan_interest_rate_update(request,pk):
	item= TransactionTypes.objects.get(id=pk)
	title="Update Loan Interest Rate  for " +  item.name
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
	'form':form,
	# 'items':items,
	'url':'loan_interest_rate_update',
	'button_text':"Update Record",
	'title':title,
	}
	return render(request,'master_templates/loan_criteria_update.html', context)


def loan_interest_deduction_soucrces_update(request,pk):
	item= TransactionTypes.objects.get(id=pk)
	title="Update Loan Interest Deduction Sources  for " +  item.name
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
	'form':form,
	# 'items':items,
	'url':'loan_interest_deduction_soucrces_update',
	'button_text':"Update Record",
	'title':title,
	}
	return render(request,'master_templates/loan_criteria_update.html', context)


def loan_maximum_amount_update(request,pk):
	item= TransactionTypes.objects.get(id=pk)
	title="Update Loan Maximum Amount  for " +  item.name
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
	'form':form,
	# 'items':items,
	'url':'loan_maximum_amount_update',
	'button_text':"Update Record",
	'title':title,
	}
	return render(request,'master_templates/loan_criteria_update.html', context)


def loan_rank_update_update(request,pk):
	item= TransactionTypes.objects.get(id=pk)
	title="Update Loan Rank  for " +  item.name
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
	'form':form,
	# 'items':items,
	'url':'loan_rank_update_update',
	'button_text':"Update Record",
	'title':title,
	}
	return render(request,'master_templates/loan_criteria_update.html', context)


def loan_admin_charges_rate_update(request,pk):
	item= TransactionTypes.objects.get(id=pk)
	title="Update Loan Rank  for " +  item.name
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
	'form':form,
	# 'items':items,
	'url':'loan_admin_charges_rate_update',
	'button_text':"Update Record",
	'title':title,
	}
	return render(request,'master_templates/loan_criteria_update.html', context)




def loan_admin_charges_update(request,pk):
	item= TransactionTypes.objects.get(id=pk)
	title="Update Loan Admin Charges  for " +  item.name
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
	'form':form,
	# 'items':items,
	'url':'loan_admin_charges_update',
	'button_text':"Update Record",
	'title':title,
	}
	return render(request,'master_templates/loan_criteria_update.html', context)

	

def loan_admin_charges_minimum_update(request,pk):
	item= TransactionTypes.objects.get(id=pk)
	title="Update Loan Admin Charges Minimum  for " +  item.name
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
	'form':form,
	# 'items':items,
	'url':'loan_admin_charges_minimum_update',
	'button_text':"Update Record",
	'title':title,
	}
	return render(request,'master_templates/loan_criteria_update.html', context)

	
def loan_salary_relationship_update(request,pk):
	item= TransactionTypes.objects.get(id=pk)
	title="Update Loan Salary Loan Relationship  for " +  item.name
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
	'form':form,
	# 'items':items,
	'url':'loan_salary_relationship_update',
	'button_text':"Update Record",
	'title':title,
	}
	return render(request,'master_templates/loan_criteria_update.html', context)
	

def loan_loan_age_update(request,pk):
	item= TransactionTypes.objects.get(id=pk)
	title="Update Loan Age  for " +  item.name
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
	'form':form,
	# 'items':items,
	'url':'loan_loan_age_update',
	'button_text':"Update Record",
	'title':title,
	}
	return render(request,'master_templates/loan_criteria_update.html', context)




####################################################################
###################### APPROVABLE TRANSACTION ######################
####################################################################

def AddApprovableTransactions(request):
	transactions = ApprovableTransactions.objects.all()
	title="Manage Approvable Transactions"
	title1="Approvable Transactions"
	form = ApprovableTransactions_form(request.POST or None)

	if request.method ==  "POST":
		status=MembershipStatus.objects.get(title="ACTIVE")
		form = ApprovableTransactions_form(request.POST)
		if form.is_valid():
			transaction_id=form.cleaned_data["transaction"]
			transaction = TransactionTypes.objects.get(id=transaction_id)
			record=ApprovableTransactions(transaction=transaction,status=status)
			record.save()
			messages.success(request,"Record Updated Successfully")
			return	HttpResponseRedirect(reverse('AddApprovableTransactions'))
	context={
	'form':form,
	'transactions':transactions,
	'url':'AddApprovableTransactions',
	'button_text':"Add Record",
	'title':title,
	'title1':title1,
	}
	return render(request,'master_templates/approvable_transactions.html', context)


def AddApprovableTransactionsUpdate(request,pk):
	status1=MembershipStatus.objects.get(title="ACTIVE")
	status2=MembershipStatus.objects.get(title="INACTIVE")
	record=ApprovableTransactions.objects.get(id=pk)
	
	if record.status==status1:
		record.status=status2
	elif record.status==status2:
		record.status=status1

	record.save()
	return	HttpResponseRedirect(reverse('AddApprovableTransactions'))


def ApprovableOfficers(request):
    user_types = UserType.objects.all()
    officers = ApprovalOfficers.objects.all()
    title="Manage Approval Officers"
    title1="Approval Officer"
    form = ApprovableOfficers_form(request.POST or None)

    if request.method ==  "POST":
        status=MembershipStatus.objects.get(title="ACTIVE")
        form = ApprovableOfficers_form(request.POST or None)
        if form.is_valid():
            officer_id=form.cleaned_data['officers']
            officer = CustomUser.objects.get(id=officer_id)

            transaction_id=form.cleaned_data["transaction"]
            transaction = ApprovableTransactions.objects.get(id=transaction_id)

            record=ApprovalOfficers(officer=officer,transaction=transaction,status=status)
            record.save()
            messages.success(request,"Record Updated Successfully")
            return	HttpResponseRedirect(reverse('ApprovableOfficers'))
    context={
    'form':form,
    'officers':officers,
    'user_types':user_types,
    'url':'ApprovableOfficers',
    'button_text':"Add Record",
    'title':title,
    'title1':title1,
    }
    return render(request,'master_templates/ApprovableOfficers.html', context)


def ApprovableOfficersUpdate(request,pk):
	status1=MembershipStatus.objects.get(title="ACTIVE")
	status2=MembershipStatus.objects.get(title="INACTIVE")
	record=ApprovalOfficers.objects.get(id=pk)
	
	if record.status==status1:
		record.status=status2
	elif record.status==status2:
		record.status=status1

	record.save()
	return	HttpResponseRedirect(reverse('ApprovableOfficers'))

	


def AddCertifiableTransactions(request):
	transactions = CertifiableTransactions.objects.all()
	title="Manage Certifiable Transactions"
	title1="Certifiable Transactions"
	form = CertifiableTransactions_form(request.POST or None)

	if request.method ==  "POST":
		status=MembershipStatus.objects.get(title="ACTIVE")
		form = CertifiableTransactions_form(request.POST)
		if form.is_valid():
			transaction_id=form.cleaned_data["transaction"]
			transaction = TransactionTypes.objects.get(id=transaction_id)
			record=CertifiableTransactions(transaction=transaction,status=status)
			record.save()
			messages.success(request,"Record Updated Successfully")
			return	HttpResponseRedirect(reverse('AddCertifiableTransactions'))
	context={
	'form':form,
	'transactions':transactions,
	'url':'AddCertifiableTransactions',
	'button_text':"Add Record",
	'title':title,
	'title1':title1,
	}
	return render(request,'master_templates/certifiable_transactions.html', context)



def AddCertifiableTransactionsUpdate(request,pk):
	status1=MembershipStatus.objects.get(title="ACTIVE")
	status2=MembershipStatus.objects.get(title="INACTIVE")
	record=CertifiableTransactions.objects.get(id=pk)
	
	if record.status==status1:
		record.status=status2
	elif record.status==status2:
		record.status=status1

	record.save()
	return	HttpResponseRedirect(reverse('AddCertifiableTransactions'))


def AddCertificationOfficers(request):
	officers = CertificationOfficers.objects.all()
	title="Manage Certification Officers"
	title1="Certification Officer"
	form = CertificationOfficers_form(request.POST or None)

	if request.method ==  "POST":
		status=MembershipStatus.objects.get(title="ACTIVE")
		form = CertificationOfficers_form(request.POST or None)
		if form.is_valid():
			officer_id=form.cleaned_data['officers']
			officer = CustomUser.objects.get(id=officer_id)

			transaction_id=form.cleaned_data["transaction"]
			transaction = CertifiableTransactions.objects.get(id=transaction_id)
			
			record=CertificationOfficers(officer=officer,transaction=transaction,status=status)
			record.save()
			messages.success(request,"Record Updated Successfully")
			return	HttpResponseRedirect(reverse('AddCertificationOfficers'))
	context={
	'form':form,
	'officers':officers,
	'url':'AddCertificationOfficers',
	'button_text':"Add Record",
	'title':title,
	'title1':title1,
	}
	return render(request,'master_templates/CertificationOfficers.html', context)



def CertificationOfficersUpdate(request,pk):
	status1=MembershipStatus.objects.get(title="ACTIVE")
	status2=MembershipStatus.objects.get(title="INACTIVE")
	record=CertificationOfficers.objects.get(id=pk)
	
	if record.status==status1:
		record.status=status2
	elif record.status==status2:
		record.status=status1

	record.save()
	return	HttpResponseRedirect(reverse('AddCertificationOfficers'))


def AddDisbursementOfficers(request):
    officers = DisbursementOfficers.objects.all()
    title="Manage Disbursement Officers"
    title1="Disbursement Officer"
    form = DisbursementOfficers_form(request.POST or None)

    if request.method ==  "POST":
        status=MembershipStatus.objects.get(title="ACTIVE")
        form = DisbursementOfficers_form(request.POST or None)
        if form.is_valid():
            officer_id=form.cleaned_data['officers']
            officer = CustomUser.objects.get(id=officer_id)
            
            record=DisbursementOfficers(officer=officer,status=status)
            record.save()
            messages.success(request,"Record Updated Successfully")
            return  HttpResponseRedirect(reverse('AddDisbursementOfficers'))
    context={
    'form':form,
    'officers':officers,
    'url':'AddDisbursementOfficers',
    'button_text':"Add Record",
    'title':title,
    'title1':title1,
    }
    return render(request,'master_templates/DisbursementOfficers.html', context)


def DisbursementOfficersUpdate(request,pk):
    status1=MembershipStatus.objects.get(title="ACTIVE")
    status2=MembershipStatus.objects.get(title="INACTIVE")
    record=DisbursementOfficers.objects.get(id=pk)
    
    if record.status==status1:
        record.status=status2
    elif record.status==status2:
        record.status=status1

    record.save()
    return  HttpResponseRedirect(reverse('AddDisbursementOfficers'))


def membership_price_settings_load(request):
	transaction=TransactionTypes.objects.get(code='100')
	title="Membership Registration"
	title1="Membership Registration Charges"

	form=membership_price_settings_form(request.POST or None)
	form.fields['admin_charges'].initial=transaction.admin_charges
	if request.method ==  "POST":
		
		form = membership_price_settings_form(request.POST)
		if form.is_valid():
			# transaction=TransactionTypes.objects.get(id=pk)
			admin_charges=form.cleaned_data['admin_charges']
			transaction.admin_charges=admin_charges
			transaction.save()
			messages.success(request,"Record Updated Successfully")
			return	HttpResponseRedirect(reverse('membership_price_settings_load'))
	
	context={
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
    'record':record,
    }
    return render(request,'master_templates/AutoReceipt_Setup.html',context)



def receipt_manager(request):
	form = receipt_manager_form(request.POST or None)
	receipts=Receipts.objects.all()
	if request.method=="POST":
		start_point = request.POST.get('start_point')
		stop_point = request.POST.get('stop_point')
		
		for i in  range(int(start_point),int(stop_point)+1): 
			record=Receipts(receipt=str(i).zfill(5))
			record.save()
		return HttpResponseRedirect(reverse('receipt_manager'))
	context={
	'form':form,
	'receipts':receipts,
	}
	return render(request,'master_templates/receipt_manager.html',context)


def receipt_manager_shop(request):
    form = receipt_manager_form(request.POST or None)
    receipts=Receipts_Shop.objects.all()
    if request.method=="POST":
        start_point = request.POST.get('start_point')
        stop_point = request.POST.get('stop_point')
        
        for i in  range(int(start_point),int(stop_point)+1): 
            record=Receipts_Shop(receipt=str(i).zfill(5))
            record.save()
        return HttpResponseRedirect(reverse('receipt_manager_shop'))
    context={
    'form':form,
    'receipts':receipts,
    }
    return render(request,'master_templates/receipt_manager_shop.html',context)


def Members_IdManager(request):
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
	'form':form,
	}
	return render(request,'master_templates/MembersIdManager.html',context)


def SharesUnits_add(request):
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
    'items':items,
    }
    return render(request,'master_templates/SharesUnits_add.html',context)


def Loan_Number_Manager(request):
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
    'form':form,
    }
    return render(request,'master_templates/Loan_Number_Manager.html',context)

#######################################################################
################## COOPERATIVE ACCOUNTS ################################
#######################################################################
def CooperativeBankAccounts_add(request):
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
    'form':form,
    'banks':banks,
    }
    return render(request,'master_templates/CooperativeBankAccounts_add.html',context)


def CooperativeBankAccounts_Remove(request,pk):
    record=CooperativeBankAccounts.objects.get(id=pk)
    record.delete()
    return HttpResponseRedirect(reverse('CooperativeBankAccounts_add'))


def CooperativeBankAccounts_Update(request,pk):
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
    'form':form,
    }
    return render(request,'master_templates/CooperativeBankAccounts_Update.html',context)

#######################################################################
################## WITHDRAWAL CONTROLLER ##############################
#######################################################################



def WithdrawalController_add(request):
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
    'form':form,
    }
    return render(request,'master_templates/WithdrawalController_add.html',context)


def WithdrawalController(request):
    transactions=WithdrawableTransactions.objects.all()
    context={
    'transactions':transactions,
    }
    return render(request,'master_templates/WithdrawalController.html',context)


def WithdrawalController_View(request,pk):
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
    'form':form,
    }
    return render(request,'master_templates/CustomerID_Manager.html',context)



#######################################################################
################## GENERAL REPORT #####################################
#######################################################################

def transaction_views_ranked(request):
    transactions=TransactionTypes.objects.filter(~Q(source__title='GENERAl')).order_by('rank')
    context={
    'transactions':transactions,

    }
    return render(request,'master_templates/reports/transaction_views_ranked.html',context)


def List_of_Users(request):
    users=Staff.objects.all()
    records=UserType.objects.all().order_by('code')
    # users=Staff.objects.annotate(full_name=Concat("admin__first_name", Value(" "), "admin__last_name")).all().values_lst("full_name")
    print(users)
    context={
    'users':users,
    'records':records,
    }
    return render(request,'master_templates/List_of_Users.html',context)