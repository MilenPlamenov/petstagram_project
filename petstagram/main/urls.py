from django.urls import path

from petstagram.main.views import index, dashboard_view, photo_detail_view, PetCreateView, PetUpdateView, PetDeleteView, \
    PhotoCreateView, PhotoUpdateView, like_photo

urlpatterns = (
    path('', index, name='index'),
    path('dashboard/', dashboard_view, name='dashboard'),
    path('photo/details/<int:pk>/', photo_detail_view, name='photo details'),
    path('pet/add/', PetCreateView.as_view(), name='create pet'),
    path('pet/edit/<int:pk>/', PetUpdateView.as_view(), name='edit pet'),
    path('pet/delete/<int:pk>/', PetDeleteView.as_view(), name='delete pet'),
    path('photo/add/', PhotoCreateView.as_view(), name='create photo'),
    path('photo/edit/<int:pk>/', PhotoUpdateView.as_view(), name='edit photo'),
    path('like/<int:pk>/', like_photo, name='like'),
)
