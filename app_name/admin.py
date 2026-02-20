from django.contrib import admin
from .models import StudentProfile, University, Major, AdmissionScore, CollegePreference

@admin.register(StudentProfile)
class StudentProfileAdmin(admin.ModelAdmin):
    list_display = ('name', 'province', 'total_score', 'subject_type', 'year', 'created_at')
    list_filter = ('province', 'subject_type', 'year')
    search_fields = ('name', 'province')
    ordering = ['-total_score']

@admin.register(University)
class UniversityAdmin(admin.ModelAdmin):
    list_display = ('name', 'province', 'city', 'university_type', 'level', 'ranking')
    list_filter = ('province', 'university_type', 'level')
    search_fields = ('name', 'province', 'city')
    ordering = ['ranking']

@admin.register(Major)
class MajorAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'code', 'employment_rate')
    list_filter = ('category',)
    search_fields = ('name', 'code', 'category')
    ordering = ['category', 'name']

@admin.register(AdmissionScore)
class AdmissionScoreAdmin(admin.ModelAdmin):
    list_display = ('university', 'major', 'province', 'subject_type', 'year', 'min_score', 'avg_score')
    list_filter = ('province', 'subject_type', 'year')
    search_fields = ('university__name', 'major__name')
    ordering = ['-year', '-min_score']

@admin.register(CollegePreference)
class CollegePreferenceAdmin(admin.ModelAdmin):
    list_display = ('student', 'university', 'major', 'preference_order', 'is_adjusted', 'created_at')
    list_filter = ('is_adjusted', 'preference_order')
    search_fields = ('student__name', 'university__name', 'major__name')
    ordering = ['preference_order']
