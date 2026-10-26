import unittest


def add_numbers(first, second):
    return first + second


def is_even(number):
    return number % 2 == 0


def apply_discount(price, percentage):
    return price - percentage


class TestBasicFunctions(unittest.TestCase):
    def test_add_numbers(self):
        # TODO: Test positive, zero, and negative inputs.
        pass

    def test_is_even(self):
        # TODO: Test both an even and an odd number.
        pass


class TestApplyDiscount(unittest.TestCase):
    def test_apply_discount(self):
        # TODO: Check that a 10% discount on 200 returns 180.
        # TODO: Check that a 0% discount leaves the price unchanged.
        pass


if __name__ == "__main__":
    unittest.main()
