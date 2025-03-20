import pytest

from bond import Bond


@pytest.fixture
def mock_bond():
    bond = Bond()
    bond.isin = "FR15"
    bond.rate = 0.04
    bond.currency = "EUR"
    bond.face_value = 100000

    return bond

def test_bond_coupon(mock_bond):
    expected = 4000.0
    actual = mock_bond.coupon_amount()

    assert actual == expected

def test_bond_description(mock_bond):
    expected = "FR15_EUR_4.00%"
    actual = mock_bond.description()

    assert expected == actual