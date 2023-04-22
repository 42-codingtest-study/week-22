num = list(input())
for i in range(0, len(num)):
    num[i] = int(num[i])

ans = 0
conti = 1

for i in range(1, len(num)):
    if num[i] - num[i-1] == 1:
        conti += 1
    else:
        if conti == 3:
            ans += 1
        conti = 1
if conti == 3:
    ans += 1
print(ans)