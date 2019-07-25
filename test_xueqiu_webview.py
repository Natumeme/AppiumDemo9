#!usr/bin/env python
#-*- coding:utf-8 -*-

import time
from appium import webdriver
import pytest
from appium.webdriver.common.touch_action import TouchAction
from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.remote.mobile import MobileBy
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class TestXueqiuAndroid(object):
	driver=WebDriver
	@classmethod
	def setup_class(cls):
		print("setup class 在当前类下的所有用例执行之前只执行一次")
		cls.driver=cls.restart_app()
		WebDriverWait(cls.driver, 20).until(EC.presence_of_element_located(MobileBy.xpath, "//*[@text='交易']"))
		cls.driver.find_element_by_xpath("//*[@text='交易']").click()

	def setup_method(self):
		print("setup method 在每个测试用例执行之前执行一次")
		self.driver=TestXueqiuAndroid.driver
		self.driver.find_element_by_xpath("//*[@text='交易']").click()

	def test_webview_simulator(self):
		self.driver.find_element_by_accessibility_id('A股开户').click()
		self.driver.find_element_by_accessibility_id('立即开户')
		WebDriverWait(self.driver,20).until(EC.presence_of_element_located(MobileBy.ACCESSIBILITY_ID,'立即开户'))

	def teardown_method(self):
		self.driver.back()

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

