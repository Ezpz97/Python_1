"""
반복문 for
for x in range(n):
"""
for x in range(5):
    print("환영합니다.")

for name in ['철수', '영희', '길동', '유신']:
    print("안녕! " + name)

for x in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]:
    print(x, end=" ")

sum = 0
for x in range(10):
    sum += x
print("\n", sum)

sum = 0
for x in range(0, 10):
    sum = sum+x
print(sum)

for x in range(0, 10, 2):
    print(x, end=" ")

for x in "abcedf":
    print(x)

num = int(input("어디까지 계산할까요: "))
sum = 0
for x in range(1, num+1):
    sum += x
print("1부터 ", num, "까지의 정수의 합=", sum)

fact = 1.0
n = int(input("정수를 입력하시요: "))

for i in range(1, n+1):
    fact = fact*i
print(n, "!은", fact, "이다.")

start = int(input("초기숫자를 입력하시오: "))
for x in range(start, 0, -1):
    print(x, end=" ")
print("발사")

for t in range(0, 100+1, 10):
    c = (t - 32.0) * 5.0 / 9.0
    print(t, " ->", round(c, 2))
