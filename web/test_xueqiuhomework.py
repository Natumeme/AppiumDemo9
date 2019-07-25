#!/usr/bin/env python
#-*-coding:utf-8-*-

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

class Testhomework(object):
	def setup(self):
		self.driver = webdriver.Chrome()
		self.driver.implicitly_wait(10)
		self.driver.get("https://xueqiu.com/")

	def test_alibaba(self):
		driver = self.driver
		search = driver.find_element_by_name('q')
		search.send_keys('阿里巴巴')
		search.send_keys(Keys.ENTER)

		driver.find_element_by_xpath('//*[contains(text(),"1688")]/../../../..//i[@class="iconfont"]').click()
		sleep(2)
		driver.find_element_by_name('username').send_keys('test@00.com')
		driver.find_element_by_name('password').send_keys('111111')
		driver.find_element_by_css_selector('.modal__login__btn').click()

	def teardown(self):
		self.driver.quit()