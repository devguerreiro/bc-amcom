from dunder_mifflin.core.application.usecase.sale.create_sale import CreateSale
from dunder_mifflin.core.application.usecase.sale.delete_sale import DeleteSale
from dunder_mifflin.core.application.usecase.sale.list_sales import ListSales
from dunder_mifflin.core.application.usecase.sale.retrieve_sale import RetrieveSale
from dunder_mifflin.core.controller.serializers.sale import ISaleReadSerializer, ISaleWriteSerializer
from dunder_mifflin.core.domain.repository.sale import ISaleRepository


class SaleController:
    def __init__(
        self,
        repo: ISaleRepository,
        read_serializer: ISaleReadSerializer = None,
        write_serializer: ISaleWriteSerializer = None,
    ) -> None:
        self._repo = repo
        self._read_serializer = read_serializer
        self._write_serializer = write_serializer

    def list(self):
        sales = ListSales(self._repo).handle()
        data = self._read_serializer.to_json(sales)
        return data, 200

    def retrieve(self, pk: int):
        sales = RetrieveSale(self._repo).handle(pk)
        data = self._read_serializer.to_json(sales)
        return data, 200

    def delete(self, pk: int):
        DeleteSale(self._repo).handle(pk)
        return None, 204

    def create(self, data: dict):
        valid_sale, valid_items = self._write_serializer.validate(data)
        new_sale = CreateSale(self._repo).handle(valid_sale, valid_items)
        data = self._read_serializer.to_json(new_sale)
        return data, 201
