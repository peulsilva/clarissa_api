from django.conf.urls import url

from . import views

app_name='pages'

urlpatterns=[
    url(r'^nova_planta/$', views.nova_planta),
    url(r'^minhas_plantas/$', views.minhas_plantas, name='minhas_plantas'),
    url(r'^banco_de_dados/$', views.banco_de_dados),
    url(r'^dados_planta/$', views.dados_planta),
    url(r'^informacoes/$', views.informacoes),
]
