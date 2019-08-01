#!/usr/bin/env python
#-*-coding:utf-8-*-
from web.page_object.page.BasePage import BasePage
from web.page_object.page.SelectedPage import SelectedPage


class ProfilePage(BasePage):
	def login(self):
		self.driver.add_cookie({"name":"device_id","value":"xxx"})
		self.driver.add_cookie({"name": "s", "value": "xxx"})
		self.driver.add_cookie({"name": "xq_a_token", "value": "xxx"})
		self.driver.add_cookie({"name": "xqat", "value": "xxx"})
		self.driver.add_cookie({"name": "xq_r_token", "value": "xxx"})
		self.driver.add_cookie({"name": "xq_is_login", "value": "1"})
		self.driver.add_cookie({"name": "u", "value": "xxx"})
		self.driver.add_cookie({"name": "xxx", "value": "xxx"})
		self.driver.add_cookie({"name": "xxx", "value": "xxx"})
		self.driver.add_cookie({"name": "snbim_minify", "value": "xxx"})
		print(self.driver.get_cookies())

		self.driver.refresh()

	def gotoSelected(self):
		return SelectedPage(self.driver)