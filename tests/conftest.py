import pytest
from model_bakery import baker

from paper.core.domain.entity.client import Client
from paper.core.domain.entity.product import CommissionPercentLimit, Product
from paper.core.domain.entity.sale import SaleItem


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
def make_commission_percent_limit():
    def factory(*args, **kwargs) -> Product:
        return baker.prepare(CommissionPercentLimit, **kwargs)

    return factory


@pytest.fixture()
def make_client():
    def factory(*args, **kwargs) -> Product:
        return baker.prepare(Client, **kwargs)

    return factory


@pytest.fixture()
def populate_client():
    def factory(*, quantity: int = 1):
        clients = baker.make(Client, _quantity=quantity)
        return clients

    yield factory
    Client.objects.all().delete()
