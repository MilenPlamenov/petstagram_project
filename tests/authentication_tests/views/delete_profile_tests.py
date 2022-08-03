from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from petstagram.petstagram_auth.models import Profile
from tests.helpers import UserAndProfileCreateMixin

UserModel = get_user_model()


class ProfilePageTests(TestCase, UserAndProfileCreateMixin):
    def test_about_correct_template_and_correct_url(self):
        user, client, profile = self.login()
        response = client.get(reverse('delete profile'))

        self.assertTemplateUsed('profile_delete.html')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(reverse('delete profile'), '/petstagramauth/profile/delete/')

    def test_delete_profile_functionality(self):
        user, client, profile = self.login()
        # check before hitting the view
        self.assertEqual(UserModel.objects.count(), 1)
        self.assertEqual(Profile.objects.count(), 1)

        response = client.post(reverse('delete profile'))
        # check after hitting the view
        self.assertEqual(UserModel.objects.count(), 0)
        self.assertEqual(Profile.objects.count(), 0)
        self.assertRedirects(response, reverse('index'))
