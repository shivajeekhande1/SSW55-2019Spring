import unittest
import Gedcom_Project
class Test_US25_unittesting(unittest.TestCase):
    def test_A(self):
        Gedcom_Project.filepath="GedcomFiles/AcceptanceTestFile.txt"
        self.assertEqual(Gedcom_Project.UniqueFirstNamesInFamily(),False)

    def test_B(self):
        Gedcom_Project.filepath = "GedcomFiles/SampleTestFile.ged"
        self.assertEqual(Gedcom_Project.UniqueFirstNamesInFamily(),True)

    
if __name__ == '__main__':
    unittest.main()
