import random
import math


def get_sum(start, end):
    sum = 0
    for i in range(start, end+1):
        sum += i
    return sum


print(get_sum(1, 10))
print(get_sum(1, 20))


def square(n):
    return n**2


print(square(10))


def get_max(x, y):
    if (x > y):
        return x
    else:
        return y


print(get_max(10, 20))


"""
n! 구하기
"""


def fact(n):
    result = 1
    for i in range(n, 1, -1):
        result *= i
    return result


n = int(input('N:'))
print(fact(n))

"""
생일 축하 함수
"""


def happyBirthday():
    print('생일축하합니다!')
    print('생일축하합니다!')
    print('사랑하는 친구의', end=" ")
    print('생일축하합니다!')


happyBirthday()

"""
생일자 이름을 매개변수로 받아 축하하기
"""


def happyBirthday_2(name):
    print('생일축하합니다!')
    print('생일축하합니다!')
    print('사랑하는 %s의' % name, end=" ")
    print('생일축하합니다!')


happyBirthday_2('철수')

"""
온도 변환 함수
"""


def FtoC(temp_f):
    temp_c = (5.0 * (temp_f - 32.0)) / 9.0
    return temp_c


temp_f = float(input('화씨온도를 입력하시오:'))

print(FtoC(temp_f))

"""
소수 찾기
"""


def prime(n):
    for i in range(2, n):
        if (n % i == 0):
            return False
    return True


n = int(input('정수를 입력하시오:'))
print(prime(n))

"""
1~100 사이의 소수 찾기
"""


def prime():
    for i in range(2, 101):
        check = True
        for j in range(2, i):
            if (i % j == 0):
                check = False
                break
        if check:
            print(i, end=" ")


prime()

print('')
"""
구의 부피 구하기
"""


def circle(r):
    volume = (4.0/3.0) * math.pi * r**3
    return volume


radius = float(input('구의 반지름을 입력하시오:'))
print(circle(radius))

"""
패스워드 생성기
"""


def genPass():
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    password = ""

    for i in range(6):
        index = random.randrange(len(alphabet))
        password = password + alphabet[index]
    return password


print(genPass())
print(genPass())
print(genPass())


"""
값을 반환하지 않는 함수
"""


def printinfo(name, age):
    print("====================")
    print("이름: ", name)
    print("나이: ", age)
    print("====================")
    return


printinfo('홍길동', 21)

"""
디폴트 인수
"""


def greet(name, msg='별일없죠?'):
    print('안녕 ', name+','+msg)


greet('영희')

"""
키워드 인수
"""


def calc(x, y, z):
    return x+y+z


calc(x=10, y=20, z=30)

"""
키워드 인수 연습
"""


def add(a, b):
    return a+b


def sub(a, b):
    return a-b


def mul(a, b):
    return a*b


def div(a, b):
    return a/b


r1 = mul(a=20, b=30)
r2 = add(a=10, b=r1)
print(r2)

"""
온도변환기
"""


def printOptions():
    print(" 'c' 섭씨온도에서 화씨온도로 변환")
    print(" 'f' 화씨온도에서 섭씨온도로 변환")
    print(" 'q' 종료")


def C2F(c_temp):
    return 9.0/5.0 * c_temp + 32


def F2C(f_temp):
    return (f_temp - 32.0) * 5.0 / 9.0


printOptions()
choice = input("메뉴에서 선택하세요.")
while choice != "q":
    if choice == "c":
        temp = float(input("섭씨온도: "))
        print("화씨온도:", C2F(temp))
    elif choice == "f":
        temp = float(input("화씨온도: "))
        print("섭씨온도: ", F2C(temp))
    printOptionS()
    choice = input("메뉴에서 선택하세요.")

"""
입력검출
"""


def area(w, h):
    return w*h


def input_pos(msg):
    value = int(input(msg))
    while value <= 0:
        value = int(input('양수를 입력하시오: '))
    return value


width = input_pos('사각형의 가로:')
height = input_pos('사각형의 세로:')

print('면적=', area(width, height))

"""
참조값에 의한 인수 전달
"""


def modify(n):
    n = n + 1


k = 10
print("k=", k)
modify(k)
print("k=", k)
