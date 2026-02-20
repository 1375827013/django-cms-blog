from django import forms
from .models import StudentProfile, CollegePreference

class StudentProfileForm(forms.ModelForm):
    class Meta:
        model = StudentProfile
        fields = ['name', 'province', 'total_score', 'chinese_score', 'math_score', 
                   'english_score', 'comprehensive_score', 'subject_type', 'year']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '请输入姓名'}),
            'province': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '请输入省份'}),
            'total_score': forms.NumberInput(attrs={'class': 'form-control', 'min': 0, 'max': 750}),
            'chinese_score': forms.NumberInput(attrs={'class': 'form-control', 'min': 0, 'max': 150}),
            'math_score': forms.NumberInput(attrs={'class': 'form-control', 'min': 0, 'max': 150}),
            'english_score': forms.NumberInput(attrs={'class': 'form-control', 'min': 0, 'max': 150}),
            'comprehensive_score': forms.NumberInput(attrs={'class': 'form-control', 'min': 0, 'max': 300}),
            'subject_type': forms.Select(attrs={'class': 'form-control'}),
            'year': forms.NumberInput(attrs={'class': 'form-control', 'min': 2020, 'max': 2030}),
        }
    
    def clean_total_score(self):
        total_score = self.cleaned_data.get('total_score')
        if total_score < 0 or total_score > 750:
            raise forms.ValidationError('总分必须在 0-750 之间')
        return total_score

class CollegePreferenceForm(forms.ModelForm):
    class Meta:
        model = CollegePreference
        fields = ['university', 'major', 'preference_order', 'is_adjusted', 'notes']
        widgets = {
            'university': forms.Select(attrs={'class': 'form-control'}),
            'major': forms.Select(attrs={'class': 'form-control'}),
            'preference_order': forms.NumberInput(attrs={'class': 'form-control', 'min': 1, 'max': 6}),
            'is_adjusted': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'notes': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': '备注信息（可选）'}),
        }
    
    def clean_preference_order(self):
        preference_order = self.cleaned_data.get('preference_order')
        if preference_order < 1 or preference_order > 6:
            raise forms.ValidationError('志愿顺序必须在 1-6 之间')
        return preference_order
