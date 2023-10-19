from django.db import models


class Client(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name="Nome do cliente",
    )
    email = models.EmailField(
        max_length=50,
        unique=True,
        verbose_name="E-mail do cliente",
    )
    phone = models.CharField(
        max_length=20,
        unique=True,
        verbose_name="Contato do cliente",
    )

    class Meta:
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"

    def __str__(self):
        return self.email

    def __repr__(self) -> str:
        return str(self)
