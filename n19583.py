

#
# 19583
# 싸이버개강총회
# https://www.acmicpc.net/problem/19583

import sys
input = sys.stdin.readline


times = list(input().split())
S = int(times[0][:2]+times[0][3:])
E = int(times[1][:2]+times[1][3:])
Q = int(times[2][:2]+times[2][3:])
student = dict()
cnt = 0

while True:
    log = input()
    if len(log) < 3:
        break
    time, chat = log.split()
    time = int(time[:2]+time[3:])
    if time <= S:
        student[chat] = 1
    elif E<=time<=Q:
        if student.get(chat) and student[chat] == 1:
            cnt +=1
            student[chat] = 0

print(cnt)