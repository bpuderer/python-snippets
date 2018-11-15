import unittest
from datetime import datetime
from datetime_utils import Range, overlap_days, ranges_overlap, in_range, all_in_range


class OverlapDaysTestCase(unittest.TestCase):

    def test_adjacent(self):
        r1 = Range(start=datetime(2018, 1, 1), end=datetime(2018, 1, 10))
        r2 = Range(start=datetime(2018, 1, 11), end=datetime(2018, 1, 30))
        self.assertEqual(overlap_days(r1, r2), 0)
        self.assertEqual(overlap_days(r2, r1), 0)

    def test_gap(self):
        r1 = Range(start=datetime(2018, 1, 1), end=datetime(2018, 1, 10))
        r2 = Range(start=datetime(2018, 1, 20), end=datetime(2018, 1, 30))
        self.assertEqual(overlap_days(r1, r2), 0)
        self.assertEqual(overlap_days(r2, r1), 0)

    def test_overlap_same(self):
        r1 = Range(start=datetime(2018, 1, 1), end=datetime(2018, 1, 10))
        self.assertEqual(overlap_days(r1, r1), 10)

    def test_overlap_boundary(self):
        r1 = Range(start=datetime(2018, 1, 1), end=datetime(2018, 1, 10))
        r2 = Range(start=datetime(2018, 1, 10), end=datetime(2018, 1, 20))
        self.assertEqual(overlap_days(r1, r2), 1)
        self.assertEqual(overlap_days(r2, r1), 1)

    def test_some_overlap(self):
        r1 = Range(start=datetime(2018, 1, 1), end=datetime(2018, 1, 10))
        r2 = Range(start=datetime(2018, 1, 5), end=datetime(2018, 1, 20))
        self.assertEqual(overlap_days(r1, r2), 6)
        self.assertEqual(overlap_days(r2, r1), 6)

    def test_contains(self):
        r1 = Range(start=datetime(2018, 1, 1), end=datetime(2018, 1, 20))
        r2 = Range(start=datetime(2018, 1, 5), end=datetime(2018, 1, 12))
        self.assertEqual(overlap_days(r1, r2), 8)
        self.assertEqual(overlap_days(r2, r1), 8)

    def test_several_no_overlap(self):
        r1 = Range(start=datetime(2018, 1, 11), end=datetime(2018, 1, 13))
        r2 = Range(start=datetime(2018, 1, 1), end=datetime(2018, 1, 3))
        r3 = Range(start=datetime(2018, 1, 7), end=datetime(2018, 1, 9))
        r4 = Range(start=datetime(2018, 1, 20), end=datetime(2018, 1, 25))
        r5 = Range(start=datetime(2018, 1, 15), end=datetime(2018, 1, 19))
        self.assertFalse(ranges_overlap([r1, r2, r3, r4, r5]))

    def test_several_with_overlap(self):
        r1 = Range(start=datetime(2018, 1, 11), end=datetime(2018, 1, 13))
        r2 = Range(start=datetime(2018, 1, 1), end=datetime(2018, 1, 3))
        r3 = Range(start=datetime(2018, 1, 15), end=datetime(2018, 1, 22))
        r4 = Range(start=datetime(2018, 1, 20), end=datetime(2018, 1, 25))
        r5 = Range(start=datetime(2018, 1, 15), end=datetime(2018, 1, 19))
        self.assertTrue(ranges_overlap([r1, r2, r3, r4, r5]))


class InRangeTestCase(unittest.TestCase):

    def test_in_range_outside(self):
        r1 = Range(start=datetime(2018, 1, 11), end=datetime(2018, 1, 13))
        r2_1 = Range(start=datetime(2018, 1, 1), end=datetime(2018, 1, 5))
        r2_2 = Range(start=datetime(2018, 1, 15), end=datetime(2018, 1, 20))
        self.assertFalse(in_range(r1, r2_1))
        self.assertFalse(in_range(r1, r2_2))

    def test_in_range_some_overlap(self):
        r1 = Range(start=datetime(2018, 1, 10), end=datetime(2018, 1, 15))
        r2_1 = Range(start=datetime(2018, 1, 1), end=datetime(2018, 1, 10))
        r2_2 = Range(start=datetime(2018, 1, 15), end=datetime(2018, 1, 20))
        r2_3 = Range(start=datetime(2018, 1, 5), end=datetime(2018, 1, 14))
        r2_4 = Range(start=datetime(2018, 1, 12), end=datetime(2018, 1, 20))
        r2_5 = Range(start=datetime(2018, 1, 12), end=datetime(2018, 1, 14))
        self.assertFalse(in_range(r1, r2_1))
        self.assertFalse(in_range(r1, r2_2))
        self.assertFalse(in_range(r1, r2_3))
        self.assertFalse(in_range(r1, r2_4))
        self.assertFalse(in_range(r1, r2_5))

    def test_in_range(self):
        r1 = Range(start=datetime(2018, 1, 10), end=datetime(2018, 1, 15))
        r2_1 = Range(start=datetime(2018, 1, 5), end=datetime(2018, 1, 20))
        r2_2 = Range(start=datetime(2018, 1, 5), end=datetime(2018, 1, 15))
        r2_3 = Range(start=datetime(2018, 1, 10), end=datetime(2018, 1, 20))
        self.assertTrue(in_range(r1, r1))
        self.assertTrue(in_range(r1, r2_1))
        self.assertTrue(in_range(r1, r2_2))
        self.assertTrue(in_range(r1, r2_3))

    def test_all_in_range(self):
        r1_1 = Range(start=datetime(2018, 1, 10), end=datetime(2018, 1, 15))
        r1_2 = Range(start=datetime(2018, 1, 10), end=datetime(2018, 1, 12))
        r1_3 = Range(start=datetime(2018, 1, 12), end=datetime(2018, 1, 15))
        r1_4 = Range(start=datetime(2018, 1, 11), end=datetime(2018, 1, 14))
        r2 = Range(start=datetime(2018, 1, 10), end=datetime(2018, 1, 15))
        self.assertTrue(all_in_range([r1_1, r1_2, r1_3, r1_4], r2))

    def test_not_all_in_range(self):
        r1_1 = Range(start=datetime(2018, 1, 10), end=datetime(2018, 1, 15))
        r1_2 = Range(start=datetime(2018, 1, 10), end=datetime(2018, 1, 12))
        r1_3 = Range(start=datetime(2018, 1, 12), end=datetime(2018, 1, 16))
        r1_4 = Range(start=datetime(2018, 1, 11), end=datetime(2018, 1, 14))
        r2 = Range(start=datetime(2018, 1, 10), end=datetime(2018, 1, 15))
        self.assertFalse(all_in_range([r1_1, r1_2, r1_3, r1_4], r2))

if __name__ == '__main__':
    unittest.main()
