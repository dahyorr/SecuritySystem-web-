
from django import forms
from . import models
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model


class RfidForm(forms.ModelForm):
    class Meta:
        model = models.RfidId
        fields = ('ownername', 'code')
        labels = {'ownername': "Tag Owner", 'code': 'Tag Code'}
        widgets = {
            'ownername': forms.TextInput(attrs={'class': 'form-control', 'label': "Tag owner"}),
            'code': forms.TextInput(attrs={'class': 'form-control'}),
        }


class UserCreateForm(UserCreationForm):
    class Meta:
        fields = ('username', 'first_name', 'last_name', 'email', "password1", 'password2')
        model = get_user_model()
