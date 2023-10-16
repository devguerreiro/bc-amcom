from paper.core.domain.entity.seller import Seller
from paper.core.domain.repository.seller import ISellerRepository


class RetrieveSeller:
    def __init__(self, repo: ISellerRepository):
        self._repo = repo

    def handle(self, pk: int) -> Seller:
        return self._repo.get_by_id(pk)
