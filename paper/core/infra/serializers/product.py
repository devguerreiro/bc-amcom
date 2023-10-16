from typing import List

from rest_framework import serializers

from paper.core.controller.serializers.product import IProductReadSerializer
from paper.core.domain.entity.product import Product


class ProductReadSerializer(IProductReadSerializer):
    class Serializer(serializers.Serializer):
        id = serializers.IntegerField(read_only=True)
        code = serializers.CharField(read_only=True)
        description = serializers.CharField(read_only=True)
        price = serializers.CharField(read_only=True)
        commission_percent = serializers.CharField(read_only=True)

    def to_json(self, instance: Product | List[Product]) -> dict:
        many = type(instance) is list
        return self.Serializer(instance, many=many).data
