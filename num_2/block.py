"""
블록
같은 위치의 들여쓰기로 블록을 나눈다
"""

"""
물건값 계산하기
인터넷 쇼핑몰에서 물건을 구입할 때,
구입액이 10만원 이상이면 5%의 할인을 해준다고 하자.
사용자에게 구입 금액을 물어보고 최종적으로 할인 금액과 지불 금액을 출력하는 프로그램을 작성해보자.
"""
total = int(input("구입 금액을 입력하시오:"))
if (total >= 100000):
    total = total*0.95
print("지불 금액은 %d입니다." % total)

"""
위의 프로그램에서 사용자의 구입액이 10만원 이하인 경우에는, 사용자에게 얼마만큼 더 구입하면 
5% 할인을 받을 수 있다고 알려주는 코드를 추가해보자.
"""
total = int(input("구입 금액을 입력하시오:"))
if (total >= 100000):
    total = total*0.95
else:
    change = 100000 - total
    print(change, "원 더 지불하시면 5%의 할인을 받으실 수 있습니다.")
print("지불 금액은 %d입니다." % total)

"""
문자열의 중간문자
문자열의 중앙에 있는 문자를출력한다.
예를 들어서 문자열이 "weekday"이라면 중앙의 문자는 
"k"가 된다.
하지만 만약 문자열이 짝수개의 문자를 가지고 있다면 중앙의 2개의 글자를 
출력한다.
예를 들어서 "string" 문자열에서는 "ri"를 반환한다.
"""
text = input("문자열을 입력하시오:")
if (len(text) % 2 == 0):
    ch1 = text[len(text)//2-1]
    ch2 = text[len(text)//2]
    print("중앙글자는 ", ch1, ch2)
else:
    ch1 = text[len(text)//2]
    print("중앙글자는 ", ch1)

"""
임금 계산
사용자에게 근무 시간과 시간당 임금을 물어본다.
주당 근무 시간이 40시간을 넘으면 1.5배의 임금을 지급해야한다고 하자.
이번 주에 받는 총임금을 계산하는 프로그램을 작성해보자
"""
time = float(input("근무시간을 입력하시오:"))
money = float(input("시간당 임금을 입력하시오:"))
if (time <= 40):
    totalWages = money*time
else:
    overtime = time - 40
    totalWages = money*40 + (1.5*money)*overtime
print("총 임금은 ", totalWages)
