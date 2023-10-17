from paper.core.domain.repository.sale import ISaleRepository


class DeleteSale:
    def __init__(self, repo: ISaleRepository):
        self._repo = repo

    def handle(self, pk: int) -> None:
        self._repo.delete_by_id(pk)
