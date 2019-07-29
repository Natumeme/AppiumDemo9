#!/usr/bin/env python
#-*-coding:utf-8-*-
import json

import time
from selenium import webdriver
from selenium.webdriver import DesiredCapabilities


class TestTesterhome(object):
	def setup(self):
		options = webdriver.ChromeOptions()
		# self.driver = webdriver.Chrome(options=options)
		self.driver = cwebdriver.Remote(desired_capabilities=DesiredCapabilities.CHROME)

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
		raw = self.driver.execute_script("return JSON.stringify(window.performance.timing)")
		print(raw)
		print(json.dumps(json.loads(raw),indent=4))

	def test_execute(self):
		self.driver.execute("getXXX",params={"x":1,"y":2})

	def test_cookie(self):
		print(self.driver.get_cookies())
		self.driver.add_cookie({"x":"c"})

	def teardown(self):
		time.sleep(2)
		self.driver.quit()