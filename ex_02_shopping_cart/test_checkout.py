from unittest import TestCase
from parameterizedtestcase import ParameterizedTestMixin
import checkout


class TestCheckout(ParameterizedTestMixin, TestCase):
    @ParameterizedTestMixin.parameterize(
        ("items", "expected_total"),
        [
            ([('1.00', 1)], '1.00'),
            ([('1.00', 2)], '2.00'),
            ([('1.00', 1), ('1.00', 1)], '2.00'),
            ([('100.00', 1)], '100.00'),
        ]
    )
    def test_items_without_discounts(self, items, expected_total):
        self.assertEqual(checkout.get_total(items), expected_total)

    @ParameterizedTestMixin.parameterize(
        ("items", "expected_total"),
        [
            ([('100.01', 1)], '95.01'),
            ([('120.00', 1)], '114.00'),
            ([('200.00', 1)], '190.00'),
        ]
    )
    def test_5_percent_discount_for_orders_over_100_pounds(
        self,
        items,
        expected_total
    ):
        self.assertEqual(checkout.get_total(items), expected_total)

    @ParameterizedTestMixin.parameterize(
        ("items", "expected_total"),
        [
            ([('300.00', 1)], '270.00'),
            ([('200.01', 1)], '180.01'),
        ]
    )
    def test_10_percent_discount_for_orders_over_200_pounds(
        self,
        items,
        expected_total
    ):
        self.assertEqual(checkout.get_total(items), expected_total)
