import unittest

class CompareDataTest(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_data_number(self,OrginalNumber,TargetNumber):
        self.assertEqual(OrginalNumber,TargetNumber)

    def test_compare_data(self,OrginalData,TargetData):
        self.assertEqual(OrginalData,TargetData)

    def test_contain_data(self,OrginalData,TargetData):
        self.assertIn(OrginalData,TargetData)

"test"

