# 입력: 홍길동
# 입력: 파이썬
# 입력: 프로그래머
# 입력: 데이터 분석가

# sum이라는 변수에 입력값 누적하여 sum을 프린트
# 0홍길동은 파이썬 프로그래머 데이터 분석가

ii = 0
ssum = ''  # 숫자가 아닐떈 ' ' 을 이용해서 +을 이용한다. 숫자끼리 더할 때는 0.
while ii < 4:
    ddata = input('입력')
    ssum = ssum + ddata
    ii = ii + 1

print(ssum)

# 무한 루프를 이용할 때 사용하는 것.
sum = ''
while True:
    data = input('입력(종료는 x):')
    # 입력된 값이 x인지를 먼저 체크해야함.
    if data == 'x' or data == 'X':
        print('반복문 종료를 완료합니다.')
        break  # 반복문을 종료한다! 라는 뜻
    sum = sum + data  # 누적 시키는 코드 형식

print(sum)
