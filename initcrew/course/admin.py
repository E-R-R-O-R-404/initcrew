from django.contrib import admin
from .models import Courses
# Register your models here.
class CourseAdmin(admin.ModelAdmin):
     list_display = ('id','heading','Author_name','is_featured','created_date')
     list_display_links = ('id','heading','Author_name')
     search_fields = ('heading','Author_name')


admin.site.register(Courses, CourseAdmin)