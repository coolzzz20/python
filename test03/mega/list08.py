data = input('지금 먹고 싶은 것? 물, 아메리카노, 맥주>>>  ')
#조건은 4자기 물, 아메리카노,맥주 , 그리고 그외의 것

if data =='물':
    print('밖으로 나가서 정수기로 갑니다.')
#if가 나오면 무조건 조건을 써야한다.
elif data == '아메리카노':
    print('이디야 가서 사먹는다.')
elif data == '맥주':
    pass #입력한 값을 쓰기 싫을 때 pass이용
else:
    print('다시 제대로 입력해주세요.')

