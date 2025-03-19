def coupon_amount(rate: float, face_value: int) -> float:
    """
    Compute the coupon amount.
    :return: the coupon amount
    """
    return rate * face_value


def bond_description(isin: str, currency_name: str, rate: float) -> str:
    """
    return a string with the main characteristics
    :return: the description as isin_currency_rate%
    """
    if rate is None:
        return f"{isin}_{currency_name}"
    return f"{isin}_{currency_name}_{"{:.2%}".format(rate)}"


if __name__ == "__main__":
    isin = "FR15"
    rate = 0.04
    currency_name = "EUR"
    face_value = 100000

    print(coupon_amount(rate, face_value))
    print(bond_description(isin, currency_name, rate))

    assert coupon_amount(rate, face_value) == 4000.0
    assert bond_description(isin, currency_name, rate) == "FR15_EUR_4.00%"
