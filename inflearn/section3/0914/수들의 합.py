import sys
sys.stdin=open('input.txt', 'r')

n, m = map(int, input().split())
a = list(map(int, input().split()))


cnt = 0
for i in range(0,n):
    sum = 0
    for j in range(i,n):
        sum += a[j]
        if sum == m:
            cnt += 1
            print(i, j)
        elif sum > m:
            break

print(cnt)


# 시간초과.
# cnt = 0
# for i in range(0, n):
#     sum1 = 0
#     for j in range(i+1, n):
#         sum1 = sum(a[i:j])
#         if sum1 == m :
#             cnt += 1
#         elif sum1 > m:
#             break
# print(cnt)