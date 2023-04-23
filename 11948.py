# a = int(input())
# b = int(input())
# c = int(input())
# d = int(input())
# e = int(input())
# f = int(input())

score = 0
min = 101
science = []
social = []
for _ in range(4):
	science.append(int(input()))
for _ in range(2):
	social.append(int(input()))

science.sort()
social.sort()

i = 1
while i <= 3:
	score +=  science[i]
	# print(science[i])
	i += 1

score += social[1]
print(score)
