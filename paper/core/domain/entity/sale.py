from django.core.validators import MinValueValidator
from django.db import models

from paper.core.domain.entity.client import Client
from paper.core.domain.entity.product import Product
from paper.core.domain.entity.seller import Seller


class SaleItem(models.Model):
    sale = models.ForeignKey(
        "Sale",
        on_delete=models.CASCADE,
        verbose_name="Venda",
    )
    product = models.ForeignKey(
        Product,
        on_delete=models.PROTECT,
        verbose_name="Produto",
    )
    quantity = models.IntegerField(
        validators=[MinValueValidator(1)],
        verbose_name="Quantidade",
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Data/hora da venda",
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name="Data/hora da alteração",
    )

    class Meta:
        verbose_name = "Item"
        verbose_name_plural = "Itens"

    def __str__(self):
        return f"{self.sale} - {self.product}"

    def __repr__(self) -> str:
        return str(self)


class Sale(models.Model):
    nfe = models.CharField(
        max_length=50,
        unique=True,
        verbose_name="Código NFE",
    )
    client = models.ForeignKey(
        Client,
        on_delete=models.PROTECT,
        related_name="purchases",
        verbose_name="Cliente",
    )
    seller = models.ForeignKey(
        Seller,
        on_delete=models.PROTECT,
        related_name="sales",
        verbose_name="Vendedor",
    )
    items = models.ManyToManyField(
        Product,
        through=SaleItem,
        verbose_name="Itens",
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Data/Hora da venda",
    )

    class Meta:
        verbose_name = "Venda"
        verbose_name_plural = "Vendas"

    def __str__(self):
        return self.nfe

    def __repr__(self) -> str:
        return str(self)
