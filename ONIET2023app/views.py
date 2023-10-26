from ONIET2023app.utils import to_json
from django.db import connection
from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.decorators import api_view


# Create your views here.

@api_view(['GET'])
def analisis(request):
    with connection.cursor() as cursor:
        cursor.execute('select Empresa, '
                       'SUM(ProduccionTotal), '
                       '(SUM(ProduccionTotal) - SUM(CantidaPiezasConFallas))                                as piezas_ok,'
                       'SUM(CantidaPiezasConFallas), '
                       '(SUM(ProduccionTotal) - SUM(CantidaPiezasConFallas)) * 100.0 / SUM(ProduccionTotal) as "%piezas_ok", '
                       '(SUM(CantidaPiezasConFallas)) * 100.0 / SUM(ProduccionTotal)                        as "%piezas_error" '
                       'from ONIET2023app_registro '
                       'group by Empresa')
        row = cursor.fetchall()
        print(row)
    return JsonResponse(to_json(
        ["Empresa", "Producción_Total", "Cantidad_Piezas_Ok", "Cantidad_Piezas_Error", "p_Piezas_Ok",
         "p_Piezas_Error"],
        row), safe=False)


def home(request):
    return render(request, "index.html")
