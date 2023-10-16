from paper.core.domain.repository.client import IClientRepository


class DeleteClient:
    def __init__(self, client_repo: IClientRepository):
        self._client_repo = client_repo

    def handle(self, pk: int) -> None:
        return self._client_repo.delete_by_id(pk)
