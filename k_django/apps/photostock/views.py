from django.http import request
from django.shortcuts import get_object_or_404, render, redirect, HttpResponseRedirect
from .models import Photo
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView
from django.views.generic.edit import UpdateView, DeleteView
from django.contrib.auth.views import LoginView, LogoutView
from .forms import PhotoForm, CustomSignupForm




class PhotoListView(ListView):
    model = Photo
    context_object_name = 'photos'
    template_name = 'photostock/photo_list.html'

class PhotoDetailView(DetailView):
    model = Photo
    context_object_name = 'photo'
    template_name = 'photostock/photo_detail.html'

class PhotoCreateView(CreateView):
    model = Photo
    context_object_name = 'photo'
    fields = ['title', 'description', 'image', 'price', 'currency']
    success_url = reverse_lazy('photo_list')
    template_name = 'photostock/photo_form.html'

class PhotoUpdateView(UpdateView):
    model = Photo
    fields = ['title', 'image', 'description', 'price', 'currency']
    context_object_name = 'photo'
    success_url = reverse_lazy('photo_list')
    template_name = 'photostock/photo_update.html'

class PhotoDeleteView(DeleteView):
    model = Photo
    context_object_name = 'photo'
    success_url = reverse_lazy('photo_list')
    template_name = 'photostock/photo_delete.html' 

class PhotoLoginView(LoginView):
    model = Photo
    template_name = 'registration/login.html'

class PhotoLogoutView(LogoutView):
    model = Photo
    template_name = 'registration/account_logout.html'

def signup(self, request, user, form):
    if request.method == 'POST':
        form = CustomSignupForm(request.POST)
        if form.is_valid():
            user.first_name = self.cleaned_data['first_name']
            user.last_name = self.cleaned_data['last_name']
            user.gender = self.cleaned_data['gender']

            user.save()

    else:
        form = CustomSignupForm()
    return render(request, 'signup.html', {'form': form})