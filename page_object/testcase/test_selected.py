#!usr/bin/env python
#-*- coding:utf-8 -*-

import pytest

from page_object.page.App import App
from page_object.page.MainPage import MainPage


class TestSelected(object):
	def test_price(self):
		assert App.main().gotoSelected().getPriceByName("科大讯飞") == 33.82

	def test_add_stock(self):
		pass

	def test_market(self):
		assert  App.main().gotoMarket().getMarketPrice('深证成指') > 8000