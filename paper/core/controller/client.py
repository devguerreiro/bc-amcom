from paper.core.application.usecase.client.create_client import CreateClient
from paper.core.application.usecase.client.delete_client import DeleteClient
from paper.core.application.usecase.client.list_clients import ListClients
from paper.core.application.usecase.client.retrieve_client import RetrieveClient
from paper.core.controller.serializers.client import IClientReadSerializer, IClientWriteSerializer
from paper.core.domain.repository.client import IClientRepository


class ClientController:
    def __init__(
        self,
        repo: IClientRepository,
        read_serializer: IClientReadSerializer = None,
        write_serializer: IClientWriteSerializer = None,
    ) -> None:
        self._repo = repo
        self._read_serializer = read_serializer
        self._write_serializer = write_serializer

    def list(self):
        clients = ListClients(self._repo).handle()
        data = self._read_serializer.to_json(clients)
        return data, 200

    def retrieve(self, pk: int):
        client = RetrieveClient(self._repo).handle(pk)
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
