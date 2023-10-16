from paper.core.domain.entity.client import Client
from paper.core.domain.repository.client import IClientRepository


class CreateClient:
    def __init__(self, repo: IClientRepository):
        self._repo = repo

    def handle(self, client: Client) -> Client:
        return self._repo.create(client)
