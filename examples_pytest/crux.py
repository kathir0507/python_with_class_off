from master import CommonFunctions
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import os
import sys
import time

class Test():
    global common_object
    common_object = CommonFunctions()
    
    
    def setup(self):
        self.driver = common_object.firefoxDriver()
        
    def performFBLogin(self):
        common_object.performLogin("https://crux.hmsdev.lan/sitesnap/login", "UserName", "UserPassword", "katmohan", "changeme", self.driver)
        
    def clickaa(self):
        time.sleep(5)
        common_object.is_ElementPresent(By.XPATH, ".//img[@src='/sitesnap/static/images/sitesnap.png']",self.driver).click()
        time.sleep(10)
        common_object.is_ElementPresent(By.XPATH, ".//input[@value='qualified']",self.driver).click()
        time.sleep(10)
        common_object.is_ElementPresent(By.XPATH, ".//input[@value='not_enrolled']",self.driver).click()
        #element3.click()
        time.sleep(5)
        common_object.is_ElementPresent(By.XPATH, ".//div[@id='aup_site_list']/a[1]",self.driver).click()
        #element5.click()
        time.sleep(10)
        common_object.is_ElementPresent(By.XPATH, ".//*[@id='cruxmenu']/ul/li[1]/a",self.driver).click()
      
        
                                                  
        

if __name__ == '__main__':
    t = Test()
    t.setup()
    t.performFBLogin()
    t.clickaa()
   
   
