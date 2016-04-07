# -*- coding: utf-8 -*-
"""
Created on Mon Mar 28 14:11:57 2016

@author: ccc
"""
# #历史行情数据
# from WindPy import w      
# from datetime import *
# w.start();#
# print(w.isconnected())
# #code=['600000.SH','600005.SH','600004.SH']    
# #field=['roe_avg','roa']    
# #print(w.wss(code,field,"rptDate=20121231"))
# q=w.wst("600000.SH", "ask,bid,volume", "2016-03-28 09:00:00", "2016-03-28 15:24:28", "")
# print(q.Codes)
# #
# #w.wsq("600000.SH,600005.SH", "rt_bsize1,rt_date,rt_time,rt_vol,rt_amt", func=DemoWSQCallback)
# w.close()

#订阅行情数据
from WindPy import *
w.start();

#open a file to write.
pf=open('d:/1.txt', 'w')
#define the callback function
def sep_fun(name,indata):
	if indata.ErrorCode!=0:
		print('error code:'+str(indata.ErrorCode)+'\n');
		return();

	global pl
	pl=name
	for k in range(0,len(indata.Fields)):
		if(indata.Fields[k] == "RT_TIME"):
			pl=pl+"\t"+str(indata.Data[k][0])
		if(indata.Fields[k] == "RT_LAST"):
			pl=pl+"\t"+str(indata.Data[k][0])
	pf.write(pl+"\n")
	print(pl);
	pf.flush()

w.wsq("IF.CFE","rt_time,rt_last",func=lambda x : sep_fun("IF",x))
w.wsq("000001.SZ","rt_time,rt_last",func=lambda x : sep_fun("000001",x))
w.wsq("600000.SH","rt_time,rt_last",func=lambda x : sep_fun("600000",x))
while 1: 
	1
