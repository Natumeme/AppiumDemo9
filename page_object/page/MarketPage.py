#!usr/bin/env python
#-*- coding:utf-8 -*-
from selenium.webdriver.common.by import By

from page_object.driver.AndroidClient import AndroidClient
from page_object.page.BasePage import BasePage


class MarketPage(BasePage):
	def addDefault(self):
		return self

	def getMarketPrice(self,name) -> float:
		price_Locator=(By.XPATH,"//*[@text='%s']" %name+ "/..//*[contains(@resource-id,'index_price') and @instance='12']")
		price=self.find(price_Locator).text

		return float(price)
