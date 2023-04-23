N = int(input())
s = list(input().split())
print(s[0][0], end="")
for i in range(1, N):
    if len(s[i - 1]) > len(s[i]):
        print(" ", end="")
    else:
        print(s[i][len(s[i - 1]) - 1], end="")
