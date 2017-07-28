def fact(n):
    return act(n,1)
def act(n,a=1):
    if n == 1:
        return a
    return act(n-1,n*a)
    
