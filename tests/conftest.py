from decimal import Decimal

import pytest

from paper.core.domain.entity.product import Product
from paper.core.domain.entity.sale import SaleItem


@pytest.fixture(scope="class")
def make_product() -> Product:
    def factory(price: Decimal, commission_percent: Decimal):
        return Product(price=price, commission_percent=commission_percent)

    return factory


@pytest.fixture(scope="class")
def make_sale_item() -> SaleItem:
    def factory(product: Product, quantity: int):
        return SaleItem(product=product, quantity=quantity)

    return factory
