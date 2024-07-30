from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import LoginForm
from django.contrib.auth import authenticate
from django.contrib.auth import login as auh_login


def login(request):
    error = False
    if request.method != 'POST':
        form = LoginForm()
    else:
        form = LoginForm(data=request.POST)
        if form.is_valid():
            # Nome Padrão é: username = request.POST.get('username')
            # Senha Padrão é: password = request.POST.get('password')
            username = request.POST.get('login')
            password = request.POST.get('senha')
            user = authenticate(username=username, password=password)
            if user:
                auh_login(request, user)
                return HttpResponseRedirect(reverse('index'))
            else:
                error = True
    context = {'form': form, 'error': error}
    return render(request, 'users/login.html', context)





