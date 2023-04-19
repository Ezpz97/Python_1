'''
2차원 리스트
'''
import random
table = []


def printlist(mylist):
    for row in range(len(mylist)):
        for col in range(len(mylist[0])):
            print(mylist[row][col], end=" ")
        print()


def init(mylist):
    for row in range(len(mylist)):
        for col in range(len(mylist)):
            if (row+col) % 2 == 0:
                table[row][col] = 1


for row in range(10):
    table += [[0]*10]

init(table)
printlist(table)

'''
TIC-TAC-TOE 게임
'''
board = [[' ' for x in range(3)] for y in range(3)]
while True:
    for r in range(3):
        print("  "+board[r][0] + "|  "+board[r][1] + "|  " + board[r][2])
        if (r != 2):
            print("---|---|---")
    x = int(input('다음 수의 x좌표를 입력하시오: '))
    y = int(input('다음 수의 y좌표를 입력하시오: '))

    if board[x][y] != ' ':
        print('잘못된 위치입니다.')
        continue
    else:
        board[x][y] = 'X'

    done = False
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ' and not done:
                board[i][j] = 'O'
                done = True
                break
    break

'''
지뢰찾기 게임
'''

board = [[False for x in range(10)] for y in range(10)]

for r in range(10):
    for c in range(10):
        if (random.random() < 0.3):
            board[r][c] = True

for r in range(10):
    for c in range(10):
        if board[r][c]:
            print('# ', end="")
        else:
            print('. ', end="")
    print()
