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

    @abstractmethod
    def delete_by_id(self, pk: int) -> None:
        pass

    @abstractmethod
    def create(self, client: Client) -> Client:
        pass
