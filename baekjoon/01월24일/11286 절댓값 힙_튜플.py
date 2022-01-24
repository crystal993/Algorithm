import heapq as hq #heapq
import sys

pq = []
input = sys.stdin.readline # 한 줄 추가하면 기존 쓰는 input이 이걸로 대체됨
for _ in range(int(input())):
    x = int(input())

    # x가 0이 아닌 경우
    if x :
        # 힙큐에 튜플을 삽입
        hq.heappush(pq, (abs(x), x))
    # x가 0인 경우
    else:
        # 제일 작은 튜플의 값부분 출력.
        print(hq.heappop(pq)[1] if pq else 0)
