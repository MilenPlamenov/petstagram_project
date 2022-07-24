from django.contrib.auth import get_user_model
from django.db import models

UserModel = get_user_model()


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

    user = models.OneToOneField(UserModel, on_delete=models.CASCADE)  # special field extends the User model from Django

    def __str__(self):
        return str(self.user)
