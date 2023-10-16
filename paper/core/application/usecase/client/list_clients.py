from typing import List

from paper.core.domain.entity.client import Client
from paper.core.domain.repository.client import IClientRepository


class ListClients:
    def __init__(self, repo: IClientRepository):
        self._repo = repo

    def handle(self) -> List[Client]:
        return self._repo.get_all()
