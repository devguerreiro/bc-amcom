from rest_framework import serializers

from paper.core.domain.serializer.client import IClientSerializer


class ListClientSerializer(IClientSerializer):
    class Serializer(serializers.Serializer):
        id = serializers.IntegerField(read_only=True)
        name = serializers.CharField(read_only=True)
        email = serializers.EmailField(read_only=True)
        phone = serializers.CharField(read_only=True)

    def to_json(self):
        return self.Serializer(self.data, many=True).data
