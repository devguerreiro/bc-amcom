from dunder_mifflin.core.domain.entity.product import Product


class TestProduct:
    @staticmethod
    def test_should_have_attributes():
        assert hasattr(Product, "id")
        assert hasattr(Product, "code")
        assert hasattr(Product, "description")
        assert hasattr(Product, "price")
        assert hasattr(Product, "commission_percent")

    @staticmethod
    def test_should_return_correct_str_conversion():
        product = Product(
            code="123ABC",
            description="Desc",
        )
        assert str(product) == f"{product.code} - {product.description}"
