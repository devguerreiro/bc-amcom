from typing import List

from rest_framework import serializers

from dunder_mifflin.core.controller.serializers.seller import ISellerReadSerializer, ISellerWriteSerializer
from dunder_mifflin.core.domain.entity.seller import Seller


class SellerReadSerializer(ISellerReadSerializer):
    class Serializer(serializers.Serializer):
        id = serializers.IntegerField(read_only=True)
        name = serializers.CharField(read_only=True)
        email = serializers.EmailField(read_only=True)
        phone = serializers.CharField(read_only=True)

    def to_json(self, instance: Seller | List[Seller]) -> dict:
        many = type(instance) is list
        return self.Serializer(instance, many=many).data


class SellerWriteSerializer(ISellerWriteSerializer):
    class Serializer(serializers.ModelSerializer):
        class Meta:
            model = Seller
            fields = ["name", "email", "phone"]

    def validate(self, data: dict) -> Seller:
        serializer = self.Serializer(data=data)
        is_valid = serializer.is_valid(raise_exception=True)
        if is_valid:
            return Seller(**serializer.validated_data)
