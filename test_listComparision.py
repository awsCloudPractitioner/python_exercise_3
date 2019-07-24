import unittest
from listcontainsall import ListComparision


class TestListComparision(unittest.TestCase):

    def test_has_common_elements(self):
        test_instance = ListComparision()
        # positive tests
        self.assertTrue(test_instance.has_common_elements([10, 20, 30, 40], [10, 20, 30, 40]))
        self.assertTrue(test_instance.has_common_elements(['abc', 'def', 'ghi', 'jkl', 'mno'], ['jkl']))
        self.assertTrue(test_instance.has_common_elements([1.1, 2.2, 3.3, 4.4], [4.4, 3.3]))

        # negative tests
        self.assertFalse(test_instance.has_common_elements(['we', 'you', 'us'], ['ours', 'theirs']))


if __name__ == '__main__':
    unittest.main()
