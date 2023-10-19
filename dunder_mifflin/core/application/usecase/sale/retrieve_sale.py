from dunder_mifflin.core.domain.entity.sale import Sale
from dunder_mifflin.core.domain.repository.sale import ISaleRepository


class RetrieveSale:
    def __init__(self, repo: ISaleRepository):
        self._repo = repo

    def handle(self, pk: int) -> Sale:
        return self._repo.get_by_id(pk)
