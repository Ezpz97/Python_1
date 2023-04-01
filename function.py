"""
함수_function란 특별한 작업을 담당하는 명령어들의 모임이다.
우리는 이제까지 print()함수와 input() 함수를 사용해왔다.
파이썬이 기본으로 제공하는 내장 함수는 상당히 많다.
여기서 우리는 계산과 관련된 함수들을 잠시 살펴보고 지나가자.
"""
# abs() - 자신에게 전달된 값의 절대값을 계산하여 반환한다.
from math import *
value = abs(-3)
print(value)
# round() - 반올림 함수
print(round(1.2345))
print(round(1.9345))
# max() - 주어진 수 중에서 최대값을 반환
print(max(10, 20))
# min() - 주어진 수 중에서 최솟값을 반환
print(min(10, 20))
# 제곱근 함수 sqrt()를 사용할 땐 import를 이용하여 선언 해줘야한다
print(sqrt(4))
# sqrt()와 같은 함수들은 모두 math라는 라이브러리에 저장되어 있다. 파이썬에선 이를 모듈(module)이라고 한다.
"""
등산 시간 계산
어떤 사람이 산악 자전거로 등산을 계획하고 있다.
평지에서는 시속 20km/h가 가능하고 오르막에서는 
10km/h, 내리막에서는 30km/h가 가능하다고 하자.
위와 같은 경로를
자전거로 주행한다면 시간이 얼마나 걸릴까?
         4km
10km 3km     3km  8km
"""
time1 = 10/20
length = (3**2+4**2)
time2 = length/10
time3 = length/30
time4 = 8/20
total = time1+time2+time3+time4
print(total)
