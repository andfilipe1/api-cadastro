from django.contrib import admin
from loja.models import Cliente, Produto, Fornecedor

class Clientes(admin.ModelAdmin):
    list_display = ('id','nome', 'rg', 'cpf', 'data_inclusao')
    list_display_links = ('id', 'nome')
    search_fields = ('nome',)
    list_per_page = 20

admin.site.register(Cliente, Clientes)

class Produtos(admin.ModelAdmin):
    list_display = ('id', 'nome', 'codigo_produto', 'descricao')
    list_display_links = ('id', 'codigo_produto')
    search_fields = ('codigo_produto',)

admin.site.register(Produto, Produtos)

class Fornecedores(admin.ModelAdmin):
    list_display = ('id', 'nome', 'cliente', 'produto', 'tipo', 'CNPJ')
    list_display_links = ('id', 'produto', 'tipo',)

admin.site.register(Fornecedor, Fornecedores)