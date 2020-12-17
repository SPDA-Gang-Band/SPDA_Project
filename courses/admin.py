from django.contrib import admin

from .models import *


# Register your models here.
class CourseRequestAdmin(admin.ModelAdmin):
    search_fields = ('login', 'course_name', 'surname', 'name',)


admin.site.register(CourseRequest, CourseRequestAdmin)