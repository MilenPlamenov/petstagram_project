from django.contrib.auth import get_user_model

from petstagram.petstagram_auth.models import Profile
from django.test import Client
UserModel = get_user_model()


class UserAndProfileCreateMixin:
    VALID_USER_CREDENTIALS = {
        'username': 'test',
        'password': '12345qwe',
    }

    VALID_PROFILE_CREDENTIALS = {
        'picture': 'test.png',
        'description': 'asd',
    }

    def user_and_profile_factory(self):
        user = UserModel.objects.create_user(**self.VALID_USER_CREDENTIALS)
        profile = Profile.objects.create(**self.VALID_PROFILE_CREDENTIALS, user=user)
        return user, profile

    def login(self):
        username = self.VALID_USER_CREDENTIALS['username']
        password = self.VALID_USER_CREDENTIALS['password']
        user = UserModel.objects.create_user(username=username)
        user.set_password(password)
        user.save()
        profile = Profile.objects.create(picture='asd.png', user=user)

        client = Client()
        client.login(username=username, password=password)
        return user, client, profile
