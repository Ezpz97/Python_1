"""
파이썬이 처리하는 자료형_data_type에는 3가지 종류가 있다.
첫 번째는 1이나 2와 같은 정수_integer, 두 번째는 3.2화 같은 실수_floating_point
마지막으로 'Hellow world'같은 문자열_string이 있다.
"""
# type() _ 자료형을 반환해준다.
print(type("Hello world"))
# 정수형 변환 함수 int()
# 실수형 변환 함수 float()
# 문자열 변환 함수 str()
x = 10
print(type(x))
x = int(x)
print(type(x))
x = float(x)
print(type(x))
x = str(x)
print(type(x))
