'''
단어 카운터
'''
file = open('proverbs.txt', 'r')

table = dict()
for line in file:
    words = line.split()
    for word in words:
        if word not in table:
            table[word] = 1
        else:
            table[word] += 1

print(table)

'''
축약어 풀어쓰기
'''
table = {"B4": "Before", "TX": "Thanks", "BBL": "Be Back Later",
         "BCNU": "Be Seeing You", "HAND": "Have A Nice Day"}

# message = input('번역할 문장을 입력하시오: ')
message = 'TX Mr.Park'
words = message.split()
result = ""
for word in words:
    if word in table:
        result += table[word] + " "
    else:
        result += word
print(result)

string = 'Empty vessels make the most sound.'

countTable = {}
for letter in string:
    countTable[letter] = countTable.get(letter, 0) + 1

print(countTable)

'''
이전값 기억시키기
'''
table = {0: 0, 1: 1}


def fib(n):
    if n not in table:
        value = fib(n-1)+fib(n-2)
        table[n] = value
    return table[n]


print(fib(100))

'''
희소 행렬 표현
'''
matrix = {(1, 2): 1, (2, 2): 2, (3, 2): 3}
for y in range(5):
    for x in range(5):
        print(matrix.get((y, x), 0), end=" ")
    print()
