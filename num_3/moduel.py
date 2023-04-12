def readList():
    nlist = []
    flag = True
    while flag:
        number = int(input('숫자를 입력하시오: '))
        if number < 0:
            flag = False
        else:
            nlist.append(number)
    return nlist


def processList(nlist):
    nlist.sort()
    return nlist


def printList(nlist):
    for i in nlist:
        print('성적=', i)


def main():
    nlist = readList()
    processList(nlist)
    printList(nlist)


if __name__ == '__main__':
    main()

"""
성적 처리 프로그램
"""
STUDENTS = 5

score = []
scoreSum = 0

for i in range(STUDENTS):
    value = int(input('성적을 입력하시오:'))
    score.append(value)
    scoreSum += value

scoreAvg = scoreSum / len(score)

highScoreStudent = 0

for i in range(len(score)):
    if score[i] >= 80:
        highScoreStudent += 1

print('성적 평균은', scoreAvg, '입니다.')
print("80점 이상 성적을 받은 학생은", highScoreStudent, '명입니다.')

"""
문자열 처리 프로그램
"""
dogName = []
while True:
    name = input('강아지의 이름을 입력하시오(종료시에는 엔터키)')
    if name == '':
        break
    dogName.append(name)

print('강아지들의 이름:')
for name in dogName:
    print(name, end=', ')
