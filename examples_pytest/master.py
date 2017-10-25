from lib2to3.pgen2.driver import Driver

import os
import platform
import time

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, \
    NoAlertPresentException
from selenium.webdriver import DesiredCapabilities
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.support.select import Select


class CommonFunctions():
     
    def firefoxDriver(self):
        driver = webdriver.Firefox()
        driver.implicitly_wait(10)
        return driver
    
    
        
    def performLogin(self, url, user_name, password, username_value, pwd_value,  driver):
    
        driver.get(url)
       
        # username_field= driver.find_element_by_id(user_name)
        username_field= self.is_ElementPresent(By.NAME, user_name, driver)
        username_field.clear()
        username_field.send_keys(username_value)

        Password_field = self.is_ElementPresent(By.NAME, password, driver)
        Password_field.clear()
        Password_field.send_keys(pwd_value)
        
        #Press Enterkey
        Password_field.send_keys(Keys.ENTER)
        
        
      
        #time.sleep(10)
        driver.set_page_load_timeout(20)
        
      

      
        
    def is_ElementPresent (self, how, what, driver):
        try:
            element = driver.find_element(by=how, value=what)
            return element
        except NoSuchElementException as e:
            e.message
            print("Following element not found " + what)
            raise NoSuchElementException
        
    
        
