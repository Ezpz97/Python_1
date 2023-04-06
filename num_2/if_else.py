"""
연속적인 if-else문
if_elif_else
"""
score = int(input("성적을 입력하시오:"))
if score >= 90:
    print("학점 A")
elif score >= 80:
    print("학점 B")
elif score >= 70:
    print("학점 C")
elif score >= 60:
    print("학점 D")
else:
    print("학점 F")

"""
음수, 0, 양수 구별하기
사용자로부터 정수를 받아서 음수 , 0 , 양수 중의 하나로 분류하여 보자.
"""
num = int(input("정수를 입력하시오:"))
if num < 0:
    print("입력된 정수는 음수입니다.")
elif num == 0:
    print("입력된 정수는 0입니다.")
else:
    print("입력된 정수는 양수입니다.")

"""
사용자로부터 나이를 받아서 어린이(~12세), 청소년(13~18), 청년(19~30), 장년(31~50),
노년(51~)로 나누어 출력하는 프로그램을 작성해보자.
"""
age = int(input("나이를 입력해주세요"))
if age < 0:
    print("나이를 정확하게 입력해주세요.")
elif age >= 0 and age <= 12:
    print("어린이")
elif age >= 13 and age <= 18:
    print("청소년")
elif age >= 19 and age <= 30:
    print("청년")
elif age >= 31 and age <= 50:
    print("장년")
else:
    print("노년")

"""
중첩(nesting) if-else
"""
apple = input("사과의 상태를 입력하시오:")
price = int(input("사과 1개의 가격을 입력하시오:"))
if apple == "신선":
    if price < 1000:
        print("10개를 산다")
    else:
        print("5개를 산다")
else:
    print("사과를 사지 않는다.")


"""
음수 0 양수 구별하기
중첩 if - else
"""
num = int(input("정수를 입력하세요:"))
if num >= 0:
    if num == 0:
        print("0입니다.")
    else:
        print("양수입니다.")
else:
    print("음수입니다.")

"""
아이디 검사
아이디를 입력받아서 등록된 아이디인지를
검사한느 프로그램을 작성해보자.
등록된 아이디를 리스트에 저장하도록 한다.
아이디가 일치하면 패스워드를 물어본다.
"""
user_list = ['김철수', '홍길동', '김영희']
user_password = ['1234', '2234', '3234']

id = input("아이디:")
if id in user_list:
    password = input("패스워드를 입력하시오:")
    if password == user_password[user_list.index(id)]:
        print('환영합니다.')
    else:
        print("잘못된 패스워드입니다.")
else:
    print("알 수 없는 사용자입니다!")
