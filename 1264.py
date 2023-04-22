mo = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
str = input()

while (str != '#'):
    cnt = 0
    for word in str :
        for i in range (len(mo)):
            if word == mo[i]:
                cnt += 1
    print(cnt)
    str = input()
