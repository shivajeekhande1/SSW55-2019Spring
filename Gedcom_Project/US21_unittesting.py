#unittesting for US21: Check whether the Spouse roles are assigned with the respective genders

import unittest
import Gedcom_Project

class Test_US21_unittesting(unittest.TestCase):
    def test_A(self):
        Gedcom_Project.filepath = "GedcomFiles/AcceptanceTestFile.txt"
        self.assertFalse(Gedcom_Project.checkrole())
    
    def test_B(self):
        Gedcom_Project.filepath = "GedcomFiles/VenkataUS06TestFile.txt"
        self.assertTrue(Gedcom_Project.checkrole())

    def test1(self):
        Gedcom_Project.filepath = "GedcomFiles/SampleTestFile.ged"
        self.assertEqual(Gedcom_Project.checkrole(),True)
        
    def test4(self):
        Gedcom_Project.filepath= "GedcomFiles/SampleTestFile.ged"
        self.assertNotEqual(Gedcom_Project.checkrole(),False)
    
    

    
            
if __name__ == '__main__':
    unittest.main()

