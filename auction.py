# def members_credit_sales_auction_approved_list(request):
#   task_array=[]
#   tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
#   for task in tasks:
#       task_array.append(task.task.title)

#   status=TransactionStatus.objects.get(title="UNTREATED")
#   approval_status=ApprovalStatus.objects.get(title='PENDING')
#   approval_status1=ApprovalStatus.objects.get(title='APPROVED')
#   items=members_credit_sales_summary.objects.filter(status=status).exclude(approval_status=approval_status)
    

#   context={
#   'task_array':task_array,
#   'items':items,
#   'approval_status1':approval_status1,

#   }
#   return render(request,'shop_templates/members_credit_sales_auction_approved_list.html',context)


# def members_credit_sales_auction_approved_item_details(request,ticket):
#   task_array=[]
#   tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
#   for task in tasks:
#       task_array.append(task.task.title)

#   form=Shop_Issue_Receipt_form(request.POST or None)
    
#   status=TransactionStatus.objects.get(title="TREATED")   
#   status2=TransactionStatus.objects.get(title="UNTREATED")

    
#   autoprint=YesNo.objects.all()
#   autoFormPrint=[]
#   if FormAutoPrints.objects.filter(title='SHOP SALES').exists():
#       autoFormPrint=FormAutoPrints.objects.get(title='SHOP SALES')

#   items=Members_Credit_Sales_Selected.objects.filter(ticket=ticket)
#   if not items:
#       return HttpResponseRedirect(reverse('members_credit_sales_auction_approved_list'))
#   amount_due=0

#   total=Members_Credit_Sales_Selected.objects.filter(ticket=ticket).aggregate(total_amount=Sum('total'))
    
#   if float(total['total_amount']):
#       amount_due=float(total['total_amount'])
    

#   item=members_credit_sales_summary.objects.get(trans_code__ticket=ticket)
#   transaction=TransactionTypes.objects.get(code=600)


#   if request.method=="POST":
        
#       tdate =  get_current_date(now)
#       autoprint_id = request.POST.get('autoprint')
#       autoprint=YesNo.objects.get(id=autoprint_id)

#       if MembersAccountsDomain.objects.filter(member=item.trans_code.member,transaction=transaction).exists():
#           member=MembersAccountsDomain.objects.get(member=item.trans_code.member,transaction=transaction)
#       else:
#           messages.error(request,"This Transaction Has no Account Number")
#           return HttpResponseRedirect(reverse('members_credit_sales_auction_approved_item_details', args=(ticket,)))

#       receipt_types_id=request.POST.get('receipt_types')
#       receipt_types=ReceiptTypes.objects.get(id=receipt_types_id)

#       if receipt_types.title=="MANUAL":
#           # return HttpResponse("MANUAL")
#           receipt_status=ReceiptStatus.objects.get(title='USED')
#           receipt_id=request.POST.get('receipt_no')       
            
            
#           if Receipts_Shop.objects.filter(receipt=receipt_id,status=receipt_status).exists():
#               messages.error(request,"This Receipt is Already in Use")
#               return HttpResponseRedirect(reverse('members_credit_sales_auction_approved_item_details',args=(ticket,)))
                
#           receipt_id=Receipts_Shop.objects.get(receipt=receipt_id)
#           receipt=receipt_id.receipt
#           receipt_id.status=receipt_status
#           receipt_id.save()

#       elif receipt_types.title=="AUTO":
#           # return HttpResponse("Auto")
#           receipt_id=AutoReceipt.objects.first()
#           receipt="AUT-" + str(receipt_id.receipt.zfill(5))
#           receipt_id.receipt=int(receipt_id.receipt)+1
#           receipt_id.save()


#       else:
#           # return HttpResponse("None")
#           messages.error(request,'Invalid Receipt Type Selection')
#           return HttpResponseRedirect(reverse('members_credit_sales_auction_approved_item_details',args=(ticket,)))

        
#       for item in items:
#           product_update=Stock_Auction.objects.get(stock__code=item.product.code)
    
#           if int(item.quantity) > int(product_update.quantity):
#               messages.error(request,"Insufficient Quantity for product with code " + str(item.product.code))
#               return HttpResponseRedirect(reverse('members_credit_sales_auction_approved_item_details',args=(ticket,)))

#       # grand_total=0
#       processed_by=CustomUser.objects.get(id=request.user.id)
#       sales_category=SalesCategory.objects.get(title='CREDIT')

#       for item in items:  
#           name = item.member.get_full_name
#           if item.member.residential_address:
#               address=item.member.residential_address
#           else:
#               address="FETHA II CTCS"
#           phone_no=item.member.phone_number
#           item_name=item.product.item_name.upper()
#           item_code=item.product.code
#           quantity=item.quantity
#           unit_selling_price=item.unit_selling_price
#           total=item.total

#           # grand_total=grand_total+float(item.total)
            
            

#           record=Daily_Sales(sales_category=sales_category,tdate=tdate,receipt=receipt,name=name,phone_no=phone_no,address=address,product=item.product,ticket=item.ticket,quantity=quantity,unit_selling_price=unit_selling_price,total=total,processed_by=item.processed_by,status=status)
#           record.save()

#           product_update=Stock_Auction.objects.get(stock__code=item_code)
#           product_update.quantity=int(product_update.quantity)-int(quantity)
#           product_update.save()
        
        
#       selected=Daily_Sales.objects.filter(ticket=ticket).first()
    

#       record=Daily_Sales_Summary(tdate=tdate,receipt=receipt,sale=selected,amount=amount_due,status=status)
#       record.save()
        
        
#       particulars="Purchases with receipt No " + str(receipt)
#       balance_amount= -float(amount_due)
#       debit_amount = amount_due
        

        
#       if CooperativeShopLedger.objects.filter(member=member.member).exists():
#           ledger_balance = CooperativeShopLedger.objects.filter(member=member.member).order_by('id').last()
            
#           balance_amount=float(ledger_balance.balance) - float(amount_due)
            
            
#       record=CooperativeShopLedger(status=status2,tdate=tdate,receipt=receipt,member=member.member,particulars=particulars,debit=debit_amount,credit=0,balance=balance_amount,processed_by=processed_by)
#       record.save()

        
#       item=members_credit_sales_summary.objects.get(trans_code__ticket=ticket)
#       item.status=status
#       item.save()

#       if autoprint.title == "NO":

#           return HttpResponseRedirect(reverse('members_credit_sales_auction_approved_list'))
#       elif autoprint.title == 'YES':
#           return HttpResponseRedirect(reverse('general_cash_issue_item_print_receipt',args=(ticket,)))


#   context={
#   'task_array':task_array,
#   'form':form,
#   'items':items,
#   'full_name':items[0].member.get_full_name,
#   'amount_due':amount_due,
#   'autoprint':autoprint,
#   'autoFormPrint':autoFormPrint,
#   'transaction':transaction,
#   }
#   return render(request,'shop_templates/members_credit_sales_auction_approved_item_details.html',context)




 # <div class="row">
 #                    <div class="col-lg-3 col-md-6">
 #                        <div class="ibox bg-success color-white widget-stat">
 #                            <div class="ibox-body">
 #                                <!-- <h2 class="m-b-5 font-strong">{{members_credit_purchases}}</h2> -->
 #                                <div class="m-b-5"><a href="{% url 'Members_Credit_sales_Auction_list_search' %}" style="color:white;">MEMBERS CREDIT SALES</a> </div><i class="ti-shopping-cart widget-stat-icon"></i>
 #                                <div><i class="fa fa-level-up m-r-5"></i><small>Auction</small></div>
 #                            </div>
 #                        </div>
 #                    </div>
 #                    <div class="col-lg-3 col-md-6">
 #                        <div class="ibox bg-info color-white widget-stat">
 #                            <div class="ibox-body">
 #                                <!-- <h2 class="m-b-5 font-strong">0</h2> -->
 #                                <div class="m-b-5"><a href="{% url 'members_cash_sales_search' %}" style="color: white;">MEMBERS CASH SALE</a> S</div><i class="ti-bar-chart widget-stat-icon"></i>
 #                                <div><i class="fa fa-level-up m-r-5"></i><small>Auction</small></div>
 #                            </div>
 #                        </div>
 #                    </div>
 #                    <div class="col-lg-3 col-md-6">
 #                        <div class="ibox bg-warning color-white widget-stat">
 #                            <div class="ibox-body">
 #                                <!-- <h2 class="m-b-5 font-strong">0</h2> -->
 #                                <div class="m-b-5"><a href="{% url 'general_cash_sales_dashboard' %}" style="color: white;" > GENERAL CASH SALES</a></div><i class="fa fa-money widget-stat-icon"></i>
 #                                <div><i class="fa fa-level-up m-r-5"></i><small>Auction</small></div>
 #                            </div>
 #                        </div>
 #                    </div>
 #                    <div class="col-lg-3 col-md-6">
 #                        <div class="ibox bg-danger color-white widget-stat">
 #                            <div class="ibox-body">
 #                                <!-- <h2 class="m-b-5 font-strong">0</h2> -->
 #                                <div class="m-b-5"> <a href="{% url 'Daily_Sales_Summarization' request.user.id %}"  style="color: white;">DAILY SALES SUMMARY</a> </div><i class="ti-user widget-stat-icon"></i>
 #                                <div><i class="fa fa-level-down m-r-5"></i><small>Auction</small></div>
 #                            </div>
 #                        </div>
 #                    </div>
 #                </div>



 
# def Members_Credit_sales_Auction_list_search(request):
#   task_array=[]
#   tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
#   for task in tasks:
#       task_array.append(task.task.title)

#   title="Search Members for Auction Shopping"
#   form = searchForm(request.POST or None)
    
#   return render(request,'shop_templates/Members_Credit_sales_Auction_list_search.html',{'form':form,'title':title,'task_array':task_array})


# def Members_Credit_sales_Auction_list_load(request):
#   task_array=[]
#   tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
#   for task in tasks:
#       task_array.append(task.task.title)

#   title="Membership Auction Credit Purchases"
#   if request.method == "POST":
#       form = searchForm(request.POST)
#       status=MembershipStatus.objects.get(title="ACTIVE")
#       if not form['title'].value():
#           messages.info(request,'Not Matchimg Record Found')
#           return HttpResponseRedirect(reverse('Members_Credit_sales_Auction_list_search'))
        
#       members=searchMembers(form['title'].value(),status)
        
#       context={
#       'task_array':task_array,

#       'members':members,
#       'title':title,
#       }
#       return render(request,'shop_templates/Members_Credit_sales_Auction_list_load.html',context)


# def Members_Credit_sales_Auction_item_select(request,pk):
#   task_array=[]
#   tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
#   for task in tasks:
#       task_array.append(task.task.title)

#   status=TransactionStatus.objects.get(title='UNTREATED')
#   processed_by_id=request.user.id
#   processed_by=CustomUser.objects.get(id=processed_by_id)
#   items=Stock_Auction.objects.filter(Q(quantity__gt=0))
#   member=Members.objects.get(id=pk)
    
#   Members_Credit_Sales_Selected.objects.filter(~Q(member=member)).filter(status=status,processed_by=processed_by).delete()

                

#   status=TransactionStatus.objects.get(title="UNTREATED")
    
#   total_item=""
#   total_amount=""
#   ticket_holder=0
#   select_items=[]
#   if Members_Credit_Sales_Selected.objects.filter(member=member,status=status,processed_by=processed_by).exists():
#       button_show=True
#       select_items = Members_Credit_Sales_Selected.objects.filter(member=member,status=status,processed_by=processed_by)
#       queryset=Members_Credit_Sales_Selected.objects.filter(ticket=select_items[0].ticket).aggregate(total_amount=Sum('total'),total_item=Sum('quantity'))
#       total_item=queryset['total_item']
#       total_amount=queryset['total_amount']
#       ticket_holder=select_items[0].ticket
#   else:
#       button_show=False



#   context={
#   'task_array':task_array,
#   'items':items,
#   'member':member,
#   'select_items':select_items,
#   'total_amount':total_amount,
#   'total_item':total_item,
#   'ticket':ticket_holder,
#   'button_show':button_show,
#   }
#   return render(request,'shop_templates/Members_Credit_sales_Auction_item_select.html',context)



# def members_credit_sales_auction_issue_item(request,pk,member_id):
    
    
#   task_array=[]
#   tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
#   for task in tasks:
#       task_array.append(task.task.title)

#   form=members_credit_issue_item_form(request.POST or None)
#   member=Members.objects.get(id=member_id)
#   approval_status=ApprovalStatus.objects.get(title='PENDING')
#   status = TransactionStatus.objects.get(title='UNTREATED')

#   if members_credit_sales_summary.objects.filter(trans_code__member=member,approval_status=approval_status,status=status).exists():
#       messages.info(request,"You still have incomplete transaction, please discard or complete the existing transaction")
#       return HttpResponseRedirect(reverse('Members_Credit_sales_Auction_item_select', args=(member_id,)))
    


#   product = Stock_Auction.objects.get(id=pk)
    
#   form.fields['code'].initial=product.stock.code
#   form.fields['item_name'].initial=product.stock.item_name
#   form.fields['details'].initial=product.stock.details
#   form.fields['available_quantity'].initial=product.quantity
#   form.fields['unit_selling_price'].initial=product.unit_selling_price

#   if request.method=="POST":  
#       tdate =  get_current_date(now)

#       status=TransactionStatus.objects.get(title="UNTREATED")
#       quantity=request.POST.get('issue_quantity')
#       if int(quantity)<=0:
#           messages.error(request,"Quantity Selected cannot be Zero (0)")
#           return HttpResponseRedirect(reverse('members_credit_issue_item', args=(pk,member_id)))
        
#       if int(quantity)>int(product.quantity):
#           messages.error(request,"Quantity Selected is more that Available Quantity")
#           return HttpResponseRedirect(reverse('members_credit_issue_item', args=(pk,member_id)))
        

#       unit_selling_price=product.unit_selling_price
        
#       total=float(quantity) * float(unit_selling_price)
#       processed_by=CustomUser.objects.get(id=request.user.id)

#       if Members_Credit_Sales_Selected.objects.filter(member=member,status=status,processed_by=processed_by):
#           ticket_id=Members_Credit_Sales_Selected.objects.filter(member=member,status=status).first()
#           selected_ticket=ticket_id.ticket
#       else:
#           _ticket=GeneralTicket.objects.first()
#           selected_ticket=_ticket.ticket
            

#           _ticket.ticket = int(_ticket.ticket) + 1
#           _ticket.save()

#           # selected_ticket=str(now.year) +  str(now.month) +  str(now.day) + str(now.hour) +  str(now.minute) + str(now.second)


#       if Members_Credit_Sales_Selected.objects.filter(member=member,product=product.stock,status=status,processed_by=processed_by):
#           record_exist=Members_Credit_Sales_Selected.objects.filter(member=member,product=product.stock,status=status).first()
#           record_exist.quantity=quantity
#           record_exist.unit_selling_price=unit_selling_price
#           record_exist.total=total
#           record_exist.save()
#           return HttpResponseRedirect(reverse('Members_Credit_sales_Auction_item_select',args=(member_id,)))

#       record=Members_Credit_Sales_Selected(tdate=tdate,member=member,status=status,product=product.stock,ticket=selected_ticket,quantity=quantity,unit_selling_price=unit_selling_price,total=total,processed_by=processed_by)
#       record.save()
#       return HttpResponseRedirect(reverse('Members_Credit_sales_Auction_item_select',args=(member_id,)))
    
    

#   context={
#   'task_array':task_array,
#   'form':form,
#   'member':member,
#   }
#   return render(request,'shop_templates/members_credit_sales_auction_issue_item.html',context)



# def Members_Credit_sales_Auction_item_select_remove(request,pk,member_id):
#   item = Members_Credit_Sales_Selected.objects.get(id=pk)
#   item.delete()
#   return HttpResponseRedirect(reverse('Members_Credit_sales_Auction_item_select',args=(member_id,)))


# def members_credit_sales_auction_item_select_preview(request,pk,ticket):
#   task_array=[]
#   tasks=System_Users_Tasks_Model.objects.filter(user=request.user)
#   for task in tasks:
#       task_array.append(task.task.title)

#   form=Members_Credit_Sales_submit_form(request.POST or None)
    
#   sales = Members_Credit_Sales_Selected.objects.filter(ticket=ticket)
#   sum_sales=Members_Credit_Sales_Selected.objects.filter(ticket=ticket).aggregate(total_sales=Sum('total'))
    
#   if sum_sales['total_sales']:
#       sum_total=float(sum_sales['total_sales'])
#   else:
#       sum_total=0

#   status=TransactionStatus.objects.get(title='UNTREATED')
#   processing_status=ProcessingStatus.objects.get(title='UNPROCESSED')

#   member=Members.objects.get(id=pk)

#   if CompulsorySavings.objects.all().exists:
#       item = CompulsorySavings.objects.first()
#       if StandingOrderAccounts.objects.filter(transaction__member_id=pk,transaction__transaction=item.transaction).count():
#           pass
#       else:
#           messages.info(request,'Some Compulsory Savings are Missing')
#           return HttpResponseRedirect(reverse('Members_Credit_sales_item_select',args=(pk,)))
        
#   else:
#       messages.info(request,'No  Compulsory savings fixed')
#       return HttpResponseRedirect(reverse('Members_Credit_sales_item_select',args=(pk,)))
    
#   monthly_contributions= StandingOrderAccounts.objects.filter(transaction__member_id=pk)
#   sum_monthly_contributions = StandingOrderAccounts.objects.filter(transaction__member_id=pk).aggregate(total_contribution=Sum('amount'))
    
#   if sum_monthly_contributions['total_contribution']:
#       monthly_contribution_debit=float(sum_monthly_contributions['total_contribution'])
#   else:
#       monthly_contribution_debit=0

#   loan_repayments=LoansRepaymentBase.objects.filter(member_id=pk,balance__lt=0)
#   sum_loan_repayments=LoansRepaymentBase.objects.filter(member_id=pk,balance__lt=0).aggregate(total_loan=Sum('repayment'))
    
#   if sum_loan_repayments['total_loan']:
#       loan_repayment_debit=float(sum_loan_repayments['total_loan'])
#   else:
#       loan_repayment_debit=0

#   new_credit_sales = members_credit_sales_summary.objects.filter(trans_code__member=member,processing_status=processing_status)
#   sum_new_credit_sales=members_credit_sales_summary.objects.filter(trans_code__member=member,processing_status=processing_status).aggregate(total_sales=Sum('amount'))
    
#   if sum_new_credit_sales['total_sales']:
#       credit_sales_total=float(sum_new_credit_sales['total_sales'])
#   else:
#       credit_sales_total=0
    
    
#   amount = credit_sales_total + loan_repayment_debit + monthly_contribution_debit + abs(sum_total)
    
#   # Posting to Summary Table

#   if request.method=="POST":
#       tdate =  get_current_date(now)

#       trans_code = Members_Credit_Sales_Selected.objects.filter(ticket=ticket).first()
        
#       status=TransactionStatus.objects.get(title='UNTREATED')
#       status1=TransactionStatus.objects.get(title='TREATED')
#       approval_status=ApprovalStatus.objects.get(title="PENDING")
        
#       comment=request.POST.get('comment')
#       payment_date=request.POST.get('payment_date')
#       net_pay=request.POST.get('net_pay')

#       if not net_pay or float(net_pay) <= 0:
#           messages.info(request,'Net Pay is missing')
#           return HttpResponseRedirect(reverse('members_credit_sales_item_select_preview',args=(pk,ticket,)))


#       if members_credit_sales_summary.objects.filter(trans_code=trans_code).exists():
#           credit_sales_summary_record=members_credit_sales_summary.objects.get(trans_code=trans_code)
        
#           credit_sales_summary_record.approval_status=approval_status
#           credit_sales_summary_record.comment=comment
#           credit_sales_summary_record.amount=sum_total
#           credit_sales_summary_record.trans_code=trans_code
#           credit_sales_summary_record.status=status
#           credit_sales_summary_record.payment_date=payment_date
#           credit_sales_summary_record.net_pay=net_pay
#           credit_sales_summary_record.save()
#       else:
#           credit_sales_summary_record=members_credit_sales_summary(net_pay=net_pay,payment_date=payment_date,tdate=tdate,approval_status=approval_status,comment=comment,amount=sum_total,trans_code=trans_code,status=status)
#           credit_sales_summary_record.save()

#       particulars="Payment as at: " + str(payment_date)
#       credit_sales_analysis_record=members_credit_sales_analysis(tdate=tdate,trans_code=trans_code,particulars=particulars,debit=0,credit=net_pay,status=status)
#       credit_sales_analysis_record.save()
        

#       for monthly_contribution in monthly_contributions:
#           monthly_contribution_record=members_credit_sales_analysis(tdate=tdate,trans_code=trans_code,particulars=monthly_contribution.transaction.transaction.name,debit=monthly_contribution.amount,credit=0,status=status)
#           monthly_contribution_record.save()
        
#       for loan_repayment in loan_repayments:
#           loan_repayment_record=members_credit_sales_analysis(tdate=tdate,trans_code=trans_code,particulars=loan_repayment.transaction.name,debit=loan_repayment.repayment,credit=0,status=status)
#           loan_repayment_record.save()
        
#       if credit_sales_total:
#           new_credit_sale=members_credit_sales_analysis(tdate=tdate,trans_code=trans_code,particulars='COOPERATIVE SHOP',debit=credit_sales_total,credit=0,status=status)
#           new_credit_sale.save()

#       member.last_used_net_pay=net_pay
#       member.save()
        
#       source_update=Members_Credit_Sales_Selected.objects.filter(ticket=ticket).update(status=status1)
#       return HttpResponseRedirect(reverse('shop_home'))

#   # return HttpResponse(credit_sales_total)
#   form.fields['comment'].initial="FOR YOUR APPROVAL"
#   form.fields['payment_date'].initial=now
#   form.fields['net_pay'].initial=member.last_used_net_pay
#   context={
#   'task_array':task_array,
#   'member':member,
#   'monthly_contributions':monthly_contributions,
#   'loan_repayments':loan_repayments,
#   'credit_sales_total':credit_sales_total,
#   'amount':amount,
#   'new_purchase':sum_total,
#   'form':form,
#   'ticket':ticket,
#   'sales':sales,
#   'sum_total':sum_total,
#   }
#   return render(request,'shop_templates/members_credit_sales_auction_item_select_preview.html',context)


# class Expiring_Products_Tracking_Auction_Product_select_Form(forms.Form):
#    available_quantity = forms.IntegerField(initial=0,label='Available Quantity', label_suffix=" : ", min_value=0,  required=False,
#                                  widget=forms.NumberInput(attrs={'class': 'form-control','readonly':'readonly'}),
#                                 disabled = False, error_messages={'required': "Please Min Unit"})
  
#    expiry_quantity = forms.IntegerField(initial=0,label='Expiry Quantity', label_suffix=" : ", min_value=1,  required=False,
#                                  widget=forms.NumberInput(attrs={'class': 'form-control'}),
#                                 disabled = False, error_messages={'required': "Please Expiry Quantity"})
  
#    unit_selling_price = forms.DecimalField(initial=0,label='Unit Selling Price', label_suffix=" : ", min_value=1,  max_digits=20,
#                               widget=forms.NumberInput(attrs={'class': 'form-control'}),
#                               decimal_places=2, required=True, 
#                               disabled = False,
#                               error_messages={'required': "Please Enter Amount Paid"})
#    unit_cost_price = forms.DecimalField(initial=0,label='Unit Cost Price', label_suffix=" : ", min_value=1,  max_digits=20,
#                               widget=forms.NumberInput(attrs={'class': 'form-control'}),
#                               decimal_places=2, required=True, 
#                               disabled = False,
#                               error_messages={'required': "Please Enter Amount Paid"})

#    expiry_date = forms.DateField(label='Expiry Date', label_suffix=" : ",
#                                 required=True, disabled=False,
#                                 widget=DateInput(attrs={'class': 'form-control'}),
#                                 error_messages={'required': "This field is required."})
#   


# path('Members_Credit_sales_Auction_list_search/', shop_views.Members_Credit_sales_Auction_list_search,name='Members_Credit_sales_Auction_list_search'),
# path('Members_Credit_sales_Auction_list_load/', shop_views.Members_Credit_sales_Auction_list_load,name='Members_Credit_sales_Auction_list_load'),
# path('Members_Credit_sales_Auction_item_select/<str:pk>/', shop_views.Members_Credit_sales_Auction_item_select,name='Members_Credit_sales_Auction_item_select'),

# path('members_credit_sales_auction_issue_item/<str:pk>/<str:member_id>/', shop_views.members_credit_sales_auction_issue_item,name='members_credit_sales_auction_issue_item'),
# path('Members_Credit_sales_Auction_item_select_remove/<str:pk>/<str:member_id>/', shop_views.Members_Credit_sales_Auction_item_select_remove,name='Members_Credit_sales_Auction_item_select_remove'),

# path('members_credit_sales_auction_item_select_preview/<str:pk>/<str:ticket>/', shop_views.members_credit_sales_auction_item_select_preview,name='members_credit_sales_auction_item_select_preview'),

# path('members_credit_sales_auction_approved_list/', shop_views.members_credit_sales_auction_approved_list,name='members_credit_sales_auction_approved_list'),
# path('members_credit_sales_auction_approved_item_details/<str:ticket>/', shop_views.members_credit_sales_auction_approved_item_details,name='members_credit_sales_auction_approved_item_details'),
