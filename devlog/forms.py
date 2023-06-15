from django import forms
from .models import Projects


class CreateProjectForm(forms.Form):
    title = forms.CharField(label='Название проекта: ', max_length=200)
    description = forms.CharField(label='Описание: ',
                                  widget=forms.Textarea,
                                  max_length=4000,
                                  required=False)
