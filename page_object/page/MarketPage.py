#!usr/bin/env python
#-*- coding:utf-8 -*-
from page_object.driver.AndroidClient import AndroidClient


class SelectedPage(object):
	def addDefault(self):
		return self

	def getPriceByName(self,name) -> float:
		price = AndroidClient.driver\
			.find_element_by_xpath("//*[contains(@resource-id, 'stockName') and @text='%s']" %name +
             "/../../..//*[contains(@resource-id, 'currentPrice')]").text
		return float(price)

	def getMarketPrice(self):
		price = AndroidClient.driver.find_element_by_xpath("//*[@text='深证成指']/..//*[contains(@resource-id,'index_price') and @instance='12']")
