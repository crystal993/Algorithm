T = int(input())
# T = 2
for i in range(0, T):
    # N개의 숫자
    # s번째부터 e번째 까지의 수
    # k번째로 나타나는 숫자

    N, s, e, k = map(int, input().split()) # N, s, e, k = 6,2,5,3
    num = list(map(int, input().split())) # num = [5,2,7,3,8,9]

    answer = num[s-1:e]
    # answer = []
    # for i in range(s-1, e):
    #   answer.append(num[i])
    answer.sort()
    print(f'#{i+1} ',answer[k-1])


