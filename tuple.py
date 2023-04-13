'''
함수의 튜플 반환 예제
'''
import math


def circle(r):
    area = math.pi * r * r
    circum = 2*math.pi*r
    return (area, circum)


radius = float(input('원의 반지름을 입력하시오: '))
(a, c) = circle(radius)
print('원의 넓이는 '+str(a)+'이고 원의 둘레는 '+str(c)+'이다.')

'''
파티 동시 참석자 알아내기
'''
partyA = set(['park', 'kim', 'lee'])
partyB = set(['park', 'choi'])

print('2개의 파티에 모두 참석한 사람은 다음과 같습니다.')
print(partyA.intersection(partyB))

'''
파일에서 중복되지 않은 단어의 개수 세기
'''


def process(w):
    output = ""
    for ch in w:
        if (ch.isalpha()):
            output += ch
    return output.lower()


words = set()

# fname = input('입력 파일 이름: ')
file = open('proverbs.txt', 'r')

for line in file:
    linewords = line.split()
    for word in linewords:
        words.add(process(word))

print('사용된 단어의 개수=', len(words))
print(words)
