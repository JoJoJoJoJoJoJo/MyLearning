def pal(s,m=0):
    l = len(s)
    print l
    n = l-m-1
    print n
    if l == 1:
        if m == 0:
            return 'only one character,cannot judge'
        return 'this is true'
    if s[m] is s[n]:
        s = s[m:n-1]
        print s
        pal(s,m)
    else:
        return 'no'
