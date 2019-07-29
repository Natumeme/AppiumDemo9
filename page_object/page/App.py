#!usr/bin/env python
#-*- coding:utf-8 -*-

from page_object.driver.AndroidClient import AndroidClient
from page_object.page.MainPage import MainPage

class App(object):
	@classmethod
	def main(self)
		#初始化
		AndroidClient.restart_app()
		return MainPage()
