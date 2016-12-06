from decimal import Decimal


def get_total(items):
    total = sum(Decimal(price) * quantity for price, quantity in items)
    if total > 100:
        discount = total * Decimal('0.05')
        total -= discount
    number_decimal_places = 2
    q = Decimal(10) ** -number_decimal_places
    return str(total.quantize(q))
