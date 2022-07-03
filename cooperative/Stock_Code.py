from .models import Product_Code


def get_stock_code():
    code=Product_Code.objects.first()

    r_code=str(code.code).zfill(5)
    code.code=int(r_code) + 1
    code.save()
    return r_code