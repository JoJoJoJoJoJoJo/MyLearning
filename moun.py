def mountain(l):
    line = 1
    while l:
        for i in range(line):
            m=l.pop(min(l))
            print m;
            line +=1
