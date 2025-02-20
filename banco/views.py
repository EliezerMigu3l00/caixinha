from datetime import datetime,date
from django.shortcuts import (
    render,
    redirect,
    get_object_or_404
)
from django.views.decorators.http import (
    require_POST,
    require_GET
)
from django.contrib import messages
from .models import (
    Cliente,
    Emprestimo,
    CartaoCredito
)


@require_GET
def home(request):
    return render(request, 'home.html')


@require_GET
def listar_cliente(request):
    clientes = Cliente.objects.all()

    contexto = {
        'clientes': clientes
    }
    return render(request, 'listar_clientes.html', contexto)


@require_POST
def cadastrar_cliente(request):
    nome = request.POST.get('nome')
    data_nascimento_str = request.POST.get('data_nascimento')
    cpf = request.POST.get('cpf')
    telefone = request.POST.get('telefone')
    renda_mensal = request.POST.get('renda_mensal')
    
    try:
        data_nascimento = datetime.strptime(
            data_nascimento_str, '%Y-%m-%d').date()
    except ValueError:
        messages.error(request, 'Formato de data de nascimento inválido.')
        return redirect('cadastrar_cliente_formulario')

    data_atual = datetime.today().date()
    idade = data_atual.year - data_nascimento.year - int(
        (data_atual.month, data_atual.day) < (data_nascimento.month, data_nascimento.day)
    )

    if idade >= 12:
        Cliente.objects.create(
            nome=nome,
            data_nascimento=data_nascimento,
            cpf=cpf,
            telefone=telefone,
            renda_mensal=renda_mensal,
        )

        messages.success(request, 'Cliente foi cadastrado com sucesso!')

        return redirect('listar_cliente')
    else:
        messages.error(
            request, 'A idade do cliente deve ser maior ou igual a 12 anos'
        )
        return redirect('cadastrar_cliente_formulario')


def excluir_cliente(request, id):
    cliente = Cliente.objects.get(id=id)
    cliente.delete()

    return redirect('listar_cliente')


def atualizar_cliente(request, id):
    cliente = get_object_or_404(Cliente, id=id)

    if request.method == 'POST':
        nome = request.POST.get('nome')
        data_nascimento_str = request.POST.get('data_nascimento')
        cpf = request.POST.get('cpf')
        telefone = request.POST.get('telefone')
        renda_mensal = request.POST.get('renda_mensal')

        try:
            data_nascimento = datetime.strptime(
                data_nascimento_str, '%Y-%m-%d').date()
        except ValueError:
            messages.error(request, 'Formato de data de nascimento inválido.')
            return redirect('atualizar_cliente', id=cliente.id)

        cliente.nome = nome
        cliente.data_nascimento = data_nascimento
        cliente.cpf = cpf
        cliente.telefone = telefone
        cliente.renda_mensal = renda_mensal

        cliente.save()

        messages.success(request, 'Cliente atualizado com sucesso!')
        return redirect('listar_cliente')

    contexto = {'cliente': cliente}
    return render(request, 'atualizar_cliente.html', contexto)


@require_GET
def cadastrar_cliente_formulario(request):
    return render(request, 'cadastro_cliente.html')


@require_POST
def solicitar_emprestimo(request, id):
    cliente = get_object_or_404(Cliente, id=id)
    if not cliente.cpf:
        messages.error(request, 'CPF não cadastrado. O cliente deve ter um CPF válido para solicitar um empréstimo.')
        return redirect('listar_cliente')

    idade = date.today().year - cliente.data_nascimento.year

    if idade >= 18:
        if cliente.renda_mensal <= 5000:
            Emprestimo.objects.create(cliente=cliente, valor_emprestimo=2500)
        elif cliente.renda_mensal <= 10000:
            Emprestimo.objects.create(cliente=cliente, valor_emprestimo=5000)
        else:
            Emprestimo.objects.create(cliente=cliente, valor_emprestimo=10000)   
        return redirect('listar_cliente')
    else:
        messages.error(request, 'Cliente deve ter pelo menos 18 anos para solicitar um empréstimo.')
        return redirect('listar_cliente')


@require_POST
def solicitar_cartao_credito(request, id):
    cliente = get_object_or_404(Cliente, id=id)
    if not cliente.cpf:
        messages.error(request, 'CPF não cadastrado. O cliente deve ter um CPF válido para solicitar um cartão de crédito.')
        return redirect('listar_cliente')

    idade = date.today().year - cliente.data_nascimento.year

    if idade < 18:
        messages.error(request, 'Cliente deve ter pelo menos 18 anos para solicitar limite de crédito.')
        return redirect('listar_cliente')

    if cliente.renda_mensal < 1350:
        messages.error(request, 'O cliente deve ter uma renda válida para solicitar um cartão de crédito.')
    elif 1350 <= cliente.renda_mensal <= 5000:
        CartaoCredito.objects.create(cliente=cliente, limite_credito=2500)
    elif 5000 < cliente.renda_mensal <= 10000:
        CartaoCredito.objects.create(cliente=cliente, limite_credito=5000)
    elif cliente.renda_mensal > 10000:
        CartaoCredito.objects.create(cliente=cliente, limite_credito=10000)

    return redirect('listar_cliente')