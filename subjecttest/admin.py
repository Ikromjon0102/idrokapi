from django.contrib import admin

from .models import Teachers, Subjects, Questions, Schools,Class,Parents,Theme,Pupils

@admin.register(Parents)
class ParentAdmin(admin.ModelAdmin):
    list_display = ['name']
@admin.register(Theme)
class ThemeAdmin(admin.ModelAdmin):
    list_display = ['name']
@admin.register(Teachers)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ['fullname', 'phone', 'school']
@admin.register(Class)
class ClassAdmin(admin.ModelAdmin):
    list_display = ['title','school','teacher']

@admin.register(Pupils)
class PupilsAdmin(admin.ModelAdmin):
    list_display = ['first_name','last_name','gender','phone', 'birthday','school', 'teacher', 'parents', 'subjects']

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

