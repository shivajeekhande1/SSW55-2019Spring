#unittesting for US22: TO check if all the ids are unique

import unittest
import Gedcom_Project

class Test_US21_unittesting(unittest.TestCase):
    def test_A(self):
        Gedcom_Project.filepath = "GedcomFiles/AcceptanceTestFile.txt"
        self.assertFalse(Gedcom_Project.uniqueIDs())
    
    def test_B(self):
        Gedcom_Project.filepath = "GedcomFiles/VenkataUS06TestFile.txt"
        self.assertTrue(Gedcom_Project.uniqueIDs())

    def test1(self):
        Gedcom_Project.filepath = "GedcomFiles/SampleTestFile.ged"
        self.assertEqual(Gedcom_Project.uniqueIDs(),True)
        
    def test4(self):
        Gedcom_Project.filepath= "GedcomFiles/SampleTestFile.ged"
        self.assertNotEqual(Gedcom_Project.uniqueIDs(),False)
    
    

    
            
if __name__ == '__main__':
    unittest.main()
