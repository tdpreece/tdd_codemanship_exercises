from copy import copy
from decimal import Decimal


def get_total(items):
    total = sum(Decimal(price) * quantity for price, quantity in items)
    if total > Decimal('200.00'):
        discount = total * Decimal('0.10')
        total -= discount
    elif total > Decimal('100.00'):
        discount = total * Decimal('0.05')
        total -= discount
    return str(get_to_nearest_penny(total))


def get_to_nearest_penny(amount_in_pounds):
    number_decimal_places = 2
    q = Decimal(10) ** -number_decimal_places
    amount_to_nearest_penny = copy(amount_in_pounds).quantize(q)
    return amount_to_nearest_penny
