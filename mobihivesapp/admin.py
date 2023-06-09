from django.contrib import admin
from .models import *


class MarksObtainedInline(admin.TabularInline):
    model = MarksObtained
    
class StudentAdmin(admin.ModelAdmin):
    inlines = [MarksObtainedInline]
    
    
admin.site.register(Student, StudentAdmin)
admin.site.register(Subject)
admin.site.register(Classroom)