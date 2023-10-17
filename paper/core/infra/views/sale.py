from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet

from paper.core.controller.sale import SaleController
from paper.core.infra.repository.sale import SaleRepository
from paper.core.infra.serializers.sale import SaleReadSerializer


class SaleView(ViewSet):
    repo = SaleRepository()
    read_serializer = SaleReadSerializer()

    def list(self, _: Request):
        data, status = SaleController(
            self.repo,
            self.read_serializer,
        ).list()
        return Response(data=data, status=status)
