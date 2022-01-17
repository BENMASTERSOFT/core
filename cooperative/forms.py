from django import forms
from cooperative.models import *
from django.db.models import Q



class DateInput(forms.DateInput):
	input_type = "date"

class searchForm(forms.Form):
   title = forms.CharField(label="", widget=forms.TextInput(attrs={"class":"form-control mb-4 mr-sm-4 mb-sm-0", "placeholder":"Search",'autocomplete':'off'}),required=False)


class search_with_date_Form(forms.Form):
   title = forms.CharField(label="", widget=forms.TextInput(attrs={"class":"form-control mb-4 mr-sm-4 mb-sm-0", "placeholder":"Search",'autocomplete':'off'}),required=False)
   
   start_date = forms.DateField(label='Start Date', label_suffix=" : ",
                             required=True, disabled=False,
                             widget=DateInput(attrs={'class': 'form-control'}),
                             error_messages={'required': "This field is required."})
   stop_date = forms.DateField(label='Stop Date', label_suffix=" : ",
                             required=True, disabled=False,
                             widget=DateInput(attrs={'class': 'form-control'}),
                             error_messages={'required': "This field is required."})


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




class addUsersForm(forms.Form):
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
   

   user_type_list=[]
 
   try:
      user_types = UserType.objects.all()
      for user_type in user_types:
         small_user_type=(user_type.id,user_type.title)
         user_type_list.append(small_user_type)
   except:
      user_type_list=[]

   user_type=forms.ChoiceField(label="user_type",choices=user_type_list,widget=forms.Select(attrs={"class":"form-control"}))
	
 
   userlevel_list=[]
 
   try:
      userlevels = UsersLevel.objects.all()
      for userlevel in userlevels:
         small_userlevel=(userlevel.id,userlevel.title)
         userlevel_list.append(small_userlevel)
   except:
      userlevel_list=[]

   userlevel=forms.ChoiceField(label="User level",choices=userlevel_list,widget=forms.Select(attrs={"class":"form-control"}))
   
 


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
   
 
   userlevel_list=[]
 
   try:
      userlevels = UsersLevel.objects.all()
      for userlevel in userlevels:
         small_userlevel=(userlevel.id,userlevel.title)
         userlevel_list.append(small_userlevel)
   except:
      userlevel_list=[]

   userlevel=forms.ChoiceField(label="User level",choices=userlevel_list,widget=forms.Select(attrs={"class":"form-control"}))
   

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

class addNOKRelationshipsForm(forms.ModelForm):
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

      for instance in NOKRelationships.objects.all():
         if instance.title == title:
            raise forms.ValidationError(str(title) + ' is already created')
      return title


class addTransactionStatusForm(forms.ModelForm):
   class Meta:
      model = TransactionStatus
      fields=['title',]

      widgets = {
      'title': forms.TextInput(attrs={'class':'form-control','placeholder':"Enter Title"})
      }


   def clean_title(self):
      title = self.cleaned_data.get('title')
      if not title:
         raise forms.ValidationError('This field is required')

      for instance in TransactionStatus.objects.all():
         if instance.title == title:
            raise forms.ValidationError(str(title) + ' is already created')
      return title


class addProcessingStatusForm(forms.ModelForm):
   class Meta:
      model = ProcessingStatus
      fields=['title',]

      widgets = {
      'title': forms.TextInput(attrs={'class':'form-control','placeholder':"Enter Title"})
      }


   def clean_title(self):
      title = self.cleaned_data.get('title')
      if not title:
         raise forms.ValidationError('This field is required')

      for instance in ProcessingStatus.objects.all():
         if instance.title == title:
            raise forms.ValidationError(str(title) + ' is already created')
      return title



class addReceiptStatusForm(forms.ModelForm):
   class Meta:
      model = ReceiptStatus
      fields=['title',]

      widgets = {
      'title': forms.TextInput(attrs={'class':'form-control','placeholder':"Enter Title"})
      }


   def clean_title(self):
      title = self.cleaned_data.get('title')
      if not title:
         raise forms.ValidationError('This field is required')

      for instance in ReceiptStatus.objects.all():
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



# class addUserLevelsForm(forms.ModelForm):
#    class Meta:
#       model = UserLevels
#       fields=['title',]

#       widgets = {
#       'title': forms.TextInput(attrs={'class':'form-control','placeholder':"Enter Title"})
#       }


   def clean_title(self):
      title = self.cleaned_data.get('title')
      if not title:
         raise forms.ValidationError('This field is required')

      for instance in UserLevels.objects.all():
         if instance.title == title:
            raise forms.ValidationError(str(title) + ' is already created')
      return title


class addMembershipStatusForm(forms.ModelForm):
   try:
      class Meta:
         model = MembershipStatus
         fields=['title',]

         widgets = {
         'title': forms.TextInput(attrs={'class':'form-control','placeholder':"Enter Title"})
         }


      def clean_title(self):
         title = self.cleaned_data.get('title')
         if not title:
            raise forms.ValidationError('This field is required')

         for instance in MembershipStatus.objects.all():
            if instance.title == title:
               raise forms.ValidationError(str(title) + ' is already created')
         return title
   except:
      pass


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



class addInterestDeductionSourceForm(forms.ModelForm):
   class Meta:
      model = InterestDeductionSource
      fields=['title',]

      widgets = {
      'title': forms.TextInput(attrs={'class':'form-control','placeholder':"Enter Title"})
      }


   def clean_title(self):
      title = self.cleaned_data.get('title')
      if not title:
         raise forms.ValidationError('This field is required')

      for instance in InterestDeductionSource.objects.all():
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
   receipt_list=[]
   try:
      receipts = ReceiptTypes.objects.all()
      for receipt in receipts:
         small_receipt=(receipt.id,receipt.title)
         receipt_list.append(small_receipt)
   except:
      receipt_list=[]

   receipts = forms.ChoiceField(label="Receipts", choices=receipt_list,widget=forms.Select(attrs={"class":"form-control"}))

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
   

      
class addTransactionTypesForm(forms.Form):
   receipt_list=[]
   try:
      receipts = ReceiptTypes.objects.all()
      for receipt in receipts:
         small_receipt=(receipt.id,receipt.title)
         receipt_list.append(small_receipt)
   except:
      receipt_list=[]

   receipts = forms.ChoiceField(label="Receipts", choices=receipt_list,widget=forms.Select(attrs={"class":"form-control"}))

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




class loan_duration_update_form(forms.Form):
   duration=forms.CharField(label="Duration",max_length=50,widget=forms.TextInput(attrs={"class":"form-control"}))


class  default_admin_charges_update_form(forms.Form):
   default_admin_charges=forms.CharField(label="Default Admin Charges",max_length=50,widget=forms.TextInput(attrs={"class":"form-control"}))


class  MultipleLoanStatus_update_form(forms.Form):
  
   status_list=[]
   try:
      statuss=MultipleLoanStatus.objects.all()
      for status in statuss:
         small_status=(status.id,status.title)
         status_list.append(small_status)
   except:
      status_list=[]

   multiple_loan_status = forms.ChoiceField(label="Status", choices=status_list,widget=forms.Select(attrs={"class":"form-control"}))


class loan_savings_based_update_form(forms.Form):
   loan_savings_based=forms.CharField(label="Savings Ratio",max_length=50,widget=forms.TextInput(attrs={"class":"form-control"}))


class loan_name_update_form(forms.Form):
   name=forms.CharField(label="Name",max_length=50,widget=forms.TextInput(attrs={"class":"form-control"}))


class loan_interest_rate_update_form(forms.Form):
   interest_rate=forms.IntegerField(label='Enter Admin Charges', label_suffix=" : ", min_value=1,  required=False,
                                 widget=forms.NumberInput(attrs={'class': 'form-control'}),
                                help_text="This value is greater than or equal to 1 & less than or equal to 100.",
                                disabled = False, error_messages={'required': "Please Enter Admin Charges."})


class loan_interest_deduction_soucrces_Form(forms.Form):
  
   source_list=[]
   try:
      sources = InterestDeductionSource.objects.all()
      for source in sources:
         small_source=(source.id,source.title)
         source_list.append(small_source)
   except:
      source_list=[]

   source = forms.ChoiceField(label="sources", choices=source_list,widget=forms.Select(attrs={"class":"form-control"}))

class loan_category_update_form(forms.Form):
   category_list=[]
   try:
      categories = LoanCategory.objects.all()
      for category in categories:
         small_category=(category.id,category.title)
         category_list.append(small_category)
   except:
      category_list=[]

   category = forms.ChoiceField(label="Category", choices=category_list,widget=forms.Select(attrs={"class":"form-control"}))
   


 

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

class loan_admin_charges_rate_update_form(forms.Form):
   admin_charges_rating_list=[]
   try:
      admin_charges_ratings = AdminCharges.objects.all()
      for admin_charges_rating in admin_charges_ratings:
         small_admin_charges_rating=(admin_charges_rating.id,admin_charges_rating.title)
         admin_charges_rating_list.append(small_admin_charges_rating)
   except:
      admin_charges_rating_list=[]

   admin_charges_rating = forms.ChoiceField(label="Admin Charges Rating", choices=admin_charges_rating_list,widget=forms.Select(attrs={"class":"form-control"}))
  
  


class loan_admin_charges_update_form(forms.Form):
   admin_charges = forms.IntegerField(label='Enter Admin Charges', label_suffix=" : ", min_value=1,  required=False,
                                 widget=forms.NumberInput(attrs={'class': 'form-control'}),
                                help_text="This value is greater than or equal to 1 & less than or equal to 100.",
                                disabled = False, error_messages={'required': "Please Enter Admin Charges."})

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

class loan_loan_age_update_form(forms.Form):
   loan_age = forms.IntegerField(label='Enter Loan Age', label_suffix=" : ", min_value=1,  required=False,
                                 widget=forms.NumberInput(attrs={'class': 'form-control'}),
                                help_text="This value is greater than or equal to 1 & less than or equal to 100.",
                                disabled = False, error_messages={'required': "Please Enter Admin Charges."})


class ApprovableTransactions_form(forms.Form):
   transactions_list=[]
   try:
      transactions = TransactionTypes.objects.all()
      for transaction in transactions:
         small_transactions=(transaction.id,transaction.name)
         transactions_list.append(small_transactions)
   except:
      transactions_list=[]

   transaction = forms.ChoiceField(label="Transactions Types", choices=transactions_list,widget=forms.Select(attrs={"class":"form-control"}))
  

class ApprovableOfficers_form(forms.Form):
   officers_list=[]
   try:
      officers = CustomUser.objects.exclude(
                                          Q(user_type=1)|Q(user_type=6)|Q(user_type=9)|Q(user_type=10)
                                          )
      for officer in officers:
         small_officers=(officer.id,officer.username + '(' + officer.user_type +')')
         officers_list.append(small_officers)
   except:
      officers_list=[]

   officers = forms.ChoiceField(label="Officers", choices=officers_list,widget=forms.Select(attrs={"class":"form-control"}))
   
   transactions_list=[]
   try:
      transactions = ApprovableTransactions.objects.all()
      for transaction in transactions:
         small_transactions=(transaction.id,transaction.transaction.name)
         transactions_list.append(small_transactions)
   except:
      transactions_list=[]

   transaction = forms.ChoiceField(label="Transactions Types", choices=transactions_list,widget=forms.Select(attrs={"class":"form-control"}))
  


class CertifiableTransactions_form(forms.Form):
   transactions_list=[]
   try:
      transactionss = TransactionTypes.objects.all()
      for transactions in transactionss:
         small_transactions=(transactions.id,transactions.name)
         transactions_list.append(small_transactions)
   except:
      transactions_list=[]

   transaction = forms.ChoiceField(label="Transactions Types", choices=transactions_list,widget=forms.Select(attrs={"class":"form-control"}))
  
  

class DisbursementOfficers_form(forms.Form):
   officers_list=[]
   try:
      officers = CustomUser.objects.filter(user_type=4)
      for officer in officers:
         small_officers=(officer.id,officer.username)
         officers_list.append(small_officers)
   except:
      officers_list=[]

   officers = forms.ChoiceField(label="Officers", choices=officers_list,widget=forms.Select(attrs={"class":"form-control"}))
   
   

class CertificationOfficers_form(forms.Form):
   officers_list=[]
   try:
      officers = CustomUser.objects.exclude(
                                          Q(user_type=1)|Q(user_type=6)|Q(user_type=2)|Q(user_type=9)|Q(user_type=10)
                                          )
      for officer in officers:
         small_officers=(officer.id,officer.username)
         officers_list.append(small_officers)
   except:
      officers_list=[]

   officers = forms.ChoiceField(label="Officers", choices=officers_list,widget=forms.Select(attrs={"class":"form-control"}))
   
   transactions_list=[]
   try:
      transactions = CertifiableTransactions.objects.all()
      for transaction in transactions:
         small_transactions=(transaction.id,transaction.transaction.name)
         transactions_list.append(small_transactions)
   except:
      transactions_list=[]

   transaction = forms.ChoiceField(label="Transactions Types", choices=transactions_list,widget=forms.Select(attrs={"class":"form-control"}))
  

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
   comment= forms.CharField(widget=forms.Textarea(attrs={"rows":5, "cols":50}))


class MemberShipRequestAdditionalAttachment_form(forms.Form):
   caption=forms.CharField(label="Caption",max_length=150,widget=forms.TextInput(attrs={"class":"form-control"}))
   image=forms.FileField(label="Image", widget=forms.FileInput(attrs={"class":"form-control"}),required=False)


class MemberShipRequest_submit_form(forms.Form):  
   try:
      transaction=CertifiableTransactions.objects.get(transaction__code='100')  
      certification_officers_list=[]
  
      certification_officers = CertificationOfficers.objects.filter(transaction=transaction)  
                                
      for certification_officer in certification_officers:
         small_certification_officer=(certification_officer.id,certification_officer.officer.username)
         certification_officers_list.append(small_certification_officer)
   except:
      certification_officers_list=[]
   
   certification_officers = forms.ChoiceField(label="Certification Officers", choices=certification_officers_list,widget=forms.Select(attrs={"class":"form-control"}))


class MemberShipRequest_certification_submit_form(forms.Form):  
   approval_officers_list=[]
   try: 
      transaction=ApprovableTransactions.objects.get(transaction__code='100') 
      approval_officers = ApprovalOfficers.objects.filter(transaction=transaction)                          
      for approval_officer in approval_officers:
         small_approval_officer=(approval_officer.id,approval_officer.officer.username)
         approval_officers_list.append(small_approval_officer)
   except:
      approval_officers_list=[]
   
   approval_officers = forms.ChoiceField(label="Approval Officers", choices=approval_officers_list,widget=forms.Select(attrs={"class":"form-control"}))
   
   certication_status_list=[]
   try:
      certication_statuss = CertificationStatus.objects.all()  
                                
      for certication_status in certication_statuss:
         small_certication_status=(certication_status.id,certication_status.title)
         certication_status_list.append(small_certication_status)
   except:
      certication_status_list=[]

   certication_status = forms.ChoiceField(label="certication_status", choices=certication_status_list,widget=forms.Select(attrs={"class":"form-control"}))
   


class MemberShipRequest_approval_comment_form(forms.Form):  
   comment= forms.CharField(widget=forms.Textarea(attrs={"rows":2, "cols":50}))
 

class MemberShipRequest_approval_attachment_form(forms.Form):  
   caption=forms.CharField(label="Caption",max_length=150,widget=forms.TextInput(attrs={"class":"form-control"}),required=True)
   image=forms.FileField(label="Image", widget=forms.FileInput(attrs={"class":"form-control"}),required=True)


class MemberShipRequest_approval_submit_form(forms.Form):  
   approval_status_list=[]
   try:
      approval_statuss = ApprovalStatus.objects.all()  
                                
      for approval_status in approval_statuss:
         small_approval_status=(approval_status.id,approval_status.title)
         approval_status_list.append(small_approval_status)
   except:
      approval_status_list=[]

   approval_status = forms.ChoiceField(label="Approval Status", choices=approval_status_list,widget=forms.Select(attrs={"class":"form-control"}))

  


class membership_price_settings_form(forms.Form):
   admin_charges = forms.DecimalField(initial=0,label='Registration Fees', label_suffix=" : ", min_value=0,  max_digits=20,
                              widget=forms.NumberInput(attrs={'class': 'form-control'}),
                              decimal_places=2, required=False, 
                              disabled = False,
                              error_messages={'required': "Please Enter Admin Charges Minimum."})


class membership_form_sales_issue_form(forms.Form):
   unit_list=[]
   try:
      admin_charge = TransactionTypes.objects.get(code='100')
      max_unit=admin_charge.share_unit_max
      min_unit=admin_charge.share_unit_min

      units = SharesUnits.objects.filter(Q(unit__gte=int(min_unit)) & Q(unit__lte=max_unit))  
      # units = SharesUnits.objects.all()  
                                
      for unit in units:
         small_unit=(unit.id,unit.unit)
         unit_list.append(small_unit)
   except:
      unit_list=[]
 
   unit = forms.ChoiceField(label="Approval Status", choices=unit_list,widget=forms.Select(attrs={"class":"form-control"}))


   receipt = forms.IntegerField(label='Receipt', label_suffix=" : ", min_value=1, required=True,
                                 widget=forms.NumberInput(attrs={'class': 'form-control'}),
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
                              widget=forms.NumberInput(attrs={'class': 'form-control'}),
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
   

   account_list=[]
   try:
      accounts = CooperativeBankAccounts.objects.all()                  
      for account in accounts:
         small_account=(account.id,account.account_name + ' - ' + str(account.account_number) + ' - ' + str(account.bank))
         account_list.append(small_account)
   except:
      account_list=[]
   account = forms.ChoiceField(label="Account", choices=account_list,widget=forms.Select(attrs={"class":"form-control"}))


class CooperativeBankAccounts_form(forms.Form): 
   account_name = forms.CharField(label="Payment Reference",max_length=255,required=True,widget=forms.TextInput(attrs={"class":"form-control"}))
   account_number =  forms.CharField(label="Account Number",max_length=10,required=True,widget=forms.TextInput(attrs={"class":"form-control"}))
 
   bank_list=[]
   try:
      banks = Banks.objects.all()                  
      for bank in banks:
         small_bank=(bank.id,bank.title)
         bank_list.append(small_bank)
   except:
      bank_list=[]
   bank = forms.ChoiceField(label="Bank", choices=bank_list,widget=forms.Select(attrs={"class":"form-control"}))

   account_type_list=[]
   try:
      account_types = AccountTypes.objects.all()                  
      for account_type in account_types:
         small_account_type=(account_type.id,account_type.title)
         account_type_list.append(small_account_type)
   except:
      account_type_list=[]
   account_type = forms.ChoiceField(label="account_types", choices=account_type_list,widget=forms.Select(attrs={"class":"form-control"}))



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
   file_no=forms.CharField(label="File No",max_length=50,widget=forms.TextInput(attrs={"class":"form-control"}),required=True)
   ippis_no=forms.CharField(label="IPPIS No/Non IPPIS No",max_length=50,widget=forms.TextInput(attrs={"class":"form-control"}),required=True)
   date_joined = forms.DateField(label='Date Joined', label_suffix=" : ",
                             required=True, disabled=False,
                             widget=DateInput(attrs={'class': 'form-control'}),
                             error_messages={'required': "This field is required."})


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
   description=forms.CharField(label="Description",max_length=255,widget=forms.TextInput(attrs={"class":"form-control"}))
   image=forms.FileField(label="Image", widget=forms.FileInput(attrs={"class":"form-control"}),required=False)
   

class MembersBankAccounts_form(forms.Form):
   account_type_list=[]
   try:
      account_types = AccountTypes.objects.all()                  
      for account_type in account_types:
         small_account_type=(account_type.id,account_type.title)
         account_type_list.append(small_account_type)
   except:
      account_type_list=[]
   account_types = forms.ChoiceField(label="account_types", choices=account_type_list,widget=forms.Select(attrs={"class":"form-control"}))

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
      guarantors = Members.objects.all()                  
      for guarantor in guarantors:
         small_guarantor=(guarantor.id,guarantor.admin.first_name + " " + guarantor.admin.last_name + " " + guarantor.middle_name)
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
      transactions = TransactionTypes.objects.filter(~Q(source__title='GENERAL') & ~Q(code='600') )                  
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
   code=forms.CharField(label="Code",max_length=255,widget=forms.TextInput(attrs={"class":"form-control",'autocomplete':'off'}),disabled = True)
   item_name=forms.CharField(label="Item Name",max_length=255,widget=forms.TextInput(attrs={"class":"form-control"}),disabled = True)
   details=forms.CharField(label="Details",max_length=255,widget=forms.TextInput(attrs={"class":"form-control"}),disabled = True)
   available_quantity = forms.IntegerField(initial=0,label='Available Quantity', label_suffix=" : ", min_value=0,  required=True,
                              widget=forms.NumberInput(attrs={'class': 'form-control'}),
                             help_text="This value is greater than or equal to 0 & less than or equal to 100.",
                             disabled = True, error_messages={'required': "Please Enter quantity."})
   issue_quantity = forms.IntegerField(initial=0,label='Enter Issue Quantity', label_suffix=" : ", min_value=0, required=True,
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

   approval_officers_list=[]
   try: 
      transaction=ApprovableTransactions.objects.get(transaction__code='400') 
      approval_officers = ApprovalOfficers.objects.filter(transaction=transaction)                          
      for approval_officer in approval_officers:
         small_approval_officer=(approval_officer.id,approval_officer.officer.username)
         approval_officers_list.append(small_approval_officer)
   except:
      approval_officers_list=[]

   approval_officers = forms.ChoiceField(label="Approval Officers", choices=approval_officers_list,widget=forms.Select(attrs={"class":"form-control"}))


class approval_form(forms.Form):  
   comment= forms.CharField(widget=forms.Textarea(attrs={"rows":2, "cols":50}))

   approval_status_list=[]
   try:
      approval_statuss = ApprovalStatus.objects.all()                  
      for approval_status in approval_statuss:
         small_approval_status=(approval_status.id,approval_status.title)
         approval_status_list.append(small_approval_status)
   except:
      approval_status_list=[]
   
   approval_status = forms.ChoiceField(label="Approval Status", choices=approval_status_list,widget=forms.Select(attrs={"class":"form-control"}))
   

class Shop_Issue_Receipt_form(forms.Form):
   receipt_type_list=[]
   try:
      receipt_types = ReceiptTypes.objects.all()                  
      for receipt_type in receipt_types:
         small_receipt_type=(receipt_type.id,receipt_type.title)
         receipt_type_list.append(small_receipt_type)
   except:
      receipt_type_list=[]
   
   receipt_types = forms.ChoiceField(label="Receipt_ Types", choices=receipt_type_list,widget=forms.Select(attrs={"class":"form-control"}))

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
   

   channel_list=[]
   try:
      channels = SalesCategory.objects.exclude(title='CREDIT')                  
      for channel in channels:
         small_channel=(channel.id,channel.title)
         channel_list.append(small_channel)
   except:
      channel_list=[]
   
   channels = forms.ChoiceField(label="Payment Channels", choices=channel_list,widget=forms.Select(attrs={"class":"form-control"}))
   
   receipt_type_list=[]
   try:
      receipt_types = ReceiptTypes.objects.all()                  
      for receipt_type in receipt_types:
         small_receipt_type=(receipt_type.id,receipt_type.title)
         receipt_type_list.append(small_receipt_type)
   except:
      receipt_type_list=[]
   
   receipt_types = forms.ChoiceField(label="Receipt_ Types", choices=receipt_type_list,widget=forms.Select(attrs={"class":"form-control"}))
   
   receipt=forms.CharField(label="Receipt No",max_length=100,widget=forms.TextInput(attrs={"class":"form-control",'autocomplete':'off'}),required=False)
   name=forms.CharField(label="Name",max_length=100,widget=forms.TextInput(attrs={"class":"form-control"}))
   address=forms.CharField(label="Address",max_length=255,widget=forms.TextInput(attrs={"class":"form-control"}))
   phone_no=forms.CharField(label="Phone Number",max_length=11,required=False,widget=forms.TextInput(attrs={"class":"form-control"}))
   

class Shop_Cheque_Sales_Release_process_form(forms.Form):
   receipt_type_list=[]
   try:
      receipt_types = ReceiptTypes.objects.all()                  
      for receipt_type in receipt_types:
         small_receipt_type=(receipt_type.id,receipt_type.title)
         receipt_type_list.append(small_receipt_type)
   except:
      receipt_type_list=[]
   
   receipt_types = forms.ChoiceField(label="Receipt_ Types", choices=receipt_type_list,widget=forms.Select(attrs={"class":"form-control"}))
   
   receipt=forms.CharField(label="Receipt No",max_length=100,widget=forms.TextInput(attrs={"class":"form-control",'autocomplete':'off'}),required=False)
   


class Members_Salary_Update_Request_form(forms.Form):  
   description=forms.CharField(label="Description",max_length=100,widget=forms.TextInput(attrs={"class":"form-control"}),disabled = False)
  
   gross_pay = forms.DecimalField(initial=0,label='Gross Pay', label_suffix=" : ", min_value=0,  max_digits=20,
                              widget=forms.NumberInput(attrs={'class': 'form-control'}),
                              decimal_places=2, required=False, 
                              disabled = False,
                              error_messages={'required': "Please Enter Amount"})

   approval_officers_list=[]
   try: 
      transaction=ApprovableTransactions.objects.get(transaction__code='200') 
      approval_officers = ApprovalOfficers.objects.filter(transaction=transaction)                          
      for approval_officer in approval_officers:
         small_approval_officer=(approval_officer.id,approval_officer.officer.username)
         approval_officers_list.append(small_approval_officer)
   except:
      approval_officers_list=[]

   approval_officers = forms.ChoiceField(label="Approval Officers", choices=approval_officers_list,widget=forms.Select(attrs={"class":"form-control"}))


class members_salary_update_request_approval_form(forms.Form):  
   approval_status_list=[]
   try:
      approval_statuss = ApprovalStatus.objects.all()                  
      for approval_status in approval_statuss:
         small_approval_status=(approval_status.id,approval_status.title)
         approval_status_list.append(small_approval_status)
   except:
      approval_status_list=[]
   
   approval_status = forms.ChoiceField(label="Approval Status", choices=approval_status_list,widget=forms.Select(attrs={"class":"form-control"}))
   
   member_id=forms.CharField(label="Member ID",max_length=100,widget=forms.TextInput(attrs={"class":"form-control",'readonly':'readonly'}))
   name=forms.CharField(label="Name",max_length=100,widget=forms.TextInput(attrs={"class":"form-control",'readonly':'readonly'}))
   
   description=forms.CharField(label="Description",max_length=150,widget=forms.TextInput(attrs={"class":"form-control",'readonly':'readonly'}),disabled = False)
  
   prev_amount = forms.DecimalField(initial=0,label='Unit Selling Price', label_suffix=" : ", min_value=0,  max_digits=20,
                              widget=forms.NumberInput(attrs={'class': 'form-control','readonly':'readonly'}),
                              decimal_places=2, required=True, 
                              disabled = False,
                              error_messages={'required': "Please Enter Amount"})

   current_amount = forms.DecimalField(initial=0,label='Unit Selling Price', label_suffix=" : ", min_value=0,  max_digits=20,
                              widget=forms.NumberInput(attrs={'class': 'form-control','readonly':'readonly'}),
                              decimal_places=2, required=True, 
                              disabled = False,
                              error_messages={'required': "Please Enter Amount"})

   comment= forms.CharField(widget=forms.Textarea(attrs={"rows":2, "cols":50}))

   approval_date = forms.DateField(label='Approval Date', label_suffix=" : ",
                             required=True, disabled=False,
                             widget=DateInput(attrs={'class': 'form-control'}),
                             error_messages={'required': "This field is required."})


class loan_request_approved_list_form_sales_form(forms.Form):
   amount = forms.DecimalField(initial=0,label='Amount', label_suffix=" : ", min_value=0,  max_digits=20,
                              widget=forms.NumberInput(attrs={'class': 'form-control','readonly':'readonly'}),
                              decimal_places=2, required=True, 
                              disabled = False,
                              error_messages={'required': "Please Enter Amount"})
   receipt = forms.IntegerField(label='Enter Receipt No', label_suffix=" : ", min_value=0, required=True,
                              widget=forms.NumberInput(attrs={'class': 'form-control','autocomplete':'off'}),
                             help_text="This value is greater than or equal to 0 & less than or equal to 100.",
                             disabled = False, error_messages={'required': "Please Enter Receipt No."})

class loan_application_processing_form(forms.Form):
   loan_type=forms.CharField(label="Loan Type",max_length=100,widget=forms.TextInput(attrs={"class":"form-control",'readonly':'readonly'}))
   loan_amount = forms.DecimalField(initial=0,label='Loan Amount', label_suffix=" : ", min_value=0,  max_digits=20,
                              widget=forms.NumberInput(attrs={'class': 'form-control','readonly':'readonly'}),
                              decimal_places=2, required=True, 
                              disabled = False,
                              error_messages={'required': "Please Enter Amount"})
   loan_new_amount = forms.DecimalField(initial=0,label='Loan New Amount', label_suffix=" : ", min_value=0,  max_digits=20,
                              widget=forms.NumberInput(attrs={'class': 'form-control'}),
                              decimal_places=2, required=True, 
                              disabled = False,
                              error_messages={'required': "Please Enter Amount"})
  
class external_fascility_form(forms.Form):
   description=forms.CharField(label="Description",max_length=150,widget=forms.TextInput(attrs={"class":"form-control"}), required=True)
   image=forms.FileField(label="Image", widget=forms.FileInput(attrs={"class":"form-control"}),required=False)
   amount = forms.DecimalField(initial=0,label='Amount', label_suffix=" : ", min_value=0,  max_digits=20,
                              widget=forms.NumberInput(attrs={'class': 'form-control'}),
                              decimal_places=2, required=True, 
                              disabled = False,
                              error_messages={'required': "Please Enter Amount"})
   
   try: 
      status=MembershipStatus.objects.get(title='ACTIVE')
      approval_officers_list=[]
      transaction=ApprovableTransactions.objects.get(transaction__code='500') 
      approval_officers = ApprovalOfficers.objects.filter(transaction=transaction,status=status)                          
      for approval_officer in approval_officers:
         small_approval_officer=(approval_officer.id,approval_officer.officer.username)
         approval_officers_list.append(small_approval_officer)
   except:
      approval_officers_list=[]
   
   approval_officers = forms.ChoiceField(label="Approval Officers", choices=approval_officers_list,widget=forms.Select(attrs={"class":"form-control"}))


class ExternalFascilitiesTemp_form(forms.Form):  
   approval_status_list=[]
   try:
      approval_statuss = ApprovalStatus.objects.all()                  
      for approval_status in approval_statuss:
         small_approval_status=(approval_status.id,approval_status.title)
         approval_status_list.append(small_approval_status)
   except:
      approval_status_list=[]
   
   approval_status = forms.ChoiceField(label="Approval Status", choices=approval_status_list,widget=forms.Select(attrs={"class":"form-control"}))
   
   comment= forms.CharField(widget=forms.Textarea(attrs={"rows":2, "cols":50}))
   
   approval_date = forms.DateField(label='Approval Date', label_suffix=" : ",
                             required=True, disabled=False,
                             widget=DateInput(attrs={'class': 'form-control'}),
                             error_messages={'required': "This field is required."})


class members_exclusiveness_request_register_form(forms.Form):  
   transaction_list=[]
   try:
      transactions = TransactionTypes.objects.filter(Q(source__title='LOAN') | Q(source__title='SAVINGS'))                  
      for transaction in transactions:
         small_transaction=(transaction.id,transaction.name)
         transaction_list.append(small_transaction)
   except:
      transaction_list=[]
   transactions = forms.ChoiceField(label="Transactions", choices=transaction_list,widget=forms.Select(attrs={"class":"form-control"}))
  

   approval_officers_list=[]
   try: 
      transaction=ApprovableTransactions.objects.get(transaction__code='300') 
      approval_officers = ApprovalOfficers.objects.filter(transaction=transaction)                          
      for approval_officer in approval_officers:
         small_approval_officer=(approval_officer.id,approval_officer.officer.username)
         approval_officers_list.append(small_approval_officer)
   except:
      approval_officers_list=[]

   approval_officers = forms.ChoiceField(label="Approval Officers", choices=approval_officers_list,widget=forms.Select(attrs={"class":"form-control"}))


class members_exclusiveness_request_approval_process_form(forms.Form):
   approval_status_list=[]
   try:
      approval_statuss = ApprovalStatus.objects.all()                  
      for approval_status in approval_statuss:
         small_approval_status=(approval_status.id,approval_status.title)
         approval_status_list.append(small_approval_status)
   except:
      approval_status_list=[]
   
   approval_status = forms.ChoiceField(label="Approval Status", choices=approval_status_list,widget=forms.Select(attrs={"class":"form-control"}))
   
   comment= forms.CharField(widget=forms.Textarea(attrs={"rows":2, "cols":55}))
   
   


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
      transactions = TransactionTypes.objects.filter(source__title='LOAN')                  
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
   interest_rate = forms.DecimalField(initial=0,label='Schedule Amount', label_suffix=" : ", min_value=0,  max_digits=20,
                              widget=forms.NumberInput(attrs={'class': 'form-control'}),
                              decimal_places=2, required=False, 
                              disabled = False,
                              error_messages={'required': "Please Enter Amount"})
  
   duration = forms.IntegerField(initial=0,label='Duration', label_suffix=" : ", min_value=0, required=True,
                              widget=forms.NumberInput(attrs={'class': 'form-control','autocomplete':'off'}),
                             help_text="This value is greater than or equal to 0 & less than or equal to 100.",
                             disabled = False, error_messages={'required': "Please Enter Duration"})

   interest_deduction_list=[]
   try:
      interest_deductions = InterestDeductionSource.objects.all()                  
      for interest_deduction in interest_deductions:
         small_interest_deduction=(interest_deduction.id,interest_deduction.title)
         interest_deduction_list.append(small_interest_deduction)
   except:
      interest_deduction_list=[]
   interest_deductions = forms.ChoiceField(label="interest_deductions", choices=interest_deduction_list,widget=forms.Select(attrs={"class":"form-control"}))
   
   start_date = forms.DateField(label='Start Date', label_suffix=" : ",
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
   date_joined = forms.DateField(label='Date Joined', label_suffix=" : ",
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
   approval_officers_list=[]
   try: 
      transaction=ApprovableTransactions.objects.get(transaction__code='701') 
      approval_officers = ApprovalOfficers.objects.filter(transaction=transaction)                          
      for approval_officer in approval_officers:
         small_approval_officer=(approval_officer.id,approval_officer.officer.username)
         approval_officers_list.append(small_approval_officer)
   except:
      approval_officers_list=[]

   approval_officers = forms.ChoiceField(label="Approval Officers", choices=approval_officers_list,widget=forms.Select(attrs={"class":"form-control"}))


class Members_Share_Purchase_Request_form(forms.Form):
   units = forms.IntegerField(initial=0,label='Units', label_suffix=" : ", min_value=0,  required=True,
                                 widget=forms.NumberInput(attrs={'class': 'form-control'}),
                                help_text="This value is greater than or equal to 0 & less than or equal to 100.",
                                disabled = False, error_messages={'required': "Please Maximum Unit."})
  
   approval_officers_list=[]
   try: 
      transaction=ApprovableTransactions.objects.get(transaction__code='700') 
      approval_officers = ApprovalOfficers.objects.filter(transaction=transaction)                          
      for approval_officer in approval_officers:
         small_approval_officer=(approval_officer.id,approval_officer.officer.username)
         approval_officers_list.append(small_approval_officer)
   except:
      approval_officers_list=[]

   approval_officers = forms.ChoiceField(label="Approval Officers", choices=approval_officers_list,widget=forms.Select(attrs={"class":"form-control"}))


class Existing_Shares_Upload_form(forms.Form):
   shares_amount = forms.DecimalField(initial=0,label='Shares Amount', label_suffix=" : ", min_value=0,  max_digits=20,
                              widget=forms.NumberInput(attrs={'class': 'form-control'}),
                              decimal_places=2, required=True, 
                              disabled = False,
                              error_messages={'required': "Please Enter Amount"})
   unit_cost = forms.DecimalField(initial=0,label='Unit ', label_suffix=" : ", min_value=0,  max_digits=20,
                              widget=forms.NumberInput(attrs={'class': 'form-control'}),
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



class Cash_Withdrawal_form(forms.Form):
   approval_officers_list=[]
   try: 
      transaction=ApprovableTransactions.objects.get(transaction__code='900') 
      approval_officers = ApprovalOfficers.objects.filter(transaction=transaction)                          
      for approval_officer in approval_officers:
         small_approval_officer=(approval_officer.id,approval_officer.officer.username)
         approval_officers_list.append(small_approval_officer)
   except:
      approval_officers_list=[]

   approval_officers = forms.ChoiceField(label="Approval Officers", choices=approval_officers_list,widget=forms.Select(attrs={"class":"form-control"}))


   try:
      status=WithdrawalStatus.objects.get(title='UNLOCKED')
      transaction_list=[]
      transactions = WithdrawableTransactions.objects.filter(status=status)                 
      for transaction in transactions:
         small_transaction=(transaction.transaction_id,transaction.transaction.name)
         transaction_list.append(small_transaction)
   except:
      transaction_list=[]

   transactions = forms.ChoiceField(label="Transactions", choices=transaction_list,widget=forms.Select(attrs={"class":"form-control"}))

   amount = forms.DecimalField(initial=0,label='Amount', label_suffix=" : ", min_value=0,  max_digits=20,
                              widget=forms.NumberInput(attrs={'class': 'form-control'}),
                              decimal_places=2, required=True, 
                              disabled = False,
                              error_messages={'required': "Please Enter Amount"})
   narration= forms.CharField(widget=forms.Textarea(attrs={"rows":2, "cols":50}))
   account_number=forms.CharField(label="Account Number",max_length=50,widget=forms.TextInput(attrs={"class":"form-control",'readonly':'readonly'}))

   ledger_balance = forms.DecimalField(initial=0,label='Ledger Balance', label_suffix=" : ", min_value=0,  max_digits=20,
                              widget=forms.NumberInput(attrs={'class': 'form-control','readonly':'readonly'}),
                              decimal_places=2, required=True, 
                              disabled = False,
                              error_messages={'required': "Please Enter Amount"})



class WithdrawalController_form(forms.Form):
   transaction_list=[]
   try:
      transactions = TransactionTypes.objects.filter(source__title='SAVINGS')                 
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
   status_list=[]
   try:
      statuss = WithdrawalStatus.objects.all()         
          
      for status in statuss:
         small_status=(status.id,status.title)
         status_list.append(small_status)
   except:
      status_list=[]

   status = forms.ChoiceField(label="Title", choices=status_list,widget=forms.Select(attrs={"class":"form-control"}))

   maturity = forms.IntegerField(initial=0,label='Maturity', label_suffix=" : ", min_value=0, required=True,
                     widget=forms.NumberInput(attrs={'class': 'form-control','autocomplete':'off'}),
                             disabled = False, error_messages={'required': "Please Enter Maturity Months"})

class savings_cash_withdrawal_preview_form(forms.Form):
   comment= forms.CharField(widget=forms.Textarea(attrs={"rows":2, "cols":50}))

   status_list=[]
   try:
      statuss = ApprovalStatus.objects.all().order_by('title')         
          
      for status in statuss:
         small_status=(status.id,status.title)
         status_list.append(small_status)
   except:
      status_list=[]

   status = forms.ChoiceField(label="Title", choices=status_list,widget=forms.Select(attrs={"class":"form-control"}))
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
   try:
      transaction=CertifiableTransactions.objects.get(transaction__code='900')  
      certification_officers_list=[]
  
      certification_officers = CertificationOfficers.objects.filter(transaction=transaction)  
                                
      for certification_officer in certification_officers:
         small_certification_officer=(certification_officer.id,certification_officer.officer.username)
         certification_officers_list.append(small_certification_officer)
   except:
      certification_officers_list=[]
   
   certification_officers = forms.ChoiceField(label="Certification Officers", choices=certification_officers_list,widget=forms.Select(attrs={"class":"form-control"}))




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
   

   channel_list=[]
   try:
      channels = PaymentChannels.objects.all()                  
      for channel in channels:
         small_channel=(channel.id,channel.title)
         channel_list.append(small_channel)
   except:
      channel_list=[]
   
   channels = forms.ChoiceField(label="Payment Channels", choices=channel_list,widget=forms.Select(attrs={"class":"form-control"}))
  
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

   try:
      disbursement_officers_list=[]
      status=MembershipStatus.objects.get(title='ACTIVE')
      disbursement_officers = DisbursementOfficers.objects.filter(status=status)  
                                
      for disbursement_officer in disbursement_officers:
         small_disbursement_officer=(disbursement_officer.id,disbursement_officer.officer.username)
         disbursement_officers_list.append(small_disbursement_officer)
   except:
      disbursement_officers_list=[]
   
   officers = forms.ChoiceField(label="Disbursement Officers", choices=disbursement_officers_list,widget=forms.Select(attrs={"class":"form-control"}))




class Updating_Date_Joined__form(forms.Form):
   date_joined = forms.DateField(label='Date Joined', label_suffix=" : ",
                             required=True, disabled=False,
                             widget=DateInput(attrs={'class': 'form-control'}),
                             error_messages={'required': "This field is required."})

  
class loan_application_approved_process_preview__form(forms.Form):
   effective_date = forms.DateField(label='Effective Date', label_suffix=" : ",
                             required=True, disabled=False,
                             widget=DateInput(attrs={'class': 'form-control'}),
                             error_messages={'required': "This field is required."})

class DataCapture_Manager_form(forms.Form):
   status_list=[]
   try:
      statuss = MembershipStatus.objects.all()         
          
      for status in statuss:
         small_status=(status.id,status.title)
         status_list.append(small_status)
   except:
      status_list=[]

   status = forms.ChoiceField(label="Title", choices=status_list,widget=forms.Select(attrs={"class":"form-control"}))

class CustomerID_Manager_form(forms.Form):
   code = forms.IntegerField(initial=0,label='Customer ID', label_suffix=" : ", min_value=0, required=True,
                     widget=forms.NumberInput(attrs={'class': 'form-control','autocomplete':'off'}),
                             disabled = False, error_messages={'required': "Please Enter Customer ID"})


class Loan_Number_Manager_form(forms.Form):
   code = forms.IntegerField(initial=0,label='Loan Number', label_suffix=" : ", min_value=0, required=True,
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

   # source_list=[]
   # try:
   #    sources = TransactionSources.objects.filter(Q(title='SAVINGS'))         
          
   #    for source in sources:
   #       small_source=(source.id,source.title)
   #       source_list.append(small_source)
   # except:
   #    source_list=[]

   # source = forms.ChoiceField(label="Title", choices=source_list,widget=forms.Select(attrs={"class":"form-control"}))


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
   approval_officers_list=[]
   try: 
      transaction=ApprovableTransactions.objects.get(transaction__code='901') 
      approval_officers = ApprovalOfficers.objects.filter(transaction=transaction)                          
      for approval_officer in approval_officers:
         small_approval_officer=(approval_officer.id,approval_officer.officer.username)
         approval_officers_list.append(small_approval_officer)
   except:
      approval_officers_list=[]

   approval_officers = forms.ChoiceField(label="Approval Officers", choices=approval_officers_list,widget=forms.Select(attrs={"class":"form-control"}))



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
   
  
   approval_officers_list=[]
   try: 
      transaction=ApprovableTransactions.objects.get(transaction__code='901') 
      approval_officers = ApprovalOfficers.objects.filter(transaction=transaction)                          
      for approval_officer in approval_officers:
         small_approval_officer=(approval_officer.id,approval_officer.officer.username)
         approval_officers_list.append(small_approval_officer)
   except:
      approval_officers_list=[]

   approval_officers = forms.ChoiceField(label="Approval Officers", choices=approval_officers_list,widget=forms.Select(attrs={"class":"form-control"}))


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
   approval_status_list=[]
   try:
      approval_statuss = ApprovalStatus.objects.all()                  
      for approval_status in approval_statuss:
         small_approval_status=(approval_status.id,approval_status.title)
         approval_status_list.append(small_approval_status)
   except:
      approval_status_list=[]
   
   approval_status = forms.ChoiceField(label="Approval Status", choices=approval_status_list,widget=forms.Select(attrs={"class":"form-control"}))
   
   comment= forms.CharField(widget=forms.Textarea(attrs={"rows":2, "cols":55}))
   
   amount = forms.DecimalField(initial=0,label='Amount', label_suffix=" : ", min_value=0,  max_digits=20,
                              widget=forms.NumberInput(attrs={'class': 'form-control','readonly':'readonly'}),
                              decimal_places=2, required=True, 
                              disabled = False,
                              error_messages={'required': "Please Enter Amount Approved"})



class Shares_Purchase_Request_Approval_Processed_form(forms.Form):
   approval_status_list=[]
   try:
      approval_statuss = ApprovalStatus.objects.all()                  
      for approval_status in approval_statuss:
         small_approval_status=(approval_status.id,approval_status.title)
         approval_status_list.append(small_approval_status)
   except:
      approval_status_list=[]

   approval_status = forms.ChoiceField(label="Approval Status", choices=approval_status_list,widget=forms.Select(attrs={"class":"form-control"}))

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


class Purchase_Summary_form(forms.Form):
   start_date = forms.DateField(label='Start Date', label_suffix=" : ",
                             required=True, disabled=False,
                             widget=DateInput(attrs={'class': 'form-control'}),
                             error_messages={'required': "This field is required."})
   stop_date = forms.DateField(label='Stop Date', label_suffix=" : ",
                             required=True, disabled=False,
                             widget=DateInput(attrs={'class': 'form-control'}),
                             error_messages={'required': "This field is required."})
