from typing import List

from paper.core.domain.entity.client import Client
from paper.core.domain.repository.client import IClientRepository


class ListClients:
    def __init__(self, client_repo: IClientRepository):
        self._client_repo = client_repo

    def handle(self) -> List[Client]:
        return self._client_repo.get_all()
