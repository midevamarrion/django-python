from django.contrib import admin

# Register your models here.
from.models import Category
class Category_admin(admin.ModelAdmin):
    list_display=["name"]
admin.site.register(Category,Category_admin)
