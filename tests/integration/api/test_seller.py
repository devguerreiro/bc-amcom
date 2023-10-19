import pytest

from dunder_mifflin.core.domain.entity.seller import Seller


@pytest.mark.django_db
class TestSellerAPI:
    BASE_URL = "/api/v1/seller"

    @staticmethod
    def test_should_list_all_sellers(client, populate_seller):
        # given
        sellers = populate_seller(quantity=3)

        url = TestSellerAPI.BASE_URL + "/"

        # when
        response = client.get(url)

        # assert
        assert response.status_code == 200
        assert len(response.data) == 3

        data = [dict(d) for d in response.data]
        assert data[0]["id"] == sellers[0].id
        assert data[1]["id"] == sellers[1].id
        assert data[2]["id"] == sellers[2].id

    @staticmethod
    def test_should_retrieve_an_existing_seller(client, populate_seller):
        # given
        seller = populate_seller()[0]

        url = f"{TestSellerAPI.BASE_URL}/{seller.id}/"

        # when
        response = client.get(url)

        # assert
        assert response.status_code == 200

        data = dict(response.data)
        assert data["id"] == seller.id

    @staticmethod
    def test_should_delete_an_existing_seller(client, populate_seller):
        # given
        seller = populate_seller()[0]

        url = f"{TestSellerAPI.BASE_URL}/{seller.id}/"

        # when
        response = client.delete(url)

        # assert
        assert response.status_code == 204
        assert response.data is None

        assert Seller.objects.count() == 0

    @staticmethod
    def test_should_create_a_new_seller(client, make_seller):
        # given
        seller = make_seller()

        url = TestSellerAPI.BASE_URL + "/"

        data = {
            "name": seller.name,
            "email": seller.email,
            "phone": seller.phone,
        }

        # when
        response = client.post(url, data)

        # assert
        assert response.status_code == 201

        data = dict(response.data)
        assert data["id"] == 1
        assert data["name"] == seller.name
        assert data["email"] == seller.email
        assert data["phone"] == seller.phone

        assert Seller.objects.count() == 1
