import math
import unittest

# Task 1: 
def calculate_packs_based_on_days(days):
    return math.ceil(days / 50)

# Task 2: 
def calculate_packs_based_on_weight(weight, days):
    daily_dose = (weight * 10) / 250
    daily_dose = round(daily_dose, 1)
    packs_required = math.ceil((daily_dose * days * 2) / 50)
    return daily_dose, packs_required

# Task 3: 
def calculate_packs_with_dosage(dose, weight, days):
    if dose not in [10, 15]:
        raise ValueError("Суточная дозировка должна быть 10 или 15 мг/кг")
    daily_dose = (weight * dose) / 250
    daily_dose = round(daily_dose, 1)
    packs_required = math.ceil((daily_dose * days * 2) / 50)
    return daily_dose, packs_required

# Task 4:
def analyze_and_calculate(result_analysis, dose, weight, days):
    alt = None
    ast = None
    for line in result_analysis.split("\\n"):
        if line.startswith("АЛТ"):
            alt = int(line.split("-")[1].strip())
        elif line.startswith("АСТ"):
            ast = int(line.split("-")[1].strip())
    
    if alt is None or ast is None:
        raise ValueError("Некорректный формат анализов")

    daily_dose, packs_required = calculate_packs_with_dosage(dose, weight, days)
    return alt, ast, daily_dose, packs_required


class TestMedicationCalculations(unittest.TestCase):

    def test_calculate_packs_based_on_days(self):
        self.assertEqual(calculate_packs_based_on_days(1), 1)
        self.assertEqual(calculate_packs_based_on_days(50), 1)
        self.assertEqual(calculate_packs_based_on_days(51), 2)
        self.assertEqual(calculate_packs_based_on_days(100), 2)
        self.assertEqual(calculate_packs_based_on_days(101), 3)

    def test_calculate_packs_based_on_weight(self):
        self.assertEqual(calculate_packs_based_on_weight(50, 1), (2.0, 1))
        self.assertEqual(calculate_packs_based_on_weight(70, 10), (2.8, 2))
        self.assertEqual(calculate_packs_based_on_weight(80, 5), (3.2, 1))
        self.assertEqual(calculate_packs_based_on_weight(60, 15), (2.4, 2))

    def test_calculate_packs_with_dosage(self):
        self.assertEqual(calculate_packs_with_dosage(10, 50, 1), (2.0, 1))
        self.assertEqual(calculate_packs_with_dosage(15, 70, 10), (4.2, 2))
        self.assertEqual(calculate_packs_with_dosage(10, 80, 5), (3.2, 1))
        with self.assertRaises(ValueError):
            calculate_packs_with_dosage(20, 50, 1)

    def test_analyze_and_calculate(self):
        self.assertEqual(analyze_and_calculate("АЛТ-45\\nАСТ-30", 10, 50, 1), (45, 30, 2.0, 1))
        self.assertEqual(analyze_and_calculate("АЛТ-60\\nАСТ-40", 15, 70, 10), (60, 40, 4.2, 2))
        self.assertEqual(analyze_and_calculate("АЛТ-50\\nАСТ-35", 10, 80, 5), (50, 35, 3.2, 1))
        with self.assertRaises(ValueError):
            analyze_and_calculate("АЛТ-80\\nАСТ-60", 20, 50, 1)


if __name__ == "__main__":
    unittest.main()
