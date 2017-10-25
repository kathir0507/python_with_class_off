from inspect import stack
import os
import sys
import unittest

import pytest
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException

from FunctionLibrary.CommonFunctions.Commonfunctions import CommonFunctions
from FunctionLibrary.CustomFunction.PopulateforcastDate import PopulateforecastDate


sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

    
Root= os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    
  
class Test_Cron1_PopulateForecaseDate(unittest.TestCase):

    global objAupPreferences
    global commonObject
    objAupPreferences = PopulateforecastDate()
    commonObject = CommonFunctions()

    @classmethod
    def setUpClass(cls):
        cls.driver = commonObject.firefoxDriver()

    @pytest.mark.sanity
    @pytest.mark.Regression
    def test_Verify_cron1_PopulateForecasedate(self):

        driver = self.driver
        

        try:
            value=objAupPreferences.CustomTestFunctions(driver)

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
            commonObject.screenhotsOnFailure(stack()[0][3], driver, Root)
            self.fail(stack()[0][3]+"TestCase Failed due to an Error or Exception")



    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()



if __name__ == '__main__':
    unittest.main()





