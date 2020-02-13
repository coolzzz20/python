# 한 줄 삭제 : ctrl + d
name = ['홍길동', '박길동', '송길동']

print(name[0])  # index가 증가
print(name[1])
print(name[2])
print('----------------------------')

index = 0  # start값
while index < 3:  # 조건식
    print(name[index])
    index = index + 1  # 증감식

print('----------------------')
print(name)  # 리스트 안 내용을 확인하고 싶을 때 이렇게 사용

print('---------------------------------------')
# 팀원의 나이의 리스트를 만들어서
# 반복문으로 찍어보고,
# 리스트의 전체 목록 확인
# 모든 프로그래밍 언에서 숫자를 쓸 때는 따옴표를 안씀
# 문자인 경우는 따옴표를 씀.

age = [28, 30, 32]
length = len(age)
inbex = 0
# while inbex < length: 이 방법과 아래 방법 둘 다 사용해도 상관없다.
while inbex < len(age):  # 직관적인 방법이다. 바로 쓰는 방법.
    print(age[inbex])
    inbex = inbex + 1

print('-----------------------------------')
print(age)

print(len(age))  # 리스트의 개수 len(리스트명)
# len 이라는 함수는 리스트의 갯수를 구할 때 사용한다
print(age[len(age) - 1])
# print(age[length - 1])
