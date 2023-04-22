import sys
input = sys.stdin.readline

a = int(input())
arr = list(map(int, input().rsplit()))

print(min(arr), max(arr))