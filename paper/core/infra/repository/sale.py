from typing import List

from paper.core.domain.entity.sale import Sale, SaleItem
from paper.core.domain.repository.sale import ISaleRepository


class SaleRepository(ISaleRepository):
    def get_all(self) -> List[Sale]:
        return list(Sale.objects.all())

    def get_by_id(self, pk: int) -> Sale:
        return Sale.objects.get(pk=pk)

    def get_items(self, sale: Sale) -> List[SaleItem]:
        pass
