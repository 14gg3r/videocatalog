from django import forms
from django.utils import dateformat
from django.utils.timezone import localtime, now

from .models import VideoCatalog


class VideoCatalogForm(forms.ModelForm):
    class Meta:
        model = VideoCatalog
        fields = [
            'user',
            'created_timestamp',
            'performer',
            'title',
            'duration',
            'video_type',
            'director',
            'screenwriter',
            'composer',
            'year',
            'youtube_link',
            'rutube_link',
            'yandex_link',
            'vk_link',
            'zen_link',
            'upc',
            'files'
        ]
    created_timestamp = forms.DateTimeField(
        label='Дата добавления',
        widget=forms.TextInput(attrs={'readonly': True,
                                      'value': dateformat.format(localtime(now()), 'Y-m-d H:i'),
                                      'class': 'date-input'})
    )
