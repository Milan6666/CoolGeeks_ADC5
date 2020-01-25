from django import forms
from .models import food

class Ourform(forms.ModelForm):
    class Meta:
        model = food
        fields = ('title', 'name', 'file')