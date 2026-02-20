from django import forms
from .models import StudentProfile, University, Major, CollegePreference

class StudentProfileForm(forms.ModelForm):
    class Meta:
        model = StudentProfile
        fields = ['name', 'province', 'total_score', 'chinese_score', 'math_score', 
                   'english_score', 'comprehensive_score', 'subject_type', 'year']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'province': forms.TextInput(attrs={'class': 'form-control'}),
            'total_score': forms.NumberInput(attrs={'class': 'form-control'}),
            'chinese_score': forms.NumberInput(attrs={'class': 'form-control'}),
            'math_score': forms.NumberInput(attrs={'class': 'form-control'}),
            'english_score': forms.NumberInput(attrs={'class': 'form-control'}),
            'comprehensive_score': forms.NumberInput(attrs={'class': 'form-control'}),
            'subject_type': forms.Select(attrs={'class': 'form-control'}),
            'year': forms.NumberInput(attrs={'class': 'form-control'}),
        }

class CollegePreferenceForm(forms.ModelForm):
    class Meta:
        model = CollegePreference
        fields = ['university', 'major', 'preference_order', 'is_adjusted', 'notes']
        widgets = {
            'university': forms.Select(attrs={'class': 'form-control'}),
            'major': forms.Select(attrs={'class': 'form-control'}),
            'preference_order': forms.NumberInput(attrs={'class': 'form-control', 'min': 1, 'max': 6}),
            'is_adjusted': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'notes': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }
