from django import forms
from accounts import models


class UserForm(forms.ModelForm):
    class Meta:
        model = models.User
        fields = ('username', 'first_name', "last_name", 'email')
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control   '}),
            'last_name': forms.TextInput(attrs={'class': 'form-control   '}),
            'email': forms.EmailInput(attrs={'class': 'form-control   '}),
        }
