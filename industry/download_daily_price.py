#get stock file list
	#read stock list
	#mkdir for industry
		#data of each stock

#from WindPy import *
#w.start();

a=w.wsd('000637.SZ','close,industry_sw,industry_swcode,indexcode_sw,industry_citic,industry_citiccode,industry_gx,industry2,industrycode,industryname','2016-04-01','2016-04-18','industryType=1','category=1','industryStandard=1','PriceAdj=F')

column=len(a.Data)
row=len(a.Data[1])
for i in range(row):
	print(a.Times[i],end=",")
	for j in range(column):
		print(a.Data[j][i],end=",")
	print('')
	