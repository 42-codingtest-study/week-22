import sys
from collections import defaultdict

students = {}
cnt = 0

input = sys.stdin.readline
times = input().split()
S = int(times[0][:2] + times[0][3:])
E = int(times[1][:2] + times[1][3:])
Q = int(times[2][:2] + times[2][3:])

while True:
    try:
        time, name = input().split()
        time = int(time[:2] + time[3:])
        if time <= S:
            students[name] = 1
        elif E <= time <= Q:
           if students.get(name) and students[name] == 1:
               cnt += 1
               students[name] = 0
    except:
        break

print(cnt)