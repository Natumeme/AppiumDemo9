#!usr/bin/env python
#-*- coding:utf-8 -*-
from page_object.driver.AndroidClient import AndroidClient


class BasePage(object):
	def __init__(self):
		self.driver=AndroidClient.driver