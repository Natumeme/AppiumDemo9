#!usr/bin/env python
#-*- coding:utf-8 -*-
from page_object.page.App import App
import pytest


class TestLogin(object):
	@classmethod
	def setup_class(cls):
		cls.profilePage=App.main().gotoProfile()

	def setup_method(self):
		self.loginPage=self.profilePage.gotoLogin()

	@pytest.mark.parametrize("user,pw,msg",[
		("1500000","111111","手机号码"),
		("15600534760","111111","密码错误")
	])
	def test_login_password(self,user,pw,msg):
		#手机号错误
		self.loginPage.loginBypassword(user,pw)
		assert msg in self.loginPage.getErrorMsg()

	def teardown_method(self):
		self.loginPage.back()