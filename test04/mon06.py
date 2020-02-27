#20번 문제
#  조건은 항상 true , false로 돌아간다.
location = []
## print(0 in range(0,5))
for x in range(0 , 5): # 0, 1, 2, 3, 4
    location.append(input('장소:   '))

print(location)

## if '강남' in location:
##    print('강남있음.')
##     #del을 사용하기 위해서 강남의 위치인 인덱스가 필요하다!
##     index = location.index('강남')
##     del location[index]
##
## print(location)

## if '강남' in location:
##     print('강남있음.')
##     location.remove('강남') #값을 가지고  삭제
##
## print(location)

# in 뒤에는 항상 범위가 있는 것이 나와야 한다.

for x in range(0,len(location)):
    if(location[x] == '강남'): #x = index
        del location[x] #del 은 파괴 함수 / 인덱스가 5개 있던 것에서 4개로 줄어들어서 실행에 오류생김
        print('강남을 삭제했습니다.')
        break # 그래서 더 이상 돌지 않게 break를 사용한다.

print(location)

location[3] = '제주시'
print(location)
print('------------------------------')

# for x in location:
#     print(x)    #인덱스가 없기 때문에 이렇게 안된다.

for x in range(0,len(location)):
    print(x+1 , "등: ", location[x])