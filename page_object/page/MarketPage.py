#!usr/bin/env python
#-*- coding:utf-8 -*-
from page_object.driver.AndroidClient import AndroidClient
from page_object.page.BasePage import BasePage


class MarketPage(BasePage):
	def addDefault(self):
		return self

	def getMarketPrice(self,name) -> float:
		price = self.driver\
		.find_element_by_xpath("//*[@text='%s']" %name+ "/..//*[contains(@resource-id,'index_price') and @instance='12']").text
		return float(price)
