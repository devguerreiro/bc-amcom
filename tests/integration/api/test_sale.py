import pytest

from dunder_mifflin.core.domain.entity.sale import Sale, SaleItem


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

    @staticmethod
    def test_should_create_a_new_sale(
        client,
        make_sale,
        populate_client,
        populate_seller,
        populate_product,
    ):
        # given
        sale = make_sale()

        _client = populate_client()[0]
        seller = populate_seller()[0]
        product = populate_product()[0]

        url = TestSaleAPI.BASE_URL + "/"

        data = {
            "nfe": sale.nfe,
            "client": _client.id,
            "seller": seller.id,
            "items": [
                {
                    "product": product.id,
                    "quantity": 1,
                },
            ],
        }

        # when
        response = client.post(url, data, content_type="application/json")

        # assert
        assert response.status_code == 201

        data = dict(response.data)
        assert data["id"] == 1
        assert data["nfe"] == sale.nfe
        assert data["client"]["id"] == _client.id
        assert data["seller"]["id"] == seller.id
        assert data["items"][0]["product"]["id"] == product.id

        assert Sale.objects.count() == 1
        assert SaleItem.objects.count() == 1

    @staticmethod
    def test_should_not_be_able_to_create_a_new_sale_without_an_item(
        client,
        make_sale,
        populate_client,
        populate_seller,
    ):
        # given
        sale = make_sale()

        _client = populate_client()[0]
        seller = populate_seller()[0]

        url = TestSaleAPI.BASE_URL + "/"

        data = {
            "nfe": sale.nfe,
            "client": _client.id,
            "seller": seller.id,
            "items": [],
        }

        # when
        response = client.post(url, data, content_type="application/json")

        # assert
        assert response.status_code == 400

        assert response.data == {
            "error": "Não é possível criar uma venda sem item",
        }

        assert Sale.objects.count() == 0
        assert SaleItem.objects.count() == 0
