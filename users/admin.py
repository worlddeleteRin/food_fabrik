from django.contrib import admin
from .models import *
# Register your models here.

class UserAdmin(admin.ModelAdmin):
    search_fields = ['phone', 'name']
    list_display = ['phone', 'name', 'bonus']

admin.site.register(User, UserAdmin)
# admin.site.register(Address)
