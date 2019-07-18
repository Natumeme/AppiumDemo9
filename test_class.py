#!usr/bin/env python
#-*- coding:utf-8 -*-

import pytest

'''
在类之前和之后执行一次
setup_class
teardown_class
'''

class TestClass(object):
	def setup_class(self):
		print("setup_class(self):每个类之前执行一次")

	def teardown_class(self):
		print("teardown_class(self):每个类之后执行一次")

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
