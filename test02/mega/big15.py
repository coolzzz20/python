# while True:
#     print('1시간 남았어요.')

# 한줄 주석 처리 (그자리에서 ctrl + /)
# 여러 줄 주석 처리 (처리 하려는 첫 자리에서 shift를 누른 후 화살표 밑으로 누른 후
# 마지막 자리까지 왔을 때 ctrl + / ) 전부 처리됨.
# 컨트롤 + / : 자동 주석

# a = 10
# while a > 0:
#     print(a, end=' ')
#     a = a - 1

# 1. 0부터 99까지 찍어보세요.
#b = 0
# while b < 100:
#     print(b)
#     b = b + 1
# 2. 1부터 100까지 찍어보세요.

# 3. 1부터 100까지 중 짝수만 찍어보시오
# while b < 100:
#     if(b % 2 == 0):
#         print(b)
#     b = b + 1

# 4. 0~99 중 3의 배수를 찍어보세요.
# while b < 100:
#     if(b % 3 == 0):
#         print(b)
#     b = b + 1

# 5. 0~99 중 5의 배수를 개수를 구해보세요.(누적 시키는 변수를 이용)
# c = 0
# while b <100:
#     if(b % 5 == 0):
#         c = c+1
#     b = b + 1
#print(c)

start = 0
count = 0
while start < 100:
    if start % 5 == 0:
        count = count + 1 # 5의 배수일 때마다 증가시키는 녀석
    start = start + 1 # if 조건을 계속 돌리는 녀석
print('5의 배수는', count , '개')

# 6. 안녕히가세요 5번 프린트
#start = 0 #시작
#while start < 5: #조건문
   # print('안녕히 가세요')
    # start = start + 1 # 증감식 /증가, 감소 시킬 수 있다.
    #횟수를 나타내기 우해서는 시작, 조건문, 증감식 3가지가 있어야한다.

# a = 100
# print(a)
b = 0
while b < 0:
    print('잘가요')
    b = b + 1


