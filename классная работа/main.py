a = int(input())
n = int(input())
def stepen (a, n):
    if n  == 0:
        return 1
    else:
        return stepen(a, n-1) * a
print(stepen(a, n))