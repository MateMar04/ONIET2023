from django.db import models

# Create your models here.


class Registro(models.Model):
    Registro = models.IntegerField(primary_key=True)
    Empresa = models.TextField(max_length=15)
    Mes = models.IntegerField()
    ProduccionTotal = models.IntegerField()
    CantidaPiezasConFallas = models.IntegerField()

    def __str__(self):
        return f"{self.Empresa} Mes: {self.Mes}"