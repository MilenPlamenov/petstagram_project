from django.contrib.auth import get_user_model
from django.db import models

UserModel = get_user_model()


class Profile(models.Model):
    MALE = 'Male'
    FEMALE = 'FEMALE'
    DO_NOT_SHOW = 'Do not show'
    GENDER_CHOICES = (MALE, FEMALE, DO_NOT_SHOW)

    PICTURE_UPLOAD_DIR = 'profiles/'

    picture = models.ImageField(
        upload_to=PICTURE_UPLOAD_DIR,
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
        max_length=len(max(GENDER_CHOICES, key=len)),
        null=True,
        blank=True,
        choices=tuple((g, g) for g in GENDER_CHOICES),
    )

    user = models.OneToOneField(UserModel, on_delete=models.CASCADE)  # special field extends the User model from Django

    def __str__(self):
        return str(self.user)
