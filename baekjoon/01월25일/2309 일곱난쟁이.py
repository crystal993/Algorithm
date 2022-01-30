heights = [int(input()) for _ in range(9)]
tot = sum(heights)

for i in range(8):
    for j in range(i+1, 9):
        if tot - heights[i] - heights[j] == 100:
            heights.remove(heights[i])
            heights.remove(heights[j])
            print(heights)
            break

for i in heights:
    print(i)
