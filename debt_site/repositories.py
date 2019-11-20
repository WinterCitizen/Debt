import dataclasses
from typing import Iterable, List

from debt_site.models import Debt


class DebtRepository:
    def create(self, first_name: str, last_name: str,
               debt_amount: str) -> Debt:
        result: Debt = Debt.objects.create(first_name=first_name,
                                           last_name=last_name,
                                           debt_amount=debt_amount)
        return result

    def filter(self, first_name: str, last_name: str,
               debt_amount: str) -> Iterable[Debt]:
        result: Iterable[Debt] = Debt.objects.filter(first_name=first_name,
                                                     last_name=last_name,
                                                     debt_amount=debt_amount)
        return result


@dataclasses.dataclass
class FakeDebtRepository:
    objects: List[Debt] = []

    def create(self, first_name: str, last_name: str,
               debt_amount: str) -> Debt:
        x = Debt(first_name=first_name,
                 last_name=last_name,
                 debt_amount=debt_amount)
        self.objects.append(x)
        return x

    def _matching(self, obj: Debt, first_name: str, last_name: str,
                  debt_amount: str) -> bool:
        if obj.first_name != first_name:
            return False
        if obj.last_name != last_name:
            return False
        if obj.debt_amount != debt_amount:
            return False
        return True

    def filter(self, first_name: str, last_name: str,
               debt_amount: str) -> Iterable[Debt]:
        matching_debts = []
        for obj in self.objects:
            if self._matching(obj, first_name, last_name, debt_amount):
                matching_debts.append(obj)
        return matching_debts
