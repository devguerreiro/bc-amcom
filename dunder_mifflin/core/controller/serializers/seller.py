from abc import ABC, abstractmethod
from typing import List

from dunder_mifflin.core.controller.serializers.base import IReadSerializer, IWriteSerializer
from dunder_mifflin.core.domain.entity.seller import Seller


class ISellerReadSerializer(IReadSerializer, ABC):
    @abstractmethod
    def to_json(self, instance: Seller | List[Seller]) -> dict:
        pass


class ISellerWriteSerializer(IWriteSerializer, ABC):
    @abstractmethod
    def validate(self, data: dict) -> Seller:
        pass
