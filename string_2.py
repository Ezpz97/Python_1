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
