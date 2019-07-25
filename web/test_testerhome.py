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

	def test_basic(self):
		#窗口的最大化和最小化
		self.driver.maximize_window()
		self.driver.fullscreen_window()

	def test_execute(self):
		#执行JS的命令


	def teardown(self):
		self.driver.quit()