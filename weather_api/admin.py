from django.contrib import admin
from . models import *
# Register your models here.

@admin.register(Description)
class DescriptionAdmin(admin.ModelAdmin):
    list_display = ['description','temperature','created_on']
