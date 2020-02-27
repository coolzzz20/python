import math
name = '홍길동'
age = 100.222
print(int(age))
print(math.floor(age)) #소수점 자리 없앤다.
print(round(age, 1)) # 소수점 첫째자리까지 언급.
print('나의 이름은 %s이다' %(name)) # %s 는 임이의 값이고 %(a)의 값이 들어간다.
print('나의 이름은 %s이고 나이는 %d' %(name, age))  # %d는 10진수로 들어갈 거야. 0.1f f는 실수인가 float인가
print('나의 이름은 {0}이고 나이는 {1:0.1f}'.format(name, age))