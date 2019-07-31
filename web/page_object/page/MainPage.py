#!/usr/bin/env python
#-*-coding:utf-8-*-

from web.page_object.page.BasePage import BasePage
from web.page_object.page.SearchPage import SearchPage
from selenium.webdriver.common.keys import Keys


class MainPage(BasePage):
	def search(self,keyword):
		self.driver.find_element_by_name("q").send_keys(keyword)
		self.driver.find_element_by_name("q").send_keys(Keys.ENTER)
		return SearchPage(self.driver)
