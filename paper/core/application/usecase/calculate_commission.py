from decimal import Decimal

from paper.core.application.usecase.get_commission_percent import GetCommissionPercent
from paper.core.domain.entity.sale import Sale
from paper.core.domain.repository.product import IProductRepository
from paper.core.domain.repository.sale import ISaleRepository


class CalculateCommission:
    def __init__(
        self,
        sale_repo: ISaleRepository,
        product_repo: IProductRepository,
    ):
        self.sale_repo = sale_repo
        self.product_repo = product_repo

    def handle(self, sale: Sale) -> Decimal:
        total_commission = Decimal("0")
        for item in self.sale_repo.get_items(sale):
            total_item_price = item.quantity * item.product.price
            commission_percent = GetCommissionPercent(self.product_repo).handle(item.product)
            total_item_commission = total_item_price * (commission_percent / 100)
            total_commission += total_item_commission
        return round(total_commission, 2)
