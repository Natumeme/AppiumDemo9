#!usr/bin/env python
#-*- coding:utf-8 -*-

import pytest
from page_object.page.MainPage import MainPage


class TestSelected(object):
	def test_price(self):
		main=MainPage()
		assert main.gotoSelected().getPriceByName("阿里巴巴") == 28.83

	def test_add_stock(self):
		pass