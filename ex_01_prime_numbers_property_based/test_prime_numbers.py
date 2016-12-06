from unittest import TestCase

from hypothesis import assume, given
from hypothesis import strategies

from .prime_numbers import prime_numbers

PRIMES = prime_numbers()


class TestPrimeNumbers(TestCase):
    def test_can_access_members_via_index(self):
        prime_numbers()[0]

    @given(strategies.sampled_from(PRIMES))
    def test_are_integers(self, prime):
        self.assertEqual(prime % 1, 0)

    @given(strategies.integers(1, len(PRIMES) - 1))
    def test_increase_in_size(self, index):
        self.assertGreater(PRIMES[index], PRIMES[index-1])

    @given(strategies.sampled_from(PRIMES))
    def test_only_one_and_itself_are_factors(self, prime):
        factors = [i for i in range(1, prime + 1) if prime % i == 0]
        self.assertEqual(factors, [1, prime])

    def test_primes_upto_1000_given(self):
        self.assertEqual(PRIMES[-1], 997)
