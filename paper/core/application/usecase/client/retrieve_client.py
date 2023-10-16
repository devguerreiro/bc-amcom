from paper.core.domain.entity.client import Client
from paper.core.domain.repository.client import IClientRepository


class RetrieveClient:
    def __init__(self, repo: IClientRepository):
        self._repo = repo

    def handle(self, pk: int) -> Client:
        return self._repo.get_by_id(pk)
