from datetime import datetime
from decimal import Decimal

from paper.core.domain.entity.product import Product
from paper.core.domain.repository.product import IProductRepository


class GetCommissionPercent:
    def __init__(self, product_repo: IProductRepository):
        self.product_repo = product_repo

    def handle(self, product: Product) -> Decimal:
        commission_percent_limits = self.product_repo.get_commission_percent_limits(product)
        currently_weekday = datetime.now().weekday()
        for limit in commission_percent_limits:
            if limit.weekday == currently_weekday:
                if product.commission_percent < limit.min_commission_percent:
                    return limit.min_commission_percent
                elif product.commission_percent > limit.max_commission_percent:
                    return limit.max_commission_percent
        return product.commission_percent
