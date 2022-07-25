from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

from petstagram.petstagram_auth.models import Profile

UserModel = get_user_model()


class CreateProfileForm(UserCreationForm):
    class Meta:
        model = UserModel
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
            UserModel.username = f'{first_name} {last_name}'
        return username

    def __init__(self, *args, **kwargs):
        super(CreateProfileForm, self).__init__(*args, **kwargs)

        for field_name in ['username', 'password1', 'password2']:
            self.fields[field_name].help_text = None


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ('user', 'description', 'birth', 'gender')


class EditProfile(forms.ModelForm):
    class Meta:
        model = UserModel
        fields = ('username', 'last_name', 'email')  # added first and last name / easier register in the app

    def __init__(self, *args, **kwargs):  # rewriting the init method to remove the help text from the fields
        super(EditProfile, self).__init__(*args, **kwargs)
        for field_name in ['username']:
            self.fields[field_name].help_text = None


class EditExtendedProfile(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('picture', 'birth', 'description')


class DeleteProfile(forms.ModelForm):
    class Meta:
        model = UserModel
        fields = ()


class DeleteExtendedProfile(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ()

