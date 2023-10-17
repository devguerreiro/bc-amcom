from abc import ABC, abstractmethod

from paper.core.domain.entity.commission import CommissionLimit


class ICommissionLimitRepository(ABC):
    @abstractmethod
    def get_by_weekday(self, weekday: int) -> CommissionLimit | None:
        pass
