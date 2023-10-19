from dunder_mifflin.core.domain.repository.seller import ISellerRepository


class DeleteSeller:
    def __init__(self, repo: ISellerRepository):
        self._repo = repo

    def handle(self, pk: int) -> None:
        return self._repo.delete_by_id(pk)
