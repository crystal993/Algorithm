import sys

C = int(sys.stdin.readline())

for _ in range(C):
    info = list(map(int, sys.stdin.readline().split()))
    s_num = info[0]
    scores = info[1:]
    avg = sum(scores)/s_num
    cnt = 0

    for i in scores:
        if i > avg:
            cnt += 1
    answer = (cnt/s_num)*100
    print(f"{answer:.3f}%")