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


url = 'http://i.waimai.meituan.com/home?lat=44.026508&lng=114.965877'
get_url = 'http://i.waimai.meituan.com/ajax/v6/poi/filter?category_type=101065&category_text=%E7%BE%8E%E9%A3%9F'
user_agent = r'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36'
headers = {'User-Agent': user_agent}
data = [
  ('uuid', 'zLSZ6qkn47NTdNdbDnS0dnfYQeH0v6L6fxfPmNA4QDix0Wr8NFNj1DzGDMFjV9YX'),
  ('platform', '3'),
  ('partner', '4'),
  ('page_index', '0'),
  ('apage', '1'),
]
cookie_jar = http.cookiejar.MozillaCookieJar(cookie_filename)
handler = urllib.request.HTTPCookieProcessor(cookie_jar)
urllib.install_opener(opener);
resp = urllib.urlopen(url);   
for index, cookie in enumerate(cj):
    print ('[',index, ']',cookie)

# cookie_filename = 'cookie_jar.txt'
# cookie_jar = http.cookiejar.MozillaCookieJar(cookie_filename)
# handler = urllib.request.HTTPCookieProcessor(cookie_jar)
# opener = urllib.request.build_opener(handler)

# request = urllib.request.Request(url, headers=headers)
# try:
#   urllib.request.install_opener(opener)
#   response=urllib.request.urlopen(url)
# 	# print(response.read().decode())
# except urllib.error.URLError as e:
#   print(e.code, ':', e.reason)

# cookie_jar.save(ignore_discard=True, ignore_expires=True)  # 保存cookie到cookie.txt中
# for item in cookie_jar:
#     print('Name = ' + item.name)

# get_request = urllib.request.Request(get_url, headers=headers, data=data)
# opener = urllib.request.build_opener(handler)
# get_response=urllib.request.urlopen(url)
# print(get_response.read().decode('utf-8'))