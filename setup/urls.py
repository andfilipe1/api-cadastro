
from django.contrib import admin
from django.urls import path,include
from loja.views import ClientesViewSet, ProdutosViewSet, FornecedorViewSet
from rest_framework import routers


router = routers.DefaultRouter()
router.register('clientes', ClientesViewSet, basename='Cliente')
router.register('produtos', ProdutosViewSet, basename='Produto')
router.register('Fornecedores', FornecedorViewSet, basename='Fornededores')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls) )
]