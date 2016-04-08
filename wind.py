# -*- coding: utf-8 -*-
"""
Created on Mon Mar 28 14:11:57 2016

@author: ccc
"""

# 公式生成器 wind  qnt cg

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
	global tpl
	tpl=name
	for k in range(0,len(indata.Fields)):
		tpl=tpl+","+str(indata.Data[k][0])
		if(indata.Fields[k] == "RT_TIME"):
			pl=pl+","+str(indata.Data[k][0])
		if(indata.Fields[k] == "RT_LAST"):
			pl=pl+","+str(indata.Data[k][0])
	pf.write(pl+"\n")
	pf.write(tpl+"\n")
	
	print(pl);
	print(tpl);
	pf.flush()

querylist="rt_date,rt_time,rt_last,rt_last_amt,rt_last_vol,rt_latest,rt_vol,rt_amt,rt_oi_chg,rt_ask1,rt_ask2,rt_ask3,rt_ask4,rt_ask5,rt_ask6,rt_ask7,rt_ask8,rt_ask9,rt_ask10,rt_bid1,rt_bid2,rt_bid3,rt_bid4,rt_bid5,rt_bid6,rt_bid7,rt_bid8,rt_bid9,rt_bid10,rt_bsize1,rt_bsize2,rt_bsize3,rt_bsize4,rt_bsize5,rt_bsize6,rt_bsize7,rt_bsize8,rt_bsize9,rt_bsize10,rt_asize1,rt_asize2,rt_asize3,rt_asize4,rt_asize5,rt_asize6,rt_asize7,rt_asize8,rt_asize9,rt_asize10";
w.wsq("IF.CFE",querylist,func=lambda x : sep_fun("IF",x))
w.wsq("000001.SZ",querylist,func=lambda x : sep_fun("000001",x))
w.wsq("600000.SH",querylist,func=lambda x : sep_fun("600000",x))
while 1: 
	1
