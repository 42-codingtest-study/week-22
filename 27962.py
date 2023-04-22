#오렌지자식

n = int(input())
str = list(input())

def vitamin(str1, str2):
    dif = 0
    for i in range(0, len(str1)):
        if str1[i] != str2[i]:
            dif += 1
    if dif == 1 :
        return True
    else :
        return False
str1=[0 for _ in range(n)]
str2=[0 for _ in range(n)]

for i in range(0, n):
    for j in range(0, i + 1):
        str1[j] = str[j]
        str2[j] = str[(n-i-1)+j]
    if vitamin(str1, str2) :
        print("YES")
        exit()

print("NO")