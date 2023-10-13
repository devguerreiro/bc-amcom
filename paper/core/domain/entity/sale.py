from datetime import datetime
from typing import List

from django.core.validators import MinValueValidator
from django.db import models

from paper.core.domain.entity.client import Client
from paper.core.domain.entity.product import Product
from paper.core.domain.entity.seller import Seller


class SaleItem(models.Model):
    sale: "Sale" = models.ForeignKey(
        "Sale",
        on_delete=models.CASCADE,
        verbose_name="Venda",
    )
    product: Product = models.ForeignKey(
        Product,
        on_delete=models.PROTECT,
        verbose_name="Produto",
    )
    quantity: int = models.IntegerField(
        validators=[MinValueValidator(1)],
        verbose_name="Quantidade",
    )
    created_at: datetime = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Data/hora da venda",
    )
    updated_at: datetime = models.DateTimeField(
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
    nfe: str = models.CharField(
        max_length=50,
        unique=True,
        verbose_name="Código NFE",
    )
    client: Seller = models.ForeignKey(
        Seller,
        on_delete=models.PROTECT,
        related_name="purchases",
        verbose_name="Cliente",
    )
    seller: Client = models.ForeignKey(
        Client,
        on_delete=models.PROTECT,
        related_name="sales",
        verbose_name="Vendedor",
    )
    items: List[Product] = models.ManyToManyField(
        Product, through=SaleItem, verbose_name="Itens"
    )
    created_at: datetime = models.DateTimeField(
        auto_now_add=True, verbose_name="Data/Hora da venda"
    )

    class Meta:
        verbose_name = "Venda"
        verbose_name_plural = "Vendas"

    def __str__(self):
        return self.nfe

    def __repr__(self) -> str:
        return str(self)
