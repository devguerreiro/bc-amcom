from django.db import models

from dunder_mifflin.core.utils.field import CommissionPercentField


class Product(models.Model):
    code = models.CharField(
        unique=True,
        max_length=20,
        verbose_name="Código",
    )
    description = models.TextField(
        verbose_name="Descrição",
    )
    price = models.DecimalField(
        max_digits=8,
        decimal_places=2,
        verbose_name="Preço",
    )
    commission_percent = CommissionPercentField(
        verbose_name="Porcentagem da comissão",
    )

    class Meta:
        verbose_name = "Produto"
        verbose_name_plural = "Produtos"

    def __str__(self):
        return f"{self.code} - {self.description}"

    def __repr__(self) -> str:
        return str(self)
