from django.shortcuts import render, redirect
from django.http import HttpResponse

###############
# BANDO DE DADOS
###############

from .models import Veiculo
from .forms import VeiculoForm

from .models import Motorista
from .forms import MotoristaForm

from .models import Controle
from .forms import ControleForm

# Create your views here.
global oleo
oleo = False
def oleoFalse():
    global oleo
    oleo = False
def trocaOleo():
    global oleo
    if oleo == False:
        oleo = True
    else:
        oleo = False

###############
# REQUEST PAGINAS
###############

def inicio(request):
    oleoFalse()
    return redirect('controle')

def motoristas(request):
    oleoFalse()
    return render(request, "motoristas/index.html")

def pergunta(request):
    oleoFalse()
    return render(request, "veiculos/pergunta.html")

def veiculos(request):
    oleoFalse()
    veiculos = Veiculo.objects.all()
    return render(request, "veiculos/index.html", {'veiculos': veiculos})

###############
# FUNÇÕES VEICULO
###############

def cadastro(request):
    oleoFalse()
    formulario = VeiculoForm(request.POST or None, request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('veiculos')
    return render(request, "veiculos/cadastro.html", {'formulario': formulario})

def visualizar(request, id):
    oleoFalse()
    veiculo= Veiculo.objects.get(id=id)
    visualizacao = True
    formulario = VeiculoForm(instance=veiculo)
    return render(request, "veiculos/visualizar.html", {'formulario': formulario, 'visualizacao': visualizacao})

def editar(request, id):
    oleoFalse()
    veiculo = Veiculo.objects.get(id=id)
    formulario = VeiculoForm(request.POST or None, request.FILES or None, instance=veiculo)
    if formulario.is_valid() and request.POST:
        formulario.save()
        return redirect('veiculos')
    return render(request, "veiculos/editar.html", {'formulario': formulario})

def excluir(request, id):
    oleoFalse()
    veiculo = Veiculo.objects.get(id=id)
    veiculo.delete()
    return redirect('veiculos')

def excluir_motorista(request, id):
    oleoFalse()
    motorista = Motorista.objects.get(id=id)
    motorista.delete()
    return redirect('motoristas')

def excluir_controle(request, id):
    oleoFalse()
    controle = Controle.objects.get(id=id)
    controle.delete()
    return redirect('controle')

###############
# FUNÇÕES MOTORISTA
###############

def motoristas(request):
    oleoFalse()
    motoristas = Motorista.objects.all()
    return render(request, "motoristas/index.html", {'motoristas': motoristas})

def cadastro_motorista(request):
    oleoFalse()
    formulario = MotoristaForm(request.POST or None, request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('motoristas')
    return render(request, "motoristas/cadastro.html", {'formulario': formulario})

def visualizar_motorista(request, id):
    oleoFalse()
    motorista= Motorista.objects.get(id=id)
    visualizacao = True
    formulario = MotoristaForm(instance=motorista)
    return render(request, "motoristas/visualizar.html", {'formulario': formulario, 'visualizacao': visualizacao})
    
def editar_motorista(request, id):
    oleoFalse()
    motorista = Motorista.objects.get(id=id)
    formulario = MotoristaForm(request.POST or None, request.FILES or None, instance=motorista)
    if formulario.is_valid() and request.POST:
        formulario.save()
        return redirect('motoristas')
    return render(request, "motoristas/editar.html", {'formulario': formulario})

###############
# FUNÇÕES CONTROLE
###############

def controles(request):
    busca = request.GET.get('search', '')
    controles = Controle.objects.all().order_by('-data_saida', '-hora_saida')
    if busca:
        controles = Controle.objects.filter(data_saida = busca)
    return render(request, "controle/index.html", {'controles': controles, 'oleo': oleo})

def cadastro_controle(request):
    formulario = ControleForm(request.POST or None)
    if formulario.is_valid():
        formulario.save()
        km_retorno = float(request.POST.get('km_retorno'))
        veiculo_id = request.POST.get('veiculo')
        km = Veiculo.objects.get(id=veiculo_id).km

        if(km_retorno >= km):
            trocaOleo()
        return redirect('controle')
    return render(request, "motoristas/cadastro.html", {'formulario': formulario})

def editar_controle(request, id):
    controle = Controle.objects.get(id=id)
    veiculo = Veiculo.objects.get(id=controle.veiculo.id)
    formulario = ControleForm(request.POST or None, instance=controle)
    if formulario.is_valid() and request.POST:
        formulario.save()
        return redirect('controle')
    return render(request, "controle/editar.html", {'formulario': formulario, 'veiculo': veiculo})

def visualizar_controle(request, id):
    controle= Controle.objects.get(id=id)
    visualizacao = True
    formulario = ControleForm(instance=controle)
    return render(request, "controle/visualizar.html", {'formulario': formulario, 'visualizacao': visualizacao})
    