from django.contrib.auth.models import User
from django import forms


# class LoginForm(forms.ModelForm):
#    class Meta:
#        model = User
#        fields = ['username', 'password']
#        labels = {'username': 'login', 'password': 'senha'}

class LoginForm(forms.Form):
    login = forms.CharField(max_length=30)
    senha = forms.CharField(max_length=30, widget=(forms.PasswordInput))