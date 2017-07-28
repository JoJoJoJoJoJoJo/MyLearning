def ss(x):
    if x == 1:
        return x
    else:
        for n in range (2,x):
            if x%n ==0:
                return True
