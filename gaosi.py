sum1 = 0
sum2 = 0
for i in range (1,101) :
    sum1 = sum1 + i
n=100
while n > 0:
    sum2 = sum2 + n
    n = n-1
if sum1 == sum2:
    print "oh yeah!"
else:
    print str(sum1),str(sum2)
