from helpers_bond import coupon_amount, bond_description


def test_coupon_amount():
    bond_rate = 0.04
    amount = 100000
    expected = 4000.0
    actual = coupon_amount(bond_rate, amount)
    assert expected == actual


def test_bond_description():
    isin = "FR15"
    bond_rate = 0.04
    currency = "EUR"
    expected = "FR15_EUR_4.00%"
    actual = bond_description(isin, currency, bond_rate)
    assert expected == actual
