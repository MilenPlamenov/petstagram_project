from django.contrib.auth.views import LogoutView
from django.urls import path

from petstagram.petstagram_auth.views import profile_page_view, create_profile, show_401, edit_profile, delete_profile, \
    PetstagramLoginView

urlpatterns = (
    path('profile/', profile_page_view, name='profile'),
    path('profile/create/', create_profile, name='create profile'),
    path('unauthorized/', show_401, name='unauthorized'),
    path('profile/edit/', edit_profile, name='edit profile'),
    path('profile/delete/', delete_profile, name='delete profile'),
    path('login/', PetstagramLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
)
