#!usr/bin/env python
#-*- coding:utf-8 -*-
from page_object.page.App import App


class TestLogin(object):
	@classmethod
	def setup_class(cls):
		cls.loginPage=App.main().gotoProfile().gotoLogin()

	def setup_method(self):
		pass

	def test_login_password(self):
		#手机号错误
		self.loginPage.loginBypassword("12345678901","123456")
		assert "手机号码" in self.loginPage.getErrorMsg()

		#密码错误
		self.loginPage.loginBypassword("12345678901", "12345e6")
		assert "密码" in self.loginPage.getErrorMsg()
	def teardown_method(self):
		pass