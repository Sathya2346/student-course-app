from django.contrib import admin
from .models import Course

class CourseAdmin(admin.ModelAdmin):
    list_display = ['title', 'price', 'duration']
    fields = ['title', 'description', 'price', 'duration', 'image']

admin.site.register(Course, CourseAdmin)