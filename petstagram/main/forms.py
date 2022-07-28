from pyexpat import model

from django import forms
from django.forms import ModelForm

from petstagram.main.models import Pet, PetPhoto


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


class PhotoForm(ModelForm):
    class Meta:
        model = PetPhoto
        fields = ('photo', 'description', 'tagged_pets')
        widgets = {

            'description': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Enter description',
                }
            ),
        }