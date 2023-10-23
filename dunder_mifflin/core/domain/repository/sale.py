from abc import ABC, abstractmethod
from datetime import date
from typing import List

from dunder_mifflin.core.domain.entity.sale import Sale, SaleItem


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
    def create(self, sale: Sale, items: List[SaleItem]) -> Sale:
        pass

    @abstractmethod
    def update(self, sale: Sale, new: Sale, items: List[SaleItem]) -> Sale:
        pass

    @abstractmethod
    def get_commissions(self, start_date: date, end_date: date) -> List[Sale]:
        pass
