import unittest
import Gedcom_Project

class TestUS05_test1(unittest.TestCase):
    
    def test_A(self):
        Gedcom_Project.filepath = "GedcomFiles/SunilUS05TestFile.txt"
        Gedcom_Project.MarriageBeforeDeath()
        errorDict = Gedcom_Project.error["US05"]["IndividualIds"]
        self.assertEqual(len(errorDict),2)

    def test_Two(self):
        Gedcom_Project.filepath = "GedcomFiles/SunilUS05TestFile.txt"
        self.assertFalse(Gedcom_Project.MarriageBeforeDeath())

    def test_Three(self):
        Gedcom_Project.filepath = "GedcomFiles/SunilUS05TestFile.txt"
        Gedcom_Project.MarriageBeforeDeath()
        errorDict=Gedcom_Project.error["US05"]["IndividualIds"]
        self.assertIsInstance(errorDict,list)
    
    def test_Four(self):
        Gedcom_Project.filepath = "GedcomFiles/SunilUS05TestFile.txt"
        Gedcom_Project.MarriageBeforeDeath()
        errorDict = Gedcom_Project.error["US05"]["IndividualIds"]
        self.assertIn("I08",errorDict[1]) #check if Individual I08 in the error dictionary
    
    def test_Five(self):
        Gedcom_Project.filepath = "GedcomFiles/SunilUS05TestFile.txt"
        self.assertIs(Gedcom_Project.MarriageBeforeDeath(),False) #check if the return type is same and value is also same
     
if __name__ == '__main__':
    unittest.main()
