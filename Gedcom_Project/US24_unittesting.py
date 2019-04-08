import unittest
import Gedcom_Project

class US24_test(unittest.TestCase):
    
    def test_One(self):
        Gedcom_Project.filepath = "GedcomFiles/AcceptanceTestFile.txt"
        Gedcom_Project.UniqueFamiliesSpouses()
        errorDict = Gedcom_Project.error["US24"]["Family id"]
        self.assertEqual(len(errorDict),1)

    def test_Two(self):
        Gedcom_Project.filepath = "GedcomFiles/AcceptanceTestFile.txt"
        self.assertFalse(Gedcom_Project.UniqueFamiliesSpouses())

     
if __name__ == '__main__':
    unittest.main()