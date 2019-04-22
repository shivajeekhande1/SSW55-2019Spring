import unittest
import Gedcom_Project
class Test_US26_unittesting(unittest.TestCase):
    def test_One(self):
        Gedcom_Project.filepath = "GedcomFiles/AcceptanceTestFile.txt"
        Gedcom_Project.CorrespondingEntries()
        errorDict=Gedcom_Project.error["US26"]["child"]
        self.assertIsInstance(errorDict,list)

    def test_Two(self):
        Gedcom_Project.filepath = "GedcomFiles/AcceptanceTestFile.txt"
        self.assertFalse(Gedcom_Project.CorrespondingEntries())

if __name__ == '__main__':
    unittest.main()
