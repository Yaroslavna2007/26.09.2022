def d():
    x = int(input())
    if x != 0:
        d()
    print(x)
d()