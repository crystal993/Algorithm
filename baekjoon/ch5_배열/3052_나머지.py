import sys

n_lst = []
for _ in range(10):
    n = int(sys.stdin.readline())
    rem = n % 42
    n_lst.append(rem)

n_lst = list(set(n_lst)) # 중복제거 후 다시 리스트로
num = n_lst[0]
cnt = 1
for i in range(1,len(n_lst)):
    if n_lst[i] != num :
        num = i
        cnt += 1
print(cnt)
