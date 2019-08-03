#!/usr/bin/env python
#-*-coding:utf-8-*-
from web.page_object.page.BasePage import BasePage


class SelectedPage(BasePage):
	def select(self,keyword,market):
		self.driver.find_element_by_css_selector('.optional .search__dropdown input').send_keys(keyword)
