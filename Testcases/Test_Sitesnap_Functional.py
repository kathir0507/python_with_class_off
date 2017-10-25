import os
import sys

from FunctionLibrary.CommonFunctions.Commonfunctions import CommonFunctions
from FunctionLibrary.CustomFunction.SitesnapFunctional import SitesnapFunctioanl
from inspect import stack
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
import unittest


sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
#from proboscis import test
#from proboscis import TestProgram

Root= os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

#@test()
class Test_Sitesnap_Functional(unittest.TestCase):

    global objsnapshot
    global commonObject
    objsnapshot = SitesnapFunctioanl()
    commonObject = CommonFunctions()

    @classmethod
    def setUpClass(cls):
        cls.driver = commonObject.firefoxDriver()

 #   @test(groups=["unit", "numbers"])
    def test_Verify_siteSnap_Functioal(self):

        driver = self.driver
        

        try:
            value=objsnapshot.CustomTestFunctions(driver)

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


  
if __name__ == '__main__':
    unittest.main()