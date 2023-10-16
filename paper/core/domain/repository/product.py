from abc import ABC, abstractmethod
from typing import List

from paper.core.domain.entity.product import CommissionPercentLimit, Product


class IProductRepository(ABC):
    @abstractmethod
    def get_all(self) -> List[Product]:
        pass

    @abstractmethod
    def get_by_id(self, pk: int) -> Product:
        pass

    @abstractmethod
    def delete_by_id(self, pk: int) -> None:
        pass

    @abstractmethod
    def create(self, product: Product) -> Product:
        pass

    @abstractmethod
    def get_commission_percent_limits(self, product: Product) -> List[CommissionPercentLimit]:
        pass
