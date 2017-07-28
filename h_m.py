
l1=[]
l2=[]
while True:
    h=raw_input('input hour')
    m=raw_input('input minute')
    if h == 'stop':
        break
    else:
        l1.append(h)
        l2.append(m)
l1=map(int,l1)
l2=map(int,l2)
s1 = sum(l1)
s2 = sum(l2)
while s2 > 150:
    m = max(l2)
    l2.pop(l2.index(m))
    s1+=1
    s2=sum(l2)
print s1,s2
