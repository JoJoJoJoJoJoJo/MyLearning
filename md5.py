import hashlib
def calc_md5(x):
    md5=hashlib.md5()
    md5.update(x)
    password=md5.hexdigest()
    return password

db={}
n=0
while n <3:
    
    i=raw_input("username")
    db[i]=calc_md5(raw_input("password"))
    n=n+1
a=raw_input("inputpassword")
b=raw_input('outpassword')
if db.get(a)==None:
    print "Wrong Input"
else:
    if db[a]==calc_md5(b):
        print True
    else:
        print False
