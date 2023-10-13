from decimal import Decimal

from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


class Product(models.Model):
    code: str = models.CharField(
        unique=True,
        max_length=20,
        verbose_name="Código",
    )
    description: str = models.TextField(
        blank=True,
        null=True,
        verbose_name="Descrição",
    )
    price: Decimal = models.DecimalField(
        max_digits=8,
        decimal_places=2,
        verbose_name="Preço",
    )
    commission_percent: Decimal = models.DecimalField(
        max_digits=4,
        decimal_places=2,
        validators=[
            MinValueValidator(Decimal("0.00")),
            MaxValueValidator(Decimal("10.00")),
        ],
        verbose_name="Porcentagem de Comissão",
    )

    class Meta:
        verbose_name = "Produto"
        verbose_name_plural = "Produtos"

    def __str__(self):
        return f"{self.code} - {self.description}"

    def __repr__(self) -> str:
        return str(self)
