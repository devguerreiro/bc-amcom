import pytest


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
