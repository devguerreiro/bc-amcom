from paper.core.application.usecase.client.create_client import CreateClient
from paper.core.application.usecase.client.delete_client import DeleteClient
from paper.core.application.usecase.seller.list_sellers import ListSellers
from paper.core.application.usecase.seller.retrieve_seller import RetrieveSeller
from paper.core.controller.serializers.seller import ISellerReadSerializer, ISellerWriteSerializer
from paper.core.domain.repository.seller import ISellerRepository


class SellerController:
    def __init__(
        self,
        repo: ISellerRepository,
        read_serializer: ISellerReadSerializer = None,
        write_serializer: ISellerWriteSerializer = None,
    ) -> None:
        self._repo = repo
        self._read_serializer = read_serializer
        self._write_serializer = write_serializer

    def list(self):
        clients = ListSellers(self._repo).handle()
        data = self._read_serializer.to_json(clients)
        return data, 200

    def retrieve(self, pk: int):
        client = RetrieveSeller(self._repo).handle(pk)
        data = self._read_serializer.to_json(client)
        return data, 200

    def delete(self, pk: int):
        DeleteClient(self._repo).handle(pk)
        return None, 204

    def create(self, data: dict):
        valid_client = self._write_serializer.validate(data)
        new_client = CreateClient(self._repo).handle(valid_client)
        data = self._read_serializer.to_json(new_client)
        return data, 201
