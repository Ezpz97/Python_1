import random
n = 0
sum = 0
score = 0

print("종료하려면 음수를 입력하세요:")
while score >= 0:
    score = int(input("성적:"))
    if score > 0:
        sum += score
        n = n + 1

if n > 0:
    average = sum/n
else:
    average = 0
print("평균은 %.1f입니다." % average)

"""
숫자 맞추기 게임
"""
number = random.randrange(1, 101)
n = 0
while n < 10:
    guess = int(input("숫자를 입력하세요:"))
    n += 1
    if guess > number:
        print("낮음!")
    elif guess < number:
        print("높음!")
    else:
        break
if n >= 10:
    print("시도횟수를 초과 하였습니다.")
else:
    print("축하합니다. 시도횟수=%d" % n)

# 중첩 루프
for y in range(5):
    for x in range(10):
        print("*", end="")
    print("")

"""
피타고라스 삼각형 찾기
"""
for a in range(1, 101, 1):
    for b in range(1, 101, 1):
        for c in range(1, 101, 1):
            if ((a**2+b**2) == c**2):
                print(a, b, c)

"""
주사위 2개를 던졌을 때, 합이 6이 되는 경우 출력
"""
for x in range(1, 7):
    for y in range(1, 7):
        if x+y == 6:
            print(x, y)
"""
주사위 3개를 사용하여 합이 10이 되는 경우 출력
"""
for x in range(1, 7):
    for y in range(1, 7):
        for z in range(1, 7):
            if x+y+z == 10:
                print(x, y, z)
"""
제곱값 출력
"""
for y in range(1, 6):
    print("x^", y, " ", end="")
print()

for x in range(1, 11):
    for y in range(1, 6):
        print(x**y, " ", end="")
    print()
