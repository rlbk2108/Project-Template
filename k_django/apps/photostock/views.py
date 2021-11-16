from django.forms import fields
from django import forms
from django.forms.models import fields_for_model
from django.http import request
from django.shortcuts import get_object_or_404, render, redirect, HttpResponseRedirect
from .models import Warehouse
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView
from django.views.generic.edit import UpdateView, DeleteView
from django.contrib.auth.views import (LoginView, 
                                       LogoutView, 
                                       PasswordChangeView, 
                                       PasswordChangeDoneView,
                                       PasswordResetView,
                                       PasswordResetConfirmView,
                                       PasswordResetCompleteView,
                                       PasswordResetDoneView)
from django.views import generic
from django.contrib.auth.forms import UserCreationForm
from .forms import CustomUserCreationForm



class PhotoListView(ListView):
    model = Warehouse
    context_object_name = 'photos'
    template_name = 'photostock/photo_list.html'

class PhotoDetailView(DetailView):
    model = Warehouse
    context_object_name = 'photo'
    template_name = 'photostock/photo_detail.html'

class PhotoCreateView(CreateView):
    model = Warehouse
    context_object_name = 'photo'
    fields = ['product_name', 'product_number']
    success_url = reverse_lazy('photo_list')
    template_name = 'photostock/photo_form.html'

class PhotoUpdateView(UpdateView):
    model = Warehouse
    fields = ['product_name', 'product_number']
    context_object_name = 'photo'
    success_url = reverse_lazy('photo_list')
    template_name = 'photostock/photo_update.html'

class PhotoDeleteView(DeleteView):
    model = Warehouse
    context_object_name = 'photo'
    success_url = reverse_lazy('photo_list')
    template_name = 'photostock/photo_delete.html' 

class PhotoLoginView(LoginView):
    model = Warehouse
    template_name = 'registration/login.html'

class PhotoLogoutView(LogoutView):
    model = Warehouse
    template_name = 'registration/logout.html'

class SignUpView(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

    def register(request):  
        if request.POST == 'POST':  
            form = CustomUserCreationForm()  
            if form.is_valid():  
                form.save()  
        else:  
            form = CustomUserCreationForm()  
        context = {  
            'form':form  
        }  
        return render(request, 'signup.html', context)  

class AccountPassChange(PasswordChangeView):
    template_name = 'registration/password_change.html'

class AccountPassChangeDone(PasswordChangeDoneView):
    pass

class AccountPassReset(PasswordResetView):
    pass

class AccountPassResetConfirm(PasswordResetConfirmView):
    pass

class AccountPassChange(PasswordChangeView):
    pass

class AccountPassChange(PasswordChangeView):
    pass

class AccountPassChange(PasswordChangeView):
    pass