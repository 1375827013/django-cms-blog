from django import forms
from .models import Article

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        # 网页表单里允许用户填写的字段
        fields = ['title', 'content', 'image'] 