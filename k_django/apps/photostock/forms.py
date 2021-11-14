import unicodedata
from django.forms import fields
from .models import Photo
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User 
from django.contrib.auth import (
    authenticate, get_user_model, password_validation, validators
)
from django.contrib.auth.validators import UnicodeUsernameValidator


class PhotoForm(forms.ModelForm):

    class Meta:
        model = Photo
        fields = ('title', 'image', 'price', 'currency', 'description')


class UsernameField(forms.CharField):
    def to_python(self, value):
        return unicodedata.normalize('NFKC', super().to_python(value))

    def widget_attrs(self, widget):
        return {
            **super().widget_attrs(widget),
            'autocapitalize': 'none',
            'autocomplete': 'username',
        }

class EmailField(forms.CharField):
    def to_python(self, value):
        return unicodedata.normalize('NFKC', super().to_python(value))

    def widget_attrs(self, widget):
        return {
            **super().widget_attrs(widget),
            'autocapitalize': 'none',
            'autocomplete': 'email',
        }

class CustomUserCreationForm(UserCreationForm):  
    error_messages = {
        'password_mismatch': ('Пароли не совпали, введите повторно'),
    }

    username = UsernameField(
        label='Имя пользователя', 
        min_length=5, 
        max_length=20, 
        widget=forms.TextInput(attrs={'autofocus': True}),
        help_text="Обязательное поле. Не более 150 символов. Только буквы, цифры и символы @/./+/-/_.")

    email = EmailField(
        label='Почта', 
        max_length=254,
        widget=forms.EmailInput(attrs={'autocomplete': 'email', 'autofocus' : True}),
        help_text='Введите почту')

    password1 = forms.CharField(
        label='Пароль', 
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}),
        help_text=password_validation.password_validators_help_text_html()) 

    password2 = forms.CharField(
        label='Подтверждение пароля', 
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}),
        strip=False,
        help_text=("Для подтверждения введите, пожалуйста, пароль ещё раз."),)

    class Meta:
        model = User
        fields = ("username",)
        field_classes = {'username': UsernameField}

    def username_clean(self):  
        username = self.cleaned_data['username'].lower()  
        new = User.objects.filter(username = username)  
        if new.count():  
            raise ValidationError("User Already Exist")  
        return username  
  
    def email_clean(self):  
        email = self.cleaned_data['email'].lower()  
        new = User.objects.filter(email=email)  
        if new.count():  
            raise ValidationError("Email Already Exist")  
        return email  
  
    def clean_password2(self):  
        password1 = self.cleaned_data['password1']  
        password2 = self.cleaned_data['password2']  
  
        if password1 and password2 and password1 != password2:  
            raise ValidationError("Password don't match")  
        return password2  
  
    def save(self, commit = True):  
        user = User.objects.create_user(  
            self.cleaned_data['username'],  
            self.cleaned_data['email'],  
            self.cleaned_data['password1']  
        )  
        return user  
