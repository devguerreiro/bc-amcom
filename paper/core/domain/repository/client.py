from abc import ABC, abstractmethod
from typing import List

from paper.core.domain.entity.client import Client


class IClientRepository(ABC):
    @abstractmethod
    def get_all(self) -> List[Client]:
        pass

    @abstractmethod
    def get_by_id(self, pk: int) -> Client:
        pass
