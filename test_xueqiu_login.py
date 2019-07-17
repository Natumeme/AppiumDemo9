#!usr/bin/env python
#-*- coding:utf-8 -*-
import time

from appium import webdriver
import pytest
from appium.webdriver.common.touch_action import TouchAction
from appium.webdriver.webdriver import WebDriver

class TestXueqiuAndroid(object):
	driver=WebDriver
	@classmethod
	def setup_class(cls):
		print("setup class 在当前类下的所有用例执行之前只执行一次")
		cls.driver=cls.install_app()

		el1 = cls.driver.find_element_by_id("user_profile_icon")
		el1.click()

	def setup_method(self):
		print("setup method 在每个测试用例执行之前执行一次")
		#获取启动的qppium的driver实例，用于后续每个case的driver
		self.driver=WebDriver
		self.driver=TestXueqiuAndroid.driver

	def test_login_phone(self):
		el2 = self.driver.find_element_by_id("iv_login_phone")
		el2.click()

	def test_login_password(self):
		el2 = self.driver.find_element_by_id("iv_login_phone")
		el2.click()
		self.driver.find_element_by_xpath("//*[@text='邮箱手机号密码登录']").click()

	def teardown_method(self):
		#不加也没关系，如果不quit，启动appium会自动quit之前的session
		self.driver.back()
		self.driver.find_element_by_xpath("//*[@text='狠心离开' and @instance='1']").click()

	@classmethod
	def install_app(cls) -> WebDriver:
		caps = {}
		#如果有必要，进行第一次安装
		#caps["app] = ''
		caps["platformName"] = "android"
		caps["deviceName"] = "hogwarts"
		caps["appPackage"] = "com.xueqiu.android"
		caps["appActivity"] = ".view.WelcomeActivityAlias"
		caps["autoGrantPermissions"] = "true"
		#解决第一次启动的问题
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
		#为了更快的启动，并保留之前的数据，从而保存上一个case执行后的状态
		caps["noReset"] = True
		driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
		driver.implicitly_wait(10)
		return driver

