from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView

from petstagram.main.forms import PetForm, PhotoForm
from petstagram.main.models import Pet, PetPhoto


def index(request):
    return render(request, 'home_page.html')


class PetCreateView(LoginRequiredMixin, CreateView):
    model = Pet
    template_name = 'pet_templates/pet_create.html'
    success_url = reverse_lazy('index')
    form_class = PetForm

    def form_valid(self, form):
        task = form.save(commit=False)
        task.user = self.request.user
        task.save()
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


class PhotoUpdateView(LoginRequiredMixin, UpdateView):
    model = PetPhoto
    template_name = 'photo_templates/photo_edit.html'
    success_url = reverse_lazy('index')
    form_class = PhotoForm


@login_required(login_url=settings.LOGIN_URL)
def dashboard_view(request):
    pet_photos = PetPhoto.objects.all()
    context = {
        'pet_photos': pet_photos,
    }
    return render(request, 'dashboard.html', context)


@login_required(login_url=settings.LOGIN_URL)
def photo_detail_view(request, pk):
    photo = PetPhoto.objects.get(pk=pk)

    context = {
        'photo': photo,
    }
    return render(request, 'photo_templates/photo_details.html', context)
