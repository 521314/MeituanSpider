#!/usr/bin/python
#-*-coding:utf-8 -*-
import redis
from ipspider import IPSpider
import telnetlib

	
class AgentController:
	'''
    Created on Oct 22, 2017

    获取可用代理ip
     
    @author: Arius@github.com/Ariussssss
    '''	
		
	def getip(self):
		r = redis.Redis(host='127.0.0.1', port=6379,db=0)
		# r.ltrim('iplist',0,0)	
		if r.llen('iplist') == 0:
			IPSpider.get()	
		ip_agent = r.lpop("iplist")
		ip_agent = ip_agent.decode('utf-8')
		ip_agent = eval(ip_agent)

		while self.check(ip_agent):
			if r.llen('iplist') == 0:
				IPSpider.get()	
			ip_agent = r.lpop("iplist")
			ip_agent = ip_agent.decode('utf-8')
			ip_agent = eval(ip_agent)
			pass

		print (r.llen('iplist'))   #获取
		print (ip_agent['ip'])   #获取
		return ip_agent

	'''
	Created on Oct 22, 2017
     
    检查ip是否可用
     
    @author: Arius@github.com/Ariussssss
    @params: {integer} numpage 
    '''	
	def check(self,ip_agent): # 需要测试的IP
		print ('checking %s : %s '%(ip_agent['ip'],ip_agent['port']))
		try:
		    telnetlib.Telnet(ip_agent['ip'], port=ip_agent['port'], timeout=5)
		except:
		    print ('connect failed')
		    return True
		else:			
		    print ('success')
		    return False
	
	def __init__(self):
		super(AgentController, self).__init__()

# IPspider.get(10)	
test = AgentController()
# ip_agent = {'ip': '123.55.185.48', 'port': '25365'}
# test.check(ip_agent)
test.getip()

