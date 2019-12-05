import dataclasses
from typing import Dict, List, Union

from django.db.models.query import QuerySet  # type: ignore

from debt_site.models import Debt


class DebtRepository:
    def create(self, *, first_name: str, last_name: str,
               debt_amount: int) -> Debt:
        result: Debt = Debt.objects.create(first_name=first_name,
                                           last_name=last_name,
                                           debt_amount=debt_amount)
        return result

    def filter(self, **fields: Dict[str, Union[str, int]]) -> QuerySet:
        result: QuerySet = Debt.objects.filter(**fields)
        return result


@dataclasses.dataclass
class FakeDebtRepository:
    _objects: List[Debt] = dataclasses.field(default_factory=list)

    def create(self, *, first_name: str, last_name: str,
               debt_amount: int) -> Debt:
        x = Debt(first_name=first_name,
                 last_name=last_name,
                 debt_amount=debt_amount)
        self._objects.append(x)
        return x

    def _matching(self, obj: Debt,
                  **fields: Dict[str, Union[str, int]]) -> bool:
        for key, value in fields.items():
            if getattr(obj, key) != value:
                return False
        return True

    def filter(self, **fields: Dict[str, Union[str, int]]) -> List[Debt]:
        matching_debts = []
        for obj in self._objects:
            if self._matching(obj, **fields):
                matching_debts.append(obj)
        return matching_debts
