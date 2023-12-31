from dunder_mifflin.core.domain.entity.product import Product
from dunder_mifflin.core.domain.repository.product import IProductRepository


class CreateProduct:
    def __init__(self, repo: IProductRepository):
        self._repo = repo

    def handle(self, product: Product) -> Product:
        return self._repo.create(product)
