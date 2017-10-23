#!/usr/bin/python
#-*-coding:utf-8 -*-
import urllib.request
import urllib.parse
import re
from bs4 import BeautifulSoup
import csv  
import json
import redis


headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'
}  

class IPSpider:
     

    
     '''
     Created on Oct 22, 2017
     
     获取大量代理ip，存入redis中

     @author: Arius@github.com/Ariussssss
     @params: {integer} numpage 
     '''
    
     def get(numpage = 2): # 爬取numpage页数的代理IP存进redis
        # writer = open('ips.txt', 'w')        
        url='http://www.xicidaili.com/nn/'  
        temp=[]  
        for num in range(1,numpage+1):  
            ipurl=url+str(num)  
            print ('Now downloading the '+str(num*100)+' ips'  )
            request=urllib.request.Request(ipurl,headers=headers)  
            content=urllib.request.urlopen(request).read()  
            bs=BeautifulSoup(content,'html.parser')  
            res=bs.find_all('tr') 
            r = redis.Redis(host='127.0.0.1', port=6379,db=0)
            for item in res:  
                try:  
                    newdist = {}
                    tds=item.find_all('td')  
                    ipcode = tds[1].text
                    port = tds[2].text
                    newdist['ip'] = ipcode
                    newdist['port'] = port
                    # print('''ip: '%s': '%s'\n'''%(ipcode,port))
                    # temp.append(newdist)  
                    r.lpush('iplist',newdist) 

                except IndexError:  
                    pass 
        # writer.write(str(temp))  
        # writer.close( )                 
        return 1

     def __init__(self):
         super(IPSpider, self).__init__()
           
