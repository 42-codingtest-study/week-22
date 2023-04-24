N = int(input())
gift = 0
for _ in range(N) :
    day = input()
    if int(day[2:]) <= 90 :
        gift += 1
print(gift)