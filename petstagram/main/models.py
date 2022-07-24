from datetime import date

from django.contrib.auth.models import User
from django.core.validators import MinLengthValidator, RegexValidator
from django.db import models


class Profile(models.Model):
    picture = models.ImageField(
        upload_to="profiles/"
    )

    birth = models.DateField(
        null=True,
        blank=True,
    )

    description = models.TextField(
        null=True,
        blank=True,
    )

    gender = models.CharField(
        max_length=20,
        null=True,
        blank=True,
        choices=(
            ('Male', 'Male'),
            ('Female', 'Female'),
            ('Do not show', 'Do not show')
        )
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE)  # special field extends the User model from Django

    def __str__(self):
        return self.user


class Pet(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )

    name = models.CharField(
        max_length=30,
    )

    pet_type = models.CharField(
        max_length=30,
        default="Other",
        choices=(
            ("cat", "Cat"),
            ("dog", "Dog"),
            ("bunny", "Bunny"),
            ("parrot", "Parrot"),
            ("fish", "Fish"),

        )
    )

    date_of_birth = models.DateField(
        null=True,
        blank=True,
    )

    def __str__(self):
        return self.name

    class Meta:
        unique_together = ('user', 'name')

    @property
    def age(self):
        today = date.today()
        age = today.year - self.date_of_birth.year - (
                    (today.month, today.day) < (self.date_of_birth.month, self.date_of_birth.day))
        return age


class PetPhoto(models.Model):
    photo = models.ImageField(
        upload_to="pets/"
    )

    tagged_pets = models.ManyToManyField(
        Pet,
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