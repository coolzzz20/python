## 현정

drink = ["사이다", "콜라", "17차", "옥수수차", "헛개차", "포카리스웨트"]
price = [500, 600, 700, 800, 900, 1000]
count = [0] * 6

print("1: 사이다(500원)\n2: 콜라(600원)\n3: 17차(700원)")
print("4: 옥수수차(800원)\n5: 헛개차(900원)\n6: 포카리스웨트(1000원)")

while True:
    choice = int(input("\n원하는 음료 번호 입력(종료는 0): "))
    if choice not in range(0, 7):
        print("잘못 입력하셨습니다. 다시 입력해주세요")
    elif choice == 0:
        print("음료 선택을 종료합니다.")
        break
    else:
        count[choice-1] = count[choice-1] + 1
        print("선택한 음료: ", end=" ")
        for i in range(0,len(drink)):
            if count[i] >= 1:
                print(drink[i], count[i], "개", end=" ")
        print()