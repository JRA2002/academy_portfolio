from django.contrib import admin
from .models import Course,Registration,Attendance

# Register your models here.

class CourseAdmin(admin.ModelAdmin):
    list_display = ('name','professor','class_quantity')
admin.site.register(Course,CourseAdmin)

class RegistrationAdmin(admin.ModelAdmin):
    list_display = ('student','course','enable')
    list_filter = ('course','student','enable')
admin.site.register(Registration,RegistrationAdmin)

class AttendanceAdmin(admin.ModelAdmin):
    list_display = ('student','course','present','date')
    list_filter = ('course','student')
admin.site.register(Attendance,AttendanceAdmin)