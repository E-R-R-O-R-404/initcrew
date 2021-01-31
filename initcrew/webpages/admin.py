from django.contrib import admin
from .models import Sliders , Navlinks ,SecurityText , IndroductionBackend , ContactUs
from django.utils.html import format_html
# Register your models here.

class SlidersAdmin(admin.ModelAdmin):
    def eventphoto(self, objects):
        return format_html('<img src="{}" width="40"/>'.format(objects.photo.url))

    list_display = ('id','eventphoto','headlines','created_date')
    list_display_links = ('id','headlines')
    search_fields = ('id','headlines')

class NavlinkAdmin(admin.ModelAdmin):
    list_display = ('id','youtube_link','twitter_link')
    list_editable = ('youtube_link','twitter_link')

class SecurityAdmin(admin.ModelAdmin):
    list_display = ('id',)

class AdminIntroduction(admin.ModelAdmin):
    list_display = ('id',)

class ContactAdmin(admin.ModelAdmin):
    list_display = ('id' , 'full_name' , 'subject', 'email')
    list_display_links = ('id' , 'full_name' , 'subject', 'email')


admin.site.register(Sliders , SlidersAdmin )
admin.site.register(Navlinks , NavlinkAdmin)
admin.site.register(SecurityText, SecurityAdmin)
admin.site.register(IndroductionBackend, AdminIntroduction)
admin.site.register(ContactUs , ContactAdmin)