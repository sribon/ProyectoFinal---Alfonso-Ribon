from django.contrib import admin
from django.urls import path
from accounts import views 

app_name= 'accounts'

urlpatterns = [
    path('signup/',views.signup,name="signup"),
    path('login/',views.login_view,name="login"),
    path('logout',views.logout_view,name="logout"),
    path('editarPerfil', views.editarPerfil, name="EditarPerfil"),
    path('crearAvatar', views.agregarAvatar,name="agregarAvatar"),
]
