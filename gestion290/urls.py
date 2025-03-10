"""
URL configuration for gestion290 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from gestion290_app.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('rol/insertar/', insertar_rol, name='insertar_rol'),
    path('rol/listar/', listar_roles , name='listar_roles'),
    
    path('usuario/insertar/', insertar_usuario, name='insertar_usuario'),
    path('usuario/listar/', listar_usuarios, name='listar_usuarios'),
    path('usuario/actualizar/<int:id>/', actualizar_usuario, name='actualizar_usuario'),
    path('usuario/eliminar/<int:id>/', eliminar_usuario, name='eliminar_usuario'),
    path('usuario/login/', login_usuario, name='login'),
    path('usuario/logout/', logout_usuario, name='logout'),
    path('usuario/ver_pefil/', ver_mi_perfil, name='ver_mi_perfil')
]
