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

	def setup_method(self):
		print("setup method 在每个测试用例执行之前执行一次")
		self.driver=self.restart_app()

	def test_action_p(self):
		rect=self.driver.get_window_rect()
		self.driver.find_element_by_xpath("//*[@text='基金' and @instance='9']").click()
		action=TouchAction(self.driver)
		for j in range(8):
			for i in range(5):
				action\
					.press(x=rect['width']*0.8,y=rect['height']*0.8)\
					.move_to(x=rect['width']*0.2,y=rect['height']*0.2)\
					.release().perform()
				time.sleep(2)
			action\
				.press(x=rect['width']*0.8,y=rect['height']*0.8)\
				.move_to(x=rect['width']*0.4,y=rect['height']*0.8)\
				.release()\
				.perform()

	def teardown_method(self):
		self.driver.quit()

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

