from typing import List

from dunder_mifflin.core.domain.entity.commission import CommissionLimit
from dunder_mifflin.core.domain.repository.commission_limit import ICommissionLimitRepository


class CommissionLimitRepository(ICommissionLimitRepository):
    def get_all(self) -> List[CommissionLimit]:
        return list(CommissionLimit.objects.all())
