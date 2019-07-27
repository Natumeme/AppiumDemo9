#!/usr/bin/env python
#-*-coding:utf-8-*-
from appium import webdriver
from appium.webdriver import WebDriver


class AndroidClient(object):
	driver:WebDriver
	@classmethod
	def install_app(cls) -> WebDriver:
		caps = {}
		# 如果有必要，进行第一次安装
		# caps["app] = ''
		caps["platformName"] = "android"
		caps["deviceName"] = "hogwarts"
		caps["appPackage"] = "com.xueqiu.android"
		caps["appActivity"] = ".view.WelcomeActivityAlias"
		caps["autoGrantPermissions"] = "true"
		# 解决第一次启动
		# caps["noReset"] = True
		cls.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
		cls.driver.implicitly_wait(10)
		return cls.driver

	@classmethod
	def restart_app(cls) -> WebDriver:
		caps = {}
		caps["platformName"] = "android"
		caps["deviceName"] = "hogwarts"
		caps["appPackage"] = "com.xueqiu.android"
		caps["appActivity"] = ".view.WelcomeActivityAlias"
		# caps["autoGrantPermissions"] = "true"
		# 为了更快的启动，并保留之前的数据，从而保存上一个case执行后的状态
		caps["noReset"] = True
		cls.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
		cls.driver.implicitly_wait(10)
		return cls.driver
