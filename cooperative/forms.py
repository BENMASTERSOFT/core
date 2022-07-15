from django import forms
from cooperative.models import *
from django.db.models import Q

from datetime import datetime
from datetime import date
import datetime

from django.utils.dateparse import parse_date
from dateutil.relativedelta import relativedelta

now = datetime.datetime.now()

MONTH_LIST =(('JANUARY','JANUARY'),
               ('FEBRUARY','FEBRUARY'),
               ('MARCH','MARCH'),
               ('APRIL','APRIL'),
               ('MAY','MAY'),
               ('JUNE','JUNE'),
               ('JULY','JULY'),
               ('AUGUST','AUGUST'),
               ('SEPTEMBER','SEPTEMBER'),
               ('OCTOBER','OCTOBER'),
               ('NOVEMBER','NOVEMBER'),
               ('DECEMBER','DECEMBER'))

TRANSACTION_RANGE =(
      ("SELECTED DATE", "SELECTED DATE"),
      ("ALL RECORDS", "ALL RECORDS"),
   )
FORM_PRINT_CHOICES =(
      ("NO", "NO"),
      ("YES", "YES"),
   )

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
                ("TRANSFER","TRANSFER")
                )

WITHDRAWAL_STATUS=(
        ("LOCKED","LOCKED"),
        ("UNLOCKED","UNLOCKED")
        )
LOAN_CATEGORY=(
            ("MONETARY","MONETARY"),
            ("NON-MONETARY","NON-MONETARY")
            )

class DateInput(forms.DateInput):
	input_type = "date"

class TimePickerInput(forms.TimeInput):
     input_type = 'time'

class DateTimePickerInput(forms.DateTimeInput):
     input_type = 'datetime'


class searchForm(forms.Form):
   title = forms.CharField(label="", widget=forms.TextInput(attrs={"class":"form-control mb-4 mr-sm-4 mb-sm-0", "placeholder":"Search",'autocomplete':'off'}),required=False)




class addUserTypesForm(forms.ModelForm):
   class Meta:
      model = UserType
      fields=['code','title']

      widgets = {
      'code': forms.TextInput(attrs={'class':'form-control','placeholder':"Enter Code"}),
      'title': forms.TextInput(attrs={'class':'form-control','placeholder':"Enter Title"})
      }

   def clean_code(self):
      code = self.cleaned_data.get('code')
      if not code:
         raise forms.ValidationError('This field is required')

      for instance in UserType.objects.all():
         if instance.code == code:
            raise forms.ValidationError(str(code) + ' is already created')
      return code

   def clean_title(self):
      title = self.cleaned_data.get('title')
      if not title:
         raise forms.ValidationError('This field is required')

      for instance in UserType.objects.all():
         if instance.title == title:
            raise forms.ValidationError(str(title) + ' is already created')
      return title


class Executive_Positions_Form(forms.Form):
   title=forms.CharField(label="Title",max_length=50,widget=forms.TextInput(attrs={"class":"form-control"}))




class Executive_Member_Select_Form(forms.Form):
  position_list=[]

  try:
      positions = ExecutivePositions.objects.all()
      for position in positions:
         small_position=(position.id,position.title)
         position_list.append(small_position)
  except:
      position_list=[]

  position=forms.ChoiceField(label="Position",choices=position_list,widget=forms.Select(attrs={"class":"form-control"}))

  elias=forms.CharField(label="Elias",max_length=50,widget=forms.TextInput(attrs={"class":"form-control"}))

  name=forms.CharField(label="Name",max_length=50,widget=forms.TextInput(attrs={"class":"form-control",'readonly':'readonly'}))
  start_date = forms.DateField(label='Start Date', label_suffix=" : ",
                             required=True, disabled=False,
                             widget=DateInput(attrs={'class': 'form-control'}),
                             error_messages={'required': "This field is required."})

  stop_date = forms.DateField(label='Stop Date', label_suffix=" : ",
                             required=True, disabled=False,
                             widget=DateInput(attrs={'class': 'form-control'}),
                             error_messages={'required': "This field is required."})



class Monthly_Deduction_Covering_Note_Form(forms.Form):
  staff1_list=[]

  try:
      staff1s = Executives.objects.filter(status='ACTIVE')
      for staff1 in staff1s:
         small_staff1=(staff1.id,staff1.name)
         staff1_list.append(small_staff1)
  except:
      staff1_list=[]

  staff1=forms.ChoiceField(label="Staff1",choices=staff1_list,widget=forms.Select(attrs={"class":"form-control"}))

  staff2_list=[]

  try:
      staff2s = Executives.objects.filter(status='ACTIVE')
      for staff2 in staff2s:
         small_staff2=(staff2.id,staff2.name)
         staff2_list.append(small_staff2)
  except:
      staff2_list=[]

  staff2=forms.ChoiceField(label="Staff2",choices=staff2_list,widget=forms.Select(attrs={"class":"form-control"}))


  account_list=[]

  try:
      accounts = CooperativeBankAccounts.objects.all()
      for account in accounts:
         small_account=(account.id,'{}-{}({})'.format(account.account_name,account.account_number,account.bank.title))
         account_list.append(small_account)
  except:
      account_list=[]

  account=forms.ChoiceField(label="Account",choices=account_list,widget=forms.Select(attrs={"class":"form-control"}))

  transaction_date = forms.DateField(label='Transaction Date', label_suffix=" : ",
                             required=True, disabled=False,
                             widget=DateInput(attrs={'class': 'form-control'}),
                             error_messages={'required': "This field is required."})

  print_date = forms.DateField(label='Print Date', label_suffix=" : ",
                             required=True, disabled=False,
                             widget=DateInput(attrs={'class': 'form-control'}),
                             error_messages={'required': "This field is required."})





class Executive_Form(forms.Form):
   name=forms.CharField(label="Title",max_length=150,widget=forms.TextInput(attrs={"class":"form-control"}))




class addUsersForm(forms.Form):
   title_list=[]

   try:
      titles = Titles.objects.all().order_by("title")
      for title in titles:
         small_title=(title.id,title.title)
         title_list.append(small_title)
   except:
      title_list=[]

   title=forms.ChoiceField(label="title",choices=title_list,widget=forms.Select(attrs={"class":"form-control"}))
   last_name=forms.CharField(label="Last Name",max_length=50,widget=forms.TextInput(attrs={"class":"form-control"}))
   first_name=forms.CharField(label="First Name",max_length=50,widget=forms.TextInput(attrs={"class":"form-control"}))
   middle_name=forms.CharField(label="Middle Name",max_length=50,required=False, widget=forms.TextInput(attrs={"class":"form-control"}))
   address=forms.CharField(label="Address",max_length=150,widget=forms.TextInput(attrs={"class":"form-control"}))
   phone_no=forms.CharField(label="Phone No",max_length=11,widget=forms.TextInput(attrs={"class":"form-control"}))

   gender_list=[]
   try:
      genders = Gender.objects.all()
      for gender in genders:
         small_gender=(gender.id,gender.title)
         gender_list.append(small_gender)
   except:
      gender_list=[]

   gender=forms.ChoiceField(label="Gender",choices=gender_list,widget=forms.Select(attrs={"class":"form-control"}))


   email=forms.EmailField(label="Email",max_length=50,widget=forms.EmailInput(attrs={"class":"form-control"}))
   username=forms.CharField(label="Username",max_length=50,widget=forms.TextInput(attrs={"class":"form-control"}))


   user_type_list=[]

   try:
      user_types = UserType.objects.all()
      for user_type in user_types:
         small_user_type=(user_type.id,user_type.title)
         user_type_list.append(small_user_type)
   except:
      user_type_list=[]

   user_type=forms.ChoiceField(label="user_type",choices=user_type_list,widget=forms.Select(attrs={"class":"form-control"}))






class add_staff_manage_form(forms.Form):
   title_list=[]

   try:
      titles = Titles.objects.all()
      for title in titles:
         small_title=(title.id,title.title)
         title_list.append(small_title)
   except:
      title_list=[]

   title=forms.ChoiceField(label="title",choices=title_list,widget=forms.Select(attrs={"class":"form-control"}))
   last_name=forms.CharField(label="Last Name",max_length=50,widget=forms.TextInput(attrs={"class":"form-control"}))
   first_name=forms.CharField(label="First Name",max_length=50,widget=forms.TextInput(attrs={"class":"form-control"}))
   middle_name=forms.CharField(label="Middle Name",max_length=50,required=False, widget=forms.TextInput(attrs={"class":"form-control"}))
   address=forms.CharField(label="Address",max_length=150,widget=forms.TextInput(attrs={"class":"form-control"}))
   phone_no=forms.CharField(label="Phone No",max_length=11,widget=forms.TextInput(attrs={"class":"form-control"}))

   gender_list=[]
   try:
      genders = Gender.objects.all()
      for gender in genders:
         small_gender=(gender.id,gender.title)
         gender_list.append(small_gender)
   except:
      gender_list=[]

   gender=forms.ChoiceField(label="Gender",choices=gender_list,widget=forms.Select(attrs={"class":"form-control"}))


   email=forms.EmailField(label="Email",max_length=50,widget=forms.EmailInput(attrs={"class":"form-control"}))
   username=forms.CharField(label="Username",max_length=50,widget=forms.TextInput(attrs={"class":"form-control"}))
   password1 = forms.CharField(required=False,widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}))
   password2 = forms.CharField(required=False,widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Repeat Password'}))


   user_type_list=[]

   try:
      user_types = UserType.objects.all()
      for user_type in user_types:
         small_user_type=(user_type.id,user_type.title)
         user_type_list.append(small_user_type)
   except:
      user_type_list=[]

   user_type=forms.ChoiceField(label="user_type",choices=user_type_list,widget=forms.Select(attrs={"class":"form-control"}))




class super_user_manage_form(forms.Form):

   last_name=forms.CharField(label="Last Name",max_length=50,widget=forms.TextInput(attrs={"class":"form-control"}))
   first_name=forms.CharField(label="First Name",max_length=50,widget=forms.TextInput(attrs={"class":"form-control"}))

   email=forms.EmailField(label="Email",max_length=50,widget=forms.EmailInput(attrs={"class":"form-control"}))
   username=forms.CharField(label="Username",max_length=50,widget=forms.TextInput(attrs={"class":"form-control"}))
   password1 = forms.CharField(required=False,widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}))
   password2 = forms.CharField(required=False,widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Repeat Password'}))


   user_type_list=[]

   try:
      user_types = UserType.objects.all()
      for user_type in user_types:
         small_user_type=(user_type.id,user_type.title)
         user_type_list.append(small_user_type)
   except:
      user_type_list=[]

   user_type=forms.ChoiceField(label="user_type",choices=user_type_list,widget=forms.Select(attrs={"class":"form-control"}))




class Useraccount_manager_form(forms.Form):
   username=forms.CharField(label="Username",max_length=50,widget=forms.TextInput(attrs={"class":"form-control"}))
   password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}))
   password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Repeat Password'}))


class addCompaniesForm(forms.ModelForm):
   class Meta:
      model = Companies
      fields=['title',]

      widgets = {
      'title': forms.TextInput(attrs={'class':'form-control','placeholder':"Enter Title"})
      }


   def clean_title(self):
      title = self.cleaned_data.get('title')
      if not title:
         raise forms.ValidationError('This field is required')

      for instance in Companies.objects.all():
         if instance.title == title:
            raise forms.ValidationError(str(title) + ' is already created')
      return title




class addStateForm(forms.ModelForm):
   class Meta:
      model = States
      fields=['title',]

      widgets = {
      'title': forms.TextInput(attrs={'class':'form-control','placeholder':"Enter Title"})
      }


   def clean_title(self):
      title = self.cleaned_data.get('title')
      if not title:
         raise forms.ValidationError('This field is required')

      for instance in States.objects.all():
         if instance.title == title:
            raise forms.ValidationError(str(title) + ' is already created')
      return title

class addExpiringDateIntervalForm(forms.ModelForm):
   class Meta:
      model = ExpiringDateInterval
      fields=['title',]

      widgets = {
      'title': forms.TextInput(attrs={'class':'form-control','placeholder':"Enter Title"})
      }


   def clean_title(self):
      title = self.cleaned_data.get('title')
      if not title:
         raise forms.ValidationError('This field is required')
      return title

class addCooperativeOperationsForm(forms.ModelForm):
   class Meta:
      model = CooperativeOperations
      fields=['title',]

      widgets = {
      'title': forms.TextInput(attrs={'class':'form-control','placeholder':"Enter Title"})
      }


   def clean_title(self):
      title = self.cleaned_data.get('title')
      if not title:
         raise forms.ValidationError('This field is required')

      for instance in CooperativeOperations.objects.all():
         if instance.title == title:
            raise forms.ValidationError(str(title) + ' is already created')
      return title


class addItemWriteOffReasonsForm(forms.ModelForm):
   class Meta:
      model = ItemWriteOffReasons
      fields=['title',]

      widgets = {
      'title': forms.TextInput(attrs={'class':'form-control','placeholder':"Enter Title"})
      }


   def clean_title(self):
      title = self.cleaned_data.get('title')
      if not title:
         raise forms.ValidationError('This field is required')

      for instance in ItemWriteOffReasons.objects.all():
         if instance.title == title:
            raise forms.ValidationError(str(title) + ' is already created')
      return title


class addNOKRelationshipsForm(forms.ModelForm):
   class Meta:
      model = NOKRelationships
      fields=['title',]

      widgets = {
      'title': forms.TextInput(attrs={'class':'form-control','placeholder':"Enter Title"})
      }


   def clean_title(self):
      title = self.cleaned_data.get('title')
      if not title:
         raise forms.ValidationError('This field is required')

      for instance in NOKRelationships.objects.all():
         if instance.title == title:
            raise forms.ValidationError(str(title) + ' is already created')
      return title


class addGenderForm(forms.ModelForm):
   class Meta:
      model = Gender
      fields=['title',]

      widgets = {
      'title': forms.TextInput(attrs={'class':'form-control','placeholder':"Enter Title"})
      }


   def clean_title(self):
      title = self.cleaned_data.get('title')
      if not title:
         raise forms.ValidationError('This field is required')

      for instance in Gender.objects.all():
         if instance.title == title:
            raise forms.ValidationError(str(title) + ' is already created')
      return title



class addTitlesForm(forms.ModelForm):
   class Meta:
      model = Titles
      fields=['title',]

      widgets = {
      'title': forms.TextInput(attrs={'class':'form-control','placeholder':"Enter Title"})
      }


   def clean_title(self):
      title = self.cleaned_data.get('title')
      if not title:
         raise forms.ValidationError('This field is required')

      for instance in Titles.objects.all():
         if instance.title == title:
            raise forms.ValidationError(str(title) + ' is already created')
      return title





class addTransactionSourcesForm(forms.ModelForm):
   class Meta:
      model = TransactionSources
      fields=['title',]

      widgets = {
      'title': forms.TextInput(attrs={'class':'form-control','placeholder':"Enter Title"})
      }


   def clean_title(self):
      title = self.cleaned_data.get('title')
      if not title:
         raise forms.ValidationError('This field is required')

      for instance in TransactionSources.objects.all():
         if instance.title == title:
            raise forms.ValidationError(str(title) + ' is already created')
      return title



class addSalaryInstitutionForm(forms.ModelForm):
   class Meta:
      model = SalaryInstitution
      fields=['title',]

      widgets = {
      'title': forms.TextInput(attrs={'class':'form-control','placeholder':"Enter Title"})
      }


   def clean_title(self):
      title = self.cleaned_data.get('title')
      if not title:
         raise forms.ValidationError('This field is required')

      for instance in SalaryInstitution.objects.all():
         if instance.title == title:
            raise forms.ValidationError(str(title) + ' is already created')
      return title


class addDefaultPasswordForm(forms.ModelForm):
   class Meta:
      model = DefaultPassword
      fields=['title',]

      widgets = {
      'title': forms.TextInput(attrs={'class':'form-control','placeholder':"Enter Password"})
      }


   def clean_title(self):
      title = self.cleaned_data.get('title')
      if not title:
         raise forms.ValidationError('This field is required')

      for instance in DefaultPassword.objects.all():
         if instance.title == title:
            raise forms.ValidationError(str(title) + ' is already created')
      return title


class addDepartmentsForm(forms.ModelForm):
   class Meta:
      model = Departments
      fields=['title',]

      widgets = {
      'title': forms.TextInput(attrs={'class':'form-control','placeholder':"Enter Title"})
      }


   def clean_title(self):
      title = self.cleaned_data.get('title')
      if not title:
         raise forms.ValidationError('This field is required')

      for instance in Departments.objects.all():
         if instance.title == title:
            raise forms.ValidationError(str(title) + ' is already created')
      return title


class addBanksForm(forms.ModelForm):
   class Meta:
      model = Banks
      fields=['title',]

      widgets = {
      'title': forms.TextInput(attrs={'class':'form-control','placeholder':"Enter Title"})
      }


   def clean_title(self):
      title = self.cleaned_data.get('title')
      if not title:
         raise forms.ValidationError('This field is required')

      for instance in Banks.objects.all():
         if instance.title == title:
            raise forms.ValidationError(str(title) + ' is already created')
      return title


class addLocationsForm(forms.ModelForm):
   class Meta:
      model = Locations
      fields=['title',]

      widgets = {
      'title': forms.TextInput(attrs={'class':'form-control','placeholder':"Enter Title"})
      }


   def clean_title(self):
      title = self.cleaned_data.get('title')
      if not title:
         raise forms.ValidationError('This field is required')

      for instance in Locations.objects.all():
         if instance.title == title:
            raise forms.ValidationError(str(title) + ' is already created')
      return title



class addTransactionTypes_update_Form(forms.Form):
   receipts = forms.ChoiceField(label="Receipts", choices=RECEIPT_TYPES,widget=forms.Select(attrs={"class":"form-control"}))

   source_list=[]
   try:
      sources = TransactionSources.objects.all()
      for source in sources:
         small_source=(source.id,source.title)
         source_list.append(small_source)
   except:
      source_list=[]

   source = forms.ChoiceField(label="sources", choices=source_list,widget=forms.Select(attrs={"class":"form-control"}))

   form_print = forms.ChoiceField(label="Form Prints", choices=YESNO,widget=forms.Select(attrs={"class":"form-control"}))


   code=forms.CharField(label="Code",max_length=50,widget=forms.TextInput(attrs={"class":"form-control"}))
   name=forms.CharField(label="Name",max_length=50,widget=forms.TextInput(attrs={"class":"form-control"}))
   rank = forms.IntegerField(initial=0,label='Enter Rank', label_suffix=" : ", min_value=0,  required=True,
                                 widget=forms.NumberInput(attrs={'class': 'form-control'}),
                                help_text="This value is greater than or equal to 0 & less than or equal to 100.",
                                disabled = False, error_messages={'required': "Please Enter Rank."})

   share_unit_min = forms.IntegerField(initial=0,label='Share Unit Min', label_suffix=" : ", min_value=0,  required=False,
                                 widget=forms.NumberInput(attrs={'class': 'form-control'}),
                                disabled = False, error_messages={'required': "Please Min Unit"})

   share_unit_max = forms.IntegerField(initial=0,label='Share Unit Min', label_suffix=" : ", min_value=0,  required=False,
                                 widget=forms.NumberInput(attrs={'class': 'form-control'}),
                                disabled = False, error_messages={'required': "Please Min Unit"})

   maximum_amount = forms.DecimalField(initial=0,label='Maximum Amount', label_suffix=" : ", min_value=0,  max_digits=20,
                              widget=forms.NumberInput(attrs={'class': 'form-control'}),
                              decimal_places=2, required=False,
                              disabled = False,
                              error_messages={'required': "Please Enter Maximum amount."})


   minimum_amount = forms.DecimalField(initial=0,label='Minimum Amount', label_suffix=" : ", min_value=0,  max_digits=20,
                              widget=forms.NumberInput(attrs={'class': 'form-control'}),
                              decimal_places=1, required=False,
                              disabled = False,
                              error_messages={'required': "Please Enter Minimum amount."})



class addTransactionTypesForm(forms.Form):
   receipts = forms.ChoiceField(label="Receipts", choices=RECEIPT_TYPES,widget=forms.Select(attrs={"class":"form-control"}))

   source_list=[]
   try:
      sources = TransactionSources.objects.all()
      for source in sources:
         small_source=(source.id,source.title)
         source_list.append(small_source)
   except:
      source_list=[]

   source = forms.ChoiceField(label="sources", choices=source_list,widget=forms.Select(attrs={"class":"form-control"}))
   code=forms.CharField(label="Code",max_length=50,widget=forms.TextInput(attrs={"class":"form-control"}))
   name=forms.CharField(label="Name",max_length=50,widget=forms.TextInput(attrs={"class":"form-control"}))
   rank = forms.IntegerField(initial=0,label='Enter Rank', label_suffix=" : ", min_value=0,  required=True,
                                 widget=forms.NumberInput(attrs={'class': 'form-control'}),
                                help_text="This value is greater than or equal to 0 & less than or equal to 100.",
                                disabled = False, error_messages={'required': "Please Enter Rank."})

   share_unit_min = forms.IntegerField(initial=0,label='Share Unit Min', label_suffix=" : ", min_value=0,  required=False,
                                 widget=forms.NumberInput(attrs={'class': 'form-control'}),
                                disabled = False, error_messages={'required': "Please Min Unit"})

   share_unit_max = forms.IntegerField(initial=0,label='Share Unit Min', label_suffix=" : ", min_value=0,  required=False,
                                 widget=forms.NumberInput(attrs={'class': 'form-control'}),
                                disabled = False, error_messages={'required': "Please Min Unit"})


   maximum_amount = forms.DecimalField(initial=0,label='Maximum Amount', label_suffix=" : ", min_value=0,  max_digits=20,
                              widget=forms.NumberInput(attrs={'class': 'form-control'}),
                              decimal_places=2, required=False,
                              disabled = False,
                              error_messages={'required': "Please Enter Maximum amount."})


   minimum_amount = forms.DecimalField(initial=0,label='Minimum Amount', label_suffix=" : ", min_value=0,  max_digits=20,
                              widget=forms.NumberInput(attrs={'class': 'form-control'}),
                              decimal_places=1, required=False,
                              disabled = False,
                              error_messages={'required': "Please Enter Minimum amount."})


   def clean_rank(self):
      rank = self.cleaned_data.get('rank')
      if not rank:
         raise forms.ValidationError('This field is required')

      for instance in Locations.objects.all():
         if instance.rank == rank:
            raise forms.ValidationError(str(rank) + ' is already created')
      return rank



class LoanBasedSavingsForm(forms.Form):

   saving_list=[]
   try:
      source=TransactionSources.objects.get(title='SAVINGS')
      savings = TransactionTypes.objects.filter(source_id=source)
      for saving in savings:
         small_saving=(saving.id,saving.name)
         saving_list.append(small_saving)
   except:
      saving_list=[]

   saving = forms.ChoiceField(label="savings", choices=saving_list,widget=forms.Select(attrs={"class":"form-control"}))


class loan_guarantors_update_form(forms.Form):
   guarantors=forms.CharField(label="Guarnators",max_length=50,widget=forms.TextInput(attrs={"class":"form-control"}))


class loan_guarantors_gross_pay_update_form(forms.Form):
   guarantors_gross_pay_rating=forms.CharField(label="Guarnator Gross Pay",max_length=50,widget=forms.TextInput(attrs={"class":"form-control"}))


class loan_duration_update_form(forms.Form):
   duration=forms.CharField(label="Duration",max_length=50,widget=forms.TextInput(attrs={"class":"form-control"}))


class  default_admin_charges_update_form(forms.Form):
   default_admin_charges=forms.CharField(label="Default Admin Charges",max_length=50,widget=forms.TextInput(attrs={"class":"form-control"}))


class  MultipleLoanStatus_update_form(forms.Form):

   multiple_loan_status = forms.ChoiceField(label="Status", choices=MULTIPLE_LOAN_STATUS,widget=forms.Select(attrs={"class":"form-control"}))


class  auto_stop_savings_update_form(forms.Form):
   auto_stop_savings = forms.ChoiceField(label="Stop Savings", choices=FORM_PRINT_CHOICES,widget=forms.Select(attrs={"class":"form-control"}))

class  receipt_types_settings_form(forms.Form):
   receipt_type = forms.ChoiceField(label="Receipt Types", choices=RECEIPT_TYPES,widget=forms.Select(attrs={"class":"form-control"}))

class loan_savings_based_update_form(forms.Form):
   loan_savings_based=forms.CharField(label="Savings Ratio",max_length=50,widget=forms.TextInput(attrs={"class":"form-control"}))

class loan_savings_based_Rate_update_form(forms.Form):
   loan_savings_based_rate=forms.CharField(label="Savings Ratio",max_length=50,widget=forms.TextInput(attrs={"class":"form-control"}))


class loan_name_update_form(forms.Form):
   name=forms.CharField(label="Name",max_length=50,widget=forms.TextInput(attrs={"class":"form-control"}))


class loan_interest_rate_update_form(forms.Form):
   interest_rate=forms.IntegerField(label='Enter Interest Rate', label_suffix=" : ", min_value=1,  required=False,
                                 widget=forms.NumberInput(attrs={'class': 'form-control'}),
                                help_text="This value is greater than or equal to 1 & less than or equal to 100.",
                                disabled = False, error_messages={'required': "Please Enter Admin Charges."})


class loan_interest_deduction_soucrces_Form(forms.Form):
   source = forms.ChoiceField(label="sources", choices=INTEREST_DEDUCTION,widget=forms.Select(attrs={"class":"form-control"}))

class loan_category_update_form(forms.Form):
   category = forms.ChoiceField(label="Category", choices=LOAN_CATEGORY,widget=forms.Select(attrs={"class":"form-control"}))





class loan_maximum_amount_update_form(forms.Form):
   maximum_amount = forms.DecimalField(initial=0,label='Maximum Amount', label_suffix=" : ", min_value=0,  max_digits=20,
                              widget=forms.NumberInput(attrs={'class': 'form-control'}),
                              decimal_places=2, required=False,
                              disabled = False,
                              error_messages={'required': "Please Enter Maximum amount."})

class loan_rank_update_form(forms.Form):
   rank = forms.IntegerField(initial=0,label='Enter Rank', label_suffix=" : ", min_value=0,  required=True,
                                 widget=forms.NumberInput(attrs={'class': 'form-control'}),
                                help_text="This value is greater than or equal to 0 & less than or equal to 100.",
                                disabled = False, error_messages={'required': "Please Enter Rank."})

class SharesUnits_Max_Min_Values_form(forms.Form):
  share_unit_max = forms.IntegerField(initial=0,label='Share Unit Max', label_suffix=" : ", min_value=0,  required=True,
                                 widget=forms.NumberInput(attrs={'class': 'form-control'}),
                                help_text="This value is greater than or equal to 0 & less than or equal to 100.",
                                disabled = False, error_messages={'required': "Please Enter Rank."})
  share_unit_min = forms.IntegerField(initial=0,label='Share Unit Min', label_suffix=" : ", min_value=0,  required=True,
                                 widget=forms.NumberInput(attrs={'class': 'form-control'}),
                                help_text="This value is greater than or equal to 0 & less than or equal to 100.",
                                disabled = False, error_messages={'required': "Please Enter Rank."})

class Savings_Manager_Update_form(forms.Form):
  amount = forms.IntegerField(initial=0,label='Amount', label_suffix=" : ", min_value=0,  required=True,
                                 widget=forms.NumberInput(attrs={'class': 'form-control'}),
                                help_text="This value is greater than or equal to 0 & less than or equal to 100.",
                                disabled = False, error_messages={'required': "Please Enter Rank."})

  share_unit_min = forms.IntegerField(initial=0,label='Share Unit Min', label_suffix=" : ", min_value=0,  required=True,
                                 widget=forms.NumberInput(attrs={'class': 'form-control'}),
                                help_text="This value is greater than or equal to 0 & less than or equal to 100.",
                                disabled = False, error_messages={'required': "Please Enter Rank."})



class loan_admin_charges_rate_update_form(forms.Form):
   admin_charges_rating = forms.ChoiceField(label="Admin Charges Rating", choices=ADMIN_CHARGES,widget=forms.Select(attrs={"class":"form-control"}))


class loan_form_print_form(forms.Form):
   form_print = forms.ChoiceField(label="Form Print", choices=YESNO,widget=forms.Select(attrs={"class":"form-control"}))



class loan_admin_charges_update_form(forms.Form):
   admin_charges = forms.DecimalField(initial=0,label='Admin Charges Rate', label_suffix=" : ", min_value=0,  max_digits=20,
                              widget=forms.NumberInput(attrs={'class': 'form-control'}),
                              decimal_places=2, required=False,
                              disabled = False,
                              error_messages={'required': "Please Enter Admin Charges Minimum."})

class loan_admin_charges_minimum_update_form(forms.Form):
   admin_charges_minimum = forms.DecimalField(initial=0,label='Admin Charges Minimum', label_suffix=" : ", min_value=0,  max_digits=20,
                              widget=forms.NumberInput(attrs={'class': 'form-control'}),
                              decimal_places=2, required=False,
                              disabled = False,
                              error_messages={'required': "Please Enter Admin Charges Minimum."})


class loan_salary_relationship_update_form(forms.Form):
   salary_loan_relationship = forms.IntegerField(label='Enter Salary Loan Relationship', label_suffix=" : ", min_value=1,  required=False,
                                 widget=forms.NumberInput(attrs={'class': 'form-control'}),
                                help_text="This value is greater than or equal to 1 & less than or equal to 100.",
                                disabled = False, error_messages={'required': "Please Enter Admin Charges."})


class loan_Receipt_type_update_form(forms.Form):
   receipt_type = forms.ChoiceField(label="Receipt_ Types", choices=RECEIPT_TYPES,widget=forms.Select(attrs={"class":"form-control"}))




class loan_loan_age_update_form(forms.Form):
   loan_age = forms.IntegerField(label='Enter Loan Age', label_suffix=" : ", min_value=1,  required=False,
                                 widget=forms.NumberInput(attrs={'class': 'form-control'}),
                                help_text="This value is greater than or equal to 1 & less than or equal to 100.",
                                disabled = False, error_messages={'required': "Please Enter Admin Charges."})

class loan_admin_charges_minimum_update_form(forms.Form):
   admin_charges_minimum = forms.DecimalField(initial=0,label='Admin Charges Minimum', label_suffix=" : ", min_value=0,  max_digits=20,
                              widget=forms.NumberInput(attrs={'class': 'form-control'}),
                              decimal_places=2, required=False,
                              disabled = False,
                              error_messages={'required': "Please Enter Admin Charges Minimum."})


class MembershipRequest_form(forms.Form):

   titles_list=[]
   try:
      titles = Titles.objects.all()

      for title in titles:
         small_title=(title.id,title.title)
         titles_list.append(small_title)
   except:
      titles_list=[]

   titles = forms.ChoiceField(label="Title", choices=titles_list,widget=forms.Select(attrs={"class":"form-control"}))


   first_name=forms.CharField(label="First Name",max_length=50,widget=forms.TextInput(attrs={"class":"form-control"}))
   last_name=forms.CharField(label="Last Name",max_length=50,widget=forms.TextInput(attrs={"class":"form-control"}))
   middle_name=forms.CharField(label="Middle Name",max_length=50,widget=forms.TextInput(attrs={"class":"form-control"}),required=False)
   phone_no=forms.CharField(label="Phone Number",max_length=11,widget=forms.TextInput(attrs={"class":"form-control"}))

   gender_list=[]
   try:
      genders = Gender.objects.all()

      for gender in genders:
         small_gender=(gender.id,gender.title)
         gender_list.append(small_gender)
   except:
      gender_list=[]

   gender = forms.ChoiceField(label="Gender", choices=gender_list,widget=forms.Select(attrs={"class":"form-control"}))

   department_list=[]
   try:
      departments = Departments.objects.all()

      for department in departments:
         small_department=(department.id,department.title)
         department_list.append(small_department)
   except:
      department_list=[]

   department = forms.ChoiceField(label="Department", choices=department_list,widget=forms.Select(attrs={"class":"form-control"}))


class MemberShipRequestAdditionalInfo_form(forms.Form):
   approval_status = forms.ChoiceField(initial="APPROVED",label="Approval Status", choices=APPROVAL_STATUS,widget=forms.Select(attrs={"class":"form-control"}))
   comment= forms.CharField(widget=forms.Textarea(attrs={"rows":2, "cols":50}),required=True)
   date_approved= forms.DateField(label='Date Approved', label_suffix=" : ",
                             required=True, disabled=False,
                             widget=DateInput(attrs={'class': 'form-control'}),
                             error_messages={'required': "This field is required."})

   date_applied =forms.DateField(label='Date Applied', label_suffix=" : ",
                             required=True, disabled=False,
                             widget=DateInput(attrs={'class': 'form-control'}),
                             error_messages={'required': "This field is required."})


class MemberShipRequestAdditionalAttachment_form(forms.Form):
   caption=forms.CharField(label="Caption",max_length=150,widget=forms.TextInput(attrs={"class":"form-control"}))
   image=forms.FileField(label="Image", widget=forms.FileInput(attrs={"class":"form-control"}),required=False)

   edit_image = forms.BooleanField(label="image", initial=False)


class MemberShipRequest_approval_comment_form(forms.Form):
   comment= forms.CharField(widget=forms.Textarea(attrs={"rows":5, "cols":50}))


class MemberShipRequest_approval_attachment_form(forms.Form):
   caption=forms.CharField(label="Caption",max_length=150,widget=forms.TextInput(attrs={"class":"form-control"}),required=True)
   image=forms.FileField(label="Image", widget=forms.FileInput(attrs={"class":"form-control"}))


class MemberShipRequest_approval_submit_form(forms.Form):
   approval_status = forms.ChoiceField(initial='APPROVED', label="Approval Status", choices=APPROVAL_STATUS,widget=forms.Select(attrs={"class":"form-control"}))




class membership_price_settings_form(forms.Form):
   admin_charges = forms.DecimalField(initial=0,label='Registration Fees', label_suffix=" : ", min_value=0,  max_digits=20,
                              widget=forms.NumberInput(attrs={'class': 'form-control'}),
                              decimal_places=2, required=False,
                              disabled = False,
                              error_messages={'required': "Please Enter Admin Charges Minimum."})


class membership_form_sales_issue_form(forms.Form):
   form_print = forms.ChoiceField(label="Form Print", choices=YESNO,widget=forms.Select(attrs={"class":"form-control"}))

   unit_list=[]
   try:
      admin_charge = TransactionTypes.objects.get(code='700')
      max_unit=admin_charge.share_unit_max
      min_unit=admin_charge.share_unit_min

      # units = SharesUnits.objects.filter(Q(unit__gte=min_unit) & Q(unit__lte=max_unit))

      units = SharesUnits.objects.filter(unit__range=[min_unit,max_unit])


      for unit in units:
         small_unit=(unit.id,unit.unit)
         unit_list.append(small_unit)
   except:
      unit_list=[]

   unit = forms.ChoiceField(label="Unit List", choices=unit_list,widget=forms.Select(attrs={"class":"form-control",'readonly':'readonly'}))


   receipt = forms.IntegerField(label='Receipt', label_suffix=" : ", min_value=1, required=True,
                                 widget=forms.NumberInput(attrs={'class': 'form-control','autocomplete':'off'}),
                                help_text="This value is greater than  less than 1.",
                                disabled = False, error_messages={'required': "Please Enter Receipt No."})


   image=forms.FileField(label="Image", widget=forms.FileInput(attrs={"class":"form-control"}),required=False)

   payment_reference = forms.CharField(label="Payment Reference",max_length=150,widget=forms.TextInput(attrs={"class":"form-control"}),required=True)



   share_unit_cost = forms.DecimalField(initial=0,label='Share Unit Cost', label_suffix=" : ", min_value=0,  max_digits=20,
                              widget=forms.NumberInput(attrs={'class': 'form-control','readonly':'readonly'}),
                              decimal_places=2, required=True,
                              disabled = False)

   registration_fees = forms.DecimalField(initial=0,label='Registration Fees', label_suffix=" : ", min_value=0,  max_digits=20,
                              widget=forms.NumberInput(attrs={'class': 'form-control','readonly':'readonly'}),
                              decimal_places=2, required=True,
                              disabled = False,
                              error_messages={'required': "Please Enter."})

   amount_paid = forms.DecimalField(initial=0,label='Amount Paid', label_suffix=" : ", min_value=0,  max_digits=20,
                              widget=forms.NumberInput(attrs={'class': 'form-control','readonly':'readonly'}),
                              decimal_places=2, required=True,
                              disabled = False,
                              error_messages={'required': "Please Enter Amount Paid."})


   welfare = forms.DecimalField(initial=0,label='Welfare', label_suffix=" : ", min_value=0,  max_digits=20,
                              widget=forms.NumberInput(attrs={'class': 'form-control','readonly':'readonly'}),
                              decimal_places=2, required=True,
                              disabled = False,
                              error_messages={'required': "Please Enter Admin Charges Minimum."})


   amount_due = forms.DecimalField(initial=0,label='Amount Due', label_suffix=" : ", min_value=0,  max_digits=20,
                              widget=forms.NumberInput(attrs={'class': 'form-control'}),
                              decimal_places=2, required=True,
                              disabled = False,
                              error_messages={'required': "Please Enter Admin Charges Minimum."})


   account_name = forms.CharField(label="Payment Reference",max_length=255,required=True,widget=forms.TextInput(attrs={"class":"form-control",'readonly':'readonly'}))
   date_paid = forms.DateField(label='Date Paid', label_suffix=" : ",
                             required=True, disabled=False,
                             widget=DateInput(attrs={'class': 'form-control'}),
                             error_messages={'required': "This field is required."})

class CooperativeBankAccounts_form(forms.Form):
   account_name = forms.CharField(label="Payment Reference",max_length=255,required=True,widget=forms.TextInput(attrs={"class":"form-control"}))
   account_number =  forms.CharField(label="Account Number",max_length=10,required=True,widget=forms.TextInput(attrs={"class":"form-control"}))
   sort_code =  forms.CharField(label="Sort Code",max_length=20,required=True,widget=forms.TextInput(attrs={"class":"form-control"}))

   bank_list=[]
   try:
      banks = Banks.objects.all()
      for bank in banks:
         small_bank=(bank.id,bank.title)
         bank_list.append(small_bank)
   except:
      bank_list=[]
   bank = forms.ChoiceField(label="Bank", choices=bank_list,widget=forms.Select(attrs={"class":"form-control"}))


   account_type = forms.ChoiceField(label="account_types", choices=ACCOUNT_TYPES,widget=forms.Select(attrs={"class":"form-control"}))



class receipt_manager_form(forms.Form):
   start_point = forms.IntegerField(label='Start Point', label_suffix=" : ", min_value=1, required=True,
                                 widget=forms.NumberInput(attrs={'class': 'form-control'}),
                                help_text="This value is greater than or equal to 1 & less than or equal to 100.",
                                disabled = False, error_messages={'required': "Please Enter Admin Charges."})

   stop_point = forms.IntegerField(label='Start Point', label_suffix=" : ", min_value=1, required=True,
                                 widget=forms.NumberInput(attrs={'class': 'form-control'}),
                                help_text="This value is greater than or equal to 1 & less than or equal to 100.",
                                disabled = False, error_messages={'required': "Please Enter Admin Charges."})


class membership_registration_register_form(forms.Form):
   titles_list=[]
   try:
      titles = Titles.objects.all().order_by('title')

      for title in titles:
         small_title=(title.id,title.title)
         titles_list.append(small_title)
   except:
      titles_list=[]

   title = forms.ChoiceField(label="Title", choices=titles_list,widget=forms.Select(attrs={"class":"form-control"}))


   email = forms.EmailField(label='Email', label_suffix=" : ",
                             required=True, disabled=False,
                             widget=forms.EmailInput(attrs={'class': 'form-control'}),
                             error_messages={'required': "This field is required."})

   username=forms.CharField(label="Username",max_length=50,widget=forms.TextInput(attrs={"class":"form-control"}))
   first_name=forms.CharField(label="First Name",max_length=50,widget=forms.TextInput(attrs={"class":"form-control"}))
   last_name=forms.CharField(label="Last Name",max_length=50,widget=forms.TextInput(attrs={"class":"form-control"}))
   middle_name=forms.CharField(label="Middle Name",max_length=50,widget=forms.TextInput(attrs={"class":"form-control"}))
   gender_list=[]
   try:
      genders = Gender.objects.all().order_by('title')
      for gender in genders:
         small_gender=(gender.id,gender.title)
         gender_list.append(small_gender)
   except:
      gender_list=[]
   gender = forms.ChoiceField(label="Gender", choices=gender_list,widget=forms.Select(attrs={"class":"form-control"}))
   phone_number=forms.CharField(label="Phone Number",max_length=11,widget=forms.TextInput(attrs={"class":"form-control"}),required=True)
   profile_pic=forms.FileField(label="Profile Pic", widget=forms.FileInput(attrs={"class":"form-control"}),required=False)
   residential_address= forms.CharField(widget=forms.Textarea(attrs={"rows":2, "cols":50}))
   permanent_home_address= forms.CharField(widget=forms.Textarea(attrs={"rows":2, "cols":50}))
   department_list=[]
   try:
      departments = Departments.objects.all().order_by('title')
      for department in departments:
         small_department=(department.id,department.title)
         department_list.append(small_department)
   except:
      department_list=[]
   department = forms.ChoiceField(label="Department", choices=department_list,widget=forms.Select(attrs={"class":"form-control"}))



   salary_institution_list=[]
   try:
      salary_institutions = SalaryInstitution.objects.all().order_by('rank')
      for salary_institution in salary_institutions:
         small_salary_institution=(salary_institution.id,salary_institution.title)
         salary_institution_list.append(small_salary_institution)
   except:
      salary_institution_list=[]
   salary_institution = forms.ChoiceField(label="Salary Institution", choices=salary_institution_list,widget=forms.Select(attrs={"class":"form-control"}))
   file_no=forms.CharField(label="File No",max_length=50,widget=forms.TextInput(attrs={"class":"form-control"}),required=True)
   ippis_no=forms.CharField(label="IPPIS No/Non IPPIS No",max_length=50,widget=forms.TextInput(attrs={"class":"form-control"}),required=True)
   last_used_net_pay = forms.DecimalField(initial=0,label='Gross Pay', label_suffix=" : ", min_value=0,  max_digits=20,
                              widget=forms.NumberInput(attrs={'class': 'form-control'}),
                              decimal_places=2, required=True,
                              disabled = False,
                              error_messages={'required': "Please Enter Admin Charges Minimum."})




   date_joined = forms.DateField(label='Date Joined', label_suffix=" : ",
                             required=True, disabled=False,
                             widget=DateInput(attrs={'class': 'form-control'}),
                             error_messages={'required': "This field is required."})
   date_of_first_appointment = forms.DateField(label='Date of First Appointment', label_suffix=" : ",
                             required=True, disabled=False,
                             widget=DateInput(attrs={'class': 'form-control'}),
                             error_messages={'required': "This field is required."})
   dob = forms.DateField(label='Date of Birth', label_suffix=" : ",
                             required=True, disabled=False,
                             widget=DateInput(attrs={'class': 'form-control'}),
                             error_messages={'required': "This field is required."})

   form_print = forms.ChoiceField(label="Form Print", choices=FORM_PRINT_CHOICES,widget=forms.Select(attrs={"class":"form-control"}))




class MembersIdManager_form(forms.Form):
   prefix_title=forms.CharField(label="Prefix",max_length=50,widget=forms.TextInput(attrs={"class":"form-control"}))
   prefix_year=forms.CharField(label="Year",max_length=50,widget=forms.TextInput(attrs={"class":"form-control"}))
   member_id=forms.CharField(label="Member Id",max_length=50,widget=forms.TextInput(attrs={"class":"form-control"}))


class standing_orderform(forms.Form):
   account_number=forms.CharField(label="Account Number",max_length=50,widget=forms.TextInput(attrs={"class":"form-control","readonly":"readonly"}),required=True)
   saving_list=[]
   try:
      savings = TransactionTypes.objects.filter(source__title='SAVINGS')
      for saving in savings:
         small_saving=(saving.id,saving.name)
         saving_list.append(small_saving)
   except:
      saving_list=[]
   savings = forms.ChoiceField(label="Savings", choices=saving_list,widget=forms.Select(attrs={"class":"form-control"}))
   amount = forms.DecimalField(initial=0,label='Amount', label_suffix=" : ", min_value=0,  max_digits=20,
                              widget=forms.NumberInput(attrs={'class': 'form-control'}),
                              decimal_places=2, required=False,
                              disabled = False,
                              error_messages={'required': "Please Enter Amount"})



class loan_request_order_form(forms.Form):
   duration = forms.IntegerField(initial=0,label='Payment Duration', label_suffix=" : ", min_value=0,
                              widget=forms.NumberInput(attrs={'class': 'form-control'}),
                             help_text="This value is greater than or equal to 0 & less than or equal to 100.",
                             disabled = False, error_messages={'required': "Please Enter quantity."})


   loan_list=[]
   try:
      loans = TransactionTypes.objects.filter(source__title='LOAN').filter(~Q(code='204') & ~Q(code='205'))
      for loan in loans:
         small_loan=(loan.id,loan.name)
         loan_list.append(small_loan)
   except:
      loan_list=[]
   loans = forms.ChoiceField(label="loans", choices=loan_list,widget=forms.Select(attrs={"class":"form-control"}))
   amount = forms.DecimalField(initial=0,label='Amount', label_suffix=" : ", min_value=0,  max_digits=20,
                              widget=forms.NumberInput(attrs={'class': 'form-control'}),
                              decimal_places=2, required=False,
                              disabled = False,
                              error_messages={'required': "Please Enter Amount"})


   try:
      period_list=[]

      periods=Commodity_Period.objects.all()


      for period in periods:
         small_period=(period.id,period.title)
         period_list.append(small_period)
   except:
      period_list=[]

   period = forms.ChoiceField(label="Periods", choices=period_list,widget=forms.Select(attrs={"class":"form-control"}))


   try:
      batch_list=[]

      batches=Commodity_Period_Batch.objects.all()


      for batch in batches:
         small_batch=(batch.id,batch.title)
         batch_list.append(small_batch)
   except:
      batch_list=[]

   batch = forms.ChoiceField(label="Batches", choices=batch_list,widget=forms.Select(attrs={"class":"form-control"}))




class loan_criteria_basic_salary_form(forms.Form):
   description=forms.CharField(label="Description",max_length=150,widget=forms.TextInput(attrs={"class":"form-control",'readonly':'readonly'}))
   amount = forms.DecimalField(initial=0,label='Amount', label_suffix=" : ", min_value=0,  max_digits=20,
                              widget=forms.NumberInput(attrs={'class': 'form-control','readonly':'readonly'}),
                              decimal_places=2, required=False,
                              disabled = False,
                              error_messages={'required': "Please Enter Amount"})



class loan_criteria_external_fascilities_form(forms.Form):
   description=forms.CharField(label="Description",max_length=150,widget=forms.TextInput(attrs={"class":"form-control"}))
   amount = forms.DecimalField(initial=0,label='Amount', label_suffix=" : ", min_value=0,  max_digits=20,
                              widget=forms.NumberInput(attrs={'class': 'form-control'}),
                              decimal_places=2, required=False,
                              disabled = False,
                              error_messages={'required': "Please Enter Amount"})


class loan_cooperative_shop_form(forms.Form):
   description=forms.CharField(label="Description",max_length=150,widget=forms.TextInput(attrs={"class":"form-control"}))
   amount = forms.DecimalField(initial=0,label='Amount', label_suffix=" : ", min_value=0,  max_digits=20,
                              widget=forms.NumberInput(attrs={'class': 'form-control','readonly':'readonly'}),
                              decimal_places=2, required=False,
                              disabled = False,
                              error_messages={'required': "Please Enter Amount"})


class members_loan_request_update_form(forms.Form):
   description=forms.CharField(label="Description",max_length=150,widget=forms.TextInput(attrs={"class":"form-control"}))
   amount = forms.DecimalField(initial=0,label='Amount', label_suffix=" : ", min_value=0,  max_digits=20,
                              widget=forms.NumberInput(attrs={'class': 'form-control'}),
                              decimal_places=2, required=False,
                              disabled = False,
                              error_messages={'required': "Please Enter Amount"})


class temporallyloan_form(forms.Form):
   loan_list=[]
   try:
      loans = TransactionTypes.objects.filter(source__title='LOAN')
      for loan in loans:
         small_loan=(loan.id,loan.name)
         loan_list.append(small_loan)
   except:
      loan_list=[]
   loans = forms.ChoiceField(label="loans", choices=loan_list,widget=forms.Select(attrs={"class":"form-control"}))
   amount = forms.DecimalField(initial=0,label='Amount', label_suffix=" : ", min_value=0,  max_digits=20,
                              widget=forms.NumberInput(attrs={'class': 'form-control'}),
                              decimal_places=2, required=False,
                              disabled = False,
                              error_messages={'required': "Please Enter Amount"})



class loan_request_document_attachment_form(forms.Form):
   payment_as_at = forms.DateField(label='Payment as at', label_suffix=" : ",
                             required=True, disabled=False,
                             widget=DateInput(attrs={'class': 'form-control'}),
                             error_messages={'required': "This field is required."})

   image=forms.FileField(label="Image", widget=forms.FileInput(attrs={"class":"form-control"}),required=False)

   gross_pay = forms.DecimalField(initial=0,label='Gross Pay', label_suffix=" : ", min_value=0,  max_digits=20,
                              widget=forms.NumberInput(attrs={'class': 'form-control','readonly':'readonly'}),
                              decimal_places=2, required=False,
                              disabled = False,
                              error_messages={'required': "Please Enter Amount"})

   net_pay = forms.DecimalField(initial=0,label='Net Pay', label_suffix=" : ", min_value=0,  max_digits=50,
                              widget=forms.NumberInput(attrs={'class': 'form-control'}),
                              decimal_places=2, required=False,
                              disabled = False,
                              error_messages={'required': "Please Enter Amount"})


class MembersBankAccounts_form(forms.Form):
   account_types = forms.ChoiceField(label="account_types", choices=ACCOUNT_TYPES,widget=forms.Select(attrs={"class":"form-control"}))

   bank_list=[]
   try:
      banks = Banks.objects.all()
      for bank in banks:
         small_bank=(bank.id,bank.title)
         bank_list.append(small_bank)
   except:
      bank_list=[]
   banks = forms.ChoiceField(label="Banks", choices=bank_list,widget=forms.Select(attrs={"class":"form-control"}))
   account_name=forms.CharField(label="Account Name",max_length=255,widget=forms.TextInput(attrs={"class":"form-control"}))
   account_number=forms.CharField(label="Account Number",max_length=10,widget=forms.TextInput(attrs={"class":"form-control"}))


class MembersNextOfKins_form(forms.Form):
   relationship_list=[]
   try:
      relationships = NOKRelationships.objects.all()
      for relationship in relationships:
         small_relationship=(relationship.id,relationship.title)
         relationship_list.append(small_relationship)
   except:
      relationship_list=[]
   relationships = forms.ChoiceField(label="Relationships", choices=relationship_list,widget=forms.Select(attrs={"class":"form-control"}))


   name=forms.CharField(label="Account Name",max_length=255,widget=forms.TextInput(attrs={"class":"form-control"}))
   address=forms.CharField(label="Address",max_length=255,widget=forms.TextInput(attrs={"class":"form-control"}))
   phone_number=forms.CharField(label="Phone Number",max_length=11,widget=forms.TextInput(attrs={"class":"form-control"}))


class GuarantorsForm(forms.Form):
   guarantor_list=[]
   try:
      guarantors = Members.objects.all().order_by('member_id')
      for guarantor in guarantors:
         small_guarantor=(guarantor.id,guarantor.admin.first_name + " " + guarantor.admin.last_name + " " + guarantor.middle_name +"(" + str(guarantor.get_member_Id) +")")
         guarantor_list.append(small_guarantor)
   except:
      guarantor_list=[]
   guarantors = forms.ChoiceField(label="guarantors", choices=guarantor_list,widget=forms.Select(attrs={"class":"form-control"}))


   ##################################################################
   ##################################################################
   ###################PERSONAL LEDGER################################
   ##################################################################
class PersonalLedger_Selected_form(forms.Form):
   start_date = forms.DateField(label='Start Date', label_suffix=" : ",
                             required=True, disabled=False,
                             widget=DateInput(attrs={'class': 'form-control'}),
                             error_messages={'required': "This field is required."})
   stop_date= forms.DateField(label='Stop Date', label_suffix=" : ",
                             required=True, disabled=False,
                             widget=DateInput(attrs={'class': 'form-control'}),
                             error_messages={'required': "This field is required."})

   transaction_list=[]
   try:
      transactions = TransactionTypes.objects.filter(~Q(source__title='GENERAL') & ~Q(code='600') )
      for transaction in transactions:
         small_transaction=(transaction.id,transaction.name)
         transaction_list.append(small_transaction)
   except:
      transaction_list=[]
   transactions = forms.ChoiceField(label="Transactions", choices=transaction_list,widget=forms.Select(attrs={"class":"form-control"}))


class PersonalLedger_Transaction_Load_form(forms.Form):
   transaction_list=[]
   try:
      transactions = TransactionTypes.objects.filter(~Q(source__title='GENERAL') & ~Q(code='600') & ~Q(code='701') & ~Q(code='800')).order_by('code')
      for transaction in transactions:
         small_transaction=(transaction.id,transaction.name)
         transaction_list.append(small_transaction)
   except:
      transaction_list=[]
   transactions = forms.ChoiceField(label="Transactions", choices=transaction_list,widget=forms.Select(attrs={"class":"form-control"}))



class PersonalLedger_Transaction_Account_Load_form(forms.Form):
   start_date = forms.DateField(label='Start Date', label_suffix=" : ",
                             required=True, disabled=False,
                             widget=DateInput(attrs={'class': 'form-control'}),
                             error_messages={'required': "This field is required."})
   stop_date= forms.DateField(label='Stop Date', label_suffix=" : ",
                             required=True, disabled=False,
                             widget=DateInput(attrs={'class': 'form-control'}),
                             error_messages={'required': "This field is required."})

   status = forms.ChoiceField(initial='ACTIVE',label="Status", choices=MEMBERSHIP_STATUS,widget=forms.Select(attrs={"class":"form-control"}))











   ##################################################################
   ###################SHOP###########################################

class Stock_form(forms.Form):

   code=forms.CharField(label="Code",max_length=255,widget=forms.TextInput(attrs={"class":"form-control",'autocomplete':'off'}))
   item_name=forms.CharField(label="Item Name",max_length=255,widget=forms.TextInput(attrs={"class":"form-control"}))
   details=forms.CharField(label="Details",max_length=255,widget=forms.TextInput(attrs={"class":"form-control"}))
   quantity = forms.IntegerField(initial=0,label='Enter Quantity', label_suffix=" : ", min_value=0,  required=True,
                              widget=forms.NumberInput(attrs={'class': 'form-control'}),
                             help_text="This value is greater than or equal to 0 & less than or equal to 100.",
                             disabled = False, error_messages={'required': "Please Enter quantity."})


   re_order_level = forms.IntegerField(initial=0,label='Enter Re-Order Level', label_suffix=" : ", min_value=0,  required=True,
                              widget=forms.NumberInput(attrs={'class': 'form-control'}),
                             help_text="This value is greater than or equal to 0 & less than or equal to 100.",
                             disabled = False, error_messages={'required': "Please Enter re_order_level."})


   no_in_pack = forms.IntegerField(initial=0,label='Enter No_in_pack', label_suffix=" : ", min_value=0,  required=True,
                              widget=forms.NumberInput(attrs={'class': 'form-control'}),
                             help_text="This value is greater than or equal to 0 & less than or equal to 100.",
                             disabled = False, error_messages={'required': "Please Enter no_in_pack."})

   unit_selling_price = forms.DecimalField(initial=0,label='Unit Selling Price', label_suffix=" : ", min_value=0,  max_digits=20,
                              widget=forms.NumberInput(attrs={'class': 'form-control'}),
                              decimal_places=2, required=False,
                              disabled = False,
                              error_messages={'required': "Please Enter Unit Selling Price"})
   unit_cost_price = forms.DecimalField(initial=0,label='Unit Cost Price', label_suffix=" : ", min_value=0,  max_digits=20,
                              widget=forms.NumberInput(attrs={'class': 'form-control'}),
                              decimal_places=2, required=False,
                              disabled = False,
                              error_messages={'required': "Please Enter Unit Selling Price"})




class Item_Return_form(forms.Form):
   name=forms.CharField(label="Name",max_length=255,widget=forms.TextInput(attrs={"class":"form-control"}))
   phone_no=forms.CharField(label="Phone Number",max_length=11,widget=forms.TextInput(attrs={"class":"form-control"}))
   address=forms.CharField(label="Address",max_length=255,widget=forms.TextInput(attrs={"class":"form-control"}))
   code=forms.CharField(label="Code",max_length=255,widget=forms.TextInput(attrs={"class":"form-control",'autocomplete':'off','readonly':'readonly'}))
   item_name=forms.CharField(label="Item Name",max_length=255,widget=forms.TextInput(attrs={"class":"form-control",'readonly':'readonly'}))

   details=forms.CharField(label="Details",max_length=255,widget=forms.TextInput(attrs={"class":"form-control",'readonly':'readonly'}))
   quantity = forms.IntegerField(initial=0,label='Enter Quantity', label_suffix=" : ", min_value=0,  required=True,
                              widget=forms.NumberInput(attrs={'class': 'form-control','readonly':'readonly'}),
                             help_text="This value is greater than or equal to 0 & less than or equal to 100.",
                             disabled = False, error_messages={'required': "Please Enter quantity."})


   quantity_returned = forms.IntegerField(initial=0,label='Enter Re-Order Level', label_suffix=" : ", min_value=0,  required=True,
                              widget=forms.NumberInput(attrs={'class': 'form-control'}),
                             help_text="This value is greater than or equal to 0 & less than or equal to 100.",
                             disabled = False, error_messages={'required': "Please Enter re_order_level."})



   unit_selling_price = forms.DecimalField(initial=0,label='Unit Selling Price', label_suffix=" : ", min_value=0,  max_digits=20,
                              widget=forms.NumberInput(attrs={'class': 'form-control','readonly':'readonly'}),
                              decimal_places=2, required=False,
                              disabled = False,
                              error_messages={'required': "Please Enter Unit Selling Price"})
   total = forms.DecimalField(initial=0,label='Unit Cost Price', label_suffix=" : ", min_value=0,  max_digits=20,
                              widget=forms.NumberInput(attrs={'class': 'form-control','readonly':'readonly'}),
                              decimal_places=2, required=False,
                              disabled = False,
                              error_messages={'required': "Please Enter Unit Selling Price"})

   reasons= forms.CharField(widget=forms.Textarea(attrs={"rows":2, "cols":60}))


class Stock_Update_form(forms.Form):
   category_list=[]
   try:
      categorys = ProductCategory.objects.all()
      for category in categorys:
         small_category=(category.id,category.title)
         category_list.append(small_category)
   except:
      category_list=[]
   category = forms.ChoiceField(label="Category", choices=category_list,widget=forms.Select(attrs={"class":"form-control"}))



   code=forms.CharField(label="Code",max_length=255,widget=forms.TextInput(attrs={"class":"form-control",'autocomplete':'off'}))
   item_name=forms.CharField(label="Item Name",max_length=255,widget=forms.TextInput(attrs={"class":"form-control"}))
   details=forms.CharField(label="Details",max_length=255,widget=forms.TextInput(attrs={"class":"form-control"}))
   quantity = forms.IntegerField(initial=0,label='Enter Quantity', label_suffix=" : ", min_value=0,  required=True,
                              widget=forms.NumberInput(attrs={'class': 'form-control'}),
                             help_text="This value is greater than or equal to 0 & less than or equal to 100.",
                             disabled = False, error_messages={'required': "Please Enter quantity."})


   re_order_level = forms.IntegerField(initial=0,label='Enter Re-Order Level', label_suffix=" : ", min_value=0,  required=True,
                              widget=forms.NumberInput(attrs={'class': 'form-control'}),
                             help_text="This value is greater than or equal to 0 & less than or equal to 100.",
                             disabled = False, error_messages={'required': "Please Enter re_order_level."})


   no_in_pack = forms.IntegerField(initial=0,label='Enter No_in_pack', label_suffix=" : ", min_value=0,  required=True,
                              widget=forms.NumberInput(attrs={'class': 'form-control'}),
                             help_text="This value is greater than or equal to 0 & less than or equal to 100.",
                             disabled = False, error_messages={'required': "Please Enter no_in_pack."})

   unit_selling_price = forms.DecimalField(initial=0,label='Unit Selling Price', label_suffix=" : ", min_value=0,  max_digits=20,
                              widget=forms.NumberInput(attrs={'class': 'form-control'}),
                              decimal_places=2, required=False,
                              disabled = False,
                              error_messages={'required': "Please Enter Unit Selling Price"})
   unit_cost_price = forms.DecimalField(initial=0,label='Unit Cost Price', label_suffix=" : ", min_value=0,  max_digits=20,
                              widget=forms.NumberInput(attrs={'class': 'form-control'}),
                              decimal_places=2, required=False,
                              disabled = False,
                              error_messages={'required': "Please Enter Unit Selling Price"})



class members_credit_issue_item_form(forms.Form):
   code=forms.CharField(label="Code",max_length=255,widget=forms.TextInput(attrs={"class":"form-control",'autocomplete':'off','readonly':'readonly'}))
   item_name=forms.CharField(label="Item Name",max_length=255,widget=forms.TextInput(attrs={"class":"form-control"}),disabled = True)
   details=forms.CharField(label="Details",max_length=255,widget=forms.TextInput(attrs={"class":"form-control"}),disabled = True)
   available_quantity = forms.IntegerField(initial=0,label='Available Quantity', label_suffix=" : ", min_value=0,  required=True,
                              widget=forms.NumberInput(attrs={'class': 'form-control'}),
                             help_text="This value is greater than or equal to 0 & less than or equal to 100.",
                             disabled = True, error_messages={'required': "Please Enter quantity."})
   issue_quantity = forms.IntegerField(initial=1,label='Enter Issue Quantity', label_suffix=" : ", min_value=0, required=True,
                              widget=forms.NumberInput(attrs={'class': 'form-control'}),
                             help_text="This value is greater than or equal to 0 & less than or equal to 100.",
                             disabled = False, error_messages={'required': "Please Enter quantity."})

   unit_selling_price = forms.DecimalField(initial=0,label='Unit Selling Price', label_suffix=" : ", min_value=0,  max_digits=20,
                              widget=forms.NumberInput(attrs={'class': 'form-control'}),
                              decimal_places=2, required=False,
                              disabled = True,
                              error_messages={'required': "Please Enter Unit Selling Price"})


class Members_Credit_Sales_external_fascilities_form(forms.Form):
   description=forms.CharField(label="Description",max_length=255,widget=forms.TextInput(attrs={"class":"form-control"}),disabled = False)

   amount = forms.DecimalField(initial=0,label='Unit Selling Price', label_suffix=" : ", min_value=0,  max_digits=20,
                              widget=forms.NumberInput(attrs={'class': 'form-control'}),
                              decimal_places=2, required=False,
                              disabled = False,
                              error_messages={'required': "Please Enter Amount"})


class Members_Credit_Sales_submit_form(forms.Form):
   comment= forms.CharField(widget=forms.Textarea(attrs={"rows":2, "cols":50}))
   net_pay = forms.DecimalField(initial=0,label='Net Pay', label_suffix=" : ",
                           widget=forms.NumberInput(attrs={'class': 'form-control'}),
                           decimal_places=2, required=True,
                           disabled = False)
   payment_date = forms.DateField(label='Payment Date', label_suffix=" : ",
                             required=True, disabled=False,
                             widget=DateInput(attrs={'class': 'form-control'}),
                             error_messages={'required': "This field is required."})


class approval_form(forms.Form):
   comment= forms.CharField(widget=forms.Textarea(attrs={"rows":2, "cols":50}))
   approval_status = forms.ChoiceField(label="Approval Status", choices=APPROVAL_STATUS,widget=forms.Select(attrs={"class":"form-control"}))

   def __init__(self, *args, **kwargs):
      super(approval_form, self).__init__(*args, **kwargs)
      # assign a (computed, I assume) default value to the choice field
      self.initial['APPROVAL_STATUS'] = 'APPROVED'



class Shop_Issue_Receipt_form(forms.Form):
   receipt_types = forms.ChoiceField(label="Receipt_ Types", choices=RECEIPT_TYPES,widget=forms.Select(attrs={"class":"form-control"}))

   receipt_no = forms.IntegerField(initial=0,label='Enter Receipt No', label_suffix=" : ", min_value=0, required=True,
                              widget=forms.NumberInput(attrs={'class': 'form-control'}),
                             help_text="This value is greater than or equal to 0 & less than or equal to 100.",
                             disabled = False, error_messages={'required': "Please Enter Receipt No."})


class Customer_Registration_form(forms.Form):
   name=forms.CharField(label="Name",max_length=100,widget=forms.TextInput(attrs={"class":"form-control"}))
   address=forms.CharField(label="Address",max_length=255,widget=forms.TextInput(attrs={"class":"form-control"}))
   phone_no=forms.CharField(label="Phone Number",max_length=11,widget=forms.TextInput(attrs={"class":"form-control"}))


class general_cash_issue_item_form(forms.Form):
   bank_list=[]
   try:
      banks = Banks.objects.all()
      for bank in banks:
         small_bank=(bank.id,bank.title)
         bank_list.append(small_bank)
   except:
      bank_list=[]

   banks = forms.ChoiceField(label="Banks", choices=bank_list,widget=forms.Select(attrs={"class":"form-control"}))

   SALES_CATEGORIES=(
        ("CASH","CASH"),
        )
   channels = forms.ChoiceField(label="Payment Channels", choices=SALES_CATEGORIES,widget=forms.Select(attrs={"class":"form-control"}))


   receipt_types = forms.ChoiceField(label="Receipt_ Types", choices=RECEIPT_TYPES,widget=forms.Select(attrs={"class":"form-control"}))

   receipt=forms.CharField(label="Receipt No",max_length=100,widget=forms.TextInput(attrs={"class":"form-control",'autocomplete':'off'}),required=False)
   name=forms.CharField(label="Name",max_length=100,widget=forms.TextInput(attrs={"class":"form-control"}))
   address=forms.CharField(label="Address",max_length=255,widget=forms.TextInput(attrs={"class":"form-control"}))
   phone_no=forms.CharField(label="Phone Number",max_length=11,required=False,widget=forms.TextInput(attrs={"class":"form-control"}))


   autoprint = forms.ChoiceField(choices = YESNO)



class Shop_Cheque_Sales_Release_process_form(forms.Form):
   receipt_types = forms.ChoiceField(label="Receipt_ Types", choices=RECEIPT_TYPES,widget=forms.Select(attrs={"class":"form-control"}))

   receipt=forms.CharField(label="Receipt No",max_length=100,widget=forms.TextInput(attrs={"class":"form-control",'autocomplete':'off'}),required=False)




class loan_request_approved_list_form_sales_form(forms.Form):
   amount = forms.DecimalField(initial=0,label='Amount', label_suffix=" : ", min_value=0,  max_digits=20,
                              widget=forms.NumberInput(attrs={'class': 'form-control','readonly':'readonly'}),
                              decimal_places=2, required=True,
                              disabled = False,
                              error_messages={'required': "Please Enter Amount"})
   loan_amount = forms.DecimalField(initial=0,label='Loan Amount', label_suffix=" : ", min_value=0,  max_digits=20,
                              widget=forms.NumberInput(attrs={'class': 'form-control','readonly':'readonly'}),
                              decimal_places=2, required=True,
                              disabled = False,
                              error_messages={'required': "Please Enter Amount"})
   receipt = forms.IntegerField(label='Enter Receipt No', label_suffix=" : ", min_value=0, required=True,
                              widget=forms.NumberInput(attrs={'class': 'form-control','autocomplete':'off'}),
                             help_text="This value is greater than or equal to 0 & less than or equal to 100.",
                             disabled = False, error_messages={'required': "Please Enter Receipt No."})

   status = forms.ChoiceField(label="Status", choices=YESNO,widget=forms.Select(attrs={"class":"form-control"}))


class loan_application_processing_form(forms.Form):
   loan_type=forms.CharField(label="Loan Type",max_length=100,widget=forms.TextInput(attrs={"class":"form-control",'readonly':'readonly'}))
   loan_amount = forms.DecimalField(initial=0,label='Loan Amount', label_suffix=" : ", min_value=0,  max_digits=20,
                              widget=forms.NumberInput(attrs={'class': 'form-control','readonly':'readonly'}),
                              decimal_places=2, required=True,
                              disabled = False,
                              error_messages={'required': "Please Enter Amount"})
   duration = forms.IntegerField(initial=0,label='Duration', label_suffix=" : ", min_value=0, required=True,
                              widget=forms.NumberInput(attrs={'class': 'form-control','autocomplete':'off'}),
                             help_text="This value is greater than or equal to 0 & less than or equal to 100.",
                             disabled = False, error_messages={'required': "Please Enter Duration"})

   loan_new_amount = forms.DecimalField(initial=0,label='Loan New Amount', label_suffix=" : ", min_value=0,  max_digits=20,
                              widget=forms.NumberInput(attrs={'class': 'form-control'}),
                              decimal_places=2, required=True,
                              disabled = False,
                              error_messages={'required': "Please Enter Amount"})



class members_exclusiveness_request_register_form(forms.Form):
   purpose=forms.CharField(label="Purpose",max_length=150,widget=forms.TextInput(attrs={"class":"form-control"}), required=True)
   exceptable_list=[]
   try:
      exceptables = ExceptableCriterias.objects.all()
      for exceptable in exceptables:
         small_exceptable=(exceptable.id,exceptable.title)
         exceptable_list.append(small_exceptable)
   except:
      exceptable_list=[]
   exceptables = forms.ChoiceField(label="Exceptables", choices=exceptable_list,widget=forms.Select(attrs={"class":"form-control"}))

   transaction_list=[]
   try:
      transactions = TransactionTypes.objects.filter(Q(source__title='LOAN'))
      for transaction in transactions:
         small_transaction=(transaction.id,transaction.name)
         transaction_list.append(small_transaction)
   except:
      transaction_list=[]
   transactions = forms.ChoiceField(label="Transactions", choices=transaction_list,widget=forms.Select(attrs={"class":"form-control"}))

   try:
      period_list=[]

      periods=Commodity_Period.objects.all()


      for period in periods:
         small_period=(period.id,period.title)
         period_list.append(small_period)
   except:
      period_list=[]

   period = forms.ChoiceField(label="Periods", choices=period_list,widget=forms.Select(attrs={"class":"form-control"}))


   try:
      batch_list=[]

      batches=Commodity_Period_Batch.objects.all()


      for batch in batches:
         small_batch=(batch.id,batch.title)
         batch_list.append(small_batch)
   except:
      batch_list=[]

   batch = forms.ChoiceField(label="Batches", choices=batch_list,widget=forms.Select(attrs={"class":"form-control"}))



class members_exclusiveness_request_approval_process_form(forms.Form):
   approval_status = forms.ChoiceField(label="Approval Status", choices=APPROVAL_STATUS,widget=forms.Select(attrs={"class":"form-control"}))

   comment= forms.CharField(widget=forms.Textarea(attrs={"rows":2, "cols":62}))




class TransactionPeriod_form(forms.Form):

   transaction_period = forms.DateField(label='Approval Date', label_suffix=" : ",
                             required=True, disabled=False,
                             widget=DateInput(attrs={'class': 'form-control'}),
                             error_messages={'required': "This field is required."})


class TransactionPeriod_view_form(forms.Form):
   transaction_period_list=[]
   try:
      transaction_periods = TransactionPeriods.objects.all().order_by('status')
      for transaction_period in transaction_periods:
         small_transaction_period=(transaction_period.id,transaction_period.transaction_period)
         transaction_period_list.append(small_transaction_period)
   except:
      transaction_period_list=[]

   transaction_period = forms.ChoiceField(label="Transaction Period", choices=transaction_period_list,widget=forms.Select(attrs={"class":"form-control"}))


class deduction_ledger_posting_form(forms.Form):
   transaction_period_list=[]
   try:
      transaction_periods = TransactionPeriods.objects.all()

      for transaction_period in transaction_periods:
         small_transaction_period=(transaction_period.id,transaction_period.transaction_period)
         transaction_period_list.append(small_transaction_period)
   except:
      transaction_period_list=[]

   transaction_period = forms.ChoiceField(label="Transaction Period", choices=transaction_period_list,widget=forms.Select(attrs={"class":"form-control"}))

   salary_institution_list=[]
   try:
      salary_institutions = SalaryInstitution.objects.all().order_by('rank')
      for salary_institution in salary_institutions:
         small_salary_institution=(salary_institution.id,salary_institution.title)
         salary_institution_list.append(small_salary_institution)
   except:
      salary_institution_list=[]
   salary_institution = forms.ChoiceField(label="Salary Institution", choices=salary_institution_list,widget=forms.Select(attrs={"class":"form-control"}))


class Uploading_Existing_Savings_form(forms.Form):
   transaction_list=[]
   try:
      transactions = TransactionTypes.objects.filter(source__title='SAVINGS')
      for transaction in transactions:
         small_transaction=(transaction.id,transaction.name)
         transaction_list.append(small_transaction)
   except:
      transaction_list=[]
   transactions = forms.ChoiceField(label="Transactions", choices=transaction_list,widget=forms.Select(attrs={"class":"form-control"}))

   balance = forms.DecimalField(initial=0,label='Balance', label_suffix=" : ", min_value=0,  max_digits=20,
                              widget=forms.NumberInput(attrs={'class': 'form-control'}),
                              decimal_places=2, required=True,
                              disabled = False,
                              error_messages={'required': "Please Enter Amount"})
   schedule_amount = forms.DecimalField(initial=0,label='Schedule Amount', label_suffix=" : ", min_value=0,  max_digits=20,
                              widget=forms.NumberInput(attrs={'class': 'form-control'}),
                              decimal_places=2, required=False,
                              disabled = False,
                              error_messages={'required': "Please Enter Amount"})
   transaction_period = forms.DateField(label='Transaction Period', label_suffix=" : ",
                             required=True, disabled=False,
                             widget=DateInput(attrs={'class': 'form-control'}),
                             error_messages={'required': "This field is required."})


   tdate = forms.DateField(label='Transaction Date', label_suffix=" : ",
                             required=True, disabled=False,
                             widget=DateInput(attrs={'class': 'form-control'}),
                             error_messages={'required': "This field is required."})



class Uploading_Existing_Savings_Verification_Update_form(forms.Form):
   balance = forms.DecimalField(initial=0,label='Balance', label_suffix=" : ", min_value=0,  max_digits=20,
                     widget=forms.NumberInput(attrs={'class': 'form-control'}),
                     decimal_places=2, required=True,
                     disabled = False,
                     error_messages={'required': "Please Enter Amount"})
   schedule_amount = forms.DecimalField(initial=0,label='Schedule Amount', label_suffix=" : ", min_value=0,  max_digits=20,
                     widget=forms.NumberInput(attrs={'class': 'form-control'}),
                     decimal_places=2, required=False,
                     disabled = False,
                     error_messages={'required': "Please Enter Amount"})



class Uploading_Existing_Loans_form(forms.Form):
  transaction_list=[]
  try:
    transactions = TransactionTypes.objects.filter(source__title='LOAN',category='MONETARY')
    for transaction in transactions:
       small_transaction=(transaction.id,transaction.name)
       transaction_list.append(small_transaction)
  except:
    transaction_list=[]
  transactions = forms.ChoiceField(label="Transactions", choices=transaction_list,widget=forms.Select(attrs={"class":"form-control"}))

  loan_amount = forms.DecimalField(initial=0,label='Loan Amount', label_suffix=" : ", min_value=0,  max_digits=20,
                            widget=forms.NumberInput(attrs={'class': 'form-control'}),
                            decimal_places=2, required=True,
                            disabled = False,
                            error_messages={'required': "Please Enter Amount"})
  balance = forms.DecimalField(initial=0,label='Loan Amount', label_suffix=" : ", min_value=0,  max_digits=20,
                            widget=forms.NumberInput(attrs={'class': 'form-control'}),
                            decimal_places=2, required=True,
                            disabled = False,
                            error_messages={'required': "Please Enter Amount"})

  repayment = forms.DecimalField(initial=0,label='Balance', label_suffix=" : ", min_value=0,  max_digits=20,
                            widget=forms.NumberInput(attrs={'class': 'form-control'}),
                            decimal_places=2, required=True,
                            disabled = False,
                            error_messages={'required': "Please Enter Amount"})
  interest_rate = forms.DecimalField(initial=0,label='Interest Rate', label_suffix=" : ", min_value=0,  max_digits=20,
                            widget=forms.NumberInput(attrs={'class': 'form-control'}),
                            decimal_places=2, required=False,
                            disabled = False,
                            error_messages={'required': "Please Enter Amount"})
  admin_charge_rate = forms.DecimalField(initial=0,label='Admin Charge Rate', label_suffix=" : ", min_value=0,  max_digits=20,
                            widget=forms.NumberInput(attrs={'class': 'form-control'}),
                            decimal_places=2, required=False,
                            disabled = False,
                            error_messages={'required': "Please Enter Amount"})

  duration = forms.IntegerField(initial=0,label='Duration', label_suffix=" : ", min_value=0, required=True,
                            widget=forms.NumberInput(attrs={'class': 'form-control','autocomplete':'off'}),
                           help_text="This value is greater than or equal to 0 & less than or equal to 100.",
                           disabled = False, error_messages={'required': "Please Enter Duration"})


  interest_deductions = forms.ChoiceField(label="interest_deductions", choices=INTEREST_DEDUCTION,widget=forms.Select(attrs={"class":"form-control"}))

  start_date = forms.DateField(label='Start Date', label_suffix=" : ",
                           required=True, disabled=False,
                           widget=DateInput(attrs={'class': 'form-control'}),
                           error_messages={'required': "This field is required."})
  transaction_period = forms.DateField(label='Transaction Period', label_suffix=" : ",
                             required=True, disabled=False,
                             widget=DateInput(attrs={'class': 'form-control'}),
                             error_messages={'required': "This field is required."})



class Updating_Gross_Pay_Preview_form(forms.Form):
   description=forms.CharField(label="Description",max_length=150,widget=forms.TextInput(attrs={"class":"form-control"}), required=True)
   gross_pay = forms.DecimalField(initial=0,label='Gross Pay', label_suffix=" : ", min_value=0,  max_digits=20,
                              widget=forms.NumberInput(attrs={'class': 'form-control'}),
                              decimal_places=2, required=True,
                              disabled = False,
                              error_messages={'required': "Please Enter Amount"})


class Updating_Updating_Department_Preview_form(forms.Form):
   department_list=[]
   try:
      departments = Departments.objects.all()

      for department in departments:
         small_department=(department.id,department.title)
         department_list.append(small_department)
   except:
      department_list=[]

   department = forms.ChoiceField(label="Department", choices=department_list,widget=forms.Select(attrs={"class":"form-control"}))


class Updating_Title_Preview_form(forms.Form):
   title_list=[]
   try:
      titles = Titles.objects.all()

      for title in titles:
         small_title=(title.id,title.title)
         title_list.append(small_title)
   except:
      title_list=[]

   title = forms.ChoiceField(label="Title", choices=title_list,widget=forms.Select(attrs={"class":"form-control"}))


class Updating_Gender_Preview_form(forms.Form):
   gender_list=[]
   try:
      genders = Gender.objects.all()

      for gender in genders:
         small_gender=(gender.id,gender.title)
         gender_list.append(small_gender)
   except:
      gender_list=[]

   gender = forms.ChoiceField(label="Gender", choices=gender_list,widget=forms.Select(attrs={"class":"form-control"}))


class Norminal_Roll_Update_form(forms.Form):
   titles_list=[]
   try:
      titles = Titles.objects.all().order_by('title')

      for title in titles:
         small_title=(title.id,title.title)
         titles_list.append(small_title)
   except:
      titles_list=[]

   title = forms.ChoiceField(label="Title", choices=titles_list,widget=forms.Select(attrs={"class":"form-control"}))


   email = forms.EmailField(label='Email', label_suffix=" : ",
                             required=True, disabled=False,
                             widget=forms.EmailInput(attrs={'class': 'form-control'}),
                             error_messages={'required': "This field is required."})


   first_name=forms.CharField(label="First Name",max_length=50,widget=forms.TextInput(attrs={"class":"form-control"}))
   last_name=forms.CharField(label="Last Name",max_length=50,widget=forms.TextInput(attrs={"class":"form-control"}))
   middle_name=forms.CharField(label="Middle Name",max_length=50,widget=forms.TextInput(attrs={"class":"form-control"}))

   gender_list=[]
   try:
      genders = Gender.objects.all().order_by('title')
      for gender in genders:
         small_gender=(gender.id,gender.title)
         gender_list.append(small_gender)
   except:
      gender_list=[]
   gender = forms.ChoiceField(label="Gender", choices=gender_list,widget=forms.Select(attrs={"class":"form-control"}))

   phone_number=forms.CharField(label="Phone Number",max_length=11,widget=forms.TextInput(attrs={"class":"form-control"}))
   profile_pic=forms.FileField(label="Profile Pic", widget=forms.FileInput(attrs={"class":"form-control"}),required=False)
   residential_address= forms.CharField(label="Residential Address",max_length=255,widget=forms.TextInput(attrs={"class":"form-control"}),required=False)
   permanent_home_address= forms.CharField(label="Permanent Home Address",max_length=11,widget=forms.TextInput(attrs={"class":"form-control"}),required=False)

   department_list=[]
   try:
      departments = Departments.objects.all().order_by('title')
      for department in departments:
         small_department=(department.id,department.title)
         department_list.append(small_department)
   except:
      department_list=[]
   department = forms.ChoiceField(label="Department", choices=department_list,widget=forms.Select(attrs={"class":"form-control"}))

   state_list=[]
   try:
      states = States.objects.all().order_by('title')

      for state in states:
         small_state=(state.id,state.title)
         state_list.append(small_state)
   except:
      state_list=[]
   state = forms.ChoiceField(label="State", choices=state_list,widget=forms.Select(attrs={"class":"form-control"}))

   lga_list=[]
   try:
      lgas = Lga.objects.all().order_by('title')
      for lga in lgas:
         small_lga=(lga.id,lga.title)
         lga_list.append(small_lga)
   except:
      lga_list=[]
   lga = forms.ChoiceField(label="lga", choices=lga_list,widget=forms.Select(attrs={"class":"form-control"}))

   salary_institution_list=[]
   try:
      salary_institutions = SalaryInstitution.objects.all().order_by('title')
      for salary_institution in salary_institutions:
         small_salary_institution=(salary_institution.id,salary_institution.title)
         salary_institution_list.append(small_salary_institution)
   except:
      salary_institution_list=[]
   salary_institution = forms.ChoiceField(label="Salary Institution", choices=salary_institution_list,widget=forms.Select(attrs={"class":"form-control"}))

   file_no=forms.CharField(label="File No",max_length=50,widget=forms.TextInput(attrs={"class":"form-control"}))
   ippis_no=forms.CharField(label="IPPIS No/Non IPPIS No",max_length=50,widget=forms.TextInput(attrs={"class":"form-control"}))
   coop_no=forms.CharField(label="Coop No",max_length=50,widget=forms.TextInput(attrs={"class":"form-control"}))

   net_pay_as_at = forms.DateField(label='Net Pay as at', label_suffix=" : ",
                             required=True, disabled=False,
                             widget=DateInput(attrs={'class': 'form-control'}),
                             error_messages={'required': "This field is required."})

   last_used_net_pay = forms.DecimalField(initial=0,label='Gross Pay', label_suffix=" : ", min_value=0,  max_digits=20,
                              widget=forms.NumberInput(attrs={'class': 'form-control'}),
                              decimal_places=2, required=True,
                              disabled = False,
                              error_messages={'required': "Please Enter Admin Charges Minimum."})

   date_joined = forms.DateField(label='Date Joined', label_suffix=" : ",
                             required=True, disabled=False,
                             widget=DateInput(attrs={'class': 'form-control'}),
                             error_messages={'required': "This field is required."})

   dob = forms.DateField(label='Date of Birth', label_suffix=" : ",
                             required=True, disabled=False,
                             widget=DateInput(attrs={'class': 'form-control'}),
                             error_messages={'required': "This field is required."})

   date_of_first_appointment = forms.DateField(label='Date of First Appointment', label_suffix=" : ",
                             required=True, disabled=False,
                             widget=DateInput(attrs={'class': 'form-control'}),
                             error_messages={'required': "This field is required."})



class MembersShareConfigurations_form(forms.Form):
   unit_cost = forms.DecimalField(initial=0,label='Maximum Unit', label_suffix=" : ", min_value=0,  max_digits=20,
                              widget=forms.NumberInput(attrs={'class': 'form-control'}),
                              decimal_places=2, required=True,
                              disabled = False,
                              error_messages={'required': "Please Enter Amount"})


class Shares_Deductions_savings_form(forms.Form):
   transaction_list=[]
   try:
      transactions = TransactionTypes.objects.filter(source__title='SAVINGS')
      for transaction in transactions:
         small_transaction=(transaction.id,transaction.name)
         transaction_list.append(small_transaction)

   except:
      transaction_list=[]
   transactions = forms.ChoiceField(label="Transactions", choices=transaction_list,widget=forms.Select(attrs={"class":"form-control"}))



class MembersInitialShare_update_form(forms.Form):
   transaction_list=[]
   try:
      transactions = SharesDeductionSavings.objects.all()
      for transaction in transactions:
         small_transaction=(transaction.id,transaction.savings.name)
         transaction_list.append(small_transaction)

   except:
      transaction_list=[]
   transactions = forms.ChoiceField(label="Transactions", choices=transaction_list,widget=forms.Select(attrs={"class":"form-control"}))

   unit_cost = forms.DecimalField(initial=0,label='Maximum Unit', label_suffix=" : ", min_value=0,  max_digits=20,
                              widget=forms.NumberInput(attrs={'class': 'form-control','readonly':'readonly'}),
                              decimal_places=2, required=True,
                              disabled = False,
                              error_messages={'required': "Please Enter Amount"})


class Members_Share_Purchase_Request_form(forms.Form):
   units = forms.IntegerField(initial=0,label='Units', label_suffix=" : ", min_value=0,  required=True,
                                 widget=forms.NumberInput(attrs={'class': 'form-control'}),
                                help_text="This value is greater than or equal to 0 & less than or equal to 100.",
                                disabled = False, error_messages={'required': "Please Maximum Unit."})



class Existing_Shares_Upload_form(forms.Form):
   shares_amount = forms.DecimalField(initial=0,label='Shares Amount', label_suffix=" : ", min_value=0,  max_digits=20,
                              widget=forms.NumberInput(attrs={'class': 'form-control'}),
                              decimal_places=2, required=True,
                              disabled = False,
                              error_messages={'required': "Please Enter Amount"})
   unit_cost = forms.DecimalField(initial=0,label='Unit ', label_suffix=" : ", min_value=0,  max_digits=20,
                              widget=forms.NumberInput(attrs={'class': 'form-control','readonly':'readonly'}),
                              decimal_places=2, required=True,
                              disabled = False,
                              error_messages={'required': "Please Enter Amount"})

   shares = forms.IntegerField(initial=0,label='Duration', label_suffix=" : ", min_value=0, required=True,
                              widget=forms.NumberInput(attrs={'class': 'form-control','autocomplete':'off'}),
                             disabled = False, error_messages={'required': "Please Enter Shares"})

   effective_date = forms.DateField(label='Effective Date', label_suffix=" : ",
                             required=True, disabled=False,
                             widget=DateInput(attrs={'class': 'form-control'}),
                             error_messages={'required': "This field is required."})


class Existing_Welfare_Upload_form(forms.Form):
   amount = forms.DecimalField(initial=0,label='Amount', label_suffix=" : ", min_value=0,  max_digits=20,
                              widget=forms.NumberInput(attrs={'class': 'form-control'}),
                              decimal_places=2, required=True,
                              disabled = False,
                              error_messages={'required': "Please Enter Amount"})






class MembersWelfare_form(forms.Form):
   amount = forms.DecimalField(initial=0,label='Gross Pay', label_suffix=" : ", min_value=0,  max_digits=20,
                              widget=forms.NumberInput(attrs={'class': 'form-control'}),
                              decimal_places=2, required=True,
                              disabled = False,
                              error_messages={'required': "Please Enter Amount"})


class Cash_Deposit_Savings_form(forms.Form):
   bank_account_list=[]
   try:
      bank_accounts = CooperativeBankAccounts.objects.all()

      for bank_account in bank_accounts:
         small_bank_account=(bank_account.id,bank_account.account_name + '-' + bank_account.account_number + '-' + bank_account.bank.title )
         bank_account_list.append(small_bank_account)
   except:
      bank_account_list=[]
   bank_accounts = forms.ChoiceField(label="bank_accounts", choices=bank_account_list,widget=forms.Select(attrs={"class":"form-control"}))



   amount = forms.DecimalField(initial=0,label='Amount', label_suffix=" : ", min_value=0,  max_digits=20,
                              widget=forms.NumberInput(attrs={'class': 'form-control'}),
                              decimal_places=2, required=True,
                              disabled = False,
                              error_messages={'required': "Please Enter Amount"})
   payment_date = forms.DateField(label='Date Paid', label_suffix=" : ",
                             required=True, disabled=False,
                             widget=DateInput(attrs={'class': 'form-control'}),
                             error_messages={'required': "This field is required."})

   payment_reference=forms.CharField(label="Payment Reference",max_length=50,required=True,widget=forms.TextInput(attrs={"class":"form-control"}))

   payment_evidience=forms.FileField(label="Payment Evidience", widget=forms.FileInput(attrs={"class":"form-control"}),required=False)
   purpose= forms.CharField(widget=forms.Textarea(attrs={"rows":2, "cols":50}))
   receipt_no = forms.IntegerField(label='Receipt No', label_suffix=" : ", min_value=0,
                  widget=forms.NumberInput(attrs={'class': 'form-control','autocomplete':'off'}),
                  disabled = False)


class Cash_Deposit_Loans_form(forms.Form):
   bank_account_list=[]
   try:
      bank_accounts = CooperativeBankAccounts.objects.all()

      for bank_account in bank_accounts:
         small_bank_account=(bank_account.id,bank_account.account_name + '-' + bank_account.account_number + '-' + bank_account.bank.title )
         bank_account_list.append(small_bank_account)
   except:
      bank_account_list=[]
   bank_accounts = forms.ChoiceField(label="bank_accounts", choices=bank_account_list,widget=forms.Select(attrs={"class":"form-control"}))


   transaction_list=[]
   try:
      transactions = TransactionTypes.objects.filter(source__title='LOAN').filter(~Q(name='SHOP'))
      for transaction in transactions:
         small_transaction=(transaction.id,transaction.name)
         transaction_list.append(small_transaction)
   except:
      transaction_list=[]
   transactions = forms.ChoiceField(label="Transactions", choices=transaction_list,widget=forms.Select(attrs={"class":"form-control"}))

   amount = forms.DecimalField(initial=0,label='Amount', label_suffix=" : ", min_value=0,  max_digits=20,
                              widget=forms.NumberInput(attrs={'class': 'form-control'}),
                              decimal_places=2, required=True,
                              disabled = False,
                              error_messages={'required': "Please Enter Amount"})
   payment_date = forms.DateField(label='Date Paid', label_suffix=" : ",
                             required=True, disabled=False,
                             widget=DateInput(attrs={'class': 'form-control'}),
                             error_messages={'required': "This field is required."})

   payment_reference=forms.CharField(label="Payment Reference",max_length=50,required=True,widget=forms.TextInput(attrs={"class":"form-control"}))

   payment_evidience=forms.FileField(label="Payment Evidience", widget=forms.FileInput(attrs={"class":"form-control"}),required=False)
   purpose= forms.CharField(widget=forms.Textarea(attrs={"rows":2, "cols":50}))



# class Cash_Withdrawal_form(forms.Form):

#    try:
#       status=WithdrawalStatus.objects.get(title='UNLOCKED')
#       transaction_list=[]
#       transactions = WithdrawableTransactions.objects.filter(status=status)
#       for transaction in transactions:
#          small_transaction=(transaction.transaction_id,transaction.transaction.name)
#          transaction_list.append(small_transaction)
#    except:
#       transaction_list=[]

#    transactions = forms.ChoiceField(label="Transactions", choices=transaction_list,widget=forms.Select(attrs={"class":"form-control"}))

#    amount = forms.DecimalField(initial=0,label='Amount', label_suffix=" : ", min_value=0,  max_digits=20,
#                               widget=forms.NumberInput(attrs={'class': 'form-control'}),
#                               decimal_places=2, required=True,
#                               disabled = False,
#                               error_messages={'required': "Please Enter Amount"})
#    narration= forms.CharField(widget=forms.Textarea(attrs={"rows":2, "cols":50}))
#    account_number=forms.CharField(label="Account Number",max_length=50,widget=forms.TextInput(attrs={"class":"form-control",'readonly':'readonly'}))

#    ledger_balance = forms.DecimalField(initial=0,label='Ledger Balance', label_suffix=" : ", min_value=0,  max_digits=20,
#                               widget=forms.NumberInput(attrs={'class': 'form-control','readonly':'readonly'}),
#                               decimal_places=2, required=True,
#                               disabled = False,
#                               error_messages={'required': "Please Enter Amount"})



class WithdrawalController_form(forms.Form):
   transaction_list=[]
   try:
      transactions = TransactionTypes.objects.filter(source__title='SAVINGS').filter(~Q(code='104'))
      for transaction in transactions:
         small_transaction=(transaction.id,transaction.name)
         transaction_list.append(small_transaction)
   except:
      transaction_list=[]
   transactions = forms.ChoiceField(label="Transactions", choices=transaction_list,widget=forms.Select(attrs={"class":"form-control"}))

   maturity = forms.IntegerField(initial=0,label='Maturity', label_suffix=" : ", min_value=0, required=True,
                              widget=forms.NumberInput(attrs={'class': 'form-control','autocomplete':'off'}),
                             disabled = False, error_messages={'required': "Please Enter Maturity Months"})



class WithdrawalController_update_form(forms.Form):
   status = forms.ChoiceField(label="Title", choices=WITHDRAWAL_STATUS,widget=forms.Select(attrs={"class":"form-control"}))

   maturity = forms.IntegerField(initial=0,label='Maturity', label_suffix=" : ", min_value=0, required=True,
                     widget=forms.NumberInput(attrs={'class': 'form-control','autocomplete':'off'}),
                             disabled = False, error_messages={'required': "Please Enter Maturity Months"})


class savings_cash_withdrawal_preview_form(forms.Form):
   comment= forms.CharField(widget=forms.Textarea(attrs={"rows":2, "cols":50}))

   status = forms.ChoiceField(label="Title", choices=APPROVAL_STATUS,widget=forms.Select(attrs={"class":"form-control"}))
   ledger_balance = forms.DecimalField(initial=0,label='Ledger Balance', label_suffix=" : ", min_value=0,  max_digits=20,
                              widget=forms.NumberInput(attrs={'class': 'form-control','readonly':'readonly','readonly':'readonly'}),
                              decimal_places=2, required=True,
                              disabled = False)
   amount_applied = forms.DecimalField(initial=0,label='Amount Applied', label_suffix=" : ", min_value=0,  max_digits=20,
                              widget=forms.NumberInput(attrs={'class': 'form-control','readonly':'readonly','readonly':'readonly'}),
                              decimal_places=2, required=True,
                              disabled = False)
   amount_approved = forms.DecimalField(initial=0,label='Amount Approved', label_suffix=" : ", min_value=0,  max_digits=20,
                              widget=forms.NumberInput(attrs={'class': 'form-control'}),
                              decimal_places=2, required=True,
                              disabled = False,
                              error_messages={'required': "Please Enter Amount Approved"})



class Cash_Withdrawal_Approved_Details_form(forms.Form):
   bank_list=[]
   try:
      banks = Banks.objects.all()
      for bank in banks:
         small_bank=(bank.id,bank.title)
         bank_list.append(small_bank)
   except:
      bank_list=[]

   banks = forms.ChoiceField(label="Banks", choices=bank_list,widget=forms.Select(attrs={"class":"form-control"}))


   channels = forms.ChoiceField(label="Payment Channels", choices=PAYMENT_CHANNEL,widget=forms.Select(attrs={"class":"form-control"}))

   account_list=[]
   try:
      accounts = CooperativeBankAccounts.objects.all()
      for account in accounts:
         small_account=(account.id,account.account_name + ' - ' + str(account.account_number) + ' - ' + str(account.bank))
         account_list.append(small_account)
   except:
      account_list=[]
   account = forms.ChoiceField(label="Account", choices=account_list,widget=forms.Select(attrs={"class":"form-control"}))


   cheque_number=forms.CharField(label="Cheque Number",max_length=50,widget=forms.TextInput(attrs={"class":"form-control"}),required=False)
   payment_date = forms.DateField(label='Payment Date', label_suffix=" : ",required=False, disabled=False,
                             widget=DateInput(attrs={'class': 'form-control'}),
                             error_messages={'required': "This field is required."})
   amount = forms.DecimalField(initial=0,label='Amount', label_suffix=" : ", min_value=0,  max_digits=20,
                              widget=forms.NumberInput(attrs={'class': 'form-control','readonly':'readonly'}),
                              decimal_places=2, required=True,
                              disabled = False,
                              error_messages={'required': "Please Enter Amount Approved"})




class Updating_Date_Joined__form(forms.Form):
   date_joined = forms.DateField(label='Date Joined', label_suffix=" : ",
                             required=True, disabled=False,
                             widget=DateInput(attrs={'class': 'form-control'}),
                             error_messages={'required': "This field is required."})


class loan_application_approved_process_preview_form(forms.Form):

   effective_date = forms.DateField(label='Effective Date', label_suffix=" : ",
                             required=True, disabled=False,
                             widget=DateInput(attrs={'class': 'form-control'}),
                             error_messages={'required': "This field is required."})

   status = forms.ChoiceField(label="Status", choices=YESNO,widget=forms.Select(attrs={"class":"form-control"}))



class DataCapture_Manager_form(forms.Form):
   status = forms.ChoiceField(label="Title", choices=MEMBERSHIP_STATUS,widget=forms.Select(attrs={"class":"form-control"}))

class CustomerID_Manager_form(forms.Form):
   code = forms.IntegerField(initial=0,label='Customer ID', label_suffix=" : ", min_value=0, required=True,
                     widget=forms.NumberInput(attrs={'class': 'form-control','autocomplete':'off'}),
                             disabled = False, error_messages={'required': "Please Enter Customer ID"})


class Loan_Number_Manager_form(forms.Form):
   code = forms.IntegerField(initial=0,label='Loan Number', label_suffix=" : ", min_value=0, required=True,
                     widget=forms.NumberInput(attrs={'class': 'form-control','autocomplete':'off'}),
                             disabled = False, error_messages={'required': "Please Enter Loan Number"})



class FailedLoanPenalty_Manager_form(forms.Form):
   code =  forms.DecimalField(initial=0,label='Rate', label_suffix=" : ", min_value=0,  max_digits=20,
                              widget=forms.NumberInput(attrs={'class': 'form-control'}),
                              decimal_places=2, required=True,
                              disabled = False,
                              error_messages={'required': "Please Enter Amount Approved"})


class FailedLoanPenalty_Duration_Manager_form(forms.Form):
   duration = forms.IntegerField(initial=0,label='Number', label_suffix=" : ", min_value=0, required=True,
                     widget=forms.NumberInput(attrs={'class': 'form-control','autocomplete':'off'}),
                             disabled = False, error_messages={'required': "Please Enter Loan Number"})


class Transaction_adjustment_Transactions_form(forms.Form):
   transaction_list=[]
   try:
      transactions = TransactionTypes.objects.filter(source__title='SAVINGS')
      for transaction in transactions:
         small_transaction=(transaction.id,transaction.name)
         transaction_list.append(small_transaction)
   except:
      transaction_list=[]
   transactions = forms.ChoiceField(label="Transactions", choices=transaction_list,widget=forms.Select(attrs={"class":"form-control"}))



class Transaction_adjustment_selection_form(forms.Form):
   effective_date = forms.DateField(label='Effective Date', label_suffix=" : ",
                             required=True, disabled=False,
                             widget=DateInput(attrs={'class': 'form-control'}),
                             error_messages={'required': "This field is required."})

   amount = forms.DecimalField(initial=0,label='Amount', label_suffix=" : ", min_value=0,  max_digits=20,
                              widget=forms.NumberInput(attrs={'class': 'form-control'}),
                              decimal_places=2, required=True,
                              disabled = False,
                              error_messages={'required': "Please Enter Amount Approved"})



class Transaction_Loan_adjustment_selection_form(forms.Form):
   purpose= forms.CharField(widget=forms.Textarea(attrs={"rows":2, "cols":50}))

   effective_date = forms.DateField(label='Effective Date', label_suffix=" : ",
                             required=True, disabled=False,
                             widget=DateInput(attrs={'class': 'form-control'}),
                             error_messages={'required': "This field is required."})

   amount = forms.DecimalField(initial=0,label='Amount', label_suffix=" : ", min_value=0,  max_digits=20,
                              widget=forms.NumberInput(attrs={'class': 'form-control'}),
                              decimal_places=2, required=True,
                              disabled = False,
                              error_messages={'required': "Please Enter Amount Approved"})




class Monthly_Account_deduction_Processing_Institution_Load_form(forms.Form):
   transaction_period_list=[]
   try:
      transaction_periods = TransactionPeriods.objects.all().order_by('status')
      for transaction_period in transaction_periods:
         small_transaction_period=(transaction_period.id,transaction_period.transaction_period)

         transaction_period_list.append(small_transaction_period)
   except:
      transaction_period_list=[]

   transaction_period = forms.ChoiceField(label="Transaction Period", choices=transaction_period_list,widget=forms.Select(attrs={"class":"form-control"}))

   salary_institution_list=[]
   try:
      salary_institutions = SalaryInstitution.objects.all().order_by('-title')
      for salary_institution in salary_institutions:
         small_salary_institution=(salary_institution.id,salary_institution.title)
         salary_institution_list.append(small_salary_institution)
   except:
      salary_institution_list=[]
   salary_institution = forms.ChoiceField(label="Salary Institution", choices=salary_institution_list,widget=forms.Select(attrs={"class":"form-control"}))




class Cash_Deposit_Report_Date_Load_form(forms.Form):
   start_date = forms.DateField(label='Start Date', label_suffix=" : ",
                             required=True, disabled=False,
                             widget=DateInput(attrs={'class': 'form-control'}),
                             error_messages={'required': "This field is required."})
   stop_date = forms.DateField(label='Stop Date', label_suffix=" : ",
                             required=True, disabled=False,
                             widget=DateInput(attrs={'class': 'form-control'}),
                             error_messages={'required': "This field is required."})


class Initial_Shares_Update_preview_form(forms.Form):
   approval_status = forms.ChoiceField(label="Approval Status", choices=APPROVAL_STATUS,widget=forms.Select(attrs={"class":"form-control"}))

   comment= forms.CharField(widget=forms.Textarea(attrs={"rows":2, "cols":55}))

   amount = forms.DecimalField(initial=0,label='Amount', label_suffix=" : ", min_value=0,  max_digits=20,
                              widget=forms.NumberInput(attrs={'class': 'form-control','readonly':'readonly'}),
                              decimal_places=2, required=True,
                              disabled = False,
                              error_messages={'required': "Please Enter Amount Approved"})



class Shares_Purchase_Request_Approval_Processed_form(forms.Form):
   approval_status = forms.ChoiceField(label="Approval Status", choices=APPROVAL_STATUS,widget=forms.Select(attrs={"class":"form-control"}))

   comment= forms.CharField(widget=forms.Textarea(attrs={"rows":2, "cols":55}))

   units = forms.IntegerField(initial=0,label='Loan Number', label_suffix=" : ", min_value=0, required=True,
                  widget=forms.NumberInput(attrs={'class': 'form-control','autocomplete':'off'}),
                  disabled = False, error_messages={'required': "Please Enter Loan Number"})


class Members_Share_Purchase_Request_Process_View_Form(forms.Form):
   payment_date = forms.DateField(label='Payment Date', label_suffix=" : ",
                             required=True, disabled=False,
                             widget=DateInput(attrs={'class': 'form-control'}),
                             error_messages={'required': "This field is required."})


   unit_cost = forms.DecimalField(initial=0,label='Unit Cost', label_suffix=" : ", min_value=0,  max_digits=20,
                              widget=forms.NumberInput(attrs={'class': 'form-control','readonly':'readonly'}),
                              decimal_places=2, required=True,
                              disabled = False)

   units = forms.IntegerField(initial=0,label='Loan Number', label_suffix=" : ", min_value=0, required=True,
                  widget=forms.NumberInput(attrs={'class': 'form-control','autocomplete':'off','readonly':'readonly'}),
                  disabled = False, error_messages={'required': "Please Enter Loan Number"})

   total_cost = forms.DecimalField(initial=0,label='Total Cost', label_suffix=" : ", min_value=0,  max_digits=20,
                              widget=forms.NumberInput(attrs={'class': 'form-control','readonly':'readonly'}),
                              decimal_places=2, required=True,
                              disabled = False)
   receipt_no = forms.IntegerField(label='Receipt No', label_suffix=" : ", min_value=0,
                  widget=forms.NumberInput(attrs={'class': 'form-control','autocomplete':'off'}),
                  disabled = False)

   payment_reference=forms.CharField(label="Payment Referencer",max_length=250,widget=forms.TextInput(attrs={"class":"form-control"}))

   image=forms.FileField(label="Image", widget=forms.FileInput(attrs={"class":"form-control"}),required=False)


   account_list=[]
   try:
      accounts = CooperativeBankAccounts.objects.all()
      for account in accounts:
         small_account=(account.id,account.account_name + ' - ' + str(account.account_number) + ' - ' + str(account.bank))
         account_list.append(small_account)
   except:
      account_list=[]
   account = forms.ChoiceField(label="Account", choices=account_list,widget=forms.Select(attrs={"class":"form-control"}))


class Cash_Deposit_Welfare_Preview_Form(forms.Form):
   enforce_payment=forms.BooleanField( )
   payment_date = forms.DateField(label='Payment Date', label_suffix=" : ",
                             required=True, disabled=False,
                             widget=DateInput(attrs={'class': 'form-control'}),
                             error_messages={'required': "This field is required."})


   amount = forms.DecimalField(initial=0,label='Amount', label_suffix=" : ",
                              widget=forms.NumberInput(attrs={'class': 'form-control'}),
                              decimal_places=2, required=True,
                              disabled = False)

   receipt_no = forms.IntegerField(label='Receipt No', label_suffix=" : ", min_value=0,
                  widget=forms.NumberInput(attrs={'class': 'form-control','autocomplete':'off'}),
                  disabled = False)
   year = forms.IntegerField(label='Year', label_suffix=" : ",
                  widget=forms.NumberInput(attrs={'class': 'form-control','autocomplete':'off'}),
                  disabled = False)

   payment_reference=forms.CharField(label="Payment Referencer",max_length=250,widget=forms.TextInput(attrs={"class":"form-control"}))

   image=forms.FileField(label="Image", widget=forms.FileInput(attrs={"class":"form-control"}),required=False)


   account_list=[]
   try:
      accounts = CooperativeBankAccounts.objects.all()
      for account in accounts:
         small_account=(account.id,account.account_name + ' - ' + str(account.account_number) + ' - ' + str(account.bank))
         account_list.append(small_account)
   except:
      account_list=[]
   account = forms.ChoiceField(label="Account", choices=account_list,widget=forms.Select(attrs={"class":"form-control"}))
   narration= forms.CharField(widget=forms.Textarea(attrs={"rows":2, "cols":55}))


class Cash_Deposit_Shares_Preview_Form(forms.Form):
   payment_date = forms.DateField(label='Payment Date', label_suffix=" : ",
                             required=True, disabled=False,
                             widget=DateInput(attrs={'class': 'form-control'}),
                             error_messages={'required': "This field is required."})


   unit_cost = forms.DecimalField(initial=0,label='Unit Cost', label_suffix=" : ",
                              widget=forms.NumberInput(attrs={'class': 'form-control','readonly':'readonly'}),
                              decimal_places=2, required=True,
                              disabled = False)
   total_amount = forms.DecimalField(initial=0,label='Unit Cost', label_suffix=" : ",
                              widget=forms.NumberInput(attrs={'class': 'form-control'}),
                              decimal_places=2, required=True,
                              disabled = False)
   units = forms.IntegerField(label='Units', label_suffix=" : ",
                  widget=forms.NumberInput(attrs={'class': 'form-control','autocomplete':'off'}),
                  disabled = False)

   receipt_no = forms.IntegerField(label='Receipt No', label_suffix=" : ", min_value=0,
                  widget=forms.NumberInput(attrs={'class': 'form-control','autocomplete':'off'}),
                  disabled = False)

   payment_reference=forms.CharField(label="Payment Referencer",max_length=250,widget=forms.TextInput(attrs={"class":"form-control"}))

   image=forms.FileField(label="Image", widget=forms.FileInput(attrs={"class":"form-control"}),required=False)


   account_list=[]
   try:
      accounts = CooperativeBankAccounts.objects.all()
      for account in accounts:
         small_account=(account.id,account.account_name + ' - ' + str(account.account_number) + ' - ' + str(account.bank))
         account_list.append(small_account)
   except:
      account_list=[]
   account = forms.ChoiceField(label="Account", choices=account_list,widget=forms.Select(attrs={"class":"form-control"}))
   narration= forms.CharField(widget=forms.Textarea(attrs={"rows":2, "cols":55}))


class CompulsorySavings_form(forms.Form):
   transaction_list=[]
   try:
      transactions = TransactionTypes.objects.filter(source__title='SAVINGS')
      for transaction in transactions:
         small_transaction=(transaction.id,transaction.name)
         transaction_list.append(small_transaction)
   except:
      transaction_list=[]
   transactions = forms.ChoiceField(label="Transactions", choices=transaction_list,widget=forms.Select(attrs={"class":"form-control"}))


class Members_Credit_sales_ledger_form(forms.Form):
   start_date = forms.DateField(label='Start Date', label_suffix=" : ",
                             required=True, disabled=False,
                             widget=DateInput(attrs={'class': 'form-control'}),
                             error_messages={'required': "This field is required."})
   stop_date = forms.DateField(label='Start Date', label_suffix=" : ",
                             required=True, disabled=False,
                             widget=DateInput(attrs={'class': 'form-control'}),
                             error_messages={'required': "This field is required."})

class Daily_Sales_Summarization_form(forms.Form):
   current_date = forms.DateField(label='Date', label_suffix=" : ",
                             required=True, disabled=False,
                             widget=DateInput(attrs={'class': 'form-control'}),
                             error_messages={'required': "This field is required."})

class Suppliers_add_form(forms.Form):
    prefix=forms.CharField(label="Prefix",max_length=15,widget=forms.TextInput(attrs={"class":"form-control",'required':'required'}),
                        error_messages={'required': "This field is required."})
    name=forms.CharField(label="Name",max_length=250,widget=forms.TextInput(attrs={"class":"form-control",'required':'required'}),
                        error_messages={'required': "This field is required."})


class Suppliers_Branches_form(forms.Form):
   address= forms.CharField(widget=forms.Textarea(attrs={"rows":2, "cols":50}))
   phone=forms.CharField(label="Phone",max_length=250,widget=forms.TextInput(attrs={"class":"form-control",'required':'required'}))

class Suppliers_Personnel_form(forms.Form):
   name=forms.CharField(label="Name",max_length=250,widget=forms.TextInput(attrs={"class":"form-control",'required':'required'}))
   phone=forms.CharField(label="Phone",max_length=250,widget=forms.TextInput(attrs={"class":"form-control",'required':'required'}))


class Product_Purchase_form(forms.Form):
   invoice=forms.CharField(label="Phone",max_length=250,widget=forms.TextInput(attrs={"class":"form-control",'required':'required'}))
   invoice_date = forms.DateField(label='Date', label_suffix=" : ",
                             required=True, disabled=False,
                             widget=DateInput(attrs={'class': 'form-control'}),
                             error_messages={'required': "This field is required."})

class Product_Purchase_Select_form(forms.Form):
   code=forms.CharField(label="Code",max_length=250,widget=forms.TextInput(attrs={"class":"form-control",'required':'required','readonly':"readonly"}))
   item_name=forms.CharField(label="Item Name",max_length=250,widget=forms.TextInput(attrs={"class":"form-control",'required':'required','readonly':"readonly"}))


   quantity = forms.IntegerField(label='Quantity', label_suffix=" : ",
                  widget=forms.NumberInput(attrs={'class': 'form-control','autocomplete':'off'}),
                  disabled = False)
   unit_cost = forms.DecimalField(initial=0,label='Unit Cost', label_suffix=" : ",
                              widget=forms.NumberInput(attrs={'class': 'form-control'}),
                              decimal_places=2, required=True,
                              disabled = False)
   unit_selling_price = forms.DecimalField(initial=0,label='Unit Selling Price', label_suffix=" : ",
                              widget=forms.NumberInput(attrs={'class': 'form-control'}),
                              decimal_places=2, required=True,
                              disabled = False)


class Purchase_Tracking_Invoice_Date_Update_form(forms.Form):
   purchase_date = forms.DateField(label='Start Date', label_suffix=" : ",
                             required=True, disabled=False,
                             widget=DateInput(attrs={'class': 'form-control'}),
                             error_messages={'required': "This field is required."})
   invoice=forms.CharField(label="Invoice No",max_length=250,widget=forms.TextInput(attrs={"class":"form-control",'required':'required'}))

class Purchase_Summary_form(forms.Form):
   start_date = forms.DateField(label='Start Date', label_suffix=" : ",
                             required=True, disabled=False,
                             widget=DateInput(attrs={'class': 'form-control'}),
                             error_messages={'required': "This field is required."})
   stop_date = forms.DateField(label='Stop Date', label_suffix=" : ",
                             required=True, disabled=False,
                             widget=DateInput(attrs={'class': 'form-control'}),
                             error_messages={'required': "This field is required."})

class Invoice_Title_form(forms.Form):
   title=forms.CharField(label="Heading",max_length=250,widget=forms.TextInput(attrs={"class":"form-control",'required':'required'}))
   address1=forms.CharField(label="Address 1",max_length=250,widget=forms.TextInput(attrs={"class":"form-control",'required':'required'}))
   address2=forms.CharField(label="Address 2",max_length=250,widget=forms.TextInput(attrs={"class":"form-control"}))
   phone_no=forms.CharField(label="Phone No.",max_length=250,widget=forms.TextInput(attrs={"class":"form-control",'required':'required'}))



class Item_Write_off_product_form(forms.Form):
   reason_list=[]
   try:
      reasons = ItemWriteOffReasons.objects.all()
      for reason in reasons:
         small_reason=(reason.id,reason.title)
         reason_list.append(small_reason)
   except:
      reason_list=[]
   reasons = forms.ChoiceField(label="reasons", choices=reason_list,widget=forms.Select(attrs={"class":"form-control"}))

   code=forms.CharField(label="Code",max_length=255,widget=forms.TextInput(attrs={"class":"form-control",'readonly':'readonly'}))
   item_name=forms.CharField(label="Item Name",max_length=255,widget=forms.TextInput(attrs={"class":"form-control",'readonly':'readonly'}))
   available_quantity = forms.IntegerField(label='Available Quantity', label_suffix=" : ",
                  widget=forms.NumberInput(attrs={'class': 'form-control','autocomplete':'off','readonly':'readonly'}),
                  disabled = False)
   quantity = forms.IntegerField(label='Request Quantity', label_suffix=" : ",
                  widget=forms.NumberInput(attrs={'class': 'form-control','autocomplete':'off'}),
                  disabled = False)

   details= forms.CharField(widget=forms.Textarea(attrs={"rows":2, "cols":55}))
   unit_cost_price = forms.DecimalField(initial=0,label='Unit Cost Price', label_suffix=" : ", min_value=1,  max_digits=20,
                              widget=forms.NumberInput(attrs={'class': 'form-control'}),
                              decimal_places=2, required=True,
                              disabled = False,
                              error_messages={'required': "Please Add Cost Price"})

   unit_selling_price = forms.DecimalField(initial=0,label='Unit Selling Price', label_suffix=" : ", min_value=1,  max_digits=20,
                              widget=forms.NumberInput(attrs={'class': 'form-control','readonly':'readonly'}),
                              decimal_places=2, required=True,
                              disabled = False,
                              error_messages={'required': "Please Enter Amount Paid"})

class Item_Write_off_Approval_form(forms.Form):
   code=forms.CharField(label="Code",max_length=255,widget=forms.TextInput(attrs={"class":"form-control",'readonly':'readonly'}))
   item_name=forms.CharField(label="Item Name",max_length=255,widget=forms.TextInput(attrs={"class":"form-control",'readonly':'readonly'}))
   quantity = forms.IntegerField(label='Request Quantity', label_suffix=" : ",
                  widget=forms.NumberInput(attrs={'class': 'form-control','autocomplete':'off','readonly':'readonly'}),
                  disabled = False)
   reasons=forms.CharField(label="Reasons",max_length=255,widget=forms.TextInput(attrs={"class":"form-control",'readonly':'readonly'}))
   details= forms.CharField(widget=forms.Textarea(attrs={"rows":2, "cols":55,'readonly':'readonly'}))

class FormAutoPrint_Settings_Form(forms.Form):
   status = forms.ChoiceField(label="Status", choices=YESNO,widget=forms.Select(attrs={"class":"form-control"}))

   title=forms.CharField(label="Title",max_length=255,widget=forms.TextInput(attrs={"class":"form-control"}))


class Daily_Sales_Summary_Form(forms.Form):
   sales_date = forms.DateField(label='Date', label_suffix=" : ",
                             required=True, disabled=False,
                             widget=DateInput(attrs={'class': 'form-control'}),
                             error_messages={'required': "This field is required."})

class Members_Credit_sales_Cash_Deposit_Details_form(forms.Form):
   payment_date = forms.DateField(label='Date', label_suffix=" : ",
                             required=True, disabled=False,
                             widget=DateInput(attrs={'class': 'form-control'}),
                             error_messages={'required': "This field is required."})

   bank_list=[]
   try:
      banks = Banks.objects.all()
      for bank in banks:
         small_bank=(bank.id,bank.title)
         bank_list.append(small_bank)
   except:
      bank_list=[]
   bank = forms.ChoiceField(label="Bank", choices=bank_list,widget=forms.Select(attrs={"class":"form-control"}))

   payment_reference=forms.CharField(label="Payment Reference",max_length=255,widget=forms.TextInput(attrs={"class":"form-control",}))

   account_list=[]
   try:
      accounts = CooperativeBankAccounts.objects.all()
      for account in accounts:
         small_account=(account.id,account.account_name + ' - ' + str(account.account_number) + ' - ' + str(account.bank))
         account_list.append(small_account)
   except:
      account_list=[]
   account = forms.ChoiceField(label="Account", choices=account_list,widget=forms.Select(attrs={"class":"form-control"}))

   amount_paid = forms.DecimalField(initial=0,label='Amount Paid', label_suffix=" : ",
                                 widget=forms.NumberInput(attrs={'class': 'form-control'}),
                                 decimal_places=2, required=True,
                                 disabled = False)
   receipt=forms.CharField(label="receipt",max_length=30,widget=forms.TextInput(attrs={"class":"form-control",}),required=False)

class Cash_Deposit_Summary_form(forms.Form):
   current_date = forms.DateField(label='Date', label_suffix=" : ",
                             required=True, disabled=False,
                             widget=DateInput(attrs={'class': 'form-control'}),
                             error_messages={'required': "This field is required."})


class Termination_Sources_upload_form(forms.Form):
   date_applied = forms.DateField(label='Date Applied', label_suffix=" : ",
                             required=True, disabled=False,
                             widget=DateInput(attrs={'class': 'form-control'}),
                             error_messages={'required': "This field is required."})

   termination_list=[]
   try:
      terminations = Termination_Types.objects.all().order_by('id')
      for termination in terminations:
         small_termination=(termination.id,termination.title)
         termination_list.append(small_termination)
   except:
      termination_list=[]

   termination_types = forms.ChoiceField(label="Termination Types", choices=termination_list,widget=forms.Select(attrs={"class":"form-control"}))

   comments= forms.CharField(widget=forms.Textarea(attrs={"rows":2, "cols":55}))


   loan_amount = forms.DecimalField(initial=0,label='Loan Amount', label_suffix=" : ",
                                 widget=forms.NumberInput(attrs={'class': 'form-control','readonly':'readonly'}),
                                 decimal_places=2, required=True,
                                 disabled = False)


class Manage_Commodity_Categories_Title_Update_form(forms.Form):
   title=forms.CharField(label="Title",max_length=30,widget=forms.TextInput(attrs={"class":"form-control",}),required=True)


class addCommodityCategoryForm(forms.Form):
   title=forms.CharField(label="Title",max_length=30,widget=forms.TextInput(attrs={"class":"form-control",}),required=True)
   interest_deductions = forms.ChoiceField(label="Interest Deductions", choices=INTEREST_DEDUCTION,widget=forms.Select(attrs={"class":"form-control"}))
   duration = forms.IntegerField(label='Duration', label_suffix=" : ",
                  widget=forms.NumberInput(attrs={'class': 'form-control','autocomplete':'off'}),
                  disabled = False)
   interest_rate=forms.DecimalField(initial=0,label='Interest Rate', label_suffix=" : ",
                                 widget=forms.NumberInput(attrs={'class': 'form-control'}),
                                 decimal_places=2, required=True,
                                 disabled = False)


   admin_charges_rating = forms.ChoiceField(label="Admin Charges Rating", choices=ADMIN_CHARGES,widget=forms.Select(attrs={"class":"form-control"}))





   admin_charges =forms.DecimalField(initial=0,label='Interest Rate', label_suffix=" : ",
                                 widget=forms.NumberInput(attrs={'class': 'form-control'}),
                                 decimal_places=2, required=True,
                                 disabled = False)

   admin_charges_minimum=forms.DecimalField(initial=0,label='Interest Rate', label_suffix=" : ",
                                 widget=forms.NumberInput(attrs={'class': 'form-control'}),
                                 decimal_places=2, required=True,
                                 disabled = False)

   default_admin_charges=forms.DecimalField(initial=0,label='Interest Rate', label_suffix=" : ",
                                 widget=forms.NumberInput(attrs={'class': 'form-control'}),
                                 decimal_places=2, required=True,
                                 disabled = False)


   guarantors= forms.IntegerField(label='Guarantors', label_suffix=" : ",
                  widget=forms.NumberInput(attrs={'class': 'form-control','autocomplete':'off'}),
                  disabled = False)

   loan_age=  forms.IntegerField(label='Guarantors', label_suffix=" : ",
                  widget=forms.NumberInput(attrs={'class': 'form-control','autocomplete':'off'}),
                  disabled = False)



   receipt_type = forms.ChoiceField(label="Receipt Type", choices=RECEIPT_TYPES,widget=forms.Select(attrs={"class":"form-control"}))

   transaction_list=[]
   try:
      transactions = TransactionTypes.objects.filter(category='NON-MONETARY',source__title='LOAN')
      for transaction in transactions:
         small_transaction=(transaction.id,transaction.name)
         transaction_list.append(small_transaction)
   except:
      transaction_list=[]
   transactions = forms.ChoiceField(label="Transactions", choices=transaction_list,widget=forms.Select(attrs={"class":"form-control"}))






class Manage_Commodity_Categories_Optional_properties_Form(forms.Form):
   REQUIRED_STATUS=(
        ('0','NO'),
        ('1','YES')
        )
   interest_rate_required = forms.ChoiceField(label="Interest Rate Required", choices=REQUIRED_STATUS,widget=forms.Select(attrs={"class":"form-control"}))
   admin_charges_required = forms.ChoiceField(label="Admin Charges Required", choices=REQUIRED_STATUS,widget=forms.Select(attrs={"class":"form-control"}))
   guarantor_required = forms.ChoiceField(label="Guarantor Required", choices=REQUIRED_STATUS,widget=forms.Select(attrs={"class":"form-control"}))


class Commodity_Products_add_Form(forms.Form):
   product_name=forms.CharField(label="Product Name",max_length=30,widget=forms.TextInput(attrs={"class":"form-control"}),required=True)
   product_model=forms.CharField(label="Product Name",max_length=30,widget=forms.TextInput(attrs={"class":"form-control"}),required=True)
   details= forms.CharField(widget=forms.Textarea(attrs={"rows":2, "cols":57}))
   unit_cost_price = forms.DecimalField(initial=0,label='Unit Cost Price', label_suffix=" : ",
                              widget=forms.NumberInput(attrs={'class': 'form-control'}),
                              decimal_places=2, required=True,
                              disabled = False)
   status_list=[]
   try:
      statuses = MembershipStatus.objects.all()
      for status in statuses:
         small_status=(status.id,status.title)
         status_list.append(small_status)
   except:
      status_list=[]
   status = forms.ChoiceField(label="Status", choices=status_list,widget=forms.Select(attrs={"class":"form-control"}))


class Commodity_Products_Update_Form(forms.Form):
   product_name=forms.CharField(label="Product Name",max_length=30,widget=forms.TextInput(attrs={"class":"form-control"}),required=True)
   product_model=forms.CharField(label="Product Name",max_length=30,widget=forms.TextInput(attrs={"class":"form-control"}),required=True)
   details= forms.CharField(widget=forms.Textarea(attrs={"rows":2, "cols":57}))
   unit_cost_price = forms.DecimalField(initial=0,label='Unit Cost Price', label_suffix=" : ",
                              widget=forms.NumberInput(attrs={'class': 'form-control'}),
                              decimal_places=2, required=True,
                              disabled = False)

   status = forms.ChoiceField(label="Status", choices=MEMBERSHIP_STATUS,widget=forms.Select(attrs={"class":"form-control"}))



class Commodity_Products_Price_Update_Form(forms.Form):
   product_name=forms.CharField(label="Product Name",max_length=30,widget=forms.TextInput(attrs={"class":"form-control",'readonly':'readonly'}),required=True)
   product_model=forms.CharField(label="Product Name",max_length=30,widget=forms.TextInput(attrs={"class":"form-control",'readonly':'readonly'}),required=True)
   details= forms.CharField(widget=forms.Textarea(attrs={"rows":2, "cols":57,'readonly':'readonly'}))
   unit_cost_price = forms.DecimalField(initial=0,label='Unit Cost Price', label_suffix=" : ",
                              widget=forms.NumberInput(attrs={'class': 'form-control'}),
                              decimal_places=2, required=True,
                              disabled = False)
   coop_price = forms.DecimalField(initial=0,label='Coop Price', label_suffix=" : ",
                              widget=forms.NumberInput(attrs={'class': 'form-control'}),
                              decimal_places=2, required=True,
                              disabled = False)

   status = forms.ChoiceField(label="Status", choices=MEMBERSHIP_STATUS,widget=forms.Select(attrs={"class":"form-control"}))


class membership_commodity_loan_Company_products_details_Form(forms.Form):
   quantity = forms.IntegerField(label='Request Quantity', label_suffix=" : ",
                  widget=forms.NumberInput(attrs={'class': 'form-control','autocomplete':'off'}),
                  disabled = False)



class membership_commodity_loan_Company_products_process_Form(forms.Form):
   # try:
   #    transaction=CertifiableTransactions.objects.get(transaction__code='204')
   #    certification_officers_list=[]

   #    certification_officers = CertificationOfficers.objects.filter(transaction=transaction)

   #    for certification_officer in certification_officers:
   #       small_certification_officer=(certification_officer.id,certification_officer.officer.username)
   #       certification_officers_list.append(small_certification_officer)
   # except:
   #    certification_officers_list=[]

   # certification_officers = forms.ChoiceField(label="Certification Officers", choices=certification_officers_list,widget=forms.Select(attrs={"class":"form-control"}))
   comments= forms.CharField(widget=forms.Textarea(attrs={"rows":2, "cols":55}),required=True)


class Dedicated_Commodity_Product_List_Add_Form1(forms.Form):
   product_name=forms.CharField(label="Product Name",max_length=30,widget=forms.TextInput(attrs={"class":"form-control"}),required=True)
   details=forms.CharField(label="Details",max_length=30,widget=forms.TextInput(attrs={"class":"form-control"}),required=True)
   unit_cost_price = forms.DecimalField(initial=0,label='Unit Cost Price', label_suffix=" : ",
                              widget=forms.NumberInput(attrs={'class': 'form-control'}),
                              decimal_places=2, required=True,
                              disabled = False)
   selling_price = forms.DecimalField(initial=0,label='Unit Cost Price', label_suffix=" : ",
                              widget=forms.NumberInput(attrs={'class': 'form-control'}),
                              decimal_places=2, required=True,
                              disabled = False)
   tyear=forms.CharField(label="Year",max_length=30,widget=forms.TextInput(attrs={"class":"form-control"}),required=True)
   period=forms.CharField(label="Period",max_length=30,widget=forms.TextInput(attrs={"class":"form-control",'readonly':'readonly'}),required=True)


class Dedicated_Commodity_Product_List_Add_Form(forms.Form):
   product_name=forms.CharField(label="Product Name",max_length=30,widget=forms.TextInput(attrs={"class":"form-control",'readonly':'readonly'}),required=True)
   details=forms.CharField(label="Details",max_length=30,widget=forms.TextInput(attrs={"class":"form-control",'readonly':'readonly'}),required=True)
   unit_cost_price = forms.DecimalField(initial=0,label='Unit Cost Price', label_suffix=" : ",
                              widget=forms.NumberInput(attrs={'class': 'form-control'}),
                              decimal_places=2, required=True,
                              disabled = False)
   selling_price = forms.DecimalField(initial=0,label='Unit Cost Price', label_suffix=" : ",
                              widget=forms.NumberInput(attrs={'class': 'form-control'}),
                              decimal_places=2, required=True,
                              disabled = False)
   tyear=forms.CharField(label="Year",max_length=30,widget=forms.TextInput(attrs={"class":"form-control"}),required=True)
   period=forms.CharField(label="Period",max_length=30,widget=forms.TextInput(attrs={"class":"form-control",'readonly':'readonly'}),required=True)



class Essential_Commodity_Product_Select_Form(forms.Form):
   product_name=forms.CharField(label="Product Name",max_length=30,widget=forms.TextInput(attrs={"class":"form-control",'readonly':'readonly'}),required=True)
   details=forms.CharField(label="Details",max_length=30,widget=forms.TextInput(attrs={"class":"form-control",'readonly':'readonly'}),required=True)
   unit_price = forms.DecimalField(initial=0,label='Unit Cost Price', label_suffix=" : ",
                              widget=forms.NumberInput(attrs={'class': 'form-control','readonly':'readonly'}),
                              decimal_places=2, required=True,
                              disabled = False)
   quantity = forms.IntegerField(initial=0,label='Request Quantity', label_suffix=" : ",
                  widget=forms.NumberInput(attrs={'class': 'form-control','autocomplete':'off'}),
                  disabled = False)


# class Essential_Commodity_Product_Selection_Summary_Form(forms.Form):
#    approval_officers_list=[]
#    try:
#       transaction=ApprovableTransactions.objects.get(transaction__code='205')
#       approval_officers = ApprovalOfficers.objects.filter(transaction=transaction)
#       for approval_officer in approval_officers:
#          small_approval_officer=(approval_officer.id,approval_officer.officer.username)
#          approval_officers_list.append(small_approval_officer)
#    except:
#       approval_officers_list=[]

#    approval_officers = forms.ChoiceField(label="Approval Officers", choices=approval_officers_list,widget=forms.Select(attrs={"class":"form-control"}))
#    comments= forms.CharField(widget=forms.Textarea(attrs={"rows":2, "cols":55}),required=True)


class Essential_Commodity_Loan_Request_Approval_Details_form(forms.Form):
   comment= forms.CharField(widget=forms.Textarea(attrs={"rows":2, "cols":50}))

   approval_status = forms.ChoiceField(label="Approval Status", choices=APPROVAL_STATUS,widget=forms.Select(attrs={"class":"form-control"}))

class Essential_Commodity_Loan_Request_Approved_Process_Form(forms.Form):

   start_date = forms.DateField(label='Start Date', label_suffix=" : ",
                             required=True, disabled=False,
                             widget=DateInput(attrs={'class': 'form-control'}),
                             error_messages={'required': "This field is required."})


# class Non_Monetary_Loan_Request_certification_Load_details_form(forms.Form):
#    approval_officers_list=[]
#    try:
#       transaction=ApprovableTransactions.objects.get(transaction__code='204')
#       approval_officers = ApprovalOfficers.objects.filter(transaction=transaction)
#       for approval_officer in approval_officers:
#          small_approval_officer=(approval_officer.id,approval_officer.officer.username)
#          approval_officers_list.append(small_approval_officer)
#    except:
#       approval_officers_list=[]

#    approval_officers = forms.ChoiceField(label="Approval Officers", choices=approval_officers_list,widget=forms.Select(attrs={"class":"form-control"}))

#    certication_status_list=[]
#    try:
#       certication_statuss = CertificationStatus.objects.all()

#       for certication_status in certication_statuss:
#          small_certication_status=(certication_status.id,certication_status.title)
#          certication_status_list.append(small_certication_status)
#    except:
#       certication_status_list=[]

#    certication_status = forms.ChoiceField(label="certication_status", choices=certication_status_list,widget=forms.Select(attrs={"class":"form-control"}))
#    comment= forms.CharField(widget=forms.Textarea(attrs={"rows":2, "cols":50}))



class loan_category_settings_form(forms.Form):
   try:
      loan_list=[]

      loans=TransactionTypes.objects.filter(source__title="LOAN")


      for loan in loans:
         small_loan=(loan.id,loan.name)
         loan_list.append(small_loan)
   except:
      loan_list=[]

   loan = forms.ChoiceField(label="Loans", choices=loan_list,widget=forms.Select(attrs={"class":"form-control"}))

   category = forms.ChoiceField(initial='MONETARY',label="categories", choices=LOAN_CATEGORY,widget=forms.Select(attrs={"class":"form-control"}))



class Commodity_Transaction_Period_form(forms.Form):
   period=forms.CharField(label="Period",max_length=255,widget=forms.TextInput(attrs={"class":"form-control"}),required=True)


class Commodity_Transaction_Period_Batch_form(forms.Form):
   batch=forms.CharField(label="Batch",max_length=255,widget=forms.TextInput(attrs={"class":"form-control"}),required=True)


class Product_Linking_Period_Load_form(forms.Form):
   try:
      transaction_list=[]

      transactions=TransactionTypes.objects.filter(category="NON-MONETARY")


      for transaction in transactions:
         small_transaction=(transaction.id,transaction.name)
         transaction_list.append(small_transaction)
   except:
      transaction_list=[]

   transaction = forms.ChoiceField(label="Transactions", choices=transaction_list,widget=forms.Select(attrs={"class":"form-control"}))


   try:
      period_list=[]

      periods=Commodity_Period.objects.all()


      for period in periods:
         small_period=(period.id,period.title)
         period_list.append(small_period)
   except:
      period_list=[]

   period = forms.ChoiceField(label="Periods", choices=period_list,widget=forms.Select(attrs={"class":"form-control"}))


   try:
      batch_list=[]

      batches=Commodity_Period_Batch.objects.all()


      for batch in batches:
         small_batch=(batch.id,batch.title)
         batch_list.append(small_batch)
   except:
      batch_list=[]

   batch = forms.ChoiceField(label="Batches", choices=batch_list,widget=forms.Select(attrs={"class":"form-control"}))




class Product_Linking_Details_Preview_form(forms.Form):

   product_name=forms.CharField(label="Name",max_length=255,widget=forms.TextInput(attrs={"class":"form-control","readonly":"readonly"}),required=True)
   product_model=forms.CharField(label="Model",max_length=255,widget=forms.TextInput(attrs={"class":"form-control","readonly":"readonly"}),required=True)
   details=forms.CharField(label="detials",max_length=255,widget=forms.TextInput(attrs={"class":"form-control","readonly":"readonly"}),required=True)


   amount = forms.DecimalField(initial=0,label='Amount', label_suffix=" : ",
                              widget=forms.NumberInput(attrs={'class': 'form-control'}),
                              decimal_places=2, required=True,
                              disabled = False)
   coop_amount = forms.DecimalField(initial=0,label='Cooperative Amount', label_suffix=" : ",
                              widget=forms.NumberInput(attrs={'class': 'form-control'}),
                              decimal_places=2, required=True,
                              disabled = False)


class membership_commodity_loan_Company_products_Criteria_Settings_form(forms.Form):
   image=forms.FileField(label="Payslip Evidience", widget=forms.FileInput(attrs={"class":"form-control"}),required=False)
   period = forms.DateField(label='Payment Period', label_suffix=" : ",
                             required=True, disabled=False,
                             widget=DateInput(attrs={'class': 'form-control'}),
                             error_messages={'required': "This field is required."})


   net_pay = forms.DecimalField(initial=0,label='Net Pay', label_suffix=" : ",
                              widget=forms.NumberInput(attrs={'class': 'form-control'}),
                              decimal_places=2, required=True,
                              disabled = False)


class Transaction_Salary_adjustment_Request_Process_form(forms.Form):
   CHOICES =(
    ("False", "NO"),
    ("True", "YES"),
   )
   update_payslip=forms.ChoiceField(label="Update Payslip", choices=CHOICES,widget=forms.Select(attrs={"class":"form-control"}))

   image=forms.FileField(label="Payslip Evidience", widget=forms.FileInput(attrs={"class":"form-control"}),required=False)
   period = forms.DateField(label='Payment Period', label_suffix=" : ",
                             required=True, disabled=False,
                             widget=DateInput(attrs={'class': 'form-control'}),
                             error_messages={'required': "This field is required."})

   existing_gross_pay = forms.DecimalField(initial=0,label='Existing Gross Pay', label_suffix=" : ",
                              widget=forms.NumberInput(attrs={'class': 'form-control','readonly':'readonly'}),
                              decimal_places=2, required=True,
                              disabled = False)

   current_gross_pay = forms.DecimalField(initial=0,label='Current Gross Pay', label_suffix=" : ",
                              widget=forms.NumberInput(attrs={'class': 'form-control'}),
                              decimal_places=2, required=True,
                              disabled = False)


class Transaction_Salary_adjustment_Request_Approval_Process_form(forms.Form):

   comment= forms.CharField(widget=forms.Textarea(attrs={"rows":5, "cols":50}))

   approval_status = forms.ChoiceField(label="Approval Status", choices=APPROVAL_STATUS,widget=forms.Select(attrs={"class":"form-control"}))



class membership_commodity_loan_Period_certification_transaction_details_form(forms.Form):
   comment= forms.CharField(widget=forms.Textarea(attrs={"rows":5, "cols":50}))

   certication_status = forms.ChoiceField(label="certication_status", choices=CERTIFICATION_STATUS,widget=forms.Select(attrs={"class":"form-control"}))


class membership_commodity_loan_Period_approval_transaction_details_form(forms.Form):
   comment= forms.CharField(widget=forms.Textarea(attrs={"rows":5, "cols":50}))
   approval_status = forms.ChoiceField(initial='APPROVED',label="approval_status", choices=APPROVAL_STATUS,widget=forms.Select(attrs={"class":"form-control"}))




class membership_commodity_loan_form_sales_transaction_form(forms.Form):

   form_print = forms.ChoiceField(label="Form Print", choices=YESNO,widget=forms.Select(attrs={"class":"form-control"}))
   channel = forms.ChoiceField(label="Payment Channels", choices=CHANNELS,widget=forms.Select(attrs={"class":"form-control"}))



   duration = forms.IntegerField(initial=0,label='Duration', label_suffix=" : ",
                  widget=forms.NumberInput(attrs={'class': 'form-control','autocomplete':'off','readonly':'readonly'}),
                  disabled = False)
   amount = forms.DecimalField(initial=0,label='Amount', label_suffix=" : ",
                           widget=forms.NumberInput(attrs={'class': 'form-control','readonly':'readonly'}),
                           decimal_places=2, required=True,
                           disabled = False)

   interest = forms.DecimalField(initial=0,label='Interest', label_suffix=" : ",
                           widget=forms.NumberInput(attrs={'class': 'form-control','readonly':'readonly'}),
                           decimal_places=2, required=True,
                              disabled = False)
   admin_charges = forms.DecimalField(initial=0,label='Admin Charges', label_suffix=" : ",
                           widget=forms.NumberInput(attrs={'class': 'form-control','readonly':'readonly'}),
                           decimal_places=2, required=True,
                              disabled = False)
   repayment = forms.DecimalField(initial=0,label='Repayment', label_suffix=" : ",
                           widget=forms.NumberInput(attrs={'class': 'form-control','readonly':'readonly'}),
                           decimal_places=2, required=True,
                              disabled = False)
   receipt_no = forms.IntegerField(label='Receipt No', label_suffix=" : ", min_value=0,
                  widget=forms.NumberInput(attrs={'class': 'form-control','autocomplete':'off'}),
                  disabled = False)


class Loan_application_approval_form(forms.Form):
   approval_status = forms.ChoiceField(initial="APPROVED",label="Approval Status", choices=APPROVAL_STATUS,widget=forms.Select(attrs={"class":"form-control"}))

   comment= forms.CharField(widget=forms.Textarea(attrs={"rows":5, "cols":50}))

   amount = forms.DecimalField(initial=0,label='Amount', label_suffix=" : ", min_value=0,  max_digits=20,
                              widget=forms.NumberInput(attrs={'class': 'form-control'}),
                              decimal_places=2, required=True,
                              disabled = False,
                              error_messages={'required': "Please Enter Amount Approved"})
   date_approved =forms.DateField(label='Date Approved', label_suffix=" : ",
                             required=True, disabled=False,
                             widget=DateInput(attrs={'class': 'form-control'}),
                             error_messages={'required': "This field is required."})



class Loan_unscheduling_approval_preview_form(forms.Form):
   approval_status = forms.ChoiceField(label="Approval Status", choices=APPROVAL_STATUS,widget=forms.Select(attrs={"class":"form-control"}))

   comment= forms.CharField(widget=forms.Textarea(attrs={"rows":5, "cols":65}))
   comment_exist= forms.CharField(widget=forms.Textarea(attrs={"rows":5, "cols":65,'readonly':'readonly'}))


class loan_unscheduling_request_transaction_processing_details_form(forms.Form):
   approval_officer = forms.CharField(label="Approval Officer",max_length=255,widget=forms.TextInput(attrs={"class":"form-control","readonly":"readonly"}),required=True)
   approved_date = forms.CharField(label="approved_date",max_length=255,widget=forms.TextInput(attrs={"class":"form-control","readonly":"readonly"}),required=True)

   approval_comment= forms.CharField(widget=forms.Textarea(attrs={"rows":5, "cols":65,'readonly':'readonly'}))
   comment_exist= forms.CharField(widget=forms.Textarea(attrs={"rows":5, "cols":65,'readonly':'readonly'}))


class Standing_Order_Suspension_Form(forms.Form):
   reasons= forms.CharField(widget=forms.Textarea(attrs={"rows":3, "cols":65}))
   saving_list=[]
   try:
      source=TransactionSources.objects.get(title='SAVINGS')
      savings = TransactionTypes.objects.filter(source_id=source).filter(~Q(code=101))
      for saving in savings:
         small_saving=(saving.id,saving.name)
         saving_list.append(small_saving)
   except:
      saving_list=[]

   saving = forms.ChoiceField(label="savings", choices=saving_list,widget=forms.Select(attrs={"class":"form-control"}))




class Standing_Order_Suspension_Transaction_Approvals_Load_Details_form(forms.Form):

   approval_status = forms.ChoiceField(label="Approval Status", choices=APPROVAL_STATUS,widget=forms.Select(attrs={"class":"form-control"}))

   comment= forms.CharField(widget=forms.Textarea(attrs={"rows":5, "cols":65}))
   purpose= forms.CharField(widget=forms.Textarea(attrs={"rows":5, "cols":65,'readonly':'readonly'}))

class Standing_Order_Suspension_Transaction_Releasing_Details_form(forms.Form):
   comment= forms.CharField(widget=forms.Textarea(attrs={"rows":5, "cols":65}))


class members_shop_sales_credit_generate_form(forms.Form):
   period = forms.DateField(label='Payment Period', label_suffix=" : ",
                             required=True, disabled=False,
                             widget=DateInput(attrs={'class': 'form-control'}),
                             error_messages={'required': "This field is required."})


class shop_monthly_deductions_generate_form(forms.Form):
   transaction_period =forms.CharField(label="detials",max_length=255,widget=forms.TextInput(attrs={"class":"form-control","readonly":"readonly"}),required=True)


class stock_status_list_details_Form(forms.Form):

   start_date = forms.DateField(label='Start Date', label_suffix=" : ",
                             required=True, disabled=False,
                             widget=DateInput(attrs={'class': 'form-control'}),
                             error_messages={'required': "This field is required."})
   stop_date = forms.DateField(label='Stop Date', label_suffix=" : ",
                             required=True, disabled=False,
                             widget=DateInput(attrs={'class': 'form-control'}),
                             error_messages={'required': "This field is required."})


class Members_Credit_sales_Cash_Deposit_Distributions_Process_form(forms.Form):
   amount_paid = forms.DecimalField(initial=0,label='Amount Paid', label_suffix=" : ", min_value=0,  max_digits=20,
                              widget=forms.NumberInput(attrs={'class': 'form-control','readonly':'readonly'}),
                              decimal_places=2, required=True,
                              disabled = False,
                              error_messages={'required': "Please Enter Amount Approved"})

   amount_distributed = forms.DecimalField(initial=0,label='Amount Distributed', label_suffix=" : ", min_value=0,  max_digits=20,
                              widget=forms.NumberInput(attrs={'class': 'form-control','readonly':'readonly'}),
                              decimal_places=2, required=True,
                              disabled = False,
                              error_messages={'required': "Please Enter Amount Approved"})

   balance_amount = forms.DecimalField(initial=0,label='Balance Amount', label_suffix=" : ", min_value=0,  max_digits=20,
                              widget=forms.NumberInput(attrs={'class': 'form-control','readonly':'readonly'}),
                              decimal_places=2, required=True,
                              disabled = False,
                              error_messages={'required': "Please Enter Amount Approved"})


class Members_Welfare_Report_General_Records_form(forms.Form):
   start_year_list=[]

   try:
      start_years = MembersWelfareAccounts.objects.all().order_by('year').values_list('id','year').distinct()

      for start_year in start_years:
         small_start_year=(start_year[1],start_year[1])
         start_year_list.append(small_start_year)
   except:
      start_year_list=[]

   start_year=forms.ChoiceField(label="start_year",choices=start_year_list,widget=forms.Select(attrs={"class":"form-control"}))

   stop_year_list=[]

   try:
      stop_years = MembersWelfareAccounts.objects.all().order_by('year').values_list('id','year').distinct()

      for stop_year in stop_years:
         small_stop_year=(stop_year[1],stop_year[1])
         stop_year_list.append(small_stop_year)
   except:
      stop_year_list=[]

   stop_year=forms.ChoiceField(label="stop_year",choices=stop_year_list,widget=forms.Select(attrs={"class":"form-control"}))


class Individual_Capture_Form(forms.Form):
   title_list=[]

   try:
      titles = Titles.objects.all().order_by("title")
      for title in titles:
         small_title=(title.id,title.title)
         title_list.append(small_title)
   except:
      title_list=[]

   title=forms.ChoiceField(label="title",choices=title_list,widget=forms.Select(attrs={"class":"form-control"}))


   year_array=[]
   for i in range(2000,now.year + 1):
      year_array.append((i,i))
   # print(year_array)
   dob = forms.DateField(label='Date of Birth', label_suffix=" : ",
                                required=True, disabled=False,
                                widget=DateInput(attrs={'class': 'form-control'}),
                                error_messages={'required': "This field is required."})
   date_hired = forms.DateField(label='Date Hired', label_suffix=" : ",
                                required=True, disabled=False,
                                widget=DateInput(attrs={'class': 'form-control'}),
                                error_messages={'required': "This field is required."})

   ippis_no =forms.CharField(label="IPPIS NO",max_length=20,widget=forms.TextInput(attrs={"class":"form-control"}),required=True)
   file_no =forms.CharField(label="File No",max_length=20,widget=forms.TextInput(attrs={"class":"form-control"}),required=True)
   coop_no =forms.CharField(label="Coop. No",max_length=10,widget=forms.TextInput(attrs={"class":"form-control"}),required=True)
   last_name =forms.CharField(label="Last Name",max_length=255,widget=forms.TextInput(attrs={"class":"form-control"}),required=True)
   first_name =forms.CharField(label="First Name",max_length=255,widget=forms.TextInput(attrs={"class":"form-control"}),required=True)
   middle_name =forms.CharField(label="Middle Name",max_length=255,widget=forms.TextInput(attrs={"class":"form-control"}))
   month_joined = forms.ChoiceField(label="Month Joined", choices=MONTH_LIST,widget=forms.Select(attrs={"class":"form-control"}))
   year_joined = forms.ChoiceField(label="Year Joined", choices=year_array,widget=forms.Select(attrs={"class":"form-control"}))
   # year_joined =forms.CharField(label="Year Joined",max_length=4,widget=forms.TextInput(attrs={"class":"form-control"}),required=True)
   phone_number =forms.CharField(label="Phone Number",max_length=11,widget=forms.TextInput(attrs={"class":"form-control"}),required=True)

   salary_institution_list=[]
   try:
      salary_institutions = SalaryInstitution.objects.all().order_by('rank')
      for salary_institution in salary_institutions:
         small_salary_institution=(salary_institution.id,salary_institution.title)
         salary_institution_list.append(small_salary_institution)
   except:
      salary_institution_list=[]
   salary_institution = forms.ChoiceField(label="Salary Institution", choices=salary_institution_list,widget=forms.Select(attrs={"class":"form-control"}))


class Termination_Loan_Allowed_load_Form(forms.Form):

   termination_type_list=[]
   try:
      termination_types = Termination_Types.objects.all().order_by('title')
      for termination_type in termination_types:
         small_termination_type=(termination_type.id,termination_type.title)
         termination_type_list.append(small_termination_type)
   except:
      termination_type_list=[]
   termination_type = forms.ChoiceField(label="Termination Type", choices=termination_type_list,widget=forms.Select(attrs={"class":"form-control"}))


class membership_termination_Duration_form(forms.Form):
   duration = forms.IntegerField(initial=0,label='Duration', label_suffix=" : ", min_value=0,  required=False,
                                 widget=forms.NumberInput(attrs={'class': 'form-control'}),
                                disabled = False, error_messages={'required': "Please Duration"})


class membership_termination_Request_Approval_Process_form(forms.Form):
   comment= forms.CharField(widget=forms.Textarea(attrs={"rows":5, "cols":60}))

   approval_status = forms.ChoiceField(label="approval_status", choices=APPROVAL_STATUS,widget=forms.Select(attrs={"class":"form-control"}))


class membership_termination_Disbursement_Processing_Preview_form(forms.Form):
   channels = forms.ChoiceField(label="Payment Channels", choices=PAYMENT_CHANNEL,widget=forms.Select(attrs={"class":"form-control"}))

   amount = forms.DecimalField(initial=0,label='Amount', label_suffix=" : ", min_value=0,  max_digits=20,
                              widget=forms.NumberInput(attrs={'class': 'form-control','readonly':'readonly'}),
                              decimal_places=2, required=True,
                              disabled = False,
                              error_messages={'required': "Please Enter Amount Approved"})


class membership_termination_Disbursement_Processing_form(forms.Form):
   pv_number =forms.CharField(label="PV Number",max_length=20,widget=forms.TextInput(attrs={"class":"form-control"}),required=True)
   amount = forms.DecimalField(initial=0,label='Amount', label_suffix=" : ", min_value=0,  max_digits=20,
                              widget=forms.NumberInput(attrs={'class': 'form-control','readonly':'readonly'}),
                              decimal_places=2, required=True,
                              disabled = False,
                              error_messages={'required': "Please Enter Amount Approved"})
   pv_date = forms.DateField(label='PV Date', label_suffix=" : ",
                                required=True, disabled=False,
                                widget=DateInput(attrs={'class': 'form-control'}),
                                error_messages={'required': "This field is required."})
   transfer_date = forms.DateField(label='Transfer Date', label_suffix=" : ",
                                required=True, disabled=False,
                                widget=DateInput(attrs={'class': 'form-control'}),
                                error_messages={'required': "This field is required."})
   cheque_date = forms.DateField(label='Cheque Date', label_suffix=" : ",
                                required=True, disabled=False,
                                widget=DateInput(attrs={'class': 'form-control'}),
                                error_messages={'required': "This field is required."})

   cheque_number =forms.CharField(label="Cheque Number",max_length=20,widget=forms.TextInput(attrs={"class":"form-control"}),required=True)

   account_list=[]
   try:
      accounts = CooperativeBankAccounts.objects.all()
      for account in accounts:
         small_account=(account.id,account.account_name + "- (" + str(account.account_number) + ' - ' + account.bank.title + ")" )
         account_list.append(small_account)
   except:
      account_list=[]

   accounts = forms.ChoiceField(label="Payment Account", choices=account_list,widget=forms.Select(attrs={"class":"form-control"}))


class standing_order_reactivate_account_form(forms.Form):
   existing_amount = forms.DecimalField(initial=0,label='Existing Amount', label_suffix=" : ", min_value=0,  max_digits=20,
                              widget=forms.NumberInput(attrs={'class': 'form-control','readonly':'readonly'}),
                              decimal_places=2, required=True,
                              disabled = False,
                              error_messages={'required': "Please Enter Amount Approved"})
   amount = forms.DecimalField(initial=0,label='Amount', label_suffix=" : ", min_value=0,  max_digits=20,
                              widget=forms.NumberInput(attrs={'class': 'form-control'}),
                              decimal_places=2, required=True,
                              disabled = False,
                              error_messages={'required': "Please Enter Amount Approved"})


class TransactionTypes_Sources_Manage_Process_form(forms.Form):
   salary_rate = forms.IntegerField(initial=0,label='Enter Rate', label_suffix=" : ", min_value=0, required=True,
                              widget=forms.NumberInput(attrs={'class': 'form-control'}),
                             help_text="This value is greater than or equal to 0 & less than or equal to 100.",
                             disabled = False, error_messages={'required': "Please Enter quantity."})
   loan_based_saving = forms.IntegerField(initial=0,label='Enter Loan Based Saving', label_suffix=" : ", min_value=0, required=True,
                              widget=forms.NumberInput(attrs={'class': 'form-control'}),
                             help_text="This value is greater than or equal to 0 & less than or equal to 100.",
                             disabled = False, error_messages={'required': "Please Enter quantity."})

   maximum_amount = forms.DecimalField(initial=0,label='Maximum Amount', label_suffix=" : ", min_value=0,  max_digits=20,
                              widget=forms.NumberInput(attrs={'class': 'form-control'}),
                              decimal_places=2, required=True,
                              disabled = False,
                              error_messages={'required': "Please Enter Amount Approved"})


class Manage_Departments_Processing_form(forms.Form):
   title =forms.CharField(label="Title",max_length=255,widget=forms.TextInput(attrs={"class":"form-control"}),required=True)


class BankAccounts_Designation_Process_form(forms.Form):
   transaction_list=[]
   try:
      transactions = TransactionTypes.objects.all()
      for transaction in transactions:
         small_transaction=(transaction.id,transaction.name)
         transaction_list.append(small_transaction)
   except:
      transaction_list=[]

   transactions = forms.ChoiceField(label="Payment transactions", choices=transaction_list,widget=forms.Select(attrs={"class":"form-control"}))





class Users_Task_Add_form(forms.Form):
   title =forms.CharField(label="Title",max_length=255,widget=forms.TextInput(attrs={"class":"form-control"}))
   rank = forms.IntegerField(initial=0,label='Rank', label_suffix=" : ", min_value=0,
                  widget=forms.NumberInput(attrs={'class': 'form-control','autocomplete':'off'}),
                  disabled = False)




class Xmas_Savings_Transaction_Period_form(forms.Form):
    batch =forms.CharField(label="Batch",max_length=255,widget=forms.TextInput(attrs={"class":"form-control"}))




class Xmas_Savings_Shortlisting_form(forms.Form):
   transaction_date = forms.DateField(label='Transaction Date', label_suffix=" : ",
                                required=True, disabled=False,
                                widget=DateInput(attrs={'class': 'form-control'}),
                                error_messages={'required': "This field is required."})
   batch_list=[]
   try:

      batches=XmasSavingsTransactionPeriod.objects.all()

      for batch in batches:
         small_batch=(batch.id,batch.batch)
         batch_list.append(small_batch)
   except:
      batch_list=[]

   batch = forms.ChoiceField(label="Batches", choices=batch_list,widget=forms.Select(attrs={"class":"form-control"}))

class Xmas_Savings_Shortlisting_Export_form(forms.Form):
   CHOICES=(
        ("CASH",'CASH'),
        ("TRANSFERRED",'TRANSFERRED')
        )
   category = forms.ChoiceField(label="Category", choices=CHOICES,widget=forms.Select(attrs={"class":"form-control"}))

   batch_list=[]
   try:

      batches=Xmas_Savings_Generated.objects.all()

      for batch in batches:
         small_batch=(batch.batch,batch.batch)
         batch_list.append(small_batch)
   except:
      batch_list=[]

   batch = forms.ChoiceField(label="Batches", choices=batch_list,widget=forms.Select(attrs={"class":"form-control"}))

class Xmas_Savings_Shortlisting_Processing_Preview_form(forms.Form):
   generated_amount = forms.DecimalField(initial=0,label='Generated Amount', label_suffix=" : ", min_value=0,  max_digits=20,
                              widget=forms.NumberInput(attrs={'class': 'form-control','readonly':'readonly'}),
                              decimal_places=2, required=True,
                              disabled = False,
                              error_messages={'required': "Please Enter Amount Paid"})
   amount_paid = forms.DecimalField(initial=0,label='Amount Paid', label_suffix=" : ", min_value=0,  max_digits=20,
                              widget=forms.NumberInput(attrs={'class': 'form-control'}),
                              decimal_places=2, required=True,
                              disabled = False,
                              error_messages={'required': "Please Enter Amount Paid"})


class Xmas_Savings_Default_Transfer_Account_form(forms.Form):
   transaction_list=[]
   try:
      transactions = TransactionTypes.objects.filter(source__title="SAVINGS")
      for transaction in transactions:
         small_transaction=(transaction.id,transaction.name)
         transaction_list.append(small_transaction)
   except:
      transaction_list=[]

   transaction = forms.ChoiceField(label="Transactions", choices=transaction_list,widget=forms.Select(attrs={"class":"form-control"}))

class TransactionEnabler_Form(forms.Form):
   title=forms.CharField(label="Title",max_length=30,widget=forms.TextInput(attrs={"class":"form-control",}),required=True)

   task_visible = forms.ChoiceField(label="Task Visible", choices=YESNO,widget=forms.Select(attrs={"class":"form-control"}))


class Expired_Products_Main_Tracking_Write_Off_Form(forms.Form):
   available_quantity = forms.IntegerField(initial=0,label='Available Quantity', label_suffix=" : ", min_value=0,  required=False,
                                 widget=forms.NumberInput(attrs={'class': 'form-control','readonly':'readonly'}),
                                disabled = False, error_messages={'required': "Please Min Unit"})

   expiry_quantity = forms.IntegerField(initial=0,label='Expiry Quantity', label_suffix=" : ", min_value=1,  required=False,
                                 widget=forms.NumberInput(attrs={'class': 'form-control'}),
                                disabled = False, error_messages={'required': "Please Expiry Quantity"})

   unit_selling_price = forms.DecimalField(initial=0,label='Unit Selling Price', label_suffix=" : ", min_value=1,  max_digits=20,
                              widget=forms.NumberInput(attrs={'class': 'form-control'}),
                              decimal_places=2, required=True,
                              disabled = False,
                              error_messages={'required': "Please Enter Amount Paid"})
   unit_cost_price = forms.DecimalField(initial=0,label='Unit Cost Price', label_suffix=" : ", min_value=1,  max_digits=20,
                              widget=forms.NumberInput(attrs={'class': 'form-control'}),
                              decimal_places=2, required=True,
                              disabled = False,
                              error_messages={'required': "Please Enter Amount Paid"})

   expiry_date = forms.DateField(label='Expiry Date', label_suffix=" : ",
                                required=True, disabled=False,
                                widget=DateInput(attrs={'class': 'form-control'}),
                                error_messages={'required': "This field is required."})


class Expired_Products_Auction_Tracking_Write_Off_Form(forms.Form):
   available_quantity = forms.IntegerField(initial=0,label='Available Quantity', label_suffix=" : ", min_value=0,  required=False,
                                 widget=forms.NumberInput(attrs={'class': 'form-control','readonly':'readonly'}),
                                disabled = False, error_messages={'required': "Please Min Unit"})


   unit_selling_price = forms.DecimalField(initial=0,label='Unit Selling Price', label_suffix=" : ", min_value=1,  max_digits=20,
                              widget=forms.NumberInput(attrs={'class': 'form-control','readonly':'readonly'}),
                              decimal_places=2, required=True,
                              disabled = False,
                              error_messages={'required': "Please Enter Amount Paid"})
   unit_cost_price = forms.DecimalField(initial=0,label='Unit Cost Price', label_suffix=" : ", min_value=1,  max_digits=20,
                              widget=forms.NumberInput(attrs={'class': 'form-control','readonly':'readonly'}),
                              decimal_places=2, required=True,
                              disabled = False,
                              error_messages={'required': "Please Enter Amount Paid"})

   expiry_date = forms.DateField(label='Expiry Date', label_suffix=" : ",
                                required=True, disabled=False,
                                widget=DateInput(attrs={'class': 'form-control','readonly':'readonly'}),
                                error_messages={'required': "This field is required."})

class Daily_Sales_Summar_Form(forms.Form):
   CHOICES=(
        ("POS",'POS'),
        ("TRANSFER",'TRANSFER')
        )
   channel = forms.ChoiceField(label="Category", choices=CHOICES,widget=forms.Select(attrs={"class":"form-control"}))

   amount = forms.DecimalField(initial=0,label='Unit Cost Price', label_suffix=" : ", min_value=1,  max_digits=20,
                              widget=forms.NumberInput(attrs={'class': 'form-control'}),
                              decimal_places=2, required=True,
                              disabled = False,
                              error_messages={'required': "Please Enter Amount Paid"})


   bank_list=[]
   try:
      banks = Banks.objects.all()
      for bank in banks:
         small_bank=(bank.id,bank.title)
         bank_list.append(small_bank)
   except:
      bank_list=[]

   banks = forms.ChoiceField(label="Banks", choices=bank_list,widget=forms.Select(attrs={"class":"form-control"}))
   account_name=forms.CharField(label="Account Name",max_length=255,widget=forms.TextInput(attrs={"class":"form-control",}),required=False)
   other_details=forms.CharField(label="Other Details",max_length=255,widget=forms.TextInput(attrs={"class":"form-control",}),required=False)

   bank_account_list=[]
   try:
      bank_accounts = CooperativeBankAccounts.objects.all()

      for bank_account in bank_accounts:
         small_bank_account=(bank_account.id,bank_account.account_name + '-' + bank_account.account_number + '-' + bank_account.bank.title )
         bank_account_list.append(small_bank_account)
   except:
      bank_account_list=[]
   coop_accounts = forms.ChoiceField(label="Coop Accounts", choices=bank_account_list,widget=forms.Select(attrs={"class":"form-control"}))


class Final_Members_Cash_Sales_Processing_form(forms.Form):
   receipt_print = forms.ChoiceField(label="Receipt Print", choices=YESNO,widget=forms.Select(attrs={"class":"form-control"}))
   # receipt_no=forms.CharField(initial=0,label="Receipt No",max_length=255,widget=forms.TextInput(attrs={"class":"form-control",}))
   receipt_no = forms.IntegerField(initial=0,label='receipt_no', label_suffix=" : ", min_value=0,  required=False,
                                 widget=forms.NumberInput(attrs={'class': 'form-control'}),
                                disabled = False, error_messages={'required': "Please Min Unit"})


class Expenditure_Manager_form(forms.Form):
   amount = forms.DecimalField(initial=0,label='Amount', label_suffix=" : ", min_value=1,  max_digits=20,
                        widget=forms.NumberInput(attrs={'class': 'form-control'}),
                              decimal_places=2, required=True,
                              disabled = False,
                              error_messages={'required': "Please Enter Amount Paid"})

   details=forms.CharField(widget=forms.Textarea(attrs={"rows":3, "cols":50}),required=True)
   reference=forms.CharField(label="Reference",max_length=255,widget=forms.TextInput(attrs={"class":"form-control",}),required=False)


class Manage_Product_CodeForm(forms.Form):
   code=forms.CharField(label="Code",max_length=255,widget=forms.TextInput(attrs={"class":"form-control",}),required=False)



class Product_Purchase_Day_End_Transaction_form(forms.Form):
   period = forms.DateField(label='Period', label_suffix=" : ",
                                required=True, disabled=False,
                                widget=DateInput(attrs={'class': 'form-control'}),
                                error_messages={'required': "This field is required."})


class members_credit_sales_debt_recovery_cash_payment_current_day_form(forms.Form):
   receipt_print = forms.ChoiceField(label="Receipt Print", choices=YESNO,widget=forms.Select(attrs={"class":"form-control"}))

   receipt_no = forms.IntegerField(initial=0,label='receipt_no', label_suffix=" : ", min_value=0,  required=False,
                                 widget=forms.NumberInput(attrs={'class': 'form-control'}),
                                disabled = False, error_messages={'required': "Please Min Unit"})
   amount_due = forms.DecimalField(initial=0,label='Amount Due', label_suffix=" : ", min_value=1,  max_digits=20,
                        widget=forms.NumberInput(attrs={'class': 'form-control','readonly':'readonly'}),
                              decimal_places=2, required=True,
                              disabled = False,
                              error_messages={'required': "Please Enter Amount Paid"})

   amount_paid = forms.DecimalField(initial=0,label='Amount Paid', label_suffix=" : ", min_value=1,  max_digits=20,
                        widget=forms.NumberInput(attrs={'class': 'form-control'}),
                              decimal_places=2, required=True,
                              disabled = False,
                              error_messages={'required': "Please Enter Amount Paid"})

   receipt_type = forms.ChoiceField(label="Receipt Type", choices=RECEIPT_TYPES,widget=forms.Select(attrs={"class":"form-control"}))



class Item_Return_Process_issue_item_Preview_Form(forms.Form):
   CHOICES=(
        ("CASH",'CASH'),
        ("POS",'POS'),
        ("TRANSFER",'TRANSFER')
        )
   channel = forms.ChoiceField(label="Category", choices=CHOICES,widget=forms.Select(attrs={"class":"form-control"}))

   prev_amount = forms.DecimalField(initial=0,label='Prev. Amount', label_suffix=" : ", min_value=1,  max_digits=20,
                              widget=forms.NumberInput(attrs={'class': 'form-control','readonly':'readonly'}),
                              decimal_places=2, required=True,
                              disabled = False,
                              error_messages={'required': "Please Enter Amount Paid"})
   current_amount = forms.DecimalField(initial=0,label='Current Amount', label_suffix=" : ", min_value=1,  max_digits=20,
                              widget=forms.NumberInput(attrs={'class': 'form-control','readonly':'readonly'}),
                              decimal_places=2, required=True,
                              disabled = False,
                              error_messages={'required': "Please Enter Amount Paid"})

   balance_amount = forms.DecimalField(initial=0,label='Balance Amount', label_suffix=" : ", min_value=1,  max_digits=20,
                              widget=forms.NumberInput(attrs={'class': 'form-control','readonly':'readonly'}),
                              decimal_places=2, required=True,
                              disabled = False,
                              error_messages={'required': "Please Enter Amount Paid"})

   receipt_type = forms.ChoiceField(label="Receipt Type", choices=RECEIPT_TYPES,widget=forms.Select(attrs={"class":"form-control"}))

   account_name=forms.CharField(label="Account Name",max_length=255,widget=forms.TextInput(attrs={"class":"form-control",}),required=False)
   other_details=forms.CharField(label="Other Details",max_length=255,widget=forms.TextInput(attrs={"class":"form-control",}),required=False)

   receipt_no = forms.IntegerField(initial=0,label='receipt_no', label_suffix=" : ", min_value=0,  required=False,
                                 widget=forms.NumberInput(attrs={'class': 'form-control'}),
                                disabled = False, error_messages={'required': "Please Min Unit"})

   amount_due = forms.DecimalField(initial=0,label='Amount Due', label_suffix=" : ", min_value=1,  max_digits=20,
                        widget=forms.NumberInput(attrs={'class': 'form-control','readonly':'readonly'}),
                              decimal_places=2, required=True,
                              disabled = False,
                              error_messages={'required': "Please Enter Amount Paid"})


   bank_list=[]
   try:
      banks = Banks.objects.all()
      for bank in banks:
         small_bank=(bank.id,bank.title)
         bank_list.append(small_bank)
   except:
      bank_list=[]

   banks = forms.ChoiceField(label="Banks", choices=bank_list,widget=forms.Select(attrs={"class":"form-control"}))

   bank_account_list=[]
   try:
      bank_accounts = CooperativeBankAccounts.objects.all()

      for bank_account in bank_accounts:
         small_bank_account=(bank_account.id,bank_account.account_name + '-' + bank_account.account_number + '-' + bank_account.bank.title )
         bank_account_list.append(small_bank_account)
   except:
      bank_account_list=[]
   coop_accounts = forms.ChoiceField(label="Coop Accounts", choices=bank_account_list,widget=forms.Select(attrs={"class":"form-control"}))


   receipt_print = forms.ChoiceField(label="Receipt Print", choices=YESNO,widget=forms.Select(attrs={"class":"form-control"}))


class Stock_Without_Prices_Update_Form(forms.Form):
   unit_cost_price = forms.DecimalField(initial=0,label='Unit Cost Price', label_suffix=" : ", min_value=1,  max_digits=20,
                              widget=forms.NumberInput(attrs={'class': 'form-control'}),
                              decimal_places=2, required=True,
                              disabled = False,
                              error_messages={'required': "Please Enter Amount"})

   unit_selling_price = forms.DecimalField(initial=0,label='Unit Selling Price', label_suffix=" : ", min_value=1,  max_digits=20,
                              widget=forms.NumberInput(attrs={'class': 'form-control','readonly':'readonly'}),
                              decimal_places=2, required=True,
                              disabled = False,
                              error_messages={'required': "Please Enter Amount Paid"})




class FormAutoPrint_Settings_Update_Form(forms.Form):
   title =forms.CharField(label="Title",max_length=255,widget=forms.TextInput(attrs={"class":"form-control"}))
   status = forms.ChoiceField(label="Form Prints", choices=YESNO,widget=forms.Select(attrs={"class":"form-control"}))

class membership_commodity_loan_Company_products_proceed_Form(forms.Form):
   channels = forms.ChoiceField(initial="CASH",label="Payment Channels", choices=CHANNELS,widget=forms.Select(attrs={"class":"form-control"}))

class membership_commodity_loan_form_sales_process_Form(forms.Form):
   form_print = forms.ChoiceField(label="Form Print", choices=YESNO,widget=forms.Select(attrs={"class":"form-control"}))
   amount = forms.DecimalField(initial=0,label='Unit Cost Price', label_suffix=" : ", min_value=1,  max_digits=20,
                              widget=forms.NumberInput(attrs={'class': 'form-control','readonly':'readonly'}),
                              decimal_places=2, required=True,
                              disabled = False,
                              error_messages={'required': "Please Enter Amount Paid"})


   bank_list=[]
   try:
      banks = Banks.objects.all()
      for bank in banks:
         small_bank=(bank.id,bank.title)
         bank_list.append(small_bank)
   except:
      bank_list=[]

   banks = forms.ChoiceField(label="Banks", choices=bank_list,widget=forms.Select(attrs={"class":"form-control"}))
   account_name=forms.CharField(label="Account Name",max_length=255,widget=forms.TextInput(attrs={"class":"form-control",}),required=False)
   other_details=forms.CharField(label="Other Details",max_length=255,widget=forms.TextInput(attrs={"class":"form-control",}),required=False)

   bank_account_list=[]
   try:
      bank_accounts = CooperativeBankAccounts.objects.all()

      for bank_account in bank_accounts:
         small_bank_account=(bank_account.id,bank_account.account_name + '-' + bank_account.account_number + '-' + bank_account.bank.title )
         bank_account_list.append(small_bank_account)
   except:
      bank_account_list=[]
   coop_accounts = forms.ChoiceField(label="Coop Accounts", choices=bank_account_list,widget=forms.Select(attrs={"class":"form-control"}))

   receipt_no = forms.IntegerField(initial=0,label='receipt_no', label_suffix=" : ", min_value=0,  required=False,
                                 widget=forms.NumberInput(attrs={'class': 'form-control'}),
                                disabled = False, error_messages={'required': "Please Min Unit"})


class RentalProducts_add_Form(forms.Form):
   description =forms.CharField(label="Description",max_length=255,widget=forms.TextInput(attrs={"class":"form-control"}))

   category_list=[]
   try:
      categories = RentalMainCategories.objects.all()

      for category in categories:
         small_category=(category.id,category.description)
         category_list.append(small_category)
   except:
      category_list=[]
   category = forms.ChoiceField(label="Category", choices=category_list,widget=forms.Select(attrs={"class":"form-control"}))


class Rental_Price_Settings_Form(forms.Form):

   category_list=[]
   try:
      categories = RentalMainCategories.objects.all()

      for category in categories:
         small_category=(category.id,category.description)
         category_list.append(small_category)
   except:
      category_list=[]
   category = forms.ChoiceField(label="Category", choices=category_list,widget=forms.Select(attrs={"class":"form-control"}))

   product_list=[]
   try:
      products = RentalProducts.objects.all()

      for product in products:
         small_product=(product.id,product.description)
         product_list.append(small_product)
   except:
      product_list=[]
   product = forms.ChoiceField(label="sub Category", choices=product_list,widget=forms.Select(attrs={"class":"form-control"}))

   amount = forms.DecimalField(initial=0,label='Price Per a Day', label_suffix=" : ", min_value=0,  max_digits=20,
                              widget=forms.NumberInput(attrs={'class': 'form-control'}),
                              decimal_places=2, required=True,
                              disabled = False,
                              error_messages={'required': "Please Enter Amount Paid"})


class Rental_Services_Booking_Preview_Form(forms.Form):

   date = forms.DateField(label='Date', label_suffix=" : ",
                                required=True, disabled=False,
                                widget=DateInput(attrs={'class': 'form-control'}),
                                error_messages={'required': "This field is required."})

   start_time = forms.TimeField(label='Start Time', label_suffix=" : ",
                                required=True, disabled=False,
                                widget=TimePickerInput(attrs={'class': 'form-control'}),
                                error_messages={'required': "This field is required."})
   stop_time = forms.TimeField(label='Stop Time', label_suffix=" : ",
                                required=True, disabled=False,
                                widget=TimePickerInput(attrs={'class': 'form-control'}),
                                error_messages={'required': "This field is required."})


   amount = forms.DecimalField(initial=0,label='Price Per a Day', label_suffix=" : ", min_value=1,  max_digits=20,
                              widget=forms.NumberInput(attrs={'class': 'form-control','readonly':'readonly'}),
                              decimal_places=2, required=True,
                              disabled = False,
                              error_messages={'required': "Please Enter Amount Paid"})


class Rental_Services_Contact_Person_Register_Form(forms.Form):
   name=forms.CharField(label="Name",max_length=100,widget=forms.TextInput(attrs={"class":"form-control",}),required=True)
   address=forms.CharField(label="Address",max_length=255,widget=forms.TextInput(attrs={"class":"form-control",}),required=True)
   phone_no=forms.CharField(label="Phone Number",max_length=11,widget=forms.TextInput(attrs={"class":"form-control",}),required=True)

class trending_commodity_signatories_form(forms.Form):
   name=forms.CharField(label="Name",max_length=100,widget=forms.TextInput(attrs={"class":"form-control",}),required=True)
   designation=forms.CharField(label="Designation",max_length=255,widget=forms.TextInput(attrs={"class":"form-control",}),required=True)
   phone_no=forms.CharField(label="Phone Number",max_length=11,widget=forms.TextInput(attrs={"class":"form-control",}),required=True)


class Rental_Date_Time_Selector_Form(forms.Form):

   date = forms.DateField(label='Date', label_suffix=" : ",
                                required=True, disabled=False,
                                widget=DateInput(attrs={'class': 'form-control'}),
                                error_messages={'required': "This field is required."})

   start_time = forms.TimeField(label='Start Time', label_suffix=" : ",
                                required=True, disabled=False,
                                widget=TimePickerInput(attrs={'class': 'form-control'}),
                                error_messages={'required': "This field is required."})
   stop_time = forms.TimeField(label='Stop Time', label_suffix=" : ",
                                required=True, disabled=False,
                                widget=TimePickerInput(attrs={'class': 'form-control'}),
                                error_messages={'required': "This field is required."})


   amount = forms.DecimalField(initial=0,label='Price Per a Day', label_suffix=" : ", min_value=1,  max_digits=20,
                              widget=forms.NumberInput(attrs={'class': 'form-control','readonly':'readonly'}),
                              decimal_places=2, required=True,
                              disabled = False,
                              error_messages={'required': "Please Enter Amount Paid"})



class Rental_Services_Selection_Preview_Form(forms.Form):
   amount = forms.DecimalField(initial=0,label='Price Per a Day', label_suffix=" : ", min_value=1,  max_digits=20,
                              widget=forms.NumberInput(attrs={'class': 'form-control','readonly':'readonly'}),
                              decimal_places=2, required=True,
                              disabled = False,
                              error_messages={'required': "Please Enter Amount Paid"})

   discount = forms.DecimalField(initial=0,label='Discount', label_suffix=" : ", min_value=0,  max_digits=20,
                              widget=forms.NumberInput(attrs={'class': 'form-control'}),
                              decimal_places=2, required=True,
                              disabled = False,
                              error_messages={'required': "Please Enter Amount Paid"})


class Rental_Services_Selection_Preview_Final_Form(forms.Form):
   amount_due = forms.DecimalField(initial=0,label='amount_due', label_suffix=" : ", min_value=1,  max_digits=20,
                              widget=forms.NumberInput(attrs={'class': 'form-control','readonly':'readonly'}),
                              decimal_places=2, required=True,
                              disabled = False,
                              error_messages={'required': "Please Enter Amount Paid"})

   amount_paid = forms.DecimalField(initial=0,label='amount_paid', label_suffix=" : ", min_value=0,  max_digits=20,
                              widget=forms.NumberInput(attrs={'class': 'form-control'}),
                              decimal_places=2, required=True,
                              disabled = False,
                              error_messages={'required': "Please Enter Amount Paid"})

   receipt_no = forms.IntegerField(initial=0,label='receipt_no', label_suffix=" : ", min_value=0,  required=False,
                                 widget=forms.NumberInput(attrs={'class': 'form-control'}),
                                disabled = False, error_messages={'required': "Please Min Unit"})



class Uploading_Existing_Savings_Done_List_Select_Period_Form(forms.Form):
  transaction_range = forms.ChoiceField(label="Transaction Range", choices=TRANSACTION_RANGE,widget=forms.Select(attrs={"class":"form-control"}))
  tdate = forms.DateField(label='Transaction Date', label_suffix=" : ",
                                required=True, disabled=False,
                                widget=DateInput(attrs={'class': 'form-control'}),
                                error_messages={'required': "This field is required."})


class Upload_Commodity_Product_Loan_Products_Select_Form(forms.Form):
   product=forms.CharField(label="Designation",max_length=255,widget=forms.TextInput(attrs={"class":"form-control",'readonly':'readonly'}),required=True)
  
   amount = forms.DecimalField(initial=0,label='Loan Amount', label_suffix=" : ", min_value=0,  max_digits=20,
                              widget=forms.NumberInput(attrs={'class': 'form-control','readonly':'readonly'}),
                              decimal_places=2, required=True,
                              disabled = False,
                              error_messages={'required': "Please Enter Amount Paid"})

   quantity = forms.IntegerField(initial=0,label='Quantity', label_suffix=" : ", min_value=0,  required=False,
                                 widget=forms.NumberInput(attrs={'class': 'form-control'}),
                                disabled = False, error_messages={'required': "Please Min Unit"})



class Upload_Commodity_Product_Loan_Products_Select_Preview_Form(forms.Form):
   product_cost = forms.DecimalField(initial=0,label='Product Cost', label_suffix=" : ", min_value=0,  max_digits=20,
                              widget=forms.NumberInput(attrs={'class': 'form-control','readonly':'readonly'}),
                              decimal_places=2, required=True,
                              disabled = False,
                              error_messages={'required': "Please Enter Amount Paid"})
   loan_amount = forms.DecimalField(initial=0,label='Loan Amount', label_suffix=" : ", min_value=0,  max_digits=20,
                              widget=forms.NumberInput(attrs={'class': 'form-control','readonly':'readonly'}),
                              decimal_places=2, required=True,
                              disabled = False,
                              error_messages={'required': "Please Enter Amount Paid"})
   repayment = forms.DecimalField(initial=0,label='Repayment', label_suffix=" : ", min_value=0,  max_digits=20,
                              widget=forms.NumberInput(attrs={'class': 'form-control'}),
                              decimal_places=2, required=True,
                              disabled = False,
                              error_messages={'required': "Please Enter Amount Paid"})
   balance = forms.DecimalField(initial=0,label='Balance', label_suffix=" : ", min_value=0,  max_digits=20,
                              widget=forms.NumberInput(attrs={'class': 'form-control'}),
                              decimal_places=2, required=True,
                              disabled = False,
                              error_messages={'required': "Please Enter Amount Paid"})
   admin_charge = forms.DecimalField(initial=0,label='Admin Charge', label_suffix=" : ", min_value=0,  max_digits=20,
                              widget=forms.NumberInput(attrs={'class': 'form-control','readonly':'readonly'}),
                              decimal_places=2, required=True,
                              disabled = False,
                              error_messages={'required': "Please Enter Amount Paid"})

   duration = forms.IntegerField(initial=0,label='Duration', label_suffix=" : ", min_value=0,  required=False,
                                 widget=forms.NumberInput(attrs={'class': 'form-control'}),
                                disabled = False, error_messages={'required': "Please Min Unit"})
   start_date = forms.DateField(label='Start Date', label_suffix=" : ",
                                required=True, disabled=False,
                                widget=DateInput(attrs={'class': 'form-control'}),
                                error_messages={'required': "This field is required."})

   balance_date = forms.DateField(label='Balance Date', label_suffix=" : ",
                                required=True, disabled=False,
                                widget=DateInput(attrs={'class': 'form-control'}),
                                error_messages={'required': "This field is required."})


class Upload_Commodity_Product_Loan_Ledger_Posting_Form(forms.Form):
   loan_amount = forms.DecimalField(initial=0,label='Loan Amount', label_suffix=" : ", min_value=0,  max_digits=20,
                              widget=forms.NumberInput(attrs={'class': 'form-control','readonly':'readonly'}),
                              decimal_places=2, required=True,
                              disabled = False,
                              error_messages={'required': "Please Enter Amount Paid"})
   balance = forms.DecimalField(initial=0,label='Balance', label_suffix=" : ", min_value=0,  max_digits=20,
                              widget=forms.NumberInput(attrs={'class': 'form-control','readonly':'readonly'}),
                              decimal_places=2, required=True,
                              disabled = False,
                              error_messages={'required': "Please Enter Amount Paid"})
   balance_date = forms.DateField(label='Effective Date', label_suffix=" : ",
                                required=True, disabled=False,
                                widget=DateInput(attrs={'class': 'form-control'}),
                                error_messages={'required': "This field is required."})
   loan_number = forms.IntegerField(initial=0,label='Loan Number', label_suffix=" : ", min_value=0,  required=False,
                                 widget=forms.NumberInput(attrs={'class': 'form-control','readonly':'readonly'}),
                                disabled = False, error_messages={'required': "Please Min Unit"})
  

class Members_Ledger_Balance_Update_Savings_load_Form(forms.Form):
   exist_amount = forms.DecimalField(initial=0,label='Existing Amount', label_suffix=" : ", min_value=0,  max_digits=20,
                              widget=forms.NumberInput(attrs={'class': 'form-control','readonly':'readonly'}),
                              decimal_places=2, required=True,
                              disabled = False,
                              error_messages={'required': "Please Enter Amount Paid"})
   current_amount= forms.DecimalField(initial=0,label='Current Balance', label_suffix=" : ", min_value=0,  max_digits=20,
                              widget=forms.NumberInput(attrs={'class': 'form-control'}),
                              decimal_places=2, required=True,
                              disabled = False,
                              error_messages={'required': "Please Enter Amount Paid"})
   balance_date = forms.DateField(label='Effective Date', label_suffix=" : ",
                                required=True, disabled=False,
                                widget=DateInput(attrs={'class': 'form-control'}),
                                error_messages={'required': "This field is required."})
   account_number = forms.IntegerField(initial=0,label='Account Number', label_suffix=" : ", min_value=0,  required=False,
                                 widget=forms.NumberInput(attrs={'class': 'form-control','readonly':'readonly'}),
                                disabled = False, error_messages={'required': "Please Min Unit"})
  
   account_name=forms.CharField(label="Account Name",max_length=255,widget=forms.TextInput(attrs={"class":"form-control",'readonly':'readonly'}),required=True)
  
class Members_Ledger_Balance_Update_Loan_Account_Form(forms.Form):
   loan_amount = forms.DecimalField(initial=0,label='Existing Amount', label_suffix=" : ", min_value=0,  max_digits=20,
                              widget=forms.NumberInput(attrs={'class': 'form-control',}),
                              decimal_places=2, required=True,
                              disabled = False,
                              error_messages={'required': "Please Enter Amount Paid"})
   balance= forms.DecimalField(initial=0,label='Current Balance', label_suffix=" : ", min_value=0,  max_digits=20,
                              widget=forms.NumberInput(attrs={'class': 'form-control'}),
                              decimal_places=2, required=True,
                              disabled = False,
                              error_messages={'required': "Please Enter Amount Paid"})
   repayment= forms.DecimalField(initial=0,label='Current Balance', label_suffix=" : ", min_value=0,  max_digits=20,
                              widget=forms.NumberInput(attrs={'class': 'form-control'}),
                              decimal_places=2, required=True,
                              disabled = False,
                              error_messages={'required': "Please Enter Amount Paid"})
  

   balance_date = forms.DateField(label='Effective Date', label_suffix=" : ",
                                required=True, disabled=False,
                                widget=DateInput(attrs={'class': 'form-control'}),
                                error_messages={'required': "This field is required."})
   start_date = forms.DateField(label='Start Date', label_suffix=" : ",
                                required=True, disabled=False,
                                widget=DateInput(attrs={'class': 'form-control'}),
                                error_messages={'required': "This field is required."})
   duration = forms.IntegerField(initial=0,label='Duration', label_suffix=" : ", min_value=0,  required=False,
                                 widget=forms.NumberInput(attrs={'class': 'form-control'}),
                                disabled = False, error_messages={'required': "Please Min Unit"})
   loan_number = forms.IntegerField(initial=0,label='Loan Number', label_suffix=" : ", min_value=0,  required=False,
                                 widget=forms.NumberInput(attrs={'class': 'form-control','readonly':'readonly'}),
                                disabled = False, error_messages={'required': "Please Min Unit"})
  
   loan_type=forms.CharField(label="Account Name",max_length=255,widget=forms.TextInput(attrs={"class":"form-control",'readonly':'readonly'}),required=True)
  

class Manual_Ledger_Posting_Ledger_details_Form(forms.Form):
   balance_amount = forms.DecimalField(initial=0,label='Existing Amount', label_suffix=" : ", min_value=0,  max_digits=20,
                              widget=forms.NumberInput(attrs={'class': 'form-control','readonly':'readonly'}),
                              decimal_places=2, required=True,
                              disabled = False,
                              error_messages={'required': "Please Enter Amount Paid"})
   amount= forms.DecimalField(initial=0,label='Amount', label_suffix=" : ", min_value=0,  max_digits=20,
                              widget=forms.NumberInput(attrs={'class': 'form-control'}),
                              decimal_places=2, required=True,
                              disabled = False,
                              error_messages={'required': "Please Enter Amount Paid"})
   period = forms.DateField(label='Transaction Date', label_suffix=" : ",
                                required=True, disabled=False,
                                widget=DateInput(attrs={'class': 'form-control'}),
                                error_messages={'required': "This field is required."})
   
   last_transaction_period = forms.DateField(label='Last_Transaction Date', label_suffix=" : ",
                                required=True, disabled=False,
                                widget=DateInput(attrs={'class': 'form-control','readonly':'readonly'}),
                                error_messages={'required': "This field is required."})
   account_number = forms.IntegerField(initial=0,label='Account Number', label_suffix=" : ", min_value=0,  required=False,
                                 widget=forms.NumberInput(attrs={'class': 'form-control','readonly':'readonly'}),
                                disabled = False, error_messages={'required': "Please Min Unit"})
  
   transaction=forms.CharField(label="Transaction",max_length=255,widget=forms.TextInput(attrs={"class":"form-control",'readonly':'readonly'}),required=True)
 
   particulars= forms.CharField(widget=forms.Textarea(attrs={"rows":2, "cols":50}),required=True)
   
 

# CURRENT DATE

# class Rental_Products_List_Load_Form(forms.Form):

#    product_list=[]
#    try:
#       products = RentalPriceSettings.objects.all()
#       print(products)
#       for product in products:
#          small_product=(product.id,str(product.products.description) -  str(product.amount))
#          product_list.append(small_product)
#    except:
#       product_list=[]
#    product = forms.ChoiceField(label="Product", choices=product_list,widget=forms.Select(attrs={"class":"form-control"}))


# |mul:-1



# receipt_types_id=request.POST.get('receipt_types')
#       receipt_types=ReceiptTypes.objects.get(id=receipt_types_id)

#       if receipt_types.title=="MANUAL":
#          # return HttpResponse("MANUAL")
#          receipt_status=ReceiptStatus.objects.get(title='USED')
#          receipt_id=request.POST.get('receipt_no')


#          if Receipts_Shop.objects.filter(receipt=receipt_id,status=receipt_status).exists():
#             messages.error(request,"This Receipt is Already in Use")
#             return HttpResponseRedirect(reverse('members_credit_sales_approved_item_details',args=(ticket,)))

#          receipt_id=Receipts_Shop.objects.get(receipt=receipt_id)
#          receipt=receipt_id.receipt
#          receipt_id.status=receipt_status
#          receipt_id.save()

#       elif receipt_types.title=="AUTO":
#          # return HttpResponse("Auto")
#          receipt_id=AutoReceipt.objects.first()
#          receipt="AUT-" + str(receipt_id.receipt.zfill(5))
#          receipt_id.receipt=int(receipt_id.receipt)+1
#          receipt_id.save()


#       else:
#          # return HttpResponse("None")
#          messages.error(request,'Invalid Receipt Type Selection')
#          return HttpResponseRedirect(reverse('members_credit_sales_approved_item_details',args=(ticket,)))



   # ledger_balance=get_cooperative_shop_balance(record.member)


   #       particulars=str(transaction_period.transaction_period) + " Month's Deduction"
   #       debit=0
   #       credit=record.account_amount
   #       balance=float(ledger_balance) + float(record.account_amount)


   #       cooperative_shop_ledger_posting(transaction_status,record.member,particulars,debit,credit,balance,tdate,processed_by)
   #



    # CHOICES=(
    #     ('NO','NO'),
    #     ('YES','YES')
    #     )

    # sources= models.CharField(default='MAIN',choices=CHOICES,max_length=15)
