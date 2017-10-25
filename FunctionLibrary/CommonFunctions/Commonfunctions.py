from datetime import timedelta
import datetime
from lib2to3.pgen2.driver import Driver
import os
import platform
import time

from pytz import timezone
import pytz
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, \
    NoAlertPresentException
from selenium.webdriver import DesiredCapabilities
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.support.select import Select
from _elementtree import iselement


#
class CommonFunctions():
    
    def firefoxDriver(self):
        """Firefox Driver"""
        if platform.system() == 'Linux':
            from pyvirtualdisplay import Display
#             print "Envrionment: Linux"
            display = Display(visible=0, size=(1440,768))
            display.start()
            driver = webdriver.Firefox()
            driver.implicitly_wait(30)
        elif platform.system() == 'Windows':
            driver = webdriver.Firefox()
            driver.implicitly_wait(30)
            driver.set_window_size(1536,864)

        return driver
        
    def loginToCrux(self, URL, obj_username, obj_password, username_value, pwd_value,driver):
        """Login to CRUX"""
        
        print "Login to CRUX"
        driver.get(URL)

        username_field=  self.is_ElementPresent(By.NAME,obj_username,driver)
        username_field.clear()
        username_field.send_keys(username_value)

        Password_field = self.is_ElementPresent(By.NAME,obj_password,driver)
        Password_field.clear()
        Password_field.send_keys(pwd_value)
        #Press Enterkey
        Password_field.send_keys(Keys.ENTER)
       
        driver.set_page_load_timeout(20)
        time.sleep(10)
        
    def logoutFromCrux(self, logoutlink,driver):
        """Logout Function"""
        
        print "Logout from CRUX and Kill the browser object"
        self.is_ElementPresent(By.CSS_SELECTOR,logoutlink,driver).click()
#         
        driver.set_page_load_timeout(20)
        
        print "Test Completed"
#    
    def gotoPage(self,Aup_id,driver):
        """This function is used to navigate to specific page given
        as a parameter"""
        
        self.is_ElementPresent(By.XPATH,Aup_id,driver).click()
        

    def alert_present(self,driver):
        """To handle alert"""
        try:
            driver.switch_to_alert().accept()
            return True
        except NoAlertPresentException: 
            return False

   

    def is_ElementPresent (self, how, what, driver):
        """
        Helper method to confirm the presence of an element on page
        :params how: By locator type
        :params what: locator value
        """
        time_interval_min = 0
        time_interval_max = 150
        time_wait=0
       
        try:
            element = driver.find_element(by=how, value=what)
            if(element):
                return element
                           
        except NoSuchElementException as e:
            while not self.is_present(By.XPATH, what, driver):
                    time_interval_min=time_interval_min+10
                   
                    time.sleep(10)
                    if(time_interval_min>=60):
                        print "Exceeded the time limit"
                        raise NoSuchElementException
            print("Following element found " + what)
            return what       

        
    def is_ElementsPresent(self, how, what, driver):
        """
        Helper method to confirm the presence of an element on page
        :params how: By locator type
        :params what: locator value
        """
        try:
            elements = driver.find_elements(by=how, value=what)
           
            return elements
        except NoSuchElementException as e:
            e.message
            print("Following element not found " + what)
            raise NoSuchElementException
    def timestamp(self):
        """To get the current time"""
        date_format='%Y-%m-%d %H'
        date = datetime.datetime.now(tz=pytz.utc)
#         print 'Current date & time is:', date.strftime(date_format)
        
        date = date.astimezone(timezone('US/Pacific'))
        
        return date.strftime(date_format)
    def timestampmonth(self):
        """To get the current month"""
        date_format='%Y-%m-%d %H'
        date = datetime.datetime.now()
        return date.strftime("%B")
    def timestampyear(self):
        """To get the current year"""
        date_format='%Y-%m-%d %H'
        date = datetime.datetime.now()
        return date.strftime("%Y")
    def currentdate(self):
        """To get the current date"""
        format='%d-%B-%Y'
        date=datetime.datetime.now()
        return date.strftime(format)
    def nextdate(self):
        """To get the nextdate"""
        format='%d-%B-%Y'
        today=datetime.datetime.now()
        nextday=(today + timedelta(days=3)).strftime("%d-%b-%Y")
        return nextday
    def is_present(self, how, what, driver):
        """
        Helper method to confirm the presence of an element on page
        :params how: By locator type
        :params what: locator value
        """
        try:
            element = driver.find_element(by=how, value=what)
            return True
        except NoSuchElementException as e:
            e.message
            return False

    def is_exists(self, how, what, driver):
        """
        Helper method to confirm the presence of an element on page
        :params how: By locator type
        :params what: locator value
        """
        try:
            element = driver.find_element(by=how, value=what)
            return True
        except NoSuchElementException as e:
            e.message
            print("Following element not found " + what)
            raise NoSuchElementException
    def pageloadtime(self,timesec,driver):
        """To get the PageLoadtime"""
        try:
            driver.set_page_load_timeout(timesec)
           
        except NoSuchElementException as e:
            e.message
            print("Timeout Error " +timesec)
    def string_split(self,content,spliter,driver):
        """To get the String split"""
        try:
            message=self.is_ElementPresent(By.XPATH,content,driver).text
            mes = []
#            membersL = [memb.split("\n")[1] for memb in message]
            for i in message.split("\n"):
                mes.append(i)
            return mes
        except NoSuchElementException as e:
            e.message
            print("Error"+e.message )
    
    def select_by_text(self,driver,dropdown_name,form_string):
        """To select the item by text"""
        try:
            select=self.is_ElementPresent(By.XPATH,dropdown_name,driver)
            sel = Select(select)
            sel.select_by_visible_text(form_string)
            return True
        except NoSuchElementException as e:
            e.message
            print("Error"+e.message )
    
    def screenshotsOnFailure(self,testName,driver,Root):
            """This function is used to navigate to specific page given
            as a parameter"""
            print Root+"\\Screenshots\\"+testName+".png"
            driver.save_screenshot(Root+"\\Screenshots\\"+testName+".png")
            
    def delete_table(self,driver):
        """ Delete the table content by clicking delete Button"""
        count=0
        trElement = driver.find_elements_by_xpath("//span[text()='Delete']")
        buttoncount=len(trElement)
        for x in range(0, buttoncount):     
            if(self.is_present(By.XPATH, "//span[text()='Delete']", driver)):
                self.is_ElementPresent(By.XPATH, "//span[text()='Delete']", driver).click()
                self.is_ElementPresent(By.XPATH, "//span[text()='Confirm']", driver).click()
                count=count+1
               
            else:
                count=0    
        if(count>0):
            return True
        else:
            return False
    def is_exists_condition(self, how, what, driver):
        """
        Helper method to confirm the presence of an element on page
        :params how: By locator type
        :params what: locator value
        """
        try:
            element = driver.find_element(by=how, value=what)
            return True
        except NoSuchElementException as e:
            return False   