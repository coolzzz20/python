import random
target = random.randint(1, 100) #1~100 중 하나를 생성
#randint(a,b)는 a부터 까지 사이의 값.
count = 0 #반복문 안에 넣으면 제 초기화가 일어나기 때문에 증가가 되지 않는다.
#초기화 변수는 반복문 안에 넣으면 안된다.
while True:
    count = count + 1
    think = int(input('생각한 값 입력>>>'))
    if think == target:
        print('정답입니다. 축하드립니다.')
        print('당신의 시도 회수:', count, '회')
        print('시스템을 종료합니다.')
        break
    # elif think > 77:
    #     print('정답이 아닙니다.정답이 더 작습니다.')
    # else:
    #     print('정답이 아닙니다. 정답이 더 큽니다.')
    #
    else:
        print('정답이 아닙니다.')
        if think > 77:
            print('정답보다 값이 큽니다.')
        if think <77:
            print('정답보다 값이 작습니다.')