from django.contrib import admin

from .models import Student,StudentClass

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display=['fname','lname','gender']
    list_filter=['classname','gender']

    
    
@admin.register(StudentClass)
class StudentClassAdmin(admin.ModelAdmin):
    list_display=['cname','code']    