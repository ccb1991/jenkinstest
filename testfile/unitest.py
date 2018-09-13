import unittest
#
# list = [1, 2, 3, 4, 5]
# listtwo = ["1", "2", "3", "4"]

class TestStringMethods(unittest.TestCase):
    # def __init__(self):
    #     self.list = [1, 2, 3, 4, 5]
    #     self.listtwo = ["1", "2", "3", "4"]

    def test_compare_list(self):
        self.assertListEqual([1, 2, 3, 4, 5],["1", "2", "3", "4"])

    def test_add(self):
        self.assertEqual(3,3)

    # _*_ coding:utf-8 _*_


class demoTest(unittest.TestCase):
    def test1(self):
        self.assertEqual(4 + 5, 9)

    def test2(self):
        self.assertNotEqual(5 * 2, 10)

    def test3(self):
        self.assertTrue(4 + 5 == 9, "The result is False")

    def test4(self):
        self.assertTrue(4 + 5 == 10, "assertion fails")

    def test5(self):
        self.assertIn([3,4], [1, 2, [3,4]])

    def test6(self):
        self.assertNotIn(3, range(5))
