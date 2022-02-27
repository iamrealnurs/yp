from django import forms
from django.forms import inlineformset_factory

from django.contrib.auth.models import User
from .models import Seller, Ad, Picture


class UpdateUserForm(forms.ModelForm):
    username = forms.CharField(max_length=100,
                               required=True,
                               widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(required=True,
                             widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ['username', 'email']


class AdForm(forms.ModelForm):
    class Meta:
        model = Ad
        fields = '__all__'


class AdPictureForm(forms.ModelForm):
    class Meta:
        model = Picture
        fields = '__all__'


AdPictureInlineFormset = inlineformset_factory(
    Ad,
    Picture,
    form=AdPictureForm,
)


def check_itn(itn):
    if len(itn) not in (10, 12):
        return False

    def itn_csum(itn):
        k = (3, 7, 2, 4, 10, 3, 5, 9, 4, 6, 8)
        pairs = zip(k[11 - len(itn):], [int(x) for x in itn])
        return str(sum([k * v for k, v in pairs]) % 11 % 10)

    if len(itn) == 10:
        return itn[-1] == itn_csum(itn[:-1])
    else:
        return itn[-2:] == itn_csum(itn[:-2]) + itn_csum(itn[:-1])


class UpdateSellerForm(forms.ModelForm):
    itn = forms.CharField(max_length=100,
                          required=True,
                          widget=forms.TextInput(attrs={'class': 'form-control'}))

    def clean_itn(self):
        data = self.cleaned_data.get('itn')

        if not check_itn(data):
            raise forms.ValidationError('ITN is Incorrect')

        return data

    class Meta:
        model = Seller
        fields = ['itn']

