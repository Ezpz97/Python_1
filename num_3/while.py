i = 0
while (i < 5):
    print("환영합니다")
    i += 1

"""
0부터 9까지 출력하기
"""
i = 0
while i < 10:
    print(i, end=" ")
    i += 1
print("")

"""
입력받은 수 까지 덧셈
"""
i = 1
x = int(input("숫자:"))
sum = 0
while (i <= x):
    sum += i
    i += 1
print(sum)

"""
(1+2+3+4+5...+9+10)
"""
i = 0
sum = 0
while i < 10:
    sum += i
    i += 1
print(sum)

"""
팩토리얼 계산
"""
i = 1
factorial = 1
while i <= 10:
    factorial = factorial * i
    i += 1
print("10!은 %d입니다." % factorial)

"""
입력된 팩토리얼 계산
"""
i = 1
factorial = 1
x = int(input("팩토리얼:"))
while i <= x:
    factorial = factorial*i
    i += 1
print("%d!은 %d입니다." % (x, factorial))

"""
구구단 출력
"""
i = 1
while i <= 9:
    print("3*%d = %d" % (i, i*3))
    i += 1

"""
입력된 구구단 출력
"""
i = 1
dan = int(input("단 입력:"))
while i <= 9:
    print("%d*%d = %d" % (dan, i, i*dan))
    i += 1

"""
투자 금액 계산하기
"""
year = 0
balance = 1000
while balance < 2000:
    year = year + 1
    interest = balance*0.05
    balance = balance + interest
print("기간: ", year)
print("총액: ", balance)

"""
이자율 입력
"""
year = 0
balance = 1000
interest = float(input("이자율:"))
while balance < 2000:
    year = year + 1
    interest = balance*interest
    balance = balance + interest
print("기간: ", year)
print("총액: ", balance)

"""
자리수의 합
"""
number = 1234
sum = 0
while number > 0:
    dight = number % 10
    sum = sum + dight
    number = number // 10
print("자리수의 합은 %d입니다." % sum)

"""
1~100까지 3의 배수의 합
"""
i = 1
sum = 0
while i <= 100:
    if (i % 3 == 0):
        sum += i
    i += 1
print("1~100까지 3의 배수의 합은 %d입니다." % sum)

"""
최대 공약수 계산하기
"""
x = int(input("정수를 입력하시오(큰수):"))
y = int(input("정수를 입력하시오(작은수):"))

while (y != 0):
    r = x % y
    x, y = y, r
print("최대 공약수는 %d입니다." % x)
