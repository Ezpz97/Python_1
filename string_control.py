from math import sqrt
from random import *
fruit = "apple"
index = 0
while index < len(fruit):
    letter = fruit[index]
    print(letter, end=" ")
    index += 1
print()

s = input('문자열을 입력하시오:')
vowels = 'aeiouAEIOU'
result = ""
for letter in s:
    if letter not in vowels:
        result += letter
print(result)

original = input('문자열을 입력하시오:')
word = original.lower()
vowels = 0
consonants = 0

if len(original) > 0 and original.isalpha():
    for char in word:
        if char in 'aeiou':
            vowels = vowels + 1
        else:
            consonants = consonants + 1
print("모음의 개수", vowels)
print("자음의 개수", consonants)

original = input('문자열을 입력하시오: ')
word = original.lower()

if len(original) > 0 and original.isalpha():
    for i in range(len(word)):
        if word[i] in 'aeiou':
            print(i)

"""
알파벳, 숫자, 스페이스의 처리
"""
statment = input("문자열을 입력하시오: ")

alphas = 0
digits = 0
spaces = 0

for c in statment:
    if c.isalpha():
        alphas = alphas + 1
    if c.isdigit():
        digits += 1
    if c.isspace():
        spaces += 1
print("알파벳의 개수: ", alphas)
print("숫자 문자의 개수: ", digits)
print("스페이스 문자의 개수: ", spaces)

"""
계좌번호 처리
"""
number = input('계좌번호를 입력하시오: ')
processed = ""
for k in number:
    if k != "-":
        processed += k
print(processed)

"""
주사위 합 확률
"""

count = int(input("주사위 실험 반복횟수: "))
rollcount = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
for i in range(count):
    die1 = randint(1, 6)
    die2 = randint(1, 6)
    rollcount[die1+die2] += 1
for i in range(2, 13):
    print(i, rollcount[i])

"""
파이 계산
"""

n = int(input('반복횟수를 입력하시오: '))

inside = 0
for i in range(0, n):
    x = random()
    y = random()
    if sqrt(x*x+y*y) <= 1:
        inside += 1
Pi = 4*inside/n
print(Pi)
