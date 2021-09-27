import sys
sys.stdin=open("in1_1.txt","r")

n = int(input())

for i in range(n):
    word = input()
    word = word.lower() #대소문자 구분없으므로, 모든 글자를 소문자로
    # print(word[::-1])
    if word == word[::-1]: #word[::-1]
        print(f'#{i+1} YES')
    else:
        print(f'#{i+1} NO')




