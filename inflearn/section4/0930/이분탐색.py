array1 = [11, 15, 16, 19, 18, 15, 16, 17] # 배열
# 이분탐색이 가능하려면 오름차순으로 정렬된 배열이어야 가능하다.
# 전제조건 : 정렬된 배열
array1.sort()
print(array1)
value1 = 18 # 내가 찾는 값

def binary_search(array, value):

    # 먼저 찾으려는 값이 있을 수 있는 상한선과 하한선을 정한다.
    # 상한선 : 첫번째 값, 하한선 : 마지막 값

    lower_bound = 0
    upper_bound = len(array) - 1
    cnt = 0

    # 상한선과 하한선 사이의 가운데 값을 계속해서 확인하는 루프를 시작한다.
    while lower_bound <= upper_bound :

        print(lower_bound , upper_bound)
        # 상한선과 하한선 사이에 중간 지점을 찾는다.
        midpoint = int((upper_bound+lower_bound)/2)


        # 중간 지점의 값을 확인한다.
        value_at_midpoint = array[midpoint]
        print("midpoint:", midpoint, "value_at_midpoint:",value_at_midpoint)

        # 찾는 값이 중간 값보다 작을 때
        # 상한선을 중간값에서 감소
        if value < value_at_midpoint:
            upper_bound = midpoint - 1

            cnt += 1

        # 찾는 값이 중간값보다 작을 때
        # 하한선을 중간값에서 증가
        elif value > value_at_midpoint:
            lower_bound = midpoint + 1
            cnt += 1

        elif value_at_midpoint == value:
            return midpoint


answer = binary_search(array1, value1)
print(f"value({value1})의 위치 : ",answer)
