from typing import List

from dunder_mifflin.core.domain.entity.product import Product
from dunder_mifflin.core.domain.repository.product import IProductRepository


class ListProducts:
    def __init__(self, repo: IProductRepository):
        self._repo = repo

    def handle(self) -> List[Product]:
        return self._repo.get_all()
