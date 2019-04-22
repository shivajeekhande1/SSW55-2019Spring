import unittest
import Gedcom_Project

class Testus33(unittest.TestCase):

    def test1(self):
        Gedcom_Project.filepath = "GedcomFiles/SampleTestFile.ged"
        self.assertEqual(Gedcom_Project.listorphans(),True)

    def test2(self):
        Gedcom_Project.filepath = "GedcomFiles/SampleTestFile.ged"
        self.assertTrue(Gedcom_Project.listorphans())

    def test3(self):
        Gedcom_Project.filepath = "GedcomFiles/SampleTestFile.ged"
        self.assertIsNot(Gedcom_Project.listorphans(),False)

    def test4(self):
        Gedcom_Project.filepath = "GedcomFiles/SampleTestFile.ged"
        self.assertNotEqual(Gedcom_Project.listorphans(),False)
    
    def test5(self):
        Gedcom_Project.filepath = "GedcomFiles/SampleTestFile.ged"
        self.assertIsNotNone(Gedcom_Project.listorphans())

if __name__=='__main__':
    unittest.main()
        