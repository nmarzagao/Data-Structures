import unittest
from data_structures.calculate import Calculate

class TestCalculate(unittest.TestCase):
    def test_append(self):
        calc = Calculate()
        
        self.assertEqual(calc.sum(2, 2), 4)
        self.assertEqual(calc.sum(3, 3), 6)

if __name__ == '__main__':
    unittest.main()