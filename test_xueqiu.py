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
		#获取启动的qppium的driver实例，用于后续每个case的driver
		self.driver=self.restart_app()

	def test_login(self):
		el1 = self.driver.find_element_by_id("user_profile_icon")
		el1.click()
		el2 = self.driver.find_element_by_id("iv_login_phone")
		el2.click()

	def test_jijin(self):
		self.driver.find_element_by_xpath("//*[@text='基金' and @instance='9']")

	def test_swipe(self):
		self.driver.find_element_by_xpath("//*[@text='基金' and @instance='9']")
		for i in range(5):
			self.driver.swipe(500,1000,200,200)
			time.sleep(2)

	def test_action(self):
		self.driver.find_element_by_xpath("//*[@text='基金' and @instance='9']")
		action=TouchAction(self.driver)
		for i in range(5):
			action.press(x=500,y=1000).move_to(x=200,y=200).release().perform()
			time.sleep(2)

	def test_window_size(self):
		print(self.driver.get_window_rect())

	def test_action_p(self):
		rect=self.driver.get_window_rect()
		self.driver.find_element_by_xpath("//*[@text='基金' and @instance='9']")
		action=TouchAction(self.driver)
		for i in range(5):
			action\
				.press(x=rect['width']*0.8,y=rect['height']*0.8)\
				.move_to(x=rect['width']*0.2,y=rect['height']*0.2)\
				.release().perform()
			time.sleep(2)
			#截图
			self.driver.get_screenshot_as_file(str(i) + '.png')

	def teardown_method(self):
		#不加也没关系，如果不quit，启动appium会自动quit之前的session
		self.driver.quit()

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

