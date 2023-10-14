from decimal import Decimal

from paper.core.domain.entity.product import Product
from paper.core.domain.entity.sale import Sale
from paper.core.domain.repository.sale import ISaleRepository


class CalculateCommission:
    def __init__(self, repo: ISaleRepository):
        self.repo = repo

    def _get_commission_percent(self, product: Product) -> Decimal:
        return product.commission_percent

    def handle(self, sale: Sale) -> Decimal:
        total_commission = Decimal("0")
        for item in self.repo.get_items(sale):
            total_item_price = item.quantity * item.product.price
            commission_percent = self._get_commission_percent(item.product)
            total_item_commission = total_item_price * (commission_percent / 100)
            total_commission += total_item_commission
        return round(total_commission, 2)
