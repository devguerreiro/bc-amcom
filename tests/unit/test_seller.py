from paper.core.domain.entity.seller import Seller


class TestSeller:
    @staticmethod
    def test_should_have_attributes():
        assert hasattr(Seller, "id")
        assert hasattr(Seller, "name")
        assert hasattr(Seller, "email")
        assert hasattr(Seller, "phone")

    @staticmethod
    def test_should_return_correct_str_conversion():
        seller = Seller(email="abc@example.com")
        assert str(seller) == seller.email
