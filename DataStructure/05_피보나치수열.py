# def solution(x):
#     if x <= 1:
#         return x
#     else :
#         return solution(x-1) + solution(x-2)

def solution(x):
    fn = 0
    for i in range(x-1):
        pre = i
        af = i+1
        if af > x:
            break
        fn = pre + af
    return fn