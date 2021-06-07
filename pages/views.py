from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='/accounts/login')
def home_page(request):
    return render(request,'login.html')

@login_required(login_url='/accounts/login')
def minhas_plantas(request):
    return render(request,'minhas_plantas.html')

@login_required(login_url='/accounts/login')
def banco_de_dados(request):
    return render(request,'banco_de_dados.html')

@login_required(login_url='/accounts/login')
def dados_planta(request):
    return render(request,'dados_planta.html')

@login_required(login_url='/accounts/login')
def informacoes(request):
    return render(request,'informacoes.html')

@login_required(login_url='/accounts/login')
def nova_planta(request):
    return render(request,'nova_planta.html')

