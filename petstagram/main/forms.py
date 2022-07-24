from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from petstagram.main.models import Profile


class CreateProfileForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'last_name')
        labels = {
            "username": "First Name", # using the username as first name.
        }
        widgets = {
            'username': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Enter first name',

                }
            ),
            'last_name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Enter last name'
                }
            ),

        }

    def clean_username(self):
        username = self.cleaned_data.get('username', False)
        if not username:
            first_name = self.cleaned_data['first_name']
            last_name = self.cleaned_data['last_name']
            User.username = f'{first_name} {last_name}'
        return username

    def __init__(self, *args, **kwargs):
        super(CreateProfileForm, self).__init__(*args, **kwargs)

        for field_name in ['username', 'password1', 'password2']:
            self.fields[field_name].help_text = None


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ('user', 'description', 'birth', 'gender')
