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

cookies = {
    '_lxsdk_cuid': '15f336a3999c8-042db71adeba35-574e6e46-3d10d-15f336a399ac8',
    '_lxsdk': '15f336a3999c8-042db71adeba35-574e6e46-3d10d-15f336a399ac8',
    '_ga': 'GA1.2.1160483408.1508395875',
    '_gid': 'GA1.2.1915325613.1508395875',
    'wx_channel_id': '0',
    'webp': '1',
    'utm_source': '0',
    'w_latlng': '23129163,113264435',
    'wm_poi_view_id': '287098077500822',
    'poiid': '287098077500822',
    'w_cid': '110100',
    'w_cpy': 'beijing',
    'w_cpy_cn': '%E5%8C%97%E4%BA%AC',
    'w_visitid': '9465eba6-c50d-406e-b197-8763496bf50c',
    '__mta': '87858855.1508395879768.1508490339911.1508516292290.19',
    '_lxsdk_s': '15f3a93ec6c-ebe-4de-570%7C%7C2',
    'terminal': 'i',
    'w_utmz': 'utm_campaign=(direct)&utm_source=5000&utm_medium=(none)&utm_content=(none)&utm_term=(none)',
    'w_uuid': 'zLSZ6qkn47NTdNdbDnS0dnfYQeH0v6L6fxfPmNA4QDix0Wr8NFNj1DzGDMFjV9YX',
    'JSESSIONID': '14hzj21kblcohe40gkopamuey',
}

headers = {
	'Cookie': 'Cookie: _lxsdk_cuid=15f336a3999c8-042db71adeba35-574e6e46-3d10d-15f336a399ac8; _lxsdk=15f336a3999c8-042db71adeba35-574e6e46-3d10d-15f336a399ac8; _ga=GA1.2.1160483408.1508395875; webp=1; _ga=GA1.3.1160483408.1508395875; __mta=87858855.1508395879768.1508570760470.1508570773538.21; w_visitid=db528d8a-2230-4427-a485-ea00bbee81bd; wm_poi_view_id=72627838141288752; poiid=72627838141288752; wx_channel_id=0; utm_source=0; w_cid=440100; w_cpy_cn="%E5%B9%BF%E5%B7%9E"; w_cpy=guangzhou; w_latlng=23041400,113394930; JSESSIONID=1elb332b1ep25198in5p3mswho; __mta=87858855.1508395879768.1508570773538.1508674708395.22; _lxsdk_s=15f4404d262-257-bf9-81c%7C%7C7; terminal=i; w_utmz="utm_campaign=(direct)&utm_source=5000&utm_medium=(none)&utm_content=(none)&utm_term=(none)"; w_uuid=zLSZ6qkn47NTdNdbDnS0dnfYQeH0v6L6fxfPmNA4QDix0Wr8NFNj1DzGDMFjV9YX',
    'Origin': 'http://i.waimai.meituan.com',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.8',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Accept': 'application/json',
    'Referer': 'http://i.waimai.meituan.com/channel?category_type=101065&sort_type=2',
    'X-Requested-With': 'XMLHttpRequest',
    'Connection': 'keep-alive',
}

def meituan():
	driver = webdriver.PhantomJS(executable_path='../node_modules/phantomjs/bin/phantomjs')
	driver.implicitly_wait(1000)
	driver.get("http://i.waimai.meituan.com/channel?category_type=101065&category_text=%E7%BE%8E%E9%A3%9F")
	driver.save_screenshot('meituan.png')
	# print (driver.get_cookies())

	# print(driver.find_element_by_tag_name('li'))
	soup = BeautifulSoup(driver.page_source,'html.parser')
	# target = soup.json()
	# driver.refresh()
	# table = driver.find_element_by_id('m-playlist')
	# target = soup.findall('li',class_=r'fl rest-li')
	# target = soup.findall('section', class_=re.compile(r"shop-list"))
	# print (target.prettify())
	file_object = open('meituan.txt', 'w')
	file_object.write(soup.prettify())
	file_object.close( ) 

def meituan1():
  
	url = 'http://i.waimai.meituan.com/ajax/v6/poi/filter?category_type=101065&category_text=%E7%BE%8E%E9%A3%9F&_token=eJx9jm1rgzAUhf9LwH5p0LyoNYKUldpi2QardmwtZaQu0zCj1matZey/L4WOsS+7XHjOPRwu5xN0ySsIMTLDINAHoz0UuIwFlBKGIMj/ej7zINh1j1MQbkYogMzztxdjae4NZgRBjAK0hT/aG20hcc1eUokJgVLrNnQcaZ+4VFzaSkj9wWs7b5STl7yuRTXOuRZF051f9LkVEUYY+d7g1xS9jqx4ZE1iK4itmFk31GIzAP/9XTZKjCuuI0JtTBj26aCqiwhjahPfdakHTEWVmYqG71fyK/WVB1nUIARi0Wep7JMsHuL7x+VtJvtFlgfHfXM6phw1hycy7IZO5R6rpGhXs4d4NS+LtWpVU0zf5muRqna2e56nxWRyt5R78PUNmKd0Iw=='   
	data = [
	  ('uuid', 'zLSZ6qkn47NTdNdbDnS0dnfYQeH0v6L6fxfPmNA4QDix0Wr8NFNj1DzGDMFjV9YX'),
	  ('platform', '3'),
	  ('partner', '4'),
	  ('page_index', '0'),
	  ('apage', '1'),
	]
	params = (
	    ('category_type', '101065'),
	    ('sort_type', '2'),
	    ('_token', 'eJydjl9rgzAUxb9LwL0s1EQXGwUZSi3o1sLU mCRkTlnQ/1TNWuVse  lDnGXne58Dv3cLicD9D7r8DCSI4JgRikJogSbOiUEGMJQf7XMzUDgpc WQFrv0QUmsTIrkYo7z02NQQxoiiDP5roGdTu5F5TvgyBgxAnS1X54sJ4zfiiLrh4Z80ib2s1P7CmKar7nImibPvpWUynwsYII4PcDG0vvg0NwP / TWLUdiKt1RcT6Ge4pmKoyvmGsimdSybSh5nspli5sDLBligCMY44qMfe7d4m4SPMR DOKfnrr2cu ji0BJtVvm4wTt3omlFHtgxEWXajW/VOgjd1J92jrc9RuTJtsHnF2kkd I='),
	)
	print(shoplist(url,data,params)) 

def shoplist(url,data,params):  
	req = urllib.request.Request(url, headers=headers,data=data)
	params = urllib.parse.urlencode(data).encode(encoding='UTF8')
	# response = opener.open(req,params)
	response = urllib.request.urlopen(req, params)  
	jsonText = response.read() 
	html = gzip.decompress(jsonText)
	html = html.decode('utf-8') 
	html = json.loads(html)
	newdata = json.dumps(html['data']['poilist'][0]['name'], ensure_ascii=False, sort_keys=True, indent=4, separators=(',', ': '))
	# print(newdata)
	file_object = open('json-meituan2.txt', 'w',newline='\n')
	# file_object.write(html)
	new = ''
	for one in html['data']['poilist']:
		new += '\n'
		new += str(one['id'])
		new += '\n距离'
		new += str(one['distance'])
		new += '\n'
		new += str(one['name'])
		new += '\n月销量：'
		new += str(one['month_sale_num'])
		new += '\n'
		
	file_object.write(new)
	file_object.close( )
	return newdata

def foodlist(id):
	url = 'http://i.waimai.meituan.com/ajax/v8/poi/food?_token=eJx9jlFrgzAUhf9LwL40aGK0GkHKSm2xbINVO7aWMlKXxTCj1matZey/L4WOsZddLnznHg6X8wm69BVEGJmhEOiD0T4KR4EXYIQRgaD463khgmDXPU5BtAlQCKk/2l6Mpbk3mLoIYhSiLfzRPtlC1zN7SaUmBEqt28hxpH1iUjFpKy71B6vtolFOUbK65tW4YJqLpju/6HPL40uTkT/4NXmvYysJrElihYmVUOuGWHQG4L+/y0bxccV07BIbedgbVLWIMSY2oR4lwPRTueln+H4lu1JfeZCiBhHgiz7PZJ/myRDfPy5vc9kv8iI87pvTMWOoOTy5w27oVN6xSkW7mj0kq3kp1qpVjZi+zdc8U+1s9zzPxGRyt5R78PUNMzRzYQ=='
	data = [
		('wm_poi_id', id),
		('uuid', 'zLSZ6qkn47NTdNdbDnS0dnfYQeH0v6L6fxfPmNA4QDix0Wr8NFNj1DzGDMFjV9YX'),
		('platform', '3'),
		('partner', '4')
	]
	req = urllib.request.Request(url, headers=headers,data=data)
	params = urllib.parse.urlencode(data).encode(encoding='UTF8')
	# response = opener.open(req,params)
	response = urllib.request.urlopen(req, params)  
	jsonText = response.read() 
	html = gzip.decompress(jsonText)
	html = html.decode('utf-8') 
	html = json.loads(html)
	# newdata = json.dumps(html['data']['food_spu_tags'][0]['spus'][0]['id'], ensure_ascii=False, sort_keys=True, indent=4, separators=(',', ': '))
	newdata = json.dumps(html, ensure_ascii=False, sort_keys=True, indent=4, separators=(',', ': '))
	print(newdata)
	file_object = open('json-meituan-foodlist.txt', 'w',newline='\n')
	file_object.write(newdata)
	# new = ''
	# for one in html['data']['food_spu_tags']:
	# 	for two in one['spus']:
	# 		new += '\n'
	# 		new += str(two['id'])
	# 		new += '\n'
	# 		new += str(two['name'])
	# 		new += '\n月销量：'
	# 		new += str(two['month_saled_content'])
	# 		new += '\n'
		
	# file_object.write(new)
	file_object.close( )
	return newdata

def shopinfo(id):
	url = 'http://i.waimai.meituan.com/ajax/v6/poi/info?_token=eJxVkN1OwzAMhd8l19Ya58dJdsdULsboQKxCTNMuSpm2CnWgNtNgiHcnSakQUqR8Pjm2Y3+xbv7Cpsg5Rw7M94E1t1qjRCV5kOo/TTjnBGlgz91jzqYbwy04TdsoPIR4g05wQG75FkbWZgtChRNd82BiB+/fp1nWTM5V01bNpN01/lQdJ/Vbm3W73lenrjr6TBlCgyiMlZKsYcBYKNGWsYR2CERB0k6MIIFUAg2ECQiIJzADEMfhiTCYY0USCEaMIBNYMLEOSQKTPCo82QRihFERbjCnFjqCRlAuAncgY7qyBmTsrsLiROyllAWMf1ZSgP53G3ApRYFOI5ACVEMnEZLTT00gE20mjCODFrbymraygdldvo5x9bulODis7q+WUfRRDHff7I9synY3H+Wit/6zyIry9hqLsr4s85ov84Us8rXoL7Onq/3sYM/Vin3/AIoDfXE='
	data = [
		('wmpoiid', id),
		('uuid', 'zLSZ6qkn47NTdNdbDnS0dnfYQeH0v6L6fxfPmNA4QDix0Wr8NFNj1DzGDMFjV9YX'),
		('platform', '3'),
		('partner', '4')
	]
	req = urllib.request.Request(url, headers=headers,data=data)
	params = urllib.parse.urlencode(data).encode(encoding='UTF8')
	# response = opener.open(req,params)
	response = urllib.request.urlopen(req, params)  
	jsonText = response.read() 
	html = gzip.decompress(jsonText)
	html = html.decode('utf-8') 
	html = json.loads(html)
	newdata = json.dumps(html['data'], ensure_ascii=False, sort_keys=True, indent=4, separators=(',', ': '))
	# print(newdata)
	file_object = open('json-meituan-shop.txt', 'w',newline='\n')
	file_object.write(newdata)
	# new = ''
	# for one in html['data']['poilist']:
	# 	new += '\n'
	# 	new += str(one['id'])
	# 	new += '\n距离'
	# 	new += str(one['distance'])
	# 	new += '\n'
	# 	new += str(one['name'])
	# 	new += '\n月销量：'
	# 	new += str(one['month_sale_num'])
	# 	new += '\n'
		
	# file_object.write(new)
	file_object.close( )
	return newdata

# def maplist():
		
# meituan1()
# shopinfo('476171127833687')
foodlist('514593905332438')