import sys

T = int(sys.stdin.readline())

# 버전1. 문자열은 하나씩 접근 가능
# for _ in range(T):
#     R,S = map(str, sys.stdin.readline().split())
#     S = list(str(S))
#     for s in S:
#         for _ in range(int(R)):
#             print(s,end='')
#     print()

# 버전2. 문자열은 하나씩 접근 가능
for _ in range(T):
    R,S = sys.stdin.readline().split()
    for s in S:
        print(s*int(R),end='')
    print()
