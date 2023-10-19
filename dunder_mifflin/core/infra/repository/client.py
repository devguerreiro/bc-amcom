from typing import List

from dunder_mifflin.core.domain.entity.client import Client
from dunder_mifflin.core.domain.repository.client import IClientRepository


class ClientRepository(IClientRepository):
    def get_all(self) -> List[Client]:
        return list(Client.objects.all())

    def get_by_id(self, pk: int) -> Client:
        return Client.objects.get(pk=pk)

    def delete_by_id(self, pk: int) -> None:
        Client.objects.filter(id=pk).delete()

    def create(self, client: Client) -> Client:
        client.save(force_insert=True)
        return client
