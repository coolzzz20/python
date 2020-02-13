# 1) 2월 전이면 아직은 조금 춥겠군요.
# 2월 이면 조금 있으면 봄이 오겠군요.
#  아니면 새해의 시작이 되겠군요.
import datetime
now = datetime.datetime.now()
weather = now.month

if weather < 2 :
    print('아직은 조금 춥겠군요')
elif weather == 2 :
    print('조금 있으면 봄이고겠군요. 아니면 새해의 시작이 되겠군요')
else:
    pass

# 2) 3~5월 까지는 봄 6~8월 까지는 여름 8~11월까지는 가울 나머지는 겨울
#month = now.month
if 3<= now.month <=5  :
    print('봄이군요')
elif 6 <= now.month <=8 :
    print('여름이군요')
elif 9<= now.month <= 11  :
    print('가을이군요')
else:
    print('겨울이군요')

# 3) 2월은 28일이나 29일까지입니다.
#    나머지 달은 30일인지, 31일인지 프린트


month = now.month
if(month == 4 or month ==6 or month ==9 or month ==11):
    print('30일 까지 입니다')
elif(month == 2):
    print('28일 또는 29일 까지 입니다')
else:
    print('31일까지입니다')


