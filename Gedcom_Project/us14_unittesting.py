#unit testing for user story 14 "Checks and returns true if there are less than 5 multiple births at a time"

import unittest
import Gedcom_Project

class Testus14(unittest.TestCase):

    def test1(self):
        Gedcom_Project.filepath="GedcomFiles/SampleTestFile.ged"
        self.assertEqual(Gedcom_Project.CheckMultipleBirths(),True)

    def test2(self):
        Gedcom_Project.filepath= "GedcomFiles/SampleTestFile.ged"
        self.assertNotEqual(Gedcom_Project.CheckMultipleBirths(),False)

    def test3(self):
        Gedcom_Project.filepath="GedcomFiles/SampleTestFile.ged"
        self.assertTrue(Gedcom_Project.CheckMultipleBirths())

    def test4(self):
        Gedcom_Project.filepath="GedcomFiles/SampleTestFile.ged"
        self.assertIsNotNone(Gedcom_Project.CheckMultipleBirths())

if __name__ == "__main__":
    unittest.main
    
    