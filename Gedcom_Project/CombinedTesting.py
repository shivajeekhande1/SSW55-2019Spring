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
from US26_unittesting import Test_US26_unittesting as US26Testing
from us01_unittesting import Testus01 as US01Testing
from us33_unittesting import Testus33 as US33Testing
from US29_unittesting import Test_US29_unittesting as US29Testing
from US30_unittesting import Test_US30_unittesting as US30Testing
from US31_unittesting import Test_US31_unittesting as US31Testing

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
US26=unittest.TestLoader().loadTestsFromTestCase(US26Testing)
US01=unittest.TestLoader().loadTestsFromTestCase(US01Testing)
US33=unittest.TestLoader().loadTestsFromTestCase(US33Testing)
US29=unittest.TestLoader().loadTestsFromTestCase(US29Testing)
US30=unittest.TestLoader().loadTestsFromTestCase(US30Testing)
US31=unittest.TestLoader().loadTestsFromTestCase(US31Testing)
class Test_CombinedTesting(unittest.TestCase):
    def test_A(self):
        TestSuite=unittest.TestSuite([US05,US06,US03,US08,US16,US19,US14,US15,US04,US17,US18,US19,US21,US22,US23,US24,US25,US38,US01,US31,US26,US33,US29,US30])

if __name__ == '__main__':
    unittest.main()
