import unittest
import Gedcom_Project

class Test_test1(unittest.TestCase):
    
    def test_A(self):
        Gedcom_Project.filepath = "C:/Users/princ/OneDrive/Documents/stevens/test.txt"
        self.assertEqual(Gedcom_Project.CheckDivorceBeforeDeath(),False)

    def test_B(self):
        Gedcom_Project.filepath = "C:/Users/princ/OneDrive/Documents/stevens/test.txt"
        self.assertFalse(Gedcom_Project.CheckDivorceBeforeDeath())

    def test_C(self):
        Gedcom_Project.filepath = "C:/Users/princ/OneDrive/Documents/stevens/Venkata_Khande_SSE555_project01.txt"
        self.assertTrue(Gedcom_Project.CheckDivorceBeforeDeath())
    
    def test_D(self):
        Gedcom_Project.filepath = "C:/Users/princ/OneDrive/Documents/stevens/Venkata_Khande_SSE555_project01.txt"
        self.assertNotEqual(Gedcom_Project.CheckDivorceBeforeDeath(),False)
    
    def test_E(self):
        Gedcom_Project.filepath = "C:/Users/princ/OneDrive/Documents/stevens/test.txt"
        error= []
        if Gedcom_Project.CheckDivorceBeforeDeath() == False:
            error = Gedcom_Project.error["US06"]["Family id"]
        self.assertIn("F03",error)



if __name__ == '__main__':
    unittest.main()
