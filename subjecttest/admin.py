from django.contrib import admin

from .models import Teachers, Subjects, Questions, Schools

@admin.register(Teachers)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ['fullname', 'phone', 'school']

@admin.register(Subjects)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ['name', 'teacher']

@admin.register(Schools)
class SchoolAdmin(admin.ModelAdmin):
    list_display = ['name']

@admin.register(Questions)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ['id','subject', 'title', 'optionA', 'optionB', 'optionC', 'optionD', 'answeroptions', 'levels']
    list_filter = ['subject']
