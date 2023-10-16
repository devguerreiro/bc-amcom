from decimal import Decimal
from typing import List, Tuple

import pytest
from pytest_mock import MockerFixture

from paper.core.application.usecase.calculate_commission import CalculateCommission
from paper.core.application.usecase.get_commission_percent import GetCommissionPercent


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
        make_product,
        make_sale_item,
        mocker: MockerFixture,
        price: Decimal,
        commission_percent: Decimal,
        quantity: int,
        expected: Decimal,
    ):
        # given
        product = make_product(
            price=price,
            commission_percent=commission_percent,
        )
        sale_item = make_sale_item(product=product, quantity=quantity)

        sale_stub = mocker.stub(name="sale")
        product_repo_stub = mocker.stub(name="product_repo")
        sale_repo_stub = mocker.stub(name="sale_repo")

        sale_repo_stub.get_items = mocker.Mock(return_value=[sale_item])

        mocker.patch.object(
            GetCommissionPercent,
            "handle",
            return_value=commission_percent,
        )

        # when
        output = CalculateCommission(sale_repo_stub, product_repo_stub).handle(sale_stub)

        # assert
        assert output == expected

    @staticmethod
    @pytest.mark.parametrize(
        ["products", "quantity", "expected"],
        [
            (
                [
                    # price             # commission percent
                    (Decimal("750.00"), Decimal("10.00")),
                    (Decimal("120.50"), Decimal("4.50")),
                ],  # products
                5,  # quantity
                Decimal("402.11"),  # expected
            ),
            (
                [
                    (Decimal("750.00"), Decimal("10.00")),
                    (Decimal("120.50"), Decimal("4.50")),
                    (Decimal("10150.79"), Decimal("3.74")),
                    (Decimal("549.90"), Decimal("8.67")),
                    (Decimal("3370.59"), Decimal("2.35")),
                ],
                3,
                Decimal("1760.84"),
            ),
        ],
    )
    def test_should_return_the_total_sale_commission_of_many_products(
        make_product,
        make_sale_item,
        mocker: MockerFixture,
        products: List[Tuple[Decimal, Decimal]],
        quantity: int,
        expected: Decimal,
    ):
        # given
        sale_stub = mocker.stub(name="sale")
        product_repo_stub = mocker.stub(name="product_repo")
        sale_repo_stub = mocker.stub(name="sale_repo")

        sale_items = [
            make_sale_item(
                product=make_product(
                    price=price,
                    commission_percent=commission_percent,
                ),
                quantity=quantity,
            )
            for price, commission_percent in products
        ]

        sale_repo_stub.get_items = mocker.Mock(return_value=sale_items)

        mocker.patch.object(
            GetCommissionPercent,
            "handle",
            side_effect=lambda p: p.commission_percent,
        )

        # when
        output = CalculateCommission(sale_repo_stub, product_repo_stub).handle(sale_stub)

        # assert
        assert output == expected
