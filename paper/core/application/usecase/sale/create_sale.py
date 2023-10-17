from typing import List

from paper.core.domain.entity.sale import Sale, SaleItem
from paper.core.domain.repository.sale import ISaleRepository


class CreateSale:
    def __init__(self, repo: ISaleRepository):
        self._repo = repo

    def handle(self, sale: Sale, items: List[SaleItem]) -> Sale:
        if not items:
            raise ValueError("Não é possível criar uma venda sem item")
        return self._repo.create(sale, items)
