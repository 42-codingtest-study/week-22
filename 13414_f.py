import sys
input = sys.stdin.readline

k, l = map(int, input().rsplit())

click = list()

for _ in range (l):
    hak = input()
    if hak in click:
        click.remove(hak)
        click.append(hak)
    else :
        click.append(hak)

for i in range(0, k):
    print(click[i], end='')