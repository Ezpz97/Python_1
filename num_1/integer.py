"""
변수가 저장하는 것
두 가지 수 
정수 - integer - int
실수 - floating_point - float
데이터의 종류 - 자료형(data_type)이라고 한다.
문자열도 저장할 수 있다.
"""
value = 3  # 정수형 int
value = 3.14  # 실수형 float
value = 'hello'  # 문자열 string

# 변수의 이름을 정할 땐 낙타체를 많이 사용한다.

"""
상수 - constant 란 한번 값이 결정되면 절대로 변경되지 않는 변수를 의미한다.
"""
TAX_RATE = 0.35  # 상수
tax = 1000 * TAX_RATE
income = 1000 - tax
print("현재의 세율은", TAX_RATE*100, "퍼센트입니다.")

"""
주선 - comment이란
소스 코드에 붙이는 설명글과 같은 것 이다.
파이선에선 #을 붙여 한줄 죽석을 만들던가 
" 3개로 많은 양의 주석을 처리할 수 있다.
"""

# 이 프로그램은 사용자로부터 2개의 정수를 받아서 그 합을 계산한다.
x = int(input("첫 번째 정수 : "))
y = int(input("두 번째 정수 : "))
sum = x + y
# diff = x - y
print("정수의 합은", sum)
