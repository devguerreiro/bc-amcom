from typing import List

from dunder_mifflin.core.domain.entity.seller import Seller
from dunder_mifflin.core.domain.repository.seller import ISellerRepository


class SellerRepository(ISellerRepository):
    def get_all(self) -> List[Seller]:
        return list(Seller.objects.all())

    def get_by_id(self, pk: int) -> Seller:
        return Seller.objects.get(pk=pk)

    def delete_by_id(self, pk: int) -> None:
        Seller.objects.filter(id=pk).delete()

    def create(self, seller: Seller) -> Seller:
        seller.save(force_insert=True)
        return seller
