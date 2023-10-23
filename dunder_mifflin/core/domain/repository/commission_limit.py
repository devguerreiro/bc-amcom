from abc import ABC, abstractmethod
from typing import List

from dunder_mifflin.core.domain.entity.commission import CommissionLimit


class ICommissionLimitRepository(ABC):
    @abstractmethod
    def get_all(self) -> List[CommissionLimit]:
        pass
