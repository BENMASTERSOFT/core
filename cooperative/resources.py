from import_export import resources
from cooperative.models import AccountDeductions,NorminalRoll, Stock


class AccountDeductionsResource(resources.ModelResource):
	class meta:
		model = AccountDeductions
		
class NorminalRollResource(resources.ModelResource):
	class meta:
		model = NorminalRoll


class StockListResource(resources.ModelResource):
	class meta:
		model = Stock
		