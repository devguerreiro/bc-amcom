from typing import List

from paper.core.domain.entity.product import Product
from paper.core.domain.repository.product import IProductRepository


class ProductRepository(IProductRepository):
    def get_all(self) -> List[Product]:
        return list(Product.objects.all())

    def get_by_id(self, pk: int) -> Product:
        return Product.objects.get(pk=pk)

    def delete_by_id(self, pk: int) -> None:
        Product.objects.filter(id=pk).delete()

    def create(self, product: Product) -> Product:
        product.save(force_insert=True)
        return product
