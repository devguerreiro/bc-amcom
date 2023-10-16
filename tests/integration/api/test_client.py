import pytest

from paper.core.domain.entity.client import Client


@pytest.mark.django_db
class TestClientAPI:
    BASE_URL = "/api/v1/client"

    @staticmethod
    def test_should_list_all_clients(client, populate_client):
        # given
        clients = populate_client(quantity=3)

        url = TestClientAPI.BASE_URL + "/"

        # when
        response = client.get(url)

        # assert
        assert response.status_code == 200
        assert len(response.data) == 3

        data = [dict(d) for d in response.data]
        assert data[0]["id"] == clients[0].id
        assert data[1]["id"] == clients[1].id
        assert data[2]["id"] == clients[2].id

    @staticmethod
    def test_should_retrieve_an_existing_client(client, populate_client):
        # given
        _client = populate_client()[0]

        url = f"{TestClientAPI.BASE_URL}/{_client.id}/"

        # when
        response = client.get(url)

        # assert
        assert response.status_code == 200

        data = dict(response.data)
        assert data["id"] == _client.id

    @staticmethod
    def test_should_delete_an_existing_client(client, populate_client):
        # given
        _client = populate_client()[0]

        url = f"{TestClientAPI.BASE_URL}/{_client.id}/"

        # when
        response = client.delete(url)

        # assert
        assert response.status_code == 204
        assert response.data is None

        assert Client.objects.count() == 0

    @staticmethod
    def test_should_create_a_new_client(client, make_client):
        # given
        _client = make_client()

        url = TestClientAPI.BASE_URL + "/"

        data = {
            "name": _client.name,
            "email": _client.email,
            "phone": _client.phone,
        }

        # when
        response = client.post(url, data)

        # assert
        assert response.status_code == 201

        data = dict(response.data)
        assert data["id"] == 1
        assert data["name"] == _client.name
        assert data["email"] == _client.email
        assert data["phone"] == _client.phone

        assert Client.objects.count() == 1
