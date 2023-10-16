from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet

from paper.core.controller.client import ClientController
from paper.core.infra.repository.client import ClientRepository
from paper.core.infra.serializers.client import ListClientSerializer


class ClientView(ViewSet):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.client_repo = ClientRepository()

    def list(self, _: Request):
        data, status = ClientController(
            self.client_repo,
            ListClientSerializer,
        ).list()
        return Response(data=data, status=status)
