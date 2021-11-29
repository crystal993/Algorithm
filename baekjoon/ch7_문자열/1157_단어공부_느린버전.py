import sys

word = sys.stdin.readline().rstrip()
word_2 = list(set(word.upper()))
check = [0]*len(word_2)
# print(check)
for i in range(len(word)):
    for j in range(len(word_2)):
        if word[i].upper() == word_2[j]:
            check[j] += 1
# print(check)
# 최댓값 구하기 
max = -1 #최솟값
ch = '' #가장 많이 체크된 단어를 담을 변수
for i in range(len(check)):
    if max < check[i]:
        max = check[i]
        ch = word_2[i]
    elif max == check[i]:
        ch = '?'
print(ch)
