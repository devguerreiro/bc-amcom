import pytest

from paper.core.domain.entity.client import Client


@pytest.mark.django_db
class TestClientController:
    @staticmethod
    def test_should_list_all_clients(client, populate_client):
        # given
        clients = populate_client(quantity=3)

        url = "/api/v1/client/"

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
        _client = populate_client(quantity=1)[0]

        url = f"/api/v1/client/{_client.id}/"

        # when
        response = client.get(url)

        # assert
        assert response.status_code == 200

        data = dict(response.data)
        assert data["id"] == _client.id

    @staticmethod
    def test_should_delete_an_existing_client(client, populate_client):
        # given
        _client = populate_client(quantity=1)[0]

        url = f"/api/v1/client/{_client.id}/"

        # when
        response = client.delete(url)

        # assert
        assert response.status_code == 204
        assert response.data is None

        assert Client.objects.count() == 0
