from abc import ABC, abstractmethod
from typing import List

from paper.core.domain.entity.client import Client


class IClientSerializer(ABC):
    def __init__(self, data: Client | List[Client]) -> None:
        self.data = data

    @abstractmethod
    def to_json(self):
        pass
