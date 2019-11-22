import dataclasses
from typing import Union

from debt_site.models import Debt
from debt_site.repositories import DebtRepository, FakeDebtRepository


@dataclasses.dataclass
class DebtCreationService:
    debt_repository: Union[DebtRepository, FakeDebtRepository]

    def run(self, *, first_name: str, last_name: str,
            debt_amount: int) -> Debt:
        result: Debt = self.debt_repository.create(first_name=first_name,
                                                   last_name=last_name,
                                                   debt_amount=debt_amount)
        return result
