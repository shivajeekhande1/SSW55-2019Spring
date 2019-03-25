import unittest
import Gedcom_Project

class Testus18(unittest.TestCase):

    def test1(self):
        Gedcom_Project.filepath = "GedcomFiles/SampleTestFile.ged"
        self.assertEqual(Gedcom_Project.checkSiblingsmarried(),True)

    def test2(self):
        Gedcom_Project.filepath = "GedcomFiles/SampleTestFile.ged"
        self.assertTrue(Gedcom_Project.checkSiblingsmarried())

    def test3(self):
        Gedcom_Project.filepath = "GedcomFiles/SampleTestFile.ged"
        self.assertIsNotNone(Gedcom_Project.checkSiblingsmarried())

    def test4(self):
        Gedcom_Project.filepath= "GedcomFiles/SampleTestFile.ged"
        self.assertNotEqual(Gedcom_Project.checkSiblingsmarried(),False)

if __name__ == "__main__":
    unittest.main()