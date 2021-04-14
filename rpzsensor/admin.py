from django.contrib import admin
from .models import Period, Place, Photo, Environment, CustomUser
from django.contrib.auth.admin import UserAdmin

# Register your models here.

class CustomUserAdmin(UserAdmin):
    model = CustomUser
#    fieldsets = UserAdmin.fieldsets + ((None, {'fields': ('sex',)}),)
#    list_display = ['username', 'email', 'sex']
 
 
admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Place)
admin.site.register(Photo)
admin.site.register(Period)
admin.site.register(Environment)
