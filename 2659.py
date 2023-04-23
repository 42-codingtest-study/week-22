# 십자카드

import sys

num = list(map(int, sys.stdin.readline().split()))

def clock_num(n) :
    min = int(''.join(map(str, n)))
    for i in range(1,4) :
        tmp = int(''.join(map(str, n[i:]+n[:i])))
        if min > tmp :
            min = tmp
    return min

clik_num = clock_num(num)
cnt = 1
for i in range(1111, clik_num) :
    if '0' not in list(str(i)) and i == clock_num(list(map(int, str(i)))) :
        cnt += 1
print(cnt)