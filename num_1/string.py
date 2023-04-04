"""
문자열_string은 문자들의 순서있는 집합_sequence of character이다.
"""
greet = "Merry Christmans"
print(greet)
"""
문법_syntax이라는 것은 컴퓨터에서는 프로그램의 문장을 바르게 구성하기 위한 
규칙을 의미한다.
"""
x = "지난 한해 저에게 보여주신 보살핌과 사랑에 깊은 감사를 드립니다."
print(x)
#\n 줄바꿈 문자
print("첫번 쨰 줄 \n두번째 줄")
# 첫번째 따옴표 앞에 r을 추가하여 특수 문자의 의미를 없앨 수 있다.
print(r'C:\some\n')
# len()_문자열 길이 반환 함수
print(len("Poter"))
"""
이스케이프 문자
\\ - 백슬래시
\' - 작은따옴표
\" - 큰따옴표
\n - 줄바꿈 문자
\t - 탭 문자
"""

"""
파이썬 쉘에서 2개 이상의 문자열 리터럴이 서로 붙어 있으면
자동으로 연결된다.
"""
text = ('Hello''world')
print(text)

"""
문자열 접합_string concatenation
변수와 변수, 또는 변수와 리터럴을 연결하고 싶으면 
+ 연산자로 합칠 수 있다.
"""
text_2 = 'Harry' + 'poter'
print(text_2)

"""
문자열과 정수 간의 변환
다른 타입 형태의 변수 두개를 +하면 오류가 발생한다.
만약 26과 string을 붙이고 싶다면
26을 str()로 변환한 뒤 합쳐야한다.
"""
text_3 = 'student' + str(26)
print(text_3)

"""
문자열의 반복
파이썬은 문자열을 반복시켜 새로운 문자열을 생성할 수 있다.
"""
line = "="
print(line)
line *= 50
print(line)

"""
문자열의 출력
문자열에 변수의 값을 삽입하여 출력하고 싶으면 %s를 이용한다.
"""
price = 10000
print("상품의 가격은 %s원입니다."%price)

message = "현재 시간은 %s입니다."
time = "12:00PM"
print(message %time)

#문자열 안에서 하나 이상의 %s를 사용할 수도 있다.
message = "오늘은 %s월 %s일입니다."
print(message %(3,1))

"""
인덱싱_indexing
문자열에 []을 붙여서 문자를 추출하는 것이다.
인덱스_index란 문자열에 포함된 각각의 문자에 매겨진 번호이다
ex) string - 012345
"""
word = 'Python'
print(word[0])
print(word[-1])

"""
숫자 추측 게임
사용자에게 단어 3개를 입력받앙서 약자_acronym을 만들어 보자.
ex ) OST = Original Sound Track
"""
first_w = input("첫 번째 단어를 입력해주세요: ")
second_w = input("두 번째 단어를 입력해주세요: ")
third_w = input("세 번째 단어를 입력해주세요: ")

acronym = first_w[0] + second_w[0] + third_w[0]
print(acronym)