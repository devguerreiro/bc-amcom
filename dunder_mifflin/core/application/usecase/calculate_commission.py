from datetime import date
from decimal import Decimal
from typing import List

from dunder_mifflin.core.domain.entity.commission import CommissionLimit
from dunder_mifflin.core.domain.entity.product import Product
from dunder_mifflin.core.domain.entity.sale import Sale
from dunder_mifflin.core.domain.repository.commission_limit import ICommissionLimitRepository
from dunder_mifflin.core.domain.repository.sale import ISaleRepository


class CalculateCommission:
    def __init__(
        self,
        sale_repo: ISaleRepository,
        commission_repo: ICommissionLimitRepository,
    ):
        self._sale_repo = sale_repo
        self._commission_repo = commission_repo

    def _get_commission_percent(
        self,
        sale: Sale,
        product: Product,
        limits: List[CommissionLimit],
    ) -> Decimal:
        sale_weekday = sale.created_at.weekday()
        limit = [limit for limit in limits if limit.weekday == sale_weekday]
        if limit:
            if product.commission_percent < limit[0].min_commission_percent:
                return limit[0].min_commission_percent
            elif product.commission_percent > limit[0].max_commission_percent:
                return limit[0].max_commission_percent
        return product.commission_percent

    def handle(self, start_date: date, end_date: date):
        sales = self._sale_repo.get_commissions(start_date, end_date)
        commission_limits = self._commission_repo.get_all()
        total_by_seller = {}
        for sale in sales:
            for item in list(sale.items.all()):
                commission_percent = self._get_commission_percent(
                    sale,
                    item.product,
                    commission_limits,
                )
                total_commission = item.quantity * item.product.price * (commission_percent / 100)
                seller_total = total_by_seller.get(sale.seller.id)
                if seller_total is None:
                    total_by_seller[sale.seller.id] = {
                        "total_commission": total_commission,
                        "total_quantity": item.quantity,
                        "seller": sale.seller.name,
                    }
                else:
                    total_by_seller[sale.seller.id]["total_commission"] += total_commission
                    total_by_seller[sale.seller.id]["total_quantity"] += item.quantity
        return list([{"id": id, **seller} for (id, seller) in total_by_seller.items()])
