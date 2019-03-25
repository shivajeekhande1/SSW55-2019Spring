import unittest
import Gedcom_Project
class Test_US08_unittesting(unittest.TestCase):
    def test_A(self):
        Gedcom_Project.filepath = "GedcomFiles/VenkataUS06TestFile.txt"
        self.assertEqual(Gedcom_Project.BirthBeforeMarriageOfParents(),True)
    
    def test_B(self):
        Gedcom_Project.filepath = "GedcomFiles/AcceptanceTestFile.txt"
        self.assertEqual(Gedcom_Project.BirthBeforeMarriageOfParents(),False)

    def test_C(self):
        Gedcom_Project.filepath = "GedcomFiles/AcceptanceTestFile.txt"
        Gedcom_Project.BirthBeforeMarriageOfParents()
        error = Gedcom_Project.error["US08"]["Family id"]
        self.assertIn("F03",error)

if __name__ == '__main__':
    unittest.main()
