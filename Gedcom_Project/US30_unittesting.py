import unittest

class Test_US30_unittesting(unittest.TestCase):
    def test_A(self):
        Gedcom_Project.ListLivingMarried()
        errorDict = Gedcom_Project.error["US30"]["IndividualIds"]
        self.assertEqual(len(errorDict),6)
    
    def test_B(self):
        self.assertTrue(Gedcom_Project.ListDeceased())

if __name__ == '__main__':
    unittest.main()
