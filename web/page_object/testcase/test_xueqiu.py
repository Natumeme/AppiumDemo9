#!/usr/bin/env python
#-*-coding:utf-8-*-

from time import sleep
from selenium import webdriver
from selenium.webdriver import DesiredCapabilities
from web.page_object.page.MainPage import MainPage


class TestXueqiu(object):
	def setup(self):
		self.driver=webdriver.Remote(desired_capabilities=DesiredCapabilities.CHROME)
		self.driver.implicitly_wait(10)
		self.driver.get("https://xueqiu.com/")
		self.main=MainPage(self.driver)

	def test_search(self):
		self.main.search("alibaba").follow("1688")
		#todo:add assertion

	def teardown(self):
		sleep(10)
		self.driver.quit()