from django.contrib import admin
from .models import * 

# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    search_fields = ['name', 'price']
class CategoryAdmin(admin.ModelAdmin):
    search_fields = ['slug', 'name']

admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Stock)

