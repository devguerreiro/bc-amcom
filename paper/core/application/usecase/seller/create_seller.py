from paper.core.domain.entity.seller import Seller
from paper.core.domain.repository.seller import ISellerRepository


class CreateClient:
    def __init__(self, repo: ISellerRepository):
        self._repo = repo

    def handle(self, seller: Seller) -> Seller:
        return self._repo.create(seller)
