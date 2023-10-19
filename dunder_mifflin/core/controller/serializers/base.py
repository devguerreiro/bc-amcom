from abc import ABC, abstractmethod
from typing import List

from django.db.models import Model


class IReadSerializer(ABC):
    @abstractmethod
    def to_json(self, instance: Model | List[Model]) -> dict:
        pass


class IWriteSerializer(ABC):
    @abstractmethod
    def validate(self, data: dict) -> Model:
        pass
