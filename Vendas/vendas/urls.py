"""vendas URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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

from django.conf.urls import include
from rest_framework import routers
from cliente.api.viewsets import ClienteViewSet
from compra.api.viewsets import CompraViewSet, CompraViewSetOut
from produto.api.viewsets import ProdutoViewSet

router = routers.DefaultRouter()
router.register(r'listaClientes', ClienteViewSet, basename="ListaClientes")
router.register(r'listaCompra', CompraViewSet, basename="ListaCompra")
router.register(r'listaProduto', ProdutoViewSet, basename="ListaProdutos")
router.register(r'ViewCompras', CompraViewSetOut, basename="ViewCompras")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]
