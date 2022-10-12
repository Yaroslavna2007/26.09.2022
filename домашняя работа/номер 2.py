n = int(input())
k = int(input())
s = []
p=-1
for x in range(n):
    s.append('I')
for i in range(k):
    l = int(input())
    r = int(input())
    for g in range(l-1,r):
        s[g] = '.'
for t in range(len(s)):
    print(s[t],end=' ')





