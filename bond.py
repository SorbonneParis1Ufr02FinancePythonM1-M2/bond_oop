class Bond:
    """
    This class represents a bond product
    """

    def __init__(self):
        self.bond_name = None
        self.isin = None
        self.rate = 0
        self.currency = None
        self.face_value = 0

    def coupon_amount(self) -> float:
        """
        Compute the coupon amount.
        :return: the coupon amount
        """
        return self.rate * self.face_value

    def description(self) -> str:
        """
        return a string with the main characteristics
        :return: the description as isin_currency_rate%
        """
        if self.rate is None:
            return f"{self.isin}_{self.currency}"
        return f"{self.isin}_{self.currency}_{"{:.2%}".format(self.rate)}"


if __name__ == "__main__":
    bond = Bond()
    bond.isin = "FR15"
    bond.rate = 0.04
    bond.currency = "EUR"
    bond.face_value = 100000

    print(bond.isin)
    print(bond.rate)
    print(bond.currency)
    print(bond.face_value)
    print(bond.coupon_amount())
    print(bond.description())
    assert bond.coupon_amount() == 4000.0
    assert bond.description() == "FR15_EUR_4.00%"
