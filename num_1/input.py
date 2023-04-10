"""
인풋함수_input() - 입력을 받기 전에 사용자에게 출력하는 프롬프트 문자열을 가질 수 있다.
변수 = input("프롬프트 문자열")
input()이 호출되면 프로그램의 실행은 사용자가 입력할 때까지
잠시 중지된다.
사용자가 입력을 끝내고 엔터키를 누르면 프로그램의 
실행이 다시 시작된다.
input()의 프롬프트 문자열은 화면에 출력된다.
"""
# ex) 사용자의 이름을 물어보고 다시 나이를 물어보는 프로그램을 작성해보자.
name = input("이름이 무엇인가요? ")
print("만나서반갑습니다. " + name + "씨!")
age = input("나이는요? ")
print("네, 그러면 당신은 이미 " + age + " 살이시군요," + name + "씨!")

# ex) 숫자입력 - 사용자로부터 정수 2개를 받아서 합계를 출력하는 프로그램을 작성해보자
x = input("첫 번째 정수: ")
y = input("두 번째 정수: ")
sum = x+y
print(sum)  # 숫자를 정수형이 아닌 문자형으로 받아서 10+20인 30이 아니라 10과20이 나란히 나온다
# ex) fix_ver _ int형으로 변환해줘야 한다.
x = int(input("첫 번째정수: "))  # int()
y = int(input("두 번째정수: "))  # int()
sum = x+y
print(sum)