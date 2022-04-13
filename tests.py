import unittest
from fractions import Fraction

import main


class TestParseNum(unittest.TestCase):
    def test_one(self):
        self.assertEqual(main.parse_num('1'), Fraction(1, 1))

    def test_one_third(self):
        self.assertEqual(main.parse_num('1/3'), Fraction(1, 3))

    def test_two_thirds(self):
        self.assertEqual(main.parse_num('2/3'), Fraction(2, 3))

    def test_negative_one(self):
        self.assertEqual(main.parse_num('-1'), Fraction(-1, 1))

    def test_negative_one_third(self):
        self.assertEqual(main.parse_num('-1/3'), Fraction(-1, 3))

    def test_negative_one_and_two_thirds(self):
        self.assertEqual(main.parse_num('-1_2/3'), Fraction(-5, 3))

    def test_two_and_one_third(self):
        self.assertEqual(main.parse_num('2_2/3'), Fraction(8, 3))

    def test_bad_fraction(self):
        self.assertRaises(ZeroDivisionError, main.parse_num, '1_1/0')


class TestFormatAnswer(unittest.TestCase):
    def test_zero(self):
        self.assertEqual(main.format_answer(Fraction(0, 1)), '0')

    def test_one(self):
        self.assertEqual(main.format_answer(Fraction(1, 1)), '1')

    def test_one_third(self):
        self.assertEqual(main.format_answer(Fraction(1, 3)), '1/3')

    def test_one_and_one_third(self):
        self.assertEqual(main.format_answer(Fraction(4, 3)), '1_1/3')

    def test_negative_one(self):
        self.assertEqual(main.format_answer(Fraction(-1, 1)), '-1')

    def test_negative_one_third(self):
        self.assertEqual(main.format_answer(Fraction(-1, 3)), '-1/3')

    def test_negative_one_and_one_third(self):
        self.assertEqual(main.format_answer(Fraction(-4, 3)), '-1_1/3')


class TestAddition(unittest.TestCase):
    def test_one_plus_one(self):
        self.assertEqual(main.compute('1 + 1'), '2')

    def test_one_third_plus_two_thirds(self):
        self.assertEqual(main.compute('1/3 + 2/3'), '1')

    def test_one_half_plus_one_third(self):
        self.assertEqual(main.compute('1/2 + 1/3'), '5/6')

    def test_one_half_plus_two_thirds(self):
        self.assertEqual(main.compute('1/2 + 2/3'), '1_1/6')

    def test_zero_plus_zero(self):
        self.assertEqual(main.compute('0 + 0'), '0')

    def test_negative_one_plus_one_third(self):
        self.assertEqual(main.compute('-1 + 1/3'), '-2/3')

    def test_negative_two_plus_one_third(self):
        self.assertEqual(main.compute('-2 + 1/3'), '-1_2/3')

    def test_two_and_three_eights_plus_nine_eights(self):
        self.assertEqual(main.compute('2_3/8 + 9/8'), '3_1/2')


class TestSubtraction(unittest.TestCase):
    def test_one_minus_one(self):
        self.assertEqual(main.compute('1 - 1'), '0')

    def test_one_third_minus_two_thirds(self):
        self.assertEqual(main.compute('1/3 - 2/3'), '-1/3')

    def test_one_half_minus_one_third(self):
        self.assertEqual(main.compute('1/2 - 1/3'), '1/6')

    def test_one_half_minus_two_thirds(self):
        self.assertEqual(main.compute('1/2 - 2/3'), '-1/6')

    def test_zero_minus_zero(self):
        self.assertEqual(main.compute('0 - 0'), '0')

    def test_negative_one_minus_one_third(self):
        self.assertEqual(main.compute('-1 - 1/3'), '-1_1/3')

    def test_negative_two_minus_one_third(self):
        self.assertEqual(main.compute('-2 - 1/3'), '-2_1/3')

    def test_two_and_three_eights_minus_nine_eights(self):
        self.assertEqual(main.compute('2_3/8 - 9/8'), '1_1/4')


class TestMultiplication(unittest.TestCase):
    def test_one_times_one(self):
        self.assertEqual(main.compute('1 * 1'), '1')

    def test_one_third_times_two_thirds(self):
        self.assertEqual(main.compute('1/3 * 2/3'), '2/9')

    def test_one_half_times_one_third(self):
        self.assertEqual(main.compute('1/2 * 1/3'), '1/6')

    def test_one_half_times_two_thirds(self):
        self.assertEqual(main.compute('1/2 * 2/3'), '1/3')

    def test_zero_times_zero(self):
        self.assertEqual(main.compute('0 * 0'), '0')

    def test_one_times_zero(self):
        self.assertEqual(main.compute('1 * 0'), '0')

    def test_negative_one_times_one_third(self):
        self.assertEqual(main.compute('-1 * 1/3'), '-1/3')

    def test_negative_two_times_one_third(self):
        self.assertEqual(main.compute('-2 * 1/3'), '-2/3')

    def test_one_half_times_three_and_three_quarters(self):
        self.assertEqual(main.compute('1/2 * 3_3/4'), '1_7/8')


class TestDivision(unittest.TestCase):
    def test_one_over_one(self):
        self.assertEqual(main.compute('1 / 1'), '1')

    def test_one_third_over_two_thirds(self):
        self.assertEqual(main.compute('1/3 / 2/3'), '1/2')

    def test_one_half_over_one_third(self):
        self.assertEqual(main.compute('1/2 / 1/3'), '1_1/2')

    def test_one_half_over_two_thirds(self):
        self.assertEqual(main.compute('1/2 / 2/3'), '3/4')

    def test_zero_over_zero(self):
        self.assertRaises(ZeroDivisionError, main.compute, '0 / 0')

    def test_one_over_zero(self):
        self.assertRaises(ZeroDivisionError, main.compute, '1 / 0')

    def test_zero_over_one(self):
        self.assertEqual(main.compute('0 / 1'), '0')

    def test_negative_one_over_one_third(self):
        self.assertEqual(main.compute('-1 / 1/3'), '-3')

    def test_negative_two_over_one_third(self):
        self.assertEqual(main.compute('-2 / 1/3'), '-6')

    def test_one_half_over_three_and_three_quarters(self):
        self.assertEqual(main.compute('1/2 / 3_3/4'), '2/15')


if __name__ == '__main__':
    unittest.main()
