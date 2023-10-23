from typing import List, Tuple

from rest_framework import serializers

from dunder_mifflin.core.controller.serializers.sale import ISaleReadSerializer, ISaleWriteSerializer
from dunder_mifflin.core.domain.entity.sale import Sale, SaleItem
from dunder_mifflin.core.infra.serializers.client import ClientReadSerializer
from dunder_mifflin.core.infra.serializers.product import ProductReadSerializer
from dunder_mifflin.core.infra.serializers.seller import SellerReadSerializer


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


class SaleWriteSerializer(ISaleWriteSerializer):
    class Serializer(serializers.ModelSerializer):
        class SaleItemWriteSerializer(serializers.ModelSerializer):
            class Meta:
                model = SaleItem
                fields = ["product", "quantity"]

        items = SaleItemWriteSerializer(many=True)

        class Meta:
            model = Sale
            fields = ["client", "seller", "items"]

    def validate(self, data: dict) -> Tuple[Sale, List[SaleItem]]:
        serializer = self.Serializer(data=data)
        is_valid = serializer.is_valid(raise_exception=True)
        if is_valid:
            items = serializer.validated_data.pop("items", [])
            return (
                Sale(**serializer.validated_data),
                [SaleItem(**sale_item) for sale_item in items],
            )
