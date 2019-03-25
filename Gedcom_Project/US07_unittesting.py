import unittest
import Gedcom_Project

class Testus07(unittest.TestCase):

    def test1(self):
        Gedcom_Project.filepath = "GedcomFiles/SampleTestFile.ged"
        self.assertEqual(Gedcom_Project.max_age(),True)

    def test2(self):
        Gedcom_Project.filepath = "GedcomFiles/SampleTestFile.ged"
        self.assertTrue(Gedcom_Project.max_age())

    def test3(self):
        Gedcom_Project.filepath = "GedcomFiles/SampleTestFile.ged"
        self.assertIsNotNone(Gedcom_Project.max_age())

    def test4(self):
        Gedcom_Project.filepath= "GedcomFiles/SampleTestFile.ged"
        self.assertNotEqual(Gedcom_Project.max_age(),False)

if __name__ == "__main__":
    unittest.main()