#!usr/bin/env python
#-*- coding:utf-8 -*-

from selenium.webdriver.common.by import By
from page_object.page.BasePage import BasePage
from page_object.page.LoginPage import LoginPage


class ProfilePage(BasePage):
	def gotoLogin(self):
		login_button=(By.ID,"iv_login_phone")
		self.find(login_button).click()
		return LoginPage()