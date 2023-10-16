from paper.core.domain.repository.product import IProductRepository


class DeleteProduct:
    def __init__(self, repo: IProductRepository):
        self._repo = repo

    def handle(self, pk: int) -> None:
        return self._repo.delete_by_id(pk)
