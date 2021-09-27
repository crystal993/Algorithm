import sys
sys.stdin=open("in1.txt","r") #15분 걸림.

N = int(input())
iscorrect_list = list(map(int, input().split()))
# print(iscorrect_list)

score_list = []
cnt = 0
for i in iscorrect_list:
    if i == 1 :
        cnt += 1
    else:
        cnt = 0
    score_list.append(cnt)
#     print(score_list)
#
# print(score_list)
print(sum(score_list))
