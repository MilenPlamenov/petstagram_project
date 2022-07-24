from django.urls import path

from petstagram.petstagram_auth.views import profile_page_view, create_profile, show_401

urlpatterns = (
    path('profile/', profile_page_view, name='profile'),
    path('profile/create/', create_profile, name='create profile'),
    path('unauthorized/', show_401, name='unauthorized'),
)