from django import forms

from django.contrib.auth.models import User
from .models import Seller, Ad


class UpdateUserForm(forms.ModelForm):
    username = forms.CharField(max_length=100,
                               required=True,
                               widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(required=True,
                             widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ['username', 'email']


class UpdateSellerForm(forms.ModelForm):
    itn = forms.CharField(max_length=100,
                               required=True,
                               widget=forms.TextInput(attrs={'class': 'form-control'}))
    class Meta:
        model = Seller
        fields = ['itn']


class AdForm(forms.ModelForm):
    class Meta:
        model = Ad
        fields = '__all__'