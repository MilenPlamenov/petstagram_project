from django.contrib import admin

from petstagram.petstagram_auth.models import Profile


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()
