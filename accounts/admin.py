from django.contrib import admin
from accounts.models import CustomUser


@admin.register(CustomUser)
class AdminNewUser(admin.ModelAdmin):
    list_display = ('email', 'username', 'is_staff')
    filter_horizontal = ('groups', 'user_permissions',)