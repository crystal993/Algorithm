from collections import Counter

counter = Counter(['red','blue','red','green','blue','blue'])

print(counter['blue']) # 'blue'가 등장한 횟수 출력
print(counter['green']) # 'green'이 등장한 횟수 출력

# {'red': 2, 'blue': 3, 'green': 1}
print(dict(counter)) # 사전 자료형으로 반환
