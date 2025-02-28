from django import forms
from .models import *


class EventForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['category'].empty_label = 'Category not selected'

    class Meta:
        model = Event
        fields = ['name', 'author', 'description', 'image', 'category']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter event name'}),
            'description': forms.Textarea(
                attrs={'class': 'form-control', 'cols': 60, 'rows': 10, 'placeholder': 'Enter event description'}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-select'}),
        }

    # def clean_name(self):
    #     name = self.cleaned_data['name']
    #     if len(name) > 49:
    #         raise forms.ValidationError('Event name too long')
    #     return name
