#!/usr/bin/python
#-*-coding:utf-8 -*-
import json
import urllib.request
import urllib.parse
import re
from bs4 import BeautifulSoup
import os
from selenium import webdriver
import time
import gzip
import http.cookiejar
import pymysql

class MeituanSpider(object):

	def getCookie(self):
		pass

	def getIp(self):
		pass

	def getShopInfo(self, id):
		url = 'http://i.waimai.meituan.com/ajax/v6/poi/info'
		data = [
			('wmpoiid', id),
			('uuid', 'zLSZ6qkn47NTdNdbDnS0dnfYQeH0v6L6fxfPmNA4QDix0Wr8NFNj1DzGDMFjV9YX'),
			('platform', '3'),
			('partner', '4')
		]
		res = self.bsRequest(url, headers, data)
		pass

	def getShopFood(self):
		pass	

	def dbConect(self):

		db = pymysql.connect("localhost","root","root","patch_restaurant",charset='utf8')
		cursor = db.cursor()
		
		return cursor

	def bsRequest(self,url, headers, data):
		req = urllib.request.Request(url, headers=headers,data=data)
		params = urllib.parse.urlencode(data).encode(encoding='UTF8')
		# response = opener.open(req,params)
		response = urllib.request.urlopen(req, params)  
		jsonText = response.read() 
		html = gzip.decompress(jsonText)
		html = html.decode('utf-8') 
		html = json.loads(html)
		return html

	def collect(self):
		cursor = self.dbConect()
		sql = "SELECT * FROM place WHERE id < 871 "
		data = cursor.execute(sql)
		data = cursor.fetchall()
		aproxy = {'http': '110.73.41.100:8123'}
		num = 0
		print(data[0][3])
		# for x in data:
		# 	if num > 26 :
		# 		print(x[0])
		# 		city = urllib.parse.quote(x[0])
		# 		self.find(city, aproxy, 1)
		# 	num += 1


	'''
	Created on Oct 23, 2017
     
    链接数据库

    @author: Arius@github.com/Ariussssss
    '''
	def dbConect(self):
		db = pymysql.connect("localhost","root","root","patch_restaurant",charset='utf8')
		cursor = db.cursor()
		return cursor

	def check (self, id):
		cursor = self.dbConect()
		sql = "SELECT * FROM shop WHERE placeid = '%s' "%id
		data = cursor.execute(sql)
		data = cursor.fetchall()
		if data:
			# print(data)
			return False
		else:
			# print('new')
			return True

	def __init__(self):
		super(MeituanSpider, self).__init__()
		
test = MeituanSpider()
test.collect()