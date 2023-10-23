from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet

from dunder_mifflin.core.controller.sale import SaleController
from dunder_mifflin.core.infra.repository.sale import SaleRepository
from dunder_mifflin.core.infra.serializers.sale import SaleReadSerializer, SaleWriteSerializer


class SaleView(ViewSet):
    repo = SaleRepository()
    read_serializer = SaleReadSerializer()
    write_serializer = SaleWriteSerializer()

    def list(self, _: Request):
        data, status = SaleController(
            self.repo,
            self.read_serializer,
        ).list()
        return Response(data=data, status=status)

    def retrieve(self, _: Request, pk: int):
        data, status = SaleController(
            self.repo,
            self.read_serializer,
        ).retrieve(pk)
        return Response(data=data, status=status)

    def delete(self, _: Request, pk: int):
        data, status = SaleController(self.repo).delete(pk)
        return Response(data=data, status=status)

    def create(self, request: Request):
        try:
            data, status = SaleController(
                self.repo,
                self.read_serializer,
                self.write_serializer,
            ).create(request.data)
            return Response(data=data, status=status)
        except Exception as e:
            return Response(data={"error": str(e)}, status=400)

    def update(self, request: Request, pk: int):
        try:
            data, status = SaleController(
                self.repo,
                self.read_serializer,
                self.write_serializer,
            ).update(request.data, pk)
            return Response(data=data, status=status)
        except Exception as e:
            return Response(data={"error": str(e)}, status=400)
