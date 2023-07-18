from django.contrib import admin
from .models import Resident
# Register your models here.

@admin.register(Resident)
class RegisterAdminClass(admin.ModelAdmin):
    list_display = ('resident_name', 'email_id', 'resident_building_name')