from decimal import Decimal

import pytest

from paper.core.application.usecase.calculate_commission import CalculateCommission
from paper.core.domain.entity.product import Product
from paper.core.domain.entity.sale import SaleItem


class TestCalculateCommission:
    @staticmethod
    @pytest.mark.parametrize(
        ["price", "commission_percent", "quantity", "expected"],
        [
            (Decimal("10.00"), Decimal("5.00"), 5, Decimal("2.50")),
            (Decimal("1533.88"), Decimal("1.00"), 3, Decimal("46.02")),
            (Decimal("3280.50"), Decimal("7.56"), 11, Decimal("2728.06")),
            (Decimal("4368.49"), Decimal("3.76"), 7, Decimal("1149.79")),
        ],
    )
    def test_should_return_the_total_sale_commission_of_one_product(
        mocker,
        price,
        commission_percent,
        quantity,
        expected,
    ):
        # given
        product = Product(
            price=price,
            commission_percent=commission_percent,
        )

        sale_stub = mocker.stub(name="sale")

        repo_stub = mocker.stub(name="repo")
        repo_stub.get_items = mocker.MagicMock(
            return_value=[
                SaleItem(product=product, quantity=quantity),
            ]
        )

        # when
        output = CalculateCommission(repo_stub).handle(sale_stub)

        # assert
        assert output == expected

    @staticmethod
    @pytest.mark.parametrize(
        ["products", "quantity", "expected"],
        [
            (
                [
                    Product(price=Decimal("750.00"), commission_percent=Decimal("10.00")),
                    Product(price=Decimal("120.50"), commission_percent=Decimal("4.50")),
                ],
                5,
                Decimal("402.11"),
            ),
            (
                [
                    Product(price=Decimal("750.00"), commission_percent=Decimal("10.00")),
                    Product(price=Decimal("120.50"), commission_percent=Decimal("4.50")),
                    Product(price=Decimal("10150.79"), commission_percent=Decimal("3.74")),
                    Product(price=Decimal("549.90"), commission_percent=Decimal("8.67")),
                    Product(price=Decimal("3370.59"), commission_percent=Decimal("2.35")),
                ],
                3,
                Decimal("1760.84"),
            ),
        ],
    )
    def test_should_return_the_total_sale_commission_of_many_products(
        mocker,
        products,
        quantity,
        expected,
    ):
        # given
        sale_stub = mocker.stub(name="sale")

        repo_stub = mocker.stub(name="repo")
        repo_stub.get_items = mocker.MagicMock(
            return_value=[SaleItem(product=product, quantity=quantity) for product in products]
        )

        # when
        output = CalculateCommission(repo_stub).handle(sale_stub)

        # assert
        assert output == expected
