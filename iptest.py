# -*- coding: UTF-8 -*-
import urllib.request
from AgentController import AgentController


#访问网址
url = 'https://restapi.amap.com/v3/place/text?s=rsv3&children=&key=3f3868abdb36336114bde5ab6eecdb68&types=%E5%95%86%E5%8A%A1%E4%BD%8F%E5%AE%85%7C%E5%AD%A6%E6%A0%A1%E4%BF%A1%E6%81%AF%7C%E7%94%9F%E6%B4%BB%E6%9C%8D%E5%8A%A1%7C%E5%85%AC%E5%8F%B8%E4%BC%81%E4%B8%9A%7C%E9%A4%90%E9%A5%AE%E6%9C%8D%E5%8A%A1%7C%E8%B4%AD%E7%89%A9%E6%9C%8D%E5%8A%A1%7C%E4%BD%8F%E5%AE%BF%E6%9C%8D%E5%8A%A1%7C%E4%BA%A4%E9%80%9A%E8%AE%BE%E6%96%BD%E6%9C%8D%E5%8A%A1%7C%E5%A8%B1%E4%B9%90%E5%9C%BA%E6%89%80%7C%E5%8C%BB%E9%99%A2%E7%B1%BB%E5%9E%8B%7C%E9%93%B6%E8%A1%8C%E7%B1%BB%E5%9E%8B%7C%E9%A3%8E%E6%99%AF%E5%90%8D%E8%83%9C%7C%E7%A7%91%E6%95%99%E6%96%87%E5%8C%96%E6%9C%8D%E5%8A%A1%7C%E6%B1%BD%E8%BD%A6%E6%9C%8D%E5%8A%A1&offset=10&city=%E5%B9%BF%E5%B7%9E&page=1&language=zh_cn&callback=jsonp_797043_&platform=JS&logversion=2.0&sdkversion=1.3&appname=http%3A%2F%2Fi.waimai.meituan.com%2Fguangzhou%3Fcity_id%3D440100&csid=B0130858-D5AC-42C1-A46F-2B572388E2C1&keywords='
# 这是代理IP
test = AgentController()
# proxy = {'ip': '221.10.159.234', 'port': '1337'}
proxy = test.getip()


proxy = { 'http':proxy['ip'] + ':' + proxy['port']}
print(proxy)
#创建ProxyHandler
proxy_support = urllib.request.ProxyHandler(proxy)
#创建Opener
opener = urllib.request.build_opener(proxy_support)
#添加User Angent
opener.addheaders = [('User-Agent','Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36')]
#安装OPener
urllib.request.install_opener(opener)
response=urllib.request.urlopen(url)
# print(page.read().decode('utf-8'))


# #使用自己安装好的Opener
# response = request.urlopen(url)
# #读取相应信息并解码
html = response.read().decode("utf-8")
#打印信息
print(html)
print(response.info())	