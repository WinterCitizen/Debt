from typing import NoReturn

import pytest

from debt_site.repositories import DBDebtRepository, FakeDebtRepository


@pytest.mark.parametrize(
    'debt_repository_class',
    [  # type: ignore
        DBDebtRepository,
        FakeDebtRepository,
    ])
@pytest.mark.django_db  # type: ignore
def test_debt_repository_create(debt_repository_class) -> NoReturn:
    repo = debt_repository_class()
    first_name, last_name, debt_amount = "Danya", "Fedyaev", 7000
    created = repo.create(first_name=first_name,
                          last_name=last_name,
                          debt_amount=debt_amount)
    filtered = repo.filter(first_name=first_name,
                           last_name=last_name,
                           debt_amount=debt_amount)
    assert len(filtered) == 1
    assert created == filtered[0]


@pytest.mark.parametrize(
    'debt_repository_class',
    [  # type: ignore
        DBDebtRepository,
        FakeDebtRepository,
    ])
@pytest.mark.django_db  # type: ignore
def test_debt_repository_filter_on_empty_db(debt_repository_class) -> NoReturn:
    repo = debt_repository_class()
    filtered = repo.filter()
    assert len(filtered) == 0


@pytest.mark.parametrize(
    'debt_repository_class',
    [  # type: ignore
        DBDebtRepository,
        FakeDebtRepository,
    ])
@pytest.mark.django_db  # type: ignore
def test_debt_repository_filter(debt_repository_class) -> NoReturn:
    repo = debt_repository_class()
    first_name, last_name, debt_amount = "Danya", "Fedyaev", 10000
    created = repo.create(first_name=first_name,
                          last_name=last_name,
                          debt_amount=debt_amount)
    repo.create(first_name="Vitya", last_name="Voronin", debt_amount=15000)
    filtered = repo.filter(first_name=first_name,
                           last_name=last_name,
                           debt_amount=debt_amount)
    assert len(filtered) == 1
    assert created == filtered[0]
