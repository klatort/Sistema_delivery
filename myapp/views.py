from time import sleep
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
    comidas = PlatoComida.objects.all()
    for x, plato in enumerate(comidas):
       setattr(plato, "pos", (x - int(x / 3) * 3 + 1, 1 + int(x / 3)))
    if request.method == 'POST':
        comida = list(request.POST)[1]
        try:
            currUser = User.objects.get(username = currentUser)
            try:
                query = CarritoCompra.objects.get(user=currUser)
            except:
                query = CarritoCompra(user=currUser)
        except:
            try:
                query.cart = request.session['cart']
                print("owo")
            except:
                class owo:
                    def __init__(self) -> None:
                        pass
                query = owo()
                setattr(query, "cart","")
        search = query.cart.find(comida)
        if search == -1:
            query.cart += comida + r"-1/"
        else:
            end = query.cart.find(r"/", search)
            auxString = query.cart[search:end]
            print(auxString)
            newString = auxString.split("-")
            print(newString)
            value = int(newString[1]) + 1
            print(value)
            newString = newString[0] + "-" + str(value)
            print(newString)
            query.cart = query.cart.replace(auxString, newString)
        try:
            query.save()
        except:
            request.session['cart'] = query.cart
            print(request.session['cart'])
    return render(request, 'index.html',{
        'user' : currentUser,
        'dishes' : comidas,
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
        messages.success(request, "Registro exitoso.")
        return redirect('login')
    
def producto(request, comida):
    currentUser = request.user.username
    producto = PlatoComida.objects.get(name=comida)
    if request.method == 'POST':
        print(request.POST)
        try:
            currUser = User.objects.get(username = currentUser)
            try:
                query = CarritoCompra.objects.get(user=currUser)
            except:
                query = CarritoCompra(user=currUser)
        except:
            try:
                query.cart = request.session['cart']
            except:
                class owo:
                    def __init__(self) -> None:
                        pass
                query = owo()
                setattr(query, 'cart',"")
        search = query.cart.find(comida)
        if search == -1:
            query.cart += comida + "-" + str(request.POST['quantity']) + r"/"
        else:
            end = query.cart.find(r"/", search)
            auxString = query.cart[search:end]
            print(auxString)
            newString = auxString.split("-")
            print(newString)
            value = int(newString[1]) + int(request.POST['quantity'])
            print(value)
            newString = newString[0] + "-" + str(value)
            print(newString)
            query.cart = query.cart.replace(auxString, newString)
        try:
            print(request.user)
            query.save()
        except:
            request.session['cart'] = query
            print(request.session['cart'])
    return render(request, 'product.html', {
        'user' : currentUser,
        'dish' : producto
    })
    
def carrito(request):
    currentUser = request.user.username
    cartData = ""
    try:
        currUser = User.objects.get(username = currentUser)
        query = CarritoCompra.objects.get(user=currUser)
    except:
        query = request.session[cart]
    cartData = query.cart.split(r"/")
    total = 0
    for i in range(len(cartData) - 1):
        cartData[i] = cartData[i].split("-")
        print(cartData[i][0])
        obj = PlatoComida.objects.get(name=cartData[i][0])
        val = float(obj.price) * float(cartData[i][1])
        cartData[i].append(str(val) + "0")
        total += val
    print(cartData)
    cartData.pop()
    return render(request, 'carrito.html',{
        'user' : currentUser,
        'data' : cartData,
        'total': str(total) + '0',
    })
    
def anotherFunction(request):
    currentUser = request.user.username
    if request.method == 'POST':
        task = Task.objects.get(name=list(request.POST)[1])
        task.done = not task.done
        task.save()
        return redirect('test')
    return render(request, 'projects.html',{
        'user' : currentUser,
        'projects': Project.objects.all(),
        'usuario' : request.user.username
    })
