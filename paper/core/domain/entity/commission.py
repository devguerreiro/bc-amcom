from django.db import models

from paper.core.utils.field import CommissionPercentField, Weekday


class CommissionLimit(models.Model):
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
