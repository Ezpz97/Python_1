import math


def calcirle(r):
    area = math.pi * r**2
    circum = 2 * math.pi*r
    return (area, circum)


# radius = float(input('원의 반지름을 입력하시오: '))
radius = 10.0
(a, c) = calcirle(radius)
print(f'원의 넓이는 {a}이고 원의 둘레는 {c}입니다.')


class Cat:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def setName(self, name):
        self.__name = name

    def getName(self):
        return self.__name

    def setAge(self, age):
        self.__age = age

    def getAge(self):
        return self.__age


missy = Cat('Missy', 3)
lucky = Cat('lucky', 5)
print(missy.getName(), missy.getAge())
print(lucky.getName(), lucky.getAge())


class Box:
    def __init__(self, width, length, height):
        self.__width = width
        self.__length = length
        self.__height = height

    def setWidht(self, width):
        self.__width = width

    def getWidht(self):
        return self.__width

    def setLength(self, length):
        self.__length = length

    def getLenght(self):
        return self.__length

    def setHeigth(self, height):
        self.__height = height

    def getHeight(self):
        return self.__height

    def getVolume(self):
        return self.__width * self.__length * self.__height

    def __str__(self):
        return '(%d, %d, %d)' % (self.__width, self.__length, self.__height)


box = Box(100, 100, 100)
print(box)
print('상자의 부피는 ', box.getVolume())


class Car:
    def __init__(self, speed=0, gear=1, color='white', oil=0):
        self.__speed = speed
        self.__gear = gear
        self.__color = color
        self.__oil = oil

    def setSpeed(self, speed):
        self.__speed = speed

    def setGear(self, gear):
        self.__gear = gear

    def setColor(self, color):
        self.__color = color

    def setOil(self, oil):
        self.__oil = oil

    def setKm(self, km):
        self.__km = km

    def __str__(self):
        return '(속도: %d  기어:%d  색상:%s 주행거리:%dkm에 필요한 연료는 %.2fL입니다.)' % (self.__speed, self.__gear, self.__color, self.__km, self.__km/52)


myCar = Car()
myCar.setGear(3)
myCar.setSpeed(100)
myCar.setKm(100)
print(myCar)


class Rectangle:
    def __init__(self, side=0):
        self.side = side

    def getArea(self):
        return self.side * self.side


def printArea(r, n):
    while n >= 1:
        print(r.side, '\t', r.getArea())
        r.side = r.side + 1
        n = n - 1


myRect = Rectangle()
count = 5
printArea(myRect, count)
print('사각형의 변=', myRect.side)
print('반복횟수=', count)
