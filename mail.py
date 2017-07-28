import re
inputmail=raw_input('email address plz:')
a=re.match(r'^([0-9a-zA-Z]+|[0-9a-zA-Z]+\.[0-9a-zA-Z]+)\@([0-9a-zA-Z]+\.[0-9a-zA-Z]+)$',inputmail)
if a==None :
    print "Wrong email"
else:
    print "Hello! %s"%a.group(1)
    
inputmail2=raw_input('Email address with name plz:')
re_nameaddress=re.compile(r'^(\<[A-Z][a-z]+\s[A-Z][a-z]+\>)\s([0-9a-zA-Z]+\@[0-9a-zA-Z]+\.[0-9a-zA-Z]+)$')
if re_nameaddress.match(inputmail2)==None:
    print "Wrong Format"
else:
    print "address:%s"%re_nameaddress.match(inputmail2).group(2)
