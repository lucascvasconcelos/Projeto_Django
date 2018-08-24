from django import forms
from forum import models

class PostForm(forms.ModelForm):

    class Meta:
        model = models.Post
        exclude = []
        widgets = {'usuario': forms.HiddenInput()}

class ComentsForm(forms.ModelForm):

    class Meta:
        model = models.Coments
        exclude = []
                


