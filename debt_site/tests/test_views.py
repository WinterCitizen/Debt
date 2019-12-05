from http import HTTPStatus

from django.test import Client

import _pytest  # noqa: WPS436
import pytest
from debt_site.repositories import FakeDebtRepository
from debt_site.services import DebtCreationService
from debt_site.views import DebtView


@pytest.fixture
def client() -> Client:
    return Client()


def test_debt_view_post(
    monkeypatch: _pytest.monkeypatch.MonkeyPatch,
    client: Client,  # noqa: WPS442
) -> None:
    repo = FakeDebtRepository()
    monkeypatch.setattr(
        DebtView, 'service', DebtCreationService(repo), raising=True,
    )
    form_data = {
        'first_name': 'Vitas',
        'last_name': 'Sabenin',
        'debt_amount': 312312,
    }
    response = client.post('/', form_data, follow=True)
    filtered = repo.filter()
    assert response.status_code == HTTPStatus.OK
    assert len(filtered) == 1
    debt = filtered[0]
    assert debt.first_name == form_data['first_name']
    assert debt.last_name == form_data['last_name']
    assert debt.debt_amount == form_data['debt_amount']
