from dunder_mifflin.core.application.usecase.product.create_product import CreateProduct
from dunder_mifflin.core.application.usecase.product.delete_product import DeleteProduct
from dunder_mifflin.core.application.usecase.product.list_products import ListProducts
from dunder_mifflin.core.application.usecase.product.retrieve_product import RetrieveProduct
from dunder_mifflin.core.controller.serializers.product import IProductReadSerializer, IProductWriteSerializer
from dunder_mifflin.core.domain.repository.product import IProductRepository


class ProductController:
    def __init__(
        self,
        repo: IProductRepository,
        read_serializer: IProductReadSerializer = None,
        write_serializer: IProductWriteSerializer = None,
    ) -> None:
        self._repo = repo
        self._read_serializer = read_serializer
        self._write_serializer = write_serializer

    def list(self):
        products = ListProducts(self._repo).handle()
        data = self._read_serializer.to_json(products)
        return data, 200

    def retrieve(self, pk: int):
        product = RetrieveProduct(self._repo).handle(pk)
        data = self._read_serializer.to_json(product)
        return data, 200

    def delete(self, pk: int):
        DeleteProduct(self._repo).handle(pk)
        return None, 204

    def create(self, data: dict):
        valid_product = self._write_serializer.validate(data)
        new_product = CreateProduct(self._repo).handle(valid_product)
        data = self._read_serializer.to_json(new_product)
        return data, 201
