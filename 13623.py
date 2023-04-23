# zero or one

lst = list(map(int, input().split()))
 
if lst[0] == lst[1] and lst[0]==lst[-1]:
    print("*")
elif lst[0]!=lst[1] and lst[0]!=lst[-1] and lst[1]==lst[-1]:
    print("A")
elif lst[1]!=lst[0] and lst[1]!=lst[-1] and lst[0]==lst[-1]:
    print("B")
else:
    print("C")