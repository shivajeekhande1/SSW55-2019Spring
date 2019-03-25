import unittest
import Gedcom_Project

class Test_US16_unittesting(unittest.TestCase):
    def test_A(self):
        Gedcom_Project.filepath = "GedcomFiles/VenkataUS06TestFile.txt"
        self.assertEqual(Gedcom_Project.AllMaleNames(),True)

    def test_B(self):
        Gedcom_Project.filepath = "GedcomFiles/AcceptanceTestFile.txt"
        self.assertEqual(Gedcom_Project.AllMaleNames(),False)

    def test_C(self):
        Gedcom_Project.filepath ="GedcomFiles/AcceptanceTestFile.txt"
        Gedcom_Project.AllMaleNames()
        error = Gedcom_Project.error["US16"]["Family id"]
        self.assertIn("F01",error)

if __name__ == '__main__':
    unittest.main()
