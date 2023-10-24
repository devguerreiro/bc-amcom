from drf_spectacular.utils import OpenApiExample, extend_schema
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet

from dunder_mifflin.core.controller.seller import SellerController
from dunder_mifflin.core.infra.repository.seller import SellerRepository
from dunder_mifflin.core.infra.serializers.seller import SellerReadSerializer, SellerWriteSerializer

SELLER_EXAMPLE = {"id": 1, "name": "Foo", "email": "foo@bar.com", "phone": "1234567890"}


class SellerView(ViewSet):
    repo = SellerRepository()
    read_serializer = SellerReadSerializer()
    write_serializer = SellerWriteSerializer()

    @extend_schema(
        responses={200: SellerReadSerializer},
        description="Listagem de todos os vendedores cadastrados",
        examples=[
            OpenApiExample(
                "Exemplo",
                value=SELLER_EXAMPLE,
            )
        ],
    )
    def list(self, _: Request):
        data, status = SellerController(
            self.repo,
            self.read_serializer,
        ).list()
        return Response(data=data, status=status)

    @extend_schema(
        responses={200: SellerReadSerializer},
        description="Recuperacao pelo id de um vendedor cadastrado",
        examples=[
            OpenApiExample(
                "Exemplo",
                value=SELLER_EXAMPLE,
            )
        ],
    )
    def retrieve(self, _: Request, pk: int):
        data, status = SellerController(
            self.repo,
            self.read_serializer,
        ).retrieve(pk)
        return Response(data=data, status=status)

    @extend_schema(
        responses={204: None},
        description="Remocao pelo id de um vendedor cadastrado",
    )
    def destroy(self, _: Request, pk: int):
        data, status = SellerController(self.repo).delete(pk)
        return Response(data=data, status=status)

    @extend_schema(
        responses={201: SellerReadSerializer},
        description="Cadastro de um novo vendedor",
        examples=[
            OpenApiExample(
                "Exemplo",
                value=SELLER_EXAMPLE,
            )
        ],
    )
    def create(self, request: Request):
        data, status = SellerController(
            self.repo,
            self.read_serializer,
            self.write_serializer,
        ).create(request.data)
        return Response(data=data, status=status)
