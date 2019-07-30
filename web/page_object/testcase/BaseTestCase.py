#!/usr/bin/env python
#-*-coding:utf-8-*-
import logging


class BaseTestCase(object):
	logging.basicConfig()
	_log=logging.getLogger("xueqiu")
	_log.setLevel(logging.DEBUG)

	#log 属性的封装
	@property
	def log(self):
		return self._log
