# https://pyvideo.org/pycon-us-2011/pycon-2011--testing-with-mock.html
# https://www.youtube.com/watch?v=haXUaGTp8Bc&t=7m55s
import unittest
from unittest.mock import Mock, MagicMock, call, patch, ANY, mock_open

from work import work_on, Helper, Worker



def print_mock_data_descriptors(mock):
    print(f'call_args: {mock.call_args}')
    print(f'call_args_list: {mock.call_args_list}')
    print(f'call_count: {mock.call_count}')
    print(f'call_called: {mock.called}')
    print(f'method_calls: {mock.method_calls}')
    print(f'mock_calls: {mock.mock_calls}')
    print(f'return_value: {mock.return_value}')
    print(f'side_effect: {mock.side_effect}')
    print('-----')


class MockDemoTest(unittest.TestCase):

    def test_magic_mock_basics(self):
        # MagicMock implements default magic methods
        mock = MagicMock()
        mock.foo.assert_not_called()
        mock.foo(1, 2, key='val')
        print_mock_data_descriptors(mock.foo)
        mock.foo.assert_called()
        mock.foo.assert_called_once()
        mock.foo.assert_called_with(1, 2, key=ANY)
        mock.foo.assert_called_with(1, 2, key='val')
        mock.foo.assert_called_once_with(1, 2, key='val')
        mock.foo.reset_mock()
        mock.foo.assert_not_called()


    def test_magic_mock_any_has(self):
        mock = MagicMock()
        mock('egg')
        mock('bacon')
        mock('spam')

        mock.assert_any_call('bacon')

        calls = [call('bacon')]
        mock.assert_has_calls(calls)

        calls = [call('egg'), call('bacon'), call('spam')]
        mock.assert_has_calls(calls)

        calls = [call('spam'), call('bacon'), call('egg')]
        mock.assert_has_calls(calls, any_order=True)

        print_mock_data_descriptors(mock)


    def test_side_effect_func(self):
        mock = Mock(side_effect=lambda x: x*2)
        self.assertEqual(mock(4), 8)


    def test_side_effect_exception(self):
        mock = Mock(side_effect=KeyError('foo'))
        with self.assertRaises(KeyError):
            mock()


    def test_side_effect_iterable(self):
        mock = Mock(side_effect=[3, 2, 1])
        self.assertEqual(mock(), 3)
        self.assertEqual(mock(), 2)


    def test_return_value(self):
        mock = Mock(return_value=9)
        self.assertEqual(mock(), 9)


    def test_configure(self):
        mock = Mock()
        attrs = {'foo.return_value': 3, 'bar.side_effect': lambda x: x*2, 'spam': 'eggs'}
        mock.configure_mock(**attrs)
        self.assertEqual(mock.foo(), 3)
        self.assertEqual(mock.bar(4), 8)
        self.assertEqual(mock.spam, 'eggs')


    def test_mock_file(self):
        # example from:
        # https://docs.python.org/3/library/unittest.mock.html#mock-open
        with patch('__main__.open', mock_open(read_data='text in a file')) as m:
            with open('foo') as f:
                result = f.read()
        m.assert_called_once_with('foo')
        self.assertEqual(result, 'text in a file')


    # patch where name is being looked up...
    # replacing name in scope where it is being looked up
    # patch examples below from Yeray Diaz
    # https://medium.com/@yeraydiazdiaz/what-the-mock-cheatsheet-mocking-in-python-6a71db997832
    # https://github.com/yeraydiazdiaz/wtmock
    def test_patch_context(self):
        with patch('work.os.getcwd', return_value='testing'):
            self.assertEqual(work_on(), 'testing')


    @patch('work.Helper', autospec=True)
    # autospec=True - mock created with spec from the object being replaced
    def test_patch_class_decorator(self, MockHelper):
        # test: Worker calls Helper with "db"
        # test: Worker returns the expected path supplied by Helper
        # 'double' return_value since MagicMock returns another
        # MagicMock on calls to __init__
        # calling get_path on instance, not class
        MockHelper.return_value.get_path.return_value = 'testing'
        worker = Worker()
        MockHelper.assert_called_once_with('db')
        self.assertEqual(worker.work(), 'testing')


    def test_patch_partial_class(self):
        with patch.object(Helper, 'get_path', return_value='testing'):
            worker = Worker()
            self.assertEqual(worker.helper.path, 'db')
            self.assertEqual(worker.work(), 'testing')


if __name__ == '__main__':
    unittest.main()
