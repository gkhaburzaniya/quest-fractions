import unittest
import main


class TestAddition(unittest.TestCase):
    def test_one_plus_one(self):
        self.assertEqual(main.compute('1 + 1'), '2')

    def test_one_half_plus_one_half(self):
        self.assertEqual(main.compute('1/2 + 1/2'), '1')


if __name__ == '__main__':
    unittest.main()
