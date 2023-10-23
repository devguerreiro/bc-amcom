from abc import ABC, abstractmethod
from typing import List

from dunder_mifflin.core.domain.entity.product import Product


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
    def get_by_params(self, query_params: dict) -> List[Product]:
        pass
