from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet

from dunder_mifflin.core.controller.product import ProductController
from dunder_mifflin.core.infra.repository.product import ProductRepository
from dunder_mifflin.core.infra.serializers.product import ProductReadSerializer, ProductWriteSerializer


class ProductView(ViewSet):
    repo = ProductRepository()
    read_serializer = ProductReadSerializer()
    write_serializer = ProductWriteSerializer()

    def list(self, request: Request):
        if request.query_params:
            data, status = ProductController(
                self.repo,
                self.read_serializer,
            ).get_by_params(request.query_params)
        else:
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

    def delete(self, _: Request, pk: int):
        data, status = ProductController(
            self.repo,
            self.read_serializer,
        ).delete(pk)
        return Response(data=data, status=status)

    def create(self, request: Request):
        data, status = ProductController(
            self.repo,
            self.read_serializer,
            self.write_serializer,
        ).create(request.data)
        return Response(data=data, status=status)
