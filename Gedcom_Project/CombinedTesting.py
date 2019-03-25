import unittest
from US05_unittesting import Test_test1 as US05Testing
from US06_unittesting import Test_test1 as US06Testing


US05=unittest.TestLoader().loadTestsFromTestCase(US05Testing)
US06=unittest.TestLoader().loadTestsFromTestCase(US06Testing)

class Test_CombinedTesting(unittest.TestCase):
    def test_A(self):
        TestSuite=unittest.TestSuite([US05,US06])

if __name__ == '__main__':
    unittest.main()
