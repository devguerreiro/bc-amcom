from typing import List

from rest_framework import serializers

from paper.core.controller.serializers.sale import ISaleReadSerializer
from paper.core.domain.entity.sale import Sale
from paper.core.infra.serializers.client import ClientReadSerializer
from paper.core.infra.serializers.product import ProductReadSerializer
from paper.core.infra.serializers.seller import SellerReadSerializer


class SaleReadSerializer(ISaleReadSerializer):
    class Serializer(serializers.Serializer):
        class SaleItemReadSerializer(serializers.Serializer):
            id = serializers.IntegerField(read_only=True)
            product = ProductReadSerializer.Serializer(read_only=True)
            quantity = serializers.IntegerField(read_only=True)
            created_at = serializers.DateTimeField(read_only=True)
            updated_at = serializers.DateTimeField(read_only=True)

        id = serializers.IntegerField(read_only=True)
        nfe = serializers.CharField(read_only=True)
        client = ClientReadSerializer.Serializer(read_only=True)
        seller = SellerReadSerializer.Serializer(read_only=True)
        items = SaleItemReadSerializer(many=True, read_only=True)
        created_at = serializers.DateTimeField(read_only=True)

    def to_json(self, instance: Sale | List[Sale]) -> dict:
        many = type(instance) is list
        return self.Serializer(instance, many=many).data
