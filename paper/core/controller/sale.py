from paper.core.application.usecase.sale.delete_sale import DeleteSale
from paper.core.application.usecase.sale.list_sales import ListSales
from paper.core.application.usecase.sale.retrieve_sale import RetrieveSale
from paper.core.controller.serializers.sale import ISaleReadSerializer
from paper.core.domain.repository.sale import ISaleRepository


class SaleController:
    def __init__(
        self,
        repo: ISaleRepository,
        read_serializer: ISaleReadSerializer = None,
    ) -> None:
        self._repo = repo
        self._read_serializer = read_serializer

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
