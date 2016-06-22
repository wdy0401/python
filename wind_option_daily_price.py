from WindPy import *
w.start();


def download(ctr,begdt,enddt,info):    
    a=w.wsd(ctr, info, begdt, enddt, "")
    fo=open("e:/tmp.txt","w",encoding='utf-8',errors='ignore')
    fo.write("date,"+info+"\n")
    col=len(a.Times)
    row=len(a.Data[1])
    for r in range(row):
        d=list()
        for c in range(col):
            d.append(str(a.Data[c][r]))
        e=",".join(d)
        e=str(a.Times[r])+","+e+"\n"
        fo.write(e)
    fo.close()

ctr="10000449.SH"
bd="2016-05-17"
ed="2016-06-15"
info="open,high,low,close,volume,amt,chg,oi,oi_chg,delta,gamma,vega,theta,rho,underlyinghisvol_30d,us_hisvol,underlyinghisvol_90d,us_impliedvol,ptmtradeday,ptmday"
download(ctr,bd,ed,info)
