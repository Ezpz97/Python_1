"""
피타고라스 삼각형
"""
new_list = []
for x in range(1, 30):
    for y in range(x, 30):
        for z in range(y, 30):
            if (x**2+y**2 == z**2):
                new_list.append((x, y, z))
print(new_list)

"""
순차 탐색 알고리즘
"""


def lineSearch(alist, key):
    for i in range(len(alist)):
        if key == alist[i]:
            return i
    return -1


number = [10, 20, 30, 40, 50, 60, 70, 80, 90]

position = lineSearch(number, 80)

if position != -1:
    print('탐색 성공 위치 =', position)
else:
    print('탐색 실패')

"""
선택 정렬을 구현하는 함수
"""


def selectionSort(alist):

    for i in range(len(alist)):
        least = i
        leastvalue = alist[i]
        for k in range(i+1, len(alist)):
            if alist[k] < leastvalue:
                least = k
                leastvalue = alist[k]

        tmp = alist[i]
        alist[i] = alist[least]
        alist[least] = tmp


list1 = [7, 9, 5, 1, 8]
selectionSort(list1)
print(list1)

'''
연락처 관리 프로그램
'''
menu = 0
friend = []
while menu != 9:
    print('--------------------------')
    print('1. 친구 리스트 출력')
    print('2. 친구추가')
    print('3. 친구삭제')
    print('4. 이름변경')
    print('9. 종료')
    menu = int(input('메뉴를 선택하시오: '))
    if menu == 1:
        print(friend)
    elif menu == 2:
        name = input('이름을 입력하세요:')
        friend.append(name)
    elif menu == 3:
        del_name = input('삭제하고 싶은 이름을 입력하시오: ')
        if del_name in friend:
            friend.remove(del_name)
        else:
            print('이름이 발견되지 않았음')
    elif menu == 4:
        old_name = input('변경하고 싶은 이름을 입력하시오: ')
        if old_name in friend:
            index = friend.index(old_name)
            new_name = input('새로운 이름을 입력하시오: ')
            friend[index] = new_name
        else:
            print('이름이 발견되지 않음')

"""
menu_def
"""


def print_options():
    print('--------------------------')
    print('1. 친구 리스트 출력')
    print('2. 친구추가')
    print('3. 친구삭제')
    print('4. 이름변경')
    print('9. 종료')


menu = 0
friend = []
while menu != 9:
    print_options()
    menu = int(input('메뉴를 선택하시오: '))
    if menu == 1:
        print(friend)
    elif menu == 2:
        name = input('이름을 입력하세요:')
        friend.append(name)
    elif menu == 3:
        del_name = input('삭제하고 싶은 이름을 입력하시오: ')
        if del_name in friend:
            friend.remove(del_name)
        else:
            print('이름이 발견되지 않았음')
    elif menu == 4:
        old_name = input('변경하고 싶은 이름을 입력하시오: ')
        if old_name in friend:
            index = friend.index(old_name)
            new_name = input('새로운 이름을 입력하시오: ')
            friend[index] = new_name
        else:
            print('이름이 발견되지 않음')

'''
2개의 주사위
'''
rows = 6
cols = 6
table = []

for row in range(rows):
    table += [[0]*cols]

for row in range(rows):
    for col in range(cols):
        table[row][col] = (row+1+col+1)

print(table)
