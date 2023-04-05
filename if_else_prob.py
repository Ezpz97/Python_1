"""
숫자-> 한글
음성 합성 장치처럼 숫자를 입력하면 한글로 읽어주는 프로그램을 작성해보자.
사용자가 값을 입력하면 화면에 "하나" "둘"
과 같이 출력하는 코드를 작성하여 보자.
if_else 사용
"""
import math
import time
num = int(input("숫자를 입력하시오"))
if num == 1:
    print("하나")
elif num == 2:
    print("둘")
elif num == 3:
    print("셋")
elif num == 4:
    print("넷")
else:
    print("많음")

"""
123 -> 일백 이십 삼
"""
num = int(input("숫자"))
a = num//100
num = num % 100
b = num//10
num = num % 10
c = num
if a == 1:
    a = "일"
    if b == 2:
        b = "이"
        if c == 3:
            c = "삼"
print(a, "백", b, "십", c)

"""
달의 일수 출력
1년의 각 달의 일수를 출력하는 프로그램을 작성하여보자.
즉 특정 달이 입력되면 그 달의 일수를 출력한다.
여러 가지 방법으로 작성할 수 있겠으나 여기서는 if-else 문을 사용하여 보자.
"""
month1 = [1, 3, 5, 7, 8, 10, 12]
month = int(input("월을 입력하시오:"))
if month in month1:
    print("월의 날수는 31")
elif month == 2:
    print("월의 날수는 29")
else:
    print("월의 날수는 30")

"""
인사말 출력하기
시스템으로부터 현재 시각을 받아서 적절한 인사를 출력하는 프로그램을 작성하여 보자.
현재 시각에 따라서 연속적인 if문을 사용하여서 프로그램을 작성하였다.
"""
now = time.localtime()
print("현재 시: %d" % (now.tm_hour))
if now.tm_hour < 11:
    print("Good morning")
elif now.tm_hour < 15:
    print("Good afternoon")
elif now.tm_hour < 20:
    print("Good evening")
else:
    print("Good night")

print("현재 달: %d" % (now.tm_mon))
if now.tm_mon > 1 and now.tm_mon < 5:
    print("spring")
elif now.tm_mon >= 5 and now.tm_mon <= 8:
    print("summer")
elif now.tm_mon >= 9 and now.tm_mon <= 11:
    print("atum")
else:
    print("winter")

"""
윤년 판단
"""
year = int(input("년도 입력:"))
if ((year % 4 == 0 and year % 100 != 0) or year % 400 == 0):
    print(year, "년은 윤년입니다.")
else:
    print(year, "년은 윤년이 아닙니다.")

"""
이차 방정식
"""
a = float(input("A"))
b = float(input("B"))
c = float(input("C"))

d = b*b - 4*a*c
if a == 0:
    print("x=", -c/b)
if d == 0:
    print("x=", -b/(2.0*a))
elif d > 0:
    print("x1=", (-b+math.sqrt(d)) / (2.0*a))
    print("x2=", (-b-math.sqrt(d)) / (2.0*a))
else:
    print("실근이 존재하지 않음")
