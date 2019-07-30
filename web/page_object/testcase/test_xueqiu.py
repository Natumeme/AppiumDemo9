#!/usr/bin/env python
#-*-coding:utf-8-*-

from time import sleep
from selenium import webdriver
from selenium.webdriver import DesiredCapabilities
from web.page_object.page.MainPage import MainPage
from web.page_object.testcase.BaseTestCase import BaseTestCase

class TestXueqiu(BaseTestCase):
	def setup(self):
		self.driver=webdriver.Remote(desired_capabilities=DesiredCapabilities.CHROME)
		self.driver.implicitly_wait(10)
		self.driver.get("https://xueqiu.com/")
		self.main=MainPage(self.driver)

	def test_search(self):
		self.main.search("alibaba").follow("1688")
		#todo:add assertion

	def test_profile(self):
		#添加cookie
		self.driver.add_cookie({"name":"xxx","value":"xxx"})
		self.driver.add_cookie({"name": "xxx", "value": "xxx"})
		self.driver.add_cookie({"name": "xxx", "value": "xxx"})
		self.driver.add_cookie({"name": "xxx", "value": "xxx"})
		self.driver.add_cookie({"name": "xxx", "value": "xxx"})
		self.driver.add_cookie({"name": "xxx", "value": "xxx"})
		self.driver.add_cookie({"name": "xxx", "value": "xxx"})
		self.driver.add_cookie({"name": "xxx", "value": "xxx"})
		self.driver.add_cookie({"name": "xxx", "value": "xxx"})
		print(self.driver.get_cookies())

		self.driver.refresh()
		self.driver.get("https://xueqiu.com/setting/user")

	def test_log(self):
		self.log.warning("warning")
		self.log.debug("debug demo")


	def teardown(self):
		sleep(3)
		self.driver.quit()