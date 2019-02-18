import unittest
import Gedcom_Project

class Test_test1(unittest.TestCase):
    
    def test_One(self):
        Gedcom_Project.filepath = "Venkata_Khande_SSE555_project01.txt"
        Gedcom_Project.BirthBeforeDeath()
        errorDict = Gedcom_Project.error["US03"]["IndividualIds"]
        self.assertEqual(len(errorDict),1)

    def test_Two(self):
        Gedcom_Project.filepath = "C:/Users/sunil/Downloads/Sunilkumar_Project#2/SampleTestFile.ged"
        self.assertFalse(Gedcom_Project.BirthBeforeDeath())

    def test_Three(self):
        Gedcom_Project.filepath = "C:/Users/sunil/Downloads/Sunilkumar_Project#2/SampleTestFile.ged"
        Gedcom_Project.BirthBeforeDeath()
        errorDict=Gedcom_Project.error["US03"]["IndividualIds"]
        self.assertIsInstance(errorDict,list)
    
    def test_Four(self):
        Gedcom_Project.filepath = "SunilUS03TestFile.ged"
        Gedcom_Project.BirthBeforeDeath()
        errorDict = Gedcom_Project.error["US03"]["IndividualIds"]
        self.assertIn("I01",errorDict) #check if Individual I01 in the error dictionary
    
    def test_Five(self):
        Gedcom_Project.filepath = "SunilUS03TestFile.file"
        self.assertIs(Gedcom_Project.BirthBeforeDeath(),True) #check if the return type is same and value is also same
     



if __name__ == '__main__':
    unittest.main()
