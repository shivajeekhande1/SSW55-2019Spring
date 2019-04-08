import unittest
import Gedcom_Project
class Test_US23_unittesting(unittest.TestCase):
    def test_A(self):
        self.assertEqual(Gedcom_Project.UniqueNamesAndDob(),False)

    def test_B(self):
        Gedcom_Project.filepath = "GedcomFiles/SampleTestFile.ged"
        self.assertEqual(Gedcom_Project.UniqueNamesAndDob(),True)

    def test_C(self):
        Gedcom_Project.UniqueNamesAndDob()
        errorDict = Gedcom_Project.error["US23"]["IndividualIds"]
        self.assertEqual(len(errorDict),1)

if __name__ == '__main__':
    unittest.main()
