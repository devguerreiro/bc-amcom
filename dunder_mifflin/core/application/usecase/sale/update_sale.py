from typing import List

from dunder_mifflin.core.domain.entity.sale import Sale, SaleItem
from dunder_mifflin.core.domain.repository.sale import ISaleRepository


class UpdateSale:
    def __init__(self, repo: ISaleRepository):
        self._repo = repo

    def handle(self, sale: Sale, new: Sale, items: List[SaleItem]) -> Sale:
        if not items:
            raise ValueError("Não é possível alterar uma venda sem item")
        return self._repo.update(sale, new, items)
