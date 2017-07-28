import functools

def log(text):
    def dec(func):
        @functools.wraps(func)
        def wrapper(*args,**kw):
            print "start call %s(%s) :"% (func.__name__,text)
            result= func(*args,**kw)
            print "end call"
            return result
        return wrapper
    return dec

L=range(5)    
@log(L)# not empty or dec got no value,and no Chinese
def fx(x):
    a=sum(x)
    print a

