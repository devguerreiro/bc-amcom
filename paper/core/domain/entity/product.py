from django.db import models

from paper.core.utils.field import CommissionPercentField, Weekday


class CommissionPercentLimit(models.Model):
    weekday = models.IntegerField(
        choices=Weekday.choices,
        unique=True,
        verbose_name="Dia da semana",
    )
    min_commission_percent = CommissionPercentField(
        verbose_name="Porcentagem mínima da comissão",
    )
    max_commission_percent = CommissionPercentField(
        verbose_name="Porcentagem máxima da comissão",
    )

    class Meta:
        verbose_name = "Limite Porcentagem da Comissão"
        verbose_name_plural = "Limites Porcentagem da Comissão"

    def __str__(self):
        weekday = Weekday.choices[self.weekday][1]
        return f"{weekday} - Mínimo {self.min_commission_percent}% | Máximo {self.max_commission_percent}%"

    def __repr__(self) -> str:
        return str(self)


class Product(models.Model):
    code = models.CharField(
        unique=True,
        max_length=20,
        verbose_name="Código",
    )
    description = models.TextField(
        blank=True,
        null=True,
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
    commission_percent_limits = models.ManyToManyField(
        CommissionPercentLimit,
        verbose_name="Limites Porcentagem da Comissão",
    )

    class Meta:
        verbose_name = "Produto"
        verbose_name_plural = "Produtos"

    def __str__(self):
        return f"{self.code} - {self.description}"

    def __repr__(self) -> str:
        return str(self)
