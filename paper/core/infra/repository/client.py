from typing import List

from paper.core.domain.entity.client import Client
from paper.core.domain.repository.client import IClientRepository


class ClientRepository(IClientRepository):
    def get_all(self) -> List[Client]:
        return list(Client.objects.all())

    def get_by_id(self, pk: int) -> Client:
        return Client.objects.get(pk=pk)