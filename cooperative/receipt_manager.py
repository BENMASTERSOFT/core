from . models import AutoReceipt, Receipts_Shop, Receipts
from django.db.models import  F, CharField, Value as V

def generate_shop_receipt(source,receipt):
    if source == 'AUTO':
        receipt_id=AutoReceipt.objects.first()
        receipt= "AUT-" + str(receipt_id.receipt.zfill(5))
        receipt_id.receipt=int(receipt_id.receipt)+1
        receipt_id.save()
        return receipt 
    elif source == 'MANUAL':
        receipt_obj=Receipts_Shop.objects.get(receipt=receipt)
        receipt=receipt_obj.receipt
        return receipt


def generate_main_receipt(source,receipt):
    if source == 'MANUAL':
      
        if Receipts.objects.filter(receipt=receipt).exists():
            
            receipt_obj=Receipts.objects.get(receipt=receipt)
            receipt=receipt_obj.receipt
            
        else:
            return "a"
            
        
        if Receipts.objects.filter(receipt=receipt,status='USED').exists():
            return 'b'
        
        Receipts.objects.filter(receipt=receipt).update(status='USED')
        return receipt

    elif source == 'AUTO':
        receipt_id=AutoReceipt.objects.first()
        receipt='C-' + str(receipt_id.receipt).zfill(5)
        AutoReceipt.objects.filter().update(receipt=F('receipt')+1)
        return receipt