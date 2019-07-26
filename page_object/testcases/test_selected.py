#!usr/bin/env python
#-*- coding:utf-8 -*-

import pytest
from page_object.pages.MainPage import MainPage


class TestSelected(object):
	def test_price(self):
		main=MainPage()
		assert main.gotoSelected().getPriceByName("科大讯飞") == 28.83

	def test_add