import sys
sys.stdin=open("in3.txt","r") #30분

card=[]
for i in range(1,21):
    card.append(i)

for _ in range(10):
    section=[] 
    section = list(map(int, input().split()))

    sub = list(card[section[0]-1:section[1]])

    for i in sub:
        card.remove(i)

    for i in range(section[0]-1,section[1]):
        n = sub.pop()
        # print(n)
        card.insert(i,n)

for i in card:
    print(i,end=' ')