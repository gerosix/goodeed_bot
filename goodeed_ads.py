# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
import unittest, time, re
from pyvirtualdisplay import Display

"""
This script allows you to connect to goodeed.com, login and watch 1 ad.
You can watch 3 ads by re-used the code below
This code lauch a graphic server on the screen

Requirements for this script:
- Create a virtualenv in python 2
    - Debian / Ubuntu : apt install virtualenv
                        apt install xvfb (for the virtual display)
                        apt install iceweasel (firefox)
                        apt install virtualenv (python virtual environment)

    - Creation:         virtualenv selenium && mkdir ./selenium/goodeed && cd selenium

- Activate the virtualenv: source bin/activate

- Install python packages:
    - With pip :        pip install selenium
                        pip install PyVirtualDisplay
                        pip install xvfbwrapper

- Put this code at ./selenium/goodeed/goodeed_ads.py

- Install gecko driver for firefox
    mkdir gecko && cd gecko; wget https://github.com/mozilla/geckodriver/releases/download/v0.18.0/geckodriver-v0.18.0-linux64.tar.gz; tar zxvf geckodriver-v0.18.0-linux64.tar.gz; cp geckodriver /bin

- Execute the script:
                        python goodeed_ads.py
"""

class Test(unittest.TestCase):
    def setUp(self):
        """ Setup of the test """
        display = Display(visible=0, size=(1024, 768))
        display.start()
        caps = webdriver.DesiredCapabilities().FIREFOX
        caps["marionette"] = False
        self.driver = webdriver.Firefox(capabilities=caps) # set a specific capabilities to correct a bug
        self.driver = webdriver.Firefox() # set a specific capabilities to correct a bug
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.goodeed.com/"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test(self):
        """ Core of the test """
        # TODO: set optimized times to driver.implicitly_wait(time_in_second)
        driver = self.driver
        driver.maximize_window()
        driver.get(self.base_url + "/")
        driver.implicitly_wait(30)
        try:
            time.sleep(1)
            driver.find_element_by_css_selector("div.lp-modal-close > span").click()
        except NoSuchElementException:
            pass
        driver.implicitly_wait(30)
        driver.find_element_by_css_selector("div.menu-user > a.btn-login-nav.ng-binding").click()
        # driver.find_element_by_css_selector("div.lp-modal-close > span").click()
        driver.find_element_by_name("email").clear()
        driver.find_element_by_name("email").send_keys("EMAIL")
        driver.find_element_by_name("password").clear()
        driver.find_element_by_name("password").send_keys("PASSWORD")
        try:
            driver.implicitly_wait(30)
            element = driver.find_element_by_xpath("//button[@type='submit']")
            driver.execute_script("arguments[0].click();", element)
        except WebDriverException:
            pass
        try:
            time.sleep(1)
            driver.implicitly_wait(30)
            driver.find_element_by_xpath("//div[@id='app']/section/div/div/div/div[2]/div[3]/project-home-item/div[3]/give-button/button").click()
            #driver.find_element_by_xpath("//div[@id='app']/section/div/div[2]/ul/li[5]/project-home-item/div[3]/give-button/button").click()
        except NoSuchElementException:
            pass
        time.sleep(40)
        driver.implicitly_wait(60)
        driver.find_element_by_xpath("//div[@id='donation-progress-bar-handler']/div/button").click()
        driver.implicitly_wait(30)
        driver.find_element_by_xpath("//button[@type='submit']").click()
        try:
            driver.implicitly_wait(30)
            driver.find_element_by_xpath("//button[2]").click()
        except NoSuchElementException:
            pass

        # Second round
        try:
            time.sleep(1)
            driver.implicitly_wait(30)
            driver.find_element_by_xpath("//div[@id='app']/section/div/div/div/div[2]/div[3]/project-home-item/div[3]/give-button/button").click()
            #driver.find_element_by_xpath("//div[@id='app']/section/div/div[2]/ul/li[5]/project-home-item/div[3]/give-button/button").click()
        except NoSuchElementException:
            pass
        time.sleep(40)
        driver.implicitly_wait(60)
        driver.find_element_by_xpath("//div[@id='donation-progress-bar-handler']/div/button").click()
        driver.implicitly_wait(30)
        driver.find_element_by_xpath("//button[@type='submit']").click()
        try:
            driver.implicitly_wait(30)
            driver.find_element_by_xpath("//button[2]").click()
        except NoSuchElementException:
            pass

        # Third Round
        try:
            time.sleep(1)
            driver.implicitly_wait(30)
            driver.find_element_by_xpath("//div[@id='app']/section/div/div/div/div[2]/div[3]/project-home-item/div[3]/give-button/button").click()
            #driver.find_element_by_xpath("//div[@id='app']/section/div/div[2]/ul/li[5]/project-home-item/div[3]/give-button/button").click()
        except NoSuchElementException:
            pass
        time.sleep(40)
        driver.implicitly_wait(60)
        driver.find_element_by_xpath("//div[@id='donation-progress-bar-handler']/div/button").click()
        driver.implicitly_wait(30)
        driver.find_element_by_xpath("//button[@type='submit']").click()
        try:
            driver.implicitly_wait(30)
            driver.find_element_by_xpath("//button[2]").click()
        except NoSuchElementException:
            pass


        # TODO: watch 2 more ads to avoid executing the script 3 times

    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True

    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True

    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
