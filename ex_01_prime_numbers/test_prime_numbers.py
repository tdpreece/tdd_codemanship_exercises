from parameterizedtestcase import ParameterizedTestCase

from .prime_numbers import prime_numbers


class TestPrimeNumbers(ParameterizedTestCase):
    def test_first_prime_is_2(self):
        self.assertEqual(prime_numbers()[0], 2)

    def test_second_prime_is_greater_than_first(self):
        self.assertGreater(prime_numbers()[1], prime_numbers()[0])

    @ParameterizedTestCase.parameterize(
            ('factor', 'index_of_prime'),
            [
                (2, 1),
                (2, 3),
                (3, 4),
                (5, 8),
            ]
    )
    def test_not_a_factor_of_prime(self, factor, index_of_prime):
        prime = prime_numbers()[index_of_prime]
        self.assertNotEqual(
            prime % factor,
            0,
            msg='{} is a factor of {}'.format(factor, prime)
        )

    def test_last_prime_is_less_than_1000(self):
        prime = prime_numbers()[-1]
        self.assertLess(prime, 1000)


