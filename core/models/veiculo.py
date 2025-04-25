from django.db import models

from core.models import Modelo, Cor, Acessorio

class Veiculo(models.Model):
    ano = models.IntegerField(blank=True, null=True, default=0)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    modelo = models.ForeignKey(Modelo, on_delete=models.PROTECT, related_name="veiculo")
    cor = models.ForeignKey(Cor, on_delete=models.PROTECT, related_name="veiculo")
    acessorios = models.ManyToManyField(Acessorio, related_name="veiculo")

    def __str__(self):
        return f"{self.id} - {self.modelo.marca} {self.modelo.nome} {self.cor.nome} {self.ano}"