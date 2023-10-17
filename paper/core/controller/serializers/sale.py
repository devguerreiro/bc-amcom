from abc import ABC, abstractmethod
from typing import List

from paper.core.controller.serializers.base import IReadSerializer
from paper.core.domain.entity.sale import Sale


class ISaleReadSerializer(IReadSerializer, ABC):
    @abstractmethod
    def to_json(self, instance: Sale | List[Sale]) -> dict:
        pass
