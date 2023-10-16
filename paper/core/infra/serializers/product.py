from typing import List

from rest_framework import serializers

from paper.core.controller.serializers.product import IProductReadSerializer, IProductWriteSerializer
from paper.core.domain.entity.product import CommissionPercentLimit, Product
from paper.core.utils.field import Weekday


class ProductReadSerializer(IProductReadSerializer):
    class Serializer(serializers.Serializer):
        class CommissionPercentLimitSerializer(serializers.Serializer):
            id = serializers.IntegerField(read_only=True)
            weekday = serializers.SerializerMethodField(read_only=True)
            min_commission_percent = serializers.CharField(read_only=True)
            max_commission_percent = serializers.CharField(read_only=True)

            def get_weekday(self, obj: CommissionPercentLimit) -> str:
                return Weekday.choices[obj.weekday % 7][1]

        id = serializers.IntegerField(read_only=True)
        code = serializers.CharField(read_only=True)
        description = serializers.CharField(read_only=True)
        price = serializers.CharField(read_only=True)
        commission_percent = serializers.CharField(read_only=True)
        commission_percent_limits = CommissionPercentLimitSerializer(
            many=True,
            read_only=True,
        )

    def to_json(self, instance: Product | List[Product]) -> dict:
        many = type(instance) is list
        return self.Serializer(instance, many=many).data


class ProductWriteSerializer(IProductWriteSerializer):
    class Serializer(serializers.ModelSerializer):
        class Meta:
            model = Product
            fields = ["code", "description", "price", "commission_percent"]

    def validate(self, data: dict) -> Product:
        serializer = self.Serializer(data=data)
        is_valid = serializer.is_valid(raise_exception=True)
        if is_valid:
            return Product(**serializer.validated_data)
