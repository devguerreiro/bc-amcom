from abc import ABC, abstractmethod
from typing import List, Tuple

from dunder_mifflin.core.controller.serializers.base import IReadSerializer, IWriteSerializer
from dunder_mifflin.core.domain.entity.sale import Sale, SaleItem


class ISaleReadSerializer(IReadSerializer, ABC):
    @abstractmethod
    def to_json(self, instance: Sale | List[Sale]) -> dict:
        pass


class ISaleWriteSerializer(IWriteSerializer, ABC):
    @abstractmethod
    def validate(self, data: dict) -> Tuple[Sale, List[SaleItem]]:
        pass
