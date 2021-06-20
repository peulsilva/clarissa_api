from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from demo.models import Planta,BD
from . import forms
from datetime import date

# Create your views here.


@login_required(login_url='/accounts/login')
def home_page(request):
    return render(request,'login.html')

@login_required(login_url='/accounts/login')
def minhas_plantas(request):
    minhas_plantas=Planta.objects.all().filter(usuario=request.user)
    return render(request,'minhas_plantas.html', {'plantas':minhas_plantas ,'user':request.user})

@login_required(login_url='/accounts/login')
def banco_de_dados(request):
    bd=BD.objects.all()
    return render(request,'banco_de_dados.html', {'bd': bd})

@login_required(login_url='/accounts/login')
def dados_planta(request):
    global name
    name=request.COOKIES.get('data')
    planta=Planta.objects.all().filter(name=request.COOKIES.get('data'))

    species=''
    for plant in planta:
        species=plant.species
    bd=BD.objects.all().filter(nome_comum=species)

    if len(planta)!=0:
        plant=Planta.objects.get(name=name)
        if request.method == 'POST':
            form = forms.RegarPlanta(request.POST, instance=plant)
            if form.is_valid():
                form.save()

            else:
                return render(request, 'nova_planta.html', {'message': 'Dados inválidos'})
        else:
            form = forms.RegarPlanta()

        return render(request,'dados_planta.html', {'planta': planta, 'form':form, 'bd': bd})
    else:
        return render(request, 'dados_planta.html')

@login_required(login_url='/accounts/login')
def informacoes(request):

    return render(request,'informacoes.html')

@login_required(login_url='/accounts/login')
def apagar(request):
    minhas_planta=Planta.objects.filter(usuario=request.user).delete()

    return render(request,'apagar.html', {'planta': minhas_planta})

@login_required(login_url='/accounts/login')
def deletar(request):
    planta_deletada=Planta.objects.all().filter(name=name).delete()
    return render(request,'deletar.html', {'deletada': planta_deletada})

@login_required(login_url='/accounts/login')
def nova_planta(request):
    bd = BD.objects.all()
    if request.method=='POST':
        form=forms.NovaPlanta(request.POST,request.FILES)
        if form.is_valid():

            #save plant to db
            instance=form.save(commit=False)
            instance.usuario=request.user
            instance.save()
            return redirect('pages:minhas_plantas')
        else:
            return render(request,'nova_planta.html', {'message': 'Dados inválidos'})
    else:
        form = forms.NovaPlanta()
    return render(request,'nova_planta.html', {'form': form ,'bd': bd})

