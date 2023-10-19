import pytest

from dunder_mifflin.core.domain.entity.product import Product


@pytest.mark.django_db
class TestProductAPI:
    BASE_URL = "/api/v1/product"

    @staticmethod
    def test_should_list_all_products(client, populate_product):
        # given
        products = populate_product(quantity=3)

        url = TestProductAPI.BASE_URL + "/"

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
    def test_should_retrieve_an_existing_product(client, populate_product):
        # given
        product = populate_product()[0]

        url = f"{TestProductAPI.BASE_URL}/{product.id}/"

        # when
        response = client.get(url)

        # assert
        assert response.status_code == 200

        data = dict(response.data)
        assert data["id"] == product.id

    @staticmethod
    def test_should_delete_an_existing_product(client, populate_product):
        # given
        product = populate_product()[0]

        url = f"{TestProductAPI.BASE_URL}/{product.id}/"

        # when
        response = client.delete(url)

        # assert
        assert response.status_code == 204
        assert response.data is None

        assert Product.objects.count() == 0

    @staticmethod
    def test_should_create_a_new_product(client, make_product):
        # given
        product = make_product()

        url = TestProductAPI.BASE_URL + "/"

        data = {
            "code": product.code,
            "description": product.description,
            "price": product.price,
            "commission_percent": product.commission_percent,
        }

        # when
        response = client.post(url, data)

        # assert
        assert response.status_code == 201

        data = dict(response.data)
        assert data["id"] == 1
        assert data["code"] == product.code
        assert data["description"] == product.description
        assert data["price"] == str(product.price)
        assert data["commission_percent"] == str(product.commission_percent)

        assert Product.objects.count() == 1
