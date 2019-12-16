import dataclasses
from typing import Dict, List, Union

from django.db.models.query import QuerySet

from debt_site.models import Debt
from debt_site.repositories import DebtRepository, FakeDebtRepository


@dataclasses.dataclass
class DebtCreationService:
    debt_repository: Union[DebtRepository, FakeDebtRepository]

    def run(
        self, *, first_name: str, last_name: str, debt_amount: int,
    ) -> Debt:
        return self.debt_repository.create(
            first_name=first_name,
            last_name=last_name,
            debt_amount=debt_amount,
        )


@dataclasses.dataclass
class DebtGetService:
    debt_repository: DebtRepository

    def run(self, **fields: Dict[str, Union[str, int]]) -> QuerySet:  # type: ignore
        return self.debt_repository.filter(**fields)
