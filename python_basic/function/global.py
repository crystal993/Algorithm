# ----------- global -----------
# global 키워드를 쓰면 전역변수로 선언
a = 0

def func():
    global a
    a += 1

for i in range(10):
    func()

print(a)

# ----- 여러개의 반환 값 -----
def operator(a,b):
    add_var = a + b
    substract_var = a - b
    multiply_var = a * b
    divide_var = a / b
    return add_var, substract_var, multiply_var, divide_var

a,b,c,d = operator(7, 3)
print(a,b,c,d)