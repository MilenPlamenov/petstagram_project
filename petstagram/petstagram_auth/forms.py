from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.core.exceptions import ValidationError

from petstagram.petstagram_auth.models import Profile
from petstagram.petstagram_auth.validators import clean_fields_factory

UserModel = get_user_model()


class CreateProfileForm(UserCreationForm):
    class Meta:
        model = UserModel
        fields = ('username', 'first_name', 'last_name')
        widgets = {
            'username': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Enter username',
                }
            ),
            'first_name': forms.TextInput(
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
        clean_fields_factory(username, 'username')
        return username

    def clean_last_name(self):
        last_name = self.cleaned_data.get('last_name')
        clean_fields_factory(last_name, 'last name')
        return last_name

    def __init__(self, *args, **kwargs):
        super(CreateProfileForm, self).__init__(*args, **kwargs)

        for field_name in ['username', 'password1', 'password2']:
            self.fields[field_name].help_text = None

        self.fields['password1'].widget = forms.PasswordInput(
            attrs={
                'placeholder': 'Enter password',
                'class': 'form-control',
            }
        )
        self.fields['password2'].widget = forms.PasswordInput(
            attrs={
                'placeholder': 'Confirm password',
                'class': 'form-control',
            }
        )


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ('user', 'description', 'birth', 'gender')


class EditProfile(forms.ModelForm):
    class Meta:
        model = UserModel
        fields = ('username', 'last_name', 'email')  # added first and last name / easier register in the app
        labels = {
            'username': 'First name',  # using the username as first name.
        }

        widgets = {
            'username': forms.TextInput(
                attrs={
                    'class': 'form-control',
                }
            ),
            'last_name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                }
            ),
            'email': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Enter email',
                }
            ),
        }

    def __init__(self, *args, **kwargs):  # rewriting the init method to remove the help text from the fields
        super(EditProfile, self).__init__(*args, **kwargs)
        for field_name in ['username']:
            self.fields[field_name].help_text = None


class EditExtendedProfile(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ('user',)
        widgets = {
            'birth': forms.TextInput(
                attrs={
                    'class': 'form-control',
                }
            ),
            'description': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Enter description',
                }
            ),
        }


class DeleteProfile(forms.ModelForm):
    class Meta:
        model = UserModel
        fields = ()


class DeleteExtendedProfile(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ()


class LoginForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Enter your username', 'class': 'form-control'}))
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Enter your password', 'class': 'form-control'}))
