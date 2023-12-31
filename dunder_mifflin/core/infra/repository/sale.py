from datetime import date
from typing import List

from django.db.models import Q

from dunder_mifflin.core.domain.entity.sale import Sale, SaleItem
from dunder_mifflin.core.domain.repository.sale import ISaleRepository


class SaleRepository(ISaleRepository):
    def get_all(self) -> List[Sale]:
        return list(Sale.objects.select_related("client", "seller").prefetch_related("items__product").all())

    def get_by_id(self, pk: int) -> Sale:
        return Sale.objects.get(pk=pk)

    def delete_by_id(self, pk: int) -> None:
        Sale.objects.filter(id=pk).delete()

    def create(self, sale: Sale, items: List[SaleItem]) -> Sale:
        sale.save(force_insert=True)

        for item in items:
            item.sale = sale

        SaleItem.objects.bulk_create(items)

        return sale

    def update(self, sale: Sale, sale_updated: Sale, items: List[SaleItem]) -> Sale:
        sale.client = sale_updated.client
        sale.seller = sale_updated.seller
        sale.save(force_update=True)

        for item in items:
            SaleItem.objects.update_or_create(
                sale=sale, product_id=item.product.id, defaults={"quantity": item.quantity}
            )

        SaleItem.objects.filter(
            ~Q(
                product_id__in=[item.product.id for item in items],
            ),
            sale=sale,
        ).delete()

    def get_commissions(self, start_date: date, end_date: date) -> List[Sale]:
        return list(
            Sale.objects.select_related("seller")
            .prefetch_related("items__product")
            .filter(
                created_at__date__lte=end_date,
                created_at__date__gte=start_date,
            )
            .all()
        )
