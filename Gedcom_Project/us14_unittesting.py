#unit testing for user story 14 "Checks and returns true if there are less than 5 multiple births at a time"

import unittest
import Gedcom_Project

class Testus14(unittest.TestCase):

    def test1(self):
        Gedcom_Project.filepath="C:/Users/eshwa/OneDrive/Desktop/CS 555/Gedcom Project/SSW555-2019Spring/SampelTest.ged"
        self.assertEqual(Gedcom_Project.MultipleBirths(),True)

    def test2(self):
        Gedcom_Project.filepath= "C:/Users/eshwa/OneDrive/Desktop/CS 555/Gedcom Project/SSW555-2019Spring/SampelTest.ged"
        self.assertNotEqual(Gedcom_Project.MultipleBirths(),False)

    def test3(self):
        Gedcom_Project.filepath="C:/Users/eshwa/OneDrive/Desktop/CS 555/Gedcom Project/SSW555-2019Spring/SampelTest.ged"
        self.assertTrue(Gedcom_Project.MultipleBirths())

    def test4(self):
        Gedcom_Project.filepath="https://docs.google.com/spreadsheets/d/1h9KaWW9lpaZqIrkSKBShNbtcgByDbyBERYt_EOtWgTg/edit?ts=5c719b71#gid=348873167"
        self.assertIsNotNone(Gedcom_Project.MultipleBirths())

if __name__ == "__main__":
    unittest.main
    
    