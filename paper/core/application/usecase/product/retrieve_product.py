from paper.core.domain.entity.product import Product
from paper.core.domain.repository.product import IProductRepository


class RetrieveProduct:
    def __init__(self, repo: IProductRepository):
        self._repo = repo

    def handle(self, pk: int) -> Product:
        return self._repo.get_by_id(pk)
