from django.forms import fields
from .models import Photo
from django import forms


class PhotoForm(forms.ModelForm):

    class Meta:
        model = Photo
        fields = ('title', 'image', 'price', 'currency', 'description')

class CustomSignupForm(forms.ModelForm):
    first_name = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'placeholder': ('First name')}))
    last_name = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'placeholder': ('Last name')}))

    GENDERS = (('man', ('Man')), ('woman', ('Woman')))
    gender = forms.ChoiceField(label=('Gender'), choices=GENDERS, widget=forms.Select())
