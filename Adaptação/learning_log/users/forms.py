from django.contrib.auth.models import User
from django import forms
from django.core.exceptions import ValidationError


# class LoginForm(forms.ModelForm):
#    class Meta:
#        model = User
#        fields = ['username', 'password']
#        labels = {'username': 'login', 'password': 'senha'}

class LoginForm(forms.Form):
    login = forms.CharField(max_length=30)
    senha = forms.CharField(max_length=30, widget=(forms.PasswordInput))


    # Seu eu precisar pegar dois campos ao memo tempo ou mais 
    # Ultiliza a função clean da seguinte maneira
    """Def clean(self)
            cleanned_data = super().clean
            nome = clenned_data.get('login')
            senha = cleanned_data.get('senha')
            
            Validação
        """
    

    def clean_login(self):
        nome = self.cleaned_data['login']
        if not(nome.isalnum()):
            raise ValidationError('O nome de usuário não pode ter caractere especial')
        return nome

