from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from petstagram.main.models import PetPhoto

ModelUser = get_user_model()


class PhotoDetailTests(TestCase):
    VALID_USER = {
        'username': 'Gosho',
        'password': '12345qwe',
    }

    VALID_PET = {
        'name': 'Gosho pet edition',
        'pet_type': 'Cat',
        'date_of_birth': '2020-01-01'
    }

    def test_view_with_proper_data(self):
        user = ModelUser.objects.create(**self.VALID_USER)
        photo = PetPhoto.objects.create(photo='217652305_514626236513399_2247992701773323938_n_3sLCfEw.jpg',
                                        user_id=user.id)
        response = self.client.get(reverse('photo details', args=(photo.id,)))

        self.assertEqual(PetPhoto.objects.count(), 1)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'photo_templates/photo_details.html')

