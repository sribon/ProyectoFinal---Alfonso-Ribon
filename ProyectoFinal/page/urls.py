from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('', views.ArticuloList.as_view(), name='List'),
    path(r'^(?P<pk>\d+)$', views.ArticuloDetalle.as_view(), name='Detail'),
    path('agregar/',views.agregarArticulo,name='agregar'),
    path(r'^editar/(?P<pk>\d+)$', views.ArticuloUpdate.as_view(), name='Edit'),
    path(r'^borrar/(?P<pk>\d+)$', views.ArticuloDelete.as_view(), name='Delete'),
    path('aboutUs/',views.aboutUs, name="AboutUs"),
]
