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
