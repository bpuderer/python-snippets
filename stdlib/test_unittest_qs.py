# python3 -m unittest -v
import unittest

class BasicTestCase(unittest.TestCase):

    # test fixtures

    @classmethod
    def setUpClass(cls):
        print('setUpClass ', end='')

    def setUp(self):
        print('setUp ', end='')

    def tearDown(self):
        print('tearDown ', end='')

    @classmethod
    def tearDownClass(cls):
        print('tearDownClass')



    def test_items(self):
        self.assertCountEqual([1, 2], [2, 1])


    def test_lists(self):
        # https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertEqual
        # type-specific equality function automatically called
        self.assertEqual([1, 2], [2, 1], msg='optional msg')


    def test_error_check(self):
        with self.assertRaises(TypeError):
            any(42)


    def test_error_check_message(self):
        with self.assertRaisesRegex(ValueError, 'ValueError msg'):
            raise ValueError('ValueError msg')


    def test_error_result(self):
        raise TypeError


    # also skipIf, skipUnless with conditions
    @unittest.skip('reason for skipping')
    def test_skip_decorator(self):
        self.fail('fail mid-test')


    def test_skip_during_test(self):
        self.skipTest('skip mid-test')


    @unittest.expectedFailure
    def test_expected_fail(self):
        self.fail()


    @unittest.expectedFailure
    def test_expected_failure_but_passes(self):
        # unexpected success
        pass


    def test_subtest(self):
        # test_input=4 will fail but test continues. notice stdout
        test_inputs = (5, 4, 3)
        expected_outputs = (2, 2, 0)

        # use of subTest allows compiling of failures...
        # instead of failing test after hitting first AssertionError
        # subTest(msg=None, **params)
        # counts as 1 test
        for test_input, expected in zip(test_inputs, expected_outputs):
            with self.subTest(test_input=test_input):
                print(f'testing test_input={test_input}', end=' ')
                self.assertEqual(test_input % 3, expected)
