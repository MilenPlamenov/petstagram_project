from django.urls import path

from petstagram.main.views import index, dashboard_view, photo_detail_view

urlpatterns = (
    path('', index, name='index'),
    path('dashboard/', dashboard_view, name='dashboard'),
    path('photo/details/<int:pk>/', photo_detail_view, name='photo details'),
)
