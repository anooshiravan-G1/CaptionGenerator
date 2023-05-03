from django import forms
from .models import ImageCaption


class ImageUploadForm(forms.ModelForm):
    class Meta:
        model = ImageCaption
        fields = ['image']
