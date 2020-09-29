from django.contrib import admin

# Register your models here.
#from django.contrib import admin

# Register your models here.
from .models import Student_info,Book_info

class Student_infoAdmin(admin.ModelAdmin):
    list_display =['user','student_name','class_name','branch','city','district','country','book_needed']
admin.site.register(Student_info,Student_infoAdmin)

class Book_infoAdmin(admin.ModelAdmin):
    list_display =['user','book_name','author','book_copies']
admin.site.register(Book_info,Book_infoAdmin)
