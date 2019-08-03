#!/usr/bin/env python
#-*-coding:utf-8-*-

from time import sleep
from selenium import webdriver
from selenium.webdriver import DesiredCapabilities
from web.page_object.page.MainPage import MainPage
from web.page_object.page.ProfilePage import ProfilePage
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
		profile=ProfilePage(self.driver)
		profile.login()
		selected=profile.gotoSelected()
		selected.select("alibaba","1688")

	def test_log(self):
		self.log.warning("warning")
		self.log.debug("debug demo")


	def teardown(self):
		sleep(3)
		self.driver.quit()