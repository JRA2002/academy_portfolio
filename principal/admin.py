from django.contrib import admin
from .models import Course,Registration,Attendance,Mark

# Register your models here.

class CourseAdmin(admin.ModelAdmin):
    list_display = ('name','professor','class_quantity')
admin.site.register(Course,CourseAdmin)

class RegistrationAdmin(admin.ModelAdmin):
    list_display = ('course','student','enable')
    list_filter = ('course','student','enable')
admin.site.register(Registration,RegistrationAdmin)

class AttendanceAdmin(admin.ModelAdmin):
    list_display = ('student','course','present','date')
    list_filter = ('course','student')
admin.site.register(Attendance,AttendanceAdmin)

class MarkAdmin(admin.ModelAdmin):
    list_display = ('student','mark1','mark2','mark3','average')
    list_filter = ('student',)

admin.site.register(Mark,MarkAdmin)