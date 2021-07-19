import unittest


class GameTestCase(unittest.TestCase):
    def setUp(self):
        mode = "unittest"

    def test_assert(self):
        self.assertEqual(1, 1)


if __name__ == "__main__":
    unittest.main()
