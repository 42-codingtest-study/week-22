while True:
    sen = input()
    count = 0
    if sen == '#' :	# 입력의 끝
        break
    for c in sen :
        if c in 'aeiouAEIOU' : # 모음이면
            count += 1
    print(count)