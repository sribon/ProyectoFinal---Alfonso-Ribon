from django.shortcuts import render , redirect
from django.views.generic.detail import DetailView
from .models import articulo
from accounts.models import Avatar
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required, permission_required
from . import forms
# Create your views here.
 


def aboutUs(request):
      return render(request, "page/aboutUs.html")


@login_required(login_url="/accounts/login/")
def agregarArticulo(request):
   if request.method =='POST':
       form=forms.CreateArticulo(request.POST,request.FILES)
       if form.is_valid :
           instance = form.save(commit=False)
           instance.autor = request.user
           instance.save()
           return redirect('List') 
   else:
       form= forms.CreateArticulo()
   return render(request,'page/agregar.html',{'formulario':form})


class ArticuloList(ListView):
      model = articulo 
      template_name = "page/articulo_list.html"

class ArticuloDetalle(DetailView):
      model = articulo
      template_name = "page/articulo_detalle.html"


class ArticuloUpdate(UpdateView):
      model = articulo
      success_url = "/pages"
      fields  = ['titulo','descripcion','cuerpo','imagen']


class ArticuloDelete(DeleteView):
      model = articulo
      success_url = "/pages"
