from paper.core.application.usecase.product.list_products import ListProducts
from paper.core.controller.serializers.product import IProductReadSerializer
from paper.core.domain.repository.product import IProductRepository


class ProductController:
    def __init__(
        self,
        repo: IProductRepository,
        read_serializer: IProductReadSerializer = None,
    ) -> None:
        self._repo = repo
        self._read_serializer = read_serializer

    def list(self):
        products = ListProducts(self._repo).handle()
        data = self._read_serializer.to_json(products)
        return data, 200
