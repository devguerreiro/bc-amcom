from abc import ABC, abstractmethod
from typing import List

from dunder_mifflin.core.controller.serializers.base import IReadSerializer, IWriteSerializer
from dunder_mifflin.core.domain.entity.client import Client


class IClientReadSerializer(IReadSerializer, ABC):
    @abstractmethod
    def to_json(self, instance: Client | List[Client]) -> dict:
        pass


class IClientWriteSerializer(IWriteSerializer, ABC):
    @abstractmethod
    def validate(self, data: dict) -> Client:
        pass
