from abc import ABC, abstractmethod
from typing import List

from paper.core.domain.entity.sale import Sale, SaleItem


class ISaleRepository(ABC):
    @abstractmethod
    def get_items(self, sale: Sale) -> List[SaleItem]:
        pass