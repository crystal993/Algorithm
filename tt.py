arr = [1,1,3,3,0,1,1]
answer = []
tmp = arr[0]
answer.append(tmp)
for i in arr:
    if tmp == i:
        pass
    else:
        answer.append(i)
        tmp = i


print(answer)