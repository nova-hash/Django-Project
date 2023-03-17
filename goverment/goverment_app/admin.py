from django.contrib import admin

from .models import aadharcardtable, registertable, applicationtable, policytable, feedbacktable


# Register your models here.

class showaadharcardtable(admin.ModelAdmin):
    list_display = ['aadharnumber', 'firstname', 'middlename', 'lastname', 'address', 'phonenumber', 'dob', 'cast',
                    'gender', 'document', 'ResidenceArea', 'DisabilityStatus', 'MinorityStatus', 'BPLStatus']


class showregistrationtable(admin.ModelAdmin):
    list_display = ['Full_Name', 'Email', 'Password', 'Mobile_no', 'Occupation', 'status', 'role', 'aadharid']


class showapplicationtable(admin.ModelAdmin):
    list_display = ['regid', 'name', 'dob', 'policyid', 'status']


class showpolicytable(admin.ModelAdmin):
    list_display = ['policyname', 'policydetails', 'policytype', 'admin_photo', 'policyAgency',
                    'policyTargetAudience', 'policyEligibleCastes', 'policyApplicableState', 'policyResidenceArea',
                    'policyDisabilityStatus', 'policyMinorityStatus', 'policyBPLStatus']


class showfeedbacktable(admin.ModelAdmin):
    list_display = ['feedbackdesk', 'timestamp']


admin.site.register(aadharcardtable, showaadharcardtable)
admin.site.register(registertable, showregistrationtable)
admin.site.register(applicationtable, showapplicationtable)
admin.site.register(policytable, showpolicytable)
admin.site.register(feedbacktable, showfeedbacktable)
