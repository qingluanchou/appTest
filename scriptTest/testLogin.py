# -*- coding: utf-8 -*-
"""
Simple iOS tests, showing accessing elements and getting/setting text from them.
"""
import unittest
import os
from random import randint
from appium import webdriver
from time import sleep

class SimpleIOSTests(unittest.TestCase):

    def setUp(self):
        # set up appium
        #app = os.path.abspath('app/newPatient.app')
        
        self.driver = webdriver.Remote(
            command_executor='http://127.0.0.1:4723/wd/hub',
            )

    def tearDown(self):
        self.driver.quit()


    def _scroll_lauchPage(self):

        for i in range(2):
            self.driver.swipe(300,400,-280,0,800)

        sleep(1)

        self.driver.find_element_by_accessibility_id('firstGuideImage03_5').click()

    def test_01_login(self):
        #self._scroll_lauchPage()

        self.driver.find_element_by_accessibility_id('前往').click()
        
        sleep(1)
        self.driver.find_element_by_ios_predicate('type == "XCUIElementTypeButton" AND name == "我"').click()


        sleep(1)
        self.driver.find_element_by_name('登 录').click()

        sleep(1)
    
        self.driver.find_element_by_name('使用用户名密码方式登录').click()
    
        sleep(1)

        self.driver.find_element_by_class_name('UIATextField').clear()
        self.driver.find_element_by_class_name('UIATextField').send_keys("huiwang227")
        self.driver.find_element_by_class_name('UIASecureTextField').send_keys("haodf1907")
        
        self.driver.hide_keyboard()

        sleep(1)
        
        self.driver.find_element_by_ios_predicate('type == "XCUIElementTypeButton" AND name == "登录"').click()
    
        sleep(5)
        
        #self.driver.find_element_by_ios_predicate('type == "XCUIElementTypeButton" AND name == "医院"').click()


#         sleep(10)
# if __name__ == '__main__':
#     suite = unittest.TestLoader().loadTestsFromTestCase(SimpleIOSTests)
#     unittest.TextTestRunner(verbosity=2).run(suite)
