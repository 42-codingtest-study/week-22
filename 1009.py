t = int(input())

for _ in range (t):
    a, b = map(int, input().split())
    a %= 10
    b %= 4
    answ = 1
    if a == 0 :
        print(10)
    else :
        if b == 0 :
            b = 4
        for _ in range (0, b):
            answ = answ * a % 10
        print(answ)