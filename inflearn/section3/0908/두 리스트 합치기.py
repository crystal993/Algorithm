import sys
sys.stdin=open("input2.txt", "r") #5분
import numpy as np

num1 = int(input())
num_list1 = list(map(int,input().split()))
num2 = int(input())
num_list2 = list(map(int,input().split()))

# 방법1 : extend() 이용하면 간단.
num_list1.extend(num_list2)
num_list1.sort()
for i in num_list1:
    print(i, end=' ')

# 방법2 : concatenate() 이용하면 간단.
# num_list3 = np.concatenate(num_list1, num_list2)
# # num_list3.sort()
# print(num_list3)


# 방법3
num_list3 = []
for i in num_list1:
    num_list3.append(i)

for i in num_list2:
    num_list3.append(i)

num_list3.sort()
for i in num_list3:
    print(i, end=' ')


