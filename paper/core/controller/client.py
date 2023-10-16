from paper.core.application.usecase.list_clients import ListClients
from paper.core.application.usecase.retrieve_client import RetrieveClient
from paper.core.domain.repository.client import IClientRepository
from paper.core.domain.serializer.client import IClientSerializer


class ClientController:
    def __init__(
        self,
        client_repo: IClientRepository,
        client_serializer: IClientSerializer,
    ) -> None:
        self._client_repo = client_repo
        self._client_serializer = client_serializer

    def list(self):
        clients = ListClients(self._client_repo).handle()
        data = self._client_serializer(clients).to_json()
        return data, 200

    def retrieve(self, pk: int):
        client = RetrieveClient(self._client_repo).handle(pk)
        data = self._client_serializer(client).to_json()
        return data, 200