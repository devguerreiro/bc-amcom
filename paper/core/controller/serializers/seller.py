from abc import ABC, abstractmethod
from typing import List

from paper.core.controller.serializers.base import IReadSerializer, IWriteSerializer
from paper.core.domain.entity.seller import Seller


class ISellerReadSerializer(IReadSerializer, ABC):
    @abstractmethod
    def to_json(self, instance: Seller | List[Seller]) -> dict:
        pass


class ISellerWriteSerializer(IWriteSerializer, ABC):
    @abstractmethod
    def validate(self, data: dict) -> Seller:
        pass
