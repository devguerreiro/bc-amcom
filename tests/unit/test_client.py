from paper.core.domain.entity.client import Client


class TestClient:
    @staticmethod
    def test_should_have_attributes():
        assert hasattr(Client, "id")
        assert hasattr(Client, "name")
        assert hasattr(Client, "email")
        assert hasattr(Client, "phone")

    @staticmethod
    def test_should_return_correct_str_conversion():
        client = Client(email="abc@example.com")
        assert str(client) == client.email
