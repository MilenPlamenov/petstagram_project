from django.contrib import admin

from petstagram.main.models import Pet, PetPhoto


@admin.register(Pet)
class PetAdmin(admin.ModelAdmin):
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()


@admin.register(PetPhoto)
class PetPhotoAdmin(admin.ModelAdmin):
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()
