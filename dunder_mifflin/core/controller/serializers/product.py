from abc import ABC, abstractmethod
from typing import List

from dunder_mifflin.core.controller.serializers.base import IReadSerializer, IWriteSerializer
from dunder_mifflin.core.domain.entity.product import Product


class IProductReadSerializer(IReadSerializer, ABC):
    @abstractmethod
    def to_json(self, instance: Product | List[Product]) -> dict:
        pass


class IProductWriteSerializer(IWriteSerializer, ABC):
    @abstractmethod
    def validate(self, data: dict) -> Product:
        pass
