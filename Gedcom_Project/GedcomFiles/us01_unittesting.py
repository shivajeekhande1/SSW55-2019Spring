import unittest
import Gedcom_Project

class Testus01(unittest.TestCase):

    def test1(self):
        Gedcom_Project.filepath = "C:/Users/eshwa/OneDrive/Desktop/CS 555/Gedcom Project/SSW555-2019Spring-master/SSW555-2019Spring-master/SampleTestFile.ged"
        self.assertEqual(Gedcom_Project.datecheck(),True)

    def test2(self):
        Gedcom_Project.filepath = "C:/Users/eshwa/OneDrive/Desktop/CS 555/Gedcom Project/SSW555-2019Spring-master/SSW555-2019Spring-master/SampleTestFile.ged"
        self.assertTrue(Gedcom_Project.datecheck())

    def test3(self):
        Gedcom_Project.filepath = "C:/Users/eshwa/OneDrive/Desktop/CS 555/Gedcom Project/SSW555-2019Spring-master/SSW555-2019Spring-master/SampleTestFile.ged"
        self.assertIsNot(Gedcom_Project.datecheck(),False)

    def test4(self):
        Gedcom_Project.filepath = "C:/Users/eshwa/OneDrive/Desktop/CS 555/Gedcom Project/SSW555-2019Spring-master/SSW555-2019Spring-master/SampleTestFile.ged"
        self.assertNotEqual(Gedcom_Project.datecheck(),False)
    
    def test5(self):
        Gedcom_Project.filepath = "C:/Users/eshwa/OneDrive/Desktop/CS 555/Gedcom Project/SSW555-2019Spring-master/SSW555-2019Spring-master/SampleTestFile.ged"
        self.assertIsNotNone(Gedcom_Project.datecheck())

if __name__=='__main__':
    unittest.main()
        