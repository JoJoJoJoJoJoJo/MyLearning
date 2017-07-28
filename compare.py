#coding:utf-8
print "请输入一个数字"

number =int( raw_input())

if number == 10:
    print"You have input %d"%number
    print "Good job!"
    
elif number >10:
    print"You have input：%d"%number
    print"太大了,重新输入"
    number = int(raw_input())
elif number <10:
    print"You have input：%d"%number
    print"太小了，重新输入"
    number = int(raw_input())
else:print "Are you fucking kidding me?"
