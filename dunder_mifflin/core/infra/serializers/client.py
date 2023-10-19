from typing import List

from rest_framework import serializers

from dunder_mifflin.core.controller.serializers.client import IClientReadSerializer, IClientWriteSerializer
from dunder_mifflin.core.domain.entity.client import Client


class ClientReadSerializer(IClientReadSerializer):
    class Serializer(serializers.Serializer):
        id = serializers.IntegerField(read_only=True)
        name = serializers.CharField(read_only=True)
        email = serializers.EmailField(read_only=True)
        phone = serializers.CharField(read_only=True)

    def to_json(self, instance: Client | List[Client]) -> dict:
        many = type(instance) is list
        return self.Serializer(instance, many=many).data


class ClientWriteSerializer(IClientWriteSerializer):
    class Serializer(serializers.ModelSerializer):
        class Meta:
            model = Client
            fields = ["name", "email", "phone"]

    def validate(self, data: dict) -> Client:
        serializer = self.Serializer(data=data)
        is_valid = serializer.is_valid(raise_exception=True)
        if is_valid:
            return Client(**serializer.validated_data)
