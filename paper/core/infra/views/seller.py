from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet

from paper.core.controller.seller import SellerController
from paper.core.infra.repository.seller import SellerRepository
from paper.core.infra.serializers.seller import SellerReadSerializer, SellerWriteSerializer


class SellerView(ViewSet):
    repo = SellerRepository()
    read_serializer = SellerReadSerializer()
    write_serializer = SellerWriteSerializer()

    def list(self, _: Request):
        data, status = SellerController(
            self.repo,
            self.read_serializer,
        ).list()
        return Response(data=data, status=status)

    def retrieve(self, _: Request, pk: int):
        data, status = SellerController(
            self.repo,
            self.read_serializer,
        ).retrieve(pk)
        return Response(data=data, status=status)

    def delete(self, _: Request, pk: int):
        data, status = SellerController(self.repo).delete(pk)
        return Response(data=data, status=status)

    def create(self, request: Request):
        data, status = SellerController(
            self.repo,
            self.read_serializer,
            self.write_serializer,
        ).create(request.data)
        return Response(data=data, status=status)
