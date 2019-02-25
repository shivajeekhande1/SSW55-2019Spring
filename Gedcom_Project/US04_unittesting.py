import unittest
import Gedcom_Project

class Test_US04_unittesting(unittest.TestCase):
    def test_A(self):
        Gedcom_Project.filepath = "GedcomFiles/VenkataUS04TestFile.txt"
        self.assertFalse(Gedcom_Project.CheckMarriageBeforeDivorce())
    
    def test_B(self):
        Gedcom_Project.filepath = "GedcomFiles/VenkataUS06TestFile.txt"
        self.assertTrue(Gedcom_Project.CheckMarriageBeforeDivorce())

    def test_C(self):
        Gedcom_Project.filepath = "GedcomFiles/VenkataUS04TestFile.txt"
        error = []
        if Gedcom_Project.CheckMarriageBeforeDivorce() == False:
            error = Gedcom_Project.error["US04"]["Family id"]
        self.assertEqual(len(error),1)
        
    def test_D(self):
        Gedcom_Project.filepath = "GedcomFiles/VenkataUS04TestFile.txt"
        error = []
        if Gedcom_Project.CheckMarriageBeforeDivorce() == False:
            error = Gedcom_Project.error["US04"]["Family id"]
        self.assertIn("F03",error)
    
    

    
            
if __name__ == '__main__':
    unittest.main()
