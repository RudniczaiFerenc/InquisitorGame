import unittest


class MyTestCase(unittest.TestCase):

    def test_something(self):
        self.assertEqual(True, True)

    def test_myTest(self):
        self.assertEquals(False, False)


if __name__ == '__main__':
    unittest.main()
