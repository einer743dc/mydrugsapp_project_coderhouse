from django.contrib import admin
from . import models

# Register your models here.

# class DrugAdmin
@admin.register(models.Drug)
class DrugAdmin(admin.ModelAdmin):
    list_display = ['name', 'company', 'composition', 'package_qty', 'drugtype', 'restricted', 'stock', 'price']
    search_fields = ['name', 'drugtype__name']

# class DrugTypeAdmin
@admin.register(models.DrugType)
class DrugTypeAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']

# class CompanyAdmin
@admin.register(models.Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ['name', 'country', 'phone', 'mail']
    search_fields = ['name', 'country__name']

# class CountryAdmin
@admin.register(models.Country)
class CountryAdmin(admin.ModelAdmin):
    pass