from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages

# Create your views here.
def index(request):
    currentUser = request.user.username
    if currentUser == "":
        currentUser = "Invitado"
    return render(request, 'index.html',{
        'titulo' : currentUser
    })

def log_in(request):
    if request.method == 'GET':
        logout(request)
        return render(request, 'Login.html', {
        'form' : LoginForm()
        })
    else:
        if 'omitir' in request.POST:
            return redirect('index')
        elif 'login' in request.POST:
            user = authenticate(username=request.POST['username'], password=request.POST['password'])
            print(user)
            if user is not None:
                login(request, user)
                return redirect('index')
            else:
                messages.add_message(request, messages.INFO, 'Revise su usuario/contraseña por favor.')
                return redirect('login')