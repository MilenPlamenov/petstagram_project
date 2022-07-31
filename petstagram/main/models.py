from datetime import date

from django.contrib.auth import get_user_model
from django.db import models

from petstagram.main.validators import validate_image

UserModel = get_user_model()


class Pet(models.Model):
    NAME_MAX_LENGTH = 30

    CAT = 'Cat'
    DOG = 'Dog'
    BUNNY = 'Bunny'
    PARROT = 'Parrot'
    FISH = 'Fish'
    OTHER = 'Other'
    TYPE_CHOICES = (CAT, DOG, BUNNY, PARROT, FISH, OTHER)

    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
    )

    name = models.CharField(
        max_length=NAME_MAX_LENGTH,
    )

    pet_type = models.CharField(
        max_length=len(max(TYPE_CHOICES, key=len)),
        default=OTHER,
        choices=tuple((p, p) for p in TYPE_CHOICES),
    )

    date_of_birth = models.DateField(
        null=True,
        blank=True,
    )

    def __str__(self):
        return self.name

    class Meta:
        unique_together = ('user', 'name')  # All pets' names should be unique for that user.

    @property
    def age(self):
        today = date.today()
        age = today.year - self.date_of_birth.year - (
                (today.month, today.day) < (self.date_of_birth.month, self.date_of_birth.day))
        return age


class PetPhoto(models.Model):
    PHOTO_UPLOAD_DIR = 'pets/'

    photo = models.ImageField(
        upload_to=PHOTO_UPLOAD_DIR,
        null=True,
        blank=True,
        validators=(
            validate_image,
        )
    )

    tagged_pets = models.ManyToManyField(
        Pet,
    )

    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
    )

    description = models.TextField(
        null=True,
        blank=True,
    )

    publication_date = models.DateTimeField(
        auto_now_add=True,
    )

    likes = models.IntegerField(
        default=0,
    )

    def __str__(self):
        return ' '.join([pet.name for pet in self.tagged_pets.all()])


class Like(models.Model):
    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
    )

    photo = models.ForeignKey(
        PetPhoto,
        on_delete=models.CASCADE,
    )