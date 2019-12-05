from typing import NoReturn

import pytest

from debt_site.repositories import DebtRepository, FakeDebtRepository


@pytest.mark.parametrize(
    'debt_repository_class',
    [  # type: ignore
        DebtRepository,
        FakeDebtRepository,
    ])
@pytest.mark.django_db  # type: ignore
def test_debt_repository_create(debt_repository_class) -> NoReturn:
    # Given:
    #   Empty repository
    repo = debt_repository_class()
    person = {
        "first_name": "Danya",
        "last_name": "Fedyaev",
        "debt_amount": 7000
    }

    # When:
    #   Debt is created
    created = repo.create(first_name=person["first_name"],
                          last_name=person["last_name"],
                          debt_amount=person["debt_amount"])
    # Then:
    #   Retrieving from repository returns list of 1 length w/ created Debt
    filtered = repo.filter()
    assert len(filtered) == 1
    assert created == filtered[0]


@pytest.mark.parametrize(
    'debt_repository_class',
    [  # type: ignore
        DebtRepository,
        FakeDebtRepository,
    ])
@pytest.mark.django_db  # type: ignore
def test_debt_repository_filter_on_empty_db(debt_repository_class) -> NoReturn:
    # Given:
    #   Empty repository
    repo = debt_repository_class()
    # When:
    #   Debt is not created
    # Then:
    #   Retrieving from repository returns list of 0 length w/o Debt
    filtered = repo.filter()
    assert len(filtered) == 0


@pytest.mark.parametrize(
    'debt_repository_class',
    [  # type: ignore
        DebtRepository,
        FakeDebtRepository,
    ])
@pytest.mark.django_db  # type: ignore
def test_debt_repository_filter(debt_repository_class) -> NoReturn:
    # Given:
    #   Empty repository
    repo = debt_repository_class()
    # When:
    #   2 Debts are created
    person = {
        "first_name": "Danya",
        "last_name": "Fedyaev",
        "debt_amount": 7000
    }
    person_2 = {
        "first_name": "Vitya",
        "last_name": "Voronin",
        "debt_amount": 15000
    }
    created = repo.create(first_name=person["first_name"],
                          last_name=person["last_name"],
                          debt_amount=person["debt_amount"])
    repo.create(first_name=person_2["first_name"],
                last_name=person_2["last_name"],
                debt_amount=person_2["debt_amount"])
    # Then
    #   Retrieving from repository returns list of 1
    #   filtered by first name, last name and debt amount
    filtered = repo.filter(first_name=person["first_name"],
                           last_name=person["last_name"],
                           debt_amount=person["debt_amount"])
    assert len(filtered) == 1
    assert created == filtered[0]
