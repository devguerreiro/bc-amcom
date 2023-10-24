from datetime import datetime

from drf_spectacular.types import OpenApiTypes
from drf_spectacular.utils import OpenApiExample, OpenApiParameter, extend_schema
from rest_framework.decorators import action
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet

from dunder_mifflin.core.controller.sale import SaleController
from dunder_mifflin.core.infra.repository.commission_limit import CommissionLimitRepository
from dunder_mifflin.core.infra.repository.sale import SaleRepository
from dunder_mifflin.core.infra.serializers.sale import SaleReadSerializer, SaleWriteSerializer

SALE_EXAMPLE = {
    "id": 1,
    "nfe": "123-456-789-1011-1245",
    "client": {"id": 1, "name": "Foo", "email": "foo@bar.com", "phone": "1234567890"},
    "seller": {"id": 1, "name": "Foo", "email": "foo@bar.com", "phone": "1234567890"},
    "items": [
        {
            "id": 1,
            "product": {
                "id": 1,
                "code": "Foo",
                "description": "Foo bar",
                "price": "10.00",
                "commission_percent": "10.00",
            },
            "quantity": 10,
            "created_at": "2000-10-31T01:30:00.000-05:00",
            "updated_at": "2000-10-31T01:30:00.000-05:00",
        },
    ],
}


class SaleView(ViewSet):
    repo = SaleRepository()
    commission_repo = CommissionLimitRepository()
    read_serializer = SaleReadSerializer()
    write_serializer = SaleWriteSerializer()

    @extend_schema(
        responses={200: SaleReadSerializer},
        description="Listagem de todas as vendas feitas",
        examples=[
            OpenApiExample(
                "Exemplo",
                value=SALE_EXAMPLE,
            )
        ],
    )
    def list(self, _: Request):
        data, status = SaleController(
            self.repo,
            self.read_serializer,
        ).list()
        return Response(data=data, status=status)

    @extend_schema(
        responses={200: SaleReadSerializer},
        description="Recuperacao pelo id de uma venda cadastrada",
        examples=[
            OpenApiExample(
                "Exemplo",
                value=SALE_EXAMPLE,
            )
        ],
    )
    def retrieve(self, _: Request, pk: int):
        data, status = SaleController(
            self.repo,
            self.read_serializer,
        ).retrieve(pk)
        return Response(data=data, status=status)

    @extend_schema(
        responses={204: None},
        description="Remocao pelo id de uma venda cadastrada",
    )
    def delete(self, _: Request, pk: int):
        data, status = SaleController(self.repo).delete(pk)
        return Response(data=data, status=status)

    @extend_schema(
        responses={200: SaleReadSerializer},
        description="Recuperacao pelo id de uma venda cadastrada",
        examples=[
            OpenApiExample(
                "Exemplo",
                value=SALE_EXAMPLE,
            )
        ],
    )
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

    @extend_schema(
        responses={200: SaleReadSerializer},
        description="Atualizacao pelo id de uma venda cadastrada",
        examples=[
            OpenApiExample(
                "Exemplo",
                value=SALE_EXAMPLE,
            )
        ],
    )
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

    @extend_schema(
        parameters=[
            OpenApiParameter("from", OpenApiTypes.DATE, examples=[OpenApiExample("Exemplo", value="dd/mm/yyyy")]),
            OpenApiParameter("to", OpenApiTypes.DATE, examples=[OpenApiExample("Exemplo", value="dd/mm/yyyy")]),
        ],
        responses={200: SaleReadSerializer},
        description="Comissao total das vendas de um periodo",
        examples=[
            OpenApiExample(
                "Exemplo",
                value=[
                    {
                        "id": 1,
                        "seller": "Foo Bar",
                        "total_commission": 1_200_000,
                        "total_quantity": 100,
                    }
                ],
            )
        ],
    )
    @action(methods=["GET"], detail=False)
    def commissions(self, request: Request):
        try:
            start_date = datetime.strptime(
                request.query_params["from"],
                "%d/%m/%Y",
            )
            end_date = datetime.strptime(
                request.query_params["to"],
                "%d/%m/%Y",
            )

            data, status = SaleController(self.repo, commission_repo=self.commission_repo).get_commissions(
                start_date, end_date
            )
            return Response(data=data, status=status)
        except Exception as e:
            return Response(data={"error": str(e)}, status=400)
