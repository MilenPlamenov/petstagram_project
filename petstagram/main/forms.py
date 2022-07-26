from django import forms
from django.forms import ModelForm

from petstagram.main.models import Pet


class PetForm(ModelForm):
    class Meta:
        model = Pet
        fields = ('name', 'date_of_birth', 'pet_type')
        widgets = {
            'name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Enter pet name',
                }
            ),
            'date_of_birth': forms.TextInput(
                attrs={
                    'class': 'form-control',
                }
            ),
        }


