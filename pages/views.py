from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from . import forms

# Create your views here.
@login_required(login_url='/accounts/login')
def home_page(request):
    return render(request,'login.html')

@login_required(login_url='/accounts/login')
def minhas_plantas(request):
    return render(request,'minhas_plantas.html', {'form': request.user.id})

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

    if request.method=='POST':
        form=forms.NovaPlanta(request.POST,request.FILES)
        if form.is_valid():

            #save plant to db
            instance=form.save(commit=False)
            instance.usuario=request.user
            instance.save()
            return redirect('pages:minhas_plantas')
    else:
        form = forms.NovaPlanta()
    return render(request,'nova_planta.html', {'form': form})

