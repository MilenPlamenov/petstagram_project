from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from petstagram.petstagram_auth.models import Profile
from tests.helpers import UserAndProfileCreateMixin

UserModel = get_user_model()


class EditProfileTests(TestCase, UserAndProfileCreateMixin):
    def test_about_correct_template_and_correct_url(self):
        user, client, profile = self.login()
        response = client.get(reverse('edit profile'))

        self.assertTemplateUsed('profile_edit.html')
        self.assertEqual(response.status_code, 200)

    def test_edit_the_account(self):
        user, client, profile = self.login()
        self.assertEqual(user.username, 'test')
        response = client.post(reverse('edit profile'), data={'username': 'sad', 'description': 'changed'})
        updated_account = UserModel.objects.get(id=1)
        updated_profile = Profile.objects.get(id=1)
        # test updated data
        self.assertEqual(updated_account.username, 'sad')
        self.assertEqual(updated_profile.description, 'changed')
