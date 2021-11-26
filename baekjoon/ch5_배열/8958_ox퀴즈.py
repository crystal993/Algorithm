import sys

n = int(sys.stdin.readline())
cnt = 0
for _ in range(n):
    test_case = sys.stdin.readline().split()
    test_case = list(str(test_case))
    score = 0
    for answer in test_case:
        if answer == 'O' :
            cnt += 1
            score += cnt
        else:
            cnt = 0
    print(score)