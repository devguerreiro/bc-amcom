from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet

from paper.core.controller.product import ProductController
from paper.core.infra.repository.product import ProductRepository
from paper.core.infra.serializers.product import ProductReadSerializer


class ProductView(ViewSet):
    repo = ProductRepository()
    read_serializer = ProductReadSerializer()

    def list(self, _: Request):
        data, status = ProductController(
            self.repo,
            self.read_serializer,
        ).list()
        return Response(data=data, status=status)

    def retrieve(self, _: Request, pk: int):
        data, status = ProductController(
            self.repo,
            self.read_serializer,
        ).retrieve(pk)
        return Response(data=data, status=status)
