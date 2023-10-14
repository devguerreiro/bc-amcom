from paper.core.domain.entity.product import CommissionPercentLimit, Product
from paper.core.utils.field import Weekday


class TestProduct:
    @staticmethod
    def test_should_have_attributes():
        assert hasattr(Product, "id")
        assert hasattr(Product, "code")
        assert hasattr(Product, "description")
        assert hasattr(Product, "price")
        assert hasattr(Product, "commission_percent")
        assert hasattr(Product, "commission_percent_limits")

    @staticmethod
    def test_should_return_correct_str_conversion():
        product = Product(
            code="123ABC",
            description="Desc",
        )
        assert str(product) == f"{product.code} - {product.description}"


class TestCommissionPercentLimit:
    @staticmethod
    def test_should_have_attributes():
        assert hasattr(CommissionPercentLimit, "id")
        assert hasattr(CommissionPercentLimit, "weekday")
        assert hasattr(CommissionPercentLimit, "min_commission_percent")
        assert hasattr(CommissionPercentLimit, "max_commission_percent")

    @staticmethod
    def test_should_return_correct_str_conversion():
        product = CommissionPercentLimit(
            weekday=Weekday.MONDAY,
            min_commission_percent="3%",
            max_commission_percent="5%",
        )
        weekday = Weekday.choices[product.weekday][1]
        assert (
            str(product)
            == f"{weekday} - Mínimo {product.min_commission_percent}% | Máximo {product.max_commission_percent}%"
        )
