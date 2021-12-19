import sys

# 에러 케이스
word = sys.stdin.readline().rstrip()

check = [1]*27
num = 2
for i in range(1,len(check)):
	check[i] = num
	if i > 19 :
		if i % 4 == 0:
			num += 1
	else:
		if i % 3 == 0 :
			num += 1
print(check)
time = 0
for w in word:
	time += check[ord(w)-ord('A')+1] + 1
print(time)