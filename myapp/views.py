from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.shortcuts import render
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.contrib.auth.models import User

# Create your views here.
def index(request):
    currentUser = request.user.username
    comida = PlatoComida.objects.all()
    for x, plato in enumerate(comida):
       setattr(plato, "pos", (x - int(x / 3) * 3 + 1, 1 + int(x / 3)))
    if currentUser == "":
        currentUser = "Invitado"
    return render(request, 'index.html',{
        'user' : currentUser,
        'dishes' : comida,
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
        User.save
        user = User(username=request.POST['username'], email=request.POST['email'])
        user.set_password(request.POST['password2'])
        user.save()
        messages.success(request, "Registro exitoso.")
        return redirect('login')
    
def producto(request, comida):
    producto = PlatoComida.objects.get(name=comida)
    return render(request, 'product.html', {
        'dish' : producto
    })
    
  
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
