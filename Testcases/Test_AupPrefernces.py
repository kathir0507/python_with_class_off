import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from FunctionLibrary.CommonFunctions.Commonfunctions import CommonFunctions
from FunctionLibrary.CustomFunction.AupPreferences import AupPreferences
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
import unittest
from inspect import stack


Root= os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


class Test_AupPrefernces(unittest.TestCase):

    global objAupPreferences
    global commonObject
    objAupPreferences = AupPreferences()
    commonObject = CommonFunctions()

    @classmethod
    def setUpClass(cls):
        cls.driver = commonObject.firefoxDriver()

 
    def test_Verify_aupPreferences(self):

        driver = self.driver
    
        try:
            value= objAupPreferences.CustomTestFunctions(driver)

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





