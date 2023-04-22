import sys

num = list(map(int, input().split()))

def find_cln(arr):
    cln = arr[0] * 1000 + arr[1] * 100 + arr[2] * 10 + arr[3]
    for i in range(1, 4):
        new = arr[(0+i)%4] * 1000 + arr[(1+i)%4] * 100 + arr[(2+i)%4] * 10 + arr[(3+i)%4]
        if cln > new :
            cln = new
    return cln

clock_num = find_cln(num)

cnt = 0
i = 1111
while(i <= clock_num):
    num = list(map(int, str(i)))
    if find_cln(num) == i and 0 not in num :
        cnt += 1
    i += 1
print(cnt)