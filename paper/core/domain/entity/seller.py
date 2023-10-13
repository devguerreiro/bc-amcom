from django.db import models


class Seller(models.Model):
    name: str = models.CharField(
        max_length=60,
        verbose_name="Nome do vendedor",
    )
    email: str = models.EmailField(
        max_length=50,
        unique=True,
        verbose_name="E-mail do vendedor",
    )
    phone: str = models.CharField(
        max_length=20,
        unique=True,
        verbose_name="Contato do vendedor",
    )

    class Meta:
        verbose_name = "Vendedor"
        verbose_name_plural = "Vendedores"

    def __str__(self):
        return self.email

    def __repr__(self) -> str:
        return str(self)
