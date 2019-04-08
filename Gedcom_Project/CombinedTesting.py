import unittest
from US05_unittesting import TestUS05_test1 as US05Testing
from US06_unittesting import Test_test1 as US06Testing
from US03_unittesting import Test_test1 as US03Testing
from US08_unittesting import Test_US08_unittesting as US08Testing
from US16_unittesting import Test_US16_unittesting as US16Testing
from US19_unittesting import Test_test1 as US19Testing
from us14_unittesting import Testus14 as US14Testing
from us15_unittesting import Testus15 as US15Testing
from US04_unittesting import Test_US04_unittesting as US04Testing
from US17_unittesting import US17_test as US17Testing
from US18_unittesting import Testus18 as US18Testing
from US19_unittesting import Test_test1 as US19Testing
from US21_unittesting import Test_US21_unittesting as US21Testing
from US22_unittesting import Test_US21_unittesting as US22Testing
from US23_unittesting import Test_US23_unittesting as US23Testing
from US24_unittesting import US24_test as US24Testing
from US25_unittesting import Test_US25_unittesting as US25Testing
from US38_unittesting import US38_test as US38Testing

US05=unittest.TestLoader().loadTestsFromTestCase(US05Testing)
US06=unittest.TestLoader().loadTestsFromTestCase(US06Testing)
US03=unittest.TestLoader().loadTestsFromTestCase(US03Testing)
US08=unittest.TestLoader().loadTestsFromTestCase(US08Testing)
US16=unittest.TestLoader().loadTestsFromTestCase(US16Testing)
US19=unittest.TestLoader().loadTestsFromTestCase(US19Testing)
US14=unittest.TestLoader().loadTestsFromTestCase(US14Testing)
US15=unittest.TestLoader().loadTestsFromTestCase(US15Testing)
US04=unittest.TestLoader().loadTestsFromTestCase(US04Testing)
US17=unittest.TestLoader().loadTestsFromTestCase(US17Testing)
US18=unittest.TestLoader().loadTestsFromTestCase(US18Testing)
US19=unittest.TestLoader().loadTestsFromTestCase(US19Testing)
US21=unittest.TestLoader().loadTestsFromTestCase(US21Testing)
US22=unittest.TestLoader().loadTestsFromTestCase(US22Testing)
US23=unittest.TestLoader().loadTestsFromTestCase(US23Testing)
US24=unittest.TestLoader().loadTestsFromTestCase(US24Testing)
US25=unittest.TestLoader().loadTestsFromTestCase(US25Testing)
US38=unittest.TestLoader().loadTestsFromTestCase(US38Testing)

class Test_CombinedTesting(unittest.TestCase):
    def test_A(self):
        TestSuite=unittest.TestSuite([US05,US06,US03,US03,US08,US16,US19,US14,US15,US04,US17])

if __name__ == '__main__':
    unittest.main()
