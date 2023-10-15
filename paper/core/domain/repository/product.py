from abc import ABC, abstractmethod
from typing import List

from paper.core.domain.entity.product import CommissionPercentLimit, Product


class IProductRepository(ABC):
    @abstractmethod
    def get_commission_percent_limits(self, product: Product) -> List[CommissionPercentLimit]:
        pass
