from dunder_mifflin.core.domain.entity.product import Product
from dunder_mifflin.core.domain.entity.sale import Sale, SaleItem


class TestSale:
    @staticmethod
    def test_should_have_attributes():
        assert hasattr(Sale, "id")
        assert hasattr(Sale, "nfe")
        assert hasattr(Sale, "client")
        assert hasattr(Sale, "seller")
        assert hasattr(Sale, "items")
        assert hasattr(Sale, "created_at")

    @staticmethod
    def test_should_return_correct_str_conversion():
        sale = Sale(
            nfe="123ABC",
        )
        assert str(sale) == sale.nfe


class TestSaleItem:
    @staticmethod
    def test_should_have_attributes():
        assert hasattr(SaleItem, "id")
        assert hasattr(SaleItem, "product")
        assert hasattr(SaleItem, "quantity")
        assert hasattr(SaleItem, "created_at")
        assert hasattr(SaleItem, "updated_at")

    @staticmethod
    def test_should_return_correct_str_conversion():
        sale = Sale(nfe="123ABC")
        product = Product(code="ABC")
        sale_item = SaleItem(sale=sale, product=product)
        assert str(sale_item) == f"{sale} - {product}"
