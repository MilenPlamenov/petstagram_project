from django.test import TestCase
from django.urls import reverse

from petstagram.main.models import PetPhoto
from tests.main_tests.views.test_photo_detail_view import ModelUser


class LikeTests(TestCase):
    VALID_USER = {
        'username': 'Gosho',
        'password': '12345qwe',
    }

    VALID_PET = {
        'name': 'Gosho pet edition',
        'pet_type': 'Cat',
        'date_of_birth': '2020-01-01'
    }

    def test_like_photo(self):
        user = ModelUser.objects.create_user(username=self.VALID_USER['username'])
        user.set_password(self.VALID_USER['password'])
        user.save()
        self.client.login(username=self.VALID_USER['username'], password=self.VALID_USER['password'])
        photo = PetPhoto.objects.create(photo='217652305_514626236513399_2247992701773323938_n_3sLCfEw.jpg',
                                        user_id=user.id)

        liked = photo.like_set.filter(user=user)
        self.assertEqual(liked.count(), 0)

        response = self.client.get(reverse('like', args=(photo.id,)))

        self.assertRedirects(response, reverse('photo details', args=(photo.id,)))
        self.assertEqual(response.status_code, 302)
        self.assertEqual(liked.count(), 1)  # check if the user liked the photo
