# Create your models here.
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.validators import MaxValueValidator, MinValueValidator

# models.PositiveSmallIntegerField(validators=[MinValueValidator(1)])

# Create your models here.


class CustomUser(AbstractUser):
    user_type_data=((1,"MASTER"),(2,"President") ,(3,"Secretary"),(4,"Treasurer"),(5,"FinSec"),(6,"DeskOfficer"),(7,"SEO"),(8,"SHOP"),(9,"Auditor"),(10,'Members'))
    user_type=models.CharField(default=1,choices=user_type_data,max_length=15)

    class Meta:
      db_table="customuser"

class AdminMASTER(models.Model):
    id=models.AutoField(primary_key=True)
    admin=models.OneToOneField(CustomUser,on_delete=models.CASCADE,blank=True,null=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    objects=models.Manager()

    class Meta:
      db_table="admin_master"

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
    
    class Meta:
        db_table = "usertype"


    def __str__(self):
        return self.title
    

# class UserLevels(titleBase):
#     def __str__(self):
#         return self.title


###########################################################
############# Status ######################################
###########################################################


class ItemWriteOffReasons(titleBase):

    class Meta(titleBase.Meta):
        db_table="item_write_off_reasons"
        ordering = ['title']

    def __str__(self):
        return self.title


class MembershipStatus(titleBase):

    class Meta(titleBase.Meta):
        db_table="membership_status"
        ordering = ['title']

    def __str__(self):
        return self.title


class LoanCategory(titleBase):

    class Meta(titleBase.Meta):
        db_table ='Loan_Category'
        ordering = ['title']

    def __str__(self):
        return self.title


class LoanScheduleStatus(titleBase):

    class Meta(titleBase.Meta):
        db_table ='Loan_Schedule_Status'
        ordering = ['title']

    def __str__(self):
        return self.title


class ProcessingStatus(titleBase):

    class Meta(titleBase.Meta):
        db_table="Processing_Status"
        ordering = ['title']

    def __str__(self):
        return self.title


class CertificationStatus(titleBase):

    class Meta(titleBase.Meta):
        db_table="Certification_Status"
        ordering = ['title']

    def __str__(self):
        return self.title


class ApprovalStatus(titleBase):

    class Meta(titleBase.Meta):
        db_table="Approval_Status"
        ordering = ['title']

    def __str__(self):
        return self.title


class TransactionStatus(titleBase):

    class Meta(titleBase.Meta):
        db_table="Transaction_Status"
        ordering = ['title']

    def __str__(self):
        return self.title



class SubmissionStatus(titleBase):

    class Meta(titleBase.Meta):
        db_table="Submission_Status"
        ordering = ['title']

    def __str__(self):
        return self.title


class ExclusiveStatus(titleBase):

    class Meta(titleBase.Meta):
        db_table="Exclusive_Status"
        ordering = ['title']

    def __str__(self):
        return self.title

class WithdrawalStatus(titleBase):

    class Meta(titleBase.Meta):
        db_table="Withdrawal_Status"
        ordering = ['title']

    def __str__(self):
        return self.title


class LockedStatus(titleBase):

    class Meta(titleBase.Meta):
        db_table="Locked_Status"
        ordering = ['title']


    def __str__(self):
        return self.title



class SavingsUploadStatus(titleBase):
    class Meta(titleBase.Meta):
        db_table="Savings_Upload_Status"
        ordering = ['title']


    def __str__(self):
        return self.title


class SharesUploadStatus(titleBase):
    class Meta(titleBase.Meta):
        db_table="Shares_Upload_Status"
        ordering = ['title']

    def __str__(self):
        return self.title


class WelfareUploadStatus(titleBase):
    class Meta(titleBase.Meta):
        db_table="Welfare_Upload_Status"
        ordering = ['title']


    def __str__(self):
        return self.title


class DateJoinedUploadStatus(titleBase):
    class Meta(titleBase.Meta):
        db_table="Datejoined_Upload_Status"
        ordering = ['title']


    def __str__(self):
        return self.title



class LoansUploadStatus(titleBase):
    class Meta(titleBase.Meta):
        db_table="Loan_Upload_Status"
        ordering = ['title']


    def __str__(self):
        return self.title


class ReceiptStatus(titleBase):
    class Meta(titleBase.Meta):
        db_table="Receipt_Status"
        ordering = ['title']


    def __str__(self):
        return self.title



class SalesCategory(titleBase):
    class Meta(titleBase.Meta):
        db_table="Sales_Category"
        ordering = ['title']


    def __str__(self):
        return self.title


class Titles(titleBase):
    class Meta(titleBase.Meta):
        db_table="Titles"
        ordering = ['title']


    def __str__(self):
        return self.title


class Gender(titleBase):
    class Meta(titleBase.Meta):
        db_table="Gender"
        ordering = ['title']


    def __str__(self):
        return self.title


class Banks(titleBase):
    class Meta(titleBase.Meta):
        db_table="Banks"
        ordering = ['title']


    def __str__(self):
        return self.title
    
 
class PaymentChannels(titleBase):
    class Meta(titleBase.Meta):
        db_table="Payment_Channels"
        ordering = ['title']

    def __str__(self):
        return self.title
    
  
class ReceiptTypes(titleBase):
    class Meta(titleBase.Meta):
        db_table="Receipt_Types"
        ordering = ['title']


    def __str__(self):
        return self.title
    
 
class Locations(titleBase):
    class Meta(titleBase.Meta):
        db_table='Locations'
        ordering = ['title']


    def __str__(self):
        return self.title

  
class AccountTypes(titleBase):
    class Meta(titleBase.Meta):
        db_table="Account_Types"
        ordering = ['title']

    def __str__(self):
        return self.title

class Departments(titleBase):
    class Meta(titleBase.Meta):
        db_table="Departments"
        ordering = ['title']


    def __str__(self):
        return self.title


class SalaryInstitution(titleBase):
    class Meta(titleBase.Meta):
        db_table="Salary_Institution"
        ordering = ['title']


    def __str__(self):
        return self.title


class TicketStatus(titleBase):
    class Meta(titleBase.Meta):
        db_table="Ticket_Status"
        ordering = ['title']


    def __str__(self):
        return self.title


class TransactionSources(titleBase):
    class Meta(titleBase.Meta):
        db_table="Transaction_Sources"
        ordering = ['title']


    def __str__(self):
        return self.title


class MultipleLoanStatus(titleBase):
    class Meta(titleBase.Meta):
        db_table="Multiple_Loan_Status"
        ordering = ['title']


    def __str__(self):
        return self.title


class LoanMergeStatus(titleBase):
    class Meta(titleBase.Meta):
        db_table="Loan_Merge_Status"
        ordering = ['title']


    def __str__(self):
        return self.title


class UsersLevel(titleBase):
    class Meta(titleBase.Meta):
        db_table="Users_level"
        ordering = ['title']


    def __str__(self):
        return self.title


class InterestDeductionSource(titleBase):
    class Meta(titleBase.Meta):
        db_table="Interest_Deduction_Source"
        ordering = ['title']


    def __str__(self):
        return self.title


class States(titleBase):
    class Meta(titleBase.Meta):
        db_table="States"
        ordering = ['title']


    def __str__(self):
        return self.title


class NOKRelationships(titleBase):
    class Meta(titleBase.Meta):
        db_table="NOK_Relationships"
        ordering = ['title']

    def __str__(self):
        return self.title

class ProductCategory(titleBase):
    code= models.CharField(max_length=255,unique=True)
    class Meta(titleBase.Meta):
        db_table="Product_Category"
        ordering = ['title']


    def __str__(self):
        return self.title


class AdminCharges(titleBase):
    class Meta(titleBase.Meta):
        db_table="admin_Charges"
        ordering = ['title']


    def __str__(self):
        return self.title



class DefaultPassword(titleBase):
    title= models.CharField(max_length=255,unique=True,verbose_name="Password")
    
    class Meta:
        db_table="Default_Password"

    def __str__(self):
        return self.title


class DateObjectsModels(models.Model):
    id=models.AutoField(primary_key=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    objects=models.Manager()

    class Meta:
        abstract=True


class CustomerID(DateObjectsModels):
    title=models.CharField(max_length=255,unique=True)

    class Meta(DateObjectsModels.Meta):
        db_table="customer_Id"

class DataCaptureManager(DateObjectsModels):
    status= models.ForeignKey(MembershipStatus,on_delete=models.DO_NOTHING,default=1)
    

    class Meta(DateObjectsModels.Meta):
        db_table="Data_Capture_Manager"

class TransactionPeriods(DateObjectsModels):
    transaction_period=models.DateField()
    status= models.ForeignKey(MembershipStatus,on_delete=models.DO_NOTHING,default=1)
    
    class Meta(DateObjectsModels.Meta):
        db_table="Transaction_Periods"



class AutoReceipt(DateObjectsModels):
    receipt= models.CharField(max_length=255,default=1)
    
    class Meta(DateObjectsModels.Meta):
        db_table="Auto_Receipt"


class LoanNumber(DateObjectsModels):
    code= models.IntegerField(unique=True)


    class Meta(DateObjectsModels.Meta):
        db_table="Loan_Number"



class Receipts(DateObjectsModels):
    id=models.AutoField(primary_key=True)
    receipt= models.CharField(max_length=255,unique=True)
    status = models.ForeignKey(ReceiptStatus,on_delete=models.CASCADE,default=1)
    

    class Meta(DateObjectsModels.Meta):
        db_table="Receipts"



class Receipts_Shop(DateObjectsModels):
    id=models.AutoField(primary_key=True)
    receipt= models.CharField(max_length=255,unique=True)
    status = models.ForeignKey(ReceiptStatus,on_delete=models.CASCADE,default=1)
    

    class Meta(DateObjectsModels.Meta):
        db_table="Receipts_Shop"


class Receipt_Cancelled(DateObjectsModels):
    receipt = models.ForeignKey(Receipts,on_delete=models.CASCADE,blank=True,null=True)
    reasons= models.TextField()
    processed_by=models.ForeignKey(CustomUser,on_delete=models.DO_NOTHING,blank=True,null=True)
    
    class Meta(DateObjectsModels.Meta):
        db_table="Receipt_Cancelled"

class SharesUnits(DateObjectsModels):
    unit= models.IntegerField(unique=True)
   
    class Meta(DateObjectsModels.Meta):
        db_table="Shares_Units"

class MembersIdManager(DateObjectsModels):
    prefix_title= models.CharField(max_length=255)
    prefix_year= models.CharField(max_length=255)
    member_id= models.IntegerField(unique=True)
    
    class Meta(DateObjectsModels.Meta):
        db_table="Members_Id_Manager"

 
class CooperativeBankAccounts(DateObjectsModels):
    bank=models.ForeignKey(Banks,on_delete=models.CASCADE,default=1)
    account_name=models.CharField(max_length=255)
    account_type=models.ForeignKey(AccountTypes,on_delete=models.DO_NOTHING,default=1)
    account_number=models.CharField(max_length=255)
    
    class Meta(DateObjectsModels.Meta):
        db_table="Cooperative_Bank_Accounts"


class Lga(DateObjectsModels):
    title= models.CharField(max_length=255,blank=True,null=True)
    state=models.ForeignKey(States,on_delete=models.CASCADE,default=1)
   
    class Meta(DateObjectsModels.Meta):
        db_table="Lga"


class Staff(DateObjectsModels):
    admin=models.OneToOneField(CustomUser,on_delete=models.CASCADE,blank=True,null=True)
    title=models.ForeignKey(Titles,on_delete=models.CASCADE,blank=True,null=True)
    middle_name=models.CharField(max_length=50)
    address=models.TextField()
    phone_number=models.CharField(max_length=50)
    gender =models.ForeignKey(Gender,on_delete=models.DO_NOTHING,blank=True,null=True)
    userlevel =models.ForeignKey(UsersLevel,on_delete=models.DO_NOTHING,default=1)
    
    @property
    def get_full_name(self):
        if self.middle_name:
              return self.admin.last_name + " " + self.admin.first_name + " " + self.middle_name
        else:
              return self.admin.last_name + " " + self.admin.first_name 
   

    class Meta(DateObjectsModels.Meta):
        db_table="Staff"


class TransactionTypes(DateObjectsModels):
    source = models.ForeignKey(TransactionSources,on_delete=models.CASCADE,blank=True,null=True)
    category = models.ForeignKey(LoanCategory,on_delete=models.CASCADE,blank=True,null=True)
    code=models.CharField(max_length=50,unique=True)
    name=models.CharField(max_length=50,unique=True)
    maximum_amount = models.DecimalField(max_digits=20,decimal_places = 2)
    minimum_amount = models.DecimalField(max_digits=20,decimal_places = 2)
    duration= models.PositiveSmallIntegerField(validators=[MinValueValidator(0)],default=0)
    interest_deduction=  models.ForeignKey(InterestDeductionSource,on_delete=models.DO_NOTHING,blank=True,null=True)
    interest_rate= models.PositiveSmallIntegerField(validators=[MinValueValidator(0)],default=0)
    rank= models.IntegerField(unique=False,default=0)
    admin_charges_rating= models.ForeignKey(AdminCharges,on_delete=models.DO_NOTHING,blank=True,null=True)
    admin_charges = models.DecimalField(max_digits=20,decimal_places = 2,blank=True,null=True)
    admin_charges_minimum= models.DecimalField(max_digits=20,decimal_places = 2,blank=True,null=True)
    default_admin_charges= models.DecimalField(max_digits=20,decimal_places = 2,default=0)
    salary_loan_relationship= models.IntegerField(default=0)
    savings_rate= models.IntegerField(default=0)
    guarantors= models.IntegerField(default=0)
    loan_age= models.IntegerField(default=0)
    share_unit_min= models.IntegerField(default=0)
    share_unit_max= models.IntegerField(default=0)
    receipt_type= models.ForeignKey(ReceiptTypes,on_delete=models.DO_NOTHING,default=1)
    status= models.ForeignKey(MembershipStatus,on_delete=models.DO_NOTHING,default=1)
    multiple_loan_status= models.ForeignKey(MultipleLoanStatus,on_delete=models.CASCADE,default=1)
    # maturity= models.IntegerField(default=0)
    
    class Meta(DateObjectsModels.Meta):
        db_table="Transaction_Types"

class  CompulsorySavings(DateObjectsModels):
    transaction=models.ForeignKey(TransactionTypes,on_delete=models.CASCADE,blank=True,null=True)
    
    class Meta(DateObjectsModels.Meta):
        db_table="Compulsory_Savings"
   

class  WithdrawableTransactions(DateObjectsModels):
    transaction=models.ForeignKey(TransactionTypes,on_delete=models.CASCADE,blank=True,null=True)
    status= models.ForeignKey(WithdrawalStatus,on_delete=models.DO_NOTHING,default=1)
    maturity= models.IntegerField(default=0)
   

    class Meta(DateObjectsModels.Meta):
        db_table="Withdrawable_Transactions"

class  LoanBasedSavings(DateObjectsModels):
    savings=models.ForeignKey(TransactionTypes,on_delete=models.CASCADE,blank=True,null=True)
    

    class Meta(DateObjectsModels.Meta):
        db_table="Loanbased_Savings"

class ApprovableTransactions(DateObjectsModels):
    transaction=models.ForeignKey(TransactionTypes,on_delete=models.CASCADE,blank=True,null=True)
    status= models.ForeignKey(MembershipStatus,on_delete=models.DO_NOTHING,default=1)
    
    class Meta(DateObjectsModels.Meta):
        db_table="Approvable_Transactions"


class ApprovalOfficers(DateObjectsModels):
    officer=models.ForeignKey(CustomUser,on_delete=models.DO_NOTHING,blank=True,null=True)
    transaction=models.ForeignKey(ApprovableTransactions,on_delete=models.CASCADE,blank=True,null=True)
    status= models.ForeignKey(MembershipStatus,on_delete=models.DO_NOTHING,default=1)
    
    class Meta(DateObjectsModels.Meta):
        db_table="Approval_Officers"


class CertifiableTransactions(DateObjectsModels):
    transaction=models.ForeignKey(TransactionTypes,on_delete=models.CASCADE,blank=True,null=True)
    status= models.ForeignKey(MembershipStatus,on_delete=models.DO_NOTHING,default=1)
   

    class Meta(DateObjectsModels.Meta):
        db_table="Certifiable_Transactions"


class CertificationOfficers(DateObjectsModels):
    officer=models.ForeignKey(CustomUser,on_delete=models.DO_NOTHING,blank=True,null=True)
    transaction=models.ForeignKey(CertifiableTransactions,on_delete=models.CASCADE,blank=True,null=True)
    status= models.ForeignKey(MembershipStatus,on_delete=models.DO_NOTHING,default=1)
   

    class Meta(DateObjectsModels.Meta):
        db_table="Certification_Officers"


class DisbursementOfficers(DateObjectsModels):
    officer=models.ForeignKey(CustomUser,on_delete=models.DO_NOTHING,blank=True,null=True)
    status= models.ForeignKey(MembershipStatus,on_delete=models.DO_NOTHING,default=1)
   
    class Meta(DateObjectsModels.Meta):
        db_table="Disbursement_Officers"


class MemberShipRequest(DateObjectsModels):
    title=models.ForeignKey(Titles,on_delete=models.DO_NOTHING,blank=True,null=True)
    first_name=models.CharField(max_length=255)
    last_name=models.CharField(max_length=255)
    middle_name=models.CharField(max_length=255,blank=True,null=True)
    gender = models.ForeignKey(Gender,on_delete=models.DO_NOTHING,blank=True,null=True)
    phone_number=models.CharField(max_length=255)
    department=models.ForeignKey(Departments,on_delete=models.DO_NOTHING,blank=True,null=True)
    
    certification_officer=models.ForeignKey(CertificationOfficers,on_delete=models.DO_NOTHING,blank=True,null=True)
    certification_status = models.ForeignKey(CertificationStatus,on_delete=models.DO_NOTHING,default=1)
    certified_date=models.DateField(blank=True,null=True)
    
    approval_officer=models.ForeignKey(ApprovalOfficers,on_delete=models.DO_NOTHING,blank=True,null=True)
    approval_status = models.ForeignKey(ApprovalStatus,on_delete=models.DO_NOTHING,default=1)
    approval_comment=models.TextField(blank=True,null=True)
    approved_date=models.DateField(blank=True,null=True)
    
    transaction_status= models.ForeignKey(TransactionStatus,on_delete=models.DO_NOTHING,default=1)
    processed_by=models.ForeignKey(CustomUser,on_delete=models.DO_NOTHING,blank=True,null=True)
    submission_status= models.ForeignKey(SubmissionStatus,on_delete=models.DO_NOTHING,default=1)
    salary_institution=models.ForeignKey(SalaryInstitution,on_delete=models.DO_NOTHING,blank=True,null=True)
    file_no=models.CharField(max_length=255,blank=True,null=True)
    ippis_no=models.CharField(max_length=255,blank=True,null=True)
    year=models.CharField(max_length=255,blank=True,null=True)
    member_id=models.CharField(max_length=255,blank=True,null=True)
    

    class Meta(DateObjectsModels.Meta):
        db_table="Membership_Request"



class MemberShipRequestAdditionalInfo(DateObjectsModels):
    applicant=models.ForeignKey(MemberShipRequest,on_delete=models.CASCADE,blank=True,null=True)
    comment=models.TextField(blank=True,null=True)
    officer=models.ForeignKey(CustomUser,on_delete=models.CASCADE,blank=True,null=True)
   
    class Meta(DateObjectsModels.Meta):
        db_table="MemberShip_Request_Additional_Info"

class MemberShipRequestAdditionalAttachment(DateObjectsModels):
    applicant=models.ForeignKey(MemberShipRequest,on_delete=models.CASCADE,blank=True,null=True)
    caption=models.CharField(max_length=255)
    image=models.FileField(blank=True,null=True)
    officer=models.ForeignKey(CustomUser,on_delete=models.CASCADE,blank=True,null=True)
   
    
    class Meta(DateObjectsModels.Meta):
        db_table="Membership_Request_Additional_Attachment"

class MemberShipFormSalesRecord(DateObjectsModels):
    applicant=models.ForeignKey(MemberShipRequest,on_delete=models.CASCADE,blank=True,null=True)
    payment_reference=models.CharField(max_length=255,blank=True,null=True)
    receipt=models.CharField(max_length=255,unique=True)
    admin_charge = models.DecimalField(max_digits=20,decimal_places = 2,blank=True,null=True)
    shares=models.IntegerField(default=0)
    share_amount = models.DecimalField(max_digits=20,decimal_places = 2,blank=True,null=True)
    welfare_amount = models.DecimalField(max_digits=20,decimal_places = 2,blank=True,null=True)
    bank_ccount= models.ForeignKey(CooperativeBankAccounts,on_delete=models.DO_NOTHING,blank=True,null=True)
    image=models.FileField(blank=True,null=True)
    status= models.ForeignKey(TransactionStatus,on_delete=models.DO_NOTHING,default=1)
    processed_by=models.ForeignKey(CustomUser,on_delete=models.CASCADE,blank=True,null=True)
   

    class Meta(DateObjectsModels.Meta):
        db_table="Membership_Form_Sales_Record"


class Members(DateObjectsModels):
    admin=models.OneToOneField(CustomUser,on_delete=models.CASCADE,blank=True,null=True)
    applicant=models.ForeignKey(MemberShipFormSalesRecord,on_delete=models.CASCADE,blank=True,null=True)
    member_id = models.CharField(max_length=255, unique=True)
    title=models.ForeignKey(Titles,on_delete=models.DO_NOTHING,blank=True,null=True)
    middle_name=models.CharField(max_length=255,blank=True,null=True)
    full_name=models.CharField(max_length=255,blank=True,null=True)
    gender = models.ForeignKey(Gender,on_delete=models.DO_NOTHING,blank=True,null=True)
    phone_number=models.CharField(max_length=255,unique=True)
    profile_pic=models.FileField(blank=True,null=True)
    residential_address=models.TextField(blank=True,null=True)
    permanent_home_address=models.TextField(blank=True,null=True)
    department=models.ForeignKey(Departments,on_delete=models.DO_NOTHING,blank=True,null=True)
    state=models.ForeignKey(States, on_delete=models.DO_NOTHING,blank=True,null=True)
    lga=models.ForeignKey(Lga, on_delete=models.DO_NOTHING,blank=True,null=True)
    salary_institution=models.ForeignKey(SalaryInstitution,on_delete=models.DO_NOTHING,blank=True,null=True)
    file_no=models.CharField(max_length=255,unique=True)
    exclusive_status= models.ForeignKey(ExclusiveStatus,on_delete=models.CASCADE,default=1)
    ippis_no=models.CharField(max_length=255,unique=True)
    gross_pay=models.DecimalField(max_digits=20,decimal_places = 2,default=0)
    gross_pay_as_at=models.CharField(max_length=255,blank=True,null=True)
    gross_pay_status=models.ForeignKey(ProcessingStatus,on_delete=models.CASCADE,default=1)
    shares=models.IntegerField(default=0)
    date_joined=models.DateField(blank=True,null=True)
    status= models.ForeignKey(MembershipStatus,on_delete=models.CASCADE,default=1)
    savings_status= models.ForeignKey(SavingsUploadStatus,on_delete=models.CASCADE,default=1)
    loan_status= models.ForeignKey(LoansUploadStatus,on_delete=models.CASCADE,default=1)
    shares_status= models.ForeignKey(SharesUploadStatus,on_delete=models.CASCADE,default=1)
    welfare_status= models.ForeignKey(WelfareUploadStatus,on_delete=models.CASCADE,default=1)
    date_joined_status= models.ForeignKey(DateJoinedUploadStatus,on_delete=models.CASCADE,default=1)
   

    def __str__(self):
        return '{} {} {}'.format(self.admin.last_name, self.admin.first_name)

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
    
    class Meta(DateObjectsModels.Meta):
        db_table="Members"

    # def save(self, *args, **kwargs):
    #     super().save(*args, **kwargs)
    #     if profile_pic:
    #         img = profile_pic.open(self.profile_pic.path)

    #         if img.height>300 or img.weight>300:
    #             output_size=(300,300)
    #             img.thumbnail(output_size)
    #             img.save(self.profile_pic.path)
            



class MembersExclusiveness(DateObjectsModels):
    member= models.ForeignKey(Members,on_delete=models.CASCADE,blank=True,null=True)
    transaction=models.ForeignKey(TransactionTypes,on_delete=models.CASCADE,blank=True,null=True)
 
    approval_officer=models.ForeignKey(ApprovalOfficers,on_delete=models.CASCADE,blank=True,null=True)
    approval_comment=models.TextField(blank=True,null=True)
    approval_status= models.ForeignKey(ApprovalStatus,on_delete=models.CASCADE,default=1)
    approved_at=models.DateField(blank=True,null=True)
    status= models.ForeignKey(TransactionStatus,on_delete=models.CASCADE,default=1)
    
    class Meta(DateObjectsModels.Meta):
        db_table="Members_Exclusiveness"

class NextOfKinsMaximun(DateObjectsModels):
    maximun=models.CharField(max_length=255)   

    class Meta(DateObjectsModels.Meta):
        db_table="Next_Of_Kins_Maximun"


class MembersNextOfKins(DateObjectsModels):
    member=models.ForeignKey(Members,on_delete=models.CASCADE,blank=True,null=True)
    name=models.CharField(max_length=255)
    relationships=models.ForeignKey(NOKRelationships,on_delete=models.DO_NOTHING,blank=True,null=True)
    address=models.TextField(blank=True,null=True)
    phone_number=models.CharField(max_length=255)
    status= models.ForeignKey(MembershipStatus,on_delete=models.CASCADE,default=1)
    lock_status= models.ForeignKey(LockedStatus,on_delete=models.CASCADE,default=1)
    


    class Meta(DateObjectsModels.Meta):
        db_table="Members_Next_Of_Kins"


class MembersBankAccounts(DateObjectsModels):
    member_id=models.ForeignKey(Members,on_delete=models.CASCADE,blank=True,null=True)
    bank=models.ForeignKey(Banks,on_delete=models.CASCADE,blank=True,null=True)
    account_name=models.CharField(max_length=255)
    account_number=models.CharField(max_length=255)
    account_type=models.ForeignKey(AccountTypes,on_delete=models.DO_NOTHING,blank=True,null=True)
    status= models.ForeignKey(MembershipStatus,on_delete=models.CASCADE,default=1)
    lock_status= models.ForeignKey(LockedStatus,on_delete=models.CASCADE,default=1)
    
    class Meta(DateObjectsModels.Meta):
        db_table="Members_Bank_Accounts"


class MembersAccountsDomain(DateObjectsModels):
    member=models.ForeignKey(Members,on_delete=models.CASCADE,default=1)
    transaction=models.ForeignKey(TransactionTypes,on_delete=models.CASCADE,default=1)
    account_number=models.CharField(max_length=255,unique=True)
    status=models.ForeignKey(MembershipStatus,on_delete=models.DO_NOTHING,default=1)
    
    class Meta(DateObjectsModels.Meta):
        db_table="Members_Accounts_Domain"


class StandingOrderAccounts(DateObjectsModels):
    transaction=models.OneToOneField(MembersAccountsDomain,on_delete=models.CASCADE,default=1)
    amount=models.DecimalField(max_digits=20,decimal_places = 2)
    status=models.ForeignKey(MembershipStatus,on_delete=models.DO_NOTHING,default=1)
    lock_status=models.ForeignKey(LockedStatus,on_delete=models.DO_NOTHING,default=1)
 

    class Meta(DateObjectsModels.Meta):
        db_table="Standing_Order_Accounts"


class SavingsUploaded(DateObjectsModels):
    transaction=models.ForeignKey(MembersAccountsDomain,on_delete=models.CASCADE,default=1)
    particulars=models.CharField(max_length=255)
    balance=models.DecimalField(max_digits=20,decimal_places = 2,default=0)
    schedule_amount=models.DecimalField(max_digits=20,decimal_places = 2,default=0)
    processed_by=models.ForeignKey(CustomUser,on_delete=models.DO_NOTHING,blank=True,null=True)
    transaction_period=models.ForeignKey(TransactionPeriods,on_delete=models.CASCADE,default=1)
    status= models.ForeignKey(TransactionStatus,on_delete=models.CASCADE,default=1)
    

    class Meta(DateObjectsModels.Meta):
        db_table="Savings_Uploaded"


class LoansUploaded(DateObjectsModels):
    member= models.ForeignKey(Members,on_delete=models.CASCADE,blank=True,null=True)
    particulars=models.CharField(max_length=255)
    transaction=models.ForeignKey(TransactionTypes,on_delete=models.CASCADE,blank=True,null=True)
    loan_amount=models.DecimalField(max_digits=20,decimal_places = 2,default=0)
    amount_paid=models.DecimalField(max_digits=20,decimal_places = 2,default=0)
    balance=models.DecimalField(max_digits=20,decimal_places = 2,default=0)
    repayment=models.DecimalField(max_digits=20,decimal_places = 2,default=0)
    duration=models.IntegerField(default=0)
    interest_rate=models.IntegerField(default=0)
    interest_deduction=models.CharField(max_length=255,blank=True,null=True)
    start_date=models.DateField(blank=True,null=True)
    stop_date=models.DateField(blank=True,null=True)
    processed_by=models.ForeignKey(CustomUser,on_delete=models.DO_NOTHING,blank=True,null=True)
    transaction_period=models.ForeignKey(TransactionPeriods,on_delete=models.CASCADE,default=1)
    status= models.ForeignKey(TransactionStatus,on_delete=models.CASCADE,default=1)
    
    class Meta(DateObjectsModels.Meta):
        db_table="Loans_Uploaded"

class LoanRequest(DateObjectsModels):
    member=models.ForeignKey(Members,on_delete=models.CASCADE,blank=True,null=True)
    loan=models.ForeignKey(TransactionTypes,on_delete=models.CASCADE,blank=True,null=True)
    loan_amount=models.DecimalField(max_digits=20,decimal_places = 2)
    approved_amount=models.DecimalField(max_digits=20,decimal_places = 2,blank=True,null=True)
    comment=models.TextField(blank=True,null=True)


    certification_officer=models.ForeignKey(CertificationOfficers,on_delete=models.DO_NOTHING,blank=True,null=True)
    certification_status = models.ForeignKey(CertificationStatus,on_delete=models.DO_NOTHING,default=1)
    certification_comment=models.TextField(blank=True,null=True)
    certification_date=models.DateField(blank=True,null=True)
    
    approval_officer=models.ForeignKey(ApprovalOfficers,on_delete=models.DO_NOTHING,blank=True,null=True)
    approval_status = models.ForeignKey(ApprovalStatus,on_delete=models.DO_NOTHING,default=1)
    approval_comment=models.TextField(blank=True,null=True)
    approval_date=models.DateField(blank=True,null=True)
    

    transaction_status= models.ForeignKey(TransactionStatus,on_delete=models.DO_NOTHING,default=1)
    processed_by=models.ForeignKey(CustomUser,on_delete=models.DO_NOTHING,blank=True,null=True)
    submission_status= models.ForeignKey(SubmissionStatus,on_delete=models.DO_NOTHING,default=1)


    class Meta(DateObjectsModels.Meta):
        db_table="Loan_Request"

class LoanGuarantors(DateObjectsModels):
    applicant= models.ForeignKey(LoanRequest,on_delete=models.CASCADE,blank=True,null=True)
    guarantor= models.ForeignKey(Members,on_delete=models.CASCADE,blank=True,null=True)
   

    class Meta(DateObjectsModels.Meta):
        db_table="Loan_Guarantors"

class ExternalFascilitiesTemp(DateObjectsModels):
    member= models.ForeignKey(Members,on_delete=models.CASCADE,blank=True,null=True)
    description=models.CharField(max_length=255,blank=True,null=True)
    amount=models.DecimalField(max_digits=20,decimal_places = 2)
    image=models.FileField(blank=True,null=True)
    approval_officer=models.ForeignKey(ApprovalOfficers,on_delete=models.CASCADE,blank=True,null=True)
    approval_comment=models.TextField(blank=True,null=True)
    status= models.ForeignKey(ApprovalStatus,on_delete=models.CASCADE,default=1)
    transaction_status= models.ForeignKey(TransactionStatus,on_delete=models.CASCADE,default=1)
    approved_at=models.DateField(blank=True,null=True)
    
    class Meta(DateObjectsModels.Meta):
        db_table="External_Fascilities_Temp"

class ExternalFascilitiesMain(DateObjectsModels):
    member= models.ForeignKey(ExternalFascilitiesTemp,on_delete=models.CASCADE,blank=True,null=True)
    status= models.ForeignKey(TransactionStatus,on_delete=models.CASCADE,default=1)
    
    class Meta(DateObjectsModels.Meta):
        db_table="External_Fascilities_Main"


 
class LoanRequestAttachments(DateObjectsModels):
    applicant=models.ForeignKey(LoanRequest,on_delete=models.CASCADE,blank=True,null=True)
    description=models.CharField(max_length=255)
    image=models.FileField()
    processed_by=models.ForeignKey(CustomUser,on_delete=models.DO_NOTHING,blank=True,null=True)
    status= models.ForeignKey(TransactionStatus,on_delete=models.CASCADE,default=1)
    
    class Meta(DateObjectsModels.Meta):
        db_table="Loan_Request_Attachments"

class LoanRequestSettings(DateObjectsModels):
    applicant=models.ForeignKey(LoanRequest,on_delete=models.CASCADE,blank=True,null=True)
    description=models.CharField(max_length=255)
    value=models.CharField(max_length=255)
    category= models.CharField(max_length=255,blank=True,null=True)
    status= models.ForeignKey(TransactionStatus,on_delete=models.CASCADE,default=1)
    
    class Meta(DateObjectsModels.Meta):
        db_table="Loan_Request_Settings"

class LoanFormIssuance(DateObjectsModels):
    applicant=models.ForeignKey(LoanRequest,on_delete=models.CASCADE,blank=True,null=True)
    receipt=models.CharField(max_length=255,unique=True)
    admin_charge=models.DecimalField(max_digits=20,decimal_places = 2)
    processing_status= models.ForeignKey(ProcessingStatus,on_delete=models.CASCADE,default=1)
    status= models.ForeignKey(TransactionStatus,on_delete=models.CASCADE,default=1)
   
    class Meta(DateObjectsModels.Meta):
        db_table="Loan_Form_Issuance"

class LoanApplication(DateObjectsModels):
    applicant=models.ForeignKey(LoanFormIssuance,on_delete=models.CASCADE,blank=True,null=True)
    loan_amount=models.DecimalField(max_digits=20,decimal_places = 2)
    approved_amount=models.DecimalField(max_digits=20,decimal_places = 2,blank=True,null=True)
    comment=models.TextField(blank=True,null=True)


    certification_officer=models.ForeignKey(CertificationOfficers,on_delete=models.DO_NOTHING,blank=True,null=True)
    certification_status = models.ForeignKey(CertificationStatus,on_delete=models.DO_NOTHING,default=1)
    certification_comment=models.TextField(blank=True,null=True)
    certification_date=models.DateField(blank=True,null=True)
    
    approval_officer=models.ForeignKey(ApprovalOfficers,on_delete=models.DO_NOTHING,blank=True,null=True)
    approval_status = models.ForeignKey(ApprovalStatus,on_delete=models.DO_NOTHING,default=1)
    approval_comment=models.TextField(blank=True,null=True)
    approval_date=models.DateField(blank=True,null=True)
    
    bank_account=models.ForeignKey(MembersBankAccounts,on_delete=models.DO_NOTHING,blank=True,null=True)
    nok=models.ForeignKey(MembersNextOfKins,on_delete=models.DO_NOTHING,blank=True,null=True)

    transaction_status= models.ForeignKey(TransactionStatus,on_delete=models.DO_NOTHING,default=1)
    processed_by=models.ForeignKey(CustomUser,on_delete=models.DO_NOTHING,blank=True,null=True)
    submission_status= models.ForeignKey(SubmissionStatus,on_delete=models.DO_NOTHING,default=1)

    class Meta(DateObjectsModels.Meta):
        db_table="Loan_Application"


class LoanApplicationGuarnators(DateObjectsModels):
    applicant=models.ForeignKey(LoanApplication,on_delete=models.CASCADE,blank=True,null=True)
    guarantor=models.ForeignKey(Members,on_delete=models.DO_NOTHING,blank=True,null=True)
    status= models.ForeignKey(TransactionStatus,on_delete=models.CASCADE,default=1)
    
    class Meta(DateObjectsModels.Meta):
        db_table="Loan_Application_Guarnators"


class LoanApplicationSettings(DateObjectsModels):
    applicant=models.ForeignKey(LoanApplication,on_delete=models.CASCADE,blank=True,null=True)
    description=models.CharField(max_length=255)
    value=models.CharField(max_length=255)
    category= models.CharField(max_length=255,blank=True,null=True)
    status= models.ForeignKey(TransactionStatus,on_delete=models.CASCADE,default=1)
    
    class Meta(DateObjectsModels.Meta):
        db_table="Loan_Application_Settings"

class LoansDisbursed(DateObjectsModels):
    member= models.ForeignKey(Members,on_delete=models.CASCADE,blank=True,null=True)
    transaction= models.ForeignKey(TransactionTypes,on_delete=models.CASCADE,blank=True,null=True)
    loan_number=models.CharField(max_length=255,unique=True)
    loan_amount=models.DecimalField(max_digits=20,decimal_places = 2)
    repayment=models.DecimalField(max_digits=20,decimal_places = 2)
    amount_paid=models.DecimalField(max_digits=20,decimal_places = 2,default=0)
    balance=models.DecimalField(max_digits=20,decimal_places = 2)
    schedule_status=models.ForeignKey(LoanScheduleStatus,on_delete=models.CASCADE,default=1)
    duration=models.IntegerField(default=0)
    interest_rate=models.IntegerField(default=0)
    interest_deduction=models.CharField(max_length=255,blank=True,null=True)
    start_date=models.DateField(blank=True,null=True)
    stop_date=models.DateField(blank=True,null=True)
    processed_by=models.ForeignKey(CustomUser,on_delete=models.CASCADE,blank=True,null=True)
    merge_account_number=models.CharField(max_length=255,blank=True,null=True)
    loan_merge_status=models.ForeignKey(LoanMergeStatus,on_delete=models.CASCADE,default=1)
    status=models.ForeignKey(MembershipStatus,on_delete=models.CASCADE,blank=True,null=True)
   

    class Meta(DateObjectsModels.Meta):
        db_table="Loans_Disbursed"


class LoansRepaymentBase(DateObjectsModels):
    member= models.ForeignKey(Members,on_delete=models.CASCADE,blank=True,null=True)
    transaction= models.ForeignKey(TransactionTypes,on_delete=models.CASCADE,blank=True,null=True)
    loan_number=models.CharField(max_length=255,unique=True)
    loan_amount=models.DecimalField(max_digits=20,decimal_places = 2)
    repayment=models.DecimalField(max_digits=20,decimal_places = 2)
    amount_paid=models.DecimalField(max_digits=20,decimal_places = 2,default=0)
    balance=models.DecimalField(max_digits=20,decimal_places = 2)
    start_date=models.DateField(blank=True,null=True)
    stop_date=models.DateField(blank=True,null=True)
    processed_by=models.ForeignKey(CustomUser,on_delete=models.CASCADE,blank=True,null=True)
    status=models.ForeignKey(MembershipStatus,on_delete=models.CASCADE,blank=True,null=True)
    loan_merge_status=models.ForeignKey(LoanMergeStatus,on_delete=models.CASCADE,default=1)
    merged_loans=models.CharField(max_length=255,blank=True,null=True)
   
    class Meta(DateObjectsModels.Meta):
        db_table="Loans_Repayment_Base"

class LoansCleared(DateObjectsModels):
    loan=models.ForeignKey(LoansRepaymentBase,on_delete=models.CASCADE,blank=True,null=True)
    processed_by=models.ForeignKey(CustomUser,on_delete=models.CASCADE,blank=True,null=True)
    status=models.ForeignKey(TransactionStatus,on_delete=models.CASCADE,blank=True,null=True)
       
    class Meta(DateObjectsModels.Meta):
        db_table="Loans_Cleared"


class MonthlyDeductionList(DateObjectsModels):
    transaction_period=models.ForeignKey(TransactionPeriods,on_delete=models.CASCADE,default=1)
    member=models.ForeignKey(Members,on_delete=models.CASCADE,blank=True,null=True)
    account_number=models.CharField(max_length=255,blank=True,null=True)
    amount=models.DecimalField(max_digits=20,decimal_places = 2,default=0)
    amount_deducted=models.DecimalField(max_digits=20,decimal_places = 2,default=0)
    transaction=models.ForeignKey(TransactionTypes,on_delete=models.CASCADE,blank=True,null=True)
    transaction_status= models.ForeignKey(TransactionStatus,on_delete=models.DO_NOTHING,default=1)
    
    class Meta(DateObjectsModels.Meta):
        db_table="Monthly_Deduction_List"


class MonthlyGeneratedTransactions(DateObjectsModels):
    transaction=models.ForeignKey(TransactionTypes,on_delete=models.CASCADE,default=1)
    transaction_period=models.ForeignKey(TransactionPeriods,on_delete=models.CASCADE,default=1)
    processed_by=models.ForeignKey(CustomUser,on_delete=models.CASCADE,blank=True,null=True)
    transaction_status= models.ForeignKey(TransactionStatus,on_delete=models.DO_NOTHING,default=1)
   
    class Meta(DateObjectsModels.Meta):
        db_table="Monthly_Generated_Transactions"


class MonthlyDeductionListGenerated(DateObjectsModels):
    transaction_period=models.ForeignKey(TransactionPeriods,on_delete=models.CASCADE,default=1)
    member=models.ForeignKey(Members,on_delete=models.CASCADE,blank=True,null=True)
    amount=models.DecimalField(max_digits=20,decimal_places = 2,default=0)
    amount_deducted=models.DecimalField(max_digits=20,decimal_places = 2,default=0)
    balance=models.DecimalField(max_digits=20,decimal_places = 2,default=0)
    salary_institution=models.ForeignKey(SalaryInstitution,on_delete=models.CASCADE,default=1)
    transaction_status= models.ForeignKey(TransactionStatus,on_delete=models.DO_NOTHING,default=1)
    

    class Meta(DateObjectsModels.Meta):
        db_table="Monthly_Deduction_List_Generated"


class MonthlyGroupGeneratedTransactions(DateObjectsModels):
    salary_institution=models.ForeignKey(SalaryInstitution,on_delete=models.CASCADE,default=1)
    transaction_period=models.ForeignKey(TransactionPeriods,on_delete=models.CASCADE,default=1)
    processed_by=models.ForeignKey(CustomUser,on_delete=models.CASCADE,blank=True,null=True)
    transaction_status= models.ForeignKey(TransactionStatus,on_delete=models.DO_NOTHING,default=1)
   
    class Meta(DateObjectsModels.Meta):
        db_table="Monthly_Group_Generated_Transactions"

class AccountDeductions(DateObjectsModels):
    salary_institution=models.ForeignKey(SalaryInstitution,on_delete=models.CASCADE,default=1)
    transaction_period=models.ForeignKey(TransactionPeriods,on_delete=models.CASCADE,default=1)
    ippis_no=models.CharField(max_length=255)
    name=models.CharField(max_length=255)
    amount=models.DecimalField(max_digits=20,decimal_places = 2,default=0)
    transaction_status= models.ForeignKey(TransactionStatus,on_delete=models.DO_NOTHING,default=1)
    
    class Meta(DateObjectsModels.Meta):
        db_table="Account_Deductions"


class NonMemberAccountDeductions(DateObjectsModels):
    salary_institution=models.ForeignKey(SalaryInstitution,on_delete=models.CASCADE,default=1)
    transaction_period=models.ForeignKey(TransactionPeriods,on_delete=models.CASCADE,default=1)
    ippis_no=models.CharField(max_length=255)
    name=models.CharField(max_length=255)
    amount=models.DecimalField(max_digits=20,decimal_places = 2,default=0)
    transaction_status= models.ForeignKey(TransactionStatus,on_delete=models.DO_NOTHING,default=1)
   
    class Meta(DateObjectsModels.Meta):
        db_table="Non_Member_Account_Deductions"


class TransactionAjustmentRequest(DateObjectsModels):
    member=models.ForeignKey(MembersAccountsDomain,on_delete=models.CASCADE,default=1)
    amount=models.DecimalField(max_digits=20,decimal_places = 2)
    approval_officer=models.ForeignKey(ApprovalOfficers,on_delete=models.CASCADE,blank=True,null=True)
    approval_status= models.ForeignKey(ApprovalStatus,on_delete=models.CASCADE,default=1)
    approved_at=models.DateField(blank=True,null=True)
    effective_date=models.DateField(blank=True,null=True)
    status=models.ForeignKey(TransactionStatus,on_delete=models.DO_NOTHING,default=1)
    

    class Meta(DateObjectsModels.Meta):
        db_table="Transaction_Adjustment_Request"


class TransactionLoanAjustmentRequest(DateObjectsModels):
    member=models.ForeignKey(LoansRepaymentBase,on_delete=models.CASCADE,default=1)
    amount=models.DecimalField(max_digits=20,decimal_places = 2)
    approval_officer=models.ForeignKey(ApprovalOfficers,on_delete=models.CASCADE,blank=True,null=True)
    approval_status= models.ForeignKey(ApprovalStatus,on_delete=models.CASCADE,default=1)
    approved_at=models.DateField(blank=True,null=True)
    effective_date=models.DateField(blank=True,null=True)
    status=models.ForeignKey(TransactionStatus,on_delete=models.DO_NOTHING,default=1)
    
    class Meta(DateObjectsModels.Meta):
        db_table="Transaction_Loan_Adjustment_Request"

class MembersSalaryUpdateRequest(DateObjectsModels):
    member=models.ForeignKey(Members,on_delete=models.CASCADE,blank=True,null=True)
    amount=models.DecimalField(max_digits=20,decimal_places = 2,default=0)
    description=models.CharField(max_length=255)
    approved_at=models.DateField(blank=True,null=True)
    approved_officer=models.ForeignKey(ApprovalOfficers,on_delete=models.CASCADE,blank=True,null=True)
    approval_comment=models.TextField(blank=True,null=True)
    image=models.FileField(blank=True,null=True)
    status=models.ForeignKey(ApprovalStatus,on_delete=models.DO_NOTHING,default=1)
    processing_status=models.ForeignKey(ProcessingStatus,on_delete=models.CASCADE,default=1)
    
    class Meta(DateObjectsModels.Meta):
        db_table="Members_Salary_Update_Request"

class NorminalRoll(DateObjectsModels):
    member_id=models.CharField(max_length=255)
    file_no=models.CharField(max_length=255)
    ippis_no=models.CharField(max_length=255)
    last_name=models.CharField(max_length=255)
    first_name=models.CharField(max_length=255)
    middle_name=models.CharField(max_length=255,blank=True,null=True)
    phone_no=models.CharField(max_length=255)
    year=models.CharField(max_length=255)
    salary_institution=models.CharField(max_length=255)
    transaction_status=models.ForeignKey(TransactionStatus,on_delete=models.CASCADE,default=1)
   

    @property
    def get_middle_name(self):
        if self.middle_name:
              return self.middle_name
        else:
              return ""

    class Meta(DateObjectsModels.Meta):
        db_table="Norminal_Roll"


####################################################################
##################### SHARES MANAGER AND STAFF WAREFSRE ###############################
####################################################################
class SharesDeductionSavings(DateObjectsModels):
    savings=models.ForeignKey(TransactionTypes,on_delete=models.CASCADE,blank=True,null=True)
    

    class Meta(DateObjectsModels.Meta):
        db_table="Shares_Deduction_Savings"

class MembersShareConfigurations(DateObjectsModels):
    unit_cost=models.DecimalField(max_digits=20,decimal_places = 2,default=0)
    
    class Meta(DateObjectsModels.Meta):
        db_table="Members_Share_Configurations"

class MembersSharePurchaseRequest(DateObjectsModels):
    member=models.ForeignKey(MembersAccountsDomain,on_delete=models.CASCADE,blank=True,null=True)
    units=models.IntegerField(default=0)
    approval_officer=models.ForeignKey(ApprovalOfficers,on_delete=models.DO_NOTHING,blank=True,null=True)
    approval_status = models.ForeignKey(ApprovalStatus,on_delete=models.DO_NOTHING,default=1)
    approval_comment=models.TextField(blank=True,null=True)
    approval_date=models.DateField(blank=True,null=True)
    status= models.ForeignKey(TransactionStatus,on_delete=models.DO_NOTHING,default=1)
    
    class Meta(DateObjectsModels.Meta):
        db_table="Members_Share_Purchase_Request"

class MembersShareAccounts(DateObjectsModels):
    member=models.ForeignKey(MembersAccountsDomain,on_delete=models.CASCADE,blank=True,null=True)
    shares=models.IntegerField(default=0)
    unit_cost=models.DecimalField(max_digits=20,decimal_places = 2,default=0)
    total_cost=models.DecimalField(max_digits=20,decimal_places = 2,default=0)
    effective_date=models.DateField(blank=True,null=True)
    year=models.IntegerField(default=0)
    processed_by=models.ForeignKey(CustomUser,on_delete=models.CASCADE,blank=True,null=True)
    status= models.ForeignKey(TransactionStatus,on_delete=models.DO_NOTHING,default=1)
    
    class Meta(DateObjectsModels.Meta):
        db_table="Members_Share_Accounts"

class MembersShareAccountsMain(DateObjectsModels):
    member=models.ForeignKey(Members,on_delete=models.CASCADE,blank=True,null=True)
    account_number=models.IntegerField(default=0)
    shares=models.IntegerField(default=0)
    unit_cost=models.DecimalField(max_digits=20,decimal_places = 2,default=0)
    total_cost=models.DecimalField(max_digits=20,decimal_places = 2,default=0)
    effective_date=models.DateField(blank=True,null=True)
    year=models.IntegerField(default=0)
    processed_by=models.ForeignKey(CustomUser,on_delete=models.CASCADE,blank=True,null=True)
    status= models.ForeignKey(MembershipStatus,on_delete=models.DO_NOTHING,default=1)
    

    class Meta(DateObjectsModels.Meta):
        db_table="Members_Share_Accounts_Main"

class MembersShareInitialUpdateRequest(DateObjectsModels):
    member=models.ForeignKey(MembersShareAccounts,on_delete=models.CASCADE,blank=True,null=True)
    transaction=models.ForeignKey(TransactionTypes,on_delete=models.CASCADE,blank=True,null=True)
    amount=models.DecimalField(max_digits=20,decimal_places = 2,default=0)
    approval_officer=models.ForeignKey(ApprovalOfficers,on_delete=models.CASCADE,blank=True,null=True)
    approval_status= models.ForeignKey(ApprovalStatus,on_delete=models.CASCADE,default=1)
    approval_comment=models.TextField(blank=True,null=True)
    approved_at=models.DateField(blank=True,null=True)
    processed_by=models.ForeignKey(CustomUser,on_delete=models.CASCADE,blank=True,null=True)
    status= models.ForeignKey(TransactionStatus,on_delete=models.DO_NOTHING,default=1)
    
    class Meta(DateObjectsModels.Meta):
        db_table="Members_Share_Initial_Update_Request"

class SharesSalesRecord(DateObjectsModels):
    member=models.ForeignKey(MembersAccountsDomain,on_delete=models.CASCADE,blank=True,null=True)
    payment_reference=models.CharField(max_length=255,blank=True,null=True)
    receipt=models.CharField(max_length=255,unique=True)
    shares=models.IntegerField(default=0)
    unit_cost = models.DecimalField(max_digits=20,decimal_places = 2,blank=True,null=True)
    share_amount = models.DecimalField(max_digits=20,decimal_places = 2,blank=True,null=True)
    bank_account= models.ForeignKey(CooperativeBankAccounts,on_delete=models.DO_NOTHING,blank=True,null=True)
    image=models.FileField(blank=True,null=True)
    status= models.ForeignKey(TransactionStatus,on_delete=models.DO_NOTHING,default=1)
    processed_by=models.ForeignKey(CustomUser,on_delete=models.CASCADE,blank=True,null=True)
   
    class Meta(DateObjectsModels.Meta):
        db_table="Shares_Sales_Record"

class MembersWelfare(DateObjectsModels):
    amount=models.DecimalField(max_digits=20,decimal_places = 2,default=0)
   

    class Meta(DateObjectsModels.Meta):
        db_table="Members_Welfare"


class MembersWelfareAccounts(DateObjectsModels):
    member=models.ForeignKey(MembersAccountsDomain,on_delete=models.CASCADE,blank=True,null=True)
    amount=models.DecimalField(max_digits=20,decimal_places = 2,default=0)
    year=models.IntegerField(default=0)
    processed_by=models.ForeignKey(CustomUser,on_delete=models.CASCADE,blank=True,null=True)
    status= models.ForeignKey(TransactionStatus,on_delete=models.DO_NOTHING,default=1)
   

    class Meta(DateObjectsModels.Meta):
        db_table="Members_Welfare_Accounts"

####################################################################
##################### MEMBERS CASH DEPOSIT/ WITHDRAWALS ############
####################################################################
class MembersCashDeposits(DateObjectsModels):
    member=models.ForeignKey(Members,on_delete=models.CASCADE,blank=True,null=True)
    bank_accounts=models.ForeignKey(CooperativeBankAccounts,on_delete=models.CASCADE,blank=True,null=True)
    account_number=models.CharField(max_length=255,blank=True,null=True)
    transaction=models.ForeignKey(TransactionTypes,on_delete=models.CASCADE,blank=True,null=True)
    amount=models.DecimalField(max_digits=20,decimal_places = 2,default=0)
    payment_reference=models.CharField(max_length=255)
    receipt=models.CharField(max_length=255,blank=True,null=True)
    purpose=models.TextField()
    payment_evidience=models.FileField(blank=True,null=True)
    payment_date=models.DateField()
    processed_by=models.ForeignKey(CustomUser,on_delete=models.CASCADE,blank=True,null=True)
    status= models.ForeignKey(TransactionStatus,on_delete=models.DO_NOTHING,default=1)
    
    class Meta(DateObjectsModels.Meta):
        db_table="Members_Cash_Deposits"

class MembersCashWithdrawals(DateObjectsModels):
    member=models.ForeignKey(MembersAccountsDomain,on_delete=models.CASCADE,blank=True,null=True)
    # transaction=models.ForeignKey(TransactionTypes,on_delete=models.CASCADE,blank=True,null=True)
    # account_number=models.IntegerField(default=0)
    amount=models.DecimalField(max_digits=20,decimal_places = 2,default=0)    
    ledger_balance=models.DecimalField(max_digits=20,decimal_places = 2,default=0)    
    narration=models.TextField()
    approved_amount=models.DecimalField(max_digits=20,decimal_places = 2,default=0)    
    approval_officer=models.ForeignKey(ApprovalOfficers,on_delete=models.DO_NOTHING,blank=True,null=True)
    approval_status = models.ForeignKey(ApprovalStatus,on_delete=models.DO_NOTHING,default=1)
    approval_comment=models.TextField(blank=True,null=True)
    approval_date=models.DateField(blank=True,null=True)
    processed_by=models.ForeignKey(CustomUser,on_delete=models.CASCADE,blank=True,null=True)
    status= models.ForeignKey(TransactionStatus,on_delete=models.DO_NOTHING,default=1)
    maturity_date=models.DateField(blank=True,null=True)


    class Meta(DateObjectsModels.Meta):
        db_table="Members_Cash_Withdrawals"


class MembersCashWithdrawalsApplication(DateObjectsModels):
    member=models.ForeignKey(MembersAccountsDomain,on_delete=models.CASCADE,blank=True,null=True)
    amount=models.DecimalField(max_digits=20,decimal_places = 2,default=0)    
    ledger_balance=models.DecimalField(max_digits=20,decimal_places = 2,default=0)    
    narration=models.TextField()
    approved_amount=models.DecimalField(max_digits=20,decimal_places = 2,default=0)    
    approval_officer=models.ForeignKey(ApprovalOfficers,on_delete=models.DO_NOTHING,blank=True,null=True)
    approval_status = models.ForeignKey(ApprovalStatus,on_delete=models.DO_NOTHING,default=1)
    approval_comment=models.TextField(blank=True,null=True)
    approval_date=models.DateField(blank=True,null=True)
    
    certification_officer=models.ForeignKey(CertificationOfficers,on_delete=models.DO_NOTHING,blank=True,null=True)
    certification_status = models.ForeignKey(CertificationStatus,on_delete=models.DO_NOTHING,default=1)
    certification_comment=models.TextField(blank=True,null=True)
    certification_date=models.DateField(blank=True,null=True)
 

    processed_by=models.ForeignKey(CustomUser,on_delete=models.CASCADE,blank=True,null=True)
    

    status= models.ForeignKey(TransactionStatus,on_delete=models.DO_NOTHING,default=1)
    maturity_date=models.DateField(blank=True,null=True)
   

    class Meta(DateObjectsModels.Meta):
        db_table="Members_Cash_Withdrawals_Application"


class MembersCashWithdrawalsMain(DateObjectsModels):
    member=models.ForeignKey(MembersCashWithdrawalsApplication,on_delete=models.CASCADE,blank=True,null=True)
    channel=models.ForeignKey(PaymentChannels,on_delete=models.CASCADE,blank=True,null=True)
    payment_date=models.DateField(blank=True,null=True)
    coop_account=models.ForeignKey(CooperativeBankAccounts,on_delete=models.DO_NOTHING,blank=True,null=True)
    member_account=models.ForeignKey(MembersBankAccounts,on_delete=models.DO_NOTHING,blank=True,null=True)
    cheque_number=models.CharField(max_length=255,blank=True,null=True)
   
    disbursement_officer=models.ForeignKey(DisbursementOfficers,on_delete=models.DO_NOTHING,blank=True,null=True)
    disbursement_status = models.ForeignKey(ApprovalStatus,on_delete=models.DO_NOTHING,default=1)
    disbursement_date=models.DateField(blank=True,null=True)
   
    processed_by=models.ForeignKey(CustomUser,on_delete=models.CASCADE,blank=True,null=True)
    status= models.ForeignKey(TransactionStatus,on_delete=models.DO_NOTHING,default=1)
    

    class Meta(DateObjectsModels.Meta):
        db_table="Members_Cash_Withdrawals_Main"


####################################################################
##################### LEDGER AND CASH BOOK #######################
####################################################################

class PersonalLedger(DateObjectsModels):
    member=models.ForeignKey(Members,on_delete=models.CASCADE,blank=True,null=True)
    transaction=models.ForeignKey(TransactionTypes,on_delete=models.CASCADE,blank=True,null=True)
    account_number=models.CharField(max_length=255)
    particulars=models.CharField(max_length=255)
    debit=models.DecimalField(max_digits=20,decimal_places = 2,default=0)
    credit=models.DecimalField(max_digits=20,decimal_places = 2,default=0)
    balance=models.DecimalField(max_digits=20,decimal_places = 2,default=0)
    transaction_period=models.DateField()
    status=models.ForeignKey(MembershipStatus,on_delete=models.CASCADE,default=1)
   

    class Meta(DateObjectsModels.Meta):
        db_table="Personal_Ledger"

class CashBook(DateObjectsModels):
    particulars=models.CharField(max_length=255)
    debit=models.DecimalField(max_digits=20,decimal_places = 2,default=0)
    credit=models.DecimalField(max_digits=20,decimal_places = 2,default=0)
    balance=models.DecimalField(max_digits=20,decimal_places = 2,default=0)
    ref_no=models.CharField(max_length=255)
    processed_by=models.ForeignKey(CustomUser,on_delete=models.CASCADE,blank=True,null=True)
    status=models.ForeignKey(MembershipStatus,on_delete=models.CASCADE,default=1)
    
    class Meta(DateObjectsModels.Meta):
        db_table="Cashbook"


####################################################################
##################### COOPERATIVE SHOP #############################
####################################################################
class Stock(DateObjectsModels):
    category= models.ForeignKey(ProductCategory,on_delete=models.DO_NOTHING,blank=True,null=True)
    code=models.CharField(max_length=255,unique=True)
    item_name=models.CharField(max_length=255)
    details=models.CharField(max_length=255,blank=True,null=True)
    quantity=models.IntegerField(default=0)
    unit_selling_price=models.DecimalField(max_digits=20,decimal_places = 2)
    unit_cost_price=models.DecimalField(max_digits=20,decimal_places = 2,default=0)
    re_order_level=models.IntegerField(default=0)
    no_in_pack=models.IntegerField(default=0)
    lock_status=models.ForeignKey(LockedStatus,on_delete=models.DO_NOTHING,default=1)


    class Meta(DateObjectsModels.Meta):
        db_table="Stock"

    # def __str__(self):
    #     return self.item_name + " " + str(self.quantity)


class Members_Credit_Sales_Selected(DateObjectsModels):
    member=models.ForeignKey(Members,on_delete=models.DO_NOTHING,blank=True,null=True)
    product= models.ForeignKey(Stock,on_delete=models.DO_NOTHING,blank=True,null=True)
    ticket=models.CharField(max_length=255)
    quantity=models.IntegerField(default=0)
    unit_selling_price=models.DecimalField(max_digits=20,decimal_places = 2)
    total=models.DecimalField(max_digits=20,decimal_places = 2)
    processed_by=models.ForeignKey(CustomUser,on_delete=models.DO_NOTHING,blank=True,null=True)
    status=models.ForeignKey(TransactionStatus,on_delete=models.DO_NOTHING,blank=True,null=True)
   
    class Meta(DateObjectsModels.Meta):
        db_table="Members_Credit_Sales_Selected"

class Members_Credit_Sales_external_fascilities(DateObjectsModels):
    trans_code=models.ForeignKey(Members_Credit_Sales_Selected,on_delete=models.CASCADE,blank=True,null=True)
    description=models.CharField(max_length=255)
    amount=models.DecimalField(max_digits=20,decimal_places = 2)
    status=models.ForeignKey(TransactionStatus,on_delete=models.DO_NOTHING,blank=True,null=True)
    
    class Meta(DateObjectsModels.Meta):
        db_table="Members_Credit_Sales_External_Fascilities"

class members_credit_purchase_summary(DateObjectsModels):
    trans_code= models.ForeignKey(Members_Credit_Sales_Selected,on_delete=models.CASCADE,blank=True,null=True)
    debit=models.DecimalField(max_digits=20,decimal_places = 2)
    credit=models.DecimalField(max_digits=20,decimal_places = 2)
    balance=models.DecimalField(max_digits=20,decimal_places = 2)
    approval_officer=models.ForeignKey(ApprovalOfficers,on_delete=models.DO_NOTHING,blank=True,null=True)
    approval_status=models.ForeignKey(ApprovalStatus,on_delete=models.DO_NOTHING,blank=True,null=True)
    approval_comment=models.TextField()
    approval_date=models.DateField(blank=True,null=True)
    status=models.ForeignKey(TransactionStatus,on_delete=models.DO_NOTHING,blank=True,null=True)
    
    class Meta(DateObjectsModels.Meta):
        db_table="Members_Credit_Purchase_Summary"

class members_credit_purchase_analysis(DateObjectsModels):
    trans_code= models.ForeignKey(Members_Credit_Sales_Selected,on_delete=models.CASCADE,blank=True,null=True)
    particulars=models.CharField(max_length=255,blank=True,null=True)
    debit=models.DecimalField(max_digits=20,decimal_places = 2)
    credit=models.DecimalField(max_digits=20,decimal_places = 2)
    status=models.ForeignKey(TransactionStatus,on_delete=models.DO_NOTHING,blank=True,null=True)
   
    class Meta(DateObjectsModels.Meta):
        db_table="Members_Credit_Purchase_Analysis"

class Members_Cash_Sales_Selected(DateObjectsModels):
    member=models.ForeignKey(Members,on_delete=models.CASCADE,blank=True,null=True)
    product= models.ForeignKey(Stock,on_delete=models.CASCADE,blank=True,null=True)
    ticket=models.CharField(max_length=255)
    quantity=models.IntegerField(default=0)
    unit_selling_price=models.DecimalField(max_digits=20,decimal_places = 2)
    total=models.DecimalField(max_digits=20,decimal_places = 2)
    processed_by=models.ForeignKey(CustomUser,on_delete=models.CASCADE,blank=True,null=True)
    status=models.ForeignKey(TransactionStatus,on_delete=models.CASCADE,blank=True,null=True)
   
    class Meta(DateObjectsModels.Meta):
        db_table="Members_Cash_Sales_Selected"

class Customers(DateObjectsModels):
    customer_id=models.CharField(max_length=255,unique=True)
    name=models.CharField(max_length=255,default='Anonymous')
    phone_no=models.CharField(max_length=255,default='Anonymous')
    address=models.CharField(max_length=255,default='Anonymous')
    birthdate=models.DateField(blank=True,null=True)
    status=models.ForeignKey(ReceiptStatus,on_delete=models.CASCADE,blank=True, null=True)
    cust_status=models.ForeignKey(MembershipStatus,on_delete=models.CASCADE,blank=True, null=True)
    active_ticket=models.CharField(max_length=255,blank=True, null=True)
    ticket_status=models.ForeignKey(TicketStatus,on_delete=models.CASCADE,blank=True, null=True)
    locked_status=models.ForeignKey(LockedStatus,on_delete=models.CASCADE,default=1)
    processed_by=models.ForeignKey(CustomUser,on_delete=models.DO_NOTHING,blank=True,null=True)

    class Meta(DateObjectsModels.Meta):
        db_table="Customers"


class General_Cash_Sales_Selected(DateObjectsModels):
    customer=models.ForeignKey(Customers,on_delete=models.CASCADE,blank=True,null=True)
    product= models.ForeignKey(Stock,on_delete=models.CASCADE,blank=True,null=True)
    ticket=models.CharField(max_length=255)
    quantity=models.IntegerField(default=0)
    unit_selling_price=models.DecimalField(max_digits=20,decimal_places = 2)
    total=models.DecimalField(max_digits=20,decimal_places = 2)
    processed_by=models.ForeignKey(CustomUser,on_delete=models.CASCADE,blank=True,null=True)
    status=models.ForeignKey(TransactionStatus,on_delete=models.CASCADE,blank=True,null=True)
   
    class Meta(DateObjectsModels.Meta):
        db_table="General_Cash_Sales_Selected"

class General_Cash_Sales_SelectedTemp(DateObjectsModels):
    customer=models.ForeignKey(Customers,on_delete=models.CASCADE,blank=True,null=True)
    product= models.ForeignKey(Stock,on_delete=models.CASCADE,blank=True,null=True)
    ticket=models.CharField(max_length=255)
    quantity=models.IntegerField(default=0)
    unit_selling_price=models.DecimalField(max_digits=20,decimal_places = 2)
    total=models.DecimalField(max_digits=20,decimal_places = 2)
    processed_by=models.ForeignKey(CustomUser,on_delete=models.CASCADE,blank=True,null=True)
    status=models.ForeignKey(TransactionStatus,on_delete=models.CASCADE,blank=True,null=True)
    

    class Meta(DateObjectsModels.Meta):
        db_table="General_Cash_Sales_Selected_Temp"


class Daily_Sales(DateObjectsModels):
    ticket=models.CharField(max_length=255)
    name=models.CharField(max_length=255,default='Anonymous')
    phone_no=models.CharField(max_length=255,default='Anonymous')
    address=models.CharField(max_length=255,default='Anonymous')
    product=models.ForeignKey(Stock,on_delete=models.CASCADE,blank=True,null=True)
    item_code=models.CharField(max_length=255)
    item_name=models.CharField(max_length=255)
    quantity=models.IntegerField(default=0)
    receipt=models.CharField(max_length=20,blank=True,null=True)
    unit_selling_price=models.DecimalField(max_digits=20,decimal_places = 2)
    total=models.DecimalField(max_digits=20,decimal_places = 2)
    status=models.ForeignKey(TransactionStatus,on_delete=models.CASCADE,blank=True,null=True)
    processed_by=models.ForeignKey(CustomUser,on_delete=models.CASCADE,blank=True,null=True)
   

    class Meta(DateObjectsModels.Meta):
        db_table="Daily_Sales"


class Daily_Sales_Summary(DateObjectsModels):
    sale=models.ForeignKey(Daily_Sales,on_delete=models.CASCADE,blank=True,null=True)
    receipt=models.CharField(max_length=255)
    amount=models.DecimalField(max_digits=20,decimal_places = 2)
    sales_category=models.ForeignKey(SalesCategory,on_delete=models.CASCADE,blank=True,null=True)
    status=models.ForeignKey(TransactionStatus,on_delete=models.CASCADE,blank=True,null=True)
    
    class Meta(DateObjectsModels.Meta):
        db_table="Daily_Sales_Summary"


class Daily_Sales_Cash_Flow_Summary(DateObjectsModels):
    description=models.CharField(max_length=255)
    amount=models.DecimalField(max_digits=20,decimal_places = 2)
    sales_category=models.ForeignKey(SalesCategory,on_delete=models.CASCADE,blank=True,null=True)
    processed_by=models.ForeignKey(CustomUser,on_delete=models.CASCADE,blank=True,null=True)
    status=models.ForeignKey(TransactionStatus,on_delete=models.CASCADE,blank=True,null=True)
    

    class Meta(DateObjectsModels.Meta):
        db_table="Daily_Sales_Cash_Flow_Summary"

class Cheque_Table(DateObjectsModels):
    sales= models.ForeignKey(General_Cash_Sales_SelectedTemp,on_delete=models.CASCADE,blank=True,null=True)
    cheque_name=models.CharField(max_length=255)
    cheque_number=models.CharField(max_length=255)
    cheque_due_date=models.DateField()
    bank=models.ForeignKey(Banks,on_delete=models.CASCADE,blank=True,null=True)
    amount=models.DecimalField(max_digits=20,decimal_places = 2,default=0)
    approval_status=models.ForeignKey(ApprovalStatus,on_delete=models.CASCADE,default=1)
    status=models.ForeignKey(TransactionStatus,on_delete=models.CASCADE,blank=True,null=True)
    date_cleared=models.DateField(blank=True, null=True)
    
    class Meta(DateObjectsModels.Meta):
        db_table="Cheque_Table"

class Suppliers(DateObjectsModels):
    prefix=models.CharField(max_length=255,blank=True,null=True)
    name=models.CharField(max_length=255)

    
    class Meta(DateObjectsModels.Meta):
        db_table="Suppliers"


class Suppliers_Branches(DateObjectsModels):
    supplier= models.ForeignKey(Suppliers,on_delete=models.CASCADE)
    address=models.TextField()
    phone=models.CharField(max_length=255)
    
    class Meta(DateObjectsModels.Meta):
        db_table="Suppliers_Branches"


class Suppliers_Reps(DateObjectsModels):
    suppliers= models.ForeignKey(Suppliers,on_delete=models.DO_NOTHING)
    name=models.CharField(max_length=255)
    phone=models.CharField(max_length=255)
   
    class Meta(DateObjectsModels.Meta):
        db_table="Suppliers_Reps"

class Suppliers_Majors(DateObjectsModels):
    supplier= models.ForeignKey(Suppliers,on_delete=models.CASCADE)
    product=models.CharField(max_length=255)

    class Meta(DateObjectsModels.Meta):
        db_table="Suppliers_Majors"


class Purchase_Header(DateObjectsModels):
    branch= models.ForeignKey(Suppliers_Branches,on_delete=models.CASCADE)
    total_amount= models.DecimalField(max_digits=20,decimal_places = 2,default=0)
    invoice=models.CharField(max_length=255)
    invoice_date=models.DateField()
    personnel=models.ForeignKey(Suppliers_Reps,on_delete=models.DO_NOTHING,blank=True,null=True)
    processed_by=models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    status=models.ForeignKey(TransactionStatus,on_delete=models.CASCADE,default=1)
    certification_status=models.ForeignKey(CertificationStatus,on_delete=models.CASCADE,default=1)

    class Meta(DateObjectsModels.Meta):
        db_table="Purchase_Header"


class Purchases_Temp(DateObjectsModels):
    purchase= models.ForeignKey(Purchase_Header,on_delete=models.CASCADE)
    product= models.ForeignKey(Stock,on_delete=models.CASCADE)
    quantity=models.IntegerField(default=0)
    cost_price =models.DecimalField(max_digits=20,decimal_places = 2,default=0)
    total_cost= models.DecimalField(max_digits=20,decimal_places = 2,default=0)
    selling_price =models.DecimalField(max_digits=20,decimal_places = 2,default=0)
    
    class Meta(DateObjectsModels.Meta):
        db_table="Purchase_Temp"


class Purchases(DateObjectsModels):
    purchase= models.ForeignKey(Purchase_Header,on_delete=models.CASCADE)
    product= models.ForeignKey(Stock,on_delete=models.CASCADE)
    quantity=models.IntegerField(default=0)
    cost_price =models.DecimalField(max_digits=20,decimal_places = 2,default=0)
    total_cost= models.DecimalField(max_digits=20,decimal_places = 2,default=0)
    selling_price =models.DecimalField(max_digits=20,decimal_places = 2,default=0)
    status=models.ForeignKey(TransactionStatus,on_delete=models.CASCADE)

    class Meta(DateObjectsModels.Meta):
        db_table="Purchases"


 
class CooperativeShopLedger(DateObjectsModels):
    member= models.ForeignKey(MembersAccountsDomain,on_delete=models.CASCADE,blank=True,null=True)
    particulars=models.CharField(max_length=255,blank=True,null=True)
    debit=models.DecimalField(max_digits=20,decimal_places = 2)
    credit=models.DecimalField(max_digits=20,decimal_places = 2)
    balance=models.DecimalField(max_digits=20,decimal_places = 2)
    receipt = models.CharField(max_length=20,blank=True, null=True)
    processed_by=models.ForeignKey(CustomUser,on_delete=models.DO_NOTHING,blank=True,null=True)
    status= models.ForeignKey(TransactionStatus,on_delete=models.DO_NOTHING,default=1)
    
    class Meta(DateObjectsModels.Meta):
        db_table="Cooperative_Shop_Ledger"


class TaskManager(DateObjectsModels):
    description=models.TextField()
    processed_by=models.ForeignKey(CustomUser,on_delete=models.CASCADE,blank=True,null=True)
    
    class Meta(DateObjectsModels.Meta):
        db_table="Task_Manager"

@receiver(post_save,sender=CustomUser)
def create_user_profile(sender,instance,created,**kwargs):
    if created:
        if instance.user_type==1:
            AdminMASTER.objects.create(admin=instance)       
        if instance.user_type==2:
            Staff.objects.create(admin=instance,middle_name="",address="",phone_number="080",gender=Gender.objects.first())
        if instance.user_type==3:
            Staff.objects.create(admin=instance,middle_name="",address="",phone_number="080",gender=Gender.objects.first())
        if instance.user_type==4:
             Staff.objects.create(admin=instance,middle_name="",address="",phone_number="080",gender=Gender.objects.first()) 
        if instance.user_type==5:
             Staff.objects.create(admin=instance,middle_name="",address="",phone_number="080",gender=Gender.objects.first()) 
        if instance.user_type==6:
            Staff.objects.create(admin=instance,middle_name="",address="",phone_number="080",gender=Gender.objects.first())
        if instance.user_type==7:
             Staff.objects.create(admin=instance,middle_name="",address="",phone_number="080",gender=Gender.objects.first()) 
        if instance.user_type==8:
             Staff.objects.create(admin=instance,middle_name="",address="",phone_number="080",gender=Gender.objects.first())
        if instance.user_type==9:
             Staff.objects.create(admin=instance,middle_name="",address="",phone_number="080",gender=Gender.objects.first())
        if instance.user_type==10:
            Members.objects.create(admin=instance,member_id="",date_joined="2020-01-01",middle_name="",phone_number="",salary_institution=SalaryInstitution.objects.first(),applicant=MemberShipFormSalesRecord.objects.first(),file_no="",permanent_home_address="",residential_address="",profile_pic="",status=MembershipStatus.objects.first()) 

         
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
    if instance.user_type==4:
        instance.staff.save()
    if instance.user_type==5:
        instance.staff.save() 
    if instance.user_type==6:
        instance.staff.save()
    if instance.user_type==7:
        instance.staff.save() 
    if instance.user_type==8:
        instance.staff.save() 
    if instance.user_type==9:
        instance.staff.save() 
    if instance.user_type==10:
        instance.members.save() 

    class Meta(DateObjectsModels.Meta):
        db_table="Save_User_Profile"