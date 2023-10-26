from ONIET2023app.models import Registro
from django.shortcuts import render


def get_registros_por_empresa(empresa):
    registros = Registro.objects.filter(Empresa=empresa)
    print(registros)
    return registros


def get_empresas():
    empresas = Registro.objects.values('Empresa').distinct()
    print(empresas)
    return empresas


def analisis_view(request):
    for empresa in get_empresas():
        get_registros_por_empresa(empresa['Empresa'])

    return render(request, "data.html")
