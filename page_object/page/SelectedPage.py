#!usr/bin/env python
#-*- coding:utf-8 -*-
from page_object.driver.AndroidClient import AndroidClient
from page_object.page.BasePage import BasePage


class SelectedPage(BasePage):
	def addDefault(self):
		return self

	def getPriceByName(self,name) -> float:
		#todo:
		price = self.driver\
			.find_element_by_xpath("//*[contains(@resource-id,'stockName') and @text='%s']" %name+"/../../../..//*[contains(@resource-id,'item_layout') and @instance='33']").text
		return float(price)

	def getPrice(self):
		pass
