"""
면적 계산기
사용자가 선택하는 도형의 면적을 계산하는 프로그램을 
만들어보자
"""
x = int(input("도형을 입력하십시오: 1.사각형 2.삼각형 3.원"))
if (x == 1):
    width = int(input("가로:"))
    height = int(input("세로:"))
    area = width*height
elif (x == 2):
    width = int(input("밑변:"))
    height = int(input("높이:"))
    area = 0.5*width*height
else:
    r = int(input("반지름:"))
    area = 3.141592*r**2
print("면적=", area)

"""
직선의 방정식
두 점의 좌표를 입력받아서 이 점들을 통과하는
직선의 방정식을 구해보자.
"""
x1 = int(input("첫 번째 점의 x좌표:"))
y1 = int(input("첫 번째 점의 y좌표:"))
x2 = int(input("두 번째 점의 x좌표:"))
y2 = int(input("두 번째 점의 y좌표:"))

if ((x2-x1) != 0):
    m = (y2-y1)/(x2-x1)
    q = y1-m*x1
    print('적선의 방정식은 ', m, 'x+ ', q)
else:
    print('직선의 방정식은 x=', x1)

"""
숫자 맞추기 게임
up and down
"""
num = 5
d = 0
print("숫자 게임에 오신 것을 환영합니다.")
while (d == 0):
    t = int(input("숫자를 맞춰 보세요:"))
    if (num == t):
        d = 1
    elif (num > t):
        print("작습니다!")
    elif (num < t):
        print("너무 큽니다!")
    print("다시 맞춰보세요!")
print("정답입니다!")

"""
가위 바위 보
"""
user = input("(가위,바위,보) 중에서 하나를 선택하세요:")
computer = "바위"
print("사용자: ", user, "컴퓨터: ", computer)
if (user == computer):
    print("비겼음!")
elif (user == "바위"):
    if (computer == "보"):
        print("컴퓨터가 이겼음!")
    else:
        print("사용자가 이겼음!")
elif (user == "보"):
    if (computer == "바위"):
        print("사용자가 이겼음!")
    else:
        print("컴퓨터가 이겼음!")
elif (user == "가위"):
    if (computer == "바위"):
        print("컴퓨터가 이겼음!")
    else:
        print("사용자가 이겼음!")

"""
사각형 충돌 조사
"""
p1x = int(input("첫 번째 사각형의 P1.x="))
p1y = int(input("첫 번째 사각형의 P1.y="))
p2x = int(input("첫 번째 사각형의 P2.x="))
p2y = int(input("첫 번째 사각형의 P2.y="))

p3x = int(input("두 번째 사각형의 P3.x="))
p3y = int(input("두 번째 사각형의 P3.y="))
p4x = int(input("두 번째 사각형의 P4.x="))
p4y = int(input("두 번째 사각형의 P4.y="))
overlapped = not (p4x < p2x or p3x > p2x or p2y < p3y or p1y > p4y)

if overlapped:
    print("두개의 사각형이 겹침!")
else:
    print("두개의 사각형이 겹치지 않음!")
