import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from FunctionLibrary.CommonFunctions.Commonfunctions import CommonFunctions
from FunctionLibrary.CustomFunction.ProductReleaseInformation import ProductReleaseInformation
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
import unittest
from inspect import stack
#from proboscis import test
#from proboscis import TestProgram

Root= os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

#@test()
class Test_ProdRelease(unittest.TestCase):

    global objProductInformation
    global commonObject
    objProductInformation=ProductReleaseInformation()
    commonObject = CommonFunctions()

    @classmethod
    def setUpClass(cls):
        cls.driver = commonObject.firefoxDriver()

 #   @test(groups=["unit", "numbers"])
    def test_Verify_prodRelease(self):

        driver = self.driver
        

        try:
            value=objProductInformation.CustomTestFunctions(driver)
            print value
            if value:
                print stack()[0][3]+ " Test Case Passed "
 
            else:
                print("Assertion Error Occurred in following test case -> "+stack()[0][3])
                commonObject.screenshotsOnFailure(stack()[0][3],driver,Root)
                self.fail("Assertion Error Occurred in following test case -> "+stack()[0][3])

        except NoSuchElementException as e:
            commonObject.screenshotsOnFailure(stack()[0][3], driver, Root)
            self.fail(stack()[0][3]+"TestCase Failed due to Element Not Found")

        except TimeoutException as e:
            commonObject.screenshotsOnFailure(stack()[0][3], driver, Root)
            self.fail(stack()[0][3]+"TestCase Failed due to Timeout")

        except Exception as e:
            commonObject.screenshotsOnFailure(stack()[0][3], driver, Root)
            self.fail(stack()[0][3]+"TestCase Failed due to an Error or Exception")



    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

# if __name__ == '__main__':
#     TestProgram().run_and_exit()



if __name__ == '__main__':
    unittest.main()





