def info():
    name = input("같이 볼 사람 이름   ")
    rea = input("그 사람과 관계     ")
    print(name, "(와)과", rea , "사이입니다")

def pay():
    price = 10000
    num = input("영화 볼 인원을 입력하시오     ")
    num1 = int(num)
    tot = num1*price
    print("영화 총 비용은", tot , "입니다.")
