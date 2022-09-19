# Create your models here.
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.validators import MaxValueValidator, MinValueValidator
from django.utils import timezone

# models.PositiveSmallIntegerField(validators=[MinValueValidator(1)])




# Create your models here.
TRANSACTION_STATUS=(
    ('UNTREATED','UNTREATED'),
    ("TREATED","TREATED"),
    ("ARCHIVED","ARCHIVED"),
    )

MANUAL_POSTING_TYPES=(
    ('CREDIT','CREDIT'),
    ("DEBIT","DEBIT")
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
        ('PENDING',"PENDING"),
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
        ('NONE','NONE'),
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
    ("NONE","NONE"),
    ("CASH","CASH"),
    ("PERCENTAGE","PERCENTAGE")
    )
LOAN_PATH=(
        ('NONE','NONE'),
        ('PROJECT','PROJECT'),
        ('EMERGENCY','EMERGENCY')
        )

INTEREST_DEDUCTION=(
                    ("NONE","NONE"),
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

PENALTY_STATUS=(
        ("NORMAL","NORMAL"),
        ("DEFAULTED","DEFAULTED")
        )
LOAN_CATEGORY=(
            ("NONE","NONE"),
            ("MONETARY","MONETARY"),
            ("NON-MONETARY","NON-MONETARY")
            )
class CustomUser(AbstractUser):
    user_type_data=((1,"MASTER"),(2,"EXECUTIVE") ,(3,"DESKOFFICE"),(4,"SHOP"),(5,"MEMBERS"))
    user_type=models.CharField(default=1,choices=user_type_data,max_length=15)

    # class Meta:
    #   db_table="customuser"

class AdminMASTER(models.Model):
    id=models.AutoField(primary_key=True)
    admin=models.OneToOneField(CustomUser,on_delete=models.CASCADE,blank=True,null=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    objects=models.Manager()

    # class Meta:
    #   db_table="admin_master"

class titleBase(models.Model):
    id=models.AutoField(primary_key=True)
    title= models.CharField(max_length=255,unique=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    objects=models.Manager()

    class Meta:
        abstract = True


class UserType(titleBase):
    code=models.CharField(max_length=2,unique=True)

    # class Meta:
    #     db_table = "usertype"


    def __str__(self):
        return self.title




###########################################################
############# Status ######################################
###########################################################


class ExpiringDateInterval(titleBase):
    class Meta(titleBase.Meta):
        # db_table="CooperativeOperations"
        ordering = ['id']

    def __str__(self):
        return self.title

class CooperativeOperations(titleBase):
    class Meta(titleBase.Meta):
        # db_table="CooperativeOperations"
        ordering = ['id']

    def __str__(self):
        return self.title


class Commodity_Period(titleBase):
    class Meta(titleBase.Meta):
        # db_table="Commodity_Period"
        ordering = ['id']

    def __str__(self):
        return self.title

class Commodity_Period_Batch(titleBase):
    title=models.CharField(max_length=255)

    def __str__(self):
        return self.title

class Termination_Types(titleBase):
    duration= models.PositiveSmallIntegerField(validators=[MinValueValidator(0)],default=0)
    class Meta(titleBase.Meta):
        # db_table="termination_types"
        ordering = ['id']

    def __str__(self):
        return self.title

class MonthlyDeductionGenerationHeaders(titleBase):

    class Meta(titleBase.Meta):
        # db_table="monthly_deduction_generation_headers"
        ordering = ['title']

    def __str__(self):
        return self.title


class ItemWriteOffReasons(titleBase):

    class Meta(titleBase.Meta):
        # db_table="item_write_off_reasons"
        ordering = ['title']

    def __str__(self):
        return self.title



class Titles(titleBase):
    class Meta(titleBase.Meta):
        # db_table="Titles"
        ordering = ['title']


    def __str__(self):
        return self.title


class Gender(titleBase):
    class Meta(titleBase.Meta):
        # db_table="Gender"
        ordering = ['title']


    def __str__(self):
        return self.title


class Banks(titleBase):
    class Meta(titleBase.Meta):
        # db_table="Banks"
        ordering = ['title']


    def __str__(self):
        return self.title


class Locations(titleBase):
    class Meta(titleBase.Meta):
        # db_table='Locations'
        ordering = ['title']


    def __str__(self):
        return self.title

class Departments(titleBase):
    class Meta(titleBase.Meta):
        # db_table="Departments"
        ordering = ['title']


    def __str__(self):
        return self.title


class SalaryInstitution(titleBase):
    rank=models.IntegerField(default=0)
    class Meta(titleBase.Meta):
        # db_table="Salary_Institution"
        ordering = ['title']


    def __str__(self):
        return self.title



class TransactionSources(titleBase):
    maximum_amount = models.DecimalField(max_digits=20,decimal_places = 2,default=0)
    salary_loan_relationship= models.IntegerField(default=0)
    loan_based_saving=models.IntegerField(default=0)

    class Meta(titleBase.Meta):
        # db_table="Transaction_Sources"
        ordering = ['title']


    def __str__(self):
        return self.title

class States(titleBase):
    class Meta(titleBase.Meta):
        # db_table="States"
        ordering = ['title']


    def __str__(self):
        return self.title


class NOKRelationships(titleBase):
    class Meta(titleBase.Meta):
        # db_table="NOK_Relationships"
        ordering = ['title']

    def __str__(self):
        return self.title

class ProductCategory(titleBase):
    code= models.CharField(max_length=255,unique=True)
    class Meta(titleBase.Meta):
        # db_table="Product_Category"
        ordering = ['title']


    def __str__(self):
        return self.title


class DefaultPassword(titleBase):
    title= models.CharField(max_length=255,unique=True,verbose_name="Password")

    # class Meta:
    #     db_table="Default_Password"

    def __str__(self):
        return self.title

class ExceptableCriterias(titleBase):
    title=models.CharField(max_length=255)

    # class Meta:
    #     db_table="ExceptableCriterias"

    def __str__(self):
        return self.title


class TransactionEnabler(titleBase):
    status = models.CharField(max_length=20,choices=YESNO,default='NO')

    class Meta(titleBase.Meta):
        # db_table="Transaction_Sources"
        ordering = ['title']


    def __str__(self):
        return self.title


class DateObjectsModels(models.Model):
    id=models.AutoField(primary_key=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    processed_by=models.CharField(max_length=100,default='ADMIN')
    tdate = models.DateField(default=timezone.now)

    objects=models.Manager()

    class Meta:
        abstract=True

class FailedLoanPenalty(DateObjectsModels):
    code = models.DecimalField(max_digits=20,decimal_places = 2)
    class Meta(DateObjectsModels.Meta):
        # db_table="FailedLoanPenalty"
        ordering = ['id']

    def __str__(self):
        return self.code

class FailedLoanPenaltyEnabler(DateObjectsModels):
    status = models.CharField(max_length=20,choices=YESNO,default='NO')
    class Meta(DateObjectsModels.Meta):
        # db_table="FailedLoanPenaltyEnabler"
        ordering = ['id']

    def __str__(self):
        return self.status


class FailedLoanPenaltyDuration(DateObjectsModels):
    duration = models.DecimalField(max_digits=20,decimal_places = 2)
    class Meta(DateObjectsModels.Meta):
        # db_table="FailedLoanPenaltyDuration"
        ordering = ['id']

    def __str__(self):
        return self.duration



class System_Users_Tasks(DateObjectsModels):
    title=models.CharField(max_length=255)
    rank=models.IntegerField(default=0)
    usertype=models.ForeignKey(UserType,on_delete=models.CASCADE)


class System_Users_Tasks_Model(DateObjectsModels):
    task=models.ForeignKey(System_Users_Tasks,on_delete=models.CASCADE)
    user=models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    status = models.BooleanField(default=False)


class CustomerID(DateObjectsModels):
    title=models.CharField(max_length=255,unique=True)

    # class Meta(DateObjectsModels.Meta):
    #     db_table="customer_Id"

class TransactionPeriods(DateObjectsModels):
    transaction_period=models.DateField()
    status= models.CharField(max_length=20,choices=MEMBERSHIP_STATUS,default='ACTIVE')

    # class Meta(DateObjectsModels.Meta):
    #     db_table="Transaction_Periods"

class AdjustmentPeriods(DateObjectsModels):
    transaction_period=models.DateField()
    status= models.CharField(max_length=20,choices=MEMBERSHIP_STATUS,default='ACTIVE')

    # class Meta(DateObjectsModels.Meta):
    #     db_table="AdjustmentPeriods"



class InvoiceHeader(DateObjectsModels):
    title= models.CharField(max_length=255)
    address1= models.CharField(max_length=255)
    address2= models.CharField(max_length=255)
    phone_no= models.CharField(max_length=255)

    # class Meta(DateObjectsModels.Meta):
    #     db_table="Invoice_Header"


class AutoReceipt(DateObjectsModels):
    receipt= models.CharField(max_length=255)

    # class Meta(DateObjectsModels.Meta):
    #     db_table="Auto_Receipt"

class LoanNumber(DateObjectsModels):
    code= models.IntegerField(unique=True)

    # class Meta(DateObjectsModels.Meta):
    #     db_table="Loan_Number"

class Receipts(DateObjectsModels):
    id=models.AutoField(primary_key=True)
    receipt= models.CharField(max_length=255,unique=True)
    status = models.CharField(max_length=30,choices=RECEIPT_STATUS,default="UNUSED")


    # class Meta(DateObjectsModels.Meta):
    #     db_table="Receipts"

class Receipts_Shop(DateObjectsModels):
    id=models.AutoField(primary_key=True)
    receipt= models.CharField(max_length=255,unique=True)
    status = models.CharField(max_length=30,choices=RECEIPT_STATUS,default="UNUSED")


    # class Meta(DateObjectsModels.Meta):
    #     db_table="Receipts_Shop"


class FormAutoPrints(DateObjectsModels):
    id=models.AutoField(primary_key=True)
    title= models.CharField(max_length=255,unique=True)
    status = models.CharField(max_length=20,choices=YESNO,default='NO')

    # class Meta(DateObjectsModels.Meta):
    #     db_table="form_auto_prints"


class Receipt_Cancelled(DateObjectsModels):
    receipt = models.ForeignKey(Receipts,on_delete=models.CASCADE,blank=True,null=True)
    reasons= models.TextField()


    # class Meta(DateObjectsModels.Meta):
    #     db_table="Receipt_Cancelled"


class SharesUnits(DateObjectsModels):
    unit= models.IntegerField(unique=True)

    # class Meta(DateObjectsModels.Meta):
    #     db_table="Shares_Units"


class MembersIdManager(DateObjectsModels):
    prefix_title= models.CharField(max_length=255)
    prefix_year= models.CharField(max_length=255)
    member_id= models.IntegerField(unique=True)

    # class Meta(DateObjectsModels.Meta):
    #     db_table="Members_Id_Manager"



class CooperativeBankAccounts(DateObjectsModels):
    bank=models.ForeignKey(Banks,on_delete=models.CASCADE)
    account_name=models.CharField(max_length=255)
    account_type=models.CharField(max_length=20,choices=ACCOUNT_TYPES,default='SAVINGS')
    account_number=models.CharField(max_length=255)
    sort_code=models.CharField(max_length=255, blank=True,null=True)

    # class Meta(DateObjectsModels.Meta):
    #     db_table="Cooperative_Bank_Accounts"

class CooperativeBankAccountsDesignationHeaders(DateObjectsModels):
    title=models.CharField(max_length=255)


    # class Meta(DateObjectsModels.Meta):
    #     db_table="CooperativeBankAccountsDesignationHeaders"


class CooperativeBankAccountsOperationalDesignations(DateObjectsModels):
    account=models.ForeignKey(CooperativeBankAccounts,on_delete=models.CASCADE)
    transaction=models.ForeignKey(CooperativeBankAccountsDesignationHeaders,on_delete=models.CASCADE)
    status=models.CharField(max_length=20,choices=MEMBERSHIP_STATUS,default='ACTIVE')



    # class Meta(DateObjectsModels.Meta):
    #     db_table="CooperativeBankAccountsOperationalDesignations"


class AccountsSignatories(DateObjectsModels):
    bank=models.ForeignKey(CooperativeBankAccounts,on_delete=models.CASCADE)
    name=models.CharField(max_length=255)
    position=models.CharField(max_length=20,choices=ACCOUNT_TYPES,default='SAVINGS')

    # class Meta(DateObjectsModels.Meta):
    #     db_table="AccountsSignatories"


class Lga(DateObjectsModels):
    title= models.CharField(max_length=255,blank=True,null=True)
    state=models.ForeignKey(States,on_delete=models.CASCADE)

    # class Meta(DateObjectsModels.Meta):
    #     db_table="Lga"


class Staff(DateObjectsModels):
    admin=models.OneToOneField(CustomUser,on_delete=models.CASCADE,blank=True,null=True)
    title=models.ForeignKey(Titles,on_delete=models.CASCADE,blank=True,null=True)
    middle_name=models.CharField(max_length=50)
    address=models.TextField()
    phone_number=models.CharField(max_length=50)
    gender =models.ForeignKey(Gender,on_delete=models.CASCADE,blank=True,null=True)
    status= models.CharField(max_length=20,choices=MEMBERSHIP_STATUS,default='ACTIVE')
    default_password=models.CharField(max_length=10,choices=YESNO,default='YES')


    # @property
    # def get_full_name(self):
    #     if self.middle_name:
    #           return self.admin.last_name + " " + self.admin.first_name + " " + self.middle_name
    #     else:
    #           return self.admin.last_name + " " + self.admin.first_name


    # class Meta(DateObjectsModels.Meta):
    #     db_table="Staff"


class TransactionTypes(DateObjectsModels):
    LOAN_PATH=(
        ('NONE','NONE'),
        ('PROJECT','PROJECT'),
        ('EMERGENCY','EMERGENCY')
        )
    source = models.ForeignKey(TransactionSources,on_delete=models.CASCADE)
    category = models.CharField(max_length=20,choices=LOAN_CATEGORY,blank=True,null=True)
    code=models.CharField(max_length=50,unique=True)
    name=models.CharField(max_length=50,unique=True)
    maximum_amount = models.DecimalField(max_digits=20,decimal_places=2,default=0)
    minimum_amount = models.DecimalField(max_digits=20,decimal_places=2,default=0)
    duration= models.PositiveSmallIntegerField(validators=[MinValueValidator(0)],default=0)
    interest_deduction=  models.CharField(max_length=30,choices=INTEREST_DEDUCTION,blank=True,null=True)
    interest_rate= models.DecimalField(max_digits=20,decimal_places = 2,default=0)
    rank= models.IntegerField(unique=False,default=0)
    admin_charges_rating= models.CharField(max_length=30,choices=ADMIN_CHARGES,blank=True,null=True)
    admin_charges = models.DecimalField(max_digits=20,decimal_places = 2,blank=True,null=True)
    admin_charges_minimum= models.DecimalField(max_digits=20,decimal_places = 2,blank=True,null=True)
    default_admin_charges= models.DecimalField(max_digits=20,decimal_places = 2,default=0)
    salary_loan_relationship= models.DecimalField(max_digits=20,decimal_places = 2,default=0)
    saving_rating= models.DecimalField(max_digits=20,decimal_places = 2,default=0)
    savings_rate=models.CharField(default='NO',choices=YESNO,max_length=15)
    guarantors= models.IntegerField(default=0)
    guarantors_gross_pay_rating= models.DecimalField(max_digits=20,decimal_places = 2,default=0)
    loan_age= models.DecimalField(max_digits=20,decimal_places = 2,default=0)
    share_unit_min= models.DecimalField(max_digits=20,decimal_places = 2,default=0)
    share_unit_max= models.DecimalField(max_digits=20,decimal_places = 2,default=0)
    receipt_type= models.CharField(max_length=30,choices=RECEIPT_TYPES,default='NONE')
    status= models.CharField(max_length=20,choices=MEMBERSHIP_STATUS,default='ACTIVE')
    multiple_loan_status= models.CharField(max_length=20,choices=MULTIPLE_LOAN_STATUS,default='NOT ALLOWED')
    auto_stop_savings= models.CharField(default='NO',choices=YESNO,max_length=15)
    form_print=models.CharField(max_length=20,choices=YESNO,default='NO')
    loan_path=models.CharField(max_length=20,choices=LOAN_PATH,default='NONE')
    transfer_enabled=models.CharField(default='NO',choices=YESNO,max_length=15)


    # class Meta(DateObjectsModels.Meta):
    #     db_table="Transaction_Types"

class XmasSavingsTransactionPeriod(DateObjectsModels):
    batch=models.CharField(max_length=100)
    status=models.CharField(max_length=20,choices=MEMBERSHIP_STATUS,default='ACTIVE')

    class Meta(DateObjectsModels.Meta):
        db_table="XmasSavingsTransactionPeriod"


class XmasTransferDefaultSaving(DateObjectsModels):
    transaction=models.ForeignKey(TransactionTypes,on_delete=models.CASCADE)

    # class Meta(DateObjectsModels.Meta):
    #     db_table="XmasTransferDefaultSaving"



class  CompulsorySavings(DateObjectsModels):
    transaction=models.ForeignKey(TransactionTypes,on_delete=models.CASCADE,blank=True,null=True)

    # class Meta(DateObjectsModels.Meta):
    #     db_table="Compulsory_Savings"


class  WithdrawableTransactions(DateObjectsModels):
    transaction=models.ForeignKey(TransactionTypes,on_delete=models.CASCADE)
    status= models.CharField(max_length=20,choices=WITHDRAWAL_STATUS,default='LOCKED')
    maturity= models.IntegerField(default=0)


    # class Meta(DateObjectsModels.Meta):
    #     db_table="Withdrawable_Transactions"

class  LoanBasedSavings(DateObjectsModels):
    savings=models.ForeignKey(TransactionTypes,on_delete=models.CASCADE)


    # class Meta(DateObjectsModels.Meta):
    #     db_table="Loanbased_Savings"


class MemberShipRequest(DateObjectsModels):
    title=models.ForeignKey(Titles,on_delete=models.CASCADE,blank=True,null=True)
    first_name=models.CharField(max_length=255)
    last_name=models.CharField(max_length=255)
    middle_name=models.CharField(max_length=255,blank=True,null=True)
    gender = models.ForeignKey(Gender,on_delete=models.CASCADE,blank=True,null=True)
    phone_number=models.CharField(max_length=255)
    department=models.ForeignKey(Departments,on_delete=models.CASCADE,blank=True,null=True)
    approval_officer=models.CharField(max_length=255,blank=True,null=True)
    approval_status = models.CharField(max_length=30,choices=APPROVAL_STATUS,default='PENDING')
    approval_comment=models.TextField(blank=True,null=True)
    approved_date=models.DateField(blank=True,null=True)
    transaction_status= models.CharField(max_length=20,choices=TRANSACTION_STATUS,default='UNTREATED')
    submission_status=  models.CharField(max_length=30,choices=SUBMISSION_STATUS,default='NOT SUBMITTED')
    salary_institution=models.ForeignKey(SalaryInstitution,on_delete=models.CASCADE,blank=True,null=True)
    file_no=models.CharField(max_length=255,blank=True,null=True)
    ippis_no=models.CharField(max_length=255,blank=True,null=True)
    month=models.CharField(max_length=255,blank=True,null=True)
    year=models.CharField(max_length=255,blank=True,null=True)
    member_id=models.CharField(max_length=255,blank=True,null=True)
    date_of_first_appointment=models.DateField(blank=True,null=True)
    dob=models.DateField(blank=True,null=True)
    next_of_kin=models.CharField(max_length=255,blank=True,null=True)
    date_applied=models.DateField(blank=True,null=True)


    # class Meta(DateObjectsModels.Meta):
    #     db_table="Membership_Request"


    def __str__(self):
        return '{} {} {}'.format(self.last_name, self.first_name, self.admin.middle_name)

    @property
    def get_middle_name(self):
        if self.middle_name:
            return self.middle_name
        else:
            return ""

    @property
    def get_full_name(self):
        if self.middle_name:
            return self.last_name + " " + self.first_name + " " + self.middle_name
        else:
            return self.last_name + " " + self.first_name


class MemberShipRequestAdditionalInfo(DateObjectsModels):
    applicant=models.ForeignKey(MemberShipRequest,on_delete=models.CASCADE,blank=True,null=True)
    comment=models.TextField(blank=True,null=True)
    officer=models.ForeignKey(CustomUser,on_delete=models.CASCADE,blank=True,null=True)

    # class Meta(DateObjectsModels.Meta):
    #     db_table="MemberShip_Request_Additional_Info"


class MemberShipRequestAdditionalAttachment(DateObjectsModels):
    applicant=models.ForeignKey(MemberShipRequest,on_delete=models.CASCADE)
    caption=models.CharField(max_length=255)
    image=models.FileField(blank=True,null=True)
    officer=models.ForeignKey(CustomUser,on_delete=models.CASCADE)


    # class Meta(DateObjectsModels.Meta):
    #     db_table="Membership_Request_Additional_Attachment"

class MemberShipFormSalesRecord(DateObjectsModels):
    applicant=models.ForeignKey(MemberShipRequest,on_delete=models.CASCADE)
    payment_reference=models.CharField(max_length=255,blank=True,null=True)
    receipt=models.CharField(max_length=255,unique=True)
    admin_charge = models.DecimalField(max_digits=20,decimal_places = 2,blank=True,null=True)
    shares=models.IntegerField(default=0)
    share_amount = models.DecimalField(max_digits=20,decimal_places = 2,blank=True,null=True)
    welfare_amount = models.DecimalField(max_digits=20,decimal_places = 2,blank=True,null=True)
    total_amount = models.DecimalField(max_digits=20,decimal_places = 2,blank=True,null=True)
    bank_ccount= models.ForeignKey(CooperativeBankAccounts,on_delete=models.CASCADE,blank=True,null=True)
    image=models.FileField(blank=True,null=True)
    status= models.CharField(max_length=20,choices=TRANSACTION_STATUS,default='UNTREATED')
    cashbook_status=models.CharField(max_length=30,choices=CASHBOOK_STATUS,default='UNPOSTED')
    new_registration=models.BooleanField(default=False)
    date_paid=models.DateField()


    # class Meta(DateObjectsModels.Meta):
    #     db_table="Membership_Form_Sales_Record"


class Members(DateObjectsModels):
    CHOICES=(
        ('OLD','OLD'),
        ('NEW','NEW')
        )

    admin=models.OneToOneField(CustomUser,on_delete=models.CASCADE)
    applicant=models.ForeignKey(MemberShipFormSalesRecord,on_delete=models.CASCADE,blank=True,null=True)
    member_id = models.CharField(max_length=255, blank=True,null=True)
    coop_no = models.CharField(max_length=15,unique=True, default='00001')
    title=models.ForeignKey(Titles,on_delete=models.CASCADE,blank=True,null=True)
    middle_name=models.CharField(max_length=255,blank=True,null=True)
    full_name=models.CharField(max_length=255,blank=True,null=True)
    gender = models.ForeignKey(Gender,on_delete=models.CASCADE,blank=True,null=True)
    phone_number=models.CharField(max_length=255,blank=True,null=True)
    profile_pic=models.FileField(blank=True,null=True)
    residential_address=models.TextField(blank=True,null=True)
    permanent_home_address=models.TextField(blank=True,null=True)
    department=models.ForeignKey(Departments,on_delete=models.CASCADE,blank=True,null=True)
    state=models.ForeignKey(States, on_delete=models.CASCADE,blank=True,null=True)
    lga=models.ForeignKey(Lga, on_delete=models.CASCADE,blank=True,null=True)
    salary_institution=models.ForeignKey(SalaryInstitution,on_delete=models.CASCADE,blank=True,null=True)
    file_no=models.CharField(max_length=255,blank=True,null=True)
    ippis_no=models.CharField(max_length=255,unique=True)
    last_used_net_pay=models.DecimalField(max_digits=20,decimal_places = 2,default=0)
    net_pay_as_at=models.DateField(blank=True,null=True)
    shares=models.IntegerField(default=0)
    date_joined=models.DateField(blank=True,null=True)
    dob=models.DateField(blank=True,null=True)
    date_of_first_appointment=models.DateField(blank=True,null=True)
    status= models.CharField(max_length=30,choices=MEMBERSHIP_STATUS,default="ACTIVE")
    savings_status= models.CharField(max_length=30,choices=UPLOAD_STATUS,default='PENDING')
    loan_status= models.CharField(max_length=30,choices=UPLOAD_STATUS,default='PENDING')
    shares_status= models.CharField(max_length=30,choices=UPLOAD_STATUS,default='PENDING')
    welfare_status= models.CharField(max_length=30,choices=UPLOAD_STATUS,default='PENDING')
    date_joined_status= models.CharField(max_length=30,choices=UPLOAD_STATUS,default='PENDING')
    date_of_first_appointment_status= models.CharField(max_length=30,choices=UPLOAD_STATUS,default='PENDING')
    dob_status= models.CharField(max_length=30,choices=UPLOAD_STATUS,default='PENDING')
    member_category=models.CharField(default='OLD',choices=CHOICES,max_length=15)



    def __str__(self):
        return '{} {} {}'.format(self.admin.last_name, self.admin.first_name, self.admin.middle_name)

    @property
    def get_middle_name(self):
        if self.middle_name:
            return self.middle_name
        else:
            return ""

    @property
    def get_full_name(self):
        if self.middle_name:
            return self.admin.last_name + " " + self.admin.first_name + " " + self.middle_name
        else:
            return self.admin.last_name + " " + self.admin.first_name


    @property
    def get_department(self):
        if self.department:
            return self.department
        else:
            return ""


    @property
    def get_member_Id(self):
        if self.member_id:
            return self.member_id[13:]
        else:
            return ""


class Event_Title(DateObjectsModels):
    title=models.CharField(max_length=255)
    pdate=models.DateField()
    status= models.CharField(max_length=20,choices=TRANSACTION_STATUS,default='UNTREATED')

    # class Meta(DateObjectsModels.Meta):
    #     db_table="Event_Title"


class Events(DateObjectsModels):
    PARTICIPANT = (
                ('MEMBER','MEMBER'),
                ('NON MEMBER','NON MEMBER'),
                )
    title=models.ForeignKey(Event_Title,on_delete=models.CASCADE)
    participant_id=models.CharField(max_length=255)
    name=models.CharField(max_length=255)
    phone_no=models.CharField(max_length=255)
    participant=models.CharField(max_length=20,choices=PARTICIPANT,default='MEMBER')
    status= models.CharField(max_length=20,choices=TRANSACTION_STATUS,default='UNTREATED')

    # class Meta(DateObjectsModels.Meta):
    #     db_table="Events"


class MembersBankAccounts(DateObjectsModels):
    member_id=models.ForeignKey(Members,on_delete=models.CASCADE)
    bank=models.ForeignKey(Banks,on_delete=models.CASCADE)
    account_name=models.CharField(max_length=255)
    account_number=models.CharField(max_length=255)
    account_type=models.CharField(max_length=20,choices=ACCOUNT_TYPES,default='SAVINGS')
    status= models.CharField(max_length=20,choices=MEMBERSHIP_STATUS,default='ACTIVE')
    account_priority=models.PositiveSmallIntegerField(validators=[MinValueValidator(0)],default=1)
    lock_status= models.CharField(max_length=20,choices=LOCK_STATUS,default='LOCKED')

    # class Meta(DateObjectsModels.Meta):
    #     db_table="Members_Bank_Accounts"

class ExecutivePositions(DateObjectsModels):
    title=models.CharField(max_length=255)

    # class Meta(DateObjectsModels.Meta):
    #     db_table="ExecutivePositions"

class Executives(DateObjectsModels):
    member=models.ForeignKey(Members,on_delete=models.CASCADE)
    name=models.CharField(max_length=255)
    position=models.ForeignKey(ExecutivePositions,on_delete=models.CASCADE)
    start_date=models.DateField()
    stop_date=models.DateField(blank=True, null=True)
    status=models.CharField(max_length=20, choices=MEMBERSHIP_STATUS,default='INACTIVE')

    # class Meta(DateObjectsModels.Meta):
    #     db_table="Executives"


class Termination_Loan_Allowed(DateObjectsModels):
    termination=models.ForeignKey(Termination_Types,on_delete=models.CASCADE)


    # class Meta(DateObjectsModels.Meta):
    #     db_table="Termination_Loan_Allowed"



class Member_Salary_Adjustment(DateObjectsModels):
    member= models.ForeignKey(Members,on_delete=models.CASCADE)
    existing_gross_pay=models.DecimalField(max_digits=20,decimal_places = 2,default=0)
    current_gross_pay=models.DecimalField(max_digits=20,decimal_places = 2,default=0)
    period=models.DateField(blank=True,null=True)
    image=models.FileField(blank=True,null=True)
    approval_officer=models.CharField(max_length=100,blank=True,null=True)
    approval_comment=models.TextField(blank=True,null=True)
    approval_status= models.CharField(max_length=30,choices=APPROVAL_STATUS,default='PENDING')
    approved_at=models.DateField(blank=True,null=True)
    status= models.CharField(max_length=20,choices=TRANSACTION_STATUS,default='UNTREATED')



class MemberShipTerminationRequest(DateObjectsModels):
    member= models.OneToOneField(Members,on_delete=models.CASCADE)
    termination=models.ForeignKey(Termination_Types,on_delete=models.CASCADE)
    loan_amount=models.DecimalField(max_digits=20,decimal_places = 2)
    maturity_date=models.DateField(blank=True,null=True)
    comment=models.TextField(blank=True,null=True)
    applied_date=models.DateField()
    approval_officer=models.CharField(max_length=255,blank=True,null=True)
    approval_comment=models.TextField(blank=True,null=True)
    approval_status= models.CharField(max_length=30,choices=APPROVAL_STATUS,default='PENDING')
    approved_at=models.DateField(blank=True,null=True)
    status= models.CharField(max_length=20,choices=TRANSACTION_STATUS,default='UNTREATED')
    processing_status=models.CharField(max_length=20,choices=PROCESSING_STATUS,default='UNPROCESSED')

    # class Meta(DateObjectsModels.Meta):
    #     db_table="member_ship_termination_request"


class MemberShipTerminationTransactionBalances(DateObjectsModels):
    applicant= models.ForeignKey(MemberShipTerminationRequest,on_delete=models.CASCADE)
    transaction= models.ForeignKey(TransactionTypes,on_delete=models.CASCADE)
    account_number=models.CharField(max_length=255,blank=True,null=True)
    debit=models.DecimalField(max_digits=20,decimal_places = 2)
    credit=models.DecimalField(max_digits=20,decimal_places = 2)
    status= models.CharField(max_length=20,choices=TRANSACTION_STATUS,default='UNTREATED')


    # class Meta(DateObjectsModels.Meta):
    #     db_table="MemberShipTerminationTransactionBalances"

class MemberShipTermination(DateObjectsModels):
    applicant= models.ForeignKey(MemberShipTerminationRequest,on_delete=models.CASCADE)
    amount=models.DecimalField(max_digits=20,decimal_places = 2)
    approval_officer=models.CharField(max_length=255,blank=True,null=True)
    approval_comment=models.TextField(blank=True,null=True)
    approval_status= models.CharField(max_length=30,choices=APPROVAL_STATUS,default='PENDING')
    approved_at=models.DateField(blank=True,null=True)
    processing_status=models.CharField(max_length=20,choices=PROCESSING_STATUS,default='UNPROCESSED')
    lock_status=models.CharField(max_length=20,choices=LOCK_STATUS,default='LOCKED')
    status= models.CharField(max_length=20,choices=TRANSACTION_STATUS,default='UNTREATED')


    # class Meta(DateObjectsModels.Meta):
    #     db_table="MemberShipTermination"


class MemberShipTerminationRequestException(DateObjectsModels):
    applicant= models.ForeignKey(MemberShipTermination,on_delete=models.CASCADE)
    reasons=models.TextField(blank=True,null=True)
    approval_officer=models.CharField(max_length=255,blank=True,null=True)
    approval_comment=models.TextField(blank=True,null=True)
    approval_status= models.CharField(max_length=30,choices=APPROVAL_STATUS,default='PENDING')
    approved_at=models.DateField(blank=True,null=True)
    status= models.CharField(max_length=20,choices=TRANSACTION_STATUS,default='UNTREATED')


    # class Meta(DateObjectsModels.Meta):
    #     db_table="MemberShipTerminationRequestException"


class MemberShipTerminationFundDisbursement(DateObjectsModels):
    member= models.ForeignKey(MemberShipTermination,on_delete=models.CASCADE)
    amount=models.DecimalField(max_digits=20,decimal_places = 2)
    pv_number=models.CharField(max_length=255)
    pv_date=models.DateField(blank=True,null=True)
    payment_channel=models.CharField(max_length=30,choices=PAYMENT_CHANNEL,default='CASH')
    cheque_number=models.CharField(max_length=255,blank=True,null=True)
    cheque_date=models.DateField(blank=True,null=True)
    coop_account=models.ForeignKey(CooperativeBankAccounts,on_delete=models.CASCADE,blank=True,null=True)
    member_account=models.ForeignKey(MembersBankAccounts,on_delete=models.CASCADE,blank=True,null=True)
    transfer_date=models.DateField(blank=True,null=True)
    status= models.CharField(max_length=20,choices=TRANSACTION_STATUS,default='UNTREATED')



    # class Meta(DateObjectsModels.Meta):
    #     db_table="MemberShipTerminationFundDisbursement"


class MembersExclusiveness(DateObjectsModels):
    member= models.ForeignKey(Members,on_delete=models.CASCADE)
    transaction=models.ForeignKey(TransactionTypes,on_delete=models.CASCADE)
    task=models.ForeignKey(ExceptableCriterias,on_delete=models.CASCADE)
    purpose=models.CharField(max_length=255)
    approval_officer=models.CharField(max_length=255)
    approval_comment=models.TextField(blank=True,null=True)
    approval_status= models.CharField(max_length=30,choices=APPROVAL_STATUS,default='PENDING')
    approved_at=models.DateField(blank=True,null=True)
    status= models.CharField(max_length=20,choices=TRANSACTION_STATUS,default='UNTREATED')
    processing_status= models.CharField(max_length=30,choices=PROCESSING_STATUS,default='UNPROCESSED')


    # class Meta(DateObjectsModels.Meta):
    #     db_table="Members_Exclusiveness"



class NextOfKinsMaximun(DateObjectsModels):
    maximun=models.CharField(max_length=255)

    # class Meta(DateObjectsModels.Meta):
    #     db_table="Next_Of_Kins_Maximun"


class MembersNextOfKins(DateObjectsModels):
    member=models.ForeignKey(Members,on_delete=models.CASCADE)
    name=models.CharField(max_length=255)
    relationships=models.ForeignKey(NOKRelationships,on_delete=models.CASCADE)
    address=models.TextField(blank=True,null=True)
    phone_number=models.CharField(max_length=255)
    status= models.CharField(max_length=20,choices=MEMBERSHIP_STATUS,default='ACTIVE')
    lock_status= models.CharField(max_length=20,choices=LOCK_STATUS,default='LOCKED')

    # class Meta(DateObjectsModels.Meta):
    #     db_table="Members_Next_Of_Kins"



class MembersAccountsDomain(DateObjectsModels):
    member=models.ForeignKey(Members,on_delete=models.CASCADE)
    transaction=models.ForeignKey(TransactionTypes,on_delete=models.CASCADE)
    account_number=models.CharField(max_length=255,blank=True,null=True)
    status=models.CharField(max_length=20,choices=MEMBERSHIP_STATUS,default='ACTIVE')
    loan_lock=models.CharField(max_length=20,choices=YESNO,default='NO')

    # class Meta(DateObjectsModels.Meta):
    #     db_table="Members_Accounts_Domain"


class StandingOrderAccounts(DateObjectsModels):
    transaction=models.OneToOneField(MembersAccountsDomain,on_delete=models.CASCADE)
    amount=models.DecimalField(max_digits=20,decimal_places = 2)
    status=models.CharField(max_length=20,choices=MEMBERSHIP_STATUS,default='ACTIVE')
    lock_status=models.CharField(max_length=20,choices=LOCK_STATUS,default='LOCKED')

    # class Meta(DateObjectsModels.Meta):
    #     db_table="Standing_Order_Accounts"


class Xmas_Savings_Generated(DateObjectsModels):
    batch=models.CharField(max_length=100)


    # class Meta(DateObjectsModels.Meta):
    #     db_table="Xmas_Savings_Generated"

class Xmas_Savings_Shortlist(DateObjectsModels):
    CHOICES=(
        ("NONE",'NONE'),
        ("CASH",'CASH'),
        ("TRANSFERRED",'TRANSFERRED')
        )
    transaction=models.ForeignKey(MembersAccountsDomain,on_delete=models.CASCADE)
    amount=models.DecimalField(max_digits=20,decimal_places = 2)
    amount_paid=models.DecimalField(max_digits=20,decimal_places = 2,default=0)
    balance=models.DecimalField(max_digits=20,decimal_places = 2,default=0)
    period=models.DateField()
    batch=models.CharField(max_length=100)
    payment_channel=models.CharField(max_length=100,choices=CHOICES,default='NONE')
    status=models.CharField(max_length=20,choices=TRANSACTION_STATUS,default='UNTREATED')
    bank_account=models.ForeignKey(MembersBankAccounts,on_delete=models.CASCADE,blank=True,null=True)
    account_status=models.CharField(max_length=30,choices=YESNO,default="NO")
    details=models.TextField(blank=True,null=True)
    processing_status=models.CharField(max_length=20,choices=PROCESSING_STATUS,default='UNPROCESSED')
    submission_status= models.CharField(max_length=30,choices=SUBMISSION_STATUS,default='NOT SUBMITTED')


    # class Meta(DateObjectsModels.Meta):
    #     db_table="Xmas_Savings_Shortlist"



class StandingOrderDeactivatedAccounts(DateObjectsModels):
    transaction=models.ForeignKey(StandingOrderAccounts,on_delete=models.CASCADE)
    status= models.CharField(max_length=20,choices=TRANSACTION_STATUS,default='UNTREATED')

    # class Meta(DateObjectsModels.Meta):
    #     db_table="StandingOrderDeactivatedAccounts"



class StandingOrderAccountsSuspensionRequest(DateObjectsModels):
    transaction=models.ForeignKey(StandingOrderAccounts,on_delete=models.CASCADE)
    purpose=models.TextField()
    approval_officer=models.CharField(max_length=255,blank=True,null=True)
    approval_status = models.CharField(max_length=30,choices=APPROVAL_STATUS,default='PENDING')
    approval_comment=models.TextField(blank=True,null=True)
    approval_date=models.DateField(blank=True,null=True)
    status= models.CharField(max_length=20,choices=TRANSACTION_STATUS,default='UNTREATED')

    # class Meta(DateObjectsModels.Meta):
    #     db_table="StandingOrderAccountsSuspensionRequest"


class StandingOrderAccountsSuspensionReleaseRequest(DateObjectsModels):
    transaction=models.ForeignKey(StandingOrderAccounts,on_delete=models.CASCADE)
    purpose=models.TextField()
    approval_officer=models.CharField(max_length=255,blank=True,null=True)
    approval_status = models.CharField(max_length=30,choices=APPROVAL_STATUS,default='PENDING')
    approval_comment=models.TextField(blank=True,null=True)
    approval_date=models.DateField(blank=True,null=True)
    status= models.CharField(max_length=20,choices=TRANSACTION_STATUS,default='UNTREATED')


    # class Meta(DateObjectsModels.Meta):
    #     db_table="StandingOrderAccountsSuspensionRequest"


class SavingsUploaded(DateObjectsModels):
    transaction=models.ForeignKey(MembersAccountsDomain,on_delete=models.CASCADE)
    particulars=models.CharField(max_length=255)
    balance=models.DecimalField(max_digits=20,decimal_places = 2,default=0)
    schedule_amount=models.DecimalField(max_digits=20,decimal_places = 2,default=0)

    transaction_period=models.DateField(blank=True,null=True)
    status= models.CharField(max_length=20,choices=TRANSACTION_STATUS,default='UNTREATED')
    standing_order_update=models.CharField(max_length=20,choices=YESNO,default='YES')

    # class Meta(DateObjectsModels.Meta):
    #     db_table="Savings_Uploaded"


class LoansUploaded(DateObjectsModels):
    member= models.ForeignKey(Members,on_delete=models.CASCADE,blank=True,null=True)
    particulars=models.CharField(max_length=255)
    loan_number=models.CharField(max_length=255,blank=True,null=True)
    transaction=models.ForeignKey(TransactionTypes,on_delete=models.CASCADE,blank=True,null=True)
    loan_amount=models.DecimalField(max_digits=20,decimal_places = 2,default=0)
    amount_paid=models.DecimalField(max_digits=20,decimal_places = 2,default=0)
    balance=models.DecimalField(max_digits=20,decimal_places = 2,default=0)
    repayment=models.DecimalField(max_digits=20,decimal_places = 2,default=0)
    duration=models.IntegerField(default=0)
    interest_rate=models.DecimalField(max_digits=20,decimal_places = 2,default=0)
    interest_deduction=models.CharField(max_length=255,choices=INTEREST_DEDUCTION,default='SOURCE')
    admin_charge_rate=models.DecimalField(max_digits=20,decimal_places = 2,default=0)

    start_date=models.DateField(blank=True,null=True)
    stop_date=models.DateField(blank=True,null=True)
    transaction_period=models.DateField(blank=True,null=True)
    status= models.CharField(max_length=20,choices=TRANSACTION_STATUS,default='UNTREATED')




    # class Meta(DateObjectsModels.Meta):
    #     db_table="Loans_Uploaded"



class LoanRequest(DateObjectsModels):
    member=models.ForeignKey(Members,on_delete=models.CASCADE)
    loan=models.ForeignKey(TransactionTypes,on_delete=models.CASCADE,blank=True,null=True)
    loan_amount=models.DecimalField(max_digits=20,decimal_places = 2)
    applied_amount=models.DecimalField(max_digits=20,decimal_places = 2)
    duration=models.IntegerField(default=0)
    interest=models.DecimalField(max_digits=20,decimal_places = 2,default=0)
    admin_charge=models.DecimalField(max_digits=20,decimal_places = 2,default=0)
    comment=models.TextField(blank=True,null=True)
    description=models.CharField(max_length=255,blank=True,null=True)
    receipt=models.CharField(max_length=255,blank=True,null=True)
    gross_pay=models.DecimalField(max_digits=20,decimal_places = 2,default=0)
    net_pay=models.DecimalField(max_digits=20,decimal_places = 2,default=0)
    savings=models.DecimalField(max_digits=20,decimal_places = 2,default=0)
    saving_status=  models.CharField(max_length=30,choices=YESNO,default='NO')
    ignore_restriction=  models.CharField(max_length=30,choices=YESNO,default='NO')
    existing_loan_balance=models.DecimalField(max_digits=20,decimal_places = 2,default=0)
    image=models.FileField(blank=True,null=True)
    transaction_status= models.CharField(max_length=20,choices=TRANSACTION_STATUS,default='UNTREATED')
    submission_status=  models.CharField(max_length=30,choices=SUBMISSION_STATUS,default='NOT SUBMITTED')
    date_applied=models.DateField(blank=True,null=True)
    loan_path= models.CharField(max_length=20,choices=LOAN_PATH,default='PROJECT')
    # short_listed=  models.CharField(max_length=30,choices=YESNO,default='NO')
    # short_listed_date=models.DateField(blank=True,null=True)
    # short_list_by=models.CharField(max_length=255,blank=True,null=True)

    # class Meta(DateObjectsModels.Meta):
    #     db_table="Loan_Request"



class LoanRequestShortListing(DateObjectsModels):
    applicant=models.ForeignKey(LoanRequest,on_delete=models.CASCADE,blank=True,null=True)
    approval_officer=models.CharField(max_length=255,blank=True,null=True)
    approval_status = models.CharField(max_length=30,choices=APPROVAL_STATUS,default='PENDING')
    approval_comment=models.TextField(blank=True,null=True)
    approval_date=models.DateField(blank=True,null=True)
    approved_amount=models.DecimalField(max_digits=20,decimal_places = 2,default=0)
    status= models.CharField(max_length=20,choices=TRANSACTION_STATUS,default='UNTREATED')

    #     db_table="LoanRequestShortListing"
    # class Meta(DateObjectsModels.Meta):

class LoanRequestAttachments(DateObjectsModels):
    applicant=models.ForeignKey(LoanRequest,on_delete=models.CASCADE,blank=True,null=True)
    description=models.CharField(max_length=255)
    image=models.FileField()
    status= models.CharField(max_length=20,choices=TRANSACTION_STATUS,default='UNTREATED')

    # class Meta(DateObjectsModels.Meta):
    #     db_table="Loan_Request_Attachments"

class LoanRequestSettings(DateObjectsModels):
    applicant=models.ForeignKey(LoanRequest,on_delete=models.CASCADE,blank=True,null=True)
    description=models.CharField(max_length=255)
    value=models.CharField(max_length=255)
    category= models.CharField(max_length=255,blank=True,null=True)
    waver=models.BooleanField(default=False)
    status= models.CharField(max_length=20,choices=TRANSACTION_STATUS,default='UNTREATED')

    # class Meta(DateObjectsModels.Meta):
    #     db_table="Loan_Request_Settings"

class LoanFormIssuance(DateObjectsModels):
    member=models.ForeignKey(Members,on_delete=models.CASCADE)
    loan=models.ForeignKey(TransactionTypes,on_delete=models.CASCADE)
    loan_amount=models.DecimalField(max_digits=20,decimal_places = 2)
    amount_saved=models.DecimalField(max_digits=20,decimal_places = 2)
    receipt=models.CharField(max_length=255,unique=True)
    processing_status= models.CharField(max_length=20,choices=PROCESSING_STATUS,default='UNPROCESSED')
    date_applied=models.DateField(blank=True,null=True)
    date_approved=models.DateField(blank=True,null=True)
    loan_path= models.CharField(max_length=20,choices=LOAN_PATH,default='PROJECT')
    status= models.CharField(max_length=20,choices=TRANSACTION_STATUS,default='UNTREATED')
    print_status= models.CharField(max_length=20,choices=YESNO,default='NO')

    # class Meta(DateObjectsModels.Meta):
    #     db_table="Loan_Form_Issuance"

class LoanApplication(DateObjectsModels):
    applicant=models.ForeignKey(LoanFormIssuance,on_delete=models.CASCADE,blank=True,null=True)
    loan_amount=models.DecimalField(max_digits=20,decimal_places = 2)
    duration=models.IntegerField(default=0)
    interest=models.DecimalField(max_digits=20,decimal_places = 2,default=0)
    admin_charge=models.DecimalField(max_digits=20,decimal_places = 2,default=0)
    comment=models.TextField(blank=True,null=True)
    ignore_restriction=  models.CharField(max_length=30,choices=YESNO,default='NO')
    gross_pay=models.DecimalField(max_digits=20,decimal_places = 2,default=0)
    net_pay=models.DecimalField(max_digits=20,decimal_places = 2,default=0)
    image=models.FileField(blank=True,null=True)
    bank_account=models.ForeignKey(MembersBankAccounts,on_delete=models.CASCADE,blank=True,null=True)
    transaction_status= models.CharField(max_length=20,choices=TRANSACTION_STATUS,default='UNTREATED')
    nok_name=models.CharField(max_length=255,blank=True,null=True)
    nok_Relationship=models.CharField(max_length=255,blank=True,null=True)
    nok_phone_no=models.CharField(max_length=255,blank=True,null=True)
    nok_address=models.CharField(max_length=255,blank=True,null=True)
    date_applied=models.DateField(blank=True,null=True)

    # class Meta(DateObjectsModels.Meta):
    #     db_table="Loan_Application"



class LoanApplicationGuarnators(DateObjectsModels):
    applicant=models.ForeignKey(LoanApplication,on_delete=models.CASCADE,blank=True,null=True)
    guarantor=models.ForeignKey(Members,on_delete=models.CASCADE,blank=True,null=True)
    status= models.CharField(max_length=20,choices=TRANSACTION_STATUS,default='UNTREATED')


    # class Meta(DateObjectsModels.Meta):
    #     db_table="Loan_Application_Guarnators"


class LoanApplicationSettings(DateObjectsModels):
    applicant=models.ForeignKey(LoanApplication,on_delete=models.CASCADE,blank=True,null=True)
    description=models.CharField(max_length=255)
    value=models.CharField(max_length=255)
    category= models.CharField(max_length=255,blank=True,null=True)
    tag= models.CharField(max_length=255,default=0)
    waver=models.BooleanField(default=False)
    status= models.CharField(max_length=20,choices=TRANSACTION_STATUS,default='UNTREATED')

    # class Meta(DateObjectsModels.Meta):
    #     db_table="Loan_Application_Settings"


class LoanApplicationShortListing(DateObjectsModels):
    applicant=models.ForeignKey(LoanApplication,on_delete=models.CASCADE,blank=True,null=True)
    approval_officer=models.CharField(max_length=255,blank=True,null=True)
    approved_amount=models.DecimalField(max_digits=20,decimal_places = 2,blank=True,null=True)
    approval_status = models.CharField(max_length=30,choices=APPROVAL_STATUS,default='PENDING')
    approval_comment=models.TextField(blank=True,null=True)
    approval_date=models.DateField(blank=True,null=True)
    loan_number=models.CharField(max_length=255,blank=True,null=True)
    status= models.CharField(max_length=20,choices=TRANSACTION_STATUS,default='UNTREATED')
    processing_status= models.CharField(max_length=20,choices=PROCESSING_STATUS,default='UNPROCESSED')
 
    # class Meta(DateObjectsModels.Meta):
    #     db_table="LoanApplicationShortListing"



class LoansRepaymentBase(DateObjectsModels):
    member= models.ForeignKey(Members,on_delete=models.CASCADE,blank=True,null=True)

    transaction= models.ForeignKey(TransactionTypes,on_delete=models.CASCADE,blank=True,null=True)
    loan_number=models.CharField(max_length=255,unique=True)
    duration=models.CharField(max_length=255,blank=True,null=True)
    interest_deduction=models.CharField(max_length=20,choices=INTEREST_DEDUCTION,default='SOURCE')
    interest_rate=models.IntegerField(default=0)
    interest=models.DecimalField(max_digits=20,decimal_places = 2,default=0)
    admin_charge=models.DecimalField(max_digits=20,decimal_places = 2,default=0)
    loan_amount=models.DecimalField(max_digits=20,decimal_places = 2)
    repayment=models.DecimalField(max_digits=20,decimal_places = 2)
    amount_paid=models.DecimalField(max_digits=20,decimal_places = 2,default=0)
    balance=models.DecimalField(max_digits=20,decimal_places = 2)
    base_amount=models.DecimalField(max_digits=20,decimal_places = 2,default=0)
    penalty_amount=models.DecimalField(max_digits=20,decimal_places = 2,default=0)
    start_date=models.DateField(blank=True,null=True)
    stop_date=models.DateField(blank=True,null=True)
    status=models.CharField(max_length=20,choices=MEMBERSHIP_STATUS,default='ACTIVE')
    schedule_status=models.CharField(max_length=20,choices=LOAN_SCHEDULE_STATUS,default='UNSCHEDULED')
    nok_name=models.CharField(max_length=255,blank=True,null=True)
    nok_Relationship=models.CharField(max_length=255,blank=True,null=True)
    nok_phone_no=models.CharField(max_length=255,blank=True,null=True)
    nok_address=models.CharField(max_length=255,blank=True,null=True)
    penalty_status=models.CharField(max_length=20,choices=PENALTY_STATUS,default='NORMAL')
    completed=  models.CharField(max_length=30,choices=YESNO,default='NO')

    # class Meta(DateObjectsModels.Meta):
    #     db_table="Loans_Repayment_Base"

class LoanGuarantors(DateObjectsModels):
    loan= models.ForeignKey(LoansRepaymentBase,on_delete=models.CASCADE,blank=True,null=True)
    member= models.ForeignKey(Members,on_delete=models.CASCADE,blank=True,null=True)
    status=models.CharField(max_length=20, choices=LOCK_STATUS,default='OPEN')

    # class Meta(DateObjectsModels.Meta):
    #     db_table="Loan_Guarantors"

class LoanUnschedulingRequest(DateObjectsModels):
    loan=models.ForeignKey(LoansRepaymentBase,on_delete=models.CASCADE)
    comment=models.CharField(max_length=255)
    approval_officer=models.CharField(max_length=255,blank=True,null=True)
    approval_status = models.CharField(max_length=30,choices=APPROVAL_STATUS,default='PENDING')
    approval_comment=models.TextField(blank=True,null=True)
    approval_date=models.DateField(blank=True,null=True)
    status=models.CharField(max_length=20,choices=TRANSACTION_STATUS,default='UNTREATED')


    # class Meta(DateObjectsModels.Meta):
    #     db_table="Loans_Cleared"

class LoansCleared(DateObjectsModels):
    loan=models.ForeignKey(LoansRepaymentBase,on_delete=models.CASCADE)
    status=models.CharField(max_length=20,choices=TRANSACTION_STATUS,default='UNTREATED')
    comment=models.CharField(max_length=255,default='Normal Clearance')

    # class Meta(DateObjectsModels.Meta):
    #     db_table="Loans_Cleared"


class MonthlyDeductionList(DateObjectsModels):
    member=models.ForeignKey(Members,on_delete=models.CASCADE)
    transaction_period=models.DateField(blank=True,null=True)
    transaction=models.ForeignKey(TransactionTypes,on_delete=models.CASCADE)
    account_number=models.CharField(max_length=255,blank=True,null=True)
    amount=models.DecimalField(max_digits=20,decimal_places = 2,default=0)
    amount_deducted=models.DecimalField(max_digits=20,decimal_places = 2,default=0)
    balance=models.DecimalField(max_digits=20,decimal_places = 2,default=0)
    repayment=models.DecimalField(max_digits=20,decimal_places = 2,default=0)
    penalty=models.DecimalField(max_digits=20,decimal_places = 2,default=0)
    processing_status=models.CharField(max_length=20,choices=PROCESSING_STATUS,default='UNPROCESSED')
    rectified=models.CharField(max_length=20,choices=YESNO,default='NO')
    salary_institution=models.ForeignKey(SalaryInstitution,on_delete=models.CASCADE)
    status= models.CharField(max_length=20,choices=TRANSACTION_STATUS,default='UNTREATED')


    # class Meta(DateObjectsModels.Meta):
    #     db_table="Monthly_Deduction_List"



class MonthlyGeneratedTransactions(DateObjectsModels):
    transaction=models.ForeignKey(TransactionTypes,on_delete=models.CASCADE)
    transaction_period=models.DateField(blank=True,null=True)
    salary_institution=models.ForeignKey(SalaryInstitution,on_delete=models.CASCADE)
    transaction_status= models.CharField(max_length=20,choices=TRANSACTION_STATUS,default='UNTREATED')


    # class Meta(DateObjectsModels.Meta):
    #     db_table="Monthly_Generated_Transactions"


class MonthlyDeductionListGenerated(DateObjectsModels):
    transaction_period=models.DateField(blank=True,null=True)
    member=models.ForeignKey(Members,on_delete=models.CASCADE)
    amount=models.DecimalField(max_digits=20,decimal_places = 2,default=0)
    aux_amount=models.DecimalField(max_digits=20,decimal_places = 2,default=0)
    amount_deducted=models.DecimalField(max_digits=20,decimal_places = 2,default=0)
    balance=models.DecimalField(max_digits=20,decimal_places = 2,default=0)
    salary_institution=models.ForeignKey(SalaryInstitution,on_delete=models.CASCADE)
    transaction_status= models.CharField(max_length=20,choices=TRANSACTION_STATUS,default='UNTREATED')
    processing_status=models.CharField(max_length=20,choices=PROCESSING_STATUS,default='UNPROCESSED')

    verification=models.CharField(max_length=20, choices=YESNO,default='NO')
    rectified=models.CharField(max_length=20, choices=YESNO,default='NO')


    # class Meta(DateObjectsModels.Meta):
    #     db_table="Monthly_Deduction_List_Generated"


class MonthlyGroupGeneratedTransactions(DateObjectsModels):
    salary_institution=models.ForeignKey(SalaryInstitution,on_delete=models.CASCADE)
    transaction_period=models.DateField(blank=True,null=True)
    transaction_status= models.CharField(max_length=20,choices=TRANSACTION_STATUS,default='UNTREATED')

    # class Meta(DateObjectsModels.Meta):
    #     db_table="Monthly_Group_Generated_Transactions"


class MonthlyDeductionGenerationHeading(DateObjectsModels):
     salary_institution=models.ForeignKey(SalaryInstitution,on_delete=models.CASCADE)
     transaction_period=models.DateField(blank=True,null=True)
     heading=models.CharField(max_length=255)
     status= models.CharField(max_length=20,choices=TRANSACTION_STATUS,default='UNTREATED')

    # class Meta(DateObjectsModels.Meta):
    #     db_table="Monthly_Deduction_Generation_Heading


class AccountDeductions(DateObjectsModels):
    salary_institution=models.ForeignKey(SalaryInstitution,on_delete=models.CASCADE)
    transaction_period=models.DateField(blank=True,null=True)
    ippis_no=models.CharField(max_length=255)
    # ippis_no1=models.CharField(max_length=255)
    name=models.CharField(max_length=255)
    amount=models.DecimalField(max_digits=20,decimal_places = 2,default=0)
    transaction_status= models.CharField(max_length=20,choices=TRANSACTION_STATUS,default='UNTREATED')


    # class Meta(DateObjectsModels.Meta):
    #     db_table="Account_Deductions"

class AuxillaryDeductions(DateObjectsModels):
    salary_institution=models.ForeignKey(SalaryInstitution,on_delete=models.CASCADE)
    transaction_period=models.DateField(blank=True,null=True)
    coop_no=models.CharField(max_length=255)
    ippis_no=models.CharField(max_length=255)
    name=models.CharField(max_length=255)
    amount=models.DecimalField(max_digits=20,decimal_places = 2,default=0)
    transaction_status= models.CharField(max_length=20,choices=TRANSACTION_STATUS,default='UNTREATED')


    # class Meta(DateObjectsModels.Meta):
    #     db_table="Account_Deductions"

# class AuxillaryDeductionsLeftOver(DateObjectsModels):
#     salary_institution=models.ForeignKey(SalaryInstitution,on_delete=models.CASCADE)
#     transaction_period=models.DateField(blank=True,null=True)
#     coop_no=models.CharField(max_length=255)
#     ippis_no=models.CharField(max_length=255)
#     name=models.CharField(max_length=255)
#     amount=models.DecimalField(max_digits=20,decimal_places = 2,default=0)
#     transaction_status= models.CharField(max_length=20,choices=TRANSACTION_STATUS,default='UNTREATED')


#     # class Meta(DateObjectsModels.Meta):
#     #     db_table="AuxillaryDeductionsLeftOver"




class TransactionAjustmentRequest(DateObjectsModels):
    member=models.ForeignKey(MembersAccountsDomain,on_delete=models.CASCADE)
    amount=models.DecimalField(max_digits=20,decimal_places = 2)
    approval_officer=models.CharField(max_length=255,blank=True,null=True)
    approval_status= models.CharField(max_length=30,choices=APPROVAL_STATUS,default='PENDING')
    approved_at=models.DateField(blank=True,null=True)
    effective_date=models.DateField(blank=True,null=True)
    status=models.CharField(max_length=20,choices=TRANSACTION_STATUS,default='UNTREATED')


    # class Meta(DateObjectsModels.Meta):
    #     db_table="Transaction_Adjustment_Request"


class TransactionAjustmentHistory(DateObjectsModels):
    member=models.ForeignKey(MembersAccountsDomain,on_delete=models.CASCADE)
    amount=models.DecimalField(max_digits=20,decimal_places = 2)
    start_date=models.DateField()
    stop_date=models.DateField()

    # class Meta(DateObjectsModels.Meta):
    #     db_table="Transaction_Ajustment_History"


class TransactionLoanAjustmentRequest(DateObjectsModels):
    member=models.ForeignKey(LoansRepaymentBase,on_delete=models.CASCADE)
    amount=models.DecimalField(max_digits=20,decimal_places = 2)
    approval_officer=models.CharField(max_length=255,blank=True,null=True)
    approval_status= models.CharField(max_length=30,choices=APPROVAL_STATUS,default='PENDING')
    approved_at=models.DateField(blank=True,null=True)
    effective_date=models.DateField(blank=True,null=True)
    status=models.CharField(max_length=20,choices=TRANSACTION_STATUS,default='UNTREATED')


    # class Meta(DateObjectsModels.Meta):
    #     db_table="Transaction_Loan_Adjustment_Request"



class Saving_Fund_Transfer_History(DateObjectsModels):
    member=models.ForeignKey(Members,on_delete=models.CASCADE)
    sources_account_name=models.CharField(max_length=255)
    sources_accoun_number=models.CharField(max_length=255)    
    destination_account_name=models.CharField(max_length=255)
    destination_accoun_number=models.CharField(max_length=255)
    amount=models.DecimalField(max_digits=20,decimal_places = 2)
    particulars= models.TextField()
    

    # class Meta(DateObjectsModels.Meta):
    #     db_table="Saving_Fund_Transfer_History"







class LoanLessRepaymentEnable(DateObjectsModels):
    status= models.CharField(max_length=30,choices=YESNO,default='NO')


    # class Meta(DateObjectsModels.Meta):
    #     db_table="LoanLessRepaymentEnable"




class NorminalRoll(DateObjectsModels):
    member_id=models.CharField(max_length=255)
    file_no=models.CharField(max_length=255,unique=True)
    ippis_no=models.CharField(max_length=255,unique=True)
    last_name=models.CharField(max_length=255)
    first_name=models.CharField(max_length=255)
    middle_name=models.CharField(max_length=255,blank=True,null=True)
    phone_no=models.CharField(max_length=255,unique=True)
    year=models.CharField(max_length=255)
    month=models.CharField(max_length=255)
    date_of_first_appointment=models.DateField()
    dob=models.DateField()
    next_of_kin=models.CharField(max_length=255,blank=True,null=True)
    salary_institution=models.CharField(max_length=255)
    transaction_status=models.CharField(max_length=20,choices=TRANSACTION_STATUS,default='UNTREATED')


    @property
    def get_middle_name(self):
        if self.middle_name:
              return self.middle_name
        else:
              return ""

    # class Meta(DateObjectsModels.Meta):
    #     db_table="Norminal_Roll"


####################################################################
##################### SHARES MANAGER AND STAFF WAREFSRE ###############################
####################################################################
class SharesDeductionSavings(DateObjectsModels):
    savings=models.ForeignKey(TransactionTypes,on_delete=models.CASCADE,blank=True,null=True)


    # class Meta(DateObjectsModels.Meta):
    #     db_table="Shares_Deduction_Savings"

class MembersShareConfigurations(DateObjectsModels):
    unit_cost=models.DecimalField(max_digits=20,decimal_places = 2,default=0)

    # class Meta(DateObjectsModels.Meta):
    #     db_table="Members_Share_Configurations"


class MembersSharePurchaseRequest(DateObjectsModels):
    member=models.ForeignKey(MembersAccountsDomain,on_delete=models.CASCADE,blank=True,null=True)
    units=models.IntegerField(default=0)
    approval_officer=models.CharField(max_length=255,blank=True,null=True)
    approval_status = models.CharField(max_length=30,choices=APPROVAL_STATUS,default='PENDING')
    approval_comment=models.TextField(blank=True,null=True)
    approval_date=models.DateField(blank=True,null=True)
    status= models.CharField(max_length=20,choices=TRANSACTION_STATUS,default='UNTREATED')

    # class Meta(DateObjectsModels.Meta):
    #     db_table="Members_Share_Purchase_Request"


class MembersShareAccounts(DateObjectsModels):
    member=models.ForeignKey(MembersAccountsDomain,on_delete=models.CASCADE,blank=True,null=True)
    shares=models.DecimalField(max_digits=20,decimal_places = 2,default=0)
    unit_cost=models.DecimalField(max_digits=20,decimal_places = 2,default=0)
    total_cost=models.DecimalField(max_digits=20,decimal_places = 2,default=0)
    effective_date=models.DateField(blank=True,null=True)
    year=models.IntegerField(default=0)
    status= models.CharField(max_length=20,choices=TRANSACTION_STATUS,default='UNTREATED')

    # class Meta(DateObjectsModels.Meta):
    #     db_table="Members_Share_Accounts"


class MembersShareAccountsMain(DateObjectsModels):
    member=models.ForeignKey(Members,on_delete=models.CASCADE)
    account_number=models.IntegerField(default=0)
    shares=models.IntegerField(default=0)
    unit_cost=models.DecimalField(max_digits=20,decimal_places = 2,default=0)
    total_cost=models.DecimalField(max_digits=20,decimal_places = 2,default=0)
    effective_date=models.DateField(blank=True,null=True)
    year=models.IntegerField(default=0)
    status= models.CharField(max_length=20,choices=MEMBERSHIP_STATUS,default='ACTIVE')


    # class Meta(DateObjectsModels.Meta):
    #     db_table="Members_Share_Accounts_Main"


class MembersShareInitialUpdateRequest(DateObjectsModels):
    member=models.ForeignKey(MembersShareAccounts,on_delete=models.CASCADE)
    transaction=models.ForeignKey(TransactionTypes,on_delete=models.CASCADE)
    amount=models.DecimalField(max_digits=20,decimal_places = 2,default=0)
    approval_officer=models.CharField(max_length=255,blank=True,null=True)
    approval_status= models.CharField(max_length=30,choices=APPROVAL_STATUS,default='PENDING')
    approval_comment=models.TextField(blank=True,null=True)
    approved_at=models.DateField(blank=True,null=True)
    status= models.CharField(max_length=20,choices=TRANSACTION_STATUS,default='UNTREATED')


    # class Meta(DateObjectsModels.Meta):
    #     db_table="Members_Share_Initial_Update_Request"


class SharesSalesRecord(DateObjectsModels):
    member=models.ForeignKey(MembersAccountsDomain,on_delete=models.CASCADE)
    payment_reference=models.CharField(max_length=255,blank=True,null=True)
    receipt=models.CharField(max_length=255,unique=True)
    shares=models.IntegerField(default=0)
    unit_cost = models.DecimalField(max_digits=20,decimal_places = 2,blank=True,null=True)
    share_amount = models.DecimalField(max_digits=20,decimal_places = 2,blank=True,null=True)
    bank_account= models.ForeignKey(CooperativeBankAccounts,on_delete=models.CASCADE,blank=True,null=True)
    image=models.FileField(blank=True,null=True)
    status= models.CharField(max_length=20,choices=TRANSACTION_STATUS,default='UNTREATED')


    # class Meta(DateObjectsModels.Meta):
    #     db_table="Shares_Sales_Record"


class MembersWelfare(DateObjectsModels):
    amount=models.DecimalField(max_digits=20,decimal_places = 2,default=0)


    # class Meta(DateObjectsModels.Meta):
    #     db_table="Members_Welfare"


class MembersWelfareAccounts(DateObjectsModels):
    member=models.ForeignKey(MembersAccountsDomain,on_delete=models.CASCADE)
    amount=models.DecimalField(max_digits=20,decimal_places = 2,default=0)
    year=models.IntegerField(default=0)
    status= models.CharField(max_length=20,choices=TRANSACTION_STATUS,default='UNTREATED')

    # class Meta(DateObjectsModels.Meta):
    #     db_table="Members_Welfare_Accounts"

####################################################################
##################### MEMBERS CASH DEPOSIT/ WITHDRAWALS ############
####################################################################
class MembersCashDeposits(DateObjectsModels):
    member=models.ForeignKey(Members,on_delete=models.CASCADE)
    bank_accounts=models.ForeignKey(CooperativeBankAccounts,on_delete=models.CASCADE)
    account_number=models.CharField(max_length=255,blank=True,null=True)
    transaction=models.ForeignKey(TransactionTypes,on_delete=models.CASCADE)
    amount=models.DecimalField(max_digits=20,decimal_places = 2,default=0)
    payment_reference=models.CharField(max_length=255)
    payment_evidience=models.FileField(blank=True,null=True)
    receipt=models.CharField(max_length=255,blank=True,null=True)
    purpose=models.TextField()
    payment_date=models.DateField()
    status= models.CharField(max_length=20,choices=TRANSACTION_STATUS,default='UNTREATED')


    # class Meta(DateObjectsModels.Meta):
    #     db_table="Members_Cash_Deposits"

class MembersCashWithdrawals(DateObjectsModels):
    member=models.ForeignKey(MembersAccountsDomain,on_delete=models.CASCADE)
    amount=models.DecimalField(max_digits=20,decimal_places = 2,default=0)
    ledger_balance=models.DecimalField(max_digits=20,decimal_places = 2,default=0)
    narration=models.TextField()
    approved_amount=models.DecimalField(max_digits=20,decimal_places = 2,default=0)
    approval_officer=models.CharField(max_length=255,blank=True,null=True)
    approval_status = models.CharField(max_length=30,choices=APPROVAL_STATUS,default='PENDING')
    approval_comment=models.TextField(blank=True,null=True)
    approval_date=models.DateField(blank=True,null=True)
    status= models.CharField(max_length=20,choices=TRANSACTION_STATUS,default='UNTREATED')
    maturity_date=models.DateField(blank=True,null=True)

    # class Meta(DateObjectsModels.Meta):
    #     db_table="Members_Cash_Withdrawals"


class MembersCashWithdrawalsApplication(DateObjectsModels):
    member=models.ForeignKey(MembersAccountsDomain,on_delete=models.CASCADE)
    amount=models.DecimalField(max_digits=20,decimal_places = 2,default=0)
    ledger_balance=models.DecimalField(max_digits=20,decimal_places = 2,default=0)
    narration=models.TextField()
    approved_amount=models.DecimalField(max_digits=20,decimal_places = 2,default=0)
    approval_officer=models.CharField(max_length=255,blank=True,null=True)
    approval_status = models.CharField(max_length=30,choices=APPROVAL_STATUS,default='PENDING')
    approval_comment=models.TextField(blank=True,null=True)
    approval_date=models.DateField(blank=True,null=True)
    certification_officer=models.CharField(max_length=255,blank=True,null=True)
    certification_status = models.CharField(max_length=20,choices=CERTIFICATION_STATUS,default='PENDING')
    certification_comment=models.TextField(blank=True,null=True)
    certification_date=models.DateField(blank=True,null=True)
    status= models.CharField(max_length=20,choices=TRANSACTION_STATUS,default='UNTREATED')
    maturity_date=models.DateField(blank=True,null=True)

    # class Meta(DateObjectsModels.Meta):
    #     db_table="Members_Cash_Withdrawals_Application"


class MembersCashWithdrawalsMain(DateObjectsModels):
    member=models.ForeignKey(MembersCashWithdrawalsApplication,on_delete=models.CASCADE)
    channel=models.CharField(max_length=30,choices=PAYMENT_CHANNEL,default='CASH')
    payment_date=models.DateField(blank=True,null=True)
    coop_account=models.ForeignKey(CooperativeBankAccounts,on_delete=models.CASCADE,blank=True,null=True)
    member_account=models.ForeignKey(MembersBankAccounts,on_delete=models.CASCADE,blank=True,null=True)
    cheque_number=models.CharField(max_length=255,blank=True,null=True)
    disbursement_officer=models.CharField(max_length=255,blank=True,null=True)
    disbursement_status = models.CharField(max_length=30,choices=APPROVAL_STATUS,default='PENDING')
    disbursement_date=models.DateField(blank=True,null=True)
    status= models.CharField(max_length=20,choices=TRANSACTION_STATUS,default='UNTREATED')

    # class Meta(DateObjectsModels.Meta):
    #     db_table="Members_Cash_Withdrawals_Main"


class Companies(titleBase):
    class Meta(titleBase.Meta):
        # db_table="companies"
        ordering = ['title']


    def __str__(self):
        return self.title



class Commodity_Categories(DateObjectsModels):

    REQUIRED_STATUS=(
        ('0','NO'),
        ('1','YES')
        )
    transaction=models.ForeignKey(TransactionTypes,on_delete=models.CASCADE)
    title=models.CharField(max_length=100,unique=True)
    duration= models.PositiveSmallIntegerField(validators=[MinValueValidator(0)],default=0)
    interest_rate_required= models.CharField(default='1',choices=REQUIRED_STATUS,max_length=15)
    interest_rate= models.PositiveSmallIntegerField(validators=[MinValueValidator(0)],default=0)
    admin_charges_required= models.CharField(default='1',choices=REQUIRED_STATUS,max_length=15)
    admin_charges_rating= models.CharField(max_length=30,choices=ADMIN_CHARGES,default="CASH")
    admin_charges = models.DecimalField(max_digits=20,decimal_places = 2,blank=True,null=True)
    guarantor_required= models.CharField(default='1',choices=REQUIRED_STATUS,max_length=15)
    guarantors= models.IntegerField(default=0)
    guarantors_gross_pay_rating= models.DecimalField(max_digits=20,decimal_places = 2,default=100)
    loan_age= models.IntegerField(default=0)
    receipt_type= models.CharField(max_length=30,choices=RECEIPT_TYPES,default='AUTO')
    status= models.CharField(max_length=20,choices=MEMBERSHIP_STATUS,default='ACTIVE')
    multiple_loan_status= models.CharField(max_length=20,choices=MULTIPLE_LOAN_STATUS,default='NOT ALLOWED')
    form_print=models.CharField(max_length=20,choices=YESNO,default='NO')


    def __str__(self):
        return self.title

class Commodity_Category_Sub(DateObjectsModels):
    category=models.ForeignKey(Commodity_Categories,on_delete=models.CASCADE)
    title=models.CharField(max_length=100,unique=True)
    status= models.CharField(max_length=20,choices=MEMBERSHIP_STATUS,default='INACTIVE')

    def __str__(self):
        return self.title


class Treanding_Commodity_Signatory(DateObjectsModels):
    name=models.CharField(max_length=100)
    designation=models.CharField(max_length=100)
    phone_no=models.CharField(max_length=11)

    def __str__(self):
        return self.name

class Company_Products_Duration(DateObjectsModels):
    product=models.ForeignKey(Commodity_Categories,on_delete=models.CASCADE)
    period=models.ForeignKey(Commodity_Period,on_delete=models.CASCADE,blank=True,null=True)
    batch=models.ForeignKey(Commodity_Period_Batch,on_delete=models.CASCADE,blank=True,null=True)
    start_date=models.DateField(blank=True,null=True)
    stop_date=models.DateField(blank=True,null=True)

    # class Meta(DateObjectsModels.Meta):
    #     db_table="Company_Products_Duration"


class Commodity_Product_List(DateObjectsModels):
    sub_category=models.ForeignKey(Commodity_Category_Sub,on_delete=models.CASCADE,blank=True,null=True)
    # category=models.CharField(max_length=255)
    product_name=models.CharField(max_length=255)
    product_model=models.CharField(max_length=100,blank=True,null=True)
    details=models.TextField(blank=True,null=True)
    no_in_pack= models.PositiveSmallIntegerField(validators=[MinValueValidator(0)],default=1)
    status= models.CharField(max_length=20,choices=MEMBERSHIP_STATUS,default='ACTIVE')


    def __str__(self):
        return self.product_name



class Company_Products(DateObjectsModels):
    product=models.ForeignKey(Commodity_Product_List,on_delete=models.CASCADE)
    company=models.ForeignKey(Companies,on_delete=models.CASCADE)
    amount=models.DecimalField(max_digits=20,decimal_places = 2,default=0)
    coop_amount=models.DecimalField(max_digits=20,decimal_places = 2,default=0)
    interest= models.DecimalField(max_digits=20,decimal_places = 2,blank=True,null=True)
    period=models.ForeignKey(Commodity_Period,on_delete=models.CASCADE,blank=True,null=True)
    batch=models.ForeignKey(Commodity_Period_Batch,on_delete=models.CASCADE,blank=True,null=True)
    status= models.CharField(max_length=20,choices=MEMBERSHIP_STATUS,default='ACTIVE')


    # class Meta(DateObjectsModels.Meta):
    #     db_table="company_products"

class Members_Xmas_Commodity_Loan_Products_Selection_Summary(DateObjectsModels):
    member=models.ForeignKey(Members,on_delete=models.CASCADE)
    period=models.ForeignKey(Commodity_Period,on_delete=models.CASCADE,blank=True,null=True)
    batch=models.ForeignKey(Commodity_Period_Batch,on_delete=models.CASCADE,blank=True,null=True)
    amount=models.DecimalField(max_digits=20,decimal_places = 2,default=0)
    interest= models.DecimalField(max_digits=20,decimal_places = 2,blank=True,null=True)
    ticket=models.CharField(max_length=255,blank=True,null=True)
    duration= models.PositiveSmallIntegerField(validators=[MinValueValidator(0)],default=0)
    status= models.CharField(max_length=20,choices=TRANSACTION_STATUS,default='UNTREATED')
    

    # class Meta(DateObjectsModels.Meta):
    #     db_table="Members_Xmas_Commodity_Loan_Products_Selection_Summary"


class Members_Xmas_Commodity_Loan_Products_Selection(DateObjectsModels):
    member=models.ForeignKey(Members,on_delete=models.CASCADE)
    product=models.ForeignKey(Company_Products,on_delete=models.CASCADE)
    quantity=models.IntegerField(default=0)
    company_price=models.DecimalField(max_digits=20,decimal_places = 2,default=0)
    coop_price=models.DecimalField(max_digits=20,decimal_places = 2,default=0)
    interest= models.DecimalField(max_digits=20,decimal_places = 2,blank=True,null=True)
    ticket=models.CharField(max_length=255,blank=True,null=True)
    admin_charges = models.DecimalField(max_digits=20,decimal_places = 2,blank=True,null=True)
    duration= models.PositiveSmallIntegerField(validators=[MinValueValidator(0)],default=0)
    status= models.CharField(max_length=20,choices=TRANSACTION_STATUS,default='UNTREATED')
    selection_completed=models.CharField(max_length=20,choices=YESNO,default='NO')

    # class Meta(DateObjectsModels.Meta):
    #     db_table="Members_Xmas_Commodity_Loan_Products_Selection"



class Members_Commodity_Loan_Products_Selection(DateObjectsModels):
    member=models.ForeignKey(Members,on_delete=models.CASCADE)
    product=models.ForeignKey(Company_Products,on_delete=models.CASCADE)
    quantity=models.IntegerField(default=0)
    company_price=models.DecimalField(max_digits=20,decimal_places = 2,default=0)
    coop_price=models.DecimalField(max_digits=20,decimal_places = 2,default=0)
    interest= models.DecimalField(max_digits=20,decimal_places = 2,blank=True,null=True)
    ticket=models.CharField(max_length=255,blank=True,null=True)
    admin_charges = models.DecimalField(max_digits=20,decimal_places = 2,blank=True,null=True)
    duration= models.PositiveSmallIntegerField(validators=[MinValueValidator(0)],default=0)
    status= models.CharField(max_length=20,choices=TRANSACTION_STATUS,default='UNTREATED')


    # class Meta(DateObjectsModels.Meta):
    #     db_table="members_commodity_loan_products_selection"





class Members_Commodity_Loan_Application(DateObjectsModels):
    member=models.ForeignKey(Members_Commodity_Loan_Products_Selection,on_delete=models.CASCADE)
    company_price=models.DecimalField(max_digits=20,decimal_places = 2,default=0)
    coop_price=models.DecimalField(max_digits=20,decimal_places = 2,default=0)
    interest= models.DecimalField(max_digits=20,decimal_places = 2,blank=True,null=True)
    admin_charge = models.DecimalField(max_digits=20,decimal_places = 2,blank=True,null=True)
    duration= models.PositiveSmallIntegerField(validators=[MinValueValidator(0)],default=0)
    repayment= models.DecimalField(max_digits=20,decimal_places = 2,default=0)
    comments=models.TextField(blank=True,null=True)
    ticket=models.CharField(max_length=255,blank=True,null=True)
    serial_no=models.CharField(max_length=255,blank=True,null=True)
    phone_no1=models.CharField(max_length=255,blank=True,null=True)
    phone_no2=models.CharField(max_length=255,blank=True,null=True)
    receipt=models.CharField(max_length=255,blank=True,null=True)
    loan_number=models.CharField(max_length=255,blank=True,null=True)
    period=models.ForeignKey(Commodity_Period,on_delete=models.CASCADE,blank=True,null=True)
    batch=models.ForeignKey(Commodity_Period_Batch,on_delete=models.CASCADE,blank=True,null=True)
    approval_officer=models.CharField(max_length=255,blank=True,null=True)
    approval_status=models.CharField(max_length=30,choices=PROCESSING_STATUS,default='UNPROCESSED')
    approval_comment=models.TextField(blank=True,null=True)
    approval_date=models.DateField(blank=True,null=True)
    net_pay = models.DecimalField(max_digits=20,decimal_places = 2,default=0)
    net_pay_as_at=models.DateField(blank=True,null=True)
    image=models.FileField(blank=True,null=True)
    loans = models.DecimalField(max_digits=20,decimal_places = 2,default=0)
    effective_date=models.DateField(blank=True,null=True)
    savings = models.DecimalField(max_digits=20,decimal_places = 2,default=0)
    standing_order = models.DecimalField(max_digits=20,decimal_places = 2,default=0)
    submission_status=models.CharField(max_length=20,choices=SUBMISSION_STATUS,default="NOT SUBMITTED")
    short_listed=  models.CharField(max_length=30,choices=YESNO,default='NO')
    status= models.CharField(max_length=20,choices=TRANSACTION_STATUS,default='UNTREATED')

    @property
    def get_total(self):
        return float(self.company_price) + float(self.interest)


    # class Meta(DateObjectsModels.Meta):
    #     db_table="members_commodity_loan_application"



class Members_Commodity_Loan_Application_Settings(DateObjectsModels):
    applicant=models.ForeignKey(Members_Commodity_Loan_Application,on_delete=models.CASCADE)
    description=models.CharField(max_length=255)
    value=models.CharField(max_length=255)
    status= models.CharField(max_length=20,choices=TRANSACTION_STATUS,default='UNTREATED')
    ticket=models.CharField(max_length=255,blank=True,null=True)

    # class Meta(DateObjectsModels.Meta):
    #     db_table="members_commodity_loan_application_settings"





class Members_Commodity_Loan_Application_Form_Sales(DateObjectsModels):
    applicant=models.ForeignKey(Members_Commodity_Loan_Application,on_delete=models.CASCADE)
    receipt=models.CharField(max_length=255,blank=True,null=True)
    status = models.CharField(max_length=20,choices=TRANSACTION_STATUS,default='UNTREATED')


    # class Meta(DateObjectsModels.Meta):
    #     db_table="Members_Commodity_Loan_Application_Form_Sales"




class Members_Commodity_Loan_Application_Guarantors(DateObjectsModels):
    applicant=models.ForeignKey(Members_Commodity_Loan_Application_Form_Sales,on_delete=models.CASCADE)
    guarantor=models.ForeignKey(Members,on_delete=models.CASCADE)
    gross_pay = models.DecimalField(max_digits=20,decimal_places = 2,default=0)


    # class Meta(DateObjectsModels.Meta):
    #     db_table="Members_Commodity_Loan_Application_Guarantors"

class Commodity_Loan_Upload_Transaction_Header(DateObjectsModels):
    member=models.ForeignKey(Members,on_delete=models.CASCADE)
    category=models.ForeignKey(Commodity_Categories,on_delete=models.CASCADE,blank=True,null=True)
    ticket=models.CharField(max_length=30)
    loan_number=models.CharField(max_length=30,blank=True,null=True)
    loan_amount= models.DecimalField(max_digits=20,decimal_places = 2,default=0)
    balance= models.DecimalField(max_digits=20,decimal_places = 2,default=0)
    repayment= models.DecimalField(max_digits=20,decimal_places = 2,default=0)
    interest_rate= models.DecimalField(max_digits=20,decimal_places = 2,default=0)
    duration= models.PositiveSmallIntegerField(validators=[MinValueValidator(0)],default=0)
    start_date=models.DateField(blank=True,null=True)
    status = models.CharField(max_length=20,choices=TRANSACTION_STATUS,default='UNTREATED')
    ledger_status = models.CharField(max_length=20,choices=PROCESSING_STATUS,default='UNPROCESSED')


    # class Meta(DateObjectsModels.Meta):
    #     db_table="Commodity_Loan_Upload_Transaction_Header"


class Commodity_Loan_Upload_Transaction_Details(DateObjectsModels):
    ticket=models.ForeignKey(Commodity_Loan_Upload_Transaction_Header,on_delete=models.CASCADE)
    product=models.ForeignKey(Company_Products,on_delete=models.CASCADE)
    company_price= models.DecimalField(max_digits=20,decimal_places = 2,default=0)
    total_company= models.DecimalField(max_digits=20,decimal_places = 2,default=0)
    amount= models.DecimalField(max_digits=20,decimal_places = 2,default=0)
    quantity= models.PositiveSmallIntegerField(validators=[MinValueValidator(0)],default=0)
    total_amount= models.DecimalField(max_digits=20,decimal_places = 2,default=0)
    status = models.CharField(max_length=20,choices=TRANSACTION_STATUS,default='UNTREATED')


    # class Meta(DateObjectsModels.Meta):
    #     db_table="Commodity_Loan_Upload_Transaction_Details"


class Commodity_Loan_Invoicing_Products_Selection_Temp(DateObjectsModels):
    member=models.ForeignKey(Members,on_delete=models.CASCADE)
    description=models.TextField()
    rate= models.DecimalField(max_digits=20,decimal_places = 2,default=0)
    quantity= models.PositiveSmallIntegerField(validators=[MinValueValidator(0)],default=0)
    duration= models.PositiveSmallIntegerField(validators=[MinValueValidator(0)],default=0)
    total= models.DecimalField(max_digits=20,decimal_places = 2,default=0)
    repayment= models.DecimalField(max_digits=20,decimal_places = 2,default=0)
    size=models.CharField(max_length=255,blank=True,null=True)
    receipt=models.CharField(max_length=255,blank=True,null=True)
    effective_date=models.DateField(blank=True,null=True)
    status = models.CharField(max_length=20,choices=TRANSACTION_STATUS,default='UNTREATED')

    # class Meta(DateObjectsModels.Meta):
    #     db_table="Commodity_Loan_Invoicing_Products_Selection_Temp"


class Members_Commodity_Loan_Completed_Transactions(DateObjectsModels):
    member=models.ForeignKey(Members,on_delete=models.CASCADE)
    product_name=models.CharField(max_length=255)
    product_model=models.CharField(max_length=100,blank=True,null=True)
    details=models.TextField(blank=True,null=True)
    quantity= models.PositiveSmallIntegerField(validators=[MinValueValidator(0)],default=0)
    duration= models.PositiveSmallIntegerField(validators=[MinValueValidator(0)],default=0)
    loan_amount=models.DecimalField(max_digits=20,decimal_places = 2,default=0)
    amount_paid=models.DecimalField(max_digits=20,decimal_places = 2,default=0)
    serial_no=models.CharField(max_length=255,blank=True,null=True)
    phone_no1=models.CharField(max_length=255,blank=True,null=True)
    phone_no2=models.CharField(max_length=255,blank=True,null=True)
    loan_number=models.CharField(max_length=255,blank=True,null=True)
    receipt=models.CharField(max_length=255,blank=True,null=True)
    start_date=models.DateField(blank=True,null=True)
   
   
    # class Meta(DateObjectsModels.Meta):
    #     db_table="Members_Commodity_Loan_Completed_Transactions"


class Members_Commodity_Receipt_Phone_no(DateObjectsModels):
    name=models.CharField(max_length=100,blank=True,null=True)
    phone_no=models.CharField(max_length=100,blank=True,null=True)
    status=models.CharField(max_length=20,choices=MEMBERSHIP_STATUS,default='INACTIVE')
   
   
    # class Meta(DateObjectsModels.Meta):
    #     db_table="Members_Commodity_Receipt_Phone_no"




####################################################################
##################### LEDGER, CASH BOOK AND OTHERS##################
####################################################################
class Day_End_Desk_Office_Transactions(DateObjectsModels):
    description=models.CharField(max_length=255)
    amount=models.DecimalField(max_digits=20,decimal_places = 2)
    status=models.CharField(max_length=20,choices=TRANSACTION_STATUS,default='UNTREATED')

    # class Meta(DateObjectsModels.Meta):
    #     db_table="Day_End_Sales_Transactions"


class PersonalLedger(DateObjectsModels):
    member=models.ForeignKey(Members,on_delete=models.CASCADE)
    transaction=models.ForeignKey(TransactionTypes,on_delete=models.CASCADE,blank=True,null=True)
    account_number=models.CharField(max_length=255)
    particulars=models.CharField(max_length=255)
    debit=models.DecimalField(max_digits=20,decimal_places = 2,default=0)
    credit=models.DecimalField(max_digits=20,decimal_places = 2,default=0)
    balance=models.DecimalField(max_digits=20,decimal_places = 2,default=0)
    transaction_period=models.DateField()
    status=models.CharField(max_length=20,choices=MEMBERSHIP_STATUS,default='ACTIVE')

    # class Meta(DateObjectsModels.Meta):
    #     db_table="Personal_Ledger"


class PersonalLedgerWithoutBalanceBF(DateObjectsModels):
    member=models.ForeignKey(Members,on_delete=models.CASCADE)
    transaction=models.ForeignKey(TransactionTypes,on_delete=models.CASCADE,blank=True,null=True)
    account_number=models.CharField(max_length=255)
    particulars=models.CharField(max_length=255)
    status=models.CharField(max_length=20,choices=TRANSACTION_STATUS,default='UNTREATED')

    # class Meta(DateObjectsModels.Meta):
    #     db_table="PersonalLedgerWithoutBalanceBF"


class FailedLoanPenaltyRecords(DateObjectsModels):
    # member=models.ForeignKey(Members,on_delete=models.CASCADE)
    transaction=models.ForeignKey(LoansRepaymentBase,on_delete=models.CASCADE)
    amount=models.DecimalField(max_digits=20,decimal_places = 2,default=0)
    penalty=models.DecimalField(max_digits=20,decimal_places = 2,default=0)
    rate=models.DecimalField(max_digits=20,decimal_places = 2,default=0)
    transaction_period=models.DateField(blank=True,null=True)
    loan_date=models.DateField()
    due_date=models.DateField()
    penalty_date=models.DateField()
    status=models.CharField(max_length=20,choices=TRANSACTION_STATUS,default='UNTREATED')

    # class Meta(DateObjectsModels.Meta):
    #     db_table="FailedLoanPenaltyRecords"




class PersonalLedgerManualPosting(DateObjectsModels):
    transaction=models.CharField(max_length=255)
    account_number=models.CharField(max_length=255)
    particulars=models.CharField(max_length=255)
    amount=models.DecimalField(max_digits=20,decimal_places = 2,default=0)
    transaction_type=models.CharField(max_length=20,choices=MANUAL_POSTING_TYPES,default='CREDIT')
    status=models.CharField(max_length=20,choices=TRANSACTION_STATUS,default='UNTREATED')
    sources=models.CharField(max_length=30,default='SAVINGS')
    # class Meta(DateObjectsModels.Meta):
    #     db_table="PersonalLedgerSavingsPosting"


class CashBook_Main(DateObjectsModels):
    particulars=models.CharField(max_length=255)
    debit=models.DecimalField(max_digits=20,decimal_places = 2,default=0)
    credit=models.DecimalField(max_digits=20,decimal_places = 2,default=0)
    balance=models.DecimalField(max_digits=20,decimal_places = 2,default=0)
    ref_no=models.CharField(max_length=255)
    source=models.CharField(max_length=50)
    status=models.CharField(max_length=20,choices=MEMBERSHIP_STATUS,default='ACTIVE')

    # class Meta(DateObjectsModels.Meta):
    #     db_table="CashBook_Main"


class CashBook_Shop(DateObjectsModels):
    particulars=models.CharField(max_length=255)
    debit=models.DecimalField(max_digits=20,decimal_places = 2,default=0)
    credit=models.DecimalField(max_digits=20,decimal_places = 2,default=0)
    balance=models.DecimalField(max_digits=20,decimal_places = 2,default=0)
    ref_no=models.CharField(max_length=255)
    source=models.CharField(max_length=50)
    status=models.CharField(max_length=50,choices=MEMBERSHIP_STATUS,default='ACTIVE')

    # class Meta(DateObjectsModels.Meta):
    #     db_table="CashBook_Shop"




####################################################################
##################### COOPERATIVE SHOP #############################
####################################################################
class Stock(DateObjectsModels):
    category= models.ForeignKey(ProductCategory,on_delete=models.CASCADE,blank=True,null=True)
    code=models.CharField(max_length=255,unique=True)
    item_name=models.CharField(max_length=255)
    details=models.CharField(max_length=255,blank=True,null=True)
    quantity=models.IntegerField(default=0)
    unit_selling_price=models.DecimalField(max_digits=20,decimal_places = 2)
    unit_cost_price=models.DecimalField(max_digits=20,decimal_places = 2,default=0)
    re_order_level=models.IntegerField(default=0)
    no_in_pack=models.IntegerField(default=0)
    lock_status=models.CharField(max_length=20,choices=LOCK_STATUS,default='LOCKED')
    delete_status=models.BooleanField(default=False)
    expiring_date=models.DateField(blank=True,null=True)


    # class Meta(DateObjectsModels.Meta):
    #     db_table="Stock"

    # def __str__(self):
    #     return self.item_name + " " + str(self.quantity)

class Stock_Auction(DateObjectsModels):
    stock= models.ForeignKey(Stock,on_delete=models.CASCADE)
    quantity=models.IntegerField(default=0)
    unit_selling_price=models.DecimalField(max_digits=20,decimal_places = 2)
    expiry_date=models.DateField()
    expiry_date2=models.DateField()
    # status=models.ForeignKey(TransactionStatus,on_delete=models.CASCADE,default=1)


    # class Meta(DateObjectsModels.Meta):
    #     db_table="Auction_Stock

class Stock_History(DateObjectsModels):
    category= models.ForeignKey(ProductCategory,on_delete=models.CASCADE,blank=True,null=True)
    code=models.CharField(max_length=255)
    item_name=models.CharField(max_length=255)
    details=models.CharField(max_length=255,blank=True,null=True)
    quantity=models.IntegerField(default=0)
    unit_cost_price=models.DecimalField(max_digits=20,decimal_places = 2,default=0)
    total=models.DecimalField(max_digits=20,decimal_places = 2)
    sources=models.CharField(max_length=255)



    # class Meta(DateObjectsModels.Meta):
    #     db_table="Stock_History"



class Product_Code(DateObjectsModels):
    code=models.IntegerField(default=0)


class GeneralTicket(DateObjectsModels):
    ticket=models.IntegerField(default=0)


class Members_Credit_Sales_Selected(DateObjectsModels):
    CHOICES=(
        ('MAIN','MAIN'),
        ('AUCTION','AUCTION')
        )
    member=models.ForeignKey(Members,on_delete=models.CASCADE)
    product= models.ForeignKey(Stock,on_delete=models.CASCADE,blank=True,null=True)
    ticket=models.CharField(max_length=255)
    quantity=models.IntegerField(default=0)
    unit_selling_price=models.DecimalField(max_digits=20,decimal_places = 2)
    total=models.DecimalField(max_digits=20,decimal_places = 2)
    status=models.CharField(max_length=20,choices=TRANSACTION_STATUS,default='UNTREATED')
    sources=models.CharField(default='MAIN',max_length=20,choices=CHOICES)

    # class Meta(DateObjectsModels.Meta):
    #     db_table="Members_Credit_Sales_Selected"


class members_credit_sales_analysis(DateObjectsModels):
    trans_code= models.ForeignKey(Members_Credit_Sales_Selected,on_delete=models.CASCADE,blank=True,null=True)
    particulars=models.CharField(max_length=255,blank=True,null=True)
    debit=models.DecimalField(max_digits=20,decimal_places = 2)
    credit=models.DecimalField(max_digits=20,decimal_places = 2)
    status=models.CharField(max_length=20,choices=TRANSACTION_STATUS,default='UNTREATED')


    # class Meta(DateObjectsModels.Meta):
    #     db_table="Members_Credit_Purchase_Analysis"



class members_credit_sales_summary(DateObjectsModels):
    trans_code= models.ForeignKey(Members_Credit_Sales_Selected,on_delete=models.CASCADE,blank=True,null=True)
    amount=models.DecimalField(max_digits=20,decimal_places = 2)
    amount_paid=models.DecimalField(max_digits=20,decimal_places = 2,default=0)
    balance=models.DecimalField(max_digits=20,decimal_places = 2,default=0)
    comment=models.TextField(blank=True,null=True)
    approval_officer=models.CharField(max_length=255,blank=True,null=True)
    approval_status=models.CharField(max_length=30,choices=PROCESSING_STATUS,default='UNPROCESSED')
    approval_comment=models.TextField(blank=True,null=True)
    approval_date=models.DateField(blank=True,null=True)
    net_pay=models.DecimalField(max_digits=20,decimal_places=2,default=0)
    payment_date = models.DateField(blank=False,null=False)
    status=models.CharField(max_length=20,choices=TRANSACTION_STATUS,default='UNTREATED')
    loan_number=models.CharField(max_length=255,blank=True,null=True)
    processing_status=models.CharField(max_length=30,choices=PROCESSING_STATUS,default='UNPROCESSED')

    # class Meta(DateObjectsModels.Meta):
    #     db_table="members_credit_sales_summary"


class members_shop_credit_loans(DateObjectsModels):
    member= models.ForeignKey(Members,on_delete=models.CASCADE,blank=True,null=True)
    account_name= models.ForeignKey(TransactionTypes,on_delete=models.CASCADE,blank=True,null=True)
    loan_number=models.CharField(max_length=255,blank=True,null=True)
    loan_amount=models.DecimalField(max_digits=20,decimal_places = 2)
    amount_paid=models.DecimalField(max_digits=20,decimal_places = 2)
    balance=models.DecimalField(max_digits=20,decimal_places = 2)
    status=models.CharField(max_length=20,choices=TRANSACTION_STATUS,default='UNTREATED')
    schedule_status=models.CharField(max_length=20,choices=LOAN_SCHEDULE_STATUS,default='UNSCHEDULED')


    # class Meta(DateObjectsModels.Meta):
    #     db_table="members_shop_credit_loans"

class members_credit_sales_debt_recovery_after_temp(DateObjectsModels):
    member= models.ForeignKey(Members,on_delete=models.CASCADE,blank=True,null=True)
    loan_number=models.CharField(max_length=255,blank=True,null=True)
    amount_due=models.DecimalField(max_digits=20,decimal_places = 2)
    amount_paid=models.DecimalField(max_digits=20,decimal_places = 2)




class members_credit_loans_Cash_Receipt(DateObjectsModels):
    member= models.ForeignKey(Members,on_delete=models.CASCADE,blank=True,null=True)
    description=models.CharField(max_length=255)
    amount=models.DecimalField(max_digits=20,decimal_places = 2)
    receipt=models.CharField(max_length=50)
    status=models.CharField(max_length=20,choices=TRANSACTION_STATUS,default='UNTREATED')


    # class Meta(DateObjectsModels.Meta):
    #     db_table="members_credit_loans_Cash_Receipt"


class members_credit_loans_Cash_Receipt_Daily_Summary(DateObjectsModels):
    amount=models.DecimalField(max_digits=20,decimal_places = 2)
    cash_book=models.CharField(max_length=50)
    day_end_code=models.CharField(max_length=50,blank=True,null=True)
    status=models.CharField(max_length=20,choices=TRANSACTION_STATUS,default='UNTREATED')


    # class Meta(DateObjectsModels.Meta):
    #     db_table="members_credit_loans_Cash_Receipt"



class members_credit_loans_Cash_Receipt_Day_End_Transaction(DateObjectsModels):
    amount=models.DecimalField(max_digits=20,decimal_places = 2)
    day_end_code=models.CharField(max_length=50)
    month_end_code=models.CharField(max_length=50,blank=True,null=True)
    status=models.CharField(max_length=20,choices=TRANSACTION_STATUS,default='UNTREATED')


    # class Meta(DateObjectsModels.Meta):
    #     db_table="members_credit_loans_Cash_Receipt_Day_End_Transaction"

class members_credit_loans_Cash_Receipt_Day_End(DateObjectsModels):
    amount=models.DecimalField(max_digits=20,decimal_places = 2)
    day_end_code=models.CharField(max_length=50)
    month_end_code=models.CharField(max_length=50,blank=True,null=True)
    status=models.CharField(max_length=20,choices=TRANSACTION_STATUS,default='UNTREATED')


    # class Meta(DateObjectsModels.Meta):
    #     db_table="members_credit_loans_Cash_Receipt_Day_End_Transaction"




class members_credit_loans_Cash_Receipt_Month_End_Transaction(DateObjectsModels):
    amount=models.DecimalField(max_digits=20,decimal_places = 2)
    month_end_code=models.CharField(max_length=50)
    year_end_code=models.CharField(max_length=50,blank=True,null=True)
    status=models.CharField(max_length=20,choices=TRANSACTION_STATUS,default='UNTREATED')


    # class Meta(DateObjectsModels.Meta):
    #     db_table="members_credit_loans_Cash_Receipt_Month_End_Transaction"




class members_credit_loans_Cash_Receipt_Year_End_Transaction(DateObjectsModels):
    amount=models.DecimalField(max_digits=20,decimal_places = 2)
    year_end_code=models.CharField(max_length=50)
    status=models.CharField(max_length=20,choices=TRANSACTION_STATUS,default='UNTREATED')


    # class Meta(DateObjectsModels.Meta):
    #     db_table="members_credit_loans_Cash_Receipt_Month_End_Transaction"



class MonthlyShopdeductionList(DateObjectsModels):
    member=models.ForeignKey(Members,on_delete=models.CASCADE)
    transaction_period=models.DateField(blank=True,null=True)
    transaction=models.ForeignKey(TransactionTypes,on_delete=models.CASCADE)
    account_number=models.CharField(max_length=255,blank=True,null=True)
    amount=models.DecimalField(max_digits=20,decimal_places = 2,default=0)
    amount_deducted=models.DecimalField(max_digits=20,decimal_places = 2,default=0)
    balance=models.DecimalField(max_digits=20,decimal_places = 2,default=0)

    salary_institution=models.ForeignKey(SalaryInstitution,on_delete=models.CASCADE)
    status= models.CharField(max_length=20,choices=TRANSACTION_STATUS,default='UNTREATED')
    processing_status= models.CharField(max_length=20,choices=PROCESSING_STATUS,default='UNPROCESSED')

    # class Meta(DateObjectsModels.Meta):
    #     db_table="MonthlyShopdeductionList"


class MonthlyShopdeductionListGenerated(DateObjectsModels):
    member= models.ForeignKey(Members,on_delete=models.CASCADE,blank=True,null=True)
    coop_amount=models.DecimalField(max_digits=20,decimal_places = 2)
    account_amount=models.DecimalField(max_digits=20,decimal_places = 2)
    balance=models.DecimalField(max_digits=20,decimal_places = 2)
    transaction_period=models.DateField(blank=True,null=True)
    status=models.CharField(max_length=20,choices=TRANSACTION_STATUS,default='UNTREATED')

    salary_institution=models.ForeignKey(SalaryInstitution,on_delete=models.CASCADE)
    processing_status= models.CharField(max_length=20,choices=PROCESSING_STATUS,default='UNPROCESSED')

    # class Meta(DateObjectsModels.Meta):
    #     db_table="members_shop_monthly_deduction"

class MonthlyShopGroupGeneratedTransactions(DateObjectsModels):
    salary_institution=models.ForeignKey(SalaryInstitution,on_delete=models.CASCADE)
    transaction_period=models.DateField(blank=True,null=True)
    transaction=models.ForeignKey(TransactionTypes,on_delete=models.CASCADE)

    transaction_status= models.CharField(max_length=20,choices=TRANSACTION_STATUS,default='UNTREATED')

    # class Meta(DateObjectsModels.Meta):
    #     db_table="MonthlyShopGroupGeneratedTransactions"


class MonthlyJointDeductionList(DateObjectsModels):
    member=models.ForeignKey(Members,on_delete=models.CASCADE)
    transaction_period=models.DateField(blank=True,null=True)
    transaction=models.CharField(max_length=255,blank=True,null=True)
    amount=models.DecimalField(max_digits=20,decimal_places = 2,default=0)
    amount_deducted=models.DecimalField(max_digits=20,decimal_places = 2,default=0)
    balance=models.DecimalField(max_digits=20,decimal_places = 2,default=0)

    salary_institution=models.ForeignKey(SalaryInstitution,on_delete=models.CASCADE)
    status= models.CharField(max_length=20,choices=TRANSACTION_STATUS,default='UNTREATED')
    processing_status= models.CharField(max_length=20,choices=PROCESSING_STATUS,default='UNPROCESSED')

    # class Meta(DateObjectsModels.Meta):
    #     db_table="MonthlyJointDeductionList"



    # class Meta(DateObjectsModels.Meta):
    #     db_table="Monthly_Deduction_List_Generated"

class MonthlyJointDeductionGeneratedTransactions(DateObjectsModels):
    salary_institution=models.ForeignKey(SalaryInstitution,on_delete=models.CASCADE)
    transaction_period=models.DateField(blank=True,null=True)
    transaction=models.CharField(max_length=255)

    transaction_status= models.CharField(max_length=20,choices=TRANSACTION_STATUS,default='UNTREATED')

    # class Meta(DateObjectsModels.Meta):
    #     db_table="MonthlyJointDeductionGeneratedTransactions"

class MonthlyJointDeductionGenerated(DateObjectsModels):
    member=models.ForeignKey(Members,on_delete=models.CASCADE)
    transaction_period=models.DateField(blank=True,null=True)
    amount=models.DecimalField(max_digits=20,decimal_places = 2,default=0)

    amount_deducted=models.DecimalField(max_digits=20,decimal_places = 2,default=0)
    balance=models.DecimalField(max_digits=20,decimal_places = 2,default=0)

    salary_institution=models.ForeignKey(SalaryInstitution,on_delete=models.CASCADE)
    status= models.CharField(max_length=20,choices=TRANSACTION_STATUS,default='UNTREATED')
    processing_status= models.CharField(max_length=20,choices=PROCESSING_STATUS,default='UNPROCESSED')
    verification=models.CharField(max_length=20, choices=YESNO,default='NO')
    # class Meta(DateObjectsModels.Meta):
    #     db_table="MonthlyJointDeductionGenerated"



class NonMemberAccountDeductions(DateObjectsModels):
    salary_institution=models.ForeignKey(SalaryInstitution,on_delete=models.CASCADE)
    transaction_period=models.DateField(blank=True,null=True)
    ippis_no=models.CharField(max_length=255)
    name=models.CharField(max_length=255)
    amount=models.DecimalField(max_digits=20,decimal_places = 2,default=0)
    transaction_status= models.CharField(max_length=20,choices=TRANSACTION_STATUS,default='UNTREATED')

    # class Meta(DateObjectsModels.Meta):
    #     db_table="Non_Member_Account_Deductions"


class WrongfulDeductionTransfer(DateObjectsModels):
    source=models.ForeignKey(NonMemberAccountDeductions,on_delete=models.CASCADE)
    member=models.ForeignKey(Members,on_delete=models.CASCADE)
    amount=models.DecimalField(max_digits=20,decimal_places = 2,default=0)
    amount_posted=models.DecimalField(max_digits=20,decimal_places = 2,default=0)
    balance=models.DecimalField(max_digits=20,decimal_places = 2,default=0)
    transaction_period=models.DateField(blank=True,null=True)
    transaction_status= models.CharField(max_length=20,choices=TRANSACTION_STATUS,default='UNTREATED')

    # class Meta(DateObjectsModels.Meta):
    #     db_table="WrongfulDeductionTransfer"

class MonthlyOverdeductionsRefund(DateObjectsModels):
    member=models.ForeignKey(Members,on_delete=models.CASCADE)
    over_deduction=models.ForeignKey(MonthlyJointDeductionGenerated,on_delete=models.CASCADE)
    channel=models.CharField(max_length=255)
    ref_number=models.CharField(max_length=255,blank=True,null=True)


    # class Meta(DateObjectsModels.Meta):
        #     db_table="Monthly_Over_deductions_Refund"


class Members_Cash_Sales_Selected(DateObjectsModels):
    CHOICES=(
        ('MAIN','MAIN'),
        ('AUCTION','AUCTION')
        )

    member=models.ForeignKey(Members,on_delete=models.CASCADE)
    product= models.ForeignKey(Stock,on_delete=models.CASCADE,blank=True,null=True)
    ticket=models.CharField(max_length=255)
    quantity=models.IntegerField(default=0)
    unit_selling_price=models.DecimalField(max_digits=20,decimal_places = 2)
    total=models.DecimalField(max_digits=20,decimal_places = 2)

    status=models.CharField(max_length=20,choices=TRANSACTION_STATUS,default='UNTREATED')
    sources= models.CharField(default='MAIN',choices=CHOICES,max_length=15)
    submission_status= models.CharField(default='NOT SUBMITTED',choices=SUBMISSION_STATUS,max_length=15)


    # class Meta(DateObjectsModels.Meta):
    #     db_table="Members_Cash_Sales_Selected"


class Customers(DateObjectsModels):
    customer_id=models.CharField(max_length=255,unique=True)
    name=models.CharField(max_length=255,default='Anonymous')
    phone_no=models.CharField(max_length=255,default='Anonymous')
    address=models.CharField(max_length=255,default='Anonymous')
    birthdate=models.DateField(blank=True,null=True)
    status=models.CharField(max_length=20,choices=RECEIPT_STATUS,default='UNUSED')
    cust_status=models.CharField(max_length=20,choices=MEMBERSHIP_STATUS,default='ACTIVE')
    active_ticket=models.CharField(max_length=255,blank=True, null=True)
    ticket_status=models.CharField(max_length=20,choices=TICKET_STATUS,default='OPEN')
    locked_status=models.CharField(max_length=20,choices=LOCK_STATUS,default='LOCKED')


    # class Meta(DateObjectsModels.Meta):
    #     db_table="Customers"


class General_Cash_Sales_Selected(DateObjectsModels):
    CHOICES=(
        ('MAIN','MAIN'),
        ('AUCTION','AUCTION')
        )
    customer=models.ForeignKey(Customers,on_delete=models.CASCADE,blank=True,null=True)
    product= models.ForeignKey(Stock,on_delete=models.CASCADE,blank=True,null=True)
    ticket=models.CharField(max_length=255)
    quantity=models.IntegerField(default=0)
    unit_selling_price=models.DecimalField(max_digits=20,decimal_places = 2)
    total=models.DecimalField(max_digits=20,decimal_places = 2)

    status=models.CharField(max_length=20,choices=TRANSACTION_STATUS,default='UNTREATED')
    sources= models.CharField(default='MAIN',choices=CHOICES,max_length=15)

    # class Meta(DateObjectsModels.Meta):
    #     db_table="General_Cash_Sales_Selected"


class General_Cash_Sales_SelectedTemp(DateObjectsModels):
    customer=models.ForeignKey(Customers,on_delete=models.CASCADE,blank=True,null=True)
    product= models.ForeignKey(Stock,on_delete=models.CASCADE,blank=True,null=True)
    ticket=models.CharField(max_length=255)
    quantity=models.IntegerField(default=0)
    unit_selling_price=models.DecimalField(max_digits=20,decimal_places = 2)
    total=models.DecimalField(max_digits=20,decimal_places = 2)

    status=models.CharField(max_length=20,choices=TRANSACTION_STATUS,default='UNTREATED')

    # class Meta(DateObjectsModels.Meta):
    #     db_table="General_Cash_Sales_Selected_Temp"


class Daily_Sales(DateObjectsModels):
    CHOICES=(
        ('MAIN','MAIN'),
        ('AUCTION','AUCTION')
        )
    ticket=models.CharField(max_length=255)
    name=models.CharField(max_length=255,default='Anonymous')
    phone_no=models.CharField(max_length=255,default='Anonymous')
    address=models.CharField(max_length=255,default='Anonymous')
    product=models.ForeignKey(Stock,on_delete=models.CASCADE,blank=True,null=True)
    sales_category=models.CharField(max_length=30,choices=SALES_CATEGORIES,default="CASH")
    quantity=models.IntegerField(default=0)
    receipt=models.CharField(max_length=20,blank=True,null=True)
    unit_selling_price=models.DecimalField(max_digits=20,decimal_places = 2)
    total=models.DecimalField(max_digits=20,decimal_places = 2)
    status=models.CharField(max_length=20,choices=TRANSACTION_STATUS,default='UNTREATED')
    processing_status=models.CharField(max_length=30,choices=PROCESSING_STATUS,default='UNPROCESSED')

    sources=models.CharField(max_length=20,choices=CHOICES,default='MAIN')
    quantity_returned=models.IntegerField(blank=False,null=False,default=0)
    date_returned = models.DateField(blank=True,null=True)

    # class Meta(DateObjectsModels.Meta):
    #     db_table="Daily_Sales"


class Daily_Sales_Item_Return(DateObjectsModels):
    sales=models.ForeignKey(Daily_Sales,on_delete=models.CASCADE,blank=True,null=True)
    quantity=models.IntegerField(default=0)
    total=models.DecimalField(max_digits=20,decimal_places = 2)
    status=models.CharField(max_length=20,choices=TRANSACTION_STATUS,default="UNTREATED")
    processing_status=models.CharField(max_length=20,choices=PROCESSING_STATUS,default="UNPROCESSED")
    reasons=models.TextField(blank=False,null=False)

    # class Meta(DateObjectsModels.Meta):
    #     db_table="Daily_Sales_Item_Return"


class Daily_Sales_Item_Return_Selection(DateObjectsModels):
    customer=models.ForeignKey(Daily_Sales_Item_Return,on_delete=models.CASCADE,blank=True,null=True)
    product= models.ForeignKey(Stock,on_delete=models.CASCADE,blank=True,null=True)
    quantity=models.IntegerField(default=0)
    unit_selling_price=models.DecimalField(max_digits=20,decimal_places = 2)
    total=models.DecimalField(max_digits=20,decimal_places = 2)
    receipt=models.CharField(max_length=255,blank=True,null=True)
    status=models.CharField(max_length=20,choices=TRANSACTION_STATUS,default='UNTREATED')


    # class Meta(DateObjectsModels.Meta):
    #     db_table="Daily_Sales_Item_Return_Selection"

class Daily_Sales_Item_Return_Summary(DateObjectsModels):
    sale=models.ForeignKey(Daily_Sales_Item_Return_Selection,on_delete=models.CASCADE,blank=True,null=True)
    receipt=models.CharField(max_length=255)
    prev_amount=models.DecimalField(max_digits=20,decimal_places = 2)
    current_amount=models.DecimalField(max_digits=20,decimal_places = 2)
    balance_amount=models.DecimalField(max_digits=20,decimal_places = 2)
    channel=models.CharField(max_length=20,choices=CHANNELS,default='CASH')

    source_bank=models.ForeignKey(Banks,on_delete=models.CASCADE,blank=True,null=True)
    account_name=models.CharField(max_length=150,blank=True,null=True)
    other_details=models.CharField(max_length=255,blank=True,null=True)
    coop_account=models.ForeignKey(CooperativeBankAccounts,on_delete=models.CASCADE,blank=True,null=True)

    submission_status=models.CharField(max_length=50,choices=SUBMISSION_STATUS,default='NOT SUBMITTED')
    status=models.CharField(max_length=20,choices=TRANSACTION_STATUS,default='UNTREATED')
    processing_status=models.CharField(max_length=20,choices=PROCESSING_STATUS,default='UNPROCESSED')


    # class Meta(DateObjectsModels.Meta):
    #     db_table="Daily_Sales_Item_Return_Summary"


class Daily_Sales_Item_Return_Left_Over_Fund(DateObjectsModels):
    sale=models.ForeignKey(Daily_Sales_Item_Return_Summary,on_delete=models.CASCADE,blank=True,null=True)
    amount=models.DecimalField(max_digits=20,decimal_places = 2)
    status=models.CharField(max_length=20,choices=TRANSACTION_STATUS,default="UNTREATED")
    processing_status=models.CharField(max_length=20,choices=PROCESSING_STATUS,default="UNPROCESSED")


    # class Meta(DateObjectsModels.Meta):
    #     db_table="Daily_Sales_Item_Return_Left_Over_Fund"

class Daily_Sales_Item_Return_Cash_Flow_Summary(DateObjectsModels):
    description=models.CharField(max_length=255)
    prev_amount=models.DecimalField(max_digits=20,decimal_places = 2,default=0)
    current_amount=models.DecimalField(max_digits=20,decimal_places = 2,default=0)
    postive_balance=models.DecimalField(max_digits=20,decimal_places = 2,default=0)
    negative_balance=models.DecimalField(max_digits=20,decimal_places = 2,default=0)
    status=models.CharField(max_length=30,choices=TRANSACTION_STATUS,default="UNTREATED")
    cash_book=models.CharField(max_length=50,blank=True,null=True)

    # class Meta(DateObjectsModels.Meta):
    #     db_table="Daily_Sales_Item_Return_Cash_Flow_Summary"

class Daily_Sales_Item_Return_Day_End_Transaction(DateObjectsModels):
    description=models.CharField(max_length=255)
    prev_amount=models.DecimalField(max_digits=20,decimal_places = 2,default=0)
    current_amount=models.DecimalField(max_digits=20,decimal_places = 2,default=0)
    postive_balance=models.DecimalField(max_digits=20,decimal_places = 2,default=0)
    negative_balance=models.DecimalField(max_digits=20,decimal_places = 2,default=0)
    status=models.CharField(max_length=30,choices=TRANSACTION_STATUS,default="UNTREATED")
    cash_book=models.CharField(max_length=50)
    month_key=models.CharField(max_length=50,blank=True,null=True)

    # class Meta(DateObjectsModels.Meta):
    #     db_table="Daily_Sales_Item_Return_Day_End_Transaction"

class Daily_Sales_Item_Return_Month_End_Transaction(DateObjectsModels):
    description=models.CharField(max_length=255)
    prev_amount=models.DecimalField(max_digits=20,decimal_places = 2,default=0)
    current_amount=models.DecimalField(max_digits=20,decimal_places = 2,default=0)
    postive_balance=models.DecimalField(max_digits=20,decimal_places = 2,default=0)
    negative_balance=models.DecimalField(max_digits=20,decimal_places = 2,default=0)
    status=models.CharField(max_length=30,choices=TRANSACTION_STATUS,default="UNTREATED")
    month_key=models.CharField(max_length=50)
    year_key=models.CharField(max_length=50,blank=True,null=True)

    # class Meta(DateObjectsModels.Meta):
    #     db_table="Daily_Sales_Item_Return_Month_End_Transaction"

class Daily_Sales_Item_Return_Year_End_Transaction(DateObjectsModels):
    description=models.CharField(max_length=255)
    prev_amount=models.DecimalField(max_digits=20,decimal_places = 2,default=0)
    current_amount=models.DecimalField(max_digits=20,decimal_places = 2,default=0)
    postive_balance=models.DecimalField(max_digits=20,decimal_places = 2,default=0)
    negative_balance=models.DecimalField(max_digits=20,decimal_places = 2,default=0)
    status=models.CharField(max_length=30,choices=TRANSACTION_STATUS,default="UNTREATED")
    year_key=models.CharField(max_length=50)

    # class Meta(DateObjectsModels.Meta):
    #     db_table="Daily_Sales_Item_Return_Year_End_Transaction"


class Daily_Sales_Summary(DateObjectsModels):
    sale=models.ForeignKey(Daily_Sales,on_delete=models.CASCADE,blank=True,null=True)
    receipt=models.CharField(max_length=255)
    ticket=models.CharField(max_length=255)
    amount=models.DecimalField(max_digits=20,decimal_places = 2)
    cash=models.DecimalField(max_digits=20,decimal_places = 2,default=0)
    pos=models.DecimalField(max_digits=20,decimal_places = 2,default=0)
    transfer=models.DecimalField(max_digits=20,decimal_places = 2,default=0)
    source_bank=models.ForeignKey(Banks,on_delete=models.CASCADE,blank=True,null=True)
    account_name=models.CharField(max_length=150,blank=True,null=True)
    other_details=models.CharField(max_length=255,blank=True,null=True)
    coop_account=models.ForeignKey(CooperativeBankAccounts,on_delete=models.CASCADE,blank=True,null=True)
    submission_status=models.CharField(max_length=50,choices=SUBMISSION_STATUS,default='NOT SUBMITTED')
    status=models.CharField(max_length=20,choices=TRANSACTION_STATUS,default='UNTREATED')
    processing_status=models.CharField(max_length=30,choices=PROCESSING_STATUS,default='UNPROCESSED')

    # class Meta(DateObjectsModels.Meta):
    #     db_table="Daily_Sales_Summary"


class Daily_Sales_Cash_Flow_Summary(DateObjectsModels):
    description=models.CharField(max_length=255)
    amount=models.DecimalField(max_digits=20,decimal_places = 2)
    sales_category=models.CharField(max_length=50,choices=SALES_CATEGORIES,default=1)
    status=models.CharField(max_length=20,choices=TRANSACTION_STATUS,default='UNTREATED')
    cash_book=models.CharField(max_length=50,blank=True,null=True)

    # class Meta(DateObjectsModels.Meta):
    #     db_table="Daily_Sales_Cash_Flow_Summary"


class Day_End_Sales_Transactions(DateObjectsModels):
    description=models.CharField(max_length=255)
    amount=models.DecimalField(max_digits=20,decimal_places = 2)
    sales_category=models.CharField(max_length=30,choices=SALES_CATEGORIES,default="CASH")
    cash_book=models.CharField(max_length=50,blank=True,null=True)
    month_key=models.CharField(max_length=50,blank=True,null=True)
    status=models.CharField(max_length=20,choices=TRANSACTION_STATUS,default='UNTREATED')

    # class Meta(DateObjectsModels.Meta):
    #     db_table="Day_End_Sales_Transactions"


class Month_End_Sales_Transactions(DateObjectsModels):
    description=models.CharField(max_length=255)
    amount=models.DecimalField(max_digits=20,decimal_places = 2)
    sales_category=models.CharField(max_length=30,choices=SALES_CATEGORIES,default="CASH")
    month_key=models.CharField(max_length=50)
    year_key=models.CharField(max_length=50,blank=True,null=True)
    status=models.CharField(max_length=20,choices=TRANSACTION_STATUS,default='UNTREATED')


    # class Meta(DateObjectsModels.Meta):
    #     db_table="Month_End_Sales_Transactions"

class Year_End_Sales_Transactions(DateObjectsModels):
    description=models.CharField(max_length=255)
    amount=models.DecimalField(max_digits=20,decimal_places = 2)
    sales_category=models.CharField(max_length=30,choices=SALES_CATEGORIES,default="CASH")
    year_key=models.CharField(max_length=50)
    status=models.CharField(max_length=20,choices=TRANSACTION_STATUS,default='UNTREATED')

    # class Meta(DateObjectsModels.Meta):
    #     db_table="Month_End_Sales_Transactions"


class Daily_Cash_Deposit_Summary(DateObjectsModels):
    description=models.CharField(max_length=255)
    amount=models.DecimalField(max_digits=20,decimal_places = 2)
    cash_book=models.CharField(max_length=50,blank=True,null=True)
    status=models.CharField(max_length=20,choices=TRANSACTION_STATUS,default='UNTREATED')

    # class Meta(DateObjectsModels.Meta):
    #     db_table="Daily_Cash_Deposit_Summary"


class Daily_Cash_Deposit_Day_End_Transaction(DateObjectsModels):
    description=models.CharField(max_length=255)
    amount=models.DecimalField(max_digits=20,decimal_places = 2)
    cash_book=models.CharField(max_length=50)
    month_end_code=models.CharField(max_length=50,blank=True,null=True)
    status=models.CharField(max_length=20,choices=TRANSACTION_STATUS,default='UNTREATED')

    # class Meta(DateObjectsModels.Meta):
    #     db_table="Daily_Cash_Deposit_Day_End_Transaction"


class Daily_Cash_Deposit_Month_End_Transaction(DateObjectsModels):
    description=models.CharField(max_length=255)
    amount=models.DecimalField(max_digits=20,decimal_places = 2)
    month_end_code=models.CharField(max_length=50)
    year_end_code=models.CharField(max_length=50,blank=True,null=True)

    status=models.CharField(max_length=20,choices=TRANSACTION_STATUS,default='UNTREATED')

    # class Meta(DateObjectsModels.Meta):
    #     db_table="Daily_Cash_Deposit_Day_End_Transaction"

class Daily_Cash_Deposit_Year_End_Transaction(DateObjectsModels):
    description=models.CharField(max_length=255)
    amount=models.DecimalField(max_digits=20,decimal_places = 2)
    year_end_code=models.CharField(max_length=50)
    status=models.CharField(max_length=20,choices=TRANSACTION_STATUS,default='UNTREATED')

    # class Meta(DateObjectsModels.Meta):
    #     db_table="Daily_Cash_Deposit_Day_End_Transaction"



class Suppliers(DateObjectsModels):
    prefix=models.CharField(max_length=255,blank=True,null=True)
    name=models.CharField(max_length=255)

    # class Meta(DateObjectsModels.Meta):
    #     db_table="Suppliers"


class Suppliers_Branches(DateObjectsModels):
    supplier= models.ForeignKey(Suppliers,on_delete=models.CASCADE)
    address=models.TextField()
    phone=models.CharField(max_length=255)

    # class Meta(DateObjectsModels.Meta):
    #     db_table="Suppliers_Branches"


class Suppliers_Reps(DateObjectsModels):
    suppliers= models.ForeignKey(Suppliers,on_delete=models.CASCADE)
    name=models.CharField(max_length=255)
    phone=models.CharField(max_length=255)

    # class Meta(DateObjectsModels.Meta):
    #     db_table="Suppliers_Reps"


class Suppliers_Majors(DateObjectsModels):
    supplier= models.ForeignKey(Suppliers,on_delete=models.CASCADE)
    product=models.CharField(max_length=255)

    # class Meta(DateObjectsModels.Meta):
    #     db_table="Suppliers_Majors"


class Purchase_Header(DateObjectsModels):
    branch= models.ForeignKey(Suppliers_Branches,on_delete=models.CASCADE)
    total_amount= models.DecimalField(max_digits=20,decimal_places = 2,default=0)
    invoice=models.CharField(max_length=255)
    invoice_date=models.DateField()
    personnel=models.ForeignKey(Suppliers_Reps,on_delete=models.CASCADE,blank=True,null=True)
    status=models.CharField(max_length=20,choices=TRANSACTION_STATUS,default='UNTREATED')
    approval_status=models.CharField(max_length=30,choices=PROCESSING_STATUS,default='UNPROCESSED')


    # class Meta(DateObjectsModels.Meta):
    #     db_table="Purchase_Header"


class Purchases_Temp(DateObjectsModels):
    purchase= models.ForeignKey(Purchase_Header,on_delete=models.CASCADE)
    product= models.ForeignKey(Stock,on_delete=models.CASCADE)
    quantity=models.IntegerField(default=0)
    cost_price =models.DecimalField(max_digits=20,decimal_places = 2,default=0)
    total_cost= models.DecimalField(max_digits=20,decimal_places = 2,default=0)
    selling_price =models.DecimalField(max_digits=20,decimal_places = 2,default=0)



    # class Meta(DateObjectsModels.Meta):
    #     db_table="Purchase_Temp"


class Purchases(DateObjectsModels):
    purchase= models.ForeignKey(Purchase_Header,on_delete=models.CASCADE)
    product= models.ForeignKey(Stock,on_delete=models.CASCADE)
    quantity=models.IntegerField(default=0)
    cost_price =models.DecimalField(max_digits=20,decimal_places = 2,default=0)
    total_cost= models.DecimalField(max_digits=20,decimal_places = 2,default=0)
    selling_price =models.DecimalField(max_digits=20,decimal_places = 2,default=0)
    cash_book=models.CharField(max_length=50,blank=True,null=True)
    status=models.CharField(max_length=20,choices=TRANSACTION_STATUS,default='UNTREATED')


    # class Meta(DateObjectsModels.Meta):
    #     db_table="Purchases"

class Purchases_Day_End_Transaction(DateObjectsModels):
    quantity=models.IntegerField(default=0)
    total_cost= models.DecimalField(max_digits=20,decimal_places = 2,default=0)
    cash_book=models.CharField(max_length=50)
    month_key=models.CharField(max_length=50,blank=True,null=True)
    status=models.CharField(max_length=20,choices=TRANSACTION_STATUS,default='UNTREATED')


    # class Meta(DateObjectsModels.Meta):
    #     db_table="Purchases_Day_End_Transaction"

class Purchases_Month_End_Transaction(DateObjectsModels):
    quantity=models.IntegerField(default=0)
    total_cost= models.DecimalField(max_digits=20,decimal_places = 2,default=0)
    month_key=models.CharField(max_length=50)
    year_key=models.CharField(max_length=50,blank=True,null=True)
    status=models.CharField(max_length=20,choices=TRANSACTION_STATUS,default='UNTREATED')


    # class Meta(DateObjectsModels.Meta):
    #     db_table="Purchases_Month_End_Transaction"


class Purchases_Year_End_Transaction(DateObjectsModels):
    quantity=models.IntegerField(default=0)
    total_cost= models.DecimalField(max_digits=20,decimal_places = 2,default=0)
    year_key=models.CharField(max_length=50)
    status=models.CharField(max_length=20,choices=TRANSACTION_STATUS,default='UNTREATED')


    # class Meta(DateObjectsModels.Meta):
    #     db_table="Purchases_Year_End_Transaction"



class ItemWriteOffTemp(DateObjectsModels):
    CHOICES=(
        ('MAIN','MAIN'),
        ('AUCTION','AUCTION')
        )
    product= models.ForeignKey(Stock,on_delete=models.CASCADE)
    reason= models.ForeignKey(ItemWriteOffReasons,on_delete=models.CASCADE)
    quantity=models.IntegerField(default=0)
    cost_price =models.DecimalField(max_digits=20,decimal_places = 2,default=0)
    total_cost= models.DecimalField(max_digits=20,decimal_places = 2,default=0)
    approval_status=models.CharField(max_length=20,choices=APPROVAL_STATUS,default="PENDING")
    details=models.TextField()
    expiry_date=models.DateField(blank=True,null=True)
    status=models.CharField(max_length=20,choices=TRANSACTION_STATUS,default="UNTREATED")
    route=models.CharField(default='MAIN',choices=CHOICES,max_length=15)
    transaction_key=models.CharField(max_length=50,blank=True,null=True)

    # class Meta(DateObjectsModels.Meta):
    #     db_table="Item_Write_Off_Temp"



class ItemWriteOff(DateObjectsModels):
    product= models.ForeignKey(ItemWriteOffTemp,on_delete=models.CASCADE)
    status=models.CharField(max_length=20,choices=TRANSACTION_STATUS,default="UNTREATED")

    # class Meta(DateObjectsModels.Meta):
    #     db_table="Item_Write_Off"



class Daily_Item_Write_Off_Summary(DateObjectsModels):
    description=models.CharField(max_length=255)
    quantity=models.IntegerField(default=0)
    amount=models.DecimalField(max_digits=20,decimal_places = 2)
    status=models.CharField(max_length=20,choices=TRANSACTION_STATUS,default='UNTREATED')
    cash_book=models.CharField(max_length=50,blank=True,null=True)

    # class Meta(DateObjectsModels.Meta):
    #     db_table="Daily_Item_Write_Off_Summary"


class Item_Write_Off_Day_End_Transactions(DateObjectsModels):
    quantity=models.IntegerField(default=0)
    amount=models.DecimalField(max_digits=20,decimal_places = 2)
    status=models.CharField(max_length=20,choices=TRANSACTION_STATUS,default='UNTREATED')
    cash_book=models.CharField(max_length=50)
    month_key=models.CharField(max_length=50,blank=True,null=True)


    # class Meta(DateObjectsModels.Meta):
    #     db_table="Daily_Item_Write_Off_Day_End_Transactions"


class Item_Write_Off_Month_End_Transactions(DateObjectsModels):
    quantity=models.IntegerField(default=0)
    amount=models.DecimalField(max_digits=20,decimal_places = 2)
    status=models.CharField(max_length=20,choices=TRANSACTION_STATUS,default='UNTREATED')
    month_key=models.CharField(max_length=50,blank=True,null=True)
    year_key=models.CharField(max_length=50,blank=True,null=True)

    # class Meta(DateObjectsModels.Meta):
    #     db_table="Item_Write_Off_Month_End_Transactions"


class Item_Write_Off_Year_End_Transactions(DateObjectsModels):
    quantity=models.IntegerField(default=0)
    amount=models.DecimalField(max_digits=20,decimal_places = 2)
    status=models.CharField(max_length=20,choices=TRANSACTION_STATUS,default='UNTREATED')
    year_key=models.CharField(max_length=50,blank=True,null=True)


    # class Meta(DateObjectsModels.Meta):
    #     db_table="Item_Write_Off_Year_End_Transactions"


class Expenditures(DateObjectsModels):
    details=models.TextField()
    amount =models.DecimalField(max_digits=20,decimal_places = 2,default=0)
    reference=models.CharField(max_length=100)
    status=models.CharField(default='UNTREATED',choices=TRANSACTION_STATUS,max_length=15)
    summary_code=models.CharField(max_length=20,blank=True,null=True)

    # class Meta(DateObjectsModels.Meta):
    #     db_table="Expenditures"


class Expenditures_Dialy_Summary(DateObjectsModels):
    amount =models.DecimalField(max_digits=20,decimal_places = 2,default=0)
    summary_code=models.CharField(max_length=20)
    status=models.CharField(default='UNTREATED',choices=TRANSACTION_STATUS,max_length=15)
    day_end_code=models.CharField(max_length=20)

    # class Meta(DateObjectsModels.Meta):
    #     db_table="Expenditures_Dialy_Summary"


class Expenditures_Day_End_Summary(DateObjectsModels):
    amount =models.DecimalField(max_digits=20,decimal_places = 2,default=0)
    status=models.CharField(default='UNTREATED',choices=TRANSACTION_STATUS,max_length=15)
    day_end_code=models.CharField(max_length=20)
    month_end_code=models.CharField(max_length=20,blank=True,null=True)

    # class Meta(DateObjectsModels.Meta):
    #     db_table="Expenditures_Day_End_Summary"

class Expenditures_Month_End_Summary(DateObjectsModels):
    amount =models.DecimalField(max_digits=20,decimal_places = 2,default=0)
    status=models.CharField(default='UNTREATED',choices=TRANSACTION_STATUS,max_length=15)
    month_end_code=models.CharField(max_length=20)
    year_end_code=models.CharField(max_length=20,blank=True,null=True)

    # class Meta(DateObjectsModels.Meta):
    #     db_table="Expenditures_Month_End_Summary"


class Expenditures_Year_End_Summary(DateObjectsModels):
    amount =models.DecimalField(max_digits=20,decimal_places = 2,default=0)
    status=models.CharField(default='UNTREATED',choices=TRANSACTION_STATUS,max_length=15)

    year_end_code=models.CharField(max_length=20)

    # class Meta(DateObjectsModels.Meta):
    #     db_table="Expenditures_Month_End_Summary"



class CooperativeShopLedger(DateObjectsModels):
    member= models.ForeignKey(Members,on_delete=models.CASCADE)
    account_number=models.CharField(max_length=255,blank=True,null=True)
    particulars=models.CharField(max_length=255)
    debit=models.DecimalField(max_digits=20,decimal_places = 2)
    credit=models.DecimalField(max_digits=20,decimal_places = 2)
    balance=models.DecimalField(max_digits=20,decimal_places = 2)
    receipt = models.CharField(max_length=20,blank=True, null=True)
    status= models.CharField(max_length=20,choices=TRANSACTION_STATUS,default='UNTREATED')

    # class Meta(DateObjectsModels.Meta):
    #     db_table="Cooperative_Shop_Ledger"


class Cooperative_Shop_Cash_Deposit(DateObjectsModels):
    member= models.ForeignKey(Members,on_delete=models.CASCADE,blank=True,null=True)
    bank= models.ForeignKey(Banks,on_delete=models.CASCADE,blank=True,null=True)
    narrations=models.CharField(max_length=255,blank=True,null=True)
    coop_account=models.ForeignKey(CooperativeBankAccounts,on_delete=models.CASCADE,blank=True,null=True)
    payment_reference=models.CharField(max_length=255,blank=True,null=True)
    amount_paid=models.DecimalField(max_digits=20,decimal_places = 2)
    amount_distributed=models.DecimalField(max_digits=20,decimal_places = 2)
    amount_balance=models.DecimalField(max_digits=20,decimal_places = 2)
    receipt = models.CharField(max_length=20,blank=True, null=True)
    status= models.CharField(max_length=20,choices=MEMBERSHIP_STATUS,default='ACTIVE')
    status2= models.CharField(default='UNTREATED',choices=TRANSACTION_STATUS,max_length=15)
    processing_status= models.CharField(max_length=20,choices=PROCESSING_STATUS,default='UNPROCESSED')

    # class Meta(DateObjectsModels.Meta):
    #     db_table="Cooperative_Shop_Cash_Deposit"


class Cooperative_Shop_Cash_Deposit_Distributions(DateObjectsModels):
    member= models.ForeignKey(Members,on_delete=models.CASCADE,blank=True,null=True)
    loan_number=models.CharField(max_length=50)
    amount_due=models.DecimalField(max_digits=20,decimal_places = 2)
    amount_distributed=models.DecimalField(max_digits=20,decimal_places = 2)
    receipt=models.ForeignKey(Cooperative_Shop_Cash_Deposit,on_delete=models.CASCADE)
    source=models.CharField(max_length=20,default="FIRST")
    status= models.CharField(max_length=20,choices=TRANSACTION_STATUS,default='UNTREATED')

    # class Meta(DateObjectsModels.Meta):
    #     db_table="Cooperative_Shop_Cash_Deposit_Distributions"



class RentalMainCategories(DateObjectsModels):
    description=models.TextField()


    # class Meta(DateObjectsModels.Meta):
    #     db_table="RentalMainCategories"


class RentalProducts(DateObjectsModels):
    description=models.TextField()


    # class Meta(DateObjectsModels.Meta):
    #     db_table="RentalSubCategories"

class RentalPriceSettings(DateObjectsModels):
    main_category=models.ForeignKey(RentalMainCategories,on_delete=models.CASCADE)
    products=models.ForeignKey(RentalProducts,on_delete=models.CASCADE)
    amount=models.DecimalField(max_digits=20,decimal_places = 2)
    status = models.CharField(max_length=10,choices=MEMBERSHIP_STATUS,default='ACTIVE')


    # class Meta(DateObjectsModels.Meta):
    #     db_table="RentalPriceSettings"

class RentalBookingHeaders(DateObjectsModels):
    category=models.ForeignKey(RentalMainCategories,on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    address=models.CharField(max_length=100,blank=True,null=True)
    phone_no=models.CharField(max_length=11,blank=True,null=True)
    status = models.CharField(max_length=10,choices=TRANSACTION_STATUS,default='UNTREATED')
    processing_status=models.CharField(max_length=20,choices=PROCESSING_STATUS,default='UNPROCESSED')


    # class Meta(DateObjectsModels.Meta):
    #     db_table="RentalBookingHeaders"


class RentalBookingSelections(DateObjectsModels):
    contact=models.ForeignKey(RentalBookingHeaders,on_delete=models.CASCADE)
    service=models.ForeignKey(RentalPriceSettings,on_delete=models.CASCADE)
    amount=models.DecimalField(max_digits=20,decimal_places = 2)
    booked_date=models.DateField()
    start_time=models.CharField(max_length=30)
    stop_time=models.CharField(max_length=30)
    status = models.CharField(max_length=10,choices=TRANSACTION_STATUS,default='UNTREATED')


    # class Meta(DateObjectsModels.Meta):
    #     db_table="RentalBookingHeaders"


class RentalBookingSelectionsSummary(DateObjectsModels):
    contact=models.ForeignKey(RentalBookingHeaders,on_delete=models.CASCADE)
    amount=models.DecimalField(max_digits=20,decimal_places=2)
    discount=models.DecimalField(max_digits=20,decimal_places=2)
    net_pay=models.DecimalField(max_digits=20,decimal_places=2,default=0)
    amount_paid=models.DecimalField(max_digits=20,decimal_places=2,default=0)
    balance=models.DecimalField(max_digits=20,decimal_places=2,default=0)
    status = models.CharField(max_length=10,choices=TRANSACTION_STATUS,default='UNTREATED')


    # class Meta(DateObjectsModels.Meta):
    #     db_table="RentalBookingSelectionsSummary"


class RentalBookingSelectionsPayment(DateObjectsModels):
    contact=models.ForeignKey(RentalBookingHeaders,on_delete=models.CASCADE)
    amount=models.DecimalField(max_digits=20,decimal_places = 2)
    receipt=models.CharField(max_length=30,blank=True,null=True)
    status = models.CharField(max_length=10,choices=TRANSACTION_STATUS,default='UNTREATED')


    # class Meta(DateObjectsModels.Meta):
    #     db_table="RentalBookingSelectionsSummary"



class TaskManager(DateObjectsModels):
    description=models.TextField()

    # class Meta(DateObjectsModels.Meta):
    #     db_table="Task_Manager"



class ReportHeader(DateObjectsModels):
    line1=models.CharField(max_length=100)
    line2=models.CharField(max_length=100)
    line3=models.CharField(max_length=100)
    line4=models.CharField(max_length=100)

    # class Meta(DateObjectsModels.Meta):
    #     db_table="ReportHeader"

class ReportFooter(DateObjectsModels):
    code=models.CharField(max_length=100)
    note=models.CharField(max_length=100)


    # class Meta(DateObjectsModels.Meta):
    #     db_table="ReportFooter"



@receiver(post_save,sender=CustomUser)
def create_user_profile(sender,instance,created,**kwargs):
    if created:
        if instance.user_type==1:
            AdminMASTER.objects.create(admin=instance)
        if instance.user_type==2:
            Staff.objects.create(admin=instance,middle_name="",address="",phone_number="080",gender=Gender.objects.first(),status="ACTIVE")
        if instance.user_type==3:
            Staff.objects.create(admin=instance,middle_name="",address="",phone_number="080",gender=Gender.objects.first(),status="ACTIVE")
            # Desk_Office_Tasks.objects.create(user=instance)
        if instance.user_type==4:
             Staff.objects.create(admin=instance,middle_name="",address="",phone_number="080",gender=Gender.objects.first(),status="ACTIVE")
        if instance.user_type==5:
            Members.objects.create(admin=instance,member_id="",date_joined="2020-01-01",
                                    middle_name="",phone_number="",
                                    salary_institution=SalaryInstitution.objects.first(),
                                    applicant=MemberShipFormSalesRecord.objects.first(),
                                    file_no="",permanent_home_address="",residential_address="",
                                    profile_pic="",status="PENDING",
                                    savings_status="PENDING",
                                    loan_status="PENDING",
                                    shares_status="PENDING",
                                    welfare_status="PENDING",
                                    date_joined_status="PENDING"
                                    )


    class Meta(DateObjectsModels.Meta):
        db_table="Create_User_Profile"


@receiver(post_save,sender=CustomUser)
def save_user_profile(sender,instance,**kwargs):
    if instance.user_type==1:
        instance.adminmaster.save()
    if instance.user_type==2:
        instance.staff.save()
    if instance.user_type==3:
        instance.staff.save()
        # instance.desk_office_tasks.save()
    if instance.user_type==4:
        instance.staff.save()
    if instance.user_type==5:
        instance.members.save()

    class Meta(DateObjectsModels.Meta):
        db_table="Save_User_Profile"
