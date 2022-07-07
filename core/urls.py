
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

    path('User_Profile/', master_views.User_Profile,name='User_Profile'),

    path('basic_form/', master_views.basic_form,name='basic_form'),
    path('basic_table/', master_views.basic_table,name='basic_table'),
    path('datatable_table/', master_views.datatable_table,name='datatable_table'),


    path('title_upload/',master_views.title_upload, name='title_upload'),
    path('states_upload/',master_views.states_upload, name='states_upload'),
    path('NOKRelationships_upload/',master_views.NOKRelationships_upload, name='NOKRelationships_upload'),
    path('lga_upload/',master_views.lga_upload, name='lga_upload'),
    path('Gender_upload/',master_views.Gender_upload, name='Gender_upload'),
    path('Banks_upload/',master_views.Banks_upload, name='Banks_upload'),
    path('Locations_upload/',master_views.Locations_upload, name='Locations_upload'),
    path('Departments_upload/',master_views.Departments_upload, name='Departments_upload'),
    path('SalaryInstitution_upload/',master_views.SalaryInstitution_upload, name='SalaryInstitution_upload'),
    path('TransactionSources_upload/',master_views.TransactionSources_upload, name='TransactionSources_upload'),

    path('SharesUnits_upload/',master_views.SharesUnits_upload, name='SharesUnits_upload'),
    path('UserTypes_upload/',master_views.UserTypes_upload, name='UserTypes_upload'),
    path('ProductCategory_upload/',master_views.ProductCategory_upload, name='ProductCategory_upload'),
    path('Stock_upload/',master_views.Stock_upload, name='Stock_upload'),
    path('Product_Write_off_Reasons_upload/',master_views.Product_Write_off_Reasons_upload, name='Product_Write_off_Reasons_upload'),
    path('MonthlyDeductionGenerationHeaders_upload/',master_views.MonthlyDeductionGenerationHeaders_upload, name='MonthlyDeductionGenerationHeaders_upload'),
    path('Termination_Sources_upload/',master_views.Termination_Sources_upload, name='Termination_Sources_upload'),
    path('ExceptableCriterias_upload/',master_views.ExceptableCriterias_upload, name='ExceptableCriterias_upload'),
    path('System_Users_Tasks_upload/',master_views.System_Users_Tasks_upload, name='System_Users_Tasks_upload'),
    path('Transaction_Types_upload/',master_views.Transaction_Types_upload, name='Transaction_Types_upload'),

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
    path('trending_commodity_signatories/', master_views.trending_commodity_signatories,name='trending_commodity_signatories'),
    path('trending_commodity_signatories_delete/<str:pk>/', master_views.trending_commodity_signatories_delete,name='trending_commodity_signatories_delete'),


    path('Executive_Users/', master_views.Executive_Users,name='Executive_Users'),
    path('Executive_Users_Tasks_Preview/<str:pk>/', master_views.Executive_Users_Tasks_Preview,name='Executive_Users_Tasks_Preview'),
    path('Executive_Users_Tasks_Remove/<str:pk>/', master_views.Executive_Users_Tasks_Remove,name='Executive_Users_Tasks_Remove'),


    path('Desk_Office_Users/', master_views.Desk_Office_Users,name='Desk_Office_Users'),
    path('Desk_Office_Tasks_Preview/<str:pk>/', master_views.Desk_Office_Tasks_Preview,name='Desk_Office_Tasks_Preview'),
    path('Desk_Office_Tasks_Remove/<str:pk>/', master_views.Desk_Office_Tasks_Remove,name='Desk_Office_Tasks_Remove'),
    # path('Desk_Office_Tasks/<str:pk>/', master_views.Desk_Office_Tasks,name='Desk_Office_Tasks'),

    path('Shop_Users/', master_views.Shop_Users,name='Shop_Users'),
    path('Shop_Users_Tasks_Preview/<str:pk>/', master_views.Shop_Users_Tasks_Preview,name='Shop_Users_Tasks_Preview'),
    path('Shop_Users_Tasks_Remove/<str:pk>/', master_views.Shop_Users_Tasks_Remove,name='Shop_Users_Tasks_Remove'),
    path('Shop_Tasks/<str:pk>/', master_views.Shop_Tasks,name='Shop_Tasks'),


    # path('system_reset/', master_views.system_reset,name='system_reset'),

    path('export_User_Task_xls/', master_views.export_User_Task_xls,name='export_User_Task_xls'),
   
    path('Users_Task_Add_Category_load/', master_views.Users_Task_Add_Category_load,name='Users_Task_Add_Category_load'),
    path('Users_Task_Add/<str:pk>/', master_views.Users_Task_Add,name='Users_Task_Add'),
    path('Users_Task_Edit/<str:pk>/', master_views.Users_Task_Edit,name='Users_Task_Edit'),
    path('Users_Task_Delete/<str:pk>/', master_views.Users_Task_Delete,name='Users_Task_Delete'),

    path('Invoice_Title/', master_views.Invoice_Title,name='Invoice_Title'),


    path('Executive_Positions_add/', master_views.Executive_Positions_add,name='Executive_Positions_add'),
    path('Executive_Positions_Delete/<str:pk>/', master_views.Executive_Positions_Delete,name='Executive_Positions_Delete'),

    path('Executive_add/', master_views.Executive_add,name='Executive_add'),
    path('Executive_Member_Select/<str:pk>/', master_views.Executive_Member_Select,name='Executive_Member_Select'),
    path('Executive_Member_Remove/<str:pk>/', master_views.Executive_Member_Remove,name='Executive_Member_Remove'),

    path('Executive_add_Existing/', master_views.Executive_add_Existing,name='Executive_add_Existing'),
    path('Executive_add_Existing_Update/<str:pk>/', master_views.Executive_add_Existing_Update,name='Executive_add_Existing_Update'),


    path('Executive_Member_Manage/', master_views.Executive_Member_Manage,name='Executive_Member_Manage'),
    path('Executive_Member_Manage_Update/<str:pk>/', master_views.Executive_Member_Manage_Update,name='Executive_Member_Manage_Update'),


    path('add_staff/', master_views.add_staff,name='add_staff'),
    path('add_staff_delete/<str:pk>/', master_views.add_staff_delete,name='add_staff_delete'),
    path('add_staff_delete_1/<str:pk>/', master_views.add_staff_delete_1,name='add_staff_delete_1'),
    path('add_staff_manage/', master_views.add_staff_manage,name='add_staff_manage'),
    path('add_staff_manage_view/<str:pk>/', master_views.add_staff_manage_view,name='add_staff_manage_view'),

    path('super_user_add/', master_views.super_user_add,name='super_user_add'),
    path('super_user_manage/', master_views.super_user_manage,name='super_user_manage'),
    path('super_user_manage_view/<str:pk>/', master_views.super_user_manage_view,name='super_user_manage_view'),

    path('addExpiringDateInterval/', master_views.addExpiringDateInterval,name='addExpiringDateInterval'),

    path('addState/', master_views.addState,name='addState'),
    path('Manage_state/', master_views.Manage_state,name='Manage_state'),
    path('delete_state/<str:pk>/', master_views.delete_state,name='delete_state'),

    path('addNOKRelationships/', master_views.addNOKRelationships,name='addNOKRelationships'),
    path('Manage_NOKRelationships/', master_views.Manage_NOKRelationships,name='Manage_NOKRelationships'),
    path('Manage_NOKRelationships_Remove/<str:pk>/', master_views.Manage_NOKRelationships_Remove,name='Manage_NOKRelationships_Remove'),
    path('Manage_NOKRelationships_Max_No/', master_views.Manage_NOKRelationships_Max_No,name='Manage_NOKRelationships_Max_No'),
    path('Xmas_Savings_Default_Transfer_Account/', master_views.Xmas_Savings_Default_Transfer_Account,name='Xmas_Savings_Default_Transfer_Account'),
    path('Xmas_Savings_Transaction_Period/', master_views.Xmas_Savings_Transaction_Period,name='Xmas_Savings_Transaction_Period'),
    path('Xmas_Savings_Transaction_Period_Delete/<str:pk>/', master_views.Xmas_Savings_Transaction_Period_Delete,name='Xmas_Savings_Transaction_Period_Delete'),
    path('Manage_Product_Code/', master_views.Manage_Product_Code,name='Manage_Product_Code'),


    path('addDefaultPassword/', master_views.addDefaultPassword,name='addDefaultPassword'),
    # path('addTransactionStatus/', master_views.addTransactionStatus,name='addTransactionStatus'),
    # path('addProcessingStatus/', master_views.addProcessingStatus,name='addProcessingStatus'),
    # path('addReceiptStatus/', master_views.addReceiptStatus,name='addReceiptStatus'),

    # path('addMembershipStatus/', master_views.addMembershipStatus,name='addMembershipStatus'),

    path('addGender/', master_views.addGender,name='addGender'),
    path('Manage_Gender/', master_views.Manage_Gender,name='Manage_Gender'),
    path('Manage_Gender_Processing/<str:pk>/', master_views.Manage_Gender_Processing, name='Manage_Gender_Processing'),

    path('addTitles/', master_views.addTitles,name='addTitles'),
    path('Manage_Titles/', master_views.Manage_Titles,name='Manage_Titles'),
    path('Manage_Titles_Processing/<str:pk>/', master_views.Manage_Titles_Processing, name='Manage_Titles_Processing'),


    path('addSalaryInstitution/', master_views.addSalaryInstitution,name='addSalaryInstitution'),
    path('Manage_Salary_Institution/', master_views.Manage_Salary_Institution,name='Manage_Salary_Institution'),
    path('Manage_Salary_Institution_Processing/<str:pk>/', master_views.Manage_Salary_Institution_Processing, name='Manage_Salary_Institution_Processing'),


    path('addDepartments/', master_views.addDepartments,name='addDepartments'),
    path('Manage_Departments/', master_views.Manage_Departments,name='Manage_Departments'),
    path('Manage_Departments_Processing/<str:pk>/', master_views.Manage_Departments_Processing, name='Manage_Departments_Processing'),

    path('addBanks/', master_views.addBanks,name='addBanks'),
    path('Manage_Banks/', master_views.Manage_Banks,name='Manage_Banks'),
    path('Manage_Banks_Processing/<str:pk>/', master_views.Manage_Banks_Processing, name='Manage_Banks_Processing'),


    path('addLocations/', master_views.addLocations,name='addLocations'),
    path('Manage_Locations/', master_views.Manage_Locations,name='Manage_Locations'),
    path('Manage_Locations_Processing/<str:pk>/', master_views.Manage_Locations_Processing, name='Manage_Locations_Processing'),

    path('TransactionTypes_Sources_Manage/', master_views.TransactionTypes_Sources_Manage,name='TransactionTypes_Sources_Manage'),
    path('TransactionTypes_Sources_Manage_Process/<str:pk>/', master_views.TransactionTypes_Sources_Manage_Process, name='TransactionTypes_Sources_Manage_Process'),

    path('addTransactionTypes/', master_views.addTransactionTypes,name='addTransactionTypes'),
    path('addTransactionTypes_Remove/<str:pk>/', master_views.addTransactionTypes_Remove, name='addTransactionTypes_Remove'),
    path('TransactionTypes_Manage_Load/', master_views.TransactionTypes_Manage_Load,name='TransactionTypes_Manage_Load'),
    path('TransactionTypes_Ranking_Load/', master_views.TransactionTypes_Ranking_Load,name='TransactionTypes_Ranking_Load'),
    path('TransactionTypes_Ranking_Update/<str:pk>/', master_views.TransactionTypes_Ranking_Update, name='TransactionTypes_Ranking_Update'),

    path('TransactionTypes_Update/<str:pk>/', master_views.TransactionTypes_Update, name='TransactionTypes_Update'),
    path('FormAutoPrint_Settings/', master_views.FormAutoPrint_Settings,name='FormAutoPrint_Settings'),
    path('FormAutoPrint_SettingsUpdate/<str:pk>/', master_views.FormAutoPrint_SettingsUpdate, name='FormAutoPrint_SettingsUpdate'),

    path('MembersCompulsorySavings/', master_views.MembersCompulsorySavings,name='MembersCompulsorySavings'),
    path('MembersCompulsorySavings_delete/<str:pk>/', master_views.MembersCompulsorySavings_delete, name='MembersCompulsorySavings_delete'),

    path('SharesUnits_add/', master_views.SharesUnits_add,name='SharesUnits_add'),
    path('SharesUnits_Max_Min_Values/', master_views.SharesUnits_Max_Min_Values,name='SharesUnits_Max_Min_Values'),
    path('AddShares_Configurations/', master_views.AddShares_Configurations,name='AddShares_Configurations'),
    path('addWelfare_Configurations/', master_views.addWelfare_Configurations,name='addWelfare_Configurations'),

    path('Shares_Deduction_savings/', master_views.Shares_Deduction_savings,name='Shares_Deduction_savings'),
    path('Shares_Deduction_savings_remove/<str:pk>/', master_views.Shares_Deduction_savings_remove, name='Shares_Deduction_savings_remove'),

    path('CooperativeBankAccounts_add/', master_views.CooperativeBankAccounts_add,name='CooperativeBankAccounts_add'),
    path('CooperativeBankAccounts_Remove/<str:pk>/', master_views.CooperativeBankAccounts_Remove, name='CooperativeBankAccounts_Remove'),
    path('CooperativeBankAccounts_Update/<str:pk>/', master_views.CooperativeBankAccounts_Update, name='CooperativeBankAccounts_Update'),

    path('BankAccounts_Designation_List_Load/', master_views.BankAccounts_Designation_List_Load,name='BankAccounts_Designation_List_Load'),
    path('BankAccounts_Designation_Process/<str:pk>/', master_views.BankAccounts_Designation_Process, name='BankAccounts_Designation_Process'),

    path('Savings_Manager_load/', master_views.Savings_Manager_load,name='Savings_Manager_load'),
    path('Savings_Manager_Update/<str:pk>/', master_views.Savings_Manager_Update, name='Savings_Manager_Update'),

    path('loan_category_settings/', master_views.loan_category_settings,name='loan_category_settings'),
    path('loan_settings_load/', master_views.loan_settings_load,name='loan_settings_load'),
    path('loan_settings_details_load/<str:pk>/', master_views.loan_settings_details_load,name='loan_settings_details_load'),

    path('loan_based_savings_update/', master_views.loan_based_savings_update,name='loan_based_savings_update'),
    path('loan_duration_update/<str:pk>/', master_views.loan_duration_update,name='loan_duration_update'),
    path('loan_category_update/<str:pk>/', master_views.loan_category_update,name='loan_category_update'),
    path('loan_guarantors_update/<str:pk>/', master_views.loan_guarantors_update,name='loan_guarantors_update'),
    path('loan_guarantors_gross_pay_update/<str:pk>/', master_views.loan_guarantors_gross_pay_update,name='loan_guarantors_gross_pay_update'),
    path('loan_savings_based_Rate_update/<str:pk>/', master_views.loan_savings_based_Rate_update,name='loan_savings_based_Rate_update'),
    path('loan_savings_based_update/<str:pk>/', master_views.loan_savings_based_update,name='loan_savings_based_update'),
    path('default_admin_charges_update/<str:pk>/', master_views.default_admin_charges_update,name='default_admin_charges_update'),
    path('MultipleLoanStatus_update/<str:pk>/', master_views.MultipleLoanStatus_update,name='MultipleLoanStatus_update'),
    path('auto_stop_savings_update/<str:pk>/', master_views.auto_stop_savings_update,name='auto_stop_savings_update'),
    path('loan_name_update/<str:pk>/', master_views.loan_name_update,name='loan_name_update'),
    path('loan_interest_rate_update/<str:pk>/', master_views.loan_interest_rate_update,name='loan_interest_rate_update'),
    path('loan_interest_deduction_soucrces_update/<str:pk>/', master_views.loan_interest_deduction_soucrces_update,name='loan_interest_deduction_soucrces_update'),
    path('loan_maximum_amount_update/<str:pk>/', master_views.loan_maximum_amount_update,name='loan_maximum_amount_update'),
    # path('loan_rank_update_update/<str:pk>/', master_views.loan_rank_update_update,name='loan_rank_update_update'),
    path('loan_admin_charges_rate_update/<str:pk>/', master_views.loan_admin_charges_rate_update,name='loan_admin_charges_rate_update'),
    path('loan_admin_charges_update/<str:pk>/', master_views.loan_admin_charges_update,name='loan_admin_charges_update'),
    path('loan_admin_charges_minimum_update/<str:pk>/', master_views.loan_admin_charges_minimum_update,name='loan_admin_charges_minimum_update'),
    path('loan_salary_relationship_update/<str:pk>/', master_views.loan_salary_relationship_update,name='loan_salary_relationship_update'),
    path('loan_loan_age_update/<str:pk>/', master_views.loan_loan_age_update,name='loan_loan_age_update'),
    path('receipt_types_settings/<str:pk>/', master_views.receipt_types_settings,name='receipt_types_settings'),

    # path('Customized_loan_duration_update/<str:pk>/', master_views.Customized_loan_duration_update,name='Customized_loan_duration_update'),
    # path('Customized_loan_category_update/<str:pk>/', master_views.Customized_loan_category_update,name='Customized_loan_category_update'),
    # path('Customized_loan_guarantors_update/<str:pk>/', master_views.Customized_loan_guarantors_update,name='Customized_loan_guarantors_update'),

    # path('Customized_loan_name_update/<str:pk>/', master_views.Customized_loan_name_update,name='Customized_loan_name_update'),
    # path('Customized_loan_interest_rate_update/<str:pk>/', master_views.Customized_loan_interest_rate_update,name='Customized_loan_interest_rate_update'),
    # path('Customized_loan_rank_update_update/<str:pk>/', master_views.Customized_loan_rank_update_update,name='Customized_loan_rank_update_update'),
    # path('Customized_loan_admin_charges_rate_update/<str:pk>/', master_views.Customized_loan_admin_charges_rate_update,name='Customized_loan_admin_charges_rate_update'),
    # path('Customized_loan_admin_charges_update/<str:pk>/', master_views.Customized_loan_admin_charges_update,name='Customized_loan_admin_charges_update'),

    # path('Customized_loan_loan_age_update/<str:pk>/', master_views.Customized_loan_loan_age_update,name='Customized_loan_loan_age_update'),
    # path('Customized_loan_form_print_update/<str:pk>/', master_views.Customized_loan_form_print_update,name='Customized_loan_form_print_update'),
    # path('Customized_receipt_type_update/<str:pk>/', master_views.Customized_receipt_type_update,name='Customized_receipt_type_update'),

    path('Commodity_SubCategeory_list_load/', master_views.Commodity_SubCategeory_list_load,name='Commodity_SubCategeory_list_load'),
    path('loan_settings_non_monetary_Sub_Categories_load/<str:pk>/', master_views.loan_settings_non_monetary_Sub_Categories_load,name='loan_settings_non_monetary_Sub_Categories_load'),
    path('loan_settings_non_monetary_Sub_Categories_Preview/<str:pk>/', master_views.loan_settings_non_monetary_Sub_Categories_Preview,name='loan_settings_non_monetary_Sub_Categories_Preview'),
    path('loan_settings_non_monetary_Sub_Categories_Update/<str:pk>/', master_views.loan_settings_non_monetary_Sub_Categories_Update,name='loan_settings_non_monetary_Sub_Categories_Update'),

    path('loan_settings_non_monetary_list_load/', master_views.loan_settings_non_monetary_list_load,name='loan_settings_non_monetary_list_load'),
    path('loan_settings_non_monetary_Categories_load/<str:pk>/', master_views.loan_settings_non_monetary_Categories_load,name='loan_settings_non_monetary_Categories_load'),

    path('loan_settings_non_monetary_settings/<str:pk>/', master_views.loan_settings_non_monetary_settings,name='loan_settings_non_monetary_settings'),
    path('non_monetary_oan_guarantors_update/<str:pk>/', master_views.non_monetary_oan_guarantors_update,name='non_monetary_oan_guarantors_update'),
    path('non_monetary_oan_guarantors_gross_pay_rating_update/<str:pk>/', master_views.non_monetary_oan_guarantors_gross_pay_rating_update,name='non_monetary_oan_guarantors_gross_pay_rating_update'),
    path('Non_Monetary_MultipleLoanStatus_update/<str:pk>/', master_views.Non_Monetary_MultipleLoanStatus_update,name='Non_Monetary_MultipleLoanStatus_update'),
    path('non_monetary_loan_duration_update/<str:pk>/', master_views.non_monetary_loan_duration_update,name='non_monetary_loan_duration_update'),
    path('non_monetary_loan_name_update/<str:pk>/', master_views.non_monetary_loan_name_update,name='non_monetary_loan_name_update'),
    path('non_monetary_loan_interest_rate_update/<str:pk>/', master_views.non_monetary_loan_interest_rate_update,name='non_monetary_loan_interest_rate_update'),
    path('non_monetary_loan_admin_charges_rate_update/<str:pk>/', master_views.non_monetary_loan_admin_charges_rate_update,name='non_monetary_loan_admin_charges_rate_update'),
    path('non_monetary_loan_admin_charges_update/<str:pk>/', master_views.non_monetary_loan_admin_charges_update,name='non_monetary_loan_admin_charges_update'),
    path('non_monetary_loan_loan_age_update/<str:pk>/', master_views.non_monetary_loan_loan_age_update,name='non_monetary_loan_loan_age_update'),
    path('non_monetary_loan_receipt_type_update/<str:pk>/', master_views.non_monetary_loan_receipt_type_update,name='non_monetary_loan_receipt_type_update'),
    # path('non_monetary_loan_form_print_update/<str:pk>/', master_views.non_monetary_loan_form_print_update,name='non_monetary_loan_form_print_update'),


    path('Commodity_Products_Add_Transactions_Load/', master_views.Commodity_Products_Add_Transactions_Load,name='Commodity_Products_Add_Transactions_Load'),
    path('Commodity_Products_Add_Transactions_Categories_Load/<str:pk>/', master_views.Commodity_Products_Add_Transactions_Categories_Load,name='Commodity_Products_Add_Transactions_Categories_Load'),

    path('Commodity_Products_add/<str:pk>/', master_views.Commodity_Products_add,name='Commodity_Products_add'),
    path('Manage_Commodity_Categories_Delete/<str:pk>/', master_views.Manage_Commodity_Categories_Delete,name='Manage_Commodity_Categories_Delete'),
    path('Manage_Commodity_Categories_Title_Update/<str:pk>/', master_views.Manage_Commodity_Categories_Title_Update,name='Manage_Commodity_Categories_Title_Update'),

    path('Commodity_Transaction_Period/', master_views.Commodity_Transaction_Period,name='Commodity_Transaction_Period'),
    path('Commodity_Transaction_Period_Delete/<str:pk>/', master_views.Commodity_Transaction_Period_Delete,name='Commodity_Transaction_Period_Delete'),

    path('Commodity_Transaction_Period_Batch/', master_views.Commodity_Transaction_Period_Batch,name='Commodity_Transaction_Period_Batch'),
    path('Commodity_Transaction_Period_Batch_Delete/<str:pk>/', master_views.Commodity_Transaction_Period_Batch_Delete,name='Commodity_Transaction_Period_Batch_Delete'),


    path('addCommodityCategory/', master_views.addCommodityCategory,name='addCommodityCategory'),
    path('addCommodityCategorySub/<str:pk>/', master_views.addCommodityCategorySub,name='addCommodityCategorySub'),
    path('Manage_Commodity_Sub_Categories_Delete/<str:pk>/', master_views.Manage_Commodity_Sub_Categories_Delete,name='Manage_Commodity_Sub_Categories_Delete'),

    path('Manage_Commodity_Categories_Core_properties_Transactions_Load/', master_views.Manage_Commodity_Categories_Core_properties_Transactions_Load,name='Manage_Commodity_Categories_Core_properties_Transactions_Load'),
    path('Manage_Commodity_Categories_Core_Values/<str:pk>/', master_views.Manage_Commodity_Categories_Core_Values,name='Manage_Commodity_Categories_Core_Values'),

    path('Manage_Commodity_Categories_Peripherals_Transactions_Load/', master_views.Manage_Commodity_Categories_Peripherals_Transactions_Load,name='Manage_Commodity_Categories_Peripherals_Transactions_Load'),
    path('Manage_Commodity_Categories_Peripherals/<str:pk>/', master_views.Manage_Commodity_Categories_Peripherals,name='Manage_Commodity_Categories_Peripherals'),



    # path('Customized_Commodity_Loan_Settings/', master_views.Customized_Commodity_Loan_Settings,name='Customized_Commodity_Loan_Settings'),

    path('membership_price_settings_load/', master_views.membership_price_settings_load,name='membership_price_settings_load'),
    path('AutoReceipt_Setup/', master_views.AutoReceipt_Setup,name='AutoReceipt_Setup'),
    path('receipt_manager/', master_views.receipt_manager,name='receipt_manager'),
    path('receipt_manager_shop/', master_views.receipt_manager_shop,name='receipt_manager_shop'),
    path('Members_IdManager/', master_views.Members_IdManager,name='Members_IdManager'),
    path('TransactionEnabler_Add/', master_views.TransactionEnabler_Add,name='TransactionEnabler_Add'),
    path('TransactionEnabler_Manage/', master_views.TransactionEnabler_Manage,name='TransactionEnabler_Manage'),
    path('Loan_Number_Manager/', master_views.Loan_Number_Manager,name='Loan_Number_Manager'),
   

    path('FailedLoanPenalty_Duration_Manager/', master_views.FailedLoanPenalty_Duration_Manager,name='FailedLoanPenalty_Duration_Manager'),
    

    path('FailedLoanPenalty_Manager/', master_views.FailedLoanPenalty_Manager,name='FailedLoanPenalty_Manager'),
    path('TransactionEnabler_delete/<str:pk>/', master_views.TransactionEnabler_delete,name='TransactionEnabler_delete'),
    path('TransactionEnabler_enabler/<str:pk>/', master_views.TransactionEnabler_enabler,name='TransactionEnabler_enabler'),

    path('check_email_exist/', master_views.check_email_exist,name='check_email_exist'),
    path('check_username_exist/', master_views.check_username_exist,name='check_username_exist'),
    path('check_phone_no_exist/', master_views.check_phone_no_exist,name='check_phone_no_exist'),

    path('WithdrawalController/', master_views.WithdrawalController,name='WithdrawalController'),
    path('WithdrawalController_add/', master_views.WithdrawalController_add,name='WithdrawalController_add'),
    path('WithdrawalController_View/<str:pk>/', master_views.WithdrawalController_View,name='WithdrawalController_View'),
    path('WithdrawalController_Process/<str:pk>/', master_views.WithdrawalController_Process,name='WithdrawalController_Process'),

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
    path('Product_UnLinking_Process/<str:comp_pk>/<str:pk>/<str:period_pk>/<str:batch_pk>/<str:transaction_pk>/', master_views.Product_UnLinking_Process,name='Product_UnLinking_Process'),

    path('Product_Settings_Period_Load/', master_views.Product_Settings_Period_Load,name='Product_Settings_Period_Load'),
    path('Product_Price_Settings_Company_Load/<str:period_obj>/<str:batch_obj>/<str:transaction_obj>/', master_views.Product_Price_Settings_Company_Load,name='Product_Price_Settings_Company_Load'),
    path('Product_Price_Settings_details/<str:pk>/<str:period_obj>/<str:batch_obj>/<str:transaction_obj>/', master_views.Product_Price_Settings_details,name='Product_Price_Settings_details'),
    path('Product_Price_Settings_Update/<str:comp_pk>/<str:pk>/', master_views.Product_Price_Settings_Update,name='Product_Price_Settings_Update'),

    path('Product_Duration_Settings_Period_Load/', master_views.Product_Duration_Settings_Period_Load,name='Product_Duration_Settings_Period_Load'),
    path('Product_Duration_Settings_Service_Load/<str:period_obj>/<str:batch_obj>/<str:transaction_obj>/', master_views.Product_Duration_Settings_Service_Load,name='Product_Duration_Settings_Service_Load'),
    path('Product_Duration_Settings_Service_Delete/<str:pk>/<str:period_obj>/<str:batch_obj>/<str:transaction_obj>/', master_views.Product_Duration_Settings_Service_Delete,name='Product_Duration_Settings_Service_Delete'),
    ###########################################
    ################## PRESIDENT################
    ############################################

    path('membership_request_approvals_list_load/', master_views.membership_request_approvals_list_load,name='membership_request_approvals_list_load'),
    path('membership_request_approval_info/<str:pk>/', master_views.membership_request_approval_info,name='membership_request_approval_info'),

    path('membership_request_approval_comment_save/<str:pk>/', master_views.membership_request_approval_comment_save,name='membership_request_approval_comment_save'),
    path('membership_request_approval_info_delete/<str:pk>/', master_views.membership_request_approval_info_delete,name='membership_request_approval_info_delete'),

    path('membership_request_approval_attachment_save/<str:pk>/', master_views.membership_request_approval_attachment_save,name='membership_request_approval_attachment_save'),
    path('membership_request_approval_attachment_delete/<str:pk>/', master_views.membership_request_approval_attachment_delete,name='membership_request_approval_attachment_delete'),

    path('MemberShipRequest_approval_submit/<str:pk>/', master_views.MemberShipRequest_approval_submit,name='MemberShipRequest_approval_submit'),

    path('loan_request_approval_period_load/', master_views.loan_request_approval_period_load,name='loan_request_approval_period_load'),
    path('Loan_request_approval_details/<str:pk>/', master_views.Loan_request_approval_details,name='Loan_request_approval_details'),

    path('Loan_application_approval_period_load/', master_views.Loan_application_approval_period_load,name='Loan_application_approval_period_load'),
    path('Loan_application_approval_details/<str:pk>/', master_views.Loan_application_approval_details,name='Loan_application_approval_details'),

    path('Loan_unscheduling_approval_load/', master_views.Loan_unscheduling_approval_load,name='Loan_unscheduling_approval_load'),
    path('Loan_unscheduling_approval_preview/<str:pk>/', master_views.Loan_unscheduling_approval_preview,name='Loan_unscheduling_approval_preview'),



    path('membership_commodity_loan_Period_approval_transaction_load/', master_views.membership_commodity_loan_Period_approval_transaction_load,name='membership_commodity_loan_Period_approval_transaction_load'),
    path('membership_commodity_loan_Period_approval_transaction_details/<str:pk>/', master_views.membership_commodity_loan_Period_approval_transaction_details,name='membership_commodity_loan_Period_approval_transaction_details'),



    path('savings_cash_withdrawal_Certitication_list_load/', master_views.savings_cash_withdrawal_Certitication_list_load,name='savings_cash_withdrawal_Certitication_list_load'),


    path('savings_cash_withdrawal_list_load/', master_views.savings_cash_withdrawal_list_load,name='savings_cash_withdrawal_list_load'),
    path('savings_cash_withdrawal_preview/<str:pk>/', master_views.savings_cash_withdrawal_preview,name='savings_cash_withdrawal_preview'),

    path('members_exclusiveness_list_load/', master_views.members_exclusiveness_list_load,name='members_exclusiveness_list_load'),
    path('members_exclusiveness_process/<str:pk>/', master_views.members_exclusiveness_process,name='members_exclusiveness_process'),

    path('Shares_Purchase_Request_Approval_List_Load/', master_views.Shares_Purchase_Request_Approval_List_Load,name='Shares_Purchase_Request_Approval_List_Load'),
    path('Shares_Purchase_Request_Approval_Processed/<str:pk>/', master_views.Shares_Purchase_Request_Approval_Processed,name='Shares_Purchase_Request_Approval_Processed'),

    path('Cash_Withdrawal_Request_Approval_List_Load/', master_views.Cash_Withdrawal_Request_Approval_List_Load,name='Cash_Withdrawal_Request_Approval_List_Load'),
    path('Cash_Withdrawal_Request_Approval_Processing/<str:pk>/', master_views.Cash_Withdrawal_Request_Approval_Processing,name='Cash_Withdrawal_Request_Approval_Processing'),

    ###############################################
    ############################ SECRETARY##########
    ################################################

    # path('Loan_request_certification_period_load/', master_views.Loan_request_certification_period_load,name='Loan_request_certification_period_load'),
    # path('Loan_request_certification_details/<str:pk>/', master_views.Loan_request_certification_details,name='Loan_request_certification_details'),

    # path('Loan_application_certification_period_load/', master_views.Loan_application_certification_period_load,name='Loan_application_certification_period_load'),
    # path('Loan_application_certification_details/<str:pk>/', master_views.Loan_application_certification_details,name='Loan_application_certification_details'),

    # path('membership_commodity_loan_Period_certification_transaction_load/', master_views.membership_commodity_loan_Period_certification_transaction_load,name='membership_commodity_loan_Period_certification_transaction_load'),
    # path('membership_commodity_loan_Period_certification_transaction_details/<str:pk>/', master_views.membership_commodity_loan_Period_certification_transaction_details,name='membership_commodity_loan_Period_certification_transaction_details'),

    path('Termination_Loan_Allowed_load/', master_views.Termination_Loan_Allowed_load,name='Termination_Loan_Allowed_load'),
    path('Termination_Loan_Allowed_Remove/<str:pk>/', master_views.Termination_Loan_Allowed_Remove,name='Termination_Loan_Allowed_Remove'),

    path('membership_termination_Duration_Manager_Transaction_Load/', master_views.membership_termination_Duration_Manager_Transaction_Load,name='membership_termination_Duration_Manager_Transaction_Load'),
    path('membership_termination_Duration_Manager/<str:pk>/', master_views.membership_termination_Duration_Manager,name='membership_termination_Duration_Manager'),


    path('membership_termination_Request_Approval_List_Load/', master_views.membership_termination_Request_Approval_List_Load,name='membership_termination_Request_Approval_List_Load'),
    path('membership_termination_Request_Approval_Process/<str:pk>/', master_views.membership_termination_Request_Approval_Process,name='membership_termination_Request_Approval_Process'),

    path('membership_termination_maturity_date_exception_Approval_List_Load/', master_views.membership_termination_maturity_date_exception_Approval_List_Load,name='membership_termination_maturity_date_exception_Approval_List_Load'),
    path('membership_termination_maturity_date_exception_Approval_Preview/<str:pk>/', master_views.membership_termination_maturity_date_exception_Approval_Preview,name='membership_termination_maturity_date_exception_Approval_Preview'),

    path('membership_termination_Disbursement_Approval_List_Load/', master_views.membership_termination_Disbursement_Approval_List_Load,name='membership_termination_Disbursement_Approval_List_Load'),
    path('membership_termination_Disbursement_Approval_Preview/<str:pk>/', master_views.membership_termination_Disbursement_Approval_Preview,name='membership_termination_Disbursement_Approval_Preview'),




    ###########################################################################
    ########################### RENTAL DEPARTMENT ######################################
    ###########################################################################
    path('RentalMainCategories_add/', master_views.RentalMainCategories_add,name='RentalMainCategories_add'),
    path('RentalMainCategories_delete/<str:pk>/', master_views.RentalMainCategories_delete,name='RentalMainCategories_delete'),


    path('RentalProducts_add/', master_views.RentalProducts_add,name='RentalProducts_add'),
    path('RentalProducts_delete/<str:pk>/', master_views.RentalProducts_delete,name='RentalProducts_delete'),

    path('Rental_Price_Settings/', master_views.Rental_Price_Settings,name='Rental_Price_Settings'),
    path('Rental_Price_Settings_delete/<str:pk>/', master_views.Rental_Price_Settings_delete,name='Rental_Price_Settings_delete'),





    ################# MASTER ADMIN REPORT ##################################
    path('transaction_views_ranked/', master_views.transaction_views_ranked,name='transaction_views_ranked'),
    path('List_of_Users/', master_views.List_of_Users,name='List_of_Users'),

    ###########################################################################
    ########################## DESK OFFICER HOME ###############################
    ###########################################################################
    # path('render_pdf_view/', deskofficer_views.render_pdf_view,name='render_pdf_view'),

    path('deskofficer_home/', deskofficer_views.deskofficer_home,name='deskofficer_home'),

    path('Useraccount_manager/', deskofficer_views.Useraccount_manager,name='Useraccount_manager'),

    path('desk_basic_form/', deskofficer_views.desk_basic_form,name='desk_basic_form'),
    path('desk_advanced_form/', deskofficer_views.desk_advanced_form,name='desk_advanced_form'),
    path('desk_basic_table/', deskofficer_views.desk_basic_table,name='desk_basic_table'),
    path('desk_datatable_table/', deskofficer_views.desk_datatable_table,name='desk_datatable_table'),
    # path('desk_form_validation/', deskofficer_views.desk_form_validation,name='desk_form_validation'),

    path('membership_request/', deskofficer_views.membership_request,name='membership_request'),
    path('membership_request_complete_search/', deskofficer_views.membership_request_complete_search,name='membership_request_complete_search'),
    path('membership_request_complete_load/', deskofficer_views.membership_request_complete_load,name='membership_request_complete_load'),
    path('membership_request_additional_info/<str:pk>/', deskofficer_views.membership_request_additional_info,name='membership_request_additional_info'),
    path('membership_request_additional_info_update/<str:pk>/', deskofficer_views.membership_request_additional_info_update,name='membership_request_additional_info_update'),

    path('membership_request_additional_info_save/<str:pk>/', deskofficer_views.membership_request_additional_info_save,name='membership_request_additional_info_save'),
    path('membership_request_additional_info_delete_confirm/<str:pk>/<str:return_pk>/', deskofficer_views.membership_request_additional_info_delete_confirm,name='membership_request_additional_info_delete_confirm'),
    path('membership_request_additional_info_delete/<str:pk>/<str:return_pk>/', deskofficer_views.membership_request_additional_info_delete,name='membership_request_additional_info_delete'),

    path('MemberShipRequestAdditionalAttachment_save/<str:pk>/', deskofficer_views.MemberShipRequestAdditionalAttachment_save,name='MemberShipRequestAdditionalAttachment_save'),
    path('MemberShipRequestAdditionalAttachment_info_delete_confirm/<str:pk>/<str:return_pk>/', deskofficer_views.MemberShipRequestAdditionalAttachment_info_delete_confirm,name='MemberShipRequestAdditionalAttachment_info_delete_confirm'),
    path('MemberShipRequestAdditionalAttachment_info_delete/<str:pk>/<str:return_pk>/', deskofficer_views.MemberShipRequestAdditionalAttachment_info_delete,name='MemberShipRequestAdditionalAttachment_info_delete'),


    path('MemberShipRequest_Delete_confirmation/<str:pk>/', deskofficer_views.MemberShipRequest_Delete_confirmation,name='MemberShipRequest_Delete_confirmation'),
    path('MemberShipRequest_Delete/<str:pk>/', deskofficer_views.MemberShipRequest_Delete,name='MemberShipRequest_Delete'),
    path('MemberShipRequest_submit/<str:pk>/', deskofficer_views.MemberShipRequest_submit,name='MemberShipRequest_submit'),

    path('membership_form_sales_Search/', deskofficer_views.membership_form_sales_Search,name='membership_form_sales_Search'),
    path('membership_form_sales_list_load/', deskofficer_views.membership_form_sales_list_load,name='membership_form_sales_list_load'),
    path('membership_form_sales_preview/<str:pk>/', deskofficer_views.membership_form_sales_preview,name='membership_form_sales_preview'),
    path('membership_form_sales_issue/<str:pk>/', deskofficer_views.membership_form_sales_issue,name='membership_form_sales_issue'),
    path('membership_form_sales_validation/<str:pk>/', deskofficer_views.membership_form_sales_validation,name='membership_form_sales_validation'),



    path('Membership_Front_Form_Print/<str:pk>/', deskofficer_views.Membership_Front_Form_Print,name='Membership_Front_Form_Print'),
    path('Membership_Deduction_Order_Form_Print/<str:pk>/', deskofficer_views.Membership_Deduction_Order_Form_Print,name='Membership_Deduction_Order_Form_Print'),

    # path('member_pdf/', deskofficer_views.member_pdf,name='member_pdf'),



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



    path('membership_registration_applicant_search/', deskofficer_views.membership_registration_applicant_search,name='membership_registration_applicant_search'),
    path('membership_registration_applicant_list_load/', deskofficer_views.membership_registration_applicant_list_load,name='membership_registration_applicant_list_load'),

    path('membership_registration_register/<str:pk>/', deskofficer_views.membership_registration_register,name='membership_registration_register'),
    path('membership_registration_register_confirmation/<str:pk>/', deskofficer_views.membership_registration_register_confirmation,name='membership_registration_register_confirmation'),
    # path('Registerd_Members_Form_Print/<str:pk>/', deskofficer_views.Registerd_Members_Form_Print,name='Registerd_Members_Form_Print'),

    path('Members_Account_Creation_Search/', deskofficer_views.Members_Account_Creation_Search,name='Members_Account_Creation_Search'),
    path('Members_Account_Creation_list_load/', deskofficer_views.Members_Account_Creation_list_load,name='Members_Account_Creation_list_load'),
    path('Members_Account_Creation_preview_all/', deskofficer_views.Members_Account_Creation_preview_all,name='Members_Account_Creation_preview_all'),
    path('Members_Account_Creation_preview/<str:pk>/', deskofficer_views.Members_Account_Creation_preview,name='Members_Account_Creation_preview'),
    path('Members_Account_Creation_process_Delete/<str:pk>/', deskofficer_views.Members_Account_Creation_process_Delete,name='Members_Account_Creation_process_Delete'),
    path('Members_Account_Creation_process/<str:pk>/', deskofficer_views.Members_Account_Creation_process,name='Members_Account_Creation_process'),

    path('Members_Account_Creation_preview_remove_duplicate/', deskofficer_views.Members_Account_Creation_preview_remove_duplicate,name='Members_Account_Creation_preview_remove_duplicate'),
    
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

    path('standing_order_reactivate_account_search/', deskofficer_views.standing_order_reactivate_account_search,name='standing_order_reactivate_account_search'),
    path('standing_order_reactivate_account_list_load/', deskofficer_views.standing_order_reactivate_account_list_load,name='standing_order_reactivate_account_list_load'),
    path('standing_order_reactivate_account/<str:pk>/', deskofficer_views.standing_order_reactivate_account,name='standing_order_reactivate_account'),
    path('standing_order_drop_account/<str:pk>/', deskofficer_views.standing_order_drop_account,name='standing_order_drop_account'),


    path('Transaction_adjustment_search/', deskofficer_views.Transaction_adjustment_search,name='Transaction_adjustment_search'),
    path('Transaction_adjustment_List_load/', deskofficer_views.Transaction_adjustment_List_load,name='Transaction_adjustment_List_load'),
    path('Transaction_adjustment_Transactions_load/<str:pk>/', deskofficer_views.Transaction_adjustment_Transactions_load,name='Transaction_adjustment_Transactions_load'),
    path('Transaction_adjustment_Transactions_Accounts_load/<str:pk>/<str:return_pk>/', deskofficer_views.Transaction_adjustment_Transactions_Accounts_load,name='Transaction_adjustment_Transactions_Accounts_load'),
    path('Transaction_adjustment_Transactions_Accounts_Remove/<str:pk>/', deskofficer_views.Transaction_adjustment_Transactions_Accounts_Remove,name='Transaction_adjustment_Transactions_Accounts_Remove'),

    path('Transaction_Adjustment_Approved_List_Load/', deskofficer_views.Transaction_Adjustment_Approved_List_Load,name='Transaction_Adjustment_Approved_List_Load'),
    path('Transaction_Adjustment_Approved_Processed/<str:pk>/', deskofficer_views.Transaction_Adjustment_Approved_Processed,name='Transaction_Adjustment_Approved_Processed'),

    path('Transaction_adjustment_history_Search/', deskofficer_views.Transaction_adjustment_history_Search,name='Transaction_adjustment_history_Search'),
    path('Transaction_adjustment_history_List_load/', deskofficer_views.Transaction_adjustment_history_List_load,name='Transaction_adjustment_history_List_load'),
    path('TransactionAjustmentHistory_Transaction_Load/<str:pk>/', deskofficer_views.TransactionAjustmentHistory_Transaction_Load,name='TransactionAjustmentHistory_Transaction_Load'),
    path('TransactionAjustmentHistory_details/<str:pk>/', deskofficer_views.TransactionAjustmentHistory_details,name='TransactionAjustmentHistory_details'),

    path('Standing_Order_Suspension_search/', deskofficer_views.Standing_Order_Suspension_search,name='Standing_Order_Suspension_search'),
    path('Standing_Order_Suspension_List_load/', deskofficer_views.Standing_Order_Suspension_List_load,name='Standing_Order_Suspension_List_load'),
    path('Standing_Order_Suspension_Transaction_Load/<str:pk>/', deskofficer_views.Standing_Order_Suspension_Transaction_Load,name='Standing_Order_Suspension_Transaction_Load'),
    path('Standing_Order_Suspension_Transaction_Delete/<str:pk>/', deskofficer_views.Standing_Order_Suspension_Transaction_Delete,name='Standing_Order_Suspension_Transaction_Delete'),

    path('Standing_Order_Suspension_Transaction_Approval_Load/', deskofficer_views.Standing_Order_Suspension_Transaction_Approval_Load,name='Standing_Order_Suspension_Transaction_Approval_Load'),
    path('Standing_Order_Suspension_Transaction_Approvals_Load_Details/<str:pk>/', deskofficer_views.Standing_Order_Suspension_Transaction_Approvals_Load_Details,name='Standing_Order_Suspension_Transaction_Approvals_Load_Details'),

    path('Standing_Order_Suspension_Transaction_Approval_Processing_Load/', deskofficer_views.Standing_Order_Suspension_Transaction_Approval_Processing_Load,name='Standing_Order_Suspension_Transaction_Approval_Processing_Load'),
    path('Standing_Order_Suspension_Transaction_Approval_Processing/<str:pk>/', deskofficer_views.Standing_Order_Suspension_Transaction_Approval_Processing,name='Standing_Order_Suspension_Transaction_Approval_Processing'),

    path('Standing_Order_Suspension_Transaction_Releasing_search/', deskofficer_views.Standing_Order_Suspension_Transaction_Releasing_search,name='Standing_Order_Suspension_Transaction_Releasing_search'),
    path('Standing_Order_Suspension_Transaction_Releasing_list_load/', deskofficer_views.Standing_Order_Suspension_Transaction_Releasing_list_load,name='Standing_Order_Suspension_Transaction_Releasing_list_load'),
    path('Standing_Order_Suspension_Transactions_Releasing_Details/<str:pk>/', deskofficer_views.Standing_Order_Suspension_Transactions_Releasing_Details,name='Standing_Order_Suspension_Transactions_Releasing_Details'),

    path('Standing_Order_Suspension_Transaction_Releasing_Approval_Load/', deskofficer_views.Standing_Order_Suspension_Transaction_Releasing_Approval_Load,name='Standing_Order_Suspension_Transaction_Releasing_Approval_Load'),
    path('Standing_Order_Suspension_Transaction_Releasing_Approval_Details/<str:pk>/', deskofficer_views.Standing_Order_Suspension_Transaction_Releasing_Approval_Details,name='Standing_Order_Suspension_Transaction_Releasing_Approval_Details'),

    path('Standing_Order_Suspension_Transaction_Activation_Approval_Processing_Load/', deskofficer_views.Standing_Order_Suspension_Transaction_Activation_Approval_Processing_Load,name='Standing_Order_Suspension_Transaction_Activation_Approval_Processing_Load'),
    path('Standing_Order_Suspension_Transaction_Activation_Approval_Processing_Processed/<str:pk>/', deskofficer_views.Standing_Order_Suspension_Transaction_Activation_Approval_Processing_Processed,name='Standing_Order_Suspension_Transaction_Activation_Approval_Processing_Processed'),

    path('Transaction_Loan_adjustment_search/', deskofficer_views.Transaction_Loan_adjustment_search,name='Transaction_Loan_adjustment_search'),
    path('Transaction_Loan_adjustment_List_load/', deskofficer_views.Transaction_Loan_adjustment_List_load,name='Transaction_Loan_adjustment_List_load'),
    path('Transaction_Loan_adjustment_Transaction_load/<str:pk>/', deskofficer_views.Transaction_Loan_adjustment_Transaction_load,name='Transaction_Loan_adjustment_Transaction_load'),
    path('Transaction_Loan_adjustment_Transaction_Preview/<str:pk>/<str:loan_code>/', deskofficer_views.Transaction_Loan_adjustment_Transaction_Preview,name='Transaction_Loan_adjustment_Transaction_Preview'),
    path('Transaction_Loan_adjustment_Transaction_Process/<str:pk>/<str:loan_code>/', deskofficer_views.Transaction_Loan_adjustment_Transaction_Process,name='Transaction_Loan_adjustment_Transaction_Process'),
    path('Transaction_Loan_adjustment_Transaction_Cancel/<str:pk>/', deskofficer_views.Transaction_Loan_adjustment_Transaction_Cancel,name='Transaction_Loan_adjustment_Transaction_Cancel'),

    path('Transaction_Loan_adjustment_Transaction_Approved_List_Load/', deskofficer_views.Transaction_Loan_adjustment_Transaction_Approved_List_Load,name='Transaction_Loan_adjustment_Transaction_Approved_List_Load'),
    path('Transaction_Loan_adjustment_Transaction_Approved_details_Processed/<str:pk>/', deskofficer_views.Transaction_Loan_adjustment_Transaction_Approved_details_Processed,name='Transaction_Loan_adjustment_Transaction_Approved_details_Processed'),

    path('MembersBankAccounts_list_search/', deskofficer_views.MembersBankAccounts_list_search,name='MembersBankAccounts_list_search'),
    path('MembersBankAccounts_list_load/', deskofficer_views.MembersBankAccounts_list_load,name='MembersBankAccounts_list_load'),
    path('Members_Bank_Accounts/<str:pk>/', deskofficer_views.Members_Bank_Accounts,name='Members_Bank_Accounts'),
    path('Members_Bank_Accounts_prioritization/<str:pk>/', deskofficer_views.Members_Bank_Accounts_prioritization,name='Members_Bank_Accounts_prioritization'),
    path('Members_Bank_Accounts_remove/<str:pk>/', deskofficer_views.Members_Bank_Accounts_remove,name='Members_Bank_Accounts_remove'),
    path('Members_Bank_Accounts_lock/<str:pk>/', deskofficer_views.Members_Bank_Accounts_lock,name='Members_Bank_Accounts_lock'),

    path('Members_Bank_Accounts_edit_search/', deskofficer_views.Members_Bank_Accounts_edit_search,name='Members_Bank_Accounts_edit_search'),
    path('Members_Bank_Accounts_edit_list_load/', deskofficer_views.Members_Bank_Accounts_edit_list_load,name='Members_Bank_Accounts_edit_list_load'),
    path('Members_Bank_Accounts_edit_details_load/<str:pk>/', deskofficer_views.Members_Bank_Accounts_edit_details_load,name='Members_Bank_Accounts_edit_details_load'),
    path('Members_Bank_Accounts_Edit_Prioritization/<str:pk>/', deskofficer_views.Members_Bank_Accounts_Edit_Prioritization,name='Members_Bank_Accounts_Edit_Prioritization'),
    path('Members_Bank_Accounts_update_form/<str:pk>/<str:return_pk>/', deskofficer_views.Members_Bank_Accounts_update_form,name='Members_Bank_Accounts_update_form'),
    path('Members_Bank_Accounts_delete/<str:pk>/<str:return_pk>/', deskofficer_views.Members_Bank_Accounts_delete,name='Members_Bank_Accounts_delete'),

    path('loan_request_order_discard/', deskofficer_views.loan_request_order_discard,name='loan_request_order_discard'),
    path('loan_request_order_discard_delete/<str:pk>/', deskofficer_views.loan_request_order_discard_delete,name='loan_request_order_discard_delete'),

    path('loan_request_search/', deskofficer_views.loan_request_search,name='loan_request_search'),
    path('loan_request_list_load/', deskofficer_views.loan_request_list_load,name='loan_request_list_load'),
    path('loan_request_order_delete/<str:pk>/<str:return_pk>/', deskofficer_views.loan_request_order_delete,name='loan_request_order_delete'),
    path('loan_request_order/<str:pk>/', deskofficer_views.loan_request_order,name='loan_request_order'),
    path('loan_request_criteria_Loading/<str:pk>/', deskofficer_views.loan_request_criteria_Loading,name='loan_request_criteria_Loading'),


    path('LoanRequestAttachments_delete/<str:pk>/<str:return_pk>/', deskofficer_views.LoanRequestAttachments_delete,name='LoanRequestAttachments_delete'),

    path('loan_request_preview/<str:pk>/', deskofficer_views.loan_request_preview,name='loan_request_preview'),

    path('loan_request_manage_period_load/', deskofficer_views.loan_request_manage_period_load,name='loan_request_manage_period_load'),
    path('loan_request_manage_transaction_delete/<str:pk>/', deskofficer_views.loan_request_manage_transaction_delete,name='loan_request_manage_transaction_delete'),

    path('loan_request_approved_Issue_form_period_load/', deskofficer_views.loan_request_approved_Issue_form_period_load,name='loan_request_approved_Issue_form_period_load'),
    path('loan_request_approved_list_form_sales/<str:pk>/', deskofficer_views.loan_request_approved_list_form_sales,name='loan_request_approved_list_form_sales'),
    path('loan_application_request_form_issuanace_confirmation/<str:pk>/', deskofficer_views.loan_application_request_form_issuanace_confirmation,name='loan_application_request_form_issuanace_confirmation'),
    path('Loan_Application_Issueance_Form_Print/<str:pk>/', deskofficer_views.Loan_Application_Issueance_Form_Print,name='Loan_Application_Issueance_Form_Print'),

    path('loan_application_approved_period_load/', deskofficer_views.loan_application_approved_period_load,name='loan_application_approved_period_load'),
    path('loan_application_form_processing/<str:pk>/', deskofficer_views.loan_application_form_processing,name='loan_application_form_processing'),

    path('loan_application_form_processing_guarantor_search/<str:pk>/', deskofficer_views.loan_application_form_processing_guarantor_search,name='loan_application_form_processing_guarantor_search'),
    path('loan_application_form_processing_guarantor_add_list_load/<str:pk>/', deskofficer_views.loan_application_form_processing_guarantor_add_list_load,name='loan_application_form_processing_guarantor_add_list_load'),
    path('loan_application_form_processing_guarantor_add/<str:pk>/<str:loan_pk>/', deskofficer_views.loan_application_form_processing_guarantor_add,name='loan_application_form_processing_guarantor_add'),
    path('loan_application_form_processing_guarantor_delete/<str:pk>/<str:return_pk>/', deskofficer_views.loan_application_form_processing_guarantor_delete,name='loan_application_form_processing_guarantor_delete'),

    path('loan_application_form_processing_bank_account_delete/<str:pk>/<str:return_pk>/', deskofficer_views.loan_application_form_processing_bank_account_delete,name='loan_application_form_processing_bank_account_delete'),
    path('loan_application_preview/<str:pk>/<str:return_pk>/', deskofficer_views.loan_application_preview,name='loan_application_preview'),

    path('Loan_application_processing_period_load/', deskofficer_views.Loan_application_processing_period_load,name='Loan_application_processing_period_load'),
    path('loan_application_approved_process_preview/<str:pk>/', deskofficer_views.loan_application_approved_process_preview,name='loan_application_approved_process_preview'),
    path('Loan_application_processing_confirmation/<str:pk>/', deskofficer_views.Loan_application_processing_confirmation,name='Loan_application_processing_confirmation'),
    path('Loan_application_processing_Form_Print/<str:pk>/', deskofficer_views.Loan_application_processing_Form_Print,name='Loan_application_processing_Form_Print'),


    path('Loan_processing_scheduling_dashboard/', deskofficer_views.Loan_processing_scheduling_dashboard,name='Loan_processing_scheduling_dashboard'),

    path('Loan_processing_scheduling_all_unscheduled/', deskofficer_views.Loan_processing_scheduling_all_unscheduled,name='Loan_processing_scheduling_all_unscheduled'),
    path('Loan_processing_scheduling_all_unscheduled_processed/<str:pk>/', deskofficer_views.Loan_processing_scheduling_all_unscheduled_processed,name='Loan_processing_scheduling_all_unscheduled_processed'),

    path('Loan_processing_scheduling_based_on_date/', deskofficer_views.Loan_processing_scheduling_based_on_date,name='Loan_processing_scheduling_based_on_date'),
    path('Loan_processing_scheduling_based_on_date_processed/<str:pk>/', deskofficer_views.Loan_processing_scheduling_based_on_date_processed,name='Loan_processing_scheduling_based_on_date_processed'),


    path('loan_unscheduling_request_search/', deskofficer_views.loan_unscheduling_request_search,name='loan_unscheduling_request_search'),
    path('loan_unscheduling_request_list_load/', deskofficer_views.loan_unscheduling_request_list_load,name='loan_unscheduling_request_list_load'),
    path('loan_unscheduling_request_transaction_load/<str:pk>/', deskofficer_views.loan_unscheduling_request_transaction_load,name='loan_unscheduling_request_transaction_load'),

    path('loan_unscheduling_request_transaction_processing/', deskofficer_views.loan_unscheduling_request_transaction_processing,name='loan_unscheduling_request_transaction_processing'),
    path('loan_unscheduling_request_transaction_processing_details/<str:pk>/', deskofficer_views.loan_unscheduling_request_transaction_processing_details,name='loan_unscheduling_request_transaction_processing_details'),

    path('Savings_Lockup_search/', deskofficer_views.Savings_Lockup_search,name='Savings_Lockup_search'),
    path('Savings_Lockup_list_load/', deskofficer_views.Savings_Lockup_list_load,name='Savings_Lockup_list_load'),
    path('Savings_Lockup_Processing/<str:pk>/', deskofficer_views.Savings_Lockup_Processing,name='Savings_Lockup_Processing'),

    path('members_wavers_request_search/', deskofficer_views.members_wavers_request_search,name='members_wavers_request_search'),
    path('members_wavers_request_list_load/', deskofficer_views.members_wavers_request_list_load,name='members_wavers_request_list_load'),
    path('members_wavers_request_register/<str:pk>/', deskofficer_views.members_wavers_request_register,name='members_wavers_request_register'),
    path('members_wavers_request_delete/<str:pk>/<str:return_pk>/', deskofficer_views.members_wavers_request_delete,name='members_wavers_request_delete'),


    path('members_exclusiveness_request_search/', deskofficer_views.members_exclusiveness_request_search,name='members_exclusiveness_request_search'),
    path('members_exclusiveness_request_list_load/', deskofficer_views.members_exclusiveness_request_list_load,name='members_exclusiveness_request_list_load'),
    path('members_exclusiveness_request_register/<str:pk>/', deskofficer_views.members_exclusiveness_request_register,name='members_exclusiveness_request_register'),



    path('Members_Next_Of_Kins_search/', deskofficer_views.Members_Next_Of_Kins_search,name='Members_Next_Of_Kins_search'),
    path('Members_Next_Of_Kins_list_load/', deskofficer_views.Members_Next_Of_Kins_list_load,name='Members_Next_Of_Kins_list_load'),
    path('addMembersNextOfKins/<str:pk>/', deskofficer_views.addMembersNextOfKins,name='addMembersNextOfKins'),
    path('MembersNextOfKins_remove/<str:pk>/', deskofficer_views.MembersNextOfKins_remove,name='MembersNextOfKins_remove'),
    path('MembersNextOfKins_lock/<str:pk>/', deskofficer_views.MembersNextOfKins_lock,name='MembersNextOfKins_lock'),

    path('Members_Next_Of_Kins_Manage_search/', deskofficer_views.Members_Next_Of_Kins_Manage_search,name='Members_Next_Of_Kins_Manage_search'),
    path('Members_Next_Of_Kins_Manage_list_load/', deskofficer_views.Members_Next_Of_Kins_Manage_list_load,name='Members_Next_Of_Kins_Manage_list_load'),
    path('Members_Next_Of_Kins_Manage_NOK_Load/<str:pk>/', deskofficer_views.Members_Next_Of_Kins_Manage_NOK_Load,name='Members_Next_Of_Kins_Manage_NOK_Load'),
    path('Members_Next_Of_Kins_Manage_NOK_Update/<str:pk>/<str:member_id>', deskofficer_views.Members_Next_Of_Kins_Manage_NOK_Update,name='Members_Next_Of_Kins_Manage_NOK_Update'),
    path('Members_Without_Next_of_Kin_list_load/', deskofficer_views.Members_Without_Next_of_Kin_list_load,name='Members_Without_Next_of_Kin_list_load'),
    path('Members_Without_Next_of_Kin_Update/<str:pk>/', deskofficer_views.Members_Without_Next_of_Kin_Update,name='Members_Without_Next_of_Kin_Update'),
    path('MembersNextOfKins_remove_2/<str:pk>/', deskofficer_views.MembersNextOfKins_remove_2,name='MembersNextOfKins_remove_2'),

    path('Members_Salary_Update_request_search/', deskofficer_views.Members_Salary_Update_request_search,name='Members_Salary_Update_request_search'),
    path('Members_Salary_Update_Request_list_load/', deskofficer_views.Members_Salary_Update_Request_list_load,name='Members_Salary_Update_Request_list_load'),
    path('Members_Salary_Update_Request_Load/<str:pk>/', deskofficer_views.Members_Salary_Update_Request_Load,name='Members_Salary_Update_Request_Load'),

    path('Members_Salary_Update_Request_approval_Load/', deskofficer_views.Members_Salary_Update_Request_approval_Load,name='Members_Salary_Update_Request_approval_Load'),
    path('Members_Salary_Update_Request_process/<str:pk>/', deskofficer_views.Members_Salary_Update_Request_process,name='Members_Salary_Update_Request_process'),


    path('TransactionPeriodManager/', deskofficer_views.TransactionPeriodManager,name='TransactionPeriodManager'),
    path('TransactionPeriodsUpdate/<str:pk>/', deskofficer_views.TransactionPeriodsUpdate,name='TransactionPeriodsUpdate'),
    path('TransactionPeriodsDelete/<str:pk>/', deskofficer_views.TransactionPeriodsDelete,name='TransactionPeriodsDelete'),

    path('Monthly_Deduction_Salary_Institution_Load/', deskofficer_views.Monthly_Deduction_Salary_Institution_Load,name='Monthly_Deduction_Salary_Institution_Load'),
    path('Monthly_Individual_Transactions_Load/<str:pk>/', deskofficer_views.Monthly_Individual_Transactions_Load,name='Monthly_Individual_Transactions_Load'),

    path('Monthly_Savings_Contribution_preview/<str:pk>/<str:salary_inst_key>/', deskofficer_views.Monthly_Savings_Contribution_preview,name='Monthly_Savings_Contribution_preview'),
    path('Monthly_Savings_Contribution_Generate/<str:pk>/<str:salary_inst_key>/', deskofficer_views.Monthly_Savings_Contribution_Generate,name='Monthly_Savings_Contribution_Generate'),

    path('Monthly_loan_repayement_preview/<str:pk>/<str:salary_inst_key>/', deskofficer_views.Monthly_loan_repayement_preview,name='Monthly_loan_repayement_preview'),
    path('Monthly_loan_repayement_Generate/<str:pk>/<str:salary_inst_key>/', deskofficer_views.Monthly_loan_repayement_Generate,name='Monthly_loan_repayement_Generate'),

    # path('Monthly_shop_repayement_preview/<str:pk>/<str:salary_inst_key>/', deskofficer_views.Monthly_shop_repayement_preview,name='Monthly_shop_repayement_preview'),

    path('MonthlyDeductionGenerationHeader/<str:caption>/<str:salary_inst_key>/', deskofficer_views.MonthlyDeductionGenerationHeader,name='MonthlyDeductionGenerationHeader'),


    path('Monthly_Group_transaction_Institution_Load/', deskofficer_views.Monthly_Group_transaction_Institution_Load,name='Monthly_Group_transaction_Institution_Load'),
    path('Monthly_Group_Generated_Transaction/<str:pk>/', deskofficer_views.Monthly_Group_Generated_Transaction,name='Monthly_Group_Generated_Transaction'),
    path('Monthly_Group_Transaction_preview/<str:pk>/', deskofficer_views.Monthly_Group_Transaction_preview,name='Monthly_Group_Transaction_preview'),
    path('Monthly_Group_Transaction_generate/<str:pk>/', deskofficer_views.Monthly_Group_Transaction_generate,name='Monthly_Group_Transaction_generate'),
    path('Monthly_Group_Transaction_View/<str:pk>/', deskofficer_views.Monthly_Group_Transaction_View,name='Monthly_Group_Transaction_View'),

    path('Monthly_Deduction_Main_and_Shop_Merger_Institution_load/', deskofficer_views.Monthly_Deduction_Main_and_Shop_Merger_Institution_load,name='Monthly_Deduction_Main_and_Shop_Merger_Institution_load'),

    path('Monthly_Deduction_Main_and_Shop_Merger_Load/<str:pk>/', deskofficer_views.Monthly_Deduction_Main_and_Shop_Merger_Load,name='Monthly_Deduction_Main_and_Shop_Merger_Load'),
    path('Monthly_Deduction_Main_and_Shop_Merger_Load_Main_Preview/<str:pk>/', deskofficer_views.Monthly_Deduction_Main_and_Shop_Merger_Load_Main_Preview,name='Monthly_Deduction_Main_and_Shop_Merger_Load_Main_Preview'),
    path('Monthly_Deduction_Main_and_Shop_Merger_Load_Main_Preview_details/<str:pk>/', deskofficer_views.Monthly_Deduction_Main_and_Shop_Merger_Load_Main_Preview_details,name='Monthly_Deduction_Main_and_Shop_Merger_Load_Main_Preview_details'),

    path('Monthly_Deduction_Main_and_Shop_Merger_Load_Shop_Preview/<str:pk>/', deskofficer_views.Monthly_Deduction_Main_and_Shop_Merger_Load_Shop_Preview,name='Monthly_Deduction_Main_and_Shop_Merger_Load_Shop_Preview'),
    path('Monthly_Deduction_Main_and_Shop_Merger_Load_Shop_Preview_details/<str:pk>/', deskofficer_views.Monthly_Deduction_Main_and_Shop_Merger_Load_Shop_Preview_details,name='Monthly_Deduction_Main_and_Shop_Merger_Load_Shop_Preview_details'),

    path('MonthlyJointDeductionsGenerate/<str:pk>/', deskofficer_views.MonthlyJointDeductionsGenerate,name='MonthlyJointDeductionsGenerate'),
    path('MonthlyJointDeductionsGenerateDetails/<str:pk>/<str:member_pk>/', deskofficer_views.MonthlyJointDeductionsGenerateDetails,name='MonthlyJointDeductionsGenerateDetails'),


    path('Monthly_Deduction_excel_Export_Institution_Load/', deskofficer_views.Monthly_Deduction_excel_Export_Institution_Load,name='Monthly_Deduction_excel_Export_Institution_Load'),
    path('Monthly_Deduction_excel_Export_load/<str:pk>/', deskofficer_views.Monthly_Deduction_excel_Export_load,name='Monthly_Deduction_excel_Export_load'),
    path('Monthly_Deduction_excel_Export_Details/<str:pk>/<str:member_pk>/', deskofficer_views.Monthly_Deduction_excel_Export_Details,name='Monthly_Deduction_excel_Export_Details'),

    path('export_monthly_deductions_xls/<str:pk>/', deskofficer_views.export_monthly_deductions_xls,name='export_monthly_deductions_xls'),
    path('export_norminal_roll_xls/', deskofficer_views.export_norminal_roll_xls,name='export_norminal_roll_xls'),

    path('export_norminal_roll_institution_xls/<str:pk>/', deskofficer_views.export_norminal_roll_institution_xls,name='export_norminal_roll_institution_xls'),

    path('Monthly_Account_deduction_Excel_import_Institution_Load/', deskofficer_views.Monthly_Account_deduction_Excel_import_Institution_Load,name='Monthly_Account_deduction_Excel_import_Institution_Load'),
    path('upload_AccountDeductionsResource/<str:pk>/', deskofficer_views.upload_AccountDeductionsResource,name='upload_AccountDeductionsResource'),

    path('Monthly_Account_deduction_Processing_Institution_Load/', deskofficer_views.Monthly_Account_deduction_Processing_Institution_Load,name='Monthly_Account_deduction_Processing_Institution_Load'),
    path('Monthly_Account_deduction_Processing_Preview/', deskofficer_views.Monthly_Account_deduction_Processing_Preview,name='Monthly_Account_deduction_Processing_Preview'),
    path('Monthly_Account_deduction_Process/<str:pk>/<str:trans_id>/', deskofficer_views.Monthly_Account_deduction_Process,name='Monthly_Account_deduction_Process'),

    path('Monthly_Account_Main_and_Shop_Deductions_Separations/', deskofficer_views.Monthly_Account_Main_and_Shop_Deductions_Separations,name='Monthly_Account_Main_and_Shop_Deductions_Separations'),


    path('Monthly_Main_Account_deductions_Separations/', deskofficer_views.Monthly_Main_Account_deductions_Separations,name='Monthly_Main_Account_deductions_Separations'),

    path('monthly_wrongful_deduction_transaction_period_load/', deskofficer_views.monthly_wrongful_deduction_transaction_period_load,name='monthly_wrongful_deduction_transaction_period_load'),
    path('Monthly_Unbalanced_transactions/', deskofficer_views.Monthly_Unbalanced_transactions,name='Monthly_Unbalanced_transactions'),
    path('Monthly_Unbalanced_transactions_Processing/<str:pk>/', deskofficer_views.Monthly_Unbalanced_transactions_Processing,name='Monthly_Unbalanced_transactions_Processing'),
    path('Monthly_Unbalanced_transactions_Processing_Savings/<str:pk>/', deskofficer_views.Monthly_Unbalanced_transactions_Processing_Savings,name='Monthly_Unbalanced_transactions_Processing_Savings'),

    path('Monthly_deduction_ledger_posting_preview/', deskofficer_views.Monthly_deduction_ledger_posting_preview,name='Monthly_deduction_ledger_posting_preview'),

    path('Monthly_Deduction_Covering_Note/', deskofficer_views.Monthly_Deduction_Covering_Note,name='Monthly_Deduction_Covering_Note'),
    path('Monthly_Deduction_Covering_Note_Print/<str:print_date>/<str:transaction_period>/<str:staff1>/<str:position1>/<str:staff2>/<str:position2>/<str:account>/', deskofficer_views.Monthly_Deduction_Covering_Note_Print,name='Monthly_Deduction_Covering_Note_Print'),

    path('upload_norminal_roll/', deskofficer_views.upload_norminal_roll,name='upload_norminal_roll'),
    path('Norminal_Roll_Preview/', deskofficer_views.Norminal_Roll_Preview,name='Norminal_Roll_Preview'),
    path('Norminal_Roll_Process/', deskofficer_views.Norminal_Roll_Process,name='Norminal_Roll_Process'),
    path('Individual_Capture/', deskofficer_views.Individual_Capture,name='Individual_Capture'),
    path('Individual_Capture_Delete_Search/', deskofficer_views.Individual_Capture_Delete_Search,name='Individual_Capture_Delete_Search'),
    path('Individual_Capture_Delete_List_load/', deskofficer_views.Individual_Capture_Delete_List_load,name='Individual_Capture_Delete_List_load'),
    path('Individual_Capture_Delete/<str:pk>/', deskofficer_views.Individual_Capture_Delete,name='Individual_Capture_Delete'),

    path('upload_distinct_norminal_roll/', deskofficer_views.upload_distinct_norminal_roll,name='upload_distinct_norminal_roll'),

    path('Uploading_Existing_Savings_Search/', deskofficer_views.Uploading_Existing_Savings_Search,name='Uploading_Existing_Savings_Search'),
    path('Uploading_Existing_Savings_List_load/', deskofficer_views.Uploading_Existing_Savings_List_load,name='Uploading_Existing_Savings_List_load'),
    path('Uploading_Existing_Savings_Preview/<str:pk>/', deskofficer_views.Uploading_Existing_Savings_Preview,name='Uploading_Existing_Savings_Preview'),
    path('Uploading_Existing_Savings_validate/<str:pk>/', deskofficer_views.Uploading_Existing_Savings_validate,name='Uploading_Existing_Savings_validate'),
    path('Uploading_Existing_Savings_delete/<str:pk>/<str:return_pk>/', deskofficer_views.Uploading_Existing_Savings_delete,name='Uploading_Existing_Savings_delete'),
    

    path('Uploading_Existing_Savings_All_List_load/', deskofficer_views.Uploading_Existing_Savings_All_List_load,name='Uploading_Existing_Savings_All_List_load'),
    path('Uploading_Existing_Savings_Preview_All/<str:pk>/', deskofficer_views.Uploading_Existing_Savings_Preview_All,name='Uploading_Existing_Savings_Preview_All'),
    path('Uploading_Existing_Savings_delete_All/<str:pk>/<str:return_pk>/', deskofficer_views.Uploading_Existing_Savings_delete_All,name='Uploading_Existing_Savings_delete_All'),
    path('Uploading_Existing_Savings_Discard_All/<str:pk>/', deskofficer_views.Uploading_Existing_Savings_Discard_All,name='Uploading_Existing_Savings_Discard_All'),

    path('Uploading_Existing_Savings_Done_Transaction_Date_Update/', deskofficer_views.Uploading_Existing_Savings_Done_Transaction_Date_Update,name='Uploading_Existing_Savings_Done_Transaction_Date_Update'),
    

    path('Uploading_Existing_Savings_Done_List_Select_Period/', deskofficer_views.Uploading_Existing_Savings_Done_List_Select_Period,name='Uploading_Existing_Savings_Done_List_Select_Period'),
    path('Uploading_Existing_Savings_Done_List_load/<str:transaction_period>/<str:tdate>/', deskofficer_views.Uploading_Existing_Savings_Done_List_load,name='Uploading_Existing_Savings_Done_List_load'),
    path('Uploading_Existing_Savings_Done_View_Details/<str:pk>/', deskofficer_views.Uploading_Existing_Savings_Done_View_Details,name='Uploading_Existing_Savings_Done_View_Details'),

    path('Cash_Deposit_Welfare_Search/', deskofficer_views.Cash_Deposit_Welfare_Search,name='Cash_Deposit_Welfare_Search'),
    path('Cash_Deposit_Welfare_list_load/', deskofficer_views.Cash_Deposit_Welfare_list_load,name='Cash_Deposit_Welfare_list_load'),
    path('Cash_Deposit_Welfare_Preview/<str:pk>/', deskofficer_views.Cash_Deposit_Welfare_Preview,name='Cash_Deposit_Welfare_Preview'),

    path('Uploading_Existing_Loans_Search/', deskofficer_views.Uploading_Existing_Loans_Search,name='Uploading_Existing_Loans_Search'),
    path('Uploading_Existing_Loans_List_load/', deskofficer_views.Uploading_Existing_Loans_List_load,name='Uploading_Existing_Loans_List_load'),
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

    path('Members_Shares_Upload_Search/', deskofficer_views.Members_Shares_Upload_Search,name='Members_Shares_Upload_Search'),
    path('Members_Shares_Upload_list_load/', deskofficer_views.Members_Shares_Upload_list_load,name='Members_Shares_Upload_list_load'),
    path('Members_Shares_Upload_Preview/<str:pk>/', deskofficer_views.Members_Shares_Upload_Preview,name='Members_Shares_Upload_Preview'),


    path('Members_Welfare_Upload_Search/', deskofficer_views.Members_Welfare_Upload_Search,name='Members_Welfare_Upload_Search'),
    path('Members_Welfare_Upload_list_load/', deskofficer_views.Members_Welfare_Upload_list_load,name='Members_Welfare_Upload_list_load'),
    path('Members_Welfare_Upload_Preview/<str:pk>/', deskofficer_views.Members_Welfare_Upload_Preview,name='Members_Welfare_Upload_Preview'),

    path('Norminal_Roll_Search/', deskofficer_views.Norminal_Roll_Search,name='Norminal_Roll_Search'),
    path('Norminal_Roll_Update_list_load/', deskofficer_views.Norminal_Roll_Update_list_load,name='Norminal_Roll_Update_list_load'),
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

    path('Members_Initial_Shares_Reports_Load/', deskofficer_views.Members_Initial_Shares_Reports_Load,name='Members_Initial_Shares_Reports_Load'),

    path('Members_Individual_Shares_Report_Search/', deskofficer_views.Members_Individual_Shares_Report_Search,name='Members_Individual_Shares_Report_Search'),
    path('Members_Individual_Shares_Report_List_load/', deskofficer_views.Members_Individual_Shares_Report_List_load,name='Members_Individual_Shares_Report_List_load'),
    path('Members_Individual_Shares_Report_Details/<str:pk>/', deskofficer_views.Members_Individual_Shares_Report_Details,name='Members_Individual_Shares_Report_Details'),

    path('Members_General_Shares_Report_List_Load/', deskofficer_views.Members_General_Shares_Report_List_Load,name='Members_General_Shares_Report_List_Load'),

    path('Members_Dashboard_Search/', deskofficer_views.Members_Dashboard_Search,name='Members_Dashboard_Search'),
    path('Members_Dashboard_Search_list_load/', deskofficer_views.Members_Dashboard_Search_list_load,name='Members_Dashboard_Search_list_load'),
    path('Members_Dashboard_Load/<str:pk>/', deskofficer_views.Members_Dashboard_Load,name='Members_Dashboard_Load'),

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


    path('Xmas_Savings_Shortlisting_list_Load/', deskofficer_views.Xmas_Savings_Shortlisting_list_Load,name='Xmas_Savings_Shortlisting_list_Load'),
    path('Xmas_Savings_Shortlisting_Filter_Batch_Load/', deskofficer_views.Xmas_Savings_Shortlisting_Filter_Batch_Load,name='Xmas_Savings_Shortlisting_Filter_Batch_Load'),
    path('Xmas_Savings_Shortlisting_Filter_List_Load/<str:batch>/<str:payment>/', deskofficer_views.Xmas_Savings_Shortlisting_Filter_List_Load,name='Xmas_Savings_Shortlisting_Filter_List_Load'),
    path('Xmas_Savings_Shortlisting_Switching/<str:pk>/', deskofficer_views.Xmas_Savings_Shortlisting_Switching,name='Xmas_Savings_Shortlisting_Switching'),

    path('Xmas_Savings_Shortlisting_Account_Linkage_Batch_Load/', deskofficer_views.Xmas_Savings_Shortlisting_Account_Linkage_Batch_Load,name='Xmas_Savings_Shortlisting_Account_Linkage_Batch_Load'),
    path('Xmas_Savings_Shortlisting_Account_Linkage_List_Load/<str:batch>/<str:payment>/', deskofficer_views.Xmas_Savings_Shortlisting_Account_Linkage_List_Load,name='Xmas_Savings_Shortlisting_Account_Linkage_List_Load'),
    path('Xmas_Savings_Shortlisting_Account_Assignment_Load_Default/<str:batch>/<str:payment>/', deskofficer_views.Xmas_Savings_Shortlisting_Account_Assignment_Load_Default,name='Xmas_Savings_Shortlisting_Account_Assignment_Load_Default'),
    path('Xmas_Savings_Shortlisting_Account_Assignment/<str:pk>/', deskofficer_views.Xmas_Savings_Shortlisting_Account_Assignment,name='Xmas_Savings_Shortlisting_Account_Assignment'),
    path('Xmas_Savings_Shortlisting_Account_Transfer/<str:pk>/', deskofficer_views.Xmas_Savings_Shortlisting_Account_Transfer,name='Xmas_Savings_Shortlisting_Account_Transfer'),

    path('Xmas_Savings_Shortlisting_Export_Batch_Load/', deskofficer_views.Xmas_Savings_Shortlisting_Export_Batch_Load,name='Xmas_Savings_Shortlisting_Export_Batch_Load'),
    path('Xmas_Savings_Shortlisting_Export_List_Load/<str:batch>/<str:payment>/', deskofficer_views.Xmas_Savings_Shortlisting_Export_List_Load,name='Xmas_Savings_Shortlisting_Export_List_Load'),
    path('export_xmas_savings_payment_xls/<str:batch>/<str:payment>/', deskofficer_views.export_xmas_savings_payment_xls,name='export_xmas_savings_payment_xls'),
    path('Xmas_Savings_Shortlisting_Processing_Update_Bank_account/<str:pk>/', deskofficer_views.Xmas_Savings_Shortlisting_Processing_Update_Bank_account,name='Xmas_Savings_Shortlisting_Processing_Update_Bank_account'),

    path('Xmas_Savings_Shortlisting_Processing_Batch_Load/', deskofficer_views.Xmas_Savings_Shortlisting_Processing_Batch_Load,name='Xmas_Savings_Shortlisting_Processing_Batch_Load'),
    path('Xmas_Savings_Shortlisting_Processing_List_Load/<str:batch>/<str:payment>/', deskofficer_views.Xmas_Savings_Shortlisting_Processing_List_Load,name='Xmas_Savings_Shortlisting_Processing_List_Load'),
    path('Xmas_Savings_Shortlisting_Processing_Preview/<str:pk>/', deskofficer_views.Xmas_Savings_Shortlisting_Processing_Preview,name='Xmas_Savings_Shortlisting_Processing_Preview'),

    path('Xmas_Savings_Shortlisting_Ledger_Posting_Batch_Load/', deskofficer_views.Xmas_Savings_Shortlisting_Ledger_Posting_Batch_Load,name='Xmas_Savings_Shortlisting_Ledger_Posting_Batch_Load'),
    path('Xmas_Savings_Shortlisting_Ledger_Posting_List_Load/<str:batch>/<str:payment>/', deskofficer_views.Xmas_Savings_Shortlisting_Ledger_Posting_List_Load,name='Xmas_Savings_Shortlisting_Ledger_Posting_List_Load'),

    path('Cash_Withdrawal_Search/', deskofficer_views.Cash_Withdrawal_Search,name='Cash_Withdrawal_Search'),
    path('Cash_Withdrawal_list_load/', deskofficer_views.Cash_Withdrawal_list_load,name='Cash_Withdrawal_list_load'),
    path('Cash_Withdrawal_Transactions_load/<str:pk>/', deskofficer_views.Cash_Withdrawal_Transactions_load,name='Cash_Withdrawal_Transactions_load'),

    path('Cash_Withdrawal_Transactions_Request_Status_list_Search/', deskofficer_views.Cash_Withdrawal_Transactions_Request_Status_list_Search,name='Cash_Withdrawal_Transactions_Request_Status_list_Search'),
    path('Cash_Withdrawal_Transactions_Request_Status_list_Load/', deskofficer_views.Cash_Withdrawal_Transactions_Request_Status_list_Load,name='Cash_Withdrawal_Transactions_Request_Status_list_Load'),
    path('Cash_Withdrawal_Transactions_Request_Status_Drop/<str:pk>/', deskofficer_views.Cash_Withdrawal_Transactions_Request_Status_Drop,name='Cash_Withdrawal_Transactions_Request_Status_Drop'),


    path('Cash_Withdrawal_Transactions_Approved_list_Search/', deskofficer_views.Cash_Withdrawal_Transactions_Approved_list_Search,name='Cash_Withdrawal_Transactions_Approved_list_Search'),
    path('Cash_Withdrawal_Transactions_Approved_list_Load/', deskofficer_views.Cash_Withdrawal_Transactions_Approved_list_Load,name='Cash_Withdrawal_Transactions_Approved_list_Load'),


    path('Cash_Withdrawal_Transactions_All_Uncleared_list_Load/', deskofficer_views.Cash_Withdrawal_Transactions_All_Uncleared_list_Load,name='Cash_Withdrawal_Transactions_All_Uncleared_list_Load'),

    path('members_credit_purchase_approval/', deskofficer_views.members_credit_purchase_approval,name='members_credit_purchase_approval'),
    path('members_credit_purchase_approval_preview/<str:ticket>/', deskofficer_views.members_credit_purchase_approval_preview,name='members_credit_purchase_approval_preview'),

    path('Initial_Shares_Update_List_Load/', deskofficer_views.Initial_Shares_Update_List_Load,name='Initial_Shares_Update_List_Load'),
    path('Initial_Shares_Update_preview/<str:pk>/', deskofficer_views.Initial_Shares_Update_preview,name='Initial_Shares_Update_preview'),

    path('Transaction_Adjustment_Approval_list_Load/', deskofficer_views.Transaction_Adjustment_Approval_list_Load,name='Transaction_Adjustment_Approval_list_Load'),
    path('Transaction_Adjustment_Approval_Process/<str:pk>/', deskofficer_views.Transaction_Adjustment_Approval_Process,name='Transaction_Adjustment_Approval_Process'),

    path('Transaction_Loan_Adjustment_Approval_list_Load/', deskofficer_views.Transaction_Loan_Adjustment_Approval_list_Load,name='Transaction_Loan_Adjustment_Approval_list_Load'),
    path('Transaction_Loan_Adjustment_Approval_list_Process/<str:pk>/', deskofficer_views.Transaction_Loan_Adjustment_Approval_list_Process,name='Transaction_Loan_Adjustment_Approval_list_Process'),

    path('membership_termination_approved_list_processing_list_load/', deskofficer_views.membership_termination_approved_list_processing_list_load,name='membership_termination_approved_list_processing_list_load'),
    path('membership_termination_approved_list_processing_preview/<str:pk>/', deskofficer_views.membership_termination_approved_list_processing_preview,name='membership_termination_approved_list_processing_preview'),
    path('membership_termination_approved_transaction_details/<str:pk>/', deskofficer_views.membership_termination_approved_transaction_details,name='membership_termination_approved_transaction_details'),
   
    path('membership_dashboard_transaction_details/<str:pk>/', deskofficer_views.membership_dashboard_transaction_details,name='membership_dashboard_transaction_details'),


    path('membership_termination_search/', deskofficer_views.membership_termination_search,name='membership_termination_search'),
    path('membership_termination_list_load/', deskofficer_views.membership_termination_list_load,name='membership_termination_list_load'),
    path('membership_termination_transactions_load/<str:pk>/', deskofficer_views.membership_termination_transactions_load,name='membership_termination_transactions_load'),

    path('membership_termination_maturity_date_exception_search/', deskofficer_views.membership_termination_maturity_date_exception_search,name='membership_termination_maturity_date_exception_search'),
    path('membership_termination_maturity_date_exception_list_load/', deskofficer_views.membership_termination_maturity_date_exception_list_load,name='membership_termination_maturity_date_exception_list_load'),
    path('membership_termination_maturity_date_exception_process/<str:pk>/', deskofficer_views.membership_termination_maturity_date_exception_process,name='membership_termination_maturity_date_exception_process'),

    path('membership_termination_maturity_date_exception_approved_list_load/', deskofficer_views.membership_termination_maturity_date_exception_approved_list_load,name='membership_termination_maturity_date_exception_approved_list_load'),
    path('membership_termination_maturity_date_exception_approved_process/<str:pk>/', deskofficer_views.membership_termination_maturity_date_exception_approved_process,name='membership_termination_maturity_date_exception_approved_process'),


    path('membership_termination_Disbursement_Processing_list_Load/', deskofficer_views.membership_termination_Disbursement_Processing_list_Load,name='membership_termination_Disbursement_Processing_list_Load'),
    path('membership_termination_Disbursement_Processing_Preview/<str:pk>/', deskofficer_views.membership_termination_Disbursement_Processing_Preview,name='membership_termination_Disbursement_Processing_Preview'),
    path('membership_termination_Disbursement_Processing_Cash/<str:pk>/<str:payment>/', deskofficer_views.membership_termination_Disbursement_Processing_Cash,name='membership_termination_Disbursement_Processing_Cash'),
    path('membership_termination_Disbursement_Processing_Cheque/<str:pk>/<str:payment>/', deskofficer_views.membership_termination_Disbursement_Processing_Cheque,name='membership_termination_Disbursement_Processing_Cheque'),
    path('membership_termination_Disbursement_Processing_Transfer/<str:pk>/<str:payment>/', deskofficer_views.membership_termination_Disbursement_Processing_Transfer,name='membership_termination_Disbursement_Processing_Transfer'),

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
    # path('membership_commodity_loan_Company_products_Guarantor_Settings/<str:member_pk>/<str:period_pk>/<str:batch_pk>/<str:transaction_pk>/', deskofficer_views.membership_commodity_loan_Company_products_Guarantor_Settings,name='membership_commodity_loan_Company_products_Guarantor_Settings'),
    # path('membership_commodity_loan_Company_products_Guarantor_Delete/<str:pk>/<str:member_pk>/<str:period_pk>/<str:batch_pk>/<str:transaction_pk>/', deskofficer_views.membership_commodity_loan_Company_products_Guarantor_Delete,name='membership_commodity_loan_Company_products_Guarantor_Delete'),
    path('membership_commodity_loan_application_submit/<str:member_pk>/<str:period_pk>/<str:batch_pk>/<str:transaction_pk>/', deskofficer_views.membership_commodity_loan_application_submit,name='membership_commodity_loan_application_submit'),

    path('membership_commodity_loan_Dashboard_load/<str:pk>/<str:return_pk>/', deskofficer_views.membership_commodity_loan_Dashboard_load,name='membership_commodity_loan_Dashboard_load'),
    path('membership_commodity_loan_Company_products_net_pay_SettingsB/<str:pk>/<str:return_pk>/', deskofficer_views.membership_commodity_loan_Company_products_net_pay_SettingsB,name='membership_commodity_loan_Company_products_net_pay_SettingsB'),
    path('membership_commodity_loan_application_submitB/<str:pk>/<str:return_pk>/', deskofficer_views.membership_commodity_loan_application_submitB,name='membership_commodity_loan_application_submitB'),


    path('membership_commodity_loan_Period__manage_transaction_load/', deskofficer_views.membership_commodity_loan_Period__manage_transaction_load,name='membership_commodity_loan_Period__manage_transaction_load'),
    path('membership_commodity_loan_Period__manage_transaction_delete_Confirmation/<str:pk>/', deskofficer_views.membership_commodity_loan_Period__manage_transaction_delete_Confirmation,name='membership_commodity_loan_Period__manage_transaction_delete_Confirmation'),
    path('membership_commodity_loan_Period__manage_transaction_delete/<str:pk>/', deskofficer_views.membership_commodity_loan_Period__manage_transaction_delete,name='membership_commodity_loan_Period__manage_transaction_delete'),


    # path('membership_commodity_loan_manage/', deskofficer_views.membership_commodity_loan_manage,name='membership_commodity_loan_manage'),
    # path('membership_commodity_loan_manage_delete/<str:pk>/', deskofficer_views.membership_commodity_loan_manage_delete,name='membership_commodity_loan_manage_delete'),
    # path('membership_commodity_loan_manage_details/<str:pk>/', deskofficer_views.membership_commodity_loan_manage_details,name='membership_commodity_loan_manage_details'),
    # path('membership_commodity_loan_manage_details_reset_Confirmation/<str:pk>/', deskofficer_views.membership_commodity_loan_manage_details_reset_Confirmation,name='membership_commodity_loan_manage_details_reset_Confirmation'),


    path('membership_commodity_loan_form_sales_transaction_period_load/', deskofficer_views.membership_commodity_loan_form_sales_transaction_period_load,name='membership_commodity_loan_form_sales_transaction_period_load'),
    path('membership_commodity_loan_form_sales/<str:pk>/', deskofficer_views.membership_commodity_loan_form_sales,name='membership_commodity_loan_form_sales'),
    path('membership_commodity_loan_form_sales_process/<str:pk>/<str:payment>/', deskofficer_views.membership_commodity_loan_form_sales_process,name='membership_commodity_loan_form_sales_process'),

    path('commodity_loan_trending_products/', deskofficer_views.commodity_loan_trending_products,name='commodity_loan_trending_products'),
    path('commodity_loan_trending_products_load/<str:pk>/', deskofficer_views.commodity_loan_trending_products_load,name='commodity_loan_trending_products_load'),
    path('commodity_loan_trending_products_details/<str:pk>/', deskofficer_views.commodity_loan_trending_products_details,name='commodity_loan_trending_products_details'),


    path('trending_products_member_Search/', deskofficer_views.trending_products_member_Search,name='trending_products_member_Search'),
    path('trending_products_member_list_load/', deskofficer_views.trending_products_member_list_load,name='trending_products_member_list_load'),
    path('commodity_trending_product_Print/<str:pk>/', deskofficer_views.commodity_trending_product_Print,name='commodity_trending_product_Print'),

    path('membership_commodity_loan_Final_Applications/', deskofficer_views.membership_commodity_loan_Final_Applications,name='membership_commodity_loan_Final_Applications'),
    path('membership_commodity_loan_Final_Applications_Process/<str:pk>/', deskofficer_views.membership_commodity_loan_Final_Applications_Process,name='membership_commodity_loan_Final_Applications_Process'),
    path('membership_commodity_loan_Final_Applications_Process_Add_Guarantors/<str:member_pk>/<str:pk>/', deskofficer_views.membership_commodity_loan_Final_Applications_Process_Add_Guarantors,name='membership_commodity_loan_Final_Applications_Process_Add_Guarantors'),

    path('membership_commodity_loan_Final_Applications_Process_Submit/<str:pk>/', deskofficer_views.membership_commodity_loan_Final_Applications_Process_Submit,name='membership_commodity_loan_Final_Applications_Process_Submit'),

    path('membership_commodity_loan_Final_Applications_Delete/<str:pk>/<str:return_pk>/', deskofficer_views.membership_commodity_loan_Final_Applications_Delete,name='membership_commodity_loan_Final_Applications_Delete'),

    path('Company_add/<str:pk>/', deskofficer_views.Company_add,name='Company_add'),

    path('Rental_Services_Category_List_Load/', deskofficer_views.Rental_Services_Category_List_Load,name='Rental_Services_Category_List_Load'),
    path('Rental_Services_Contact_Person_Register/<str:pk>/', deskofficer_views.Rental_Services_Contact_Person_Register,name='Rental_Services_Contact_Person_Register'),
    path('Rental_Services_Contact_Person_Register_Delete/<str:pk>/', deskofficer_views.Rental_Services_Contact_Person_Register_Delete,name='Rental_Services_Contact_Person_Register_Delete'),
    path('Rental_Date_Time_Selector/<str:pk>/', deskofficer_views.Rental_Date_Time_Selector,name='Rental_Date_Time_Selector'),

    path('Rental_Products_List_Load/<str:pk>/<str:b_date>/<str:start_time>/<str:stop_time>/', deskofficer_views.Rental_Products_List_Load,name='Rental_Products_List_Load'),
    path('Rental_Services_Selection_List_Load_Delete/<str:pk>/<str:b_date>/<str:start_time>/<str:stop_time>/', deskofficer_views.Rental_Services_Selection_List_Load_Delete,name='Rental_Services_Selection_List_Load_Delete'),
    path('Rental_Services_Group_Selection_List_Load_Delete/<str:pk>/', deskofficer_views.Rental_Services_Group_Selection_List_Load_Delete,name='Rental_Services_Group_Selection_List_Load_Delete'),

    path('Rental_Services_Selection_Preview/<str:pk>/', deskofficer_views.Rental_Services_Selection_Preview,name='Rental_Services_Selection_Preview'),

    path('Rental_Services_Unpaid_Bill/', deskofficer_views.Rental_Services_Unpaid_Bill,name='Rental_Services_Unpaid_Bill'),
    path('Rental_Services_Unpaid_Bill_Preview/<str:pk>/', deskofficer_views.Rental_Services_Unpaid_Bill_Preview,name='Rental_Services_Unpaid_Bill_Preview'),

    path('Rental_Services_Management/', deskofficer_views.Rental_Services_Management,name='Rental_Services_Management'),
    path('Rental_Services_Management_Process/<str:pk>/', deskofficer_views.Rental_Services_Management_Process,name='Rental_Services_Management_Process'),
    path('Rental_Services_Management_Process_Details/<str:pk>/<str:contact>/', deskofficer_views.Rental_Services_Management_Process_Details,name='Rental_Services_Management_Process_Details'),
    path('Rental_Services_Management_Process_Completed/<str:pk>/<str:b_date>/', deskofficer_views.Rental_Services_Management_Process_Completed,name='Rental_Services_Management_Process_Completed'),

    # path('index/', deskofficer_views.index,name='index'),


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

    path('Norminal_Roll_By_Institution_Load/', deskofficer_views.Norminal_Roll_By_Institution_Load,name='Norminal_Roll_By_Institution_Load'),
    path('Norminal_Roll_By_Institution_List_Load/<str:pk>/', deskofficer_views.Norminal_Roll_By_Institution_List_Load,name='Norminal_Roll_By_Institution_List_Load'),
    

    path('MemberShipFormSalesReport/', deskofficer_views.MemberShipFormSalesReport,name='MemberShipFormSalesReport'),
    path('MemberShipFormSales_Report_individual_Search/', deskofficer_views.MemberShipFormSales_Report_individual_Search,name='MemberShipFormSales_Report_individual_Search'),
    path('MemberShipFormSales_Report_individual_list_Load/', deskofficer_views.MemberShipFormSales_Report_individual_list_Load,name='MemberShipFormSales_Report_individual_list_Load'),

    path('Over_Deductions_report/', deskofficer_views.Over_Deductions_report,name='Over_Deductions_report'),
    path('Under_Deductions_report/', deskofficer_views.Under_Deductions_report,name='Under_Deductions_report'),
    path('Non_Members_Deductions_report/', deskofficer_views.Non_Members_Deductions_report,name='Non_Members_Deductions_report'),


    path('check_receipt_no_already_used/', deskofficer_views.check_receipt_no_already_used,name='check_receipt_no_already_used'),
    path('check_membership_phone_no_exist/', deskofficer_views.check_membership_phone_no_exist,name='check_membership_phone_no_exist'),

    path('Monthly_Deductions_Report_Search/', deskofficer_views.Monthly_Deductions_Report_Search,name='Monthly_Deductions_Report_Search'),
    path('Monthly_Deductions_Report_list_load/', deskofficer_views.Monthly_Deductions_Report_list_load,name='Monthly_Deductions_Report_list_load'),
    path('Monthly_Deductions_Report_Preview/<str:pk>/', deskofficer_views.Monthly_Deductions_Report_Preview,name='Monthly_Deductions_Report_Preview'),

    path('Monthly_Deductions_All_Records_Report_Period/', deskofficer_views.Monthly_Deductions_All_Records_Report_Period,name='Monthly_Deductions_All_Records_Report_Period'),
    path('Monthly_Deductions_All_Records_Report_Deatials/<str:pk>/', deskofficer_views.Monthly_Deductions_All_Records_Report_Deatials,name='Monthly_Deductions_All_Records_Report_Deatials'),


    ###########################################################################
    ############################ SHOP ######################################
    ###########################################################################
    path('shop_home/', shop_views.shop_home,name='shop_home'),
    path('Useraccount_manager_Shop/', shop_views.Useraccount_manager_Shop,name='Useraccount_manager_Shop'),
    path('advance_form/', shop_views.advance_form,name='advance_form'),
    path('editable_invoice/', shop_views.editable_invoice,name='editable_invoice'),

# Members_Cash_Sales_Selected
    path('members_cash_sales_manage_list_load/', shop_views.members_cash_sales_manage_list_load,name='members_cash_sales_manage_list_load'),
    path('members_cash_sales_manage_delete_single_record/<str:pk>/', shop_views.members_cash_sales_manage_delete_single_record,name='members_cash_sales_manage_delete_single_record'),


    path('members_cash_sales_search/', shop_views.members_cash_sales_search,name='members_cash_sales_search'),
    path('members_cash_sales_list_load/', shop_views.members_cash_sales_list_load,name='members_cash_sales_list_load'),


    path('members_cash_sales_product_load/<str:pk>/<str:ticket>/', shop_views.members_cash_sales_product_load,name='members_cash_sales_product_load'),
    path('members_cash_sales_item_issue/<str:pk>/<str:member_id>/', shop_views.members_cash_sales_item_issue,name='members_cash_sales_item_issue'),
    path('members_cash_sales_item_delete/<str:pk>/', shop_views.members_cash_sales_item_delete,name='members_cash_sales_item_delete'),
    # path('members_cash_sales_receipt/<str:pk>/', shop_views.members_cash_sales_receipt,name='members_cash_sales_receipt'),

    path('members_cash_sales_processing/<str:pk>/<str:pay_status>/', shop_views.members_cash_sales_processing,name='members_cash_sales_processing'),


    path('members_cash_sales_auction_item_issue/<str:pk>/<str:member_id>/<str:ticket>/', shop_views.members_cash_sales_auction_item_issue,name='members_cash_sales_auction_item_issue'),

    path('Stock_Category_Load/', shop_views.Stock_Category_Load,name='Stock_Category_Load'),
    path('Stock_add/<str:pk>/', shop_views.Stock_add,name='Stock_add'),
    path('Update_Stock/<str:pk>/<str:return_pk>/', shop_views.Update_Stock,name='Update_Stock'),

    path('Item_Write_off_Reasons/', shop_views.Item_Write_off_Reasons,name='Item_Write_off_Reasons'),

    path('Item_Write_off_Reasons_delete/<str:pk>/', shop_views.Item_Write_off_Reasons_delete,name='Item_Write_off_Reasons_delete'),
    path('Item_Write_off_search/', shop_views.Item_Write_off_search,name='Item_Write_off_search'),
    path('Item_Write_off_product_load/', shop_views.Item_Write_off_product_load,name='Item_Write_off_product_load'),
    path('Item_Write_off_product_Preview/<str:pk>/', shop_views.Item_Write_off_product_Preview,name='Item_Write_off_product_Preview'),

    path('Item_Write_off_product_Auction_Preview/<str:pk>/', shop_views.Item_Write_off_product_Auction_Preview,name='Item_Write_off_product_Auction_Preview'),


    path('Item_Write_off_manage/', shop_views.Item_Write_off_manage,name='Item_Write_off_manage'),
    path('Item_Write_off_manage_delete/<str:pk>/', shop_views.Item_Write_off_manage_delete,name='Item_Write_off_manage_delete'),
    path('Item_Write_off_manage_Preview/<str:pk>/', shop_views.Item_Write_off_manage_Preview,name='Item_Write_off_manage_Preview'),
    path('Item_Write_off_Approval/', shop_views.Item_Write_off_Approval,name='Item_Write_off_Approval'),
    path('Item_Write_off_Approval_Preview/<str:pk>/', shop_views.Item_Write_off_Approval_Preview,name='Item_Write_off_Approval_Preview'),
    path('Item_Write_off_Approved_List/', shop_views.Item_Write_off_Approved_List,name='Item_Write_off_Approved_List'),
    path('Item_Write_off_Approved_Process/<str:pk>/', shop_views.Item_Write_off_Approved_Process,name='Item_Write_off_Approved_Process'),

    path('Item_Write_off_Daily_Summary/', shop_views.Item_Write_off_Daily_Summary,name='Item_Write_off_Daily_Summary'),
    path('Item_Write_off_Day_End_Transactions/', shop_views.Item_Write_off_Day_End_Transactions,name='Item_Write_off_Day_End_Transactions'),
    path('Item_Write_off_Month_End_Transactions/', shop_views.Item_Write_off_Month_End_Transactions,name='Item_Write_off_Month_End_Transactions'),
    path('Item_Write_off_Year_End_Transactions/', shop_views.Item_Write_off_Year_End_Transactions,name='Item_Write_off_Year_End_Transactions'),

    path('Members_Credit_sales_list_search/', shop_views.Members_Credit_sales_list_search,name='Members_Credit_sales_list_search'),
    path('Members_Credit_sales_list_load/', shop_views.Members_Credit_sales_list_load,name='Members_Credit_sales_list_load'),
    path('Members_Credit_sales_item_select/<str:pk>/', shop_views.Members_Credit_sales_item_select,name='Members_Credit_sales_item_select'),

    path('members_credit_issue_auction_item/<str:pk>/<str:member_id>/', shop_views.members_credit_issue_auction_item,name='members_credit_issue_auction_item'),
    path('members_credit_issue_item/<str:pk>/<str:member_id>/', shop_views.members_credit_issue_item,name='members_credit_issue_item'),
    path('Members_Credit_sales_item_select_remove/<str:pk>/<str:member_id>/', shop_views.Members_Credit_sales_item_select_remove,name='Members_Credit_sales_item_select_remove'),

    path('members_credit_sales_item_select_preview/<str:pk>/<str:ticket>/', shop_views.members_credit_sales_item_select_preview,name='members_credit_sales_item_select_preview'),
    path('members_credit_sales_summary_add/<str:member_id>/<str:debit>/<str:credit>/<str:balance>/<str:ticket>/', shop_views.members_credit_sales_summary_add,name='members_credit_sales_summary_add'),


    path('members_credit_purchase_manage/', shop_views.members_credit_purchase_manage,name='members_credit_purchase_manage'),
    path('members_credit_sales_manage_preview/<str:ticket>/', shop_views.members_credit_sales_manage_preview,name='members_credit_sales_manage_preview'),

    path('members_credit_purchase_selection_reset_confirmation/<str:ticket>/', shop_views.members_credit_purchase_selection_reset_confirmation,name='members_credit_purchase_selection_reset_confirmation'),
    path('members_credit_purchase_selection_reset_update/<str:ticket>/', shop_views.members_credit_purchase_selection_reset_update,name='members_credit_purchase_selection_reset_update'),

    path('members_credit_purchase_selection_discard_confirmation/<str:ticket>/', shop_views.members_credit_purchase_selection_discard_confirmation,name='members_credit_purchase_selection_discard_confirmation'),
    path('members_credit_purchase_selection_discard_update/<str:ticket>/', shop_views.members_credit_purchase_selection_discard_update,name='members_credit_purchase_selection_discard_update'),

    path('members_credit_sales_approved_list/', shop_views.members_credit_sales_approved_list,name='members_credit_sales_approved_list'),
    path('members_credit_sales_approved_item_details/<str:ticket>/', shop_views.members_credit_sales_approved_item_details,name='members_credit_sales_approved_item_details'),

    path('members_credit_sales_debt_recovery_cash_payment_search/', shop_views.members_credit_sales_debt_recovery_cash_payment_search,name='members_credit_sales_debt_recovery_cash_payment_search'),
    path('members_credit_sales_debt_recovery_cash_payment_list_load/', shop_views.members_credit_sales_debt_recovery_cash_payment_list_load,name='members_credit_sales_debt_recovery_cash_payment_list_load'),
    path('members_credit_sales_debt_recovery_cash_payment_levels/<str:pk>/', shop_views.members_credit_sales_debt_recovery_cash_payment_levels,name='members_credit_sales_debt_recovery_cash_payment_levels'),
    path('members_credit_sales_debt_recovery_cash_payment_current_day/<str:pk>/', shop_views.members_credit_sales_debt_recovery_cash_payment_current_day,name='members_credit_sales_debt_recovery_cash_payment_current_day'),

    path('members_credit_sales_debt_recovery_cash_payment_daily_summary_list_load/', shop_views.members_credit_sales_debt_recovery_cash_payment_daily_summary_list_load,name='members_credit_sales_debt_recovery_cash_payment_daily_summary_list_load'),
    path('members_credit_sales_debt_recovery_cash_payment_Day_End_Transaction_list_load/', shop_views.members_credit_sales_debt_recovery_cash_payment_Day_End_Transaction_list_load,name='members_credit_sales_debt_recovery_cash_payment_Day_End_Transaction_list_load'),
    path('members_credit_sales_debt_recovery_cash_payment_Month_End_Transaction_list_load/', shop_views.members_credit_sales_debt_recovery_cash_payment_Month_End_Transaction_list_load,name='members_credit_sales_debt_recovery_cash_payment_Month_End_Transaction_list_load'),
    path('members_credit_sales_debt_recovery_cash_payment_Year_End_Transaction_list_load/', shop_views.members_credit_sales_debt_recovery_cash_payment_Year_End_Transaction_list_load,name='members_credit_sales_debt_recovery_cash_payment_Year_End_Transaction_list_load'),

    path('members_credit_sales_debt_recovery_cash_payment_after_transaction_list_load/<str:pk>/', shop_views.members_credit_sales_debt_recovery_cash_payment_after_transaction_list_load,name='members_credit_sales_debt_recovery_cash_payment_after_transaction_list_load'),
    path('members_credit_sales_debt_recovery_cash_payment_after_transaction_delete/<str:pk>/', shop_views.members_credit_sales_debt_recovery_cash_payment_after_transaction_delete,name='members_credit_sales_debt_recovery_cash_payment_after_transaction_delete'),



    path('general_cash_sales_dashboard/', shop_views.general_cash_sales_dashboard,name='general_cash_sales_dashboard'),
    path('general_cash_sales_products_load_routes/', shop_views.general_cash_sales_products_load_routes,name='general_cash_sales_products_load_routes'),

    # path('general_cash_sales_products_load_route/', shop_views.general_cash_sales_products_load_route,name='general_cash_sales_products_load_route'),
    path('general_cash_sales_products_load/<str:pk>/<str:ticket>/', shop_views.general_cash_sales_products_load,name='general_cash_sales_products_load'),
    path('general_cash_issue_item/<str:pk>/<str:cust_id>/', shop_views.general_cash_issue_item,name='general_cash_issue_item'),
    path('general_cash_sales_select_remove/<str:pk>/<str:cust_id>/<str:ticket>/', shop_views.general_cash_sales_select_remove,name='general_cash_sales_select_remove'),

    path('general_cash_issue_auction_item/<str:pk>/<str:cust_id>/<str:ticket>/', shop_views.general_cash_issue_auction_item,name='general_cash_issue_auction_item'),

    path('general_cash_issue_item_preview/<str:ticket>/', shop_views.general_cash_issue_item_preview,name='general_cash_issue_item_preview'),
    path('general_cash_issue_item_print_receipt/<str:ticket>/', shop_views.general_cash_issue_item_print_receipt,name='general_cash_issue_item_print_receipt'),

    path('general_cash_issue_item_discard_payment/<str:ticket>/<str:pk>/', shop_views.general_cash_issue_item_discard_payment,name='general_cash_issue_item_discard_payment'),

    path('general_cash_load_existing_customers_search/', shop_views.general_cash_load_existing_customers_search,name='general_cash_load_existing_customers_search'),
    path('general_cash_load_existing_customers/', shop_views.general_cash_load_existing_customers,name='general_cash_load_existing_customers'),

    path('auction_stock_item_list/', shop_views.auction_stock_item_list,name='auction_stock_item_list'),


    path('check_code_exist/', shop_views.check_code_exist,name='check_code_exist'),
    path('check_receipt_no_exist/', shop_views.check_receipt_no_exist,name='check_receipt_no_exist'),

    path('members_credit_sales_status_search/', shop_views.members_credit_sales_status_search,name='members_credit_sales_status_search'),
    path('members_credit_sales_status_list_load/', shop_views.members_credit_sales_status_list_load,name='members_credit_sales_status_list_load'),
    path('members_credit_sales_status_details/<str:pk>/', shop_views.members_credit_sales_status_details,name='members_credit_sales_status_details'),
    path('members_credit_sales_status_details_preview/<str:pk>/', shop_views.members_credit_sales_status_details_preview,name='members_credit_sales_status_details_preview'),

    path('members_shop_credit_loan_salary_institution_select/', shop_views.members_shop_credit_loan_salary_institution_select,name='members_shop_credit_loan_salary_institution_select'),
    path('members_shop_sales_credit_generate/<str:pk>/', shop_views.members_shop_sales_credit_generate,name='members_shop_sales_credit_generate'),
    # path('members_shop_sales_credit_generate_details/<str:pk>/', shop_views.members_shop_sales_credit_generate_details,name='members_shop_sales_credit_generate_details'),

    path('Item_Return_Search_Page/', shop_views.Item_Return_Search_Page,name='Item_Return_Search_Page'),
    path('Item_Return_list_load/', shop_views.Item_Return_list_load,name='Item_Return_list_load'),
    path('Item_Return_Select/<str:pk>/', shop_views.Item_Return_Select,name='Item_Return_Select'),
    path('Item_Return_Process/<str:pk>/', shop_views.Item_Return_Process,name='Item_Return_Process'),
    path('Item_Return_Process_Type/<str:pk>/', shop_views.Item_Return_Process_Type,name='Item_Return_Process_Type'),
    path('Item_Return_Process_Stock_List_Load/<str:pk>/', shop_views.Item_Return_Process_Stock_List_Load,name='Item_Return_Process_Stock_List_Load'),
    path('Item_Return_Process_issue_item/<str:pk>/<str:item_return>/', shop_views.Item_Return_Process_issue_item,name='Item_Return_Process_issue_item'),
    path('Item_Return_Process_issue_item_Delete/<str:pk>/<str:item_return>/', shop_views.Item_Return_Process_issue_item_Delete,name='Item_Return_Process_issue_item_Delete'),
    path('Item_Return_Process_issue_item_Preview/<str:pk>/', shop_views.Item_Return_Process_issue_item_Preview,name='Item_Return_Process_issue_item_Preview'),
    path('Item_Return_Process_issue_item_processing/<str:pk>/<str:channel>/<str:receipt_type>/', shop_views.Item_Return_Process_issue_item_processing,name='Item_Return_Process_issue_item_processing'),
    path('Item_Return_Process_issue_item_processing_Daily_Summary/', shop_views.Item_Return_Process_issue_item_processing_Daily_Summary,name='Item_Return_Process_issue_item_processing_Daily_Summary'),
    path('Item_Return_Process_issue_item_processing_Day_End_Transaction/', shop_views.Item_Return_Process_issue_item_processing_Day_End_Transaction,name='Item_Return_Process_issue_item_processing_Day_End_Transaction'),
    path('Item_Return_Process_issue_item_processing_Month_End_Transaction/', shop_views.Item_Return_Process_issue_item_processing_Month_End_Transaction,name='Item_Return_Process_issue_item_processing_Month_End_Transaction'),
    path('Item_Return_Process_issue_item_processing_Year_End_Transaction/', shop_views.Item_Return_Process_issue_item_processing_Year_End_Transaction,name='Item_Return_Process_issue_item_processing_Year_End_Transaction'),


    path('Item_Return_Manage_List_Load/', shop_views.Item_Return_Manage_List_Load,name='Item_Return_Manage_List_Load'),
    path('Item_Return_Manage_List_Delete/<str:pk>/', shop_views.Item_Return_Manage_List_Delete,name='Item_Return_Manage_List_Delete'),

    path('stock_status_search/', shop_views.stock_status_search,name='stock_status_search'),
    path('stock_status_list_load/', shop_views.stock_status_list_load,name='stock_status_list_load'),
    path('stock_status_list_details/<str:pk>/', shop_views.stock_status_list_details,name='stock_status_list_details'),


    path('monthly_deductions_salary_institution_select/', shop_views.monthly_deductions_salary_institution_select,name='monthly_deductions_salary_institution_select'),
    path('monthly_individual_deductions_generate/<str:pk>/', shop_views.monthly_individual_deductions_generate,name='monthly_individual_deductions_generate'),

    path('monthly_grouped_deductions_salary_institution_select/', shop_views.monthly_grouped_deductions_salary_institution_select,name='monthly_grouped_deductions_salary_institution_select'),
    path('monthly_grouped_deductions_generated/<str:pk>/', shop_views.monthly_grouped_deductions_generated,name='monthly_grouped_deductions_generated'),

    path('Shop_Account_Deductions_Upload_salary_institution_select/', shop_views.Shop_Account_Deductions_Upload_salary_institution_select,name='Shop_Account_Deductions_Upload_salary_institution_select'),
    path('Shop_Account_Deductions_Upload_Load/<str:pk>/', shop_views.Shop_Account_Deductions_Upload_Load,name='Shop_Account_Deductions_Upload_Load'),


    path('Delete_Daily_Sales/', shop_views.Delete_Daily_Sales,name='Delete_Daily_Sales'),
    path('Delete_Daily_Sales1/', shop_views.Delete_Daily_Sales1,name='Delete_Daily_Sales1'),


    path('Members_Credit_sales_Cash_Deposit_search/', shop_views.Members_Credit_sales_Cash_Deposit_search,name='Members_Credit_sales_Cash_Deposit_search'),
    path('Members_Credit_sales_Cash_Deposit_list_load/', shop_views.Members_Credit_sales_Cash_Deposit_list_load,name='Members_Credit_sales_Cash_Deposit_list_load'),
    path('Members_Credit_sales_Cash_Deposit_Details/<str:pk>/', shop_views.Members_Credit_sales_Cash_Deposit_Details,name='Members_Credit_sales_Cash_Deposit_Details'),

    path('Members_Credit_sales_Cash_Deposit_Distributions_list_load/', shop_views.Members_Credit_sales_Cash_Deposit_Distributions_list_load,name='Members_Credit_sales_Cash_Deposit_Distributions_list_load'),
    path('Members_Credit_sales_Cash_Deposit_Distributions_Process/<str:pk>/', shop_views.Members_Credit_sales_Cash_Deposit_Distributions_Process,name='Members_Credit_sales_Cash_Deposit_Distributions_Process'),
    path('Members_Credit_sales_Cash_Deposit_Distributions_Add/<str:pk>/', shop_views.Members_Credit_sales_Cash_Deposit_Distributions_Add,name='Members_Credit_sales_Cash_Deposit_Distributions_Add'),
    path('Members_Credit_sales_Cash_Deposit_Distributions_Transaction_Select/<str:pk>/<str:member_id>/', shop_views.Members_Credit_sales_Cash_Deposit_Distributions_Transaction_Select,name='Members_Credit_sales_Cash_Deposit_Distributions_Transaction_Select'),
    path('Members_Credit_sales_Cash_Deposit_Distributions_Transaction_Drop/<str:pk>/<str:member_id>/', shop_views.Members_Credit_sales_Cash_Deposit_Distributions_Transaction_Drop,name='Members_Credit_sales_Cash_Deposit_Distributions_Transaction_Drop'),

    path('Members_Credit_sales_Cash_Deposit_Distributions_Add_2nd_level/<str:pk>/', shop_views.Members_Credit_sales_Cash_Deposit_Distributions_Add_2nd_level,name='Members_Credit_sales_Cash_Deposit_Distributions_Add_2nd_level'),
    path('Members_Credit_sales_Cash_Deposit_Distributions_Transaction_2nd_Level_Select/<str:pk>/<str:member_id>/', shop_views.Members_Credit_sales_Cash_Deposit_Distributions_Transaction_2nd_Level_Select,name='Members_Credit_sales_Cash_Deposit_Distributions_Transaction_2nd_Level_Select'),

    path('Cash_Deposit_Summary/', shop_views.Cash_Deposit_Summary,name='Cash_Deposit_Summary'),
    path('Cash_Deposit_Day_End_Transactions/', shop_views.Cash_Deposit_Day_End_Transactions,name='Cash_Deposit_Day_End_Transactions'),
    path('Cash_Deposit_Month_End_Transactions/', shop_views.Cash_Deposit_Month_End_Transactions,name='Cash_Deposit_Month_End_Transactions'),
    path('Cash_Deposit_Year_End_Transactions/', shop_views.Cash_Deposit_Year_End_Transactions,name='Cash_Deposit_Year_End_Transactions'),

    path('Expiring_Date_Tracking_search/', shop_views.Expiring_Date_Tracking_search,name='Expiring_Date_Tracking_search'),
    path('Expiring_Date_Tracking_Product_Load/', shop_views.Expiring_Date_Tracking_Product_Load,name='Expiring_Date_Tracking_Product_Load'),
    path('Expiring_Date_Tracking_Product_Preview/<str:pk>/', shop_views.Expiring_Date_Tracking_Product_Preview,name='Expiring_Date_Tracking_Product_Preview'),

    path('Expiring_Products_Tracking_Load/', shop_views.Expiring_Products_Tracking_Load,name='Expiring_Products_Tracking_Load'),
    path('Expiring_Products_Tracking_Auction_Product_select/<str:pk>/', shop_views.Expiring_Products_Tracking_Auction_Product_select,name='Expiring_Products_Tracking_Auction_Product_select'),

    path('Expired_Products_Main_Tracking_Load/', shop_views.Expired_Products_Main_Tracking_Load,name='Expired_Products_Main_Tracking_Load'),
    path('Expired_Products_Main_Tracking_Write_Off/<str:pk>/', shop_views.Expired_Products_Main_Tracking_Write_Off,name='Expired_Products_Main_Tracking_Write_Off'),

    path('Expired_Products_Auction_Tracking_Load/', shop_views.Expired_Products_Auction_Tracking_Load,name='Expired_Products_Auction_Tracking_Load'),
    path('Expired_Products_Auction_Tracking_Write_Off/<str:pk>/', shop_views.Expired_Products_Auction_Tracking_Write_Off,name='Expired_Products_Auction_Tracking_Write_Off'),

    path('Members_Credit_sales_ledger_search/', shop_views.Members_Credit_sales_ledger_search,name='Members_Credit_sales_ledger_search'),
    path('Members_Credit_sales_ledger_list_load/', shop_views.Members_Credit_sales_ledger_list_load,name='Members_Credit_sales_ledger_list_load'),
    path('Members_Credit_sales_ledger_preview/<str:pk>/', shop_views.Members_Credit_sales_ledger_preview,name='Members_Credit_sales_ledger_preview'),
    path('Members_Credit_sales_ledger_details/<str:pk>/', shop_views.Members_Credit_sales_ledger_details,name='Members_Credit_sales_ledger_details'),

    path('Daily_Sales_Summarization/<str:pk>/', shop_views.Daily_Sales_Summarization,name='Daily_Sales_Summarization'),
    path('Daily_Sales_Summary_Detail/<str:pk>/', shop_views.Daily_Sales_Summary_Detail,name='Daily_Sales_Summary_Detail'),

    path('Day_End_Transaction_Summary/', shop_views.Day_End_Transaction_Summary,name='Day_End_Transaction_Summary'),
    path('Day_End_Transaction_Summary_Details/<str:pk>/<str:tday>/<str:tmonth>/<str:tyear>/', shop_views.Day_End_Transaction_Summary_Details,name='Day_End_Transaction_Summary_Details'),

    path('Month_End_Transaction_Summary/', shop_views.Month_End_Transaction_Summary,name='Month_End_Transaction_Summary'),


    path('Year_End_Transaction_Summary/', shop_views.Year_End_Transaction_Summary,name='Year_End_Transaction_Summary'),

    path('Stock_Status/', shop_views.Stock_Status,name='Stock_Status'),
    path('Manage_Stock_Product_Lock/', shop_views.Manage_Stock_Product_Lock,name='Manage_Stock_Product_Lock'),
    path('Manage_Stock_Product_Lock_Individuals/<str:pk>/', shop_views.Manage_Stock_Product_Lock_Individuals,name='Manage_Stock_Product_Lock_Individuals'),
    path('Manage_Stock_Product_UnLock_Individuals/<str:pk>/', shop_views.Manage_Stock_Product_UnLock_Individuals,name='Manage_Stock_Product_UnLock_Individuals'),
    path('Manage_Stock_Product_Lock_Multiple/', shop_views.Manage_Stock_Product_Lock_Multiple,name='Manage_Stock_Product_Lock_Multiple'),
    path('Manage_Stock_Product_UNLock_Multiple/', shop_views.Manage_Stock_Product_UNLock_Multiple,name='Manage_Stock_Product_UNLock_Multiple'),

    path('Manage_Stock_Product_load_All/', shop_views.Manage_Stock_Product_load_All,name='Manage_Stock_Product_load_All'),
    path('Manage_Stock_Product_Update_All/<str:pk>/', shop_views.Manage_Stock_Product_Update_All,name='Manage_Stock_Product_Update_All'),
    path('Manage_Stock_Product_load_All/<str:pk>/', shop_views.Manage_Stock_Product_load_All,name='Manage_Stock_Product_load_All'),

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
    path('Purchase_Tracking_Invoice_Delete/<str:pk>/', shop_views.Purchase_Tracking_Invoice_Delete,name='Purchase_Tracking_Invoice_Delete'),


    path('Purchase_Certification_List_load/', shop_views.Purchase_Certification_List_load,name='Purchase_Certification_List_load'),
    path('Purchase_Certification_item_Preview/<str:pk>/', shop_views.Purchase_Certification_item_Preview,name='Purchase_Certification_item_Preview'),
    path('Purchase_Certification_item_Edit/<str:pk>/', shop_views.Purchase_Certification_item_Edit,name='Purchase_Certification_item_Edit'),
    path('Purchase_Certification_item_Preview_Remove/<str:pk>/', shop_views.Purchase_Certification_item_Preview_Remove,name='Purchase_Certification_item_Preview_Remove'),
    path('Purchase_Certification_item_Preview_Reload/<str:pk>/', shop_views.Purchase_Certification_item_Preview_Reload,name='Purchase_Certification_item_Preview_Reload'),
    path('Purchase_Certification_item_Preview_Processed/<str:pk>/', shop_views.Purchase_Certification_item_Preview_Processed,name='Purchase_Certification_item_Preview_Processed'),

    path('Purchase_Certification_item_Add_Item/<str:pk>/', shop_views.Purchase_Certification_item_Add_Item,name='Purchase_Certification_item_Add_Item'),
    path('Purchase_Certification_Product_Purchase_Details_Select/<str:pk>/<str:invoice_id>/', shop_views.Purchase_Certification_Product_Purchase_Details_Select,name='Purchase_Certification_Product_Purchase_Details_Select'),

    path('Purchase_Certification_item_Add_Stock/<str:pk>/', shop_views.Purchase_Certification_item_Add_Stock,name='Purchase_Certification_item_Add_Stock'),

    path('Product_Purchase_Day_End_Transaction/', shop_views.Product_Purchase_Day_End_Transaction,name='Product_Purchase_Day_End_Transaction'),
    path('Product_Purchase_Month_End_Transaction/', shop_views.Product_Purchase_Month_End_Transaction,name='Product_Purchase_Month_End_Transaction'),
    path('Product_Purchase_Year_End_Transaction/', shop_views.Product_Purchase_Year_End_Transaction,name='Product_Purchase_Year_End_Transaction'),

    path('Stock_Taken/', shop_views.Stock_Taken,name='Stock_Taken'),
    path('Stock_Without_Prices/', shop_views.Stock_Without_Prices,name='Stock_Without_Prices'),
    path('Stock_Without_Prices_Update/<str:pk>/', shop_views.Stock_Without_Prices_Update,name='Stock_Without_Prices_Update'),

    ################################################################
    ########################## REPORTS #############################
    ################################################################


    path('Members_Welfare_Report_Search/', deskofficer_views.Members_Welfare_Report_Search,name='Members_Welfare_Report_Search'),
    path('Members_Welfare_Report_list_load/', deskofficer_views.Members_Welfare_Report_list_load,name='Members_Welfare_Report_list_load'),
    path('Members_Welfare_Report_details/<str:pk>/', deskofficer_views.Members_Welfare_Report_details,name='Members_Welfare_Report_details'),

    path('Members_Welfare_Report_General_Records/', deskofficer_views.Members_Welfare_Report_General_Records,name='Members_Welfare_Report_General_Records'),
    path('Members_Welfare_Report_General_Record_details/<str:pk>/<str:member_id>/', deskofficer_views.Members_Welfare_Report_General_Record_details,name='Members_Welfare_Report_General_Record_details'),

    path('Members_Cleared_Loans_Records/', deskofficer_views.Members_Cleared_Loans_Records,name='Members_Cleared_Loans_Records'),
    path('Members_Cleared_Loans_Records_Details/<str:pk>/', deskofficer_views.Members_Cleared_Loans_Records_Details,name='Members_Cleared_Loans_Records_Details'),


    path('GeneratePdf/', shop_views.GeneratePdf.as_view(),name='GeneratePdf'),
    path('GeneratePdf2/', shop_views.GeneratePdf2.as_view(),name='GeneratePdf2'),
    path('GeneratePdf3/', shop_views.GeneratePdf3.as_view(),name='GeneratePdf3'),
    path('GeneratePdf4/', shop_views.GeneratePdf4.as_view(),name='GeneratePdf4'),
    path('All_Stock_Status_Pdf/', shop_views.All_Stock_Status_Pdf,name='All_Stock_Status_Pdf'),

    path('All_Stock_Status/', shop_views.All_Stock_Status,name='All_Stock_Status'),
    path('Purchase_Summary/', shop_views.Purchase_Summary,name='Purchase_Summary'),
    path('Purchase_Summary_Details/<str:pk>/', shop_views.Purchase_Summary_Details,name='Purchase_Summary_Details'),

    path('All_Auction_Stock_Status/', shop_views.All_Auction_Stock_Status,name='All_Auction_Stock_Status'),


    path('Daily_Sales_Report/', shop_views.Daily_Sales_Report,name='Daily_Sales_Report'),


    path('Daily_Sales_Report_Summary/', shop_views.Daily_Sales_Report_Summary,name='Daily_Sales_Report_Summary'),
    path('Daily_Sales_Report_Details/<str:pk>/', shop_views.Daily_Sales_Report_Details,name='Daily_Sales_Report_Details'),
    path('Daily_Sales_Report_Receipt_Details/<str:pk>/', shop_views.Daily_Sales_Report_Receipt_Details,name='Daily_Sales_Report_Receipt_Details'),
    path('Daily_Sales_Report_All_Details/<str:year>/<str:month>/<str:day>/<str:sales_category>/', shop_views.Daily_Sales_Report_All_Details,name='Daily_Sales_Report_All_Details'),

    path('Daily_Sales_All_Category_Report_Details/<str:d1>/<str:m1>/<str:y1>/<str:d2>/<str:m2>/<str:y2>/', shop_views.Daily_Sales_All_Category_Report_Details,name='Daily_Sales_All_Category_Report_Details'),

    path('Expenditure_Manager/', shop_views.Expenditure_Manager,name='Expenditure_Manager'),
    path('Expenditure_Discard/<str:pk>/', shop_views.Expenditure_Discard,name='Expenditure_Discard'),
    path('Expenditure_Daily_Summary/', shop_views.Expenditure_Daily_Summary,name='Expenditure_Daily_Summary'),
    path('Expenditure_Day_End_Summary/', shop_views.Expenditure_Day_End_Summary,name='Expenditure_Day_End_Summary'),
    path('Expenditure_Month_End_Summary/', shop_views.Expenditure_Month_End_Summary,name='Expenditure_Month_End_Summary'),
    path('Expenditure_Year_End_Summary/', shop_views.Expenditure_Year_End_Summary,name='Expenditure_Year_End_Summary'),

    path('CashBook_Shop_Display/', shop_views.CashBook_Shop_Display,name='CashBook_Shop_Display'),

    path('load_branches/', shop_views.load_branches,name='ajax_load_branches'),


]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
