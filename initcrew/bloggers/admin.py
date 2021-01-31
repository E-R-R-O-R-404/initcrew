from django.contrib import admin
from .models import Bloggers
# Register your models here.
class BlogAdmin(admin.ModelAdmin):
     list_display = ('id','full_name','heading','is_featured','created_date')
     list_display_links = ('id','full_name')
     search_fields = ('full_name','heading')


admin.site.register(Bloggers, BlogAdmin)