from django.db import models

# Create your models here.

CHOICE = [
    ('e-book', 'E-BOOKS'),
    ('copy', 'COPY')
]


class contact(models.Model):
    name = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    phone = models.IntegerField()
    message = models.TextField()

    def __str__(self):
        return self.name


class Book(models.Model):
    book_name = models.CharField(max_length=32)
    book_category = models.CharField(max_length=32)
    book_author_name = models.CharField(max_length=32)
    book_description = models.CharField(max_length=32)
    book_price = models.IntegerField()
    number_of_pages = models.IntegerField()
