#!usr/bin/env python
#-*- coding:utf-8 -*-
from selenium.webdriver.common.by import By

from page_object.driver.AndroidClient import AndroidClient
from page_object.page.BasePage import BasePage
from page_object.page.MarketPage import MarketPage
from page_object.page.ProfilePage import ProfilePage
from page_object.page.SearchPage import SearchPage
from page_object.page.SelectedPage import SelectedPage

class MainPage(BasePage):
	_profile_button=(By.ID,"user_profile_icon")
	_search_button=(By.ID,"home_search")
	def gotoSelected(self):
		#调用全局的driver对象使用webdriver api操纵app
		zixuan=("自选")
		self.findByText(zixuan)
		self.findByText(zixuan).click()

		return SelectedPage()

	def gotoMarket(self):
		# AndroidClient.driver.find_element_by_xpath("//*[@text='行情']")
		# AndroidClient.driver.find_element_by_xpath("//*[@text='行情']").click()

		market=("行情")
		self.findByText(market)
		self.findByText(market).click()

		return MarketPage()

	def gotoSearch(self):
		self.find(self._search_button).click()
		return SearchPage()

	def gotoProfile(self):
		self.find(MainPage._profile_button).click()
		return ProfilePage()