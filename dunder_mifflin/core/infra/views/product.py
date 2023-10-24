from drf_spectacular.utils import OpenApiExample, extend_schema
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet

from dunder_mifflin.core.controller.product import ProductController
from dunder_mifflin.core.infra.repository.product import ProductRepository
from dunder_mifflin.core.infra.serializers.product import ProductReadSerializer, ProductWriteSerializer

PRODUCT_EXAMPLE = {
    "id": 1,
    "code": "Foo",
    "description": "Foo bar",
    "price": "10.00",
    "commission_percent": "10.00",
}


class ProductView(ViewSet):
    repo = ProductRepository()
    read_serializer = ProductReadSerializer()
    write_serializer = ProductWriteSerializer()

    @extend_schema(
        responses={200: ProductReadSerializer},
        description="Listagem de todos os produtos cadastrados",
        examples=[
            OpenApiExample(
                "Exemplo",
                value=PRODUCT_EXAMPLE,
            )
        ],
    )
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

    @extend_schema(
        responses={200: ProductReadSerializer},
        description="Recuperacao pelo id de um produto cadastrado",
        examples=[
            OpenApiExample(
                "Exemplo",
                value=PRODUCT_EXAMPLE,
            )
        ],
    )
    def retrieve(self, _: Request, pk: int):
        data, status = ProductController(
            self.repo,
            self.read_serializer,
        ).retrieve(pk)
        return Response(data=data, status=status)

    @extend_schema(
        responses={204: None},
        description="Remocao pelo id de um produto cadastrado",
    )
    def destroy(self, _: Request, pk: int):
        data, status = ProductController(
            self.repo,
            self.read_serializer,
        ).delete(pk)
        return Response(data=data, status=status)

    @extend_schema(
        responses={201: ProductReadSerializer},
        description="Cadastro de um novo produto",
        examples=[
            OpenApiExample(
                "Exemplo",
                value=PRODUCT_EXAMPLE,
            )
        ],
    )
    def create(self, request: Request):
        data, status = ProductController(
            self.repo,
            self.read_serializer,
            self.write_serializer,
        ).create(request.data)
        return Response(data=data, status=status)
