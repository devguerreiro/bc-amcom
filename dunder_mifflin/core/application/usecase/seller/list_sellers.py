from typing import List

from dunder_mifflin.core.domain.entity.seller import Seller
from dunder_mifflin.core.domain.repository.seller import ISellerRepository


class ListSellers:
    def __init__(self, repo: ISellerRepository):
        self._repo = repo

    def handle(self) -> List[Seller]:
        return self._repo.get_all()
