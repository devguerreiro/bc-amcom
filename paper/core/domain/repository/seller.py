from abc import ABC, abstractmethod
from typing import List

from paper.core.domain.entity.seller import Seller


class ISellerRepository(ABC):
    @abstractmethod
    def get_all(self) -> List[Seller]:
        pass

    @abstractmethod
    def get_by_id(self, pk: int) -> Seller:
        pass

    @abstractmethod
    def delete_by_id(self, pk: int) -> None:
        pass

    @abstractmethod
    def create(self, eller: Seller) -> Seller:
        pass
