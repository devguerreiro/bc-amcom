from datetime import datetime
from decimal import Decimal

from paper.core.domain.entity.product import Product
from paper.core.domain.entity.sale import Sale
from paper.core.domain.repository.commission import ICommissionLimitRepository
from paper.core.domain.repository.sale import ISaleRepository


class CalculateCommission:
    def __init__(
        self,
        sale_repo: ISaleRepository,
        commission_repo: ICommissionLimitRepository,
    ):
        self._sale_repo = sale_repo
        self._commission_repo = commission_repo

    def _get_commission_percent(self, product: Product) -> Decimal:
        weekday_now = datetime.now().weekday()
        commission_limit = self._commission_repo.get_by_weekday(weekday_now)
        if commission_limit:
            if product.commission_percent < commission_limit.min_commission_percent:
                return commission_limit.min_commission_percent
            elif product.commission_percent > commission_limit.max_commission_percent:
                return commission_limit.max_commission_percent
        return product.commission_percent

    def handle(self, sale: Sale) -> Decimal:
        total_commission = Decimal("0")
        for item in self._sale_repo.get_items(sale):
            total_item_price = item.quantity * item.product.price
            commission_percent = self._get_commission_percent(item.product)
            total_item_commission = total_item_price * (commission_percent / 100)
            total_commission += total_item_commission
        return round(total_commission, 2)
