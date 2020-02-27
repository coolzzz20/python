#정리된 음료수 자판기.

drink = ['사이다', '콜라', '17차', '옥수수차', '헛개차', '포카리스웨트']
price = [500, 600, 700, 800, 900, 1000]
num = [0, 0, 0, 0, 0, 0]
i = 0

print('1 : 사이다, 2 : 콜라, 3 : 17차, 4 : 옥수수차, 5 : 헛개차, 6: 포카리스웨트  종료는 -1입니다.')
print('7: 지금까지 음료수 선택 확인')

while True:
    print('--------------------------')
    choice = int(input("원하시는 음료의 번호를 선택해주세요. "))

    for x in range(0, len(drink)):
        print(x, end=' ')
    print('\n------------------------')

    for x in num:
        print(x, end=' ')
    print('\n--------------------')

    if choice == -1:
        print('프로그램을 종료합니다.')
        break

    else:
        if choice == 1:
            num[0] = num[0] + 1
            print('사이다를', str(num[0]) + '개', '선택하셨습니다.')
        if choice == 2:
            num[1] = num[1] + 1
            print('콜라를', str(num[1]) + '개', ' 선택하셨습니다.')
        if choice == 3:
            num[2] = num[2] + 1
            print('17차를', str(num[2]) + '개', ' 선택하셨습니다.')
        if choice == 4:
            num[3] = num[3] + 1
            print('옥수수차를', str(num[3]) + '개', ' 선택하셨습니다.')
        if choice == 5:
            num[4] = num[4] + 1
            print('헛개차를', str(num[4]) + '개', ' 선택하셨습니다.')
        if choice == 6:
            num[5] = num[5] + 1
            print('포카리스웨트를', str(num[5]) + '개', ' 선택하셨습니다.')
        if choice == 7:
            print('사이다', num[0], '콜라', num[1], '17차', num[2], '옥수수차', num[3], end='')
            print('헛개차', num[4], '포카리스웨트', num[5], '선택하셨습니다.')
        elif choice > 8 and choice < 0 and choice != -1:
            print('잘못된 입력입니다. 다시 선택해주세요.')

tal = num[0] * price[0] + num[1] * price[1] + num[2] * price[2] + num[3] * price[3] + num[4] * price[4] + num[5] * \
      price[5]
print('총 가격은', tal, '입니다.')
print(num)

while True:
    pay = int(input('현금은 1번, 카드는 2번을 눌러주세요.'))
    if pay == 1:
        while True:
            money = int(input('현금을 넣어주세요'))
            if money == tal:
                for x in range(0, 6):
                    if num[x] >= 1:
                        print(drink[x] + '를', str(num[x]) + '개,', end=' ')
                print('총', str(tal) + '금액만큼', end='')
                print(' 구매하셨습니다.')
                print('안녕히가세요')
                break
            elif money > tal:
                print('거스름 돈', money - tal, '반환되었습니다.')
                for x in range(0, 6):
                    if num[x] >= 1:
                        print(drink[x] + '를', str(num[x]) + '개,', end=' ')
                print('총', str(tal) + '금액만큼', end='')
                print(' 구매하셨습니다.')
                print('안녕히가세요')
                break
            elif money < 0:
                print('시스템오류. 시스템오류. 처음으로 돌아가시오.')


            else:
                print('금액이 부족합니다. 돈을 더 넣어주세요.')
                chu = int(input('추가 금액>>>>'))
                if money + chu == tal:
                    for x in range(0, 6):
                        if num[x] >= 1:
                            print(drink[x] + '를', str(num[x]) + '개,', end=' ')
                    print('총', str(tal) + '금액만큼', end='')
                    print(' 구매하셨습니다.')
                    print('조심히가요!')
                    break
                elif chu + money > tal:
                    print('거스름 돈', chu + money - tal, '반환되었습니다.' )
                    for x in range(0, 6):
                        if num[x] >= 1:
                            print(drink[x] + '를', str(num[x]) + '개,', end=' ')
                    print('총', str(tal) + '금액만큼', end='')
                    print(' 구매하셨습니다.')
                    print('안녕히 가세요.')
                    break
                elif chu + money < tal:
                    while True:
                        chu2 = int(input('추가 금액을 넣어주세요.'))
                        if tal - money - chu - i - chu2 == 0 :
                            for x in range(0, 6):
                                if num[x] >= 1:
                                    print(drink[x] + '를', str(num[x]) + '개,', end=' ')
                            print('총', str(tal) + '금액만큼', end='')
                            print(' 구매하셨습니다.')
                            print('안녕히 가세요.')
                            break
                        elif tal - money -chu - i -chu2 > 0 and chu2 != 0:
                            print('추가로 돈을 더 넣어주세요.')
                            i = chu2 + i
                        elif chu2 == 0:
                            print('거래를 종료합니다. 돈이 반환됩니다.')
                            break
                        else:
                            print(money + chu + i + chu2 - tal , '잔돈이 반환되었습니다.')
                            for x in range(0, 6):
                                if num[x] >= 1:
                                    print(drink[x] + '를', str(num[x]) + '개,', end=' ')
                            print('총', str(tal) + '금액만큼', end='')
                            print(' 구매하셨습니다.')
                            print('안녕히 가세요.')
                            break

                    break
        break
    elif pay == 2:
        card = int(input('화면의 보이는 것처럼 카드를 사용해주세요.(잔액입력)'))
        if card >= tal:
            for x in range(0, 6):
                if num[x] >= 1:
                    print(drink[x] + '를', str(num[x]) + '개,', end=' ')
            print('총', str(tal) + '금액만큼', end='')
            print(' 구매하셨습니다.')
            print('계산이 완료되었습니다. 안녕히가세요')
            break

        else:
            print('잔액이 부족합니다. 카드를 바꿔주세요.')
            print('카드변경 1번, 현금결제로 변경은2번')
            print('기술 한계로 여러 개의 카드로 나누어 계산 할 수 없습니다.')
            choice2 = int(input('번호 입력해주세요.'))
            while True:

                if choice2 == 1:
                    card2 = int(input('화면의 보이는 것처럼 카드를 사용해주세요.(잔액입력)'))
                    if card2 >= tal:
                        for x in range(0, 6):
                            if num[x] >= 1:
                                print(drink[x] + '를', str(num[x]) + '개,', end=' ')
                        print('총', str(tal) + '금액만큼', end='')
                        print(' 구매하셨습니다.')
                        print('계산이 완료되었습니다. 안녕히가세요')
                        break

                    else:
                        print('잔액이 부족한 카드입니다.')
                        print('카드를 바꿔주세요.')
                        print('현금으로 계산하시겠습니까?')
                        papa = input('카드 or 현금')
                        if papa == '현금':
                                print('프로그램을 종료 후 재시작 해주세요.')
                                break
                        else:
                                pass
                elif choice2 == 2:
                    print('프로그램을 종료 후 재시작 해주세요.')
                    break
            break
    else:
        print('다시 선택해주세요.')
        pass
if choice2 != 2 and papa != '현금':
    print('영수증')
    print('----------------------------------------')
    print()
    print()
    for x in range(0, 6):
        if num[x] >= 1:
            print(drink[x] + '를', str(num[x]) + '개,', end=' ')
    print('총', str(tal) + '금액만큼', end='')
    print(' 구매하셨습니다.')
    print()
    print()
    print('------------------------------------------')
else:
    print('프로그램이 재실행됩니다.')