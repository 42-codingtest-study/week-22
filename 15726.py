a, b, c = map(int,input().split())
res = 0
res2 = 0

res = (a * b) / c
res2 = (a / b) * c

if res >= res2:
    print(int(res))
else:
    print(int(res2))
