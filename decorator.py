def deco(func):
    print 'd'
    def wrapper(*args,**kwargs):
        print 'w'
        func(*args,**kwargs)
    return wrapper

@deco
def foo():
    print 'f'
