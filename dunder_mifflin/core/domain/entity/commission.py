from django.core.exceptions import ValidationError
from django.db import models

from dunder_mifflin.core.utils.field import CommissionPercentField, Weekday


class CommissionLimit(models.Model):
    weekday = models.IntegerField(
        choices=Weekday.choices,
        unique=True,
        verbose_name="Dia da Semana",
    )
    min_commission_percent = CommissionPercentField(
        verbose_name="Porcentagem Mínima",
        help_text="Deve ser um valor entre 0 e 10",
    )
    max_commission_percent = CommissionPercentField(
        verbose_name="Porcentagem Máxima",
        help_text="Deve ser um valor entre 0 e 10",
    )

    class Meta:
        verbose_name = "Limite da Comissão"
        verbose_name_plural = "Limites da Comissão"

    def __str__(self):
        weekday = Weekday.choices[self.weekday][1]
        return f"{weekday} - Mínimo {self.min_commission_percent}% | Máximo {self.max_commission_percent}%"

    def __repr__(self) -> str:
        return str(self)

    def clean(self):
        if self.max_commission_percent <= self.min_commission_percent:
            raise ValidationError("Porcentagem Máxima deve ser maior que Porcentagem Mínima")
