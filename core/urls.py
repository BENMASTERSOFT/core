
from django.contrib import admin
from django.urls import path, include
from core import settings
from django.conf.urls.static import static
from cooperative import views
from cooperative import master_views,shop_views, deskofficer_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.ShowLoginPage,name='ShowLoginPage'),
    path('doLogin/', views.doLogin,name='doLogin'),
    
    path('logout_user', views.logout_user,name='logout_user'),
    path('GetUserDetails', views.GetUserDetails,name='GetUserDetails'),

    path('basic_form/', master_views.basic_form,name='basic_form'),
    path('basic_table/', master_views.basic_table,name='basic_table'),
    path('datatable_table/', master_views.datatable_table,name='datatable_table'),


    path('title_upload/',master_views.title_upload, name='title_upload'),
    path('states_upload/',master_views.states_upload, name='states_upload'),
    path('NOKRelationships_upload/',master_views.NOKRelationships_upload, name='NOKRelationships_upload'),
    path('lga_upload/',master_views.lga_upload, name='lga_upload'),
    path('MembershipStatus_upload/',master_views.MembershipStatus_upload, name='MembershipStatus_upload'),
    path('ProcessingStatus_upload/',master_views.ProcessingStatus_upload, name='ProcessingStatus_upload'),
    path('TransactionStatus_upload/',master_views.TransactionStatus_upload, name='TransactionStatus_upload'),
    path('ReceiptStatus_upload/',master_views.ReceiptStatus_upload, name='ReceiptStatus_upload'),
    path('Gender_upload/',master_views.Gender_upload, name='Gender_upload'),
    path('Banks_upload/',master_views.Banks_upload, name='Banks_upload'),
    path('Locations_upload/',master_views.Locations_upload, name='Locations_upload'),
    path('AccountTypes_upload/',master_views.AccountTypes_upload, name='AccountTypes_upload'),
    path('Departments_upload/',master_views.Departments_upload, name='Departments_upload'),
    path('SalaryInstitution_upload/',master_views.SalaryInstitution_upload, name='SalaryInstitution_upload'),
    path('InterestDeductionSource_upload/',master_views.InterestDeductionSource_upload, name='InterestDeductionSource_upload'),
    path('TransactionSources_upload/',master_views.TransactionSources_upload, name='TransactionSources_upload'),
    path('UserType_upload/',master_views.UserType_upload, name='UserType_upload'),
    path('AdminCharges_upload/',master_views.AdminCharges_upload, name='AdminCharges_upload'),
    path('CertificationStatus_upload/',master_views.CertificationStatus_upload, name='CertificationStatus_upload'),
    path('ApprovalStatus_upload/',master_views.ApprovalStatus_upload, name='ApprovalStatus_upload'),
    path('SubmissionStatus_upload/',master_views.SubmissionStatus_upload, name='SubmissionStatus_upload'),
    path('loan_criteria_base_upload/',master_views.loan_criteria_base_upload, name='loan_criteria_base_upload'),
    path('ProductCategory_upload/',master_views.ProductCategory_upload, name='ProductCategory_upload'),
    path('Stock_upload/',master_views.Stock_upload, name='Stock_upload'),
    path('SalesCategory_upload/',master_views.SalesCategory_upload, name='SalesCategory_upload'),
    path('TicketStatus_upload/',master_views.TicketStatus_upload, name='TicketStatus_upload'),
    path('PaymentChannels_upload/',master_views.PaymentChannels_upload, name='PaymentChannels_upload'),
    path('ReceiptTypes_upload/',master_views.ReceiptTypes_upload, name='ReceiptTypes_upload'),
    path('LockedStatus_upload/',master_views.LockedStatus_upload, name='LockedStatus_upload'),
    path('ExlusiveStatus_upload/',master_views.ExlusiveStatus_upload, name='ExlusiveStatus_upload'),
    path('LoanScheduleStatus_upload/',master_views.LoanScheduleStatus_upload, name='LoanScheduleStatus_upload'),
    path('LoansUploadStatus_upload/',master_views.LoansUploadStatus_upload, name='LoansUploadStatus_upload'),
    path('SavingsUploadStatus_upload/',master_views.SavingsUploadStatus_upload, name='SavingsUploadStatus_upload'),
    path('LoanCategory_upload/',master_views.LoanCategory_upload, name='LoanCategory_upload'),
    path('SharesUnits_upload/',master_views.SharesUnits_upload, name='SharesUnits_upload'),
    path('UsersLevel_upload/',master_views.UsersLevel_upload, name='UsersLevel_upload'),
    path('SharesUploadStatus_upload/',master_views.SharesUploadStatus_upload, name='SharesUploadStatus_upload'),
    path('WelfareUploadStatus_upload/',master_views.WelfareUploadStatus_upload, name='WelfareUploadStatus_upload'),
    path('DateJoinedUploadStatus_upload/',master_views.DateJoinedUploadStatus_upload, name='DateJoinedUploadStatus_upload'),
    path('Date_of_birth_status_upload/',master_views.Date_of_birth_status_upload, name='Date_of_birth_status_upload'),
    path('DateOfFirstAppointment_Status_upload/',master_views.DateOfFirstAppointment_Status_upload, name='DateOfFirstAppointment_Status_upload'),
    path('WithdrawalStatus_upload/',master_views.WithdrawalStatus_upload, name='WithdrawalStatus_upload'),
    path('MultipleLoanStatus_upload/',master_views.MultipleLoanStatus_upload, name='MultipleLoanStatus_upload'),
    path('LoanMergeStatus_upload/',master_views.LoanMergeStatus_upload, name='LoanMergeStatus_upload'),
    path('Product_Write_off_Reasons_upload/',master_views.Product_Write_off_Reasons_upload, name='Product_Write_off_Reasons_upload'),
    path('YesNo_upload/',master_views.YesNo_upload, name='YesNo_upload'),
    path('MonthlyDeductionGenerationHeaders_upload/',master_views.MonthlyDeductionGenerationHeaders_upload, name='MonthlyDeductionGenerationHeaders_upload'),
    path('Termination_Sources_upload/',master_views.Termination_Sources_upload, name='Termination_Sources_upload'),
   



    path('admin_home/', master_views.admin_home,name='admin_home'),
    
    
    path('User_Task_Manager_Update_Membership/<str:pk>/', master_views.User_Task_Manager_Update_Membership,name='User_Task_Manager_Update_Membership'),
    path('User_Task_Manager_Update_loan/<str:pk>/', master_views.User_Task_Manager_Update_loan,name='User_Task_Manager_Update_loan'),
    path('User_Task_Manager_Update_transaction_adjustment/<str:pk>/', master_views.User_Task_Manager_Update_transaction_adjustment,name='User_Task_Manager_Update_transaction_adjustment'),
    path('User_Task_Manager_Update_cash_withdrawal/<str:pk>/', master_views.User_Task_Manager_Update_cash_withdrawal,name='User_Task_Manager_Update_cash_withdrawal'),
    path('User_Task_Manager_Update_termination/<str:pk>/', master_views.User_Task_Manager_Update_termination,name='User_Task_Manager_Update_termination'),
    path('User_Task_Manager_Update_shares/<str:pk>/', master_views.User_Task_Manager_Update_shares,name='User_Task_Manager_Update_shares'),
    path('User_Task_Manager_Update_credit_sales/<str:pk>/', master_views.User_Task_Manager_Update_credit_sales,name='User_Task_Manager_Update_credit_sales'),
    path('User_Task_Manager_Update_stock_update/<str:pk>/', master_views.User_Task_Manager_Update_stock_update,name='User_Task_Manager_Update_stock_update'),
    path('User_Task_Manager_Update_exclusiveness/<str:pk>/', master_views.User_Task_Manager_Update_exclusiveness,name='User_Task_Manager_Update_exclusiveness'),
    path('User_Task_Manager_Update_system_admin/<str:pk>/', master_views.User_Task_Manager_Update_system_admin,name='User_Task_Manager_Update_system_admin'),
    path('User_Task_Manager_Update_desk_office/<str:pk>/', master_views.User_Task_Manager_Update_desk_office,name='User_Task_Manager_Update_desk_office'),
   
    path('General_Tasks_Manager/', master_views.General_Tasks_Manager,name='General_Tasks_Manager'),
    

    path('Executive_Users/', master_views.Executive_Users,name='Executive_Users'),
    path('Executive_Tasks/<str:pk>/', master_views.Executive_Tasks,name='Executive_Tasks'),

    path('Desk_Office_Users/', master_views.Desk_Office_Users,name='Desk_Office_Users'),
    path('Desk_Office_Tasks/<str:pk>/', master_views.Desk_Office_Tasks,name='Desk_Office_Tasks'),
    
    path('Shop_Users/', master_views.Shop_Users,name='Shop_Users'),
    path('Shop_Tasks/<str:pk>/', master_views.Shop_Tasks,name='Shop_Tasks'),
    
    path('system_reset/', master_views.system_reset,name='system_reset'),
    
    path('Invoice_Title/', master_views.Invoice_Title,name='Invoice_Title'),
    

    path('add_staff/', master_views.add_staff,name='add_staff'),
    path('add_staff_manage/', master_views.add_staff_manage,name='add_staff_manage'),
    path('add_staff_manage_view/<str:pk>/', master_views.add_staff_manage_view,name='add_staff_manage_view'),
    
    path('super_user_add/', master_views.super_user_add,name='super_user_add'),
    path('super_user_manage/', master_views.super_user_manage,name='super_user_manage'),
    path('super_user_manage_view/<str:pk>/', master_views.super_user_manage_view,name='super_user_manage_view'),
    
    path('addState/', master_views.addState,name='addState'),
    path('Manage_state/', master_views.Manage_state,name='Manage_state'),
    path('delete_state/<str:pk>/', master_views.delete_state,name='delete_state'),

    path('addNOKRelationships/', master_views.addNOKRelationships,name='addNOKRelationships'),
    path('Manage_NOKRelationships/', master_views.Manage_NOKRelationships,name='Manage_NOKRelationships'),
    path('Manage_NOKRelationships_Remove/<str:pk>/', master_views.Manage_NOKRelationships_Remove,name='Manage_NOKRelationships_Remove'),
    path('Manage_NOKRelationships_Max_No/', master_views.Manage_NOKRelationships_Max_No,name='Manage_NOKRelationships_Max_No'),
    

    path('addDefaultPassword/', master_views.addDefaultPassword,name='addDefaultPassword'),
    # path('addTransactionStatus/', master_views.addTransactionStatus,name='addTransactionStatus'),
    # path('addProcessingStatus/', master_views.addProcessingStatus,name='addProcessingStatus'),
    # path('addReceiptStatus/', master_views.addReceiptStatus,name='addReceiptStatus'),
    
    # path('addMembershipStatus/', master_views.addMembershipStatus,name='addMembershipStatus'),
    
    path('addGender/', master_views.addGender,name='addGender'),
    path('addTitles/', master_views.addTitles,name='addTitles'),
    
    
    path('addSalaryInstitution/', master_views.addSalaryInstitution,name='addSalaryInstitution'),
    path('addDepartments/', master_views.addDepartments,name='addDepartments'),
    path('addBanks/', master_views.addBanks,name='addBanks'),
    path('addLocations/', master_views.addLocations,name='addLocations'),

    path('addTransactionTypes/', master_views.addTransactionTypes,name='addTransactionTypes'),
    path('TransactionTypes_Manage_Load/', master_views.TransactionTypes_Manage_Load,name='TransactionTypes_Manage_Load'),
    path('TransactionTypes_Update/<str:pk>/', master_views.TransactionTypes_Update, name='TransactionTypes_Update'),
    path('FormAutoPrint_Settings/', master_views.FormAutoPrint_Settings,name='FormAutoPrint_Settings'),
    path('FormAutoPrint_SettingsUpdate/<str:pk>/', master_views.FormAutoPrint_SettingsUpdate, name='FormAutoPrint_SettingsUpdate'),

    path('MembersCompulsorySavings/', master_views.MembersCompulsorySavings,name='MembersCompulsorySavings'),
    path('MembersCompulsorySavings_delete/<str:pk>/', master_views.MembersCompulsorySavings_delete, name='MembersCompulsorySavings_delete'),
    
    path('SharesUnits_add/', master_views.SharesUnits_add,name='SharesUnits_add'),
    path('AddShares_Configurations/', master_views.AddShares_Configurations,name='AddShares_Configurations'),
    path('addWelfare_Configurations/', master_views.addWelfare_Configurations,name='addWelfare_Configurations'),

    path('Shares_Deduction_savings/', master_views.Shares_Deduction_savings,name='Shares_Deduction_savings'),
    path('Shares_Deduction_savings_remove/<str:pk>/', master_views.Shares_Deduction_savings_remove, name='Shares_Deduction_savings_remove'),
    
    path('CooperativeBankAccounts_add/', master_views.CooperativeBankAccounts_add,name='CooperativeBankAccounts_add'),
    path('CooperativeBankAccounts_Remove/<str:pk>/', master_views.CooperativeBankAccounts_Remove, name='CooperativeBankAccounts_Remove'),
    path('CooperativeBankAccounts_Update/<str:pk>/', master_views.CooperativeBankAccounts_Update, name='CooperativeBankAccounts_Update'),

  
    path('loan_category_settings/', master_views.loan_category_settings,name='loan_category_settings'),
    path('loan_settings_load/', master_views.loan_settings_load,name='loan_settings_load'),
    path('loan_settings_details_load/<str:pk>/', master_views.loan_settings_details_load,name='loan_settings_details_load'),
    
    path('loan_based_savings_update/', master_views.loan_based_savings_update,name='loan_based_savings_update'),
    path('loan_duration_update/<str:pk>/', master_views.loan_duration_update,name='loan_duration_update'),
    path('loan_category_update/<str:pk>/', master_views.loan_category_update,name='loan_category_update'),
    path('loan_guarantors_update/<str:pk>/', master_views.loan_guarantors_update,name='loan_guarantors_update'),
    path('loan_savings_based_update/<str:pk>/', master_views.loan_savings_based_update,name='loan_savings_based_update'),
    path('default_admin_charges_update/<str:pk>/', master_views.default_admin_charges_update,name='default_admin_charges_update'),
    path('MultipleLoanStatus_update/<str:pk>/', master_views.MultipleLoanStatus_update,name='MultipleLoanStatus_update'),
    path('loan_name_update/<str:pk>/', master_views.loan_name_update,name='loan_name_update'),
    path('loan_interest_rate_update/<str:pk>/', master_views.loan_interest_rate_update,name='loan_interest_rate_update'),
    path('loan_interest_deduction_soucrces_update/<str:pk>/', master_views.loan_interest_deduction_soucrces_update,name='loan_interest_deduction_soucrces_update'),
    path('loan_maximum_amount_update/<str:pk>/', master_views.loan_maximum_amount_update,name='loan_maximum_amount_update'),
    path('loan_rank_update_update/<str:pk>/', master_views.loan_rank_update_update,name='loan_rank_update_update'),
    path('loan_admin_charges_rate_update/<str:pk>/', master_views.loan_admin_charges_rate_update,name='loan_admin_charges_rate_update'),
    path('loan_admin_charges_update/<str:pk>/', master_views.loan_admin_charges_update,name='loan_admin_charges_update'),
    path('loan_admin_charges_minimum_update/<str:pk>/', master_views.loan_admin_charges_minimum_update,name='loan_admin_charges_minimum_update'),
    path('loan_salary_relationship_update/<str:pk>/', master_views.loan_salary_relationship_update,name='loan_salary_relationship_update'),
    path('loan_loan_age_update/<str:pk>/', master_views.loan_loan_age_update,name='loan_loan_age_update'),
    

    # path('Customized_loan_based_savings_update/', master_views.Customized_loan_based_savings_update,name='Customized_loan_based_savings_update'),
    path('Customized_loan_duration_update/<str:pk>/', master_views.Customized_loan_duration_update,name='Customized_loan_duration_update'),
    path('Customized_loan_category_update/<str:pk>/', master_views.Customized_loan_category_update,name='Customized_loan_category_update'),
    path('Customized_loan_guarantors_update/<str:pk>/', master_views.Customized_loan_guarantors_update,name='Customized_loan_guarantors_update'),
    # path('Customized_loan_savings_based_update/<str:pk>/', master_views.Customized_loan_savings_based_update,name='Customized_loan_savings_based_update'),
    # path('Customized_default_admin_charges_update/<str:pk>/', master_views.Customized_default_admin_charges_update,name='Customized_default_admin_charges_update'),
    # path('Customized_MultipleLoanStatus_update/<str:pk>/', master_views.Customized_MultipleLoanStatus_update,name='Customized_MultipleLoanStatus_update'),
    path('Customized_loan_name_update/<str:pk>/', master_views.Customized_loan_name_update,name='Customized_loan_name_update'),
    path('Customized_loan_interest_rate_update/<str:pk>/', master_views.Customized_loan_interest_rate_update,name='Customized_loan_interest_rate_update'),
    # path('Customized_loan_interest_deduction_soucrces_update/<str:pk>/', master_views.Customized_loan_interest_deduction_soucrces_update,name='Customized_loan_interest_deduction_soucrces_update'),
    # path('Customized_loan_maximum_amount_update/<str:pk>/', master_views.Customized_loan_maximum_amount_update,name='Customized_loan_maximum_amount_update'),
    path('Customized_loan_rank_update_update/<str:pk>/', master_views.Customized_loan_rank_update_update,name='Customized_loan_rank_update_update'),
    path('Customized_loan_admin_charges_rate_update/<str:pk>/', master_views.Customized_loan_admin_charges_rate_update,name='Customized_loan_admin_charges_rate_update'),
    path('Customized_loan_admin_charges_update/<str:pk>/', master_views.Customized_loan_admin_charges_update,name='Customized_loan_admin_charges_update'),
    # path('Customized_loan_admin_charges_minimum_update/<str:pk>/', master_views.Customized_loan_admin_charges_minimum_update,name='Customized_loan_admin_charges_minimum_update'),
    # path('Customized_loan_salary_relationship_update/<str:pk>/', master_views.Customized_loan_salary_relationship_update,name='Customized_loan_salary_relationship_update'),
    path('Customized_loan_loan_age_update/<str:pk>/', master_views.Customized_loan_loan_age_update,name='Customized_loan_loan_age_update'),
    path('Customized_loan_form_print_update/<str:pk>/', master_views.Customized_loan_form_print_update,name='Customized_loan_form_print_update'),
    path('Customized_receipt_type_update/<str:pk>/', master_views.Customized_receipt_type_update,name='Customized_receipt_type_update'),
   
    path('loan_settings_non_monetary_list_load/', master_views.loan_settings_non_monetary_list_load,name='loan_settings_non_monetary_list_load'),
    path('loan_settings_non_monetary_Categories_load/<str:pk>/', master_views.loan_settings_non_monetary_Categories_load,name='loan_settings_non_monetary_Categories_load'),
    

    # path('loan_settings_non_monetary_load/', master_views.loan_settings_non_monetary_load,name='loan_settings_non_monetary_load'),
    path('loan_settings_non_monetary_settings/<str:pk>/', master_views.loan_settings_non_monetary_settings,name='loan_settings_non_monetary_settings'),
    path('non_monetary_oan_guarantors_update/<str:pk>/', master_views.non_monetary_oan_guarantors_update,name='non_monetary_oan_guarantors_update'),
    path('Non_Monetary_MultipleLoanStatus_update/<str:pk>/', master_views.Non_Monetary_MultipleLoanStatus_update,name='Non_Monetary_MultipleLoanStatus_update'),
    path('non_monetary_loan_duration_update/<str:pk>/', master_views.non_monetary_loan_duration_update,name='non_monetary_loan_duration_update'),
    path('non_monetary_loan_name_update/<str:pk>/', master_views.non_monetary_loan_name_update,name='non_monetary_loan_name_update'),
    path('non_monetary_loan_interest_rate_update/<str:pk>/', master_views.non_monetary_loan_interest_rate_update,name='non_monetary_loan_interest_rate_update'),
    path('non_monetary_loan_admin_charges_rate_update/<str:pk>/', master_views.non_monetary_loan_admin_charges_rate_update,name='non_monetary_loan_admin_charges_rate_update'),
    path('non_monetary_loan_admin_charges_update/<str:pk>/', master_views.non_monetary_loan_admin_charges_update,name='non_monetary_loan_admin_charges_update'),
    path('non_monetary_loan_loan_age_update/<str:pk>/', master_views.non_monetary_loan_loan_age_update,name='non_monetary_loan_loan_age_update'),
    path('non_monetary_loan_receipt_type_update/<str:pk>/', master_views.non_monetary_loan_receipt_type_update,name='non_monetary_loan_receipt_type_update'),
    path('non_monetary_loan_form_print_update/<str:pk>/', master_views.non_monetary_loan_form_print_update,name='non_monetary_loan_form_print_update'),

    
    path('Commodity_Products_Add_Transactions_Load/', master_views.Commodity_Products_Add_Transactions_Load,name='Commodity_Products_Add_Transactions_Load'),
    path('Commodity_Products_Add_Transactions_Categories_Load/<str:pk>/', master_views.Commodity_Products_Add_Transactions_Categories_Load,name='Commodity_Products_Add_Transactions_Categories_Load'),

    # path('Commodity_Products_Categories/', master_views.Commodity_Products_Categories,name='Commodity_Products_Categories'),
    path('Commodity_Products_add/<str:pk>/', master_views.Commodity_Products_add,name='Commodity_Products_add'),
    path('Manage_Commodity_Categories_Delete/<str:pk>/', master_views.Manage_Commodity_Categories_Delete,name='Manage_Commodity_Categories_Delete'),
    
    path('Commodity_Transaction_Period/', master_views.Commodity_Transaction_Period,name='Commodity_Transaction_Period'),
    path('Commodity_Transaction_Period_Delete/<str:pk>/', master_views.Commodity_Transaction_Period_Delete,name='Commodity_Transaction_Period_Delete'),
    
    path('Commodity_Transaction_Period_Batch/', master_views.Commodity_Transaction_Period_Batch,name='Commodity_Transaction_Period_Batch'),
    path('Commodity_Transaction_Period_Batch_Delete/<str:pk>/', master_views.Commodity_Transaction_Period_Batch_Delete,name='Commodity_Transaction_Period_Batch_Delete'),

   
    path('addCommodityCategory/', master_views.addCommodityCategory,name='addCommodityCategory'),
    
    path('Manage_Commodity_Categories_Core_properties_Transactions_Load/', master_views.Manage_Commodity_Categories_Core_properties_Transactions_Load,name='Manage_Commodity_Categories_Core_properties_Transactions_Load'),
    path('Manage_Commodity_Categories_Core_Values/<str:pk>/', master_views.Manage_Commodity_Categories_Core_Values,name='Manage_Commodity_Categories_Core_Values'),
    
    path('Manage_Commodity_Categories_Peripherals_Transactions_Load/', master_views.Manage_Commodity_Categories_Peripherals_Transactions_Load,name='Manage_Commodity_Categories_Peripherals_Transactions_Load'),
    path('Manage_Commodity_Categories_Peripherals/<str:pk>/', master_views.Manage_Commodity_Categories_Peripherals,name='Manage_Commodity_Categories_Peripherals'),
    


    path('Customized_Commodity_Loan_Settings/', master_views.Customized_Commodity_Loan_Settings,name='Customized_Commodity_Loan_Settings'),

    path('membership_price_settings_load/', master_views.membership_price_settings_load,name='membership_price_settings_load'),
    path('AutoReceipt_Setup/', master_views.AutoReceipt_Setup,name='AutoReceipt_Setup'),
    path('receipt_manager/', master_views.receipt_manager,name='receipt_manager'),
    path('receipt_manager_shop/', master_views.receipt_manager_shop,name='receipt_manager_shop'),
    path('Members_IdManager/', master_views.Members_IdManager,name='Members_IdManager'),
    path('Loan_Number_Manager/', master_views.Loan_Number_Manager,name='Loan_Number_Manager'),

    path('check_email_exist/', master_views.check_email_exist,name='check_email_exist'),
    path('check_username_exist/', master_views.check_username_exist,name='check_username_exist'),
    path('check_phone_no_exist/', master_views.check_phone_no_exist,name='check_phone_no_exist'),

    path('WithdrawalController/', master_views.WithdrawalController,name='WithdrawalController'),
    path('WithdrawalController_add/', master_views.WithdrawalController_add,name='WithdrawalController_add'),
    path('WithdrawalController_View/<str:pk>/', master_views.WithdrawalController_View,name='WithdrawalController_View'),
    path('WithdrawalController_Process/<str:pk>/', master_views.WithdrawalController_Process,name='WithdrawalController_Process'),

   
    path('DataCapture_Manager/', master_views.DataCapture_Manager,name='DataCapture_Manager'),
   
    path('CustomerID_Manager/', master_views.CustomerID_Manager,name='CustomerID_Manager'),
    path('upload_stock_roll/', master_views.upload_stock_roll,name='upload_stock_roll'),
    path('upload_stock_roll/', master_views.upload_stock_roll,name='upload_stock_roll'),
    
    path('Manage_Commodity_Categories_Core_properties/<str:pk>/', master_views.Manage_Commodity_Categories_Core_properties,name='Manage_Commodity_Categories_Core_properties'),
    path('Manage_Commodity_Categories_Update/<str:pk>/', master_views.Manage_Commodity_Categories_Update,name='Manage_Commodity_Categories_Update'),
    
    path('Commodity_Products_Manage_Transactions_Load/', master_views.Commodity_Products_Manage_Transactions_Load,name='Commodity_Products_Manage_Transactions_Load'),
    path('Commodity_Products_Manage_Load/<str:pk>/', master_views.Commodity_Products_Manage_Load,name='Commodity_Products_Manage_Load'),
    path('Commodity_Products_Manage_Update/<str:pk>/', master_views.Commodity_Products_Manage_Update,name='Commodity_Products_Manage_Update'),
    path('Commodity_Products_Manage_Remove/<str:pk>/', master_views.Commodity_Products_Manage_Remove,name='Commodity_Products_Manage_Remove'),
   
    path('addCompanies/', master_views.addCompanies,name='addCompanies'),
    path('Manage_Companies/', master_views.Manage_Companies,name='Manage_Companies'),
    path('Manage_Companies_update/<str:pk>/', master_views.Manage_Companies_update,name='Manage_Companies_update'),
    path('Delete_Companies/<str:pk>/', master_views.Delete_Companies,name='Delete_Companies'),

    path('Product_Linking_Period_Load/', master_views.Product_Linking_Period_Load,name='Product_Linking_Period_Load'),
    path('Product_Linking_Company_Load/<str:period_obj>/<str:batch_obj>/<str:transaction_obj>/', master_views.Product_Linking_Company_Load,name='Product_Linking_Company_Load'),
    path('Product_Linking_Details/<str:pk>/<str:period_pk>/<str:batch_pk>/<str:transaction_pk>/', master_views.Product_Linking_Details,name='Product_Linking_Details'),
    path('Product_Linking_Details_Preview/<str:comp_pk>/<str:pk>/<str:period_pk>/<str:batch_pk>/<str:transaction_pk>/', master_views.Product_Linking_Details_Preview,name='Product_Linking_Details_Preview'),
    # path('Product_Linking_Details_Process/<str:comp_pk>/<str:pk>/', master_views.Product_Linking_Details_Process,name='Product_Linking_Details_Process'),
    path('Product_UnLinking_Process/<str:comp_pk>/<str:pk>/<str:period_pk>/<str:batch_pk>/<str:transaction_pk>/', master_views.Product_UnLinking_Process,name='Product_UnLinking_Process'),
    
    path('Product_Settings_Period_Load/', master_views.Product_Settings_Period_Load,name='Product_Settings_Period_Load'),
    path('Product_Price_Settings_Company_Load/<str:period_obj>/<str:batch_obj>/<str:transaction_obj>/', master_views.Product_Price_Settings_Company_Load,name='Product_Price_Settings_Company_Load'),
    path('Product_Price_Settings_details/<str:pk>/<str:period_obj>/<str:batch_obj>/<str:transaction_obj>/', master_views.Product_Price_Settings_details,name='Product_Price_Settings_details'),
    path('Product_Price_Settings_Update/<str:comp_pk>/<str:pk>//', master_views.Product_Price_Settings_Update,name='Product_Price_Settings_Update'),

    ###########################################
    ################## PRESIDENT################
    ############################################ 

    # path('president_home/', master_views.president_home,name='president_home'),
    path('membership_request_approvals_list_load/', master_views.membership_request_approvals_list_load,name='membership_request_approvals_list_load'),
    path('membership_request_approval_info/<str:pk>/', master_views.membership_request_approval_info,name='membership_request_approval_info'),
    
    path('membership_request_approval_comment_save/<str:pk>/', master_views.membership_request_approval_comment_save,name='membership_request_approval_comment_save'),
    path('membership_request_approval_info_delete/<str:pk>/', master_views.membership_request_approval_info_delete,name='membership_request_approval_info_delete'),
    
    path('membership_request_approval_attachment_save/<str:pk>/', master_views.membership_request_approval_attachment_save,name='membership_request_approval_attachment_save'),
    path('membership_request_approval_attachment_delete/<str:pk>/', master_views.membership_request_approval_attachment_delete,name='membership_request_approval_attachment_delete'),
    
    path('MemberShipRequest_approval_submit/<str:pk>/', master_views.MemberShipRequest_approval_submit,name='MemberShipRequest_approval_submit'),

    path('loan_request_approval_list_load/', master_views.loan_request_approval_list_load,name='loan_request_approval_list_load'),
    path('Loan_request_approval_details/<str:pk>/', master_views.Loan_request_approval_details,name='Loan_request_approval_details'),
    
    path('loan_application_approval_list_load/', master_views.loan_application_approval_list_load,name='loan_application_approval_list_load'),
    path('Loan_application_approval_details/<str:pk>/', master_views.Loan_application_approval_details,name='Loan_application_approval_details'),

    path('savings_cash_withdrawal_Certitication_list_load/', master_views.savings_cash_withdrawal_Certitication_list_load,name='savings_cash_withdrawal_Certitication_list_load'),
    

    path('savings_cash_withdrawal_list_load/', master_views.savings_cash_withdrawal_list_load,name='savings_cash_withdrawal_list_load'),
    path('savings_cash_withdrawal_preview/<str:pk>/', master_views.savings_cash_withdrawal_preview,name='savings_cash_withdrawal_preview'),

    path('members_exclusiveness_list_load/', master_views.members_exclusiveness_list_load,name='members_exclusiveness_list_load'),
    path('members_exclusiveness_process/<str:pk>/', master_views.members_exclusiveness_process,name='members_exclusiveness_process'),

    path('Shares_Purchase_Request_Approval_List_Load/', master_views.Shares_Purchase_Request_Approval_List_Load,name='Shares_Purchase_Request_Approval_List_Load'),
    path('Shares_Purchase_Request_Approval_Processed/<str:pk>/', master_views.Shares_Purchase_Request_Approval_Processed,name='Shares_Purchase_Request_Approval_Processed'),
    
    path('Cash_Withdrawal_Request_Approval_List_Load/', master_views.Cash_Withdrawal_Request_Approval_List_Load,name='Cash_Withdrawal_Request_Approval_List_Load'),

    ###############################################
    ############################ SECRETARY##########
    ################################################

  
    path('Loan_request_certification_list_load/', master_views.Loan_request_certification_list_load,name='Loan_request_certification_list_load'),
    path('Loan_request_certification_details/<str:pk>/', master_views.Loan_request_certification_details,name='Loan_request_certification_details'),
    
    path('Loan_application_certification_list_load/', master_views.Loan_application_certification_list_load,name='Loan_application_certification_list_load'),
    path('Loan_application_certification_details/<str:pk>/', master_views.Loan_application_certification_details,name='Loan_application_certification_details'),
    
    path('Non_Monetary_Loan_Request_certification_Load/', master_views.Non_Monetary_Loan_Request_certification_Load,name='Non_Monetary_Loan_Request_certification_Load'),
    path('Non_Monetary_Loan_Request_certification_Load_details/<str:pk>/', master_views.Non_Monetary_Loan_Request_certification_Load_details,name='Non_Monetary_Loan_Request_certification_Load_details'),
   

  ###########################################################################
    ############################ TREASURER   ######################################
    ###########################################################################
    # path('treasurer_home/', master_views.treasurer_home,name='treasurer_home'),
    path('withdrawal_confirmation_list_load/', master_views.withdrawal_confirmation_list_load,name='withdrawal_confirmation_list_load'),
    path('withdrawal_confirmation_details/<str:pk>/', master_views.withdrawal_confirmation_details,name='withdrawal_confirmation_details'),

   



    ###########################################################################
    ########################### #FIN SEC ######################################
    ###########################################################################
    # path('FINSEC_home/', finsec_views.FINSEC_home,name='FINSEC_home'),
    
    path('Cash_Withdrawal_Approved_list_load/', master_views.Cash_Withdrawal_Approved_list_load,name='Cash_Withdrawal_Approved_list_load'),
    path('Cash_Withdrawal_Approved_Details/<str:pk>/', master_views.Cash_Withdrawal_Approved_Details,name='Cash_Withdrawal_Approved_Details'),


    ################# MASTER ADMIN REPORT ##################################
    path('transaction_views_ranked/', master_views.transaction_views_ranked,name='transaction_views_ranked'),
    path('List_of_Users/', master_views.List_of_Users,name='List_of_Users'),

    ###########################################################################
    ########################## DESK OFFICER HOME ###############################
    ###########################################################################
    path('deskofficer_home/', deskofficer_views.deskofficer_home,name='deskofficer_home'),

    path('Useraccount_manager/', deskofficer_views.Useraccount_manager,name='Useraccount_manager'),
    
    path('desk_basic_form/', deskofficer_views.desk_basic_form,name='desk_basic_form'),
    path('desk_advanced_form/', deskofficer_views.desk_advanced_form,name='desk_advanced_form'),
    path('desk_basic_table/', deskofficer_views.desk_basic_table,name='desk_basic_table'),
    path('desk_datatable_table/', deskofficer_views.desk_datatable_table,name='desk_datatable_table'),
    
    path('membership_request/', deskofficer_views.membership_request,name='membership_request'),
    path('membership_request_complete_search/', deskofficer_views.membership_request_complete_search,name='membership_request_complete_search'),
    path('membership_request_complete_load/', deskofficer_views.membership_request_complete_load,name='membership_request_complete_load'),
    path('membership_request_additional_info/<str:pk>/', deskofficer_views.membership_request_additional_info,name='membership_request_additional_info'),
    path('membership_request_additional_info_update/<str:pk>/', deskofficer_views.membership_request_additional_info_update,name='membership_request_additional_info_update'),
   
    path('membership_request_additional_info_save/<str:pk>/', deskofficer_views.membership_request_additional_info_save,name='membership_request_additional_info_save'),
    path('membership_request_additional_info_delete_confirm/<str:pk>/<str:return_pk>/', deskofficer_views.membership_request_additional_info_delete_confirm,name='membership_request_additional_info_delete_confirm'),
    path('membership_request_additional_info_delete/<str:pk>/<str:return_pk>/', deskofficer_views.membership_request_additional_info_delete,name='membership_request_additional_info_delete'),

    path('MemberShipRequestAdditionalAttachment_save/<str:pk>/', deskofficer_views.MemberShipRequestAdditionalAttachment_save,name='MemberShipRequestAdditionalAttachment_save'),
    path('MemberShipRequest_Delete_confirmation/<str:pk>/', deskofficer_views.MemberShipRequest_Delete_confirmation,name='MemberShipRequest_Delete_confirmation'),
    path('MemberShipRequest_Delete/<str:pk>/', deskofficer_views.MemberShipRequest_Delete,name='MemberShipRequest_Delete'),
    path('MemberShipRequest_submit/<str:pk>/', deskofficer_views.MemberShipRequest_submit,name='MemberShipRequest_submit'),

    path('membership_request_manage_search/', deskofficer_views.membership_request_manage_search,name='membership_request_manage_search'),
    path('membership_request_manage_list_load/', deskofficer_views.membership_request_manage_list_load,name='membership_request_manage_list_load'),
    path('membership_request_manage_details/<str:pk>/', deskofficer_views.membership_request_manage_details,name='membership_request_manage_details'),
    path('membership_request_manage_details_edit_comment/<str:pk>/', deskofficer_views.membership_request_manage_details_edit_comment,name='membership_request_manage_details_edit_comment'),
    path('membership_request_manage_details_delete_comment/<str:pk>/', deskofficer_views.membership_request_manage_details_delete_comment,name='membership_request_manage_details_delete_comment'),
    path('membership_request_manage_details_add_comment/<str:pk>/', deskofficer_views.membership_request_manage_details_add_comment,name='membership_request_manage_details_add_comment'),
    
    path('membership_request_manage_details_edit_attachment/<str:pk>/', deskofficer_views.membership_request_manage_details_edit_attachment,name='membership_request_manage_details_edit_attachment'),
    path('membership_request_manage_details_edit_attachment_delete/<str:pk>/', deskofficer_views.membership_request_manage_details_edit_attachment_delete,name='membership_request_manage_details_edit_attachment_delete'),
    path('membership_request_manage_details_edit_attachment_add/<str:pk>/', deskofficer_views.membership_request_manage_details_edit_attachment_add,name='membership_request_manage_details_edit_attachment_add'),


    path('membership_request_delete_confirmation/<str:pk>/', deskofficer_views.membership_request_delete_confirmation,name='membership_request_delete_confirmation'),
    path('membership_request_delete/<str:pk>/', deskofficer_views.membership_request_delete,name='membership_request_delete'),
   

    path('membership_form_sales_list_load/', deskofficer_views.membership_form_sales_list_load,name='membership_form_sales_list_load'),
    path('membership_form_sales_preview/<str:pk>/', deskofficer_views.membership_form_sales_preview,name='membership_form_sales_preview'),
    path('membership_form_sales_issue/<str:pk>/', deskofficer_views.membership_form_sales_issue,name='membership_form_sales_issue'),

     
    path('membership_registration_applicant_search/', deskofficer_views.membership_registration_applicant_search,name='membership_registration_applicant_search'),
    path('membership_registration_applicant_list_load/', deskofficer_views.membership_registration_applicant_list_load,name='membership_registration_applicant_list_load'),
    
    # path('membership_registration_list_load/', deskofficer_views.membership_registration_list_load,name='membership_registration_list_load'),
    path('membership_registration_register/<str:pk>/', deskofficer_views.membership_registration_register,name='membership_registration_register'),
    
    path('Members_Account_Creation_Search/', deskofficer_views.Members_Account_Creation_Search,name='Members_Account_Creation_Search'),
    path('Members_Account_Creation_list_load/', deskofficer_views.Members_Account_Creation_list_load,name='Members_Account_Creation_list_load'),
    path('Members_Account_Creation_preview/<str:pk>/', deskofficer_views.Members_Account_Creation_preview,name='Members_Account_Creation_preview'),
    path('Members_Account_Creation_process/<str:pk>/', deskofficer_views.Members_Account_Creation_process,name='Members_Account_Creation_process'),
    
    path('Members_Multiple_Account_Creation_preview/', deskofficer_views.Members_Multiple_Account_Creation_preview,name='Members_Multiple_Account_Creation_preview'),
    path('Members_Multiple_Account_Creation_process/', deskofficer_views.Members_Multiple_Account_Creation_process,name='Members_Multiple_Account_Creation_process'),

    path('Members_account_details_list/<str:pk>/', deskofficer_views.Members_account_details_list,name='Members_account_details_list'),

    path('standing_order_selected_search/', deskofficer_views.standing_order_selected_search,name='standing_order_selected_search'),
    path('standing_order_selected_list_load/', deskofficer_views.standing_order_selected_list_load,name='standing_order_selected_list_load'),
    path('standing_order_selected_form/<str:pk>/', deskofficer_views.standing_order_selected_form,name='standing_order_selected_form'),
    
    path('standing_order_list_load/', deskofficer_views.standing_order_list_load,name='standing_order_list_load'),
    path('standing_order_form/<str:pk>/', deskofficer_views.standing_order_form,name='standing_order_form'),
    path('standing_order_locked/<str:pk>/', deskofficer_views.standing_order_locked,name='standing_order_locked'),
    path('standing_order_remove/<str:pk>/', deskofficer_views.standing_order_remove,name='standing_order_remove'),

    path('Transaction_adjustment_search/', deskofficer_views.Transaction_adjustment_search,name='Transaction_adjustment_search'),
    path('Transaction_adjustment_List_load/', deskofficer_views.Transaction_adjustment_List_load,name='Transaction_adjustment_List_load'),
    path('Transaction_adjustment_Transactions_load/<str:pk>/', deskofficer_views.Transaction_adjustment_Transactions_load,name='Transaction_adjustment_Transactions_load'),
    path('Transaction_adjustment_Transactions_Accounts_load/<str:pk>/<str:return_pk>/', deskofficer_views.Transaction_adjustment_Transactions_Accounts_load,name='Transaction_adjustment_Transactions_Accounts_load'),
    path('Transaction_adjustment_Transactions_Accounts_Remove/<str:pk>/', deskofficer_views.Transaction_adjustment_Transactions_Accounts_Remove,name='Transaction_adjustment_Transactions_Accounts_Remove'),
   
    path('Transaction_Adjustment_Approved_List_Load/', deskofficer_views.Transaction_Adjustment_Approved_List_Load,name='Transaction_Adjustment_Approved_List_Load'),
    path('Transaction_Adjustment_Approved_Processed/<str:pk>/', deskofficer_views.Transaction_Adjustment_Approved_Processed,name='Transaction_Adjustment_Approved_Processed'),

    path('Transaction_adjustment_Search/', deskofficer_views.Transaction_adjustment_Search,name='Transaction_adjustment_Search'),
    path('Transaction_adjustment_List_load/', deskofficer_views.Transaction_adjustment_List_load,name='Transaction_adjustment_List_load'),
    path('TransactionAjustmentHistory_details/<str:pk>/', deskofficer_views.TransactionAjustmentHistory_details,name='TransactionAjustmentHistory_details'),
    

    path('Transaction_Loan_adjustment_search/', deskofficer_views.Transaction_Loan_adjustment_search,name='Transaction_Loan_adjustment_search'),
    path('Transaction_Loan_adjustment_List_load/', deskofficer_views.Transaction_Loan_adjustment_List_load,name='Transaction_Loan_adjustment_List_load'),
    path('Transaction_Loan_adjustment_Transaction_load/<str:pk>/', deskofficer_views.Transaction_Loan_adjustment_Transaction_load,name='Transaction_Loan_adjustment_Transaction_load'),
    path('Transaction_Loan_adjustment_Transaction_Preview/<str:pk>/<str:loan_code>/', deskofficer_views.Transaction_Loan_adjustment_Transaction_Preview,name='Transaction_Loan_adjustment_Transaction_Preview'),
    path('Transaction_Loan_adjustment_Transaction_Process/<str:pk>/<str:loan_code>/', deskofficer_views.Transaction_Loan_adjustment_Transaction_Process,name='Transaction_Loan_adjustment_Transaction_Process'),
    path('Transaction_Loan_adjustment_Transaction_Cancel/<str:pk>/', deskofficer_views.Transaction_Loan_adjustment_Transaction_Cancel,name='Transaction_Loan_adjustment_Transaction_Cancel'),

    path('Transaction_Loan_adjustment_Transaction_Approved_List_Load/', deskofficer_views.Transaction_Loan_adjustment_Transaction_Approved_List_Load,name='Transaction_Loan_adjustment_Transaction_Approved_List_Load'),

    path('Transaction_Salary_adjustment_Request_search/', deskofficer_views.Transaction_Salary_adjustment_Request_search,name='Transaction_Salary_adjustment_Request_search'),
    path('Transaction_Salary_adjustment_Request_List_load/', deskofficer_views.Transaction_Salary_adjustment_Request_List_load,name='Transaction_Salary_adjustment_Request_List_load'),
    path('Transaction_Salary_adjustment_Request_Process/<str:pk>/', deskofficer_views.Transaction_Salary_adjustment_Request_Process,name='Transaction_Salary_adjustment_Request_Process'),
    path('Transaction_Salary_adjustment_Request_Manage_List_Load/', deskofficer_views.Transaction_Salary_adjustment_Request_Manage_List_Load,name='Transaction_Salary_adjustment_Request_Manage_List_Load'),
    path('Transaction_Salary_adjustment_Request_Manage_Preview/<str:pk>/', deskofficer_views.Transaction_Salary_adjustment_Request_Manage_Preview,name='Transaction_Salary_adjustment_Request_Manage_Preview'),
    
    path('Transaction_Salary_adjustment_Request_Manage_Process_List_Load/', deskofficer_views.Transaction_Salary_adjustment_Request_Manage_Process_List_Load,name='Transaction_Salary_adjustment_Request_Manage_Process_List_Load'),
    path('Transaction_Salary_adjustment_Request_Manage_Process/<str:pk>/', deskofficer_views.Transaction_Salary_adjustment_Request_Manage_Process,name='Transaction_Salary_adjustment_Request_Manage_Process'),
    

    path('Transaction_Salary_adjustment_Request_Approval_List_Load/', deskofficer_views.Transaction_Salary_adjustment_Request_Approval_List_Load,name='Transaction_Salary_adjustment_Request_Approval_List_Load'),
    path('Transaction_Salary_adjustment_Request_Approval_Process/<str:pk>/', deskofficer_views.Transaction_Salary_adjustment_Request_Approval_Process,name='Transaction_Salary_adjustment_Request_Approval_Process'),

    path('MembersBankAccounts_list_search/', deskofficer_views.MembersBankAccounts_list_search,name='MembersBankAccounts_list_search'),
    path('MembersBankAccounts_list_load/', deskofficer_views.MembersBankAccounts_list_load,name='MembersBankAccounts_list_load'),
    path('Members_Bank_Accounts/<str:pk>/', deskofficer_views.Members_Bank_Accounts,name='Members_Bank_Accounts'),
    path('Members_Bank_Accounts_remove/<str:pk>/', deskofficer_views.Members_Bank_Accounts_remove,name='Members_Bank_Accounts_remove'),
    path('Members_Bank_Accounts_lock/<str:pk>/', deskofficer_views.Members_Bank_Accounts_lock,name='Members_Bank_Accounts_lock'),
    
    path('Members_Bank_Accounts_edit_search/', deskofficer_views.Members_Bank_Accounts_edit_search,name='Members_Bank_Accounts_edit_search'),
    path('Members_Bank_Accounts_edit_list_load/', deskofficer_views.Members_Bank_Accounts_edit_list_load,name='Members_Bank_Accounts_edit_list_load'),
    path('Members_Bank_Accounts_edit_details_load/<str:pk>/', deskofficer_views.Members_Bank_Accounts_edit_details_load,name='Members_Bank_Accounts_edit_details_load'),
    path('Members_Bank_Accounts_update_form/<str:pk>/<str:return_pk>/', deskofficer_views.Members_Bank_Accounts_update_form,name='Members_Bank_Accounts_update_form'),
    path('Members_Bank_Accounts_delete/<str:pk>/<str:return_pk>/', deskofficer_views.Members_Bank_Accounts_delete,name='Members_Bank_Accounts_delete'),

    
    path('loan_request_search/', deskofficer_views.loan_request_search,name='loan_request_search'),
    path('loan_request_list_load/', deskofficer_views.loan_request_list_load,name='loan_request_list_load'),
    path('loan_request_order_delete/<str:pk>/<str:return_pk>/', deskofficer_views.loan_request_order_delete,name='loan_request_order_delete'),
    path('loan_request_order/<str:pk>/', deskofficer_views.loan_request_order,name='loan_request_order'),
    path('loan_request_criteria_Load/<str:pk>/', deskofficer_views.loan_request_criteria_Load,name='loan_request_criteria_Load'),
    
  
    path('LoanRequestAttachments_delete/<str:pk>/<str:return_pk>/', deskofficer_views.LoanRequestAttachments_delete,name='LoanRequestAttachments_delete'),
    # path('LoanExternalFascilities_delete/<str:pk>/<str:return_pk>/', deskofficer_views.LoanExternalFascilities_delete,name='LoanExternalFascilities_delete'),
    

    path('loan_request_preview/<str:pk>/', deskofficer_views.loan_request_preview,name='loan_request_preview'),

    path('loan_request_approved_list_load/', deskofficer_views.loan_request_approved_list_load,name='loan_request_approved_list_load'),
    path('loan_request_approved_list_form_sales/<str:pk>/', deskofficer_views.loan_request_approved_list_form_sales,name='loan_request_approved_list_form_sales'),
    
    path('loan_application_list_load/', deskofficer_views.loan_application_list_load,name='loan_application_list_load'),
    path('loan_application_processing/<str:pk>/', deskofficer_views.loan_application_processing,name='loan_application_processing'),
    path('loan_application_preview/<str:pk>/<str:return_pk>/', deskofficer_views.loan_application_preview,name='loan_application_preview'),

    path('loan_application_approved_list_load/', deskofficer_views.loan_application_approved_list_load,name='loan_application_approved_list_load'),
    path('loan_application_approved_process_preview/<str:pk>/', deskofficer_views.loan_application_approved_process_preview,name='loan_application_approved_process_preview'),
    
   
    path('members_exclusiveness_request_search/', deskofficer_views.members_exclusiveness_request_search,name='members_exclusiveness_request_search'),
    path('members_exclusiveness_request_list_load/', deskofficer_views.members_exclusiveness_request_list_load,name='members_exclusiveness_request_list_load'),
    path('members_exclusiveness_request_register/<str:pk>/', deskofficer_views.members_exclusiveness_request_register,name='members_exclusiveness_request_register'),
    path('members_exclusiveness_request_delete/<str:pk>/<str:return_pk>/', deskofficer_views.members_exclusiveness_request_delete,name='members_exclusiveness_request_delete'),

    path('members_exclusiveness_approved_list_load/', deskofficer_views.members_exclusiveness_approved_list_load,name='members_exclusiveness_approved_list_load'),
    path('members_exclusiveness_approved_processed/<str:pk>/', deskofficer_views.members_exclusiveness_approved_processed,name='members_exclusiveness_approved_processed'),


    path('Members_Next_Of_Kins_search/', deskofficer_views.Members_Next_Of_Kins_search,name='Members_Next_Of_Kins_search'),
    path('Members_Next_Of_Kins_list_load/', deskofficer_views.Members_Next_Of_Kins_list_load,name='Members_Next_Of_Kins_list_load'),
    path('addMembersNextOfKins/<str:pk>/', deskofficer_views.addMembersNextOfKins,name='addMembersNextOfKins'),
    path('MembersNextOfKins_remove/<str:pk>/', deskofficer_views.MembersNextOfKins_remove,name='MembersNextOfKins_remove'),
    path('MembersNextOfKins_lock/<str:pk>/', deskofficer_views.MembersNextOfKins_lock,name='MembersNextOfKins_lock'),

    path('Members_Next_Of_Kins_Manage_search/', deskofficer_views.Members_Next_Of_Kins_Manage_search,name='Members_Next_Of_Kins_Manage_search'),
    path('Members_Next_Of_Kins_Manage_list_load/', deskofficer_views.Members_Next_Of_Kins_Manage_list_load,name='Members_Next_Of_Kins_Manage_list_load'),
    path('Members_Next_Of_Kins_Manage_NOK_Load/<str:pk>/', deskofficer_views.Members_Next_Of_Kins_Manage_NOK_Load,name='Members_Next_Of_Kins_Manage_NOK_Load'),
    path('Members_Next_Of_Kins_Manage_NOK_Update/<str:pk>/<str:member_id>', deskofficer_views.Members_Next_Of_Kins_Manage_NOK_Update,name='Members_Next_Of_Kins_Manage_NOK_Update'),
    
    path('Members_Salary_Update_request_search/', deskofficer_views.Members_Salary_Update_request_search,name='Members_Salary_Update_request_search'),
    path('Members_Salary_Update_Request_list_load/', deskofficer_views.Members_Salary_Update_Request_list_load,name='Members_Salary_Update_Request_list_load'),
    path('Members_Salary_Update_Request_Load/<str:pk>/', deskofficer_views.Members_Salary_Update_Request_Load,name='Members_Salary_Update_Request_Load'),

    path('Members_Salary_Update_Request_approval_Load/', deskofficer_views.Members_Salary_Update_Request_approval_Load,name='Members_Salary_Update_Request_approval_Load'),
    path('Members_Salary_Update_Request_process/<str:pk>/', deskofficer_views.Members_Salary_Update_Request_process,name='Members_Salary_Update_Request_process'),

  
    path('TransactionPeriodManager/', deskofficer_views.TransactionPeriodManager,name='TransactionPeriodManager'),
    path('TransactionPeriodsUpdate/<str:pk>/', deskofficer_views.TransactionPeriodsUpdate,name='TransactionPeriodsUpdate'),

    path('Monthly_Deduction_Salary_Institution_Load/', deskofficer_views.Monthly_Deduction_Salary_Institution_Load,name='Monthly_Deduction_Salary_Institution_Load'),
    path('Monthly_Individual_Transactions_Load/<str:pk>/', deskofficer_views.Monthly_Individual_Transactions_Load,name='Monthly_Individual_Transactions_Load'),
    
    path('Monthly_Savings_Contribution_preview/<str:pk>/<str:salary_inst_key>/', deskofficer_views.Monthly_Savings_Contribution_preview,name='Monthly_Savings_Contribution_preview'),
    path('Monthly_Savings_Contribution_Generate/<str:pk>/<str:salary_inst_key>/', deskofficer_views.Monthly_Savings_Contribution_Generate,name='Monthly_Savings_Contribution_Generate'),

    path('Monthly_loan_repayement_preview/<str:pk>/<str:salary_inst_key>/', deskofficer_views.Monthly_loan_repayement_preview,name='Monthly_loan_repayement_preview'),
    path('Monthly_loan_repayement_Generate/<str:pk>/<str:salary_inst_key>/', deskofficer_views.Monthly_loan_repayement_Generate,name='Monthly_loan_repayement_Generate'),

    path('MonthlyDeductionGenerationHeader/<str:caption>/<str:salary_inst_key>/', deskofficer_views.MonthlyDeductionGenerationHeader,name='MonthlyDeductionGenerationHeader'),
    

    path('Monthly_Group_transaction_Institution_Load/', deskofficer_views.Monthly_Group_transaction_Institution_Load,name='Monthly_Group_transaction_Institution_Load'),
    path('Monthly_Group_Generated_Transaction/<str:pk>/', deskofficer_views.Monthly_Group_Generated_Transaction,name='Monthly_Group_Generated_Transaction'),
    path('Monthly_Group_Transaction_preview/<str:pk>/', deskofficer_views.Monthly_Group_Transaction_preview,name='Monthly_Group_Transaction_preview'),
    path('Monthly_Group_Transaction_generate/<str:pk>/', deskofficer_views.Monthly_Group_Transaction_generate,name='Monthly_Group_Transaction_generate'),
    path('Monthly_Group_Transaction_View/<str:pk>/', deskofficer_views.Monthly_Group_Transaction_View,name='Monthly_Group_Transaction_View'),

    path('Monthly_Deduction_excel_Export_Institution_Load/', deskofficer_views.Monthly_Deduction_excel_Export_Institution_Load,name='Monthly_Deduction_excel_Export_Institution_Load'),
    path('Monthly_Deduction_excel_Export_load/<str:pk>/', deskofficer_views.Monthly_Deduction_excel_Export_load,name='Monthly_Deduction_excel_Export_load'),
    
    path('export_users_xls/<str:pk>/', deskofficer_views.export_users_xls,name='export_users_xls'),
    path('export_norminal_roll_xls/', deskofficer_views.export_norminal_roll_xls,name='export_norminal_roll_xls'),
    

    path('Monthly_Account_deduction_Excel_import_Institution_Load/', deskofficer_views.Monthly_Account_deduction_Excel_import_Institution_Load,name='Monthly_Account_deduction_Excel_import_Institution_Load'),
    path('upload_AccountDeductionsResource/<str:pk>/', deskofficer_views.upload_AccountDeductionsResource,name='upload_AccountDeductionsResource'),

    path('Monthly_Account_deduction_Processing_Institution_Load/', deskofficer_views.Monthly_Account_deduction_Processing_Institution_Load,name='Monthly_Account_deduction_Processing_Institution_Load'),
    path('Monthly_Account_deduction_Processing_Preview/', deskofficer_views.Monthly_Account_deduction_Processing_Preview,name='Monthly_Account_deduction_Processing_Preview'),
    path('Monthly_Account_deduction_Process/<str:pk>/<str:trans_id>/', deskofficer_views.Monthly_Account_deduction_Process,name='Monthly_Account_deduction_Process'),
    
    path('Monthly_Account_deductions_Separations/', deskofficer_views.Monthly_Account_deductions_Separations,name='Monthly_Account_deductions_Separations'),

    

    path('monthly_wrongful_deduction_transaction_period_load/', deskofficer_views.monthly_wrongful_deduction_transaction_period_load,name='monthly_wrongful_deduction_transaction_period_load'),
    path('Monthly_Unbalanced_transactions/', deskofficer_views.Monthly_Unbalanced_transactions,name='Monthly_Unbalanced_transactions'),
    path('Monthly_Unbalanced_transactions_Processing/<str:pk>/', deskofficer_views.Monthly_Unbalanced_transactions_Processing,name='Monthly_Unbalanced_transactions_Processing'),
    path('Monthly_Unbalanced_transactions_Processing_Savings/<str:pk>/', deskofficer_views.Monthly_Unbalanced_transactions_Processing_Savings,name='Monthly_Unbalanced_transactions_Processing_Savings'),

    path('Monthly_deduction_ledger_posting_preview/', deskofficer_views.Monthly_deduction_ledger_posting_preview,name='Monthly_deduction_ledger_posting_preview'),
    
   
    path('upload_norminal_roll/', deskofficer_views.upload_norminal_roll,name='upload_norminal_roll'),
    path('Norminal_Roll_Preview/', deskofficer_views.Norminal_Roll_Preview,name='Norminal_Roll_Preview'),
    path('Norminal_Roll_Process/', deskofficer_views.Norminal_Roll_Process,name='Norminal_Roll_Process'),
    
    path('upload_distinct_norminal_roll/', deskofficer_views.upload_distinct_norminal_roll,name='upload_distinct_norminal_roll'),

    path('Uploading_Existing_Savings/', deskofficer_views.Uploading_Existing_Savings,name='Uploading_Existing_Savings'),
    path('Uploading_Existing_Savings_Preview/<str:pk>/', deskofficer_views.Uploading_Existing_Savings_Preview,name='Uploading_Existing_Savings_Preview'),
    path('Uploading_Existing_Savings_validate/<str:pk>/', deskofficer_views.Uploading_Existing_Savings_validate,name='Uploading_Existing_Savings_validate'),
    path('Uploading_Existing_Savings_delete/<str:pk>/<str:return_pk>/', deskofficer_views.Uploading_Existing_Savings_delete,name='Uploading_Existing_Savings_delete'),
   
   
    path('Cash_Deposit_Welfare_Search/', deskofficer_views.Cash_Deposit_Welfare_Search,name='Cash_Deposit_Welfare_Search'),
    path('Cash_Deposit_Welfare_list_load/', deskofficer_views.Cash_Deposit_Welfare_list_load,name='Cash_Deposit_Welfare_list_load'),
    path('Cash_Deposit_Welfare_Preview/<str:pk>/', deskofficer_views.Cash_Deposit_Welfare_Preview,name='Cash_Deposit_Welfare_Preview'),
    # path('Uploading_Existing_Savings_Verification_Processed/<str:pk>/', deskofficer_views.Uploading_Existing_Savings_Verification_Processed,name='Uploading_Existing_Savings_Verification_Processed'),
    # path('Uploading_Existing_Savings_Verification_Processed_Validate/<str:pk>/', deskofficer_views.Uploading_Existing_Savings_Verification_Processed_Validate,name='Uploading_Existing_Savings_Verification_Processed_Validate'),
    # path('Uploading_Existing_Savings_Verification_Update/<str:pk>/', deskofficer_views.Uploading_Existing_Savings_Verification_Update,name='Uploading_Existing_Savings_Verification_Update'),
   
    path('Uploading_Existing_Loans/', deskofficer_views.Uploading_Existing_Loans,name='Uploading_Existing_Loans'),
    path('Uploading_Existing_Loans_Preview/<str:pk>/', deskofficer_views.Uploading_Existing_Loans_Preview,name='Uploading_Existing_Loans_Preview'),
    path('Uploading_Existing_Loans_delete/<str:pk>/<str:return_pk>/', deskofficer_views.Uploading_Existing_Loans_delete,name='Uploading_Existing_Loans_delete'),
    path('Uploading_Existing_Loans_validate/<str:pk>/', deskofficer_views.Uploading_Existing_Loans_validate,name='Uploading_Existing_Loans_validate'),

    path('Uploading_Existing_Aditional_Loans/', deskofficer_views.Uploading_Existing_Aditional_Loans,name='Uploading_Existing_Aditional_Loans'),
    path('Uploading_Existing_Additional_Loans_Preview/<str:pk>/', deskofficer_views.Uploading_Existing_Additional_Loans_Preview,name='Uploading_Existing_Additional_Loans_Preview'),
    path('Uploading_Existing_Additional_Loans_validate/<str:pk>/', deskofficer_views.Uploading_Existing_Additional_Loans_validate,name='Uploading_Existing_Additional_Loans_validate'),
    path('Uploading_Existing_Additional_Loans_delete/<str:pk>/<str:return_pk>/', deskofficer_views.Uploading_Existing_Additional_Loans_delete,name='Uploading_Existing_Additional_Loans_delete'),
    
    path('Uploading_Existing_Savings_Additional_search/', deskofficer_views.Uploading_Existing_Savings_Additional_search,name='Uploading_Existing_Savings_Additional_search'),
    path('Uploading_Existing_Savings_Additional_list_load/', deskofficer_views.Uploading_Existing_Savings_Additional_list_load,name='Uploading_Existing_Savings_Additional_list_load'),
    path('Uploading_Existing_Savings_Additional_Preview/<str:pk>/', deskofficer_views.Uploading_Existing_Savings_Additional_Preview,name='Uploading_Existing_Savings_Additional_Preview'),
    path('Uploading_Existing_Savings_Additional_validate/<str:pk>/', deskofficer_views.Uploading_Existing_Savings_Additional_validate,name='Uploading_Existing_Savings_Additional_validate'),
    path('Uploading_Existing_Savings_Additional_delete/<str:pk>/<str:return_pk>/', deskofficer_views.Uploading_Existing_Savings_Additional_delete,name='Uploading_Existing_Savings_Additional_delete'),

    path('Members_Shares_Upload_list_load/', deskofficer_views.Members_Shares_Upload_list_load,name='Members_Shares_Upload_list_load'),
    path('Members_Shares_Upload_Preview/<str:pk>/', deskofficer_views.Members_Shares_Upload_Preview,name='Members_Shares_Upload_Preview'),

    # path('Members_Shares_Upload_Verification_list_load/', deskofficer_views.Members_Shares_Upload_Verification_list_load,name='Members_Shares_Upload_Verification_list_load'),
    # path('Members_Shares_Upload_verication_Preview/<str:pk>/', deskofficer_views.Members_Shares_Upload_verication_Preview,name='Members_Shares_Upload_verication_Preview'),
    
    path('Members_Welfare_Upload_list_load/', deskofficer_views.Members_Welfare_Upload_list_load,name='Members_Welfare_Upload_list_load'),
    path('Members_Welfare_Upload_Preview/<str:pk>/', deskofficer_views.Members_Welfare_Upload_Preview,name='Members_Welfare_Upload_Preview'),

    
 
    path('Norminal_Roll/', deskofficer_views.Norminal_Roll,name='Norminal_Roll'),
    path('Norminal_Roll_Update/<str:pk>/', deskofficer_views.Norminal_Roll_Update,name='Norminal_Roll_Update'),
    path('Member_delete/<str:pk>/', deskofficer_views.Member_delete,name='Member_delete'),
    

    
    path('Members_Share_Purchase_Request_Search/', deskofficer_views.Members_Share_Purchase_Request_Search,name='Members_Share_Purchase_Request_Search'),
    path('Members_Share_Purchase_Request_list_load/', deskofficer_views.Members_Share_Purchase_Request_list_load,name='Members_Share_Purchase_Request_list_load'),
    path('Members_Share_Purchase_Request_View/<str:pk>/', deskofficer_views.Members_Share_Purchase_Request_View,name='Members_Share_Purchase_Request_View'),

    path('Members_Share_Purchase_Request_Process/', deskofficer_views.Members_Share_Purchase_Request_Process,name='Members_Share_Purchase_Request_Process'),
    path('Members_Share_Purchase_Request_Process_View/<str:pk>/', deskofficer_views.Members_Share_Purchase_Request_Process_View,name='Members_Share_Purchase_Request_Process_View'),
    
    path('Members_Share_Purchase_Request_Manage_Search/', deskofficer_views.Members_Share_Purchase_Request_Manage_Search,name='Members_Share_Purchase_Request_Manage_Search'),
    path('Members_Share_Purchase_Request_Manage_list_load/', deskofficer_views.Members_Share_Purchase_Request_Manage_list_load,name='Members_Share_Purchase_Request_Manage_list_load'),
    path('Members_Share_Purchase_Request_Manage_Details/<str:pk>/', deskofficer_views.Members_Share_Purchase_Request_Manage_Details,name='Members_Share_Purchase_Request_Manage_Details'),
    path('Members_Share_Purchase_Request_Manage_Details_delete_Confirmation/<str:pk>/', deskofficer_views.Members_Share_Purchase_Request_Manage_Details_delete_Confirmation,name='Members_Share_Purchase_Request_Manage_Details_delete_Confirmation'),
    path('Members_Share_Purchase_Request_Manage_Details_delete/<str:pk>/', deskofficer_views.Members_Share_Purchase_Request_Manage_Details_delete,name='Members_Share_Purchase_Request_Manage_Details_delete'),

    

    path('Members_Initial_Shares_update_Search/', deskofficer_views.Members_Initial_Shares_update_Search,name='Members_Initial_Shares_update_Search'),
    path('Members_Initial_Shares_update_list_load/', deskofficer_views.Members_Initial_Shares_update_list_load,name='Members_Initial_Shares_update_list_load'),
    path('Members_Initial_Shares_update_preview/<str:pk>/', deskofficer_views.Members_Initial_Shares_update_preview,name='Members_Initial_Shares_update_preview'),
    
    path('Members_Initial_Shares_update_approved_list_load/', deskofficer_views.Members_Initial_Shares_update_approved_list_load,name='Members_Initial_Shares_update_approved_list_load'),
    path('Members_Initial_Shares_update_approved_processed/<str:pk>/', deskofficer_views.Members_Initial_Shares_update_approved_processed,name='Members_Initial_Shares_update_approved_processed'),

    path('PersonalLedger_Selected_Search/', deskofficer_views.PersonalLedger_Selected_Search,name='PersonalLedger_Selected_Search'),
    path('PersonalLedger_Selected_list_load/', deskofficer_views.PersonalLedger_Selected_list_load,name='PersonalLedger_Selected_list_load'),
    path('PersonalLedger_Transaction_Load/<str:pk>/', deskofficer_views.PersonalLedger_Transaction_Load,name='PersonalLedger_Transaction_Load'),
    path('PersonalLedger_Transaction_Account_Load/<str:pk>/<str:trans_id>/', deskofficer_views.PersonalLedger_Transaction_Account_Load,name='PersonalLedger_Transaction_Account_Load'),
    path('PersonalLedger_Display/<str:account_number>/<str:start_date>/<str:stop_date>/', deskofficer_views.PersonalLedger_Display,name='PersonalLedger_Display'),
    
    
    path('Cash_Deposit_Savings_Search/', deskofficer_views.Cash_Deposit_Savings_Search,name='Cash_Deposit_Savings_Search'),
    path('Cash_Deposit_Savings_list_load/', deskofficer_views.Cash_Deposit_Savings_list_load,name='Cash_Deposit_Savings_list_load'),
    path('Cash_Deposit_Savings_Load/<str:pk>/', deskofficer_views.Cash_Deposit_Savings_Load,name='Cash_Deposit_Savings_Load'),
    path('Cash_Deposit_Savings_Preview/<str:pk>/', deskofficer_views.Cash_Deposit_Savings_Preview,name='Cash_Deposit_Savings_Preview'),

    path('Cash_Deposit_Loans_Search/', deskofficer_views.Cash_Deposit_Loans_Search,name='Cash_Deposit_Loans_Search'),
    path('Cash_Deposit_Loan_list_load/', deskofficer_views.Cash_Deposit_Loan_list_load,name='Cash_Deposit_Loan_list_load'),
    path('Cash_Deposit_Loans_Preview/<str:pk>/', deskofficer_views.Cash_Deposit_Loans_Preview,name='Cash_Deposit_Loans_Preview'),

    path('Cash_Deposit_Shares_Search/', deskofficer_views.Cash_Deposit_Shares_Search,name='Cash_Deposit_Shares_Search'),
    path('Cash_Deposit_Shares_list_load/', deskofficer_views.Cash_Deposit_Shares_list_load,name='Cash_Deposit_Shares_list_load'),
    path('Cash_Deposit_Shares_Preview/<str:pk>/', deskofficer_views.Cash_Deposit_Shares_Preview,name='Cash_Deposit_Shares_Preview'),
    

    path('Cash_Withdrawal_Search/', deskofficer_views.Cash_Withdrawal_Search,name='Cash_Withdrawal_Search'),
    path('Cash_Withdrawal_list_load/', deskofficer_views.Cash_Withdrawal_list_load,name='Cash_Withdrawal_list_load'),
    path('Cash_Withdrawal_Transactions_load/<str:pk>/', deskofficer_views.Cash_Withdrawal_Transactions_load,name='Cash_Withdrawal_Transactions_load'),

    path('Cash_Withdrawal_Transactions_Approved_list_Search/', deskofficer_views.Cash_Withdrawal_Transactions_Approved_list_Search,name='Cash_Withdrawal_Transactions_Approved_list_Search'),
    path('Cash_Withdrawal_Transactions_Approved_list_Load/', deskofficer_views.Cash_Withdrawal_Transactions_Approved_list_Load,name='Cash_Withdrawal_Transactions_Approved_list_Load'),
  




    path('members_credit_purchase_approval/', deskofficer_views.members_credit_purchase_approval,name='members_credit_purchase_approval'),
    path('members_credit_purchase_approval_preview/<str:ticket>/', deskofficer_views.members_credit_purchase_approval_preview,name='members_credit_purchase_approval_preview'),

   
  
    path('members_exclusiveness_request_approval_list_load/', deskofficer_views.members_exclusiveness_request_approval_list_load,name='members_exclusiveness_request_approval_list_load'),
    path('members_exclusiveness_request_approval_process/<str:pk>/', deskofficer_views.members_exclusiveness_request_approval_process,name='members_exclusiveness_request_approval_process'),

    path('Shop_Cheque_Sales_List_Load/', deskofficer_views.Shop_Cheque_Sales_List_Load,name='Shop_Cheque_Sales_List_Load'),
    path('Shop_Cheque_Sales_process/<str:pk>/', deskofficer_views.Shop_Cheque_Sales_process,name='Shop_Cheque_Sales_process'),

    path('Initial_Shares_Update_List_Load/', deskofficer_views.Initial_Shares_Update_List_Load,name='Initial_Shares_Update_List_Load'),
    path('Initial_Shares_Update_preview/<str:pk>/', deskofficer_views.Initial_Shares_Update_preview,name='Initial_Shares_Update_preview'),
   
    path('Transaction_Adjustment_Approval_list_Load/', deskofficer_views.Transaction_Adjustment_Approval_list_Load,name='Transaction_Adjustment_Approval_list_Load'),
    path('Transaction_Adjustment_Approval_Process/<str:pk>/', deskofficer_views.Transaction_Adjustment_Approval_Process,name='Transaction_Adjustment_Approval_Process'),

    path('Transaction_Loan_Adjustment_Approval_list_Load/', deskofficer_views.Transaction_Loan_Adjustment_Approval_list_Load,name='Transaction_Loan_Adjustment_Approval_list_Load'),
    path('Transaction_Loan_Adjustment_Approval_list_Process/<str:pk>/', deskofficer_views.Transaction_Loan_Adjustment_Approval_list_Process,name='Transaction_Loan_Adjustment_Approval_list_Process'),
    
    path('membership_termination_search/', deskofficer_views.membership_termination_search,name='membership_termination_search'),
    path('membership_termination_transactions_load/<str:pk>/', deskofficer_views.membership_termination_transactions_load,name='membership_termination_transactions_load'),
    path('membership_termination_list_load/', deskofficer_views.membership_termination_list_load,name='membership_termination_list_load'),

    path('membership_commodity_loan_search/', deskofficer_views.membership_commodity_loan_search,name='membership_commodity_loan_search'),
    path('membership_commodity_loan_list_load/', deskofficer_views.membership_commodity_loan_list_load,name='membership_commodity_loan_list_load'),
    path('membership_commodity_loan_Period_Transactions_load/<str:pk>/', deskofficer_views.membership_commodity_loan_Period_Transactions_load,name='membership_commodity_loan_Period_Transactions_load'),
    path('membership_commodity_loan_Company_load/<str:pk>/<str:period_pk>/<str:batch_pk>/<str:transaction_pk>/', deskofficer_views.membership_commodity_loan_Company_load,name='membership_commodity_loan_Company_load'),
    

   
    path('membership_commodity_loan_Company_products/<str:return_pk>/<str:period_pk>/<str:batch_pk>/<str:transaction_pk>/<str:pk>/', deskofficer_views.membership_commodity_loan_Company_products,name='membership_commodity_loan_Company_products'),
    path('membership_commodity_loan_Company_products_details/<str:comp_pk>/<str:pk>/<str:member_pk>/<str:period_pk>/<str:batch_pk>/<str:transaction_pk>/', deskofficer_views.membership_commodity_loan_Company_products_details,name='membership_commodity_loan_Company_products_details'),
    path('membership_commodity_loan_Company_products_delete/<str:pk>/<str:mem_pk>/<str:period_pk>/<str:batch_pk>/<str:transaction_pk>/<str:comp_pk>/', deskofficer_views.membership_commodity_loan_Company_products_delete,name='membership_commodity_loan_Company_products_delete'),
    
    path('membership_commodity_loan_Company_products_proceed/<str:mem_pk>/<str:comp_pk>/<str:period_pk>/<str:batch_pk>/<str:transaction_pk>/', deskofficer_views.membership_commodity_loan_Company_products_proceed,name='membership_commodity_loan_Company_products_proceed'),
    path('membership_commodity_loan_Company_products_Criteria_Dashboard/<str:member_pk>/<str:period_pk>/<str:batch_pk>/<str:transaction_pk>/', deskofficer_views.membership_commodity_loan_Company_products_Criteria_Dashboard,name='membership_commodity_loan_Company_products_Criteria_Dashboard'),
    

    path('membership_commodity_loan_Company_products_net_pay_Settings/<str:member_pk>/<str:period_pk>/<str:batch_pk>/<str:transaction_pk>/', deskofficer_views.membership_commodity_loan_Company_products_net_pay_Settings,name='membership_commodity_loan_Company_products_net_pay_Settings'),
    path('membership_commodity_loan_Company_products_Guarantor_Settings/<str:member_pk>/<str:period_pk>/<str:batch_pk>/<str:transaction_pk>/', deskofficer_views.membership_commodity_loan_Company_products_Guarantor_Settings,name='membership_commodity_loan_Company_products_Guarantor_Settings'),

    path('membership_commodity_loan_manage/', deskofficer_views.membership_commodity_loan_manage,name='membership_commodity_loan_manage'),
    # path('membership_commodity_loan_manage_delete_Confirmation/<str:pk>/', deskofficer_views.membership_commodity_loan_manage_delete_Confirmation,name='membership_commodity_loan_manage_delete_Confirmation'),
    path('membership_commodity_loan_manage_delete/<str:pk>/', deskofficer_views.membership_commodity_loan_manage_delete,name='membership_commodity_loan_manage_delete'),
    path('membership_commodity_loan_manage_details/<str:pk>/', deskofficer_views.membership_commodity_loan_manage_details,name='membership_commodity_loan_manage_details'),
    path('membership_commodity_loan_manage_details_reset_Confirmation/<str:pk>/', deskofficer_views.membership_commodity_loan_manage_details_reset_Confirmation,name='membership_commodity_loan_manage_details_reset_Confirmation'),
    path('membership_commodity_loan_manage_details_delete/<str:pk>/', deskofficer_views.membership_commodity_loan_manage_details_delete,name='membership_commodity_loan_manage_details_delete'),
    path('membership_commodity_loan_manage_details_edit/<str:pk>/', deskofficer_views.membership_commodity_loan_manage_details_edit,name='membership_commodity_loan_manage_details_edit'),
    
    path('membership_commodity_loan_form_sales/', deskofficer_views.membership_commodity_loan_form_sales,name='membership_commodity_loan_form_sales'),

  
    path('Company_add/<str:pk>/', deskofficer_views.Company_add,name='Company_add'),


    ################################################################################
    #################################### DAY END TRANSACTIONS ####################################
    ################################################################################
    path('MemberShipFormSalesSummary/', deskofficer_views.MemberShipFormSalesSummary,name='MemberShipFormSalesSummary'),
    path('MemberShip_Form_Sales_Summary_Details/<str:pk>/', deskofficer_views.MemberShip_Form_Sales_Summary_Details,name='MemberShip_Form_Sales_Summary_Details'),
    

    ################################################################################
    #################################### REPORTS ####################################
    ################################################################################

    path('Members_General_Search/', deskofficer_views.Members_General_Search,name='Members_General_Search'),
    

    path('Cash_Deposit_Report_Date_Load/', deskofficer_views.Cash_Deposit_Report_Date_Load,name='Cash_Deposit_Report_Date_Load'),
    path('Load_Active_loans/', deskofficer_views.Load_Active_loans,name='Load_Active_loans'),

    path('Norminal_Roll_List_Load/', deskofficer_views.Norminal_Roll_List_Load,name='Norminal_Roll_List_Load'),
    path('Norminal_Roll_Personel_Detail/<str:pk>/', deskofficer_views.Norminal_Roll_Personel_Detail,name='Norminal_Roll_Personel_Detail'),
    
    path('MemberShipFormSalesReport/', deskofficer_views.MemberShipFormSalesReport,name='MemberShipFormSalesReport'),

    path('Over_Deductions_report/', deskofficer_views.Over_Deductions_report,name='Over_Deductions_report'),


    path('check_receipt_no_already_used/', deskofficer_views.check_receipt_no_already_used,name='check_receipt_no_already_used'),
    path('check_membership_phone_no_exist/', deskofficer_views.check_membership_phone_no_exist,name='check_membership_phone_no_exist'),
   


    ###########################################################################
    ############################ SHOP ######################################
    ###########################################################################
    path('shop_home/', shop_views.shop_home,name='shop_home'),
    path('advance_form/', shop_views.advance_form,name='advance_form'),
    path('editable_invoice/', shop_views.editable_invoice,name='editable_invoice'),
    

    
    path('members_cash_sales_search/', shop_views.members_cash_sales_search,name='members_cash_sales_search'),
    path('members_cash_sales_list_load/', shop_views.members_cash_sales_list_load,name='members_cash_sales_list_load'),
    

    path('members_cash_sales_product_load/<str:pk>/', shop_views.members_cash_sales_product_load,name='members_cash_sales_product_load'),
    path('members_cash_sales_item_issue/<str:pk>/<str:member_id>/', shop_views.members_cash_sales_item_issue,name='members_cash_sales_item_issue'),
    path('members_cash_sales_item_delete/<str:pk>/', shop_views.members_cash_sales_item_delete,name='members_cash_sales_item_delete'),
    # path('members_cash_sales_receipt/<str:pk>/', shop_views.members_cash_sales_receipt,name='members_cash_sales_receipt'),

    path('Stock_Category_Load/', shop_views.Stock_Category_Load,name='Stock_Category_Load'),
    path('Stock_add/<str:pk>/', shop_views.Stock_add,name='Stock_add'),
    path('Update_Stock/<str:pk>/<str:return_pk>/', shop_views.Update_Stock,name='Update_Stock'),

    path('Item_Write_off_Reasons/', shop_views.Item_Write_off_Reasons,name='Item_Write_off_Reasons'),
    
    path('Item_Write_off_Reasons_delete/<str:pk>/', shop_views.Item_Write_off_Reasons_delete,name='Item_Write_off_Reasons_delete'),
    path('Item_Write_off_search/', shop_views.Item_Write_off_search,name='Item_Write_off_search'),
    path('Item_Write_off_product_load/', shop_views.Item_Write_off_product_load,name='Item_Write_off_product_load'),
    path('Item_Write_off_product_Preview/<str:pk>/', shop_views.Item_Write_off_product_Preview,name='Item_Write_off_product_Preview'),
    path('Item_Write_off_manage/', shop_views.Item_Write_off_manage,name='Item_Write_off_manage'),
    path('Item_Write_off_manage_Preview/<str:pk>/', shop_views.Item_Write_off_manage_Preview,name='Item_Write_off_manage_Preview'),
    path('Item_Write_off_Approval/', shop_views.Item_Write_off_Approval,name='Item_Write_off_Approval'),
    path('Item_Write_off_Approval_Preview/<str:pk>/', shop_views.Item_Write_off_Approval_Preview,name='Item_Write_off_Approval_Preview'),
    path('Item_Write_off_Approved_List/', shop_views.Item_Write_off_Approved_List,name='Item_Write_off_Approved_List'),
    path('Item_Write_off_Approved__Process/<str:pk>/', shop_views.Item_Write_off_Approved_Process,name='Item_Write_off_Approved_Process'),
    


    path('Members_Credit_sales_list_search/', shop_views.Members_Credit_sales_list_search,name='Members_Credit_sales_list_search'),
    path('Members_Credit_sales_list_load/', shop_views.Members_Credit_sales_list_load,name='Members_Credit_sales_list_load'),
    path('Members_Credit_sales_item_select/<str:pk>/', shop_views.Members_Credit_sales_item_select,name='Members_Credit_sales_item_select'),

    path('members_credit_issue_item/<str:pk>/<str:member_id>/', shop_views.members_credit_issue_item,name='members_credit_issue_item'),
    path('Members_Credit_sales_item_select_remove/<str:pk>/<str:member_id>/', shop_views.Members_Credit_sales_item_select_remove,name='Members_Credit_sales_item_select_remove'),

    path('members_credit_sales_item_select_preview/<str:pk>/<str:ticket>/', shop_views.members_credit_sales_item_select_preview,name='members_credit_sales_item_select_preview'),
    path('members_credit_purchase_summary_add/<str:member_id>/<str:debit>/<str:credit>/<str:balance>/<str:ticket>/', shop_views.members_credit_purchase_summary_add,name='members_credit_purchase_summary_add'),
    path('members_credit_purchase_summary_add/<str:member_id>/<str:debit>/<str:credit>/<str:balance>/<str:ticket>/', shop_views.members_credit_purchase_summary_add,name='members_credit_purchase_summary_add'),
    
    path('members_credit_purchase_manage/', shop_views.members_credit_purchase_manage,name='members_credit_purchase_manage'),
    path('members_credit_purchase_manage_preview/<str:ticket>/', shop_views.members_credit_purchase_manage_preview,name='members_credit_purchase_manage_preview'),

    path('members_credit_purchase_selection_reset_confirmation/<str:ticket>/', shop_views.members_credit_purchase_selection_reset_confirmation,name='members_credit_purchase_selection_reset_confirmation'),
    path('members_credit_purchase_selection_reset_update/<str:ticket>/', shop_views.members_credit_purchase_selection_reset_update,name='members_credit_purchase_selection_reset_update'),

    path('members_credit_purchase_selection_discard_confirmation/<str:ticket>/', shop_views.members_credit_purchase_selection_discard_confirmation,name='members_credit_purchase_selection_discard_confirmation'),
    path('members_credit_purchase_selection_discard_update/<str:ticket>/', shop_views.members_credit_purchase_selection_discard_update,name='members_credit_purchase_selection_discard_update'),
    
    path('members_credit_purchases_approved_list/', shop_views.members_credit_purchases_approved_list,name='members_credit_purchases_approved_list'),
    path('members_credit_purchases_approved_item_details/<str:ticket>/', shop_views.members_credit_purchases_approved_item_details,name='members_credit_purchases_approved_item_details'),

    path('general_cash_sales_dashboard/', shop_views.general_cash_sales_dashboard,name='general_cash_sales_dashboard'),
    path('general_cash_sales_products_load_route/', shop_views.general_cash_sales_products_load_route,name='general_cash_sales_products_load_route'),
    path('general_cash_sales_products_load/<str:pk>/<str:ticket>/', shop_views.general_cash_sales_products_load,name='general_cash_sales_products_load'),
    path('general_cash_issue_item/<str:pk>/<str:cust_id>/', shop_views.general_cash_issue_item,name='general_cash_issue_item'),
    path('general_cash_sales_select_remove/<str:pk>/<str:cust_id>/<str:ticket>/', shop_views.general_cash_sales_select_remove,name='general_cash_sales_select_remove'),
    
   
    path('general_cash_issue_item_preview/<str:ticket>/', shop_views.general_cash_issue_item_preview,name='general_cash_issue_item_preview'),
    path('general_cash_issue_item_print_receipt/<str:ticket>/', shop_views.general_cash_issue_item_print_receipt,name='general_cash_issue_item_print_receipt'),

    path('general_cash_load_existing_customers_search/', shop_views.general_cash_load_existing_customers_search,name='general_cash_load_existing_customers_search'),
    path('general_cash_load_existing_customers/', shop_views.general_cash_load_existing_customers,name='general_cash_load_existing_customers'),

   

    path('check_code_exist/', shop_views.check_code_exist,name='check_code_exist'),
    path('check_receipt_no_exist/', shop_views.check_receipt_no_exist,name='check_receipt_no_exist'),

    path('monthly_deductions_salary_institution_select/', shop_views.monthly_deductions_salary_institution_select,name='monthly_deductions_salary_institution_select'),
    path('monthly_deductions_generate/<str:pk>/', shop_views.monthly_deductions_generate,name='monthly_deductions_generate'),
    path('monthly_deductions_generate_process/<str:pk>/', shop_views.monthly_deductions_generate_process,name='monthly_deductions_generate_process'),
    path('monthly_deductions_generate_process_Completed/<str:pk>/', shop_views.monthly_deductions_generate_process_Completed,name='monthly_deductions_generate_process_Completed'),
    path('monthly_deductions_ledger_posting/', shop_views.monthly_deductions_ledger_posting,name='monthly_deductions_ledger_posting'),
    path('monthly_deductions_ledger_posting_preview/', shop_views.monthly_deductions_ledger_posting_preview,name='monthly_deductions_ledger_posting_preview'),
    path('monthly_deductions_ledger_posting_process/<str:institution>/<str:period>/', shop_views.monthly_deductions_ledger_posting_process,name='monthly_deductions_ledger_posting_process'),

    path('Members_Credit_sales_Cash_Deposit_search/', shop_views.Members_Credit_sales_Cash_Deposit_search,name='Members_Credit_sales_Cash_Deposit_search'),
    path('Members_Credit_sales_Cash_Deposit_list_load/', shop_views.Members_Credit_sales_Cash_Deposit_list_load,name='Members_Credit_sales_Cash_Deposit_list_load'),
    path('Members_Credit_sales_Cash_Deposit_Details/<str:pk>/', shop_views.Members_Credit_sales_Cash_Deposit_Details,name='Members_Credit_sales_Cash_Deposit_Details'),
    path('Cash_Deposit_Summary/', shop_views.Cash_Deposit_Summary,name='Cash_Deposit_Summary'),
   
    path('Members_Credit_sales_ledger_search/', shop_views.Members_Credit_sales_ledger_search,name='Members_Credit_sales_ledger_search'),
    path('Members_Credit_sales_ledger_list_load/', shop_views.Members_Credit_sales_ledger_list_load,name='Members_Credit_sales_ledger_list_load'),
    path('Members_Credit_sales_ledger_preview/<str:pk>/', shop_views.Members_Credit_sales_ledger_preview,name='Members_Credit_sales_ledger_preview'),
    path('Members_Credit_sales_ledger_details/<str:pk>/', shop_views.Members_Credit_sales_ledger_details,name='Members_Credit_sales_ledger_details'),

    path('Daily_Sales_Summarization/<str:pk>/', shop_views.Daily_Sales_Summarization,name='Daily_Sales_Summarization'),
    path('Daily_Sales_Summary_Detail/<str:pk>/', shop_views.Daily_Sales_Summary_Detail,name='Daily_Sales_Summary_Detail'),

    path('Day_End_Transaction_Summary/', shop_views.Day_End_Transaction_Summary,name='Day_End_Transaction_Summary'),
    # path('Load_Credit_Sales/', shop_views.Load_Credit_Sales,name='Load_Credit_Sales'),


    path('Stock_Status/', shop_views.Stock_Status,name='Stock_Status'),
    path('Manage_Stock_Product_Lock/', shop_views.Manage_Stock_Product_Lock,name='Manage_Stock_Product_Lock'),
    path('Manage_Stock_Product_Lock_Individuals/<str:pk>/', shop_views.Manage_Stock_Product_Lock_Individuals,name='Manage_Stock_Product_Lock_Individuals'),
    path('Manage_Stock_Product_UnLock_Individuals/<str:pk>/', shop_views.Manage_Stock_Product_UnLock_Individuals,name='Manage_Stock_Product_UnLock_Individuals'),
    path('Manage_Stock_Product_Lock_Multiple/', shop_views.Manage_Stock_Product_Lock_Multiple,name='Manage_Stock_Product_Lock_Multiple'),
    
    path('Manage_Stock_search/', shop_views.Manage_Stock_search,name='Manage_Stock_search'),
    path('Manage_Stock_Product_load/', shop_views.Manage_Stock_Product_load,name='Manage_Stock_Product_load'),
    path('Manage_Stock_Product_Update/<str:pk>/', shop_views.Manage_Stock_Product_Update,name='Manage_Stock_Product_Update'),
    path('Manage_Stock_Product_delete/<str:pk>/', shop_views.Manage_Stock_Product_delete,name='Manage_Stock_Product_delete'),
    

    path('Supplier_add/', shop_views.Supplier_add,name='Supplier_add'),
    path('Supplier_edit/<str:pk>/', shop_views.Supplier_edit,name='Supplier_edit'),
    
    path('Supplier_Branches_add/<str:pk>/', shop_views.Supplier_Branches_add,name='Supplier_Branches_add'),
    path('Supplier_Branches_edit/<str:pk>/', shop_views.Supplier_Branches_edit,name='Supplier_Branches_edit'),

    path('Supplier_Personnel_add/<str:pk>/', shop_views.Supplier_Personnel_add,name='Supplier_Personnel_add'),
    path('Supplier_Personnel_Edit/<str:pk>/', shop_views.Supplier_Personnel_Edit,name='Supplier_Personnel_Edit'),

    path('Product_Purchase/', shop_views.Product_Purchase,name='Product_Purchase'),
    path('Product_Purchase_Details/<str:pk>/', shop_views.Product_Purchase_Details,name='Product_Purchase_Details'),
    path('Product_Purchase_Details_Select/<str:pk>/<str:invoice_id>/', shop_views.Product_Purchase_Details_Select,name='Product_Purchase_Details_Select'),
    path('Product_Purchase_Details_Select_Remove/<str:pk>/', shop_views.Product_Purchase_Details_Select_Remove,name='Product_Purchase_Details_Select_Remove'),
    path('Product_Purchase_Details_Select_Edit/<str:pk>/', shop_views.Product_Purchase_Details_Select_Edit,name='Product_Purchase_Details_Select_Edit'),
    
    path('Product_Purchase_Addnew_Item/<str:pk>/', shop_views.Product_Purchase_Addnew_Item,name='Product_Purchase_Addnew_Item'),
    path('Product_Purchase_Add_Supplier/', shop_views.Product_Purchase_Add_Supplier,name='Product_Purchase_Add_Supplier'),
    path('Product_Purchase_Add_Supplier_Personnel/<str:pk>/<str:return_pk>/', shop_views.Product_Purchase_Add_Supplier_Personnel,name='Product_Purchase_Add_Supplier_Personnel'),

    path('Purchase_Tracking_Manage/', shop_views.Purchase_Tracking_Manage,name='Purchase_Tracking_Manage'),
    path('Purchase_Tracking_Details/<str:pk>/', shop_views.Purchase_Tracking_Details,name='Purchase_Tracking_Details'),
    path('Purchase_Tracking_Details_Update/<str:pk>/', shop_views.Purchase_Tracking_Details_Update,name='Purchase_Tracking_Details_Update'),
    path('Purchase_Tracking_Invoice_Date_Update/<str:pk>/', shop_views.Purchase_Tracking_Invoice_Date_Update,name='Purchase_Tracking_Invoice_Date_Update'),
    

    path('Purchase_Certification_List_load/', shop_views.Purchase_Certification_List_load,name='Purchase_Certification_List_load'),
    path('Purchase_Certification_item_Preview/<str:pk>/', shop_views.Purchase_Certification_item_Preview,name='Purchase_Certification_item_Preview'),
    path('Purchase_Certification_item_Edit/<str:pk>/', shop_views.Purchase_Certification_item_Edit,name='Purchase_Certification_item_Edit'),
    path('Purchase_Certification_item_Preview_Remove/<str:pk>/', shop_views.Purchase_Certification_item_Preview_Remove,name='Purchase_Certification_item_Preview_Remove'),
    path('Purchase_Certification_item_Preview_Reload/<str:pk>/', shop_views.Purchase_Certification_item_Preview_Reload,name='Purchase_Certification_item_Preview_Reload'),
    path('Purchase_Certification_item_Preview_Processed/<str:pk>/', shop_views.Purchase_Certification_item_Preview_Processed,name='Purchase_Certification_item_Preview_Processed'),
    
    path('Purchase_Certification_item_Add_Item/<str:pk>/', shop_views.Purchase_Certification_item_Add_Item,name='Purchase_Certification_item_Add_Item'),
    path('Purchase_Certification_Product_Purchase_Details_Select/<str:pk>/<str:invoice_id>/', shop_views.Purchase_Certification_Product_Purchase_Details_Select,name='Purchase_Certification_Product_Purchase_Details_Select'),
    
    path('Purchase_Certification_item_Add_Stock/<str:pk>/', shop_views.Purchase_Certification_item_Add_Stock,name='Purchase_Certification_item_Add_Stock'),
    

    ################################################################
    ########################## REPORTS #############################
    ################################################################

    path('GeneratePdf/', shop_views.GeneratePdf.as_view(),name='GeneratePdf'),
    path('GeneratePdf2/', shop_views.GeneratePdf2.as_view(),name='GeneratePdf2'),
    path('GeneratePdf3/', shop_views.GeneratePdf3.as_view(),name='GeneratePdf3'),
    path('GeneratePdf4/', shop_views.GeneratePdf4.as_view(),name='GeneratePdf4'),
    path('All_Stock_Status_Pdf/', shop_views.All_Stock_Status_Pdf,name='All_Stock_Status_Pdf'),
    
    path('All_Stock_Status/', shop_views.All_Stock_Status,name='All_Stock_Status'),
    path('Purchase_Summary/', shop_views.Purchase_Summary,name='Purchase_Summary'),
    path('Purchase_Summary_Details/<str:pk>/', shop_views.Purchase_Summary_Details,name='Purchase_Summary_Details'),
    
    path('Daily_Sales_Report_Summary/', shop_views.Daily_Sales_Report_Summary,name='Daily_Sales_Report_Summary'),
    path('Daily_Sales_Report_Details/<str:pk>/', shop_views.Daily_Sales_Report_Details,name='Daily_Sales_Report_Details'),
    path('Daily_Sales_Report_Receipt_Details/<str:pk>/', shop_views.Daily_Sales_Report_Receipt_Details,name='Daily_Sales_Report_Receipt_Details'),
    path('Daily_Sales_Report_All_Details/<str:year>/<str:month>/<str:day>/<str:sales_category>/', shop_views.Daily_Sales_Report_All_Details,name='Daily_Sales_Report_All_Details'),
   
    path('Daily_Sales_All_Category_Report_Details/<str:d1>/<str:m1>/<str:y1>/<str:d2>/<str:m2>/<str:y2>/', shop_views.Daily_Sales_All_Category_Report_Details,name='Daily_Sales_All_Category_Report_Details'),

    path('load_branches/', shop_views.load_branches,name='ajax_load_branches'),
    

    ####################################################
    ############### SEO DESK ###########################
    ####################################################
    # path('SEO_home/', SEO_views.SEO_home,name='SEO_home'),
    
    # path('members_credit_purchase_approval/', SEO_views.members_credit_purchase_approval,name='members_credit_purchase_approval'),
    # path('members_credit_purchase_approval_preview/<str:ticket>/', SEO_views.members_credit_purchase_approval_preview,name='members_credit_purchase_approval_preview'),

    # path('members_salary_update_request_approval_load_list/', SEO_views.members_salary_update_request_approval_load_list,name='members_salary_update_request_approval_load_list'),
    # path('members_salary_update_request_approval/<str:pk>/', SEO_views.members_salary_update_request_approval,name='members_salary_update_request_approval'),

    # path('external_fascilities_update_request_approval_load_list/', SEO_views.external_fascilities_update_request_approval_load_list,name='external_fascilities_update_request_approval_load_list'),
    # path('external_fascilities_update_request_approval/<str:pk>/', SEO_views.external_fascilities_update_request_approval,name='external_fascilities_update_request_approval'),

    # path('members_exclusiveness_request_approval_list_load/', SEO_views.members_exclusiveness_request_approval_list_load,name='members_exclusiveness_request_approval_list_load'),
    # path('members_exclusiveness_request_approval_process/<str:pk>/', SEO_views.members_exclusiveness_request_approval_process,name='members_exclusiveness_request_approval_process'),

    # path('Shop_Cheque_Sales_List_Load/', SEO_views.Shop_Cheque_Sales_List_Load,name='Shop_Cheque_Sales_List_Load'),
    # path('Shop_Cheque_Sales_process/<str:pk>/', SEO_views.Shop_Cheque_Sales_process,name='Shop_Cheque_Sales_process'),

    # path('Initial_Shares_Update_List_Load/', SEO_views.Initial_Shares_Update_List_Load,name='Initial_Shares_Update_List_Load'),
    # path('Initial_Shares_Update_preview/<str:pk>/', SEO_views.Initial_Shares_Update_preview,name='Initial_Shares_Update_preview'),
   
    # path('Transaction_Adjustment_Approval_list_Load/', SEO_views.Transaction_Adjustment_Approval_list_Load,name='Transaction_Adjustment_Approval_list_Load'),
    # path('Transaction_Adjustment_Approval_Process/<str:pk>/', SEO_views.Transaction_Adjustment_Approval_Process,name='Transaction_Adjustment_Approval_Process'),

    # path('Transaction_Loan_Adjustment_Approval_list_Load/', SEO_views.Transaction_Loan_Adjustment_Approval_list_Load,name='Transaction_Loan_Adjustment_Approval_list_Load'),
    # path('Transaction_Loan_Adjustment_Approval_list_Process/<str:pk>/', SEO_views.Transaction_Loan_Adjustment_Approval_list_Process,name='Transaction_Loan_Adjustment_Approval_list_Process'),
    



] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
