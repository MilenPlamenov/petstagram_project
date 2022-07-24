from django.urls import path

from petstagram.main.views import index, dashboard_view, profile_page_view, photo_detail_view, create_profile

urlpatterns = [
    path('', index, name='index'),
    path('dashboard/', dashboard_view, name='dashboard'),
    path('profile/', profile_page_view, name='profile'),
    path('photo/details/<int:pk>/', photo_detail_view, name='photo details'),
    path('profile/create/', create_profile, name='create profile'),
]
