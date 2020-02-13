food = ['라면', '커피', '아이스크림', '라떼', '팥빙수']

#인덱싱 : 리스트의 하나하나 값을 아는 것
print(food[0])
print(food[-1])  #사이즈는 필요 없는데 끝에 무엇이 있는지 알고 싶을 때 이용
print(food[-2])

#슬라이싱 : 리스트의 값 중 a~ b까지 값을 아는 것.
print(food[0:2]) # a~b 까지 쓸 때 : 을 사용한다. a:b는 내가 가지고 싶은 b 값보다 +1 크게 해야한다.
                 # 저렇게 하면 라면 커피 2개 나온다.
print(food[2:5])
print(food[2:]) # 끝까지 인덱스
print(food[:3]) # 0~2 0부터 시작.

print('------------------------------------')
drink = ['물', '아메리카노', '맥주']
all = food + drink
print(all)

print('---------------------------------------')
drink3 = drink*3 # *숫자는 숫자만큼 앞에(drink)값을 반복해주세요
print(drink3)
print('-----------------------------------------')

drink.insert(0,'라뗴') #insert 는 파괴형 함수
print(drink)

print(drink.index('라뗴'))