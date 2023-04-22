#dict() 는 순서도 신경씀, key value 있음{}

import sys
input = sys.stdin.readline

k, l = map(int, input().split())

click = dict()

for i in range (0, l):
    click[input().rstrip()] = i

sorted_click = sorted(click.items(), key= lambda item: item[1])

if (k > len(sorted_click)) :
    k = len(sorted_click)

for i in range(0, k):
    print(sorted_click[i][0])