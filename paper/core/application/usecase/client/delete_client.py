from paper.core.domain.repository.client import IClientRepository


class DeleteClient:
    def __init__(self, repo: IClientRepository):
        self._repo = repo

    def handle(self, pk: int) -> None:
        return self._repo.delete_by_id(pk)
