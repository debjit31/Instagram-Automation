## Automation using selenium webdriver 

import os
import time
import sys
from secrets import username, password
from selenium import webdriver

## Using selenium to automate tasks

class InstagramBot():
	def __init__(self):
		self.driver = webdriver.Chrome('chromedriver.exe')

	def login(self):
		self.driver.get("http://www.instagram.com")

		time.sleep(2)

		self.driver.find_element_by_name('username').send_keys(username)

		self.driver.find_element_by_name('password').send_keys(password)


		self.driver.find_elements_by_xpath("//div[contains(text(), 'Log In')]")[0].click()


b = InstagramBot()
b.login()
