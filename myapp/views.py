from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.shortcuts import get_object_or_404, render
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.contrib.auth.models import User

# Create your views here.
def index(request):
    currentUser = request.user.username
    
    if currentUser == "":
        currentUser = "Invitado"
    return render(request, 'index.html',{
        'usuario' : currentUser
    })

def log_in(request):
    if request.method == 'GET':
        logout(request)
        return render(request, 'Login.html', {
        'form' : LoginForm()
        })
    else:
        user = authenticate(username=request.POST['username'], password=request.POST['password'])
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            messages.add_message(request, messages.INFO, 'Revise su usuario/contraseña por favor.')
            return redirect('login')
            
def register(request):
    if request.method == 'GET':
        return render(request, 'register.html', {
            'form' : NewUserForm()
            })
    else:
        user = User(username=request.POST['username'], email=request.POST['email'])
        user.set_password(request.POST['password2'])
        user.save()
        login(request, user)
        messages.success(request, "Registro exitoso.")
        return redirect('index')
    
def anotherFunction(request):
    if request.method == 'POST':
        task = Task.objects.get(name=list(request.POST)[1])
        task.done = not task.done
        task.save()
        return redirect('test')
    return render(request, 'projects.html',{
        'projects': Project.objects.all(),
        'usuario' : request.user.username
    })