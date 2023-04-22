#set()은 중복은 제거하지만 순서는 고려 안해서 뒤죽박죽임{}

import sys
input = sys.stdin.readline

S, E, Q = input().split()
S = int(S[:2] + S[3:])
E = int(E[:2] + E[3:])
Q = int(Q[:2] + Q[3:])

attend = set()
cnt = 0

while (1):
    try : 
        time, name = input().split()
        time = int(time[:2] + time[3:])
        if time <= S :
            attend.add(name)
        elif E <= time <= Q and name in attend:
            attend.remove(name)
            cnt += 1
    except :
        break

print(cnt)