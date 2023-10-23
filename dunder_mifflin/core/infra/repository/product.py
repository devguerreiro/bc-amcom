from typing import List

from django.db.models import Q

from dunder_mifflin.core.domain.entity.product import Product
from dunder_mifflin.core.domain.repository.product import IProductRepository


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

    def get_by_params(self, query_params: dict) -> List[Product]:
        code = query_params.get("code")
        description = query_params.get("description")
        return list(Product.objects.filter(Q(code__icontains=code) | Q(description__icontains=description)).all())
