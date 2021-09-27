N, K = map(int, input().split())
num = list(map(int, input().split()))
# N, K = 10, 3
# num = [13,15,34,23,45,65,33,11,26,42]

sum = []

for i in range(N):
    for j in range(i+1,N):
        for k in range(j+1,N):
            s = num[i]+num[j]+num[k]
            # if s not in sum:
            #     # 중복을 제거하면 sum에 입력
            sum.append(s)

sum = list(set(sum))
sum.sort(reverse=True)
# print(sum)
print(sum[K-1])
