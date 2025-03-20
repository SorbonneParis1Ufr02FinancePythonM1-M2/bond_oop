from helpers_bond import coupon_amount, bond_description


def add_bonds_properties(raw_data, config):
    results = raw_data.copy()
    fields = config['bonds_fields']
    for isin, b in results.items():
        isin = row[fields["isin"]]
        rate = row[fields["rate"]]
        currency = row[fields["currency"]]
        value = row[fields["face_value"]]
        coupon = coupon_amount(rate, value)
        description = bond_description(isin, currency, rate)
        row[fields["coupon"]] = coupon
        row[fields["description"]] = description
    return results


if __name__ == "__main__":
    data = [
        {"code": "US1234567890", "rate": 0.12, "currency": "USD", "value": 150},
        {"code": "US9876543210", "rate": 0.08, "currency": "EUR", "value": 999},
    ]
    print(f"id(data)={id(data)}")
    results = add_bonds_properties(data)
    print(f"id(results)={id(results)}")
    print(results)
