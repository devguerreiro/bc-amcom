from typing import List

from paper.core.domain.entity.sale import Sale, SaleItem
from paper.core.domain.repository.sale import ISaleRepository


class CreateSale:
    def __init__(self, repo: ISaleRepository):
        self._repo = repo

    def handle(self, sale: Sale, items: List[SaleItem]) -> Sale:
        return self._repo.create(sale, items)
