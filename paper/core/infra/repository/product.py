from typing import List

from paper.core.domain.entity.product import CommissionPercentLimit, Product
from paper.core.domain.repository.product import IProductRepository


class ProductRepository(IProductRepository):
    def get_all(self) -> List[Product]:
        return list(Product.objects.all())

    def get_commission_percent_limits(self, product: Product) -> List[CommissionPercentLimit]:
        pass
