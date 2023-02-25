from django.db import models

# Create your models here.
from django.utils.safestring import mark_safe


class product(models.Model):
    productname = models.CharField(max_length=30)
    productprice = models.IntegerField()
    productdesc = models.TextField
    productimage = models.ImageField(upload_to="photos")


def product_image(self):
    return mark_safe('<img src="{}" width="100"/>'.format(self.productimage))

product_image.allow_tag = True
