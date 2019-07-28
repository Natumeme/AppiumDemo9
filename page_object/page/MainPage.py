#!usr/bin/env python
#-*- coding:utf-8 -*-
from selenium.webdriver.common.by import By

from page_object.driver.AndroidClient import AndroidClient
from page_object.page.BasePage import BasePage
from page_object.page.MarketPage import MarketPage
from page_object.page.SelectedPage import SelectedPage

class MainPage(BasePage):
	def gotoSelected(self):
		#调用全局的driver对象使用webdriver api操纵app
		# self.driver.find_element(BY.xpath,"//*[@text='自选']")
		zixuan=(By.XPATH,"//*[@text='自选']")
		self.find(zixuan)
		#self.driver.find_element_by_xpath("//*[@text='自选']")
		self.find(zixuan).click()
		#self.driver.find_element_by_xpath("//*[@text='自选']").click()

		return SelectedPage()

	def gotoMarket(self):
		# AndroidClient.driver.find_element_by_xpath("//*[@text='行情']")
		# AndroidClient.driver.find_element_by_xpath("//*[@text='行情']").click()

		market=(By.XPATH,"//*[@text='行情']")
		self.find(market)
		self.find(market).click()

		return MarketPage()