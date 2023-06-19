"""
Sample tests
"""

from django.test import SimpleTestCase

from app import calc


class CalcTests(SimpleTestCase):
    """Test the calc module"""

    def test_add_numbers(self):
        """test adding numbers together"""

        res = calc.add(5, 6)

        self.assertEquals(res, 11)

    def test_subtract_numbers(self):
        """Testing subtracting numbers"""

        res = calc.subtract(8, 4)

        self.assertEquals(res, 4)
