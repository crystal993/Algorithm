n,m = map(int, input().split(" "))
array = list(map(int, input().split(" ")))
sum = 0
sum_max = 0
for i in range(0,n-2):
    for j in range(i+1,n-1):
        for k in range(j+1,n):
            sum = array[i] + array[j] + array[k]
            print(i,j,k,"\n",end="")
            if sum == m:
                sum_max = sum
            elif sum < m :
                for i in array:
                    if sum_max < i:
                        sum_max = i
print(sum_max)
