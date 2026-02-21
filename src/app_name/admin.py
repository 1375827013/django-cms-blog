from django.contrib import admin
from .models import StudentProfile, University, Major, AdmissionScore, CollegePreference

admin.site.site_header = '高考志愿填报助手管理后台'
admin.site.site_title = '高考志愿填报助手'
admin.site.index_title = '管理首页'

@admin.register(StudentProfile)
class StudentProfileAdmin(admin.ModelAdmin):
    list_display = ('name', 'province', 'total_score', 'subject_type', 'year', 'created_at')
    list_filter = ('province', 'subject_type', 'year')
    search_fields = ('name', 'province')
    ordering = ['-total_score']
    list_per_page = 20

@admin.register(University)
class UniversityAdmin(admin.ModelAdmin):
    list_display = ('name', 'province', 'city', 'university_type', 'level', 'ranking')
    list_filter = ('province', 'university_type', 'level')
    search_fields = ('name', 'province', 'city')
    ordering = ['ranking']
    list_per_page = 20

@admin.register(Major)
class MajorAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'code', 'employment_rate')
    list_filter = ('category',)
    search_fields = ('name', 'code', 'category')
    ordering = ['category', 'name']
    list_per_page = 20

@admin.register(AdmissionScore)
class AdmissionScoreAdmin(admin.ModelAdmin):
    list_display = ('university', 'major', 'province', 'subject_type', 'year', 'min_score', 'avg_score')
    list_filter = ('province', 'subject_type', 'year')
    search_fields = ('university__name', 'major__name')
    ordering = ['-year', '-min_score']
    list_per_page = 20

@admin.register(CollegePreference)
class CollegePreferenceAdmin(admin.ModelAdmin):
    list_display = ('student', 'university', 'major', 'preference_order', 'is_adjusted', 'created_at')
    list_filter = ('is_adjusted', 'preference_order')
    search_fields = ('student__name', 'university__name', 'major__name')
    ordering = ['preference_order']
    list_per_page = 20
