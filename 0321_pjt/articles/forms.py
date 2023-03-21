from django import forms
from .models import Article

# class ArticleForm(forms.Form):
#     title = forms.CharField(max_length=10)
#     content = forms.CharField(widget=forms.Textarea)

class ArticleForm(forms.ModelForm):

    class Meta:
        model = Article
        fields = '__all__'  # article에 있는 모든 field의 값을 가져오겠다