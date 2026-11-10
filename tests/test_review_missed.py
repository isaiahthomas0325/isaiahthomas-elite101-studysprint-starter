import unittest
from features import core


class TestReviewMissed(unittest.TestCase):
    def test_returns_only_missed_cards(self):
        cards = [{"id": 1}, {"id": 2}, {"id": 3}]
        results = [True, False, True]
        self.assertEqual(core.review_missed(cards, results), [{"id": 2}])

    def test_nothing_missed_returns_empty_list(self):
        cards = [{"id": 1}, {"id": 2}]
        results = [True, True]
        self.assertEqual(core.review_missed(cards, results), [])

    def test_all_missed_returns_every_card(self):
        cards = [{"id": 1}, {"id": 2}]
        results = [False, False]
        self.assertEqual(core.review_missed(cards, results), cards)