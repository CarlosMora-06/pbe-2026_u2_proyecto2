"""
URL configuration for u2_proyecto1 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.1/topics/http/urls/
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

from pedidos_app.views import crear_cliente, listar_clientes, listar_cliente, borrar_cliente, modificar_cliente

urlpatterns = [
    #cliente
    path('admin/', admin.site.urls),
    path('cliente/agregar', crear_cliente),
    path('clientes', listar_clientes),
    path('cliente/<int:id>', listar_cliente),
    path('cliente/eliminar/<int:id>', borrar_cliente),
    path('cliente/modificar/<int:id>', modificar_cliente),

    #items
    path('item/agregar', crear_item),
    path('item', listar_items),
    path('item/<int:id>', listar_item),
    path('item/eliminar/<int:id>', eliminar_item),
    path('item/modificar/<int:id>', modificar_item),
]