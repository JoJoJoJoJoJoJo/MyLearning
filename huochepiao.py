#-*- coding=gbk -*-
import requests
import time
import sys

#global
station={'�Ϻ�':'SHH','�˳�':'YNV','����Ͽ':'SMF','��ϲ':'WXV','̫ԭ':'TYV','����':'JXV','����':'SZH'}

try:
	start = station.get(sys.argv[1])
	terminal = station.get (sys.argv[2])
except KeyError:
	print 'Wrong Argv'
finally:
	date = sys.argv[3]
print start,terminal,date
url = 'https://kyfw.12306.cn/otn/leftTicket/query?leftTicketDTO.train_date={}&leftTicketDTO.from_station={}&leftTicketDTO.to_station={}&purpose_codes=ADULT'.format(date,start,terminal)
r=requests.get(url,verify=False)
i=r.json()
info=i['data']

for i in range(len(info)):
         print info[i]['queryLeftNewDTO']['station_train_code']+':'
         print info[i]['queryLeftNewDTO'][u'yz_num']+u'Ӳ��'
         print info[i]['queryLeftNewDTO'][u'yw_num']+u'Ӳ��'
         print info[i]['queryLeftNewDTO'][u'rw_num']+u'����'
