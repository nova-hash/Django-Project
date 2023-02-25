from django.db import models

class registertable(models.Model):
    Full_Name = models.CharField(max_length=30)
    Email = models.EmailField()
    Address = models.TextField()
    Password = models.CharField(max_length=32)
    Mobile_no  = models.BigIntegerField(max_length=10)


# Create your models here.
