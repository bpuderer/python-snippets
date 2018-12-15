import unittest
from datetime import date
from freezegun import freeze_time
from broadcast_cal_utils import *


class BroadcastCalUtilsTestCase(unittest.TestCase):

    def test_broadcast_week_start(self):
        # saturday
        self.assertEqual(broadcast_week_start(date(2018, 12, 15)), date(2018, 12, 10))
        # monday
        self.assertEqual(broadcast_week_start(date(2018, 12, 17)), date(2018, 12, 17))

    def test_broadcast_month_start(self):
        # first lands on sunday
        self.assertEqual(broadcast_month_start(2018, 12), date(2018, 11, 26))
        # first lands on monday
        self.assertEqual(broadcast_month_start(2018, 10), date(2018, 10, 1))

    def test_quarter_start_month(self):
        self.assertEqual(quarter_start_month(3), 7)
        with self.assertRaisesRegex(ValueError, 'invalid quarter'):
            quarter_start_month(5)

    def test_quarter_for_month(self):
        self.assertEqual(quarter_for_month(10), 4)
        with self.assertRaisesRegex(ValueError, 'invalid month'):
            quarter_for_month(13)

    def test_next_quarter(self):
        self.assertEqual(next_quarter(2018, 1), (2018, 2))
        self.assertEqual(next_quarter(2018, 2, num=2), (2018, 4))
        self.assertEqual(next_quarter(2018, 2, num=8), (2020, 2))
        self.assertEqual(next_quarter(2018, 2, num=-2), (2017, 4))
        with self.assertRaisesRegex(ValueError, 'invalid quarter'):
            next_quarter(2018, 5)

    def test_broadcast_quarter_dates(self):
        self.assertEqual(broadcast_quarter_dates(2019, 1),
                         (date(2018, 12, 31), date(2019, 3, 31)))
        self.assertEqual(broadcast_quarter_dates(2019, 1, num=5),
                         (date(2018, 12, 31), date(2020, 3, 29)))
        self.assertEqual(broadcast_quarter_dates(2019, 1, num=5, start_offset=3, end_offset=-5),
                         (date(2019, 1, 3), date(2020, 3, 24)))
        with self.assertRaisesRegex(ValueError, 'num must be >= 1'):
            broadcast_quarter_dates(2019, 1, num=-2)

    def test_next_quarter_broadcast_dates(self):
        # on beginning of quarter
        with freeze_time('2018-12-31'):
            self.assertEqual(next_quarter_broadcast_dates(),
                             (date(2019, 4, 1), date(2019, 6, 30)))

        # day before beginning of quarter
        with freeze_time('2018-12-30'):
            self.assertEqual(next_quarter_broadcast_dates(),
                             (date(2018, 12, 31), date(2019, 3, 31)))
            self.assertEqual(next_quarter_broadcast_dates(num=3),
                             (date(2018, 12, 31), date(2019, 9, 29)))
            self.assertEqual(next_quarter_broadcast_dates(end_offset=3),
                             (date(2018, 12, 31), date(2019, 4, 3)))
            self.assertEqual(next_quarter_broadcast_dates(start_offset=3),
                             (date(2019, 1, 3), date(2019, 3, 31)))
            # *next* quarter with offset taken into account
            self.assertEqual(next_quarter_broadcast_dates(start_offset=-1),
                             (date(2019, 3, 31), date(2019, 6, 30)))

    def test_broadcast_week_starts(self):
        self.assertEqual(broadcast_week_starts(date(2018, 12, 15), date(2018, 12, 14)), [])
        self.assertEqual(broadcast_week_starts(date(2018, 12, 15), date(2018, 12, 15)),
                         [date(2018, 12, 10)])
        self.assertEqual(broadcast_week_starts(date(2018, 12, 10), date(2018, 12, 10)),
                         [date(2018, 12, 10)])
        self.assertEqual(broadcast_week_starts(date(2018, 12, 10), date(2018, 12, 18)),
                         [date(2018, 12, 10), date(2018, 12, 17)])

    def test_broadcast_weeks(self):
        self.assertEqual(broadcast_weeks(date(2018, 12, 15), date(2018, 12, 14)), [])
        self.assertEqual(broadcast_weeks(date(2018, 12, 15), date(2018, 12, 15)),
                         [(date(2018, 12, 10), date(2018, 12, 16))])
        self.assertEqual(broadcast_weeks(date(2018, 12, 10), date(2018, 12, 10)),
                         [(date(2018, 12, 10), date(2018, 12, 16))])
        self.assertEqual(broadcast_weeks(date(2018, 12, 10), date(2018, 12, 18)),
                         [(date(2018, 12, 10), date(2018, 12, 16)),
                          (date(2018, 12, 17), date(2018, 12, 23))])


if __name__ == '__main__':
    unittest.main()
