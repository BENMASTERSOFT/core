
from django.contrib import admin
from django.urls import path, include
from core import settings
from django.conf.urls.static import static
from cooperative import views
from cooperative import finsec_views,master_views,treasurer_views,shop_views, deskofficer_views,secretary_views,president_views, SEO_views

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
    path('WithdrawalStatus_upload/',master_views.WithdrawalStatus_upload, name='WithdrawalStatus_upload'),
    path('MultipleLoanStatus_upload/',master_views.MultipleLoanStatus_upload, name='MultipleLoanStatus_upload'),
    path('LoanMergeStatus_upload/',master_views.LoanMergeStatus_upload, name='LoanMergeStatus_upload'),
    path('Product_Write_off_Reasons_upload/',master_views.Product_Write_off_Reasons_upload, name='Product_Write_off_Reasons_upload'),
   



    path('admin_home/', master_views.admin_home,name='admin_home'),
    path('system_reset/', master_views.system_reset,name='system_reset'),
    path('addUserType/', master_views.addUserType,name='addUserType'),
    path('UserType_delete/<str:pk>/', master_views.UserType_delete,name='UserType_delete'),
    
    path('add_staff/', master_views.add_staff,name='add_staff'),
    path('add_staff_manage/', master_views.add_staff_manage,name='add_staff_manage'),
    path('add_staff_manage_view/<str:pk>/', master_views.add_staff_manage_view,name='add_staff_manage_view'),
    
    path('super_user_manage/', master_views.super_user_manage,name='super_user_manage'),
    path('super_user_manage_view/<str:pk>/', master_views.super_user_manage_view,name='super_user_manage_view'),
    
    path('addState/', master_views.addState,name='addState'),
    path('Manage_state/', master_views.Manage_state,name='Manage_state'),
    path('delete_state/<str:pk>/', master_views.delete_state,name='delete_state'),

    path('addNOKRelationships/', master_views.addNOKRelationships,name='addNOKRelationships'),
    path('Manage_NOKRelationships/', master_views.Manage_NOKRelationships,name='Manage_NOKRelationships'),
    path('Manage_NOKRelationships_Remove/<str:pk>/', master_views.Manage_NOKRelationships_Remove,name='Manage_NOKRelationships_Remove'),
    

    path('addDefaultPassword/', master_views.addDefaultPassword,name='addDefaultPassword'),
    path('addTransactionStatus/', master_views.addTransactionStatus,name='addTransactionStatus'),
    path('addProcessingStatus/', master_views.addProcessingStatus,name='addProcessingStatus'),
    path('addReceiptStatus/', master_views.addReceiptStatus,name='addReceiptStatus'),
    path('addMembershipStatus/', master_views.addMembershipStatus,name='addMembershipStatus'),
    path('addGender/', master_views.addGender,name='addGender'),
    path('addTitles/', master_views.addTitles,name='addTitles'),
    # path('addUserLevels/', master_views.addUserLevels,name='addUserLevels'),
    path('addTransactionSources/', master_views.addTransactionSources,name='addTransactionSources'),
    path('addInterestDeductionSource/', master_views.addInterestDeductionSource,name='addInterestDeductionSource'),
    path('addSalaryInstitution/', master_views.addSalaryInstitution,name='addSalaryInstitution'),
    path('addDepartments/', master_views.addDepartments,name='addDepartments'),
    path('addBanks/', master_views.addBanks,name='addBanks'),
    path('addLocations/', master_views.addLocations,name='addLocations'),

    path('addTransactionTypes/', master_views.addTransactionTypes,name='addTransactionTypes'),
    path('TransactionTypes_Manage_Load/', master_views.TransactionTypes_Manage_Load,name='TransactionTypes_Manage_Load'),
    path('TransactionTypes_Update/<str:pk>/', master_views.TransactionTypes_Update, name='TransactionTypes_Update'),

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
   

    path('AddApprovableTransactions/', master_views.AddApprovableTransactions,name='AddApprovableTransactions'),
    path('AddApprovableTransactionsUpdate/<str:pk>/', master_views.AddApprovableTransactionsUpdate,name='AddApprovableTransactionsUpdate'),
    
    path('AddCertifiableTransactions/', master_views.AddCertifiableTransactions,name='AddCertifiableTransactions'),
    path('AddCertifiableTransactionsUpdate/<str:pk>/', master_views.AddCertifiableTransactionsUpdate,name='AddCertifiableTransactionsUpdate'),
    
    path('ApprovableOfficers/', master_views.ApprovableOfficers,name='ApprovableOfficers'),
    path('ApprovableOfficersUpdate/<str:pk>/', master_views.ApprovableOfficersUpdate,name='ApprovableOfficersUpdate'),

    path('AddCertificationOfficers/', master_views.AddCertificationOfficers,name='AddCertificationOfficers'),
    path('CertificationOfficersUpdate/<str:pk>/', master_views.CertificationOfficersUpdate,name='CertificationOfficersUpdate'),
    
    path('AddDisbursementOfficers/', master_views.AddDisbursementOfficers,name='AddDisbursementOfficers'),
    path('DisbursementOfficersUpdate/<str:pk>/', master_views.DisbursementOfficersUpdate,name='DisbursementOfficersUpdate'),

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
   






    ################# MASTER ADMIN REPORT ##################################
    path('transaction_views_ranked/', master_views.transaction_views_ranked,name='transaction_views_ranked'),
    path('List_of_Users/', master_views.List_of_Users,name='List_of_Users'),

    ###########################################################################
    ########################## DESK OFFICER HOME ###############################
    ###########################################################################
    path('deskofficer_home/', deskofficer_views.deskofficer_home,name='deskofficer_home'),

    path('Useraccount_manager/', deskofficer_views.Useraccount_manager,name='Useraccount_manager'),
    
    path('desk_basic_form/', deskofficer_views.desk_basic_form,name='desk_basic_form'),
    path('desk_basic_table/', deskofficer_views.desk_basic_table,name='desk_basic_table'),
    path('desk_datatable_table/', deskofficer_views.desk_datatable_table,name='desk_datatable_table'),
    
    path('membership_request/', deskofficer_views.membership_request,name='membership_request'),
    path('membership_request_complete_search/', deskofficer_views.membership_request_complete_search,name='membership_request_complete_search'),
    path('membership_request_complete_load/', deskofficer_views.membership_request_complete_load,name='membership_request_complete_load'),
    path('membership_request_additional_info/<str:pk>/', deskofficer_views.membership_request_additional_info,name='membership_request_additional_info'),
   
    path('membership_request_additional_info_save/<str:pk>/', deskofficer_views.membership_request_additional_info_save,name='membership_request_additional_info_save'),
    path('membership_request_additional_info_delete_confirm/<str:pk>/<str:return_pk>/', deskofficer_views.membership_request_additional_info_delete_confirm,name='membership_request_additional_info_delete_confirm'),
    path('membership_request_additional_info_delete/<str:pk>/<str:return_pk>/', deskofficer_views.membership_request_additional_info_delete,name='membership_request_additional_info_delete'),

    path('MemberShipRequestAdditionalAttachment_save/<str:pk>/', deskofficer_views.MemberShipRequestAdditionalAttachment_save,name='MemberShipRequestAdditionalAttachment_save'),
    path('MemberShipRequest_submit/<str:pk>/', deskofficer_views.MemberShipRequest_submit,name='MemberShipRequest_submit'),

    path('membership_form_sales_list_load/', deskofficer_views.membership_form_sales_list_load,name='membership_form_sales_list_load'),
    path('membership_form_sales_preview/<str:pk>/', deskofficer_views.membership_form_sales_preview,name='membership_form_sales_preview'),
    path('membership_form_sales_issue/<str:pk>/', deskofficer_views.membership_form_sales_issue,name='membership_form_sales_issue'),

    path('membership_registration_list_load/', deskofficer_views.membership_registration_list_load,name='membership_registration_list_load'),
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

    path('Transaction_Loan_adjustment_search/', deskofficer_views.Transaction_Loan_adjustment_search,name='Transaction_Loan_adjustment_search'),
    path('Transaction_Loan_adjustment_List_load/', deskofficer_views.Transaction_Loan_adjustment_List_load,name='Transaction_Loan_adjustment_List_load'),
    path('Transaction_Loan_adjustment_Transaction_load/<str:pk>/', deskofficer_views.Transaction_Loan_adjustment_Transaction_load,name='Transaction_Loan_adjustment_Transaction_load'),
    path('Transaction_Loan_adjustment_Transaction_Preview/<str:pk>/<str:loan_code>/', deskofficer_views.Transaction_Loan_adjustment_Transaction_Preview,name='Transaction_Loan_adjustment_Transaction_Preview'),
    path('Transaction_Loan_adjustment_Transaction_Process/<str:pk>/<str:loan_code>/', deskofficer_views.Transaction_Loan_adjustment_Transaction_Process,name='Transaction_Loan_adjustment_Transaction_Process'),
    path('Transaction_Loan_adjustment_Transaction_Cancel/<str:pk>/', deskofficer_views.Transaction_Loan_adjustment_Transaction_Cancel,name='Transaction_Loan_adjustment_Transaction_Cancel'),

    path('Transaction_Loan_adjustment_Transaction_Approved_List_Load/', deskofficer_views.Transaction_Loan_adjustment_Transaction_Approved_List_Load,name='Transaction_Loan_adjustment_Transaction_Approved_List_Load'),

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
    path('loan_application_preview/<str:pk>/', deskofficer_views.loan_application_preview,name='loan_application_preview'),

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

    path('external_fascility_update_search/', deskofficer_views.external_fascility_update_search,name='external_fascility_update_search'),
    path('external_fascility_update_list_load/', deskofficer_views.external_fascility_update_list_load,name='external_fascility_update_list_load'),
    path('external_fascility_update_process/<str:pk>/', deskofficer_views.external_fascility_update_process,name='external_fascility_update_process'),
    path('external_fascility_update_process_remove/<str:pk>/<str:return_pk>/', deskofficer_views.external_fascility_update_process_remove,name='external_fascility_update_process_remove'),

    path('external_fascility_update_approved_list_load/', deskofficer_views.external_fascility_update_approved_list_load,name='external_fascility_update_approved_list_load'),
    path('external_fascility_update_approved_processed/<str:pk>/', deskofficer_views.external_fascility_update_approved_processed,name='external_fascility_update_approved_processed'),


    path('TransactionPeriodManager/', deskofficer_views.TransactionPeriodManager,name='TransactionPeriodManager'),
    path('TransactionPeriodsUpdate/<str:pk>/', deskofficer_views.TransactionPeriodsUpdate,name='TransactionPeriodsUpdate'),

    path('Monthly_Deduction_Salary_Institution_Load/', deskofficer_views.Monthly_Deduction_Salary_Institution_Load,name='Monthly_Deduction_Salary_Institution_Load'),
    path('Monthly_Individual_Transactions_Load/<str:pk>/', deskofficer_views.Monthly_Individual_Transactions_Load,name='Monthly_Individual_Transactions_Load'),
    
    path('Monthly_Savings_Contribution_preview/<str:pk>/<str:salary_inst_key>/', deskofficer_views.Monthly_Savings_Contribution_preview,name='Monthly_Savings_Contribution_preview'),
    path('Monthly_Savings_Contribution_Generate/<str:pk>/<str:salary_inst_key>/', deskofficer_views.Monthly_Savings_Contribution_Generate,name='Monthly_Savings_Contribution_Generate'),

    path('Monthly_loan_repayement_preview/<str:pk>/<str:salary_inst_key>/', deskofficer_views.Monthly_loan_repayement_preview,name='Monthly_loan_repayement_preview'),
    path('Monthly_loan_repayement_Generate/<str:pk>/<str:salary_inst_key>/', deskofficer_views.Monthly_loan_repayement_Generate,name='Monthly_loan_repayement_Generate'),

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

    path('monthly_wrongful_deduction_transaction_period_load/', deskofficer_views.monthly_wrongful_deduction_transaction_period_load,name='monthly_wrongful_deduction_transaction_period_load'),
    path('Monthly_Unbalanced_transactions/', deskofficer_views.Monthly_Unbalanced_transactions,name='Monthly_Unbalanced_transactions'),

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

    # path('Members_Welfare_Upload_Verification_list_load/', deskofficer_views.Members_Welfare_Upload_Verification_list_load,name='Members_Welfare_Upload_Verification_list_load'),
    # path('Members_Welfare_Upload_verication_Preview/<str:pk>/', deskofficer_views.Members_Welfare_Upload_verication_Preview,name='Members_Welfare_Upload_verication_Preview'),

    path('Updating_Date_Joined/', deskofficer_views.Updating_Date_Joined,name='Updating_Date_Joined'),
    path('Updating_Date_Joined_Preview/<str:pk>/', deskofficer_views.Updating_Date_Joined_Preview,name='Updating_Date_Joined_Preview'),

    path('Updating_Date_Joined_Manage_List_load/', deskofficer_views.Updating_Date_Joined_Manage_List_load,name='Updating_Date_Joined_Manage_List_load'),
    path('Updating_Date_Joined_Manage_Preview/<str:pk>/', deskofficer_views.Updating_Date_Joined_Manage_Preview,name='Updating_Date_Joined_Manage_Preview'),

    path('Updating_Gross_Pay_selected_search/', deskofficer_views.Updating_Gross_Pay_selected_search,name='Updating_Gross_Pay_selected_search'),
    path('Updating_Gross_Pay_selected_list_load/', deskofficer_views.Updating_Gross_Pay_selected_list_load,name='Updating_Gross_Pay_selected_list_load'),
    path('Updating_Gross_Pay_selected_Preview/<str:pk>/', deskofficer_views.Updating_Gross_Pay_selected_Preview,name='Updating_Gross_Pay_selected_Preview'),
    

    path('Updating_Gross_Pay/', deskofficer_views.Updating_Gross_Pay,name='Updating_Gross_Pay'),
    path('Updating_Gross_Pay_Preview/<str:pk>/', deskofficer_views.Updating_Gross_Pay_Preview,name='Updating_Gross_Pay_Preview'),

    path('Updating_Gross_Pay_Manage/', deskofficer_views.Updating_Gross_Pay_Manage,name='Updating_Gross_Pay_Manage'),
    path('Updating_Gross_Pay_Manage_Preview/<str:pk>/', deskofficer_views.Updating_Gross_Pay_Manage_Preview,name='Updating_Gross_Pay_Manage_Preview'),

    path('Norminal_Roll/', deskofficer_views.Norminal_Roll,name='Norminal_Roll'),
    path('Norminal_Roll_Update/<str:pk>/', deskofficer_views.Norminal_Roll_Update,name='Norminal_Roll_Update'),
    

    path('Updating_Title_list_load/', deskofficer_views.Updating_Title_list_load,name='Updating_Title_list_load'),
    path('Updating_Updating_Title_Preview/<str:pk>/', deskofficer_views.Updating_Updating_Title_Preview,name='Updating_Updating_Title_Preview'),
    
    path('Updating_Title_selected_search/', deskofficer_views.Updating_Title_selected_search,name='Updating_Title_selected_search'),
    path('Updating_Title_selected_list_load/', deskofficer_views.Updating_Title_selected_list_load,name='Updating_Title_selected_list_load'),
    path('Updating_Updating_Title_Preview1/<str:pk>/', deskofficer_views.Updating_Updating_Title_Preview1,name='Updating_Updating_Title_Preview1'),
    

    path('Updating_Department_list_load/', deskofficer_views.Updating_Department_list_load,name='Updating_Department_list_load'),
    path('Updating_Updating_Department_Preview/<str:pk>/', deskofficer_views.Updating_Updating_Department_Preview,name='Updating_Updating_Department_Preview'),
    
    path('Updating_Department_selected_search/', deskofficer_views.Updating_Department_selected_search,name='Updating_Department_selected_search'),
    path('Updating_Department_selected_list_load/', deskofficer_views.Updating_Department_selected_list_load,name='Updating_Department_selected_list_load'),
    path('Updating_Updating_Department_Preview1/<str:pk>/', deskofficer_views.Updating_Updating_Department_Preview1,name='Updating_Updating_Department_Preview1'),

    path('Updating_Gender_list_load/', deskofficer_views.Updating_Gender_list_load,name='Updating_Gender_list_load'),
    path('Updating_Gender_Preview/<str:pk>/', deskofficer_views.Updating_Gender_Preview,name='Updating_Gender_Preview'),
    
    path('Updating_Gender_selected_search/', deskofficer_views.Updating_Gender_selected_search,name='Updating_Gender_selected_search'),
    path('Updating_Gender_selected_list_load/', deskofficer_views.Updating_Gender_selected_list_load,name='Updating_Gender_selected_list_load'),
    path('Updating_Gender_Preview1/<str:pk>/', deskofficer_views.Updating_Gender_Preview1,name='Updating_Gender_Preview1'),

    path('Members_Share_Purchase_Request_Search/', deskofficer_views.Members_Share_Purchase_Request_Search,name='Members_Share_Purchase_Request_Search'),
    path('Members_Share_Purchase_Request_list_load/', deskofficer_views.Members_Share_Purchase_Request_list_load,name='Members_Share_Purchase_Request_list_load'),
    path('Members_Share_Purchase_Request_View/<str:pk>/', deskofficer_views.Members_Share_Purchase_Request_View,name='Members_Share_Purchase_Request_View'),

    path('Members_Share_Purchase_Request_Process/', deskofficer_views.Members_Share_Purchase_Request_Process,name='Members_Share_Purchase_Request_Process'),
    path('Members_Share_Purchase_Request_Process_View/<str:pk>/', deskofficer_views.Members_Share_Purchase_Request_Process_View,name='Members_Share_Purchase_Request_Process_View'),
    

    path('Members_Initial_Shares_update_Search/', deskofficer_views.Members_Initial_Shares_update_Search,name='Members_Initial_Shares_update_Search'),
    path('Members_Initial_Shares_update_list_load/', deskofficer_views.Members_Initial_Shares_update_list_load,name='Members_Initial_Shares_update_list_load'),
    path('Members_Initial_Shares_update_preview/<str:pk>/', deskofficer_views.Members_Initial_Shares_update_preview,name='Members_Initial_Shares_update_preview'),
    
    path('Members_Initial_Shares_update_approved_list_load/', deskofficer_views.Members_Initial_Shares_update_approved_list_load,name='Members_Initial_Shares_update_approved_list_load'),
    path('Members_Initial_Shares_update_approved_processed/<str:pk>/', deskofficer_views.Members_Initial_Shares_update_approved_processed,name='Members_Initial_Shares_update_approved_processed'),

    path('PersonalLedger_Selected_Search/', deskofficer_views.PersonalLedger_Selected_Search,name='PersonalLedger_Selected_Search'),
    path('PersonalLedger_Selected_list_load/', deskofficer_views.PersonalLedger_Selected_list_load,name='PersonalLedger_Selected_list_load'),
    path('PersonalLedger_Transaction_Load/<str:pk>/', deskofficer_views.PersonalLedger_Transaction_Load,name='PersonalLedger_Transaction_Load'),
    path('PersonalLedger_Transaction_Account_Load/<str:pk>/<str:trans_id>/', deskofficer_views.PersonalLedger_Transaction_Account_Load,name='PersonalLedger_Transaction_Account_Load'),
    # path('PersonalLedger_Selected_View/<str:pk>/<str:trans_id>/', deskofficer_views.PersonalLedger_Selected_View,name='PersonalLedger_Selected_View'),
    
    
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
  

    ################################################################################
    #################################### REPORTS ####################################
    ################################################################################

    path('Cash_Deposit_Report_Date_Load/', deskofficer_views.Cash_Deposit_Report_Date_Load,name='Cash_Deposit_Report_Date_Load'),
    path('Load_Active_loans/', deskofficer_views.Load_Active_loans,name='Load_Active_loans'),

    path('Norminal_Roll_List_Load/', deskofficer_views.Norminal_Roll_List_Load,name='Norminal_Roll_List_Load'),
    path('Norminal_Roll_Personel_Detail/<str:pk>/', deskofficer_views.Norminal_Roll_Personel_Detail,name='Norminal_Roll_Personel_Detail'),
    







    path('temporallyloan/', deskofficer_views.temporallyloan,name='temporallyloan'),
    path('temporally_loan_form/<str:pk>/', deskofficer_views.temporally_loan_form,name='temporally_loan_form'),

   
    path('check_receipt_no_already_used/', deskofficer_views.check_receipt_no_already_used,name='check_receipt_no_already_used'),
    path('check_membership_phone_no_exist/', deskofficer_views.check_membership_phone_no_exist,name='check_membership_phone_no_exist'),
   



    ###########################################################################
    ############################ SECRETARY######################################
    ########################################################################### 

    path('secretary_home/', secretary_views.secretary_home,name='secretary_home'),
    path('membership_request_certification_list_load/', secretary_views.membership_request_certification_list_load,name='membership_request_certification_list_load'),
    path('membership_request_certification_info/<str:pk>/', secretary_views.membership_request_certification_info,name='membership_request_certification_info'),
    path('membership_request_certification_additional_info_save/<str:pk>/', secretary_views.membership_request_certification_additional_info_save,name='membership_request_certification_additional_info_save'),
    path('membership_request_certification_additional_info_delete/<str:pk>/<str:return_pk>/', secretary_views.membership_request_certification_additional_info_delete,name='membership_request_certification_additional_info_delete'),
    
    path('MemberShipRequestAdditionalAttachment_certification_save/<str:pk>/', secretary_views.MemberShipRequestAdditionalAttachment_certification_save,name='MemberShipRequestAdditionalAttachment_certification_save'),
    path('MemberShipRequestAdditionalAttachment_certification_delete/<str:pk>/<str:return_pk>/', secretary_views.MemberShipRequestAdditionalAttachment_certification_delete,name='MemberShipRequestAdditionalAttachment_certification_delete'),

    path('MemberShipRequest_certification_submit/<str:pk>/', secretary_views.MemberShipRequest_certification_submit,name='MemberShipRequest_certification_submit'),

    path('Loan_request_certification_list_load/', secretary_views.Loan_request_certification_list_load,name='Loan_request_certification_list_load'),
    path('Loan_request_certification_details/<str:pk>/', secretary_views.Loan_request_certification_details,name='Loan_request_certification_details'),
    
    path('Loan_application_certification_list_load/', secretary_views.Loan_application_certification_list_load,name='Loan_application_certification_list_load'),
    path('Loan_application_certification_details/<str:pk>/', secretary_views.Loan_application_certification_details,name='Loan_application_certification_details'),
   


    ###########################################################################
    ############################ PRESIDENT######################################
    ########################################################################### 

    path('president_home/', president_views.president_home,name='president_home'),
    path('membership_request_approvals_list_load/', president_views.membership_request_approvals_list_load,name='membership_request_approvals_list_load'),
    path('membership_request_approval_info/<str:pk>/', president_views.membership_request_approval_info,name='membership_request_approval_info'),
    
    path('membership_request_approval_comment_save/<str:pk>/', president_views.membership_request_approval_comment_save,name='membership_request_approval_comment_save'),
    path('membership_request_approval_info_delete/<str:pk>/', president_views.membership_request_approval_info_delete,name='membership_request_approval_info_delete'),
    
    path('membership_request_approval_attachment_save/<str:pk>/', president_views.membership_request_approval_attachment_save,name='membership_request_approval_attachment_save'),
    path('membership_request_approval_attachment_delete/<str:pk>/', president_views.membership_request_approval_attachment_delete,name='membership_request_approval_attachment_delete'),
    
    path('MemberShipRequest_approval_submit/<str:pk>/', president_views.MemberShipRequest_approval_submit,name='MemberShipRequest_approval_submit'),

    path('loan_request_approval_list_load/', president_views.loan_request_approval_list_load,name='loan_request_approval_list_load'),
    path('Loan_request_approval_details/<str:pk>/', president_views.Loan_request_approval_details,name='Loan_request_approval_details'),
    
    path('loan_application_approval_list_load/', president_views.loan_application_approval_list_load,name='loan_application_approval_list_load'),
    path('Loan_application_approval_details/<str:pk>/', president_views.Loan_application_approval_details,name='Loan_application_approval_details'),

    path('savings_cash_withdrawal_list_load/', president_views.savings_cash_withdrawal_list_load,name='savings_cash_withdrawal_list_load'),
    path('savings_cash_withdrawal_preview/<str:pk>/', president_views.savings_cash_withdrawal_preview,name='savings_cash_withdrawal_preview'),

    path('members_exclusiveness_list_load/', president_views.members_exclusiveness_list_load,name='members_exclusiveness_list_load'),
    path('members_exclusiveness_process/<str:pk>/', president_views.members_exclusiveness_process,name='members_exclusiveness_process'),

    path('Shares_Purchase_Request_Approval_List_Load/', president_views.Shares_Purchase_Request_Approval_List_Load,name='Shares_Purchase_Request_Approval_List_Load'),
    path('Shares_Purchase_Request_Approval_Processed/<str:pk>/', president_views.Shares_Purchase_Request_Approval_Processed,name='Shares_Purchase_Request_Approval_Processed'),
    



    ###########################################################################
    ########################### #FIN SEC ######################################
    ###########################################################################
    path('FINSEC_home/', finsec_views.FINSEC_home,name='FINSEC_home'),
    
    path('Cash_Withdrawal_Approved_list_load/', finsec_views.Cash_Withdrawal_Approved_list_load,name='Cash_Withdrawal_Approved_list_load'),
    path('Cash_Withdrawal_Approved_Details/<str:pk>/', finsec_views.Cash_Withdrawal_Approved_Details,name='Cash_Withdrawal_Approved_Details'),

    path('finsec_AutoReceipt_Setup/', finsec_views.finsec_AutoReceipt_Setup,name='finsec_AutoReceipt_Setup'),
    path('finsec_receipt_manager/', finsec_views.finsec_receipt_manager,name='finsec_receipt_manager'),
    path('finsec_CooperativeBankAccounts_add/', finsec_views.finsec_CooperativeBankAccounts_add,name='finsec_CooperativeBankAccounts_add'),
    path('finsec_CooperativeBankAccounts_Remove/<str:pk>/', finsec_views.finsec_CooperativeBankAccounts_Remove,name='finsec_CooperativeBankAccounts_Remove'),
    path('finsec_CooperativeBankAccounts_Update/<str:pk>/', finsec_views.finsec_CooperativeBankAccounts_Update,name='finsec_CooperativeBankAccounts_Update'),





    ###########################################################################
    ############################ TREASURER   ######################################
    ###########################################################################
    path('treasurer_home/', treasurer_views.treasurer_home,name='treasurer_home'),
    path('withdrawal_confirmation_list_load/', treasurer_views.withdrawal_confirmation_list_load,name='withdrawal_confirmation_list_load'),
    path('withdrawal_confirmation_details/<str:pk>/', treasurer_views.withdrawal_confirmation_details,name='withdrawal_confirmation_details'),

    path('tre_AutoReceipt_Setup/', treasurer_views.tre_AutoReceipt_Setup,name='tre_AutoReceipt_Setup'),
    path('tre_receipt_manager/', treasurer_views.tre_receipt_manager,name='tre_receipt_manager'),
    
    path('tre_CooperativeBankAccounts_add/', treasurer_views.tre_CooperativeBankAccounts_add,name='tre_CooperativeBankAccounts_add'),
    path('tre_CooperativeBankAccounts_Remove/<str:pk>/', treasurer_views.tre_CooperativeBankAccounts_Remove,name='tre_CooperativeBankAccounts_Remove'),
    path('tre_CooperativeBankAccounts_Update/<str:pk>/', treasurer_views.tre_CooperativeBankAccounts_Update,name='tre_CooperativeBankAccounts_Update'),



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

    path('Stock_Category_Load/', shop_views.Stock_Category_Load,name='Stock_Category_Load'),
    path('Stock_add/<str:pk>/', shop_views.Stock_add,name='Stock_add'),
    path('Update_Stock/<str:pk>/<str:return_pk>/', shop_views.Update_Stock,name='Update_Stock'),

    path('Item_Write_off_search/', shop_views.Item_Write_off_search,name='Item_Write_off_search'),
    path('Item_Write_off_product_load/', shop_views.Item_Write_off_product_load,name='Item_Write_off_product_load'),
    path('Item_Write_off_product_Preview/<str:pk>/', shop_views.Item_Write_off_product_Preview,name='Item_Write_off_product_Preview'),
    


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

    path('general_cash_load_existing_customers_search/', shop_views.general_cash_load_existing_customers_search,name='general_cash_load_existing_customers_search'),
    path('general_cash_load_existing_customers/', shop_views.general_cash_load_existing_customers,name='general_cash_load_existing_customers'),

   

    path('check_code_exist/', shop_views.check_code_exist,name='check_code_exist'),
    path('check_receipt_no_exist/', shop_views.check_receipt_no_exist,name='check_receipt_no_exist'),

    path('monthly_deductions_salary_institution_select/', shop_views.monthly_deductions_salary_institution_select,name='monthly_deductions_salary_institution_select'),
    path('monthly_deductions_generate/<str:pk>/', shop_views.monthly_deductions_generate,name='monthly_deductions_generate'),
    path('monthly_deductions_generate_process/<str:pk>/', shop_views.monthly_deductions_generate_process,name='monthly_deductions_generate_process'),

    path('Members_Credit_sales_Cash_Deposit_search/', shop_views.Members_Credit_sales_Cash_Deposit_search,name='Members_Credit_sales_Cash_Deposit_search'),
    path('Members_Credit_sales_Cash_Deposit_list_load/', shop_views.Members_Credit_sales_Cash_Deposit_list_load,name='Members_Credit_sales_Cash_Deposit_list_load'),
    path('Members_Credit_sales_Cash_Deposit_Details/<str:pk>/', shop_views.Members_Credit_sales_Cash_Deposit_Details,name='Members_Credit_sales_Cash_Deposit_Details'),
   
    path('Members_Credit_sales_ledger_search/', shop_views.Members_Credit_sales_ledger_search,name='Members_Credit_sales_ledger_search'),
    path('Members_Credit_sales_ledger_list_load/', shop_views.Members_Credit_sales_ledger_list_load,name='Members_Credit_sales_ledger_list_load'),
    path('Members_Credit_sales_ledger_preview/<str:pk>/', shop_views.Members_Credit_sales_ledger_preview,name='Members_Credit_sales_ledger_preview'),
    path('Members_Credit_sales_ledger_details/<str:pk>/', shop_views.Members_Credit_sales_ledger_details,name='Members_Credit_sales_ledger_details'),

    path('Daily_Sales_Summarization/<str:pk>/', shop_views.Daily_Sales_Summarization,name='Daily_Sales_Summarization'),
    path('Daily_Sales_Summary_Detail/<str:pk>/', shop_views.Daily_Sales_Summary_Detail,name='Daily_Sales_Summary_Detail'),

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

    path('All_Stock_Status/', shop_views.All_Stock_Status,name='All_Stock_Status'),
    path('Purchase_Summary/', shop_views.Purchase_Summary,name='Purchase_Summary'),
    path('Purchase_Summary_Details/<str:pk>/', shop_views.Purchase_Summary_Details,name='Purchase_Summary_Details'),
    

    path('load_branches/', shop_views.load_branches,name='ajax_load_branches'),
    

    ####################################################
    ############### SEO DESK ###########################
    ####################################################
    path('SEO_home/', SEO_views.SEO_home,name='SEO_home'),
    
    path('members_credit_purchase_approval/', SEO_views.members_credit_purchase_approval,name='members_credit_purchase_approval'),
    path('members_credit_purchase_approval_preview/<str:ticket>/', SEO_views.members_credit_purchase_approval_preview,name='members_credit_purchase_approval_preview'),

    path('members_salary_update_request_approval_load_list/', SEO_views.members_salary_update_request_approval_load_list,name='members_salary_update_request_approval_load_list'),
    path('members_salary_update_request_approval/<str:pk>/', SEO_views.members_salary_update_request_approval,name='members_salary_update_request_approval'),

    path('external_fascilities_update_request_approval_load_list/', SEO_views.external_fascilities_update_request_approval_load_list,name='external_fascilities_update_request_approval_load_list'),
    path('external_fascilities_update_request_approval/<str:pk>/', SEO_views.external_fascilities_update_request_approval,name='external_fascilities_update_request_approval'),

    path('members_exclusiveness_request_approval_list_load/', SEO_views.members_exclusiveness_request_approval_list_load,name='members_exclusiveness_request_approval_list_load'),
    path('members_exclusiveness_request_approval_process/<str:pk>/', SEO_views.members_exclusiveness_request_approval_process,name='members_exclusiveness_request_approval_process'),

    path('Shop_Cheque_Sales_List_Load/', SEO_views.Shop_Cheque_Sales_List_Load,name='Shop_Cheque_Sales_List_Load'),
    path('Shop_Cheque_Sales_process/<str:pk>/', SEO_views.Shop_Cheque_Sales_process,name='Shop_Cheque_Sales_process'),

    path('Initial_Shares_Update_List_Load/', SEO_views.Initial_Shares_Update_List_Load,name='Initial_Shares_Update_List_Load'),
    path('Initial_Shares_Update_preview/<str:pk>/', SEO_views.Initial_Shares_Update_preview,name='Initial_Shares_Update_preview'),
   
    path('Transaction_Adjustment_Approval_list_Load/', SEO_views.Transaction_Adjustment_Approval_list_Load,name='Transaction_Adjustment_Approval_list_Load'),
    path('Transaction_Adjustment_Approval_Process/<str:pk>/', SEO_views.Transaction_Adjustment_Approval_Process,name='Transaction_Adjustment_Approval_Process'),

    path('Transaction_Loan_Adjustment_Approval_list_Load/', SEO_views.Transaction_Loan_Adjustment_Approval_list_Load,name='Transaction_Loan_Adjustment_Approval_list_Load'),
    path('Transaction_Loan_Adjustment_Approval_list_Process/<str:pk>/', SEO_views.Transaction_Loan_Adjustment_Approval_list_Process,name='Transaction_Loan_Adjustment_Approval_list_Process'),
    



] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
