### 조장님

menu = ["사이다", "콜라", "17차", "옥수수차", "헛개차", "포카리스웨트"]
price = [500, 500, 700, 700, 700, 800]
count = [0, 0, 0, 0, 0, 0]

while True:
    choice = input("원하는 메뉴 입력(종료:0): ")
    if int(choice) == 0:
        print("끝")
        break
    elif int(choice) not in menu:
        print("다시 입력해주세요")
    else:
        print("00","를 선택하셨습니다.")
