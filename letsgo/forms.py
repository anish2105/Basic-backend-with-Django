from django import forms
from .models import details

class detailform(forms.ModelForm):
    class Meta:
        model = details
        fields = ['name','views']
