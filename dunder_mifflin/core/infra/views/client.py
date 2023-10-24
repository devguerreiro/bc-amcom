from drf_spectacular.utils import OpenApiExample, extend_schema
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet

from dunder_mifflin.core.controller.client import ClientController
from dunder_mifflin.core.infra.repository.client import ClientRepository
from dunder_mifflin.core.infra.serializers.client import ClientReadSerializer, ClientWriteSerializer

CLIENT_EXAMPLE = {"id": 1, "name": "Foo", "email": "foo@bar.com", "phone": "1234567890"}


class ClientView(ViewSet):
    repo = ClientRepository()
    read_serializer = ClientReadSerializer()
    write_serializer = ClientWriteSerializer()

    @extend_schema(
        responses={200: ClientReadSerializer},
        description="Listagem de todos os clientes cadastrados",
        examples=[
            OpenApiExample(
                "Exemplo",
                value=CLIENT_EXAMPLE,
            )
        ],
    )
    def list(self, _: Request):
        data, status = ClientController(
            self.repo,
            self.read_serializer,
        ).list()
        return Response(data=data, status=status)

    @extend_schema(
        responses={200: ClientReadSerializer},
        description="Recuperacao pelo id de um cliente cadastrado",
        examples=[
            OpenApiExample(
                "Exemplo",
                value=CLIENT_EXAMPLE,
            )
        ],
    )
    def retrieve(self, _: Request, pk: int):
        data, status = ClientController(
            self.repo,
            self.read_serializer,
        ).retrieve(pk)
        return Response(data=data, status=status)

    @extend_schema(
        responses={204: None},
        description="Remocao pelo id de um cliente cadastrado",
    )
    def destroy(self, _: Request, pk: int):
        data, status = ClientController(self.repo).delete(pk)
        return Response(data=data, status=status)

    @extend_schema(
        responses={201: ClientReadSerializer},
        description="Cadastro de um novo cliente",
        examples=[
            OpenApiExample(
                "Exemplo",
                value=CLIENT_EXAMPLE,
            )
        ],
    )
    def create(self, request: Request):
        data, status = ClientController(
            self.repo,
            self.read_serializer,
            self.write_serializer,
        ).create(request.data)
        return Response(data=data, status=status)
