import unittest
import Gedcom_Project

class US38_test(unittest.TestCase):
    
    def test_One(self):
        Gedcom_Project.filepath = "GedcomFiles/AcceptanceTestFile.txt"
        Gedcom_Project.ListUpcomingBirthdays()
        errorDict = Gedcom_Project.error["US38"]["IndividualIds"]
        self.assertEqual(len(errorDict),1)

    def test_Two(self):
        Gedcom_Project.filepath = "GedcomFiles/AcceptanceTestFile.txt"
        self.assertTrue(Gedcom_Project.ListUpcomingBirthdays())

     
if __name__ == '__main__':
    unittest.main()