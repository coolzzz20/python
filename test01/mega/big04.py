# 기본 입력 처리
# name 이라는 것은 ram의 저장 공간 이다 소문자로 시작해야하고 숫자로 시작할수없다.
# name age 는 정해지는 것이 아닌 내가 사용하기 편하기 위해서 정한 것이다.
name = input("이름 입력: ")
age = input("나이 입력: ")
print(name, "님 환영합니다.")
print("당신의 나이는 ", age ,"세")

# input은 print와 다르게 값을 써 주어야 다음 input 또는 print가 작용한다.