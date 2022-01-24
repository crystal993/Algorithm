n = int(input())
lst = []
for _ in range(n):
    lst.append(int(input()))

max = 0
for n in range(0, len(lst)):
    for m in range(n+1, len(lst)):
        sum = lst[m]+lst[n]
        if max < sum:
            max = sum
print(max)
