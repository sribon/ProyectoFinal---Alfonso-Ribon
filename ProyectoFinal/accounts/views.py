from django.http import request
from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login,logout
from accounts.forms import UserRegisterForm, UserEditForm , AvatarCreateForm 
from accounts.models import Avatar
from django.contrib.auth.decorators import login_required
from .models import Avatar
from django.views.generic.edit import CreateView, UpdateView, DeleteView
# Create your views here.

 



def signup(request):
      
      if request.method == "POST":

            form = UserRegisterForm(request.POST)

            if form.is_valid():
                  username = form.cleaned_data['username']
                 
                  form.save()

                  return render(request, "page/home.html", {"mensaje": "Usuario creado exitosamente"})

      else: 
            form = UserRegisterForm()

      return render(request, "accounts/signup.html", {"form": form})
 
def login_view(request):
   if request.method =='POST':
       form=AuthenticationForm(data=request.POST)
       if form.is_valid():
           user=form.get_user()
           login(request,user)
           return redirect('home')
   else:
       form= AuthenticationForm()
   return render(request,'accounts/login.html',{'formulario':form})
 
def logout_view(request):
   if request.method=='POST':
       logout(request)
       return redirect('home')


###
def editarPerfil(request):
    
    usuario = request.user  #Instancia del login
    if request.method == 'POST':
        
        miFormulario = UserEditForm(request.POST)
        if miFormulario.is_valid():
            
            informacion = miFormulario.cleaned_data
            
            usuario.email = informacion['email']
            usuario.password1 = informacion['password1']
            usuario.password2 = informacion['password2']
            usuario.save()
            
            return render(request, "page/home.html")
    
    else:
        miFormulario = UserEditForm(initial={'email':usuario.email})
        avatares= Avatar.objects.filter(user=request.user)
    return render(request, "accounts/editarPerfil.html", {"miFormulario":miFormulario, "usuario":usuario, "avatar":avatares})


@login_required(login_url="/accounts/login/")
def agregarAvatar(request):
   if request.method =='POST':
       form= AvatarCreateForm(request.POST,request.FILES)
       if form.is_valid() :
           instance = form.save(commit=False)
           instance.user = request.user
           instance.save()
           return render(request,"page/home.html") 
   else:
       form= AvatarCreateForm()
   return render(request,"accounts/agregarAvatar.html",{"formulario":form})




