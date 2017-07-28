import functools
def log(text):
    if callable (text)== False:#is it a func
        def dec(func): 
            @functools.wraps(func)
            def wrapper(*args,**kw):
                print "%s,begin call %s()"%(text,func.__name__)
                result=func(*args,**kw)
                print "End call"
                return result
            return wrapper
        return dec
    else:
        @functools.wraps(text) #now text is a func
        def wrapper(*args,**kw):
            print "begin call %s()"%text.__name__
            result=text(*args,**kw)
            print "End call"
            return result
        return wrapper
    
@log("input")
def fx(t=None):
    print t

@log
def fy(x=None):
    print x
    
