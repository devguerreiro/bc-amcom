from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet

from paper.core.controller.sale import SaleController
from paper.core.infra.repository.sale import SaleRepository
from paper.core.infra.serializers.sale import SaleReadSerializer, SaleWriteSerializer


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
