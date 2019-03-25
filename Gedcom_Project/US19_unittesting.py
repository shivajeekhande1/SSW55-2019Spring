import unittest
import Gedcom_Project

class Test_test1(unittest.TestCase):
    
    def test_One(self):
        Gedcom_Project.filepath = "GedcomFiles/AcceptanceTestFile.txt"
        Gedcom_Project.FirstCousinsNoMarriageChildren()
        errorDict = Gedcom_Project.error["US19"]["Family"]
        self.assertEqual(len(errorDict),1)

    def test_Two(self):
        Gedcom_Project.filepath = "GedcomFiles/AcceptanceTestFile.txt"
        self.assertTrue(Gedcom_Project.FirstCousinsNoMarriageChildren())

     
if __name__ == '__main__':
    unittest.main()