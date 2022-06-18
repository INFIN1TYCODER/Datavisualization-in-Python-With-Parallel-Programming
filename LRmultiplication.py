def multiply(a):
    x=a[0]
    y=a[1]
    return sum(i[0]*i[1] for i in zip(x,y))
