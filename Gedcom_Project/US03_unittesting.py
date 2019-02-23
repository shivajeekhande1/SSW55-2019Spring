import unittest
import Gedcom_Project

class Test_test1(unittest.TestCase):
    
    def test_One(self):
        Gedcom_Project.filepath = "GedcomFiles/SunilUS03TestFile.txt"
        Gedcom_Project.BirthBeforeDeath()
        errorDict = Gedcom_Project.error["US03"]["IndividualIds"]
        self.assertEqual(len(errorDict),1)

    def test_Two(self):
        Gedcom_Project.filepath = "GedcomFiles/SunilUS03TestFile.txt"
        self.assertFalse(Gedcom_Project.BirthBeforeDeath())

    def test_Three(self):
        Gedcom_Project.filepath = "GedcomFiles/SunilUS03TestFile.txt"
        Gedcom_Project.BirthBeforeDeath()
        errorDict=Gedcom_Project.error["US03"]["IndividualIds"]
        self.assertIsInstance(errorDict,list)
    
    def test_Four(self):
        Gedcom_Project.filepath = "GedcomFiles/SunilUS03TestFile.txt"
        Gedcom_Project.BirthBeforeDeath()
        errorDict = Gedcom_Project.error["US03"]["IndividualIds"]
        self.assertIn("I01",errorDict) #check if Individual I01 in the error dictionary
    
    def test_Five(self):
        Gedcom_Project.filepath = "GedcomFiles/SunilUS03TestFile.txt"
        self.assertIs(Gedcom_Project.BirthBeforeDeath(),False) #check if the return type is same and value is also same
     
if __name__ == '__main__':
    unittest.main()
