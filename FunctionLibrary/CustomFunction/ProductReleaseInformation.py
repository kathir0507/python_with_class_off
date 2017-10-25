import ConfigParser
import os
import sys
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from FunctionLibrary.CommonFunctions.Commonfunctions import CommonFunctions


sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


Config = ConfigParser.ConfigParser()
Root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

Config.read(Root + "/../ObjectLibrary/HomepageObjects.ini")
Config.read(Root+ "/../ObjectLibrary/LoginpageObjects.ini")
Config.read(Root+ "/../DataBank/Datavalue.ini")
Config.read(Root + "/../ObjectLibrary/HomepageObjects.ini")
Config.read(Root + "/../ObjectLibrary/ProductReleaseInformationObject.ini")
Config.read(Root +  "/../ObjectLibrary/AupSchedulerObject.ini")

class ProductReleaseInformation():
    global commonObject
    commonObject = CommonFunctions()

    url=Config.get('LoginpageObjects', 'URL')
    userName=Config.get('LoginpageObjects', 'username')
    passWord=Config.get('LoginpageObjects', 'passsword')
    usname_Value=Config.get('Datavalue', 'usname_value')
    password_Value=Config.get('Datavalue', 'pssword_value')
    generateForecasteDate_btn=Config.get('ProductReleaseInformationObject', 'generateForecasteDate_btn')
    print generateForecasteDate_btn
    runbatch_text=Config.get('ProductReleaseInformationObject', 'runbatch_text')
    proceed_btn=Config.get('ProductReleaseInformationObject', 'proceed_btn')
    ok_btn=Config.get('ProductReleaseInformationObject', 'ok_btn')
    aup_shd_lnk_proce=Config.get('AupSchedulerObject', 'lnk_scheduler_ProductMenuLink')
    expectedMessage="Generated Forecast Dates For 17.8"
    home_lnk=Config.get('HomepageObjects', 'img_home_schedulerLink')
  
    def CustomTestFunctions(self,driver):

        #         print func_name
        """This function will create the object for AUP preferences view controller and triggers the required
         UI test cases via the class methods"""
        try:
#             print os.path.abspath(os.curdir)  
            commonObject.loginToCrux(self.url,self.userName,self.passWord,self.usname_Value,self.password_Value,driver)
            
            # Navigate to AUP preferences page from Home page.
            self.gotoPreferencesview(commonObject,self.home_lnk,self.aup_shd_lnk_proce,driver)

            Actual_mesg =self.generateForecasteDate(commonObject,self.generateForecasteDate_btn,self.runbatch_text,
                                                    self.proceed_btn,self.ok_btn,Root,driver)
            
            print Actual_mesg
            ## Logout from CRUX and kill the browser object
            assert Actual_mesg==self.expectedMessage
            return True
#             commonObject.logoutFromCrux(self.logout,driver)
#             return True

        except AssertionError :
            print (" Tese Case Failed ")
            raise AssertionError
            return False



    def gotoPreferencesview(self,commonObject, schedulerLink, ProductReleaseInformationObject,driver):
        """This function opens the AUP Preferences view"""
        print "On Home page, Clicking on Scheduler Link"
        # You are now on home page. Search scheduler link and click
        commonObject.gotoPage(schedulerLink,driver)
        time.sleep(20)
        print "On ProductReleaseInformation page, Clicking on ProductReleaseInformation Link"
        # You are on AUP Scheduler main view. find Preference link and Click
        commonObject.gotoPage(ProductReleaseInformationObject,driver)
        driver.set_page_load_timeout(10)

    def generateForecasteDate(self,commonObject,generateForecasteDate_btn,runbatch_text,
                                                    proceed_btn,ok_btn,Root,driver):
        
        try:
          
            commonObject.is_ElementPresent(By.XPATH,generateForecasteDate_btn,driver).click()
            time.sleep(10)
            commonObject.is_ElementPresent(By.XPATH,proceed_btn,driver).click()
            time.sleep(10)            
            Actual_message=commonObject.is_ElementPresent(By.XPATH,runbatch_text,driver).text
            time.sleep(10) 
            commonObject.is_ElementPresent(By.XPATH,ok_btn,driver).click()
            return Actual_message
        except AssertionError :
            print (" Tese Case Failed ")
            raise AssertionError
            return False
    
   