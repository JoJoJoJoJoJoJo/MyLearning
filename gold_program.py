#-*-coding:utf-8-*-
day1=int(raw_input(u'首日充值金额:'))
day2=int(raw_input(u'第二天充值金币:'))
day3=int(raw_input(u'第三天充值金币:'))
day4=int(raw_input(u'第四天充值金币:'))
day5=int(raw_input(u'第五天充值金币:'))

rebate_rate = float(raw_input(u'连续充值返还比例'))

d={0:day1,
   1:day2,
   2:day3,
   3:day4,
   4:day5}






def rebate_gold(gold):
    if gold <500:
        rebate =0
    elif gold <2000:
        rebate = gold*0.1
    elif gold <4000:
        rebate = gold*0.15
    elif gold <10000:
        rebate = gold*0.2
    elif gold < 20000:
        rebate = gold*0.25
    else:
        rebate = gold *0.3
    return rebate

g=0
for i in range(5):
    rebate=rebate_gold(d[i])
    g+=rebate

gold=0
if d[0]>0 and d[1]>0 and d[2]>0 and d[3]>0 and d[4]>0:
    for i in range(5):
        gold +=d[i]
    extra = gold*rebate_rate
else:
    extra = None
    
if extra:
    g+=extra
else:
    g=g

print g
