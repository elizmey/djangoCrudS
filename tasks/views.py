# filepath: c:\Users\Admin\Documents\ProyectosPythonS\djangoCrudS\tasks\views.py
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

def home(request):
    return render(request, 'home.html')

def signup(request):
    return render(request, 'signup.html')

def signup(request):
    if request.method =="GET":
        return render(request,
                      "signup.html",
                      {"form":UserCreationForm})
    else:
        if request.POST["password1"]==request.POST["password2"]:
            try:
               user = User.objects.create_user(username=request.POST["username"],
                                         password=request.POST["password1"])
               user.save()
               return HttpResponse("el usuario creado correctamente")
            except Exception as e:
                return HttpResponse(f"Error al crear el usuario: {e}")
        else:
            return HttpResponse("las contraseñas no coinciden")
        