from typing import List

from paper.core.domain.entity.client import Client
from paper.core.domain.repository.client import IClientRepository


class ClientRepository(IClientRepository):
    def get_all(self) -> List[Client]:
        return Client.objects.all()
