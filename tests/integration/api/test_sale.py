import pytest

from paper.core.domain.entity.sale import Sale


@pytest.mark.django_db
class TestSaleAPI:
    BASE_URL = "/api/v1/sale"

    @staticmethod
    def test_should_list_all_sale(client, populate_sale):
        # given
        products = populate_sale(quantity=3)

        url = TestSaleAPI.BASE_URL + "/"

        # when
        response = client.get(url)

        # assert
        assert response.status_code == 200
        assert len(response.data) == 3

        data = [dict(d) for d in response.data]
        assert data[0]["id"] == products[0].id
        assert data[1]["id"] == products[1].id
        assert data[2]["id"] == products[2].id

    @staticmethod
    def test_should_retrieve_an_existing_sale(client, populate_sale):
        # given
        sale = populate_sale()[0]

        url = f"{TestSaleAPI.BASE_URL}/{sale.id}/"

        # when
        response = client.get(url)

        # assert
        assert response.status_code == 200

        data = dict(response.data)
        assert data["id"] == sale.id

    @staticmethod
    def test_should_delete_an_existing_sale(client, populate_sale):
        # given
        sale = populate_sale()[0]

        url = f"{TestSaleAPI.BASE_URL}/{sale.id}/"

        # when
        response = client.delete(url)

        # assert
        assert response.status_code == 204
        assert response.data is None

        assert Sale.objects.count() == 0

    # @staticmethod
    # def test_should_create_a_new_client(client, make_client):
    #     # given
    #     _client = make_client()

    #     url = TestSaleAPI.BASE_URL + "/"

    #     data = {
    #         "name": _client.name,
    #         "email": _client.email,
    #         "phone": _client.phone,
    #     }

    #     # when
    #     response = client.post(url, data)

    #     # assert
    #     assert response.status_code == 201

    #     data = dict(response.data)
    #     assert data["id"] == 1
    #     assert data["name"] == _client.name
    #     assert data["email"] == _client.email
    #     assert data["phone"] == _client.phone

    #     assert Client.objects.count() == 1
