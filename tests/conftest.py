from decimal import Decimal

import pytest
from model_bakery import baker

from paper.core.domain.entity.client import Client
from paper.core.domain.entity.product import CommissionPercentLimit, Product
from paper.core.domain.entity.sale import SaleItem


@pytest.fixture()
def make_product():
    def factory(price: Decimal, commission_percent: Decimal) -> Product:
        return Product(price=price, commission_percent=commission_percent)

    return factory


@pytest.fixture()
def make_sale_item():
    def factory(product: Product, quantity: int) -> SaleItem:
        return SaleItem(product=product, quantity=quantity)

    return factory


@pytest.fixture()
def make_commission_percent_limit():
    def factory(
        weekday: int,
        min_commission_percent: Decimal,
        max_commission_percent: Decimal,
    ) -> CommissionPercentLimit:
        return CommissionPercentLimit(
            weekday=weekday,
            min_commission_percent=min_commission_percent,
            max_commission_percent=max_commission_percent,
        )

    return factory


@pytest.fixture()
def populate_client():
    def factory(*, quantity: int):
        clients = baker.make(Client, _quantity=quantity)
        return clients

    yield factory
    Client.objects.all().delete()
