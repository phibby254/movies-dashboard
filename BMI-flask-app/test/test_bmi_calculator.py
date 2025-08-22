import unittest
from src.utils import calculate_bmi, bmi_category

class TestBMICalculator(unittest.TestCase):

    def test_calculate_bmi(self):
        self.assertAlmostEqual(calculate_bmi(70, 1.75), 22.8571, places=4)
        self.assertAlmostEqual(calculate_bmi(50, 1.60), 19.5312, places=4)
        with self.assertRaises(ValueError):
            calculate_bmi(70, 0)  # height cannot be zero

    def test_bmi_category(self):
        self.assertEqual(bmi_category(17), "Underweight")
        self.assertEqual(bmi_category(22), "Normal weight")
        self.assertEqual(bmi_category(27), "Overweight")
        self.assertEqual(bmi_category(32), "Obesity")

if __name__ == "__main__":
    unittest.main()
