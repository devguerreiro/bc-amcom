from typing import List

from dunder_mifflin.core.domain.entity.product import Product
from dunder_mifflin.core.domain.repository.product import IProductRepository


class ListProductsByParams:
    def __init__(self, repo: IProductRepository):
        self._repo = repo

    def handle(self, query_params: dict) -> List[Product]:
        return self._repo.get_by_params(query_params)
