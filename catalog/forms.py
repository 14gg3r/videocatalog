from django import forms

from .models import VideoCatalog


class VideoCatalogForm(forms.ModelForm):
    class Meta:
        model = VideoCatalog
        fields = '__all__'
