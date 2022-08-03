from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from petstagram.main.models import PetPhoto
from tests.helpers import UserAndProfileCreateMixin

UserModel = get_user_model()


class ProfilePageTests(TestCase, UserAndProfileCreateMixin):
    def test_about_correct_template_and_correct_url(self):
        user, client, profile = self.login()
        response = client.get(reverse('profile'))

        self.assertTemplateUsed('profile_details.html')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(reverse('profile'), '/petstagramauth/profile/')

    def test_account_likes_and_photos_count(self):
        user, client, profile = self.login()
        PetPhoto.objects.create(photo='asd.png', likes=10, user=user)

        response = client.post(reverse('profile'))
        # self.assertEqual(response.context['photos_count'], 1)
        # self.assertEqual(response.context['photos_likes'], 10)
        # self.assertEqual(PetPhoto.objects.count(), 1)
