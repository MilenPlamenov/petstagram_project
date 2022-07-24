from django.contrib import admin

# Register your models here.
from petstagram.main.models import Profile, Pet, PetPhoto

admin.site.register(Profile)

admin.site.register(Pet)

admin.site.register(PetPhoto)