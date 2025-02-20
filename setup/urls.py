from django.contrib import admin
from django.urls import path
from banco.views import (
    home,
    listar_cliente,
    cadastrar_cliente_formulario,
    cadastrar_cliente,
    solicitar_emprestimo,
    solicitar_cartao_credito,
    excluir_cliente,
    atualizar_cliente
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('listar-cliente/',
         listar_cliente,
         name='listar_cliente'),
    path(
        'cadastrar-cliente_formulario/',
        cadastrar_cliente_formulario,
        name='cadastrar_cliente_formulario'),
    path('cadastrar_cliente',
         cadastrar_cliente,
         name='cadastrar_cliente'),
    path('solicitar-emprestimo/<int:id>',
         solicitar_emprestimo,
         name='solicitar_emprestimo'),
    path('solicitar-cartao-credito/<int:id>',
         solicitar_cartao_credito,
         name='solicitar_cartao_credito'),
    path('exclir-cliente/<int:id>',
         excluir_cliente,
         name='excluir_cliente'),
    path('atualizar-cliente/<int:id>/',
         atualizar_cliente,
         name='atualizar_cliente'),
]
