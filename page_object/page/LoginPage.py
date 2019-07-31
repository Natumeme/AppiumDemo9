#!usr/bin/env python
#-*- coding:utf-8 -*-
from time import sleep

from selenium.webdriver.common.by import By

from page_object.page.BasePage import BasePage

from selenium.webdriver.support.wait import WebDriverWait


class LoginPage(BasePage):
	_iv_login_phone=(By.ID,"iv_login_phone")
	_close_locator=(By.ID,"iv_action_back")
	_register_phone_number=(By.ID,"register_phone_number")
	_register_code=(By.ID,"register_code")
	_button_next = (By.ID, "button_next")
	_login_account=(By.ID,"login_account")
	_login_password=(By.ID,"login_password")
	_action_back=(By.ID,"action_back")
	_md_buttonDefaultNegative=(By.ID,"md_buttonDefaultNegative")
	_error_msg=(By.ID,"md_content")
	_tv_login_with_account=(By.ID,"tv_login_with_account")
	_iv_action_back=(By.ID,"iv_action_back")
	_back_locator=(By.XPATH,"//*[contains(@resource-id, 'iv_close') or contains(@resource-id, 'iv_action_back')]")
	_md_buttonDefaultNegative=(By.ID,"md_buttonDefaultNegative")

	def loginByWX(self):
		return self

	def loginByMSG(self,phone,code):
		return self

	def loginBypassword(self,account,password):
		self.find(self._tv_login_with_account).click()
		self.find(self._login_account).send_keys(account)
		self.find(self._login_password).send_keys(password)
		self.find(self._button_next).click()
		return self

	def loginSuccessBypassword(self,account,password):
		from page_object.page.MainPage import MainPage
		return MainPage()

	def back(self):
		self.find(self._back_locator).click()
		self.find(self._md_buttonDefaultNegative).click()
		from page_object.page.ProfilePage import ProfilePage
		#todo:
		return ProfilePage()

	def getErrorMsg(self):
		msg=self.find(self._error_msg).text
		self.findByText("确定").click()
		return msg
