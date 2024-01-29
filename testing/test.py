import unittest
import main


class TestMain(unittest.TestCase):
    def setUp(self):
        print('About to test a function')

    def test_do_stuff(self):
        t_param = 10
        result = main.do_stuff(t_param)
        self.assertEqual(result, 11)

    def test_do_stuff2(self):
        t_param = 'test'
        result = main.do_stuff(t_param)
        self.assertIsInstance(result, ValueError)

    def test_do_stuff3(self):
        t_param = None
        result = main.do_stuff(t_param)
        self.assertEqual(result, 'Please enter number')

    def test_do_stuff4(self):
        t_param = ''
        result = main.do_stuff(t_param)
        self.assertEqual(result, 'Please enter number')

    def tearDown(self):
        print('Cleaning up')


if __name__ == '__main__':
    unittest.main()
