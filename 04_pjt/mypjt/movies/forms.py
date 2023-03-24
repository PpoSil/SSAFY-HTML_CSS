import datetime
from django import forms
from .models import Movie
# from django.core.validators import MinValueValidator, MaxValueValidator

class MovieForm(forms.ModelForm):
    # GENRE_CHOICES = (
    # ('코미디', 'coomedy'),
    # ('공포', 'horror'),
    # ('로맨스', 'romance'),
    # ('스릴러', 'thriller'),
    # )
    genre = forms.ChoiceField(choices=[('코미디', 'comedy',), ('공포', 'horror'), ('로맨스', 'romance'),('스릴러', 'thriller'),])
    score = forms.FloatField(min_value=0, max_value=5, widget=forms.NumberInput(attrs={'step': 0.5}))  # 더 설정!
    release_date = forms.DateField(initial=datetime.date.today)
    # release_date = forms.DateField(auto_now_add==True)
    class Meta:
        model = Movie
        fields = '__all__'  # ('genre', 'score', 'release_data',)
        
