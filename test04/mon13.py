import random
jumsu = []
random.seed(4) # 똑같은 값을 일정하게 나오게 고정시키는 것 see(a) a<--숫자에 따라 다르다.
for x in range(0,1000000):
    jumsu.append(random.randint(1, 1000))

# randint( a , b) 는 a에서 b사이의 값이 골고루 나오게 하는 모튤.정규분포표를 이용했다함
print(jumsu)

# 몇개인지 알고 싶다.

##count = jumsu.count(555)
##print(count)

count2 = 0
for x in jumsu:
    #인덱스를 쓸 수 없다.
    if x == 455:
        count2 = count2 + 1
print(count2)

# print(jumsu.index(455))
for x in range(0,len(jumsu)):
    if jumsu[x] == 455:
        print('위치는: ', x )
