from django.contrib import admin
from .models import Books, Categories

# Register your models here.
class BooksAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'in_stock']
    list_filter = ['in_stock']
    search_fields = ['name']
    
admin.site.register(Books, BooksAdmin)
admin.site.register(Categories)