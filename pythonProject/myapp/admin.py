from django.contrib import admin
from .models import contact
from .models import Book


# Register your models here.
class showContact(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone', 'message']


class showBook(admin.ModelAdmin):
    list_display = ['book_name', 'book_category', 'book_author_name', 'book_description', 'book_price',
                    'number_of_pages']


admin.site.register(contact, showContact)
admin.site.register(Book, showBook)
