from django.contrib import admin
from .models import ExtendedUser
# Register your models here.

class ExtendedUserAdmin(admin.ModelAdmin):
    list_display = ('id','user','phone_num','is_purchased')
    list_display_links = ('id','user')
    list_filter = ('is_purchased',)
    search_fields = ('id','phone_num')

admin.site.register(ExtendedUser, ExtendedUserAdmin)