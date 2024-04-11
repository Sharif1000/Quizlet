from django.contrib import admin
from .models import Student
# Register your models here.

class StudentAdmin(admin.ModelAdmin):
    list_display = ['first_name','last_name','subject', 'session', 'university', 'mobile_no']

    def first_name(self,obj):
        return obj.user.first_name 
    
    def last_name(self,obj):
        return obj.user.last_name
    
admin.site.register(Student, StudentAdmin)
