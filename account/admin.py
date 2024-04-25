from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . models import Account
# Register your models here.

class AccountAdmin(UserAdmin):
    list_display = ('email', 'first_name', 'last_name', 'username', 'phone_number', 'created_at','last_login', 'is_admin', 'is_staff')
    search_fields = ('email', 'first_name', 'last_name', 'username')
    list_display_links = ('email', 'first_name', 'last_name', 'username')
    readonly_fields = ('created_at', 'last_login', 'password')
    ordering = ('-created_at',)
    

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

admin.site.register(Account, AccountAdmin)