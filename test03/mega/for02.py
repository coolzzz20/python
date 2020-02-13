#3번 반복하고 싶은 경우.
for x in range(0, 3):
    print('★',end=' a')
    print()
#range( a, b ) 는 a부터 b까지 1씩 증가하는 값을 가짐.
#range ( a, b , c) 의 경우 c는 c의 숫자만큼 숫자를 올린다 a + c
print('----------------')
for x in range(0, 10, 2): # for_in range(0 , 10) <--- x를 사용하지 않는 경우 _ 를 이용한다.
    # # print(x)
    print('★',end=' ') # ㅁ->한자->별찾음
print() # 값 나오는 곳에 엔터를 누른 것 처럼 줄을 넘기는 것 = 공백 생기는 것
print()

for y in range(0, 10):
    for x in range(0, 10):
    # # print(x)
     print('★', end=' ')
    print()

# 위의 경우 print(별 end )를 해 준 후 print() 까지 실행 한 다음 다시 처음으로 돌아간다.

