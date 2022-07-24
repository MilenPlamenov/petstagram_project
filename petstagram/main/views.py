from django.contrib.auth import login
from django.db import transaction
from django.shortcuts import render, redirect

from petstagram.main.forms import CreateProfileForm, ProfileForm
from petstagram.main.models import Pet, PetPhoto


def index(request):
    return render(request, 'home_page.html')


def dashboard_view(request):
    pet_photos = PetPhoto.objects.all()
    context = {
        'pet_photos': pet_photos,
    }
    return render(request, 'dashboard.html', context)


def profile_page_view(request):
    user_pets = Pet.objects.filter(user=request.user)
    pet_photos = PetPhoto.objects \
        .filter(tagged_pets__in=user_pets) \
        .distinct()

    photos_count = pet_photos.count()
    photos_likes = sum([p.likes for p in pet_photos])
    context = {
        'user_pets': user_pets,
        'photos_count': photos_count,
        'photos_likes': photos_likes,
    }
    return render(request, 'profile_details.html', context)


def photo_detail_view(request, pk):
    photo = PetPhoto.objects.get(pk=pk)

    context = {
        'photo': photo,
    }
    return render(request, 'photo_details.html', context)


@transaction.atomic  # if one operation is invalid - all are
def create_profile(request):
    if request.method == "GET":
        user_form = CreateProfileForm()
        profile_form = ProfileForm()
    else:
        user_form = CreateProfileForm(request.POST)
        profile_form = ProfileForm(request.POST, request.FILES)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()

            login(request, user)
            return redirect('/')

    context = {
        "user_form": user_form,
        "profile_form": profile_form,
    }

    return render(request, 'profile_create.html', context)
