from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet

from paper.core.controller.client import ClientController
from paper.core.infra.repository.client import ClientRepository
from paper.core.infra.serializers.client import ClientReadSerializer, ClientWriteSerializer


class ClientView(ViewSet):
    repo = ClientRepository()
    read_serializer = ClientReadSerializer()
    write_serializer = ClientWriteSerializer()

    def list(self, _: Request):
        data, status = ClientController(
            self.repo,
            self.read_serializer,
        ).list()
        return Response(data=data, status=status)

    def retrieve(self, _: Request, pk: int):
        data, status = ClientController(
            self.repo,
            self.read_serializer,
        ).retrieve(pk)
        return Response(data=data, status=status)

    def delete(self, _: Request, pk: int):
        data, status = ClientController(self.repo).delete(pk)
        return Response(data=data, status=status)

    def create(self, request: Request):
        data, status = ClientController(
            self.repo,
            self.read_serializer,
            self.write_serializer,
        ).create(request.data)
        return Response(data=data, status=status)
