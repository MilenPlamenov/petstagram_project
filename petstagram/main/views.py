from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.urls import reverse

from petstagram.main.models import Pet, PetPhoto


def index(request):
    return render(request, 'home_page.html')


@login_required(login_url='/petstagramauth/unauthorized/')
def dashboard_view(request):
    pet_photos = PetPhoto.objects.all()
    context = {
        'pet_photos': pet_photos,
    }
    return render(request, 'dashboard.html', context)


@login_required(login_url='/petstagramauth/unauthorized/')
def photo_detail_view(request, pk):
    photo = PetPhoto.objects.get(pk=pk)

    context = {
        'photo': photo,
    }
    return render(request, 'photo_details.html', context)
