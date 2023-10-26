from ONIET2023app.models import Registro
from django.db import connection
from django.http import JsonResponse


def get_registros_por_empresa(empresa):
    registros = Registro.objects.filter(Empresa=empresa)

    return registros


def get_empresas():
    empresas = Registro.objects.values('Empresa').distinct()
    print(empresas)
    return empresas


def analisis_view(request):
    with connection.cursor() as cursor:
        cursor.execute('select Empresa, '
                       '(SUM(ProduccionTotal) - SUM(CantidaPiezasConFallas))                                as piezas_ok, '
                       '(SUM(ProduccionTotal) - SUM(CantidaPiezasConFallas)) * 100.0 / SUM(ProduccionTotal) as "%piezas_ok", '
                       '(SUM(CantidaPiezasConFallas)) * 100.0 / SUM(ProduccionTotal) as "%piezas_error" '
                       'from ONIET2023app_registro '
                       'group by Empresa')
        row = cursor.fetchall()
        print(row)
    return JsonResponse(row, safe=False)
