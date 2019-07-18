#!usr/bin/env python
#-*- coding:utf-8 -*-

import pytest

'''
开始于方法始末（在类中）
setup_method
teardown_method
'''

class TestMethod(object):
	def setup_class(self):
		print("setup_class(self)：每个类之前执行一次\n")

	def teardown_class(self):
		print("teardown_class(self)：每个类之后执行一次")

	def setup_method(self):
		print("setup_method(self):在每个方法之前执行")

	def teardown_method(self):
		print("teardown_method(self):在每个方法之后执行\n")

	def add(self,a,b):
		print("这是加法运算")
		return a+b

	def test_01(self):
		print("正在执行test1")
		x="this"
		assert 'h' in x

	def test_add(self):
		print("正在执行test_add()")
		assert self.add(3,4) == 7

