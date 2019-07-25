#!/usr/bin/env python
#-*-coding:utf-8-*-

import time
from selenium import webdriver

class TestTesterhome(object):
	def setup(self):
		self.driver = webdriver.Chrome()
		self.driver.implicitly_wait(10)
		self.driver.get("https://testerhome.com/")

	def test_mtsc2019(self):
		self.driver.find_element_by_partial_link_text("TesterHome Girls").click()
		time.sleep(2)
		self.driver.find_element_by_xpath('//*[@data-toggle="dropdown" and @class="btn btn-default"]').click()
		self.driver.find_element_by_link_text('其他').click()
