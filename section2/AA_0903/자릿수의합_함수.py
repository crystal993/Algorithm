import sys
sys.stdin=open("input.txt","r")

N = int(input())
num = list(map(int, input().split()))

# print(num)

str_list = []
sum_list=[]
def digit_sum(x):
    sum = 0
    for num_list in str_list:
        sum = 0
        for n in num_list:
            sum += int(n)
    sum_list.append(sum)

for n in num:
    str_list.append(list(str(n)))
    digit_sum(n)

# print(str_list)
# print(num)
# print(sum_list)

max = 0
midx = 0
for idx, i in enumerate(sum_list):
    if i > max:
        max=i
        midx=idx

print(num[midx])



