from .models import MonthlyDeductionList, MonthlyGeneratedTransactions,MonthlyDeductionGenerationHeading, \
					MonthlyGroupGeneratedTransactions, MonthlyDeductionListGenerated, \
					MonthlyJointDeductionList, MonthlyJointDeductionGeneratedTransactions, \
					MonthlyJointDeductionGenerated, AuxillaryDeductions




def reset_monthly_generated_transaction(salary_institution,transaction_period):

	MonthlyDeductionList.objects.filter(transaction_period=transaction_period,salary_institution=salary_institution).delete()
	MonthlyGeneratedTransactions.objects.filter(transaction_period=transaction_period,salary_institution=salary_institution).delete()
	MonthlyDeductionGenerationHeading.objects.filter(transaction_period=transaction_period,salary_institution=salary_institution).delete()
	
	MonthlyGroupGeneratedTransactions.objects.filter(transaction_period=transaction_period,salary_institution=salary_institution).delete()
	MonthlyDeductionListGenerated.objects.filter(transaction_period=transaction_period,salary_institution=salary_institution).delete()


	MonthlyJointDeductionList.objects.filter(transaction_period=transaction_period,salary_institution=salary_institution).delete()
	MonthlyJointDeductionGeneratedTransactions.objects.filter(transaction_period=transaction_period,salary_institution=salary_institution).delete()
	MonthlyJointDeductionGenerated.objects.filter(transaction_period=transaction_period,salary_institution=salary_institution).delete()


	return 0