import unittest
from itertools import filterfalse


def exactly_one_false_val_using_all(iterable):
    i = iter(iterable)
    return not all(i) and all(i)

def exactly_one_false_val_using_filterfalse(iterable):
    return len(list(filterfalse(None, iterable))) == 1


class UsingAllTestCase(unittest.TestCase):

    def test_empty(self):
        lst = []
        self.assertFalse(exactly_one_false_val_using_all(lst))

    def test_single_val_true(self):
        lst = [True]
        self.assertFalse(exactly_one_false_val_using_all(lst))

    def test_single_val_false(self):
        lst = [False]
        self.assertTrue(exactly_one_false_val_using_all(lst))

    def test_only_true_vals(self):
        lst = [True, True, True]
        self.assertFalse(exactly_one_false_val_using_all(lst))

    def test_only_false_vals(self):
        lst = [False, False, False]
        self.assertFalse(exactly_one_false_val_using_all(lst))

    def test_multiple_false_start_with_true(self):
        lst = [True, False, False]
        self.assertFalse(exactly_one_false_val_using_all(lst))

    def test_single_false_beginning(self):
        lst = [False, True, True]
        self.assertTrue(exactly_one_false_val_using_all(lst))

    def test_single_false_middle(self):
        lst = [True, False, True]
        self.assertTrue(exactly_one_false_val_using_all(lst))

    def test_single_false_end(self):
        lst = [True, True, False]
        self.assertTrue(exactly_one_false_val_using_all(lst))


class UsingFilterFalseTestCase(unittest.TestCase):

    def test_empty(self):
        lst = []
        self.assertFalse(exactly_one_false_val_using_filterfalse(lst))

    def test_single_val_true(self):
        lst = [True]
        self.assertFalse(exactly_one_false_val_using_filterfalse(lst))

    def test_single_val_false(self):
        lst = [False]
        self.assertTrue(exactly_one_false_val_using_filterfalse(lst))

    def test_only_true_vals(self):
        lst = [True, True, True]
        self.assertFalse(exactly_one_false_val_using_filterfalse(lst))

    def test_only_false_vals(self):
        lst = [False, False, False]
        self.assertFalse(exactly_one_false_val_using_filterfalse(lst))

    def test_multiple_false_start_with_true(self):
        lst = [True, False, False]
        self.assertFalse(exactly_one_false_val_using_filterfalse(lst))

    def test_single_false_beginning(self):
        lst = [False, True, True]
        self.assertTrue(exactly_one_false_val_using_filterfalse(lst))

    def test_single_false_middle(self):
        lst = [True, False, True]
        self.assertTrue(exactly_one_false_val_using_filterfalse(lst))

    def test_single_false_end(self):
        lst = [True, True, False]
        self.assertTrue(exactly_one_false_val_using_filterfalse(lst))


if __name__ == '__main__':
    unittest.main()
