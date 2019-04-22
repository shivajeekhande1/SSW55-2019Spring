import unittest
import Gedcom_Project

class Test_US29_unittesting(unittest.TestCase):
    def test_A(self):
        Gedcom_Project.filepath = "GedcomFiles/AcceptanceTestFile.txt"
        Gedcom_Project.ListDeceased()
        errorDict = Gedcom_Project.error["US29"]["IndividualIds"]
        self.assertEqual(len(errorDict),11)
    
    def test_B(self):
        Gedcom_Project.filepath = "GedcomFiles/AcceptanceTestFile.txt"
        self.assertTrue(Gedcom_Project.ListDeceased())

if __name__ == '__main__':
    unittest.main()
