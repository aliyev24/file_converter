from django import forms
from . import models

FILE_CHOICES = (

    ("jpg", "Convert to JPG"),
    ("png", "Convert to PNG"),
)


class FaylForm(forms.ModelForm):
    file_field = forms.ChoiceField(choices=FILE_CHOICES)

    class Meta:
        model = models.File
        fields = '__all__'
