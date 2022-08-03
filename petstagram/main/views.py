from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView

from petstagram.main.forms import PetForm, PhotoForm
from petstagram.main.models import Pet, PetPhoto, Like


def index(request):
    if request.user.is_authenticated:
        return redirect(reverse('dashboard'))
    return render(request, 'home_page.html')


class PetCreateView(LoginRequiredMixin, CreateView):
    model = Pet
    template_name = 'pet_templates/pet_create.html'
    success_url = reverse_lazy('index')
    form_class = PetForm

    def form_valid(self, form):
        pet = form.save(commit=False)
        pet.user = self.request.user
        pet.save()
        return redirect(reverse('index'))


class PetUpdateView(LoginRequiredMixin, UpdateView):
    model = Pet
    template_name = 'pet_templates/pet_edit.html'
    success_url = reverse_lazy('index')
    form_class = PetForm


class PetDeleteView(LoginRequiredMixin, DeleteView):
    model = Pet
    template_name = 'pet_templates/pet_delete.html'
    success_url = reverse_lazy('index')


class PhotoCreateView(LoginRequiredMixin, CreateView):
    model = PetPhoto
    template_name = 'photo_templates/photo_create.html'
    success_url = reverse_lazy('index')
    form_class = PhotoForm

    def form_valid(self, form):
        photo = form.save(commit=False)
        photo.user = self.request.user
        photo.save()
        return redirect(reverse('index'))


class PhotoUpdateView(LoginRequiredMixin, UpdateView):
    model = PetPhoto
    template_name = 'photo_templates/photo_edit.html'
    success_url = reverse_lazy('index')
    form_class = PhotoForm


def dashboard_view(request):
    pet_photos = PetPhoto.objects.all()
    context = {
        'pet_photos': pet_photos,
    }
    return render(request, 'dashboard.html', context)


def photo_detail_view(request, pk):
    photo = PetPhoto.objects.get(pk=pk)
    if request.user.is_authenticated:
        already_liked = photo.like_set.filter(user=request.user)
    else:
        already_liked = None
    context = {
        'photo': photo,
        'already_liked': already_liked,
    }
    return render(request, 'photo_templates/photo_details.html', context)


def like_photo(request, pk):
    new_like, created = Like.objects.get_or_create(user=request.user, photo_id=pk)
    photo = PetPhoto.objects.get(pk=pk)
    if created:
        photo.likes += 1
        photo.save()
    # else:
    #     photo.likes -= 1
    #     photo.like_set.first().delete()
    #     photo.save()

    return redirect(reverse('photo details', args=(pk, )))
