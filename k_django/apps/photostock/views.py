from django.forms import fields
from django import forms
from django.forms.models import fields_for_model
from django.http import request
<<<<<<< HEAD
from django.shortcuts import render, redirect, HttpResponse
from .models import Photo
=======
from django.shortcuts import get_object_or_404, render, redirect, HttpResponseRedirect
from .models import Warehouse
>>>>>>> 017fc8feb087caab074262456c3bca2009da94bd
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
from django.contrib.auth.forms import UserCreationForm, PasswordResetForm
from .forms import CustomUserCreationForm
from django.db.models.query_utils import Q
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.contrib import messages
from django.contrib.auth.tokens import default_token_generator
from django.contrib.auth.models import User
from django.core.mail import send_mail, BadHeaderError
from django.template.loader import render_to_string



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

def password_reset_request(request):
	if request.method == "POST":
		password_reset_form = PasswordResetForm(request.POST)
		if password_reset_form.is_valid():
			data = password_reset_form.cleaned_data['email']
			associated_users = User.objects.filter(Q(email=data))
			if associated_users.exists():
				for user in associated_users:
					subject = "Password Reset Requested"
					email_template_name = "password/password_reset_email.txt"
					c = {
					"email":user.email,
					'domain':'127.0.0.1:8000',
					'site_name': '',
					"uid": urlsafe_base64_encode(force_bytes(user.pk)),
					'token': default_token_generator.make_token(user),
					'protocol': 'https',
					}
					email = render_to_string(email_template_name, c)
					try:
						send_mail(subject, email, 'EMAIL_HOST_USER', [user.email], fail_silently=False)
					except BadHeaderError:

						return HttpResponse('Invalid header found.')
						
					messages.success(request, 'A message with reset password instructions has been sent to your inbox.')
					return redirect ("/photos")
			messages.error(request, 'An invalid email has been entered.')
	password_reset_form = PasswordResetForm()
	return render(request=request, template_name="password/password_reset.html", context={"password_reset_form":password_reset_form})



class AccountPassChange(PasswordChangeView):
    template_name = 'password/password_change.html'

class AccountPassChangeDone(PasswordChangeDoneView):
    template_name = 'password/password_change_done.html'

class AccountPassReset(PasswordResetView):
    template_name = 'password/password_reset.html'

class AccountPassResetConfirm(PasswordResetConfirmView):
    template_name = 'password/password_reset_confirm.html'

class AccountPassResetComplete(PasswordResetCompleteView):
    template_name = 'password/password_reset_complete.html'

class AccountPassResetDone(PasswordResetDoneView):
    template_name = 'password/password_reset_done.html'
