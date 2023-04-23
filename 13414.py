# 수강신청

import sys
input = sys.stdin.readline

def solution():
    k, l = map(int, input().split())
    section = {}
    for number in range(l) :
        section[input().rstrip()] = number

    section = sorted(section.items(), key = lambda x: x[1])
    cnt = 0
    
    for key in section :
        if cnt == k :
            break
        print(key[0])
        cnt += 1

solution()