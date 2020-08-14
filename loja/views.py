from rest_framework import viewsets
from loja.models import Cliente, Produto, Fornecedor
from loja.serializer import ClienteSerializer, ProdutoSerializer, FornecedorSerializer

class ClientesViewSet(viewsets.ModelViewSet):
    """Exibindo todos os clientes"""
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

class ProdutosViewSet(viewsets.ModelViewSet):
    """Exibindo todos os produtos"""
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer

class FornecedorViewSet(viewsets.ModelViewSet):
    """Listando todos os Fornecedores"""
    queryset = Fornecedor.objects.all()
    serializer_class = FornecedorSerializer

    