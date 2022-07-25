from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.shortcuts import render, redirect
from django.urls import reverse

from petstagram.main.models import Pet, PetPhoto
from petstagram.petstagram_auth.forms import CreateProfileForm, ProfileForm, EditProfile, EditExtendedProfile, \
    DeleteProfile, DeleteExtendedProfile
from petstagram.petstagram_auth.models import Profile


def show_401(request):
    return render(request, '401_error.html')


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

    return render(request, 'auth_templates/profile_create.html', context)


@login_required(login_url='/petstagramauth/unauthorized/')
def edit_profile(request):
    profile = Profile.objects.get(id=request.user.id)
    if profile.id != request.user.id:
        return redirect(reverse('index'))

    if request.method == "GET":
        user_form = EditProfile(instance=request.user)
        profile_form = EditExtendedProfile(instance=profile)
    else:
        user_form = EditProfile(request.POST, request.FILES, instance=request.user)
        profile_form = EditExtendedProfile(request.POST, request.FILES, instance=profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect(reverse('index'))

    context = {
        "user_form": user_form,
        "profile_form": profile_form,
    }
    return render(request, 'auth_templates/profile_edit.html', context)


@login_required(login_url='/petstagramauth/unauthorized/')
def delete_profile(request):
    profile = Profile.objects.get(id=request.user.id)
    if profile.id != request.user.id:
        return redirect(reverse('index'))

    if request.method == "GET":
        user_form = DeleteProfile(instance=request.user)
        profile_form = DeleteExtendedProfile(instance=profile)
    else:
        profile.picture.delete()
        profile.delete()
        request.user.delete()
        return redirect(reverse('index'))
    context = {
        "user_form": user_form,
        "profile_form": profile_form,
    }
    return render(request, 'auth_templates/profile_delete.html', context)


@login_required(login_url='/petstagramauth/unauthorized/')
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
    return render(request, 'auth_templates/profile_details.html', context)
