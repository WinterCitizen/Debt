import dataclasses
from typing import Dict, List, Union

from django.db.models.query import QuerySet

from debt_site.models import Debt


class DebtRepository:
    def create(
        self, *, first_name: str, last_name: str, debt_amount: int,
    ) -> Debt:
        return Debt.objects.create(
            first_name=first_name,
            last_name=last_name,
            debt_amount=debt_amount,
        )

    def filter(  # noqa: A003
        self, **fields: Dict[str, Union[str, int]],
    ) -> QuerySet:  # type: ignore
        return Debt.objects.filter(**fields)


@dataclasses.dataclass
class FakeDebtRepository:
    _debts: List[Debt] = dataclasses.field(default_factory=list)

    def create(
        self, *, first_name: str, last_name: str, debt_amount: int,
    ) -> Debt:
        debt = Debt(
            first_name=first_name,
            last_name=last_name,
            debt_amount=debt_amount,
        )
        self._debts.append(debt)
        return debt

    def filter(  # noqa: A003
        self, **fields: Dict[str, Union[str, int]],
    ) -> List[Debt]:
        matching_debts = []
        for debt in self._debts:
            if self._matching(debt, **fields):
                matching_debts.append(debt)
        return matching_debts

    def _matching(
        self, debt: Debt, **fields: Dict[str, Union[str, int]],
    ) -> bool:
        for key, value in fields.items():  # noqa: WPS110
            if getattr(debt, key) != value:
                return False
        return True
