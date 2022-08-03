from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from petstagram.petstagram_auth.models import Profile
from tests.helpers import UserAndProfileCreateMixin
UserModel = get_user_model()


class CreateProfileTests(TestCase, UserAndProfileCreateMixin):
    def test_about_correct_template_and_correct_url(self):
        user, profile = self.user_and_profile_factory()
        response = self.client.get(reverse('create profile'), kwargs={'pk': profile.pk})

        self.assertTemplateUsed('profile_create.html')

        self.assertEqual(response.status_code, 200)

    def test_create_account_with_proper_data_expect_success(self):
        user, profile = self.user_and_profile_factory()
        response = self.client.post(reverse('create profile'), kwargs={'pk': profile.pk})

        self.assertEqual(UserModel.objects.count(), 1)
        self.assertEqual(Profile.objects.count(), 1)
        self.assertEqual(response.status_code, 200)

