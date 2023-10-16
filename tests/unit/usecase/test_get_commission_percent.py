from decimal import Decimal

import pytest
from pytest_mock import MockerFixture

from paper.core.application.usecase.get_commission_percent import GetCommissionPercent
from paper.core.utils.field import Weekday


class TestGetCommissionPercent:
    @staticmethod
    @pytest.mark.parametrize(
        [
            "commission_percent",
            "min_commission_percent",
            "max_commission_percent",
            "expected",
        ],
        [
            (Decimal("2.00"), Decimal("3.00"), Decimal("5.00"), Decimal("3.00")),
            (Decimal("10.00"), Decimal("3.00"), Decimal("5.00"), Decimal("5.00")),
        ],
    )
    def test_should_return_the_limit_commission_percent_if_today_has_it(
        mocker: MockerFixture,
        make_commission_percent_limit,
        commission_percent: Decimal,
        min_commission_percent: Decimal,
        max_commission_percent: Decimal,
        expected: Decimal,
    ):
        # given
        product_stub = mocker.stub(name="product")
        product_stub.commission_percent = commission_percent

        product_repo_stub = mocker.stub(name="product_repo")
        product_repo_stub.get_commission_percent_limits = mocker.Mock(
            return_value=[
                make_commission_percent_limit(
                    weekday=Weekday.MONDAY,  # limit for monday
                    min_commission_percent=min_commission_percent,
                    max_commission_percent=max_commission_percent,
                )
            ]
        )

        mocked_weekday = mocker.Mock()
        mocked_weekday.weekday = mocker.Mock(return_value=0)  # it is monday

        mocked_datetime = mocker.patch(
            "paper.core.application.usecase.get_commission_percent.datetime",
        )
        mocked_datetime.now = mocker.Mock(return_value=mocked_weekday)

        # when
        output = GetCommissionPercent(product_repo_stub).handle(product_stub)

        # assert
        assert output == expected

    @staticmethod
    def test_should_return_product_commission_percent_if_has_no_limit(
        mocker: MockerFixture,
    ):
        # given
        product_stub = mocker.stub(name="product")
        product_stub.commission_percent = Decimal("10.00")

        product_repo_stub = mocker.stub(name="product_repo")
        product_repo_stub.get_commission_percent_limits = mocker.Mock(return_value=[])

        # when
        output = GetCommissionPercent(product_repo_stub).handle(product_stub)

        # assert
        assert output == product_stub.commission_percent

    @staticmethod
    def test_should_return_product_commission_percent_if_today_has_no_limit(
        mocker: MockerFixture,
        make_commission_percent_limit,
    ):
        # given
        product_stub = mocker.stub(name="product")
        product_stub.commission_percent = Decimal("10.00")

        product_repo_stub = mocker.stub(name="product_repo")
        product_repo_stub.get_commission_percent_limits = mocker.Mock(
            return_value=[
                make_commission_percent_limit(
                    weekday=Weekday.MONDAY,  # limit for monday
                    min_commission_percent=Decimal("3.00"),
                    max_commission_percent=Decimal("5.00"),
                )
            ]
        )

        mocked_weekday = mocker.Mock()
        mocked_weekday.weekday = mocker.Mock(return_value=1)  # it is tuesday

        mocked_datetime = mocker.patch(
            "paper.core.application.usecase.get_commission_percent.datetime",
        )
        mocked_datetime.now = mocker.Mock(return_value=mocked_weekday)

        # when
        output = GetCommissionPercent(product_repo_stub).handle(product_stub)

        # assert
        assert output == product_stub.commission_percent
