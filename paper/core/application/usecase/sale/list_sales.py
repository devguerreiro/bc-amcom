from typing import List

from paper.core.domain.entity.sale import Sale
from paper.core.domain.repository.sale import ISaleRepository


class ListSales:
    def __init__(self, repo: ISaleRepository):
        self._repo = repo

    def handle(self) -> List[Sale]:
        return self._repo.get_all()
