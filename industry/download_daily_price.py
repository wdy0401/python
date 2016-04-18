#get stock file list
	#read stock list
	#mkdir for industry
		#data of each stock

from WindPy import *
w.start();

print(w.wsd("000159.SZ", "sec_name,close,pe_ttm", "2010-01-01", "2016-04-17", "PriceAdj=F"))