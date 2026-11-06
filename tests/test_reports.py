import unittest
from features import reports


class TestAverageScore(unittest.TestCase):
    def test_empty_history_is_zero(self):
        self.assertEqual(reports.average_score({"history": []}), 0.0)

    def test_one_score(self):
        self.assertEqual(reports.average_score({"history": [8]}), 8.0)

    def test_several_scores(self):
        self.assertEqual(reports.average_score({"history": [5, 6, 4]}), 5.0)

    def test_rounds_to_one_decimal(self):
        self.assertEqual(reports.average_score({"history": [1, 2, 2]}), 1.7)