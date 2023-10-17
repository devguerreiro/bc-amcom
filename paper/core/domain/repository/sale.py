from abc import ABC, abstractmethod
from typing import List

from paper.core.domain.entity.sale import Sale, SaleItem


class ISaleRepository(ABC):
    @abstractmethod
    def get_all(self) -> List[Sale]:
        pass

    @abstractmethod
    def get_by_id(self, pk: int) -> Sale:
        pass

    @abstractmethod
    def delete_by_id(self, pk: int) -> None:
        pass

    @abstractmethod
    def get_items(self, sale: Sale) -> List[SaleItem]:
        pass
