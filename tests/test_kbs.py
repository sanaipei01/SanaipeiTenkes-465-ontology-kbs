import unittest
from kbs import UniversityOntologyKBS

class TestUniversityKBS(unittest.TestCase):
    def setUp(self):
        self.kbs = UniversityOntologyKBS()
        self.kbs.add_course("Math")
        self.kbs.add_course("Stats")
        self.kbs.add_prerequisite("Stats", "Math")
        self.kbs.add_student("Kimani")

    def test_add_student(self):
        self.assertIn("Kimani", self.kbs.students)

    def test_complete_course(self):
        self.kbs.complete_course("Kimani", "Math")
        self.assertIn("Math", self.kbs.students["Kimani"])

    def test_eligible_logic(self):
        self.kbs.complete_course("Kimani", "Math")
        eligible, _ = self.kbs.can_take("Kimani", "Stats")
        self.assertTrue(eligible)

    def test_missing_prereqs(self):
        eligible, missing = self.kbs.can_take("Kimani", "Stats")
        self.assertFalse(eligible)
        self.assertIn("Math", missing)

    def test_recommendation_sorting(self):
        self.kbs.add_course("Alpha")
        self.kbs.add_student("Omondi")
        recs = self.kbs.recommend_courses("Omondi")
        self.assertEqual(recs, ["Alpha", "Math"]) # Sorted alphabetically

    def test_invalid_input_error(self):
        with self.assertRaises(ValueError):
            self.kbs.can_take("NonExistent", "Math")

if __name__ == "__main__":
    unittest.main()

