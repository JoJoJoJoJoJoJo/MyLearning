#-*- coding=gbk -*-
import requests
import time
import sys

#global
station={'上海':'SHH','运城':'YNV','三门峡':'SMF','闻喜':'WXV','太原':'TYV','介休':'JXV','苏州':'SZH'}

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
         print info[i]['queryLeftNewDTO'][u'yz_num']+u'硬座'
         print info[i]['queryLeftNewDTO'][u'yw_num']+u'硬卧'
         print info[i]['queryLeftNewDTO'][u'rw_num']+u'软卧'
