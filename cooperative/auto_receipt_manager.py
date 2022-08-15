from .models import AutoReceipt 


def get_receipt():
    receipt_obj=AutoReceipt.objects.first()
    receipt= str(receipt_obj.receipt).zfill(5)
    receipt_obj.receipt=int(receipt_obj.receipt)+1
    receipt_obj.save()
    return receipt