import unittest
import Gedcom_Project
class Test_US31_unittesting(unittest.TestCase):
    def test_One(self):
        Gedcom_Project.filepath = "GedcomFiles/AcceptanceTestFile.txt"
        self.assertTrue(Gedcom_Project.LivingSingle())

    def test_Two(self):
        Gedcom_Project.filepath = "GedcomFiles/AcceptanceTestFile.txt"
        Gedcom_Project.LivingSingle()
        errorDict = Gedcom_Project.error["US31"]["Individuals"]
        self.assertIn("I07",errorDict)

if __name__ == '__main__':
    unittest.main()
