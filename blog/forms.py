from django import forms
from .models import Post
from .widgets import GoogleMapPointWidget


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'
        widgets = {
            'lnglat': GoogleMapPointWidget,
        }

