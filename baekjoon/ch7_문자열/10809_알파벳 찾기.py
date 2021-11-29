# 이 문제는 다시 풀기
import sys

word = list(str(sys.stdin.readline().rstrip()))
check = [-1]*26

# print(word)
for i in range(len(word)):
    if check[ord(word[i])-ord('a')] != -1:
        continue
    else:
        check[ord(word[i]) - ord('a')] = i

for i in range(26):
    print(check[i],end=' ')


