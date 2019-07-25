#!usr/bin/env python
#-*- coding:utf-8 -*-
import time

from appium import webdriver
import pytest
from appium.webdriver.webdriver import WebDriver

class TestXueqiuLogin(object):
	driver=WebDriver
	@classmethod
	def setup_class(cls):
		print("setup class 在当前类下的所有用例执行之前只执行一次")
		cls.driver=cls.install_app()
		cls.driver.find_element_by_id("user_profile_icon").click()
		cls.driver.find_element_by_id("iv_login_phone").click()
		cls.driver.find_element_by_id("tv_login_with_account").click()

	def setup_method(self):
		print("setup method 在每个测试用例执行之前执行一次")
		self.driver=WebDriver
		self.driver=TestXueqiuLogin.driver

	def test_login_password(self):
		self.driver.find_element_by_id("login_account").send_keys("123")
		self.driver.find_element_by_id("login_password").send_keys("123")
		self.driver.find_element_by_xpath("//*[@text='登录' and @instance='3']").click()

	def teardown_method(self):
		self.driver.back()
		self.driver.find_element_by_xpath("//*[@text='狠心离开' and @instance='1']").click()

	@classmethod
	def install_app(cls) -> WebDriver:
		caps = {}
		caps["platformName"] = "android"
		caps["deviceName"] = "hogwarts"
		caps["appPackage"] = "com.xueqiu.android"
		caps["appActivity"] = ".view.WelcomeActivityAlias"
		caps["autoGrantPermissions"] = "true"
		# caps["noReset"] = True
		driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
		driver.implicitly_wait(10)
		return driver

	@classmethod
	def restart_app(cls) -> WebDriver:
		caps = {}
		caps["platformName"] = "android"
		caps["deviceName"] = "hogwarts"
		caps["appPackage"] = "com.xueqiu.android"
		caps["appActivity"] = ".view.WelcomeActivityAlias"
		# caps["autoGrantPermissions"] = "true"
		caps["noReset"] = True
		driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
		driver.implicitly_wait(10)
		return driver

