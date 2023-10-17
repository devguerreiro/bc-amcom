from decimal import Decimal
from random import random

import pytest
from model_bakery import baker

from paper.core.domain.entity.client import Client
from paper.core.domain.entity.commission import CommissionLimit
from paper.core.domain.entity.product import Product
from paper.core.domain.entity.sale import Sale, SaleItem
from paper.core.domain.entity.seller import Seller

baker.generators.add(
    "paper.core.utils.field.CommissionPercentField",
    lambda: round(Decimal(random() * 10), 2),
)


@pytest.fixture()
def make_product():
    def factory(*args, **kwargs) -> Product:
        return baker.prepare(Product, **kwargs)

    return factory


@pytest.fixture()
def make_sale_item():
    def factory(*args, **kwargs) -> Product:
        return baker.prepare(SaleItem, **kwargs)

    return factory


@pytest.fixture()
def make_commission_limit():
    def factory(*args, **kwargs) -> Product:
        return baker.prepare(CommissionLimit, **kwargs)

    return factory


@pytest.fixture()
def make_client():
    def factory(*args, **kwargs) -> Product:
        return baker.prepare(Client, **kwargs)

    return factory


@pytest.fixture()
def make_seller():
    def factory(*args, **kwargs) -> Product:
        return baker.prepare(Seller, **kwargs)

    return factory


@pytest.fixture()
def make_sale():
    def factory(*args, **kwargs) -> Product:
        return baker.prepare(Sale, **kwargs)

    return factory


@pytest.fixture()
def populate_client():
    def factory(*, quantity: int = 1):
        clients = baker.make(Client, _quantity=quantity)
        return clients

    yield factory
    Sale.objects.all().delete()
    Client.objects.all().delete()


@pytest.fixture()
def populate_seller():
    def factory(*, quantity: int = 1):
        sellers = baker.make(Seller, _quantity=quantity)
        return sellers

    yield factory
    Sale.objects.all().delete()
    Seller.objects.all().delete()


@pytest.fixture()
def populate_product():
    def factory(*, quantity: int = 1):
        products = baker.make(Product, _quantity=quantity)
        return products

    yield factory
    Sale.objects.all().delete()
    Product.objects.all().delete()


@pytest.fixture()
def populate_sale():
    def factory(*, quantity: int = 1):
        sale = baker.make(Sale, _quantity=quantity, make_m2m=True)
        return sale

    yield factory
    Sale.objects.all().delete()
    SaleItem.objects.all().delete()
    Product.objects.all().delete()
    Client.objects.all().delete()
    Seller.objects.all().delete()
