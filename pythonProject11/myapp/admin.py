from django.contrib import admin

from .models import book
# Register your models here.

class showbook(admin.ModelAdmin):
   list_display = ('admin_photo', 'name', 'title', 'description', 'publish_date')

admin.site.register(book, showbook)

