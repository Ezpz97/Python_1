'''
회문 검사하기
'''


def check_pal(s):
    low = 0
    high = len(s) - 1
    while True:
        if low > high:
            return True
        a = s[low]
        b = s[high]

        if a != b:
            return False
        low += 1
        high -= 1


s = 'dad'
if (check_pal(s) == True):
    print('회문입니다.')
else:
    print('회문이 아닙니다.')

'''
머리 글자어 만들기
'''
phrase = "North Atlantic Treaty Organization"

acronmy = ""
for word in phrase.upper().split():
    acronmy += word[0]
print(acronmy)

'''
이메일 주소 분석
'''
address = 'aaa@gmail.com'
(id, domain) = address.split('@')
print(address)
print(id)
print(domain)

'''
문자열 분석
'''
setence = 'A picture is worth a thousand words'

talbe = {'alphas': 0, 'spaces': 0, 'digits': 0}

for i in setence:
    if i.isalpha():
        talbe['alphas'] += 1
    if i.isspace():
        talbe['spaces'] += 1
    if i.isdigit():
        talbe['digits'] += 1
print(talbe)
