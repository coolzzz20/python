#지금 시각은? >>
#11시 이전이면 굿모닝
#17시 이전이면 굿애프터눈
#22시 이전이면 굿이브닝
#나머지는 굿나잇

import datetime
##time = int(input('지금 시각은?>>   '))
now = datetime.datetime.now() #파이썬파일.패키지.함수
print('현재는: ', now)
hour = now.hour
#자동으로 값의 범위가 앞에서부터 제한되어져 가는 것인가?
print('현재 시각은: ', hour, '시')
if hour <= 11 :
    print('굿모닝')
elif hour <= 17 :
    print('굿애프터눈')
elif hour <= 22 :
    print('굿이브닝')
else:
    print('굿나잇')
print('-------------------------------')
print('올해는' , now.year, '년')
print('현재 달은' , now.month, '월')
print('오늘은' , now.day, '일')

