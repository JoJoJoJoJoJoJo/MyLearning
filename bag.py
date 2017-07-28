def knap(t,w):
    n=len(w)
    stack=[]
    k=0
    while stack or k<n:
        while t>0 and k<n:
            if t>=w[k]:
                stack.append(k)
                t-=w[k]
            k+=1
        if t==0:
            print stack

        k=stack.pop()
        t+=w[k]
        k+=1
