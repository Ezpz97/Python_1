"""
call_by_value
pass_by_value
"""


def modify(n):
    n += 1


k = 10
print("k=", k)
modify(k)
print('k=', k)


def modify1(s):
    s += "To you"


msg = 'Happy Birthday'
print('msg=', msg)
modify1(msg)
print('msg=', msg)


def modify2(li):
    li += [100, 200]


list = [1, 2, 3, 4, 5]
print(list)
modify2(list)
print(list)

"""
지역 변수와 전역 변수
전역 변수 - 함수의 외부에 있는 변수
지역 변수 - 함수의 내부에 있는 변수
"""


def sub():
    s = '바나나가 좋음!'
    print(s)


sub()


def sub():
    print(s)


s = '사과가 좋음!'
sub()


def sub1():
    s = '바나나가 좋음'
    print(s)


s = '사과가 좋음'
print(s)


def sub3(x, y):
    global a
    a = 7
    x, y = y, x
    b = 3
    print(a, b, x, y)


a, b, x, y = 1, 2, 3, 4
sub3(x, y)
print(a, b, x, y)

"""
매개변수 = 지역변수
"""


def sub4(mylist):
    mylist = [1, 2, 3, 4]
    print('함수 내부에서의  mylist: ', mylist)
    return


mylist = [10, 20, 30, 40]
sub4(mylist)
print("함수 외부에서의 mylist: ", mylist)

"""
전역변수와 지역변수
"""
PI = 3.141592


def main():
    radius = float(input('원의 반지름을입력하시오: '))
    print('원의 면적: ', circleArea(radius))
    print('원의 둘레: ', circleCircumference(radius))


def circleArea(radius):
    return PI*radius**2


def circleCircumference(radius):
    return 2*PI*radius


main()

"""
여러 개의 값 반환하기
"""


def sub_m():
    return 1, 2, 3


a, b, c = sub_m()
print(a, b, c)

"""
여러개의 값 반환
"""


def get_line(x1, y1, x2, y2):
    if (x1 == x2):
        return 0, 0
    else:
        slope = (float)(y2-y1) / (float)(x2-x1)
        yintercept = y1 - slope*x1
        return slope, yintercept


x1 = int(input('x1='))
x2 = int(input('x2='))
y1 = int(input('y1='))
y2 = int(input('y2='))
slope, yintercept = get_line(x1, x2, y1, y2)
print('기울기=', slope, 'y절편=', yintercept)

"""
사용자로부터 2개의 정수를 받아서 크기 순으로 반환하는 함수를 작성하고 테스트해보자.
ex) 20 10 -> 10 20
"""


def sort_m(x, y):
    t = max(x, y)
    k = min(x, y)
    return k, t


x = int(input('1번 정수:'))
y = int(input('2번 정수:'))
print(x, y)
print(sort_m(x, y))

"""
무명 함수 (람다식)
"""
def sum(x, y): return x+y


print('정수의 합: ', sum(10, 20))
print('정수의 합: ', sum(20, 20))

L = [lambda x: x ** 2, lambda x: x**3, lambda x: x**4]

for f in L:
    print(f(3))

min = (lambda x, y: x if x < y else y)
min(100, 200)
