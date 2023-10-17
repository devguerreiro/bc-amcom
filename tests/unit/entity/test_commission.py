from decimal import Decimal

from paper.core.domain.entity.commission import CommissionLimit
from paper.core.utils.field import Weekday


class TestCommissionLimit:
    @staticmethod
    def test_should_have_attributes():
        assert hasattr(CommissionLimit, "id")
        assert hasattr(CommissionLimit, "weekday")
        assert hasattr(CommissionLimit, "min_commission_percent")
        assert hasattr(CommissionLimit, "max_commission_percent")

    @staticmethod
    def test_should_return_correct_str_conversion():
        product = CommissionLimit(
            weekday=Weekday.MONDAY,
            min_commission_percent=Decimal("3"),
            max_commission_percent=Decimal("5"),
        )
        weekday = Weekday.choices[product.weekday][1]
        assert (
            str(product)
            == f"{weekday} - Mínimo {product.min_commission_percent}% | Máximo {product.max_commission_percent}%"
        )
