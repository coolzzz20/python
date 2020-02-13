# 점수 입력: 80
# 점수 입력: 90
# 점수 입력: 70
# ------------------
# 점수의 합계 : 240
# 점수의 평균 : 80
jumsu = []  # 빈리스트
i = 0
sum = 0
while i < 3:
    data = input('점수 입력>> ')  # data = int(input('점수 입력>>')) 도 가능
    jumsu.append(int(data))  # 숫자에는 ''를 사용하지 않는다. 사용하면 문자.
    sum = sum + jumsu[i]
    i = i + 1

print(jumsu)
print('합계: ', sum)
print('평균: ', sum / i)
##print(jumsu.count(70))
# count( ) 는 ( ) 에 있는 같은 것이 몇게 있나 알려주는 것.
# 다양한 기능은 직접 확인하거나 인터넷 검색 해본다.
##jumsu.sort() #sort() 는 오름차순으로 정리
##print(jumsu)
##print(jumsu[1])
# sort() 함수를 이용한 다음에 print()를 이용하면 된다.
# sort() 함수는 원본을 건듬 -> 파괴적 함수 라고 함.
# print() 함수는 원본을 그대로 ->비파괴적 함수 라고 함.

##print(input('점수를 또 입력>>'))
# input은 입력한 값을 가져다 주는 함수이다. 그래서 print를 할 수 있다.
# input가져와서 가능. append나 sort는 계산해! 하고 안가져오기 때문에 print할게 없다.


# 위에 내용을 짝궁에게 설명해주는 내용

jumsu = []  # RAM에 공간을 만든다.
i = 0  # RAM에 만들어진 공간에 0을 넣어둔다.
sum = 0  # RAM에 만들어진 공간에 0을 넣어둔다.
while i < 3:  # 주어진 조건으로 i<3 작을 경우 CPU로 보내서 계산을 한 후 다시 시작한다
    # i>3 일 경우 CPU계산을 종료한다.
    data = input('점수 입력>> ')  # 계산을 위한 데이터 값을 입력한다.
    jumsu.append(int(data))  # RAM에 있는 jumsu라는 공간에 데이터 값을 저장한다.
    sum = sum + jumsu[i]  # RAM에 저장해둔 0의 값에 jumsu[i]값을 더하고 더한 값을 저장한다.
    i = i + 1  # RAM에 저장해둔 0의 값에 1을 더하고 더한 값을 저장한다.

print(jumsu)  # RAM에 있는 jumsu라는 공간에 저장된 값을 불러온다.
print('합계: ', sum)  # RAM에 있는 sum에 저장된 값을 불러온다.
print('평균: ', sum / i)  # RAM에 있는 sum에 저장된 값에서 i만큼 나누어진 값을 불러온다.
