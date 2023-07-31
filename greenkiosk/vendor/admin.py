from django.contrib import admin

# Register your models here.
from .models import Vendor

class VendorAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'address')
    search_fields = ('name', 'email', 'phone')

admin.site.register(Vendor, VendorAdmin)
