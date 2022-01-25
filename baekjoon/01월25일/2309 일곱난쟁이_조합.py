from itertools import combinations

human = [int(input()) for _ in range(9)]
for combi in combinations(human, 7):
    if sum(combi) == 100:
        for height in sorted(combi):
            print(height)
        break
