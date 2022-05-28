from django.contrib import admin
from .models import * 

class PharmaSalesAdmin(admin.ModelAdmin):
    list_display = [field.name for field in PharmaSales._meta.get_fields()]

admin.site.register(PharmaSales, PharmaSalesAdmin)