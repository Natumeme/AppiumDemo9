#!/usr/bin/env python
#-*-coding:utf-8-*-
from web.page_object.page.BasePage import BasePage


class ProfilePage(BasePage):
	def gotoSelected(self):
		return new SelectedPage()