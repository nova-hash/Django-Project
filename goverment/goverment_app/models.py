from django.utils.safestring import mark_safe
from django.db import models

CHOICE1 = [
    {'0', 'inactive'},
    {'1', 'active'}
]

CHOICE2 = [
    {'0', 'male'},
    {'1', 'female'}
]


class aadharcardtable(models.Model):
    aadharnumber = models.BigIntegerField()
    firstname = models.CharField(max_length=30)
    middlename = models.CharField(max_length=30, null=True)
    lastname = models.CharField(max_length=30)
    address = models.TextField()
    phonenumber = models.BigIntegerField()
    dob = models.DateField()
    cast = models.CharField(max_length=30)
    gender = models.IntegerField(choices=CHOICE2)
    document = models.FileField()

    def __str__(self):
        return self.aadharnumber


class registertable(models.Model):
    Full_Name = models.CharField(max_length=30)
    Email = models.EmailField()
    Password = models.CharField(max_length=32)
    Mobile_no = models.BigIntegerField()
    Occupation = models.CharField(max_length=40)
    status = models.IntegerField(choices=CHOICE1, null=True)
    role = models.IntegerField(null=True)
    aadharid = models.ForeignKey(aadharcardtable, on_delete=models.CASCADE, null=True)


class policytable(models.Model):
    policyname = models.CharField(max_length=120)
    policydetails = models.TextField()
    policytype = models.CharField(max_length=100)
    policyphoto = models.ImageField(upload_to='photos')
    policyAgency = models.CharField(max_length=100)
    policyTargetAudience = models.CharField(max_length=100)
    policyEligibleCastes = models.CharField(max_length=30)
    policyApplicableState = models.CharField(max_length=30)
    policyResidenceArea = models.CharField(max_length=30)
    policyDisabilityStatus = models.CharField(max_length=30)
    policyMinorityStatus = models.CharField(max_length=30)
    policyBPLStatus = models.CharField(max_length=30)
    policyurl = models.CharField(max_length=100, null=True)

    def admin_photo(self):
        return mark_safe('<img src="{}" width="100"/>'.format(self.policyphoto.url))

    policyphoto.allow_tags = True

    def __str__(self):
        return self.policyname


class applicationtable(models.Model):
    regid = models.ForeignKey(registertable, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    dob = models.DateField()
    policyid = models.ForeignKey(policytable, on_delete=models.CASCADE, null=True)
    status = models.IntegerField()


class feedbacktable(models.Model):
    regid = models.ForeignKey(registertable, on_delete=models.CASCADE, null=True)
    feedbackdesk = models.CharField(max_length=30)
    timestamp = models.DateField
