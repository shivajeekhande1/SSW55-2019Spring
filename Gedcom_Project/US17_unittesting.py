import unittest
import Gedcom_Project

class US17_test(unittest.TestCase):
    
    def test_One(self):
        Gedcom_Project.filepath = "GedcomFiles/AcceptanceTestFile.txt"
        Gedcom_Project.FirstCousinsNoMarriageChildren()
        errorDict = Gedcom_Project.error["US17"]["Family"]
        self.assertEqual(len(errorDict),3)

    def test_Two(self):
        Gedcom_Project.filepath = "GedcomFiles/AcceptanceTestFile.txt"
        self.assertFalse(Gedcom_Project.NoMarriageChildren())

     
if __name__ == '__main__':
    unittest.main()