#!/usr/bin/python
#-*-coding:utf-8 -*-
import re
import json
import urllib.request
import urllib.parse
import pymysql
from AgentController import AgentController


class AllPlace(object):
	'''
	Created on Oct 23, 2017
	
    获取所有省份名称，返回为urlencode格式

    @author: Arius@github.com/Ariussssss
    '''

	def main(self):
		cursor = self.dbConect()
		sql = "SELECT city_name FROM map "
		data = cursor.execute(sql)
		data = cursor.fetchall()
		aproxy = {'http': '110.73.41.100:8123'}
		num = 0
		for x in data:
			if num > 500 :
				print(x[0])
				city = urllib.parse.quote(x[0])
				self.find(city, aproxy, 1)
			num += 1


	'''
	Created on Oct 23, 2017
     
    链接数据库

    @author: Arius@github.com/Ariussssss
    '''
	def dbConect(self):
		db = pymysql.connect("localhost","root","root","patch_restaurant",charset='utf8')
		cursor = db.cursor()
		return cursor

	'''
	Created on Oct 23, 2017
     
	根据城市寻找地区

	@author: Arius@github.com/Ariussssss
	@params(string) city
	'''
	def find(self, city, proxy, page = 1):# city为urlencode格式
		headers = [('User-Agent','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36')]
		# proxy = {'http': '110.73.41.100:8123'}
		url = self.createUrl(city,page)
		proxy_support = urllib.request.ProxyHandler(proxy)
		opener = urllib.request.build_opener(proxy_support)
		opener.addheaders = headers
		urllib.request.install_opener(opener)
		response = urllib.request.urlopen(url)
		# print(response.read().decode("utf-8"))
		html = response.read().decode("utf-8")
		html = self.loads_jsonp(html)
		if html == 1:
			newIp = self.newIp()
			print(newIp)
			self.find(city, newIp, page)
		else:
			for x in html["pois"]:
				self.save(x)
			page += 1
			if page * 10 < int(html['count']):
				self.find(city, proxy, page)

	def newIp(self):
		test = AgentController()
		proxy = test.getip()
		proxy = { 'http':proxy['ip'] + ':' + proxy['port']}
		return proxy

	def loads_jsonp(self, _jsonp):
		try:
			return json.loads(re.match(".*?({.*}).*",_jsonp,re.S).group(1))
		except:
			return 1
	
	'''
	Created on Oct 23, 2017
	 
    生成爬取的url

    @author: Arius@github.com/Ariussssss
    @params(string) city
    @params(integer) page
    '''
	def createUrl(self, city, page):# 爬取的页面请求数据
		url = 'https://restapi.amap.com/v3/place/text?s=rsv3&children=&key=3f3868abdb36336114bde5ab6eecdb68&types=%E5%95%86%E5%8A%A1%E4%BD%8F%E5%AE%85%7C%E5%AD%A6%E6%A0%A1%E4%BF%A1%E6%81%AF%7C%E7%94%9F%E6%B4%BB%E6%9C%8D%E5%8A%A1%7C%E5%85%AC%E5%8F%B8%E4%BC%81%E4%B8%9A%7C%E9%A4%90%E9%A5%AE%E6%9C%8D%E5%8A%A1%7C%E8%B4%AD%E7%89%A9%E6%9C%8D%E5%8A%A1%7C%E4%BD%8F%E5%AE%BF%E6%9C%8D%E5%8A%A1%7C%E4%BA%A4%E9%80%9A%E8%AE%BE%E6%96%BD%E6%9C%8D%E5%8A%A1%7C%E5%A8%B1%E4%B9%90%E5%9C%BA%E6%89%80%7C%E5%8C%BB%E9%99%A2%E7%B1%BB%E5%9E%8B%7C%E9%93%B6%E8%A1%8C%E7%B1%BB%E5%9E%8B%7C%E9%A3%8E%E6%99%AF%E5%90%8D%E8%83%9C%7C%E7%A7%91%E6%95%99%E6%96%87%E5%8C%96%E6%9C%8D%E5%8A%A1%7C%E6%B1%BD%E8%BD%A6%E6%9C%8D%E5%8A%A1&offset=10&'
		url +='city='
		url += str(city)
		url += '&page='
		url += str(page)
		url += '&language=zh_cn&callback=jsonp_453999_&platform=JS&logversion=2.0&sdkversion=1.3&appname=http%3A%2F%2Fi.waimai.meituan.com'
		return url
	'''
	Created on Oct 23, 2017
     
    生成爬取的url

    @author: Arius@github.com/Ariussssss
    @params(list) data
    '''
	def save (self,data):
		db = pymysql.connect("localhost","root","root","patch_restaurant",charset='utf8')
		cursor = db.cursor()
		if self.check(data['id']):
			print(data['id'])
			arr = (data['id'],data['name'].replace("'",''),data['location'],data['pname'],data['cityname'],data['adname'])
			sql = """INSERT INTO place(placeid,name,location,pname,cityname,adname)
				VALUES ('%s', '%s', '%s', '%s', '%s', '%s') """%\
				arr
			cursor.execute(sql)
			db.commit()
		else: 
			print('existed')

	'''
	Created on Oct 23, 2017
     
    检查地址是否重复保存

    @author: Arius@github.com/Ariussssss
    @params(integer) id
    '''
	def check (self, id):
		cursor = self.dbConect()
		sql = "SELECT * FROM place WHERE placeid = '%s' "%id
		data = cursor.execute(sql)
		data = cursor.fetchall()
		if data:
			# print(data)
			return False
		else:
			# print('new')
			return True

	def __init__(self):
		super(AllPlace, self).__init__()


test = AllPlace()
test.main()
# aproxy = {'http': '110.73.41.100:8123'}
# test.find('%E5%B9%BF%E5%B7%9E', aproxy, 1)