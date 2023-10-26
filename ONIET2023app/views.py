from django.shortcuts import render, HttpResponse
from django.db import connection
from django.http import JsonResponse

# Create your views here.
def home(request):
    return render(request,"index.html")

def analisis_view(request):
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
    return JsonResponse(row, safe=False)
