from .models import *
from django.db.models import Q


def generalMemberSearch(frm,status):
	records=Members.objects.filter(Q(phone_number__icontains=frm) | Q(file_no__icontains=frm) | Q(ippis_no__icontains=frm)  | Q(admin__first_name__icontains=frm) | Q(admin__last_name__icontains=frm) | Q(middle_name__icontains=frm)).filter(status=status)

	return records


def searchMembersForShopDeduction(frm,status,salary_pk):
	salary_institution=SalaryInstitution.objects.get(id=salary_pk)
	records=Members.objects.filter(Q(coop_no__icontains=frm) | Q(ippis_no__icontains=frm)  | Q(admin__first_name__icontains=frm) | Q(admin__last_name__icontains=frm) | Q(middle_name__icontains=frm)).filter(status=status,salary_institution=salary_institution).order_by('coop_no')

	return records

def searchMembers(frm,status):
	records=Members.objects.filter(Q(coop_no__icontains=frm) | Q(ippis_no__icontains=frm)  | Q(admin__first_name__icontains=frm) | Q(admin__last_name__icontains=frm) | Q(middle_name__icontains=frm)).filter(status=status).order_by('coop_no')

	return records

def searchMembersFormSales(frm):
	records=MemberShipFormSalesRecord.objects.filter(Q(applicant__phone_number__icontains=frm)| Q(applicant__ippis_no__icontains=frm)  | Q(applicant__first_name__icontains=frm) | Q(applicant__last_name__icontains=frm) | Q(applicant__middle_name__icontains=frm) | Q(receipt__icontains=frm))

	return records

def searchGuarantorMembers(frm,status,member):
	# records=Members.objects.filter(Q(member_id__icontains=frm) | Q(ippis_no__icontains=frm)).filter(status=status).filter(~Q(id=member.id))
	records=Members.objects.filter(Q(member_id__icontains=frm) | Q(phone_number__icontains=frm) | Q(file_no__icontains=frm) | Q(ippis_no__icontains=frm)  | Q(admin__first_name__icontains=frm) | Q(admin__last_name__icontains=frm) | Q(middle_name__icontains=frm)).filter(status=status).filter(~Q(id=member.id))

	return records


def searchShopMembers(frm,status):
	records=CooperativeShopLedger.objects.filter(Q(member__member__ippis_no__icontains=frm) | Q(member__member__admin__first_name__icontains=frm) | Q(member__member__admin__last_name__icontains=frm) | Q(member__member__middle_name__icontains=frm)).values_list('member__member__member_id','member__member__admin__last_name' + ' ' + 'member__member__admin__first_name' + ' ' + 'member__member__middle_name').distinct()
	# items=Daily_Sales.objects.filter(processed_by_id=processed_by.id,created_at__year=year,created_at__month= month,created_at__day= day).order_by('receipt').values_list('receipt','item_code','item_name').distinct()
	return records


def searchMemberShip(frm,submission_status):
	records=MemberShipRequest.objects.filter(Q(phone_number__icontains=frm) | Q(first_name__icontains=frm) | Q(last_name__icontains=frm) | Q(middle_name__icontains=frm)).filter(submission_status=submission_status)
	
	return records