# 극장 예매시스템
#  1. 화면을 만든다.
#  -- 0이 10개 들어간 리스트 필요

#  크다 작다 를 파악하는게 아닌 자리를 파악할 때는 리스트가 좋다.

seat = [0] * 10   #[ ] 안에 있는 수가 10개 들어가 있다.
count = 0
price = 10000
while True:
    # print(seat)  10개 잘 있는지 확인
    # alt + 화살표 => 그 줄을 이동시킬 수 있다.
    print('--------------------------------------')
    for x in range(0, len(seat)):
        print(x, end="  ")

    print('\n--------------------------------------')
    # \n <-- 다음 줄 부터 나타나게 해라

    # 자리 예약 상태 프린트(0 => 예약x , 1=> 예약o)
    for x in seat:
        print(x, end='  ')
    print('\n--------------------------------------')

    print('현재 당신의 예약 현황은 '+str(count)+' 자리 입니다.')

    print('현재 예약 가능한 자리의 수는',str(10-count)+'입니다.')
    choice = int(input('원하는 좌석 번호 입력(종료: -1)>>> '))
    if choice == -1:
        print('예매 프로그램을 종료합니다.')
        break
    #입력값은 리스트의 index로 사용될 예정
    #index는 좌석번호로 사용

    print(choice, '를 선택하셨군요')
    count = count + 1
#  이미 예매처리가 된 경우, 불가능하다고 처리
    if seat[choice] == 1:
        print('이미 예매가 된 좌석입니다.')
        print('다시 다른 좌석을 선택해주세요.')
        count = count - 1
    else:
# 이미 그 자리에
# 예매 처리가 안된 경우
# 입력받은 좌석번호로 예매처리
#  1번 클리어!
#  입력 받은 좌석 번호로 예매 처리
        seat[choice] = 1
        print('예매 처리를 완료하였습니다')
        print()

print('전체 예매된 좌석수는'+str(count)+'입니다')
print('결제 금액은 총'+str(count*price)+'입니다.')

name = input('이름 입력>>>')
print(name+'님의 예매 확인 영수증 입니다.')

# 오류뜸
# for x in range(0, len(seat)):
# 	if seat[x] == 1:
#         print('str(x),'자리는', end=''')

# for x in range( 0, len(seat)):
#     print(x)
print('예매한 자리는', end=' ')
for x in range(0, len(seat)):
	if seat[x] == 1:
	    print(str(x), '좌석', end=' ')
print('입니다')









