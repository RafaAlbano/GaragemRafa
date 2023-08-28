from django.db import models

from uploader.models import Image

from garagem.models import Cor, Categoria, Marca

class Veiculo(models.Model):
    ano = models.IntegerField(blank=True, null=True, default=0)
    preco = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True, default=0)
    cor =models.ForeignKey(
        Cor, on_delete=models.CASCADE
    )
    categoria = models.ForeignKey(
        Categoria, on_delete=models.CASCADE
    )
    marca = models.ForeignKey(
        Marca, on_delete=models.CASCADE
    )

    def __str__(self):
        return f"{self.marca} {self.categoria} {self.ano} {self.cor}" 
    
    capa = models.ForeignKey(
        Image,
        related_name="+",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        default=None,
    )    